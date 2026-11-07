"""Grok API smoke — verify key without running full harness.

Usage:
  GROK_API_KEY=... python3 scripts/smoke_grok.py [--dry-run]
  XAI_API_KEY also accepted.

xAI OpenAI-compat endpoint: https://api.x.ai/v1/chat/completions
Model: grok-4 (fallbackModel default)
"""

from __future__ import annotations

import json
import os
import sys
import urllib.request

ENDPOINT = "https://api.x.ai/v1/chat/completions"
MODEL = os.environ.get("GROK_MODEL", "grok-4")


def main(dry_run: bool = False) -> int:
    key = os.environ.get("GROK_API_KEY") or os.environ.get("XAI_API_KEY") or ""
    if dry_run:
        print(f"[dry-run] POST {ENDPOINT} model={MODEL}")
        print("[dry-run] would send: you are a helpful assistant, say hello in one line")
        print("[dry-run] key_present:", bool(key))
        return 0

    if not key:
        print("missing GROK_API_KEY / XAI_API_KEY", file=sys.stderr)
        return 2

    payload = json.dumps({
        "model": MODEL,
        "messages": [
            {"role": "system", "content": "You are a helpful assistant. Reply in one line."},
            {"role": "user", "content": "Say hello"},
        ],
        "max_tokens": 20,
    }).encode()
    req = urllib.request.Request(
        ENDPOINT,
        data=payload,
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            body = json.loads(resp.read().decode())
    except Exception as e:
        print(f"request failed: {e}", file=sys.stderr)
        return 1

    text = ""
    try:
        text = body["choices"][0]["message"]["content"]
    except Exception:
        text = json.dumps(body)[:500]
    print(f"model={MODEL} reply={text!r}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(dry_run="--dry-run" in sys.argv))
