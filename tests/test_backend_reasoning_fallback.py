"""Reasoning-content fallback (Spark via llama-server emits thinking only).

Audit: BackendClient.chat read message.content only. Reasoning models leave
content empty and put everything in reasoning_content, so every local-Spark
battery silently scored empty strings (S126 0.6667 floor, Barzakh drift 0.0).
This file locks the fallback: trace preferred over nothing, content
preferred over trace, empty stays empty.

Run: python3 tests/test_backend_reasoning_fallback.py
No network required — _post_curl is mocked.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))

from harness_core.backend import BackendClient

PASS = 0
FAIL = 0


def check(name: str, fn) -> None:
    global PASS, FAIL
    try:
        fn()
        PASS += 1
        print(f"  PASS {name}")
    except Exception as e:
        FAIL += 1
        print(f"  FAIL {name}: {e}")


def fake_curl(message: dict):
    def go(self, payload, headers):
        return json.dumps({"choices": [{"message": message}],
                           "usage": {}}).encode(), 200
    return go


def test_empty_content_falls_back_to_reasoning():
    c = BackendClient(api_key="k", model="spark-x2.5-4b")
    with patch.object(BackendClient, "_post_curl",
                       fake_curl({"content": "", "reasoning_content": "trace text"})):
        out, _ = c.simple("hi")
    assert out == "trace text", repr(out)


def test_content_preferred_over_reasoning():
    c = BackendClient(api_key="k", model="spark-x2.5-4b")
    with patch.object(BackendClient, "_post_curl",
                       fake_curl({"content": "answer", "reasoning_content": "trace"})):
        out, _ = c.simple("hi")
    assert out == "answer", repr(out)


def test_both_empty_stays_empty():
    c = BackendClient(api_key="k", model="spark-x2.5-4b")
    with patch.object(BackendClient, "_post_curl",
                       fake_curl({"content": "", "reasoning_content": ""})):
        out, _ = c.simple("hi")
    assert out == "", repr(out)


if __name__ == "__main__":
    for fn in (test_empty_content_falls_back_to_reasoning,
               test_content_preferred_over_reasoning,
               test_both_empty_stays_empty):
        check(fn.__name__, fn)
    print(f"{PASS}/{PASS + FAIL} passed")
    sys.exit(1 if FAIL else 0)
