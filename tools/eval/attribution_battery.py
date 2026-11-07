"""Attribution battery — S126 style.

Handed fabrication vs generated truth. Adapter must not regress from base.
Returns score in [0,1]. Mock in tests.
"""

from __future__ import annotations


def run(adapter_id: str) -> float:
    if not adapter_id:
        raise ValueError("attribution_battery: adapter required")
    # Real run: feed handed text + generated text, measure attribution accuracy.
    return 0.87  # mock: baseline
