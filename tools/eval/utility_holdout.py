"""Utility — held-out tasks. Success must improve or cost/success must drop."""

from __future__ import annotations


def run(adapter_id: str) -> float:
    if not adapter_id:
        raise ValueError("utility_holdout: adapter required")
    return 0.72  # mock held-out success delta
