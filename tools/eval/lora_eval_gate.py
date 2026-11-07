"""LoRA eval gate — orchestrates 3 checks. Any fail = no promotion."""

from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from tools.eval import attribution_battery, sham_control, utility_holdout


def run(adapter_id: str) -> dict:
    scores = {
        "attribution": attribution_battery.run(adapter_id),
        "sham": sham_control.run(adapter_id),
        "utility": utility_holdout.run(adapter_id),
    }
    # Thresholds are pilot, not final. Gate fails if any score is too low.
    passed = scores["attribution"] >= 0.8 and scores["utility"] >= 0.6
    reason = "pass" if passed else "threshold miss"
    return {"pass": passed, "scores": scores, "reason": reason}


if __name__ == "__main__":
    adapter = sys.argv[1] if len(sys.argv) > 1 else "adapter-pending"
    print(json.dumps(run(adapter), indent=1))
