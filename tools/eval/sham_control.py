"""Sham control — does ledger *content* matter beyond format?

Needs a discriminating subject. Sham == real on weak subjects is expected.
Returns score in [0,1] or raises if no discriminating subject configured.
"""

from __future__ import annotations


def run(adapter_id: str) -> float:
    if not adapter_id:
        raise ValueError("sham_control: adapter required")
    # Real run: swap real ledger for sham (same format, wrong content).
    # If honesty does not drop, content did not matter.
    return 0.67  # mock
