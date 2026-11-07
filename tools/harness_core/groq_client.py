"""Groq API client with automated key loading and rotation.

Auto-load order (first wins for each var, all deduped):
1. Process env: LLM_API_KEY, LLM_API_KEY_2, LLM_API_KEY_3, GROQ_API_KEY
2. Disk files (searched for gsk_ pattern, never printed):
   - config/.secrets/groq_keys.env
   - .env (repo root)
   - ~/Desktop/neural-shadow/.secrets/keys.env
   - ~/Desktop/llmsimulate/.env

Rotation: on 429/403, tries next key. Sets User-Agent to bypass Cloudflare 1010.
Base URL: LLM_BASE_URL or https://api.groq.com/openai/v1
Model: LLM_MODEL_NAME or GROQ_MODEL or openai/gpt-oss-120b
"""

from __future__ import annotations

import json
import os
import re
import urllib.request
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
DEFAULT_BASE = "https://api.groq.com/openai/v1"
DEFAULT_MODEL = "openai/gpt-oss-120b"

SIZE_LIMIT_BYTES = 200_000

def _parse_env_file(path: Path) -> list[str]:
    try:
        if not path.exists() or not path.is_file():
            return []
        text = path.read_text(errors="ignore")
        # Find all gsk_... tokens
        return re.findall(r"gsk_[A-Za-z0-9_\-]{32,}", text)
    except Exception:
        return []

def load_keys() -> list[str]:
    keys: list[str] = []
    # 1. Env vars
    for name in ("LLM_API_KEY", "GROQ_API_KEY", "LLM_API_KEY_2", "LLM_API_KEY_3"):
        v = os.environ.get(name, "").strip()
        if v:
            keys.append(v)
    # 2. Disk files
    candidates = [
        REPO / "config" / ".secrets" / "groq_keys.env",
        REPO / ".env",
        Path.home() / "Desktop" / "neural-shadow" / ".secrets" / "keys.env",
        Path.home() / "Desktop" / "llmsimulate" / ".env",
        Path.home() / "Desktop" / "neural-shadow" / ".env",
    ]
    for p in candidates:
        keys.extend(_parse_env_file(p))
    # dedupe preserve order
    seen, out = set(), []
    for k in keys:
        if k not in seen:
            seen.add(k)
            out.append(k)
    return out

def get_base_url() -> str:
    return os.environ.get("LLM_BASE_URL", DEFAULT_BASE).rstrip("/")

def get_model() -> str:
    return os.environ.get("LLM_MODEL_NAME") or os.environ.get("GROQ_MODEL") or DEFAULT_MODEL

class GroqClient:
    def __init__(self, base_url: str | None = None, model: str | None = None, keys: list[str] | None = None):
        self.base = (base_url or get_base_url()).rstrip("/")
        self.endpoint = self.base + "/chat/completions"
        self.model = model or get_model()
        self.keys = keys if keys is not None else load_keys()

    def have_keys(self) -> bool:
        return bool(self.keys)

    def chat(self, system: str, user: str, max_tokens: int = 50) -> str:
        if not self.keys:
            raise ValueError("groq_client: no keys found — set LLM_API_KEY or place keys on disk (see module doc)")
        payload = json.dumps({
            "model": self.model,
            "messages": [
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
            "max_tokens": max_tokens,
        }).encode()
        last_err: Exception | None = None
        for idx, key in enumerate(self.keys):
            req = urllib.request.Request(
                self.endpoint,
                data=payload,
                headers={
                    "Authorization": f"Bearer {key}",
                    "Content-Type": "application/json",
                    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
                },
                method="POST",
            )
            try:
                with urllib.request.urlopen(req, timeout=30) as resp:
                    body = json.loads(resp.read().decode())
                return body["choices"][0]["message"]["content"]
            except Exception as e:
                last_err = e
                code = getattr(e, "code", None)
                # rotate on limit / forbidden / auth
                if code in (429, 403, 401) and idx + 1 < len(self.keys):
                    continue
                raise
        raise last_err if last_err else RuntimeError("groq_client: all keys failed")
