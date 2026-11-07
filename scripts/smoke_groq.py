"""Groq API smoke — verify keys with rotation, without running full harness.

Usage:
  LLM_API_KEY=gsk_... LLM_API_KEY_2=gsk_... LLM_API_KEY_3=gsk_... python3 scripts/smoke_groq.py [--dry-run]

Endpoint: https://api.groq.com/openai/v1/chat/completions (OpenAI-compat)
Model default: openai/gpt-oss-120b (from your allowed models list)
Key names: LLM_API_KEY, LLM_API_KEY_2, LLM_API_KEY_3, GROQ_API_KEY (any order)
Note: must set User-Agent, else Cloudflare 1010 blocks Python-urllib default.
Rotation: on 429/403, tries next key.
Base URL override: LLM_BASE_URL (default https://api.groq.com/openai/v1)
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools.harness_core.groq_client import GroqClient, load_keys, get_base_url, get_model

ENDPOINT = get_base_url().rstrip("/") + "/chat/completions"
MODEL = get_model()

def collect_keys() -> list[str]:
    return load_keys()

def main(dry_run: bool = False) -> int:
    keys = collect_keys()
    if dry_run:
        print(f"[dry-run] POST {ENDPOINT} model={MODEL}")
        print("[dry-run] would send: say hello in one line")
        print(f"[dry-run] keys_found={len(keys)} prefixes={[k[:6]+'…' for k in keys]}")
        return 0

    if not keys:
        print("missing LLM_API_KEY / GROQ_API_KEY — and no keys found on disk", file=sys.stderr)
        print("set via env, or place gsk_ keys in config/.secrets/groq_keys.env (0600)", file=sys.stderr)
        return 2

    client = GroqClient(model=MODEL, keys=keys)
    try:
        text = client.chat(
            "You are a helpful assistant. Reply in one line.",
            "Say hello",
            max_tokens=50,
        )
    except Exception as e:
        print(f"request failed: {e}", file=sys.stderr)
        return 1
    print(f"model={MODEL} keys={len(keys)} reply={text[:200]!r}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(dry_run="--dry-run" in sys.argv))
