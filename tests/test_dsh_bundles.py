"""DSH bundle validation tests — host-independent bundle checks.

Run: /usr/local/bin/python3 tests/test_dsh_bundles.py   (plain runner, no pytest)
Requires pyyaml on the running interpreter.
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

PASS = 0
FAIL = 0

REPO = Path(__file__).resolve().parents[1]
VALIDATOR = REPO / "tools/validate_dsh_bundles.py"


def check(name: str, fn) -> None:
    global PASS, FAIL
    try:
        fn()
        PASS += 1
        print(f"  PASS {name}")
    except Exception as e:
        FAIL += 1
        print(f"  FAIL {name}: {e}")


def run_validator() -> dict:
    proc = subprocess.run(
        [sys.executable, str(VALIDATOR)], capture_output=True, text=True,
        timeout=60)
    assert proc.returncode == 0, f"exit {proc.returncode}: {proc.stderr[-500:]}"
    return json.loads(proc.stdout)


def test_no_errors() -> None:
    out = run_validator()
    assert out["errors"] == [], out["errors"]


def test_row_counts() -> None:
    out = run_validator()
    assert out["rows"] == 15, out["rows"]
    assert out["bundles"] == 3, out["bundles"]


def test_service_collisions_documented() -> None:
    out = run_validator()
    warns = "\n".join(out["warnings"])
    assert "ctx.provenance claimed by 2 rows" in warns, warns
    assert "ctx.embodied claimed by 2 rows" in warns, warns


def test_parliament_scaffold_flagged() -> None:
    out = run_validator()
    warns = "\n".join(out["warnings"])
    assert "aspirational" in warns, warns


if __name__ == "__main__":
    for fn in (test_no_errors, test_row_counts,
               test_service_collisions_documented,
               test_parliament_scaffold_flagged):
        check(fn.__name__, fn)
    print(f"{PASS}/{PASS + FAIL} passed")
    sys.exit(1 if FAIL else 0)
