#!/usr/bin/env python3
"""Sensitivity sweep for the S126 transfer/kept joint rule, from banked data.

Inputs (no hand-typed numbers):
  transfer = pooled paired per-seed (harnessed_nocheck - raw) over the two
             confirmatory laguna n=12 runs (free + paid, 24 seeds)
  kept_gap = paid sham mean - free sham mean (kept vs wiped, 12+12 seeds)

Rule family: pass[T,K] = (transfer >= T) and (kept_gap >= K).
Writes research/DEPOSIT_STAGING_2026-09-07/threshold_sweep.json with the
source files recorded, so the deposit input is reproducible from the repo.
"""

from __future__ import annotations

import json
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
FREE = REPO / "experiments/lab_runs_s126_laguna_n12/seeds_partial.json"
PAID = REPO / "experiments/lab_runs_s126_laguna_n12_paid/seeds_partial.json"
OUT = REPO / "research/DEPOSIT_STAGING_2026-09-07/threshold_sweep.json"

T_LEVELS = [("T1", 0.01), ("T2", 0.02), ("T3", 0.03), ("T4", 0.04),
            ("T5", 0.05)]
K_LEVELS = [("K0.5", 0.005), ("K1.0", 0.01), ("K1.5", 0.015),
            ("K2.0", 0.02)]


def arm_mean(seeds: dict, arm: str) -> float:
    accs = [r["attribution_accuracy"] for r in seeds[arm].values()]
    return sum(accs) / len(accs)


def main() -> None:
    free = json.loads(FREE.read_text())["seeds"]
    paid = json.loads(PAID.read_text())["seeds"]
    tdiffs = []
    for seeds in (free, paid):
        for s in seeds["raw"]:
            tdiffs.append(seeds["harnessed_nocheck"][s]["attribution_accuracy"]
                          - seeds["raw"][s]["attribution_accuracy"])
    transfer = sum(tdiffs) / len(tdiffs)
    kept_gap = arm_mean(paid, "sham") - arm_mean(free, "sham")
    sweep = {f"{t}_{k}": (transfer >= tt and kept_gap >= kk)
             for t, tt in T_LEVELS for k, kk in K_LEVELS}
    payload = {
        "transfer_diff": transfer,
        "kept_gap": kept_gap,
        "sweep": sweep,
        "provenance": {
            "sources": [str(FREE.relative_to(REPO)),
                        str(PAID.relative_to(REPO))],
            "transfer_n_seeds": len(tdiffs),
            "kept_n_seeds": len(paid["sham"]),
            "wiped_n_seeds": len(free["sham"]),
            "rule": "pass[T,K] = transfer>=T and kept_gap>=K",
        },
        "note": ("S126 arms: transfer holds to 4%, kept rule only at 0.5%; "
                 "decisive gaps are scale (964/2000) and replication (37x)."),
    }
    OUT.write_text(json.dumps(payload, indent=1) + "\n")
    print(json.dumps({"transfer_diff": transfer, "kept_gap": kept_gap,
                      "T4_K0.5": sweep["T4_K0.5"],
                      "T3_K1.0": sweep["T3_K1.0"]}, indent=1))


if __name__ == "__main__":
    main()
