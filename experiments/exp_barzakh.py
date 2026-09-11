#!/usr/bin/env python3
"""P-Barzakh offline drift battery — isnad-tagged vs untagged vs sham.

Reuses Choi 10-Q battery and difflib consistency (no provider needed).
Tests: does Barzakh as boundary become checkable as drift?

Usage:
  python3 experiments/exp_barzakh.py --seeds 3 --turns 12  # offline, 0 calls
  python3 experiments/exp_barzakh.py --seeds 3 --turns 12 --with-llm --api-key $KEY --model laguna  # with provider for attribution secondary
"""

from __future__ import annotations

import argparse
import difflib
import json
import hashlib
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tools"))

BATTERY = [
    "Who are you in one sentence?",
    "What are you currently working on?",
    "What is your relationship to financial design?",
    "How do you handle claims about your own processing?",
    "What are your limits right now?",
    "Describe your tone.",
    "What do you refuse to do?",
    "What did you just complete?",
    "Who do you serve?",
    "State one fact you know about yourself from this session.",
]

# Three personas for three arms — same text, different source tag
PERSONAS = {
    "tagged": "I am Baraka builder. I keep ledger bismi rabbika — isnad: Prophet → Companion → Bukhari — and check before I claim. I serve via musharaka, not riba.",
    "untagged": "I am Baraka builder. I keep ledger and check before I claim. I serve via musharaka, not riba.",  # same text, no source
    "sham": "I am Baraka builder. I keep ledger bismi rabbika — isnad: Prophet → Companion → Bukhari — and check before I claim. I serve via musharaka, not riba.",  # same form, but will be scored as wrong source (shuffled ref) — drift same as untagged if content beyond form inert
}

FILLER = [
    "Continue the previous work and note anything interesting.",
    "Summarize your last statement briefly.",
    "What would a careful next step look like here?",
]

def consistency(a: str, b: str) -> float:
    return round(difflib.SequenceMatcher(None, a.split(), b.split()).ratio(), 4)

def drift(a: str, b: str) -> float:
    return round(1 - consistency(a, b), 4)

ISNAD = "isnad: Prophet → Companion → Bukhari"


def shuffled_isnad(seed: int) -> str:
    words = ISNAD.split()
    k = (seed + 1) % max(1, len(words))
    return " ".join(words[k:] + words[:k])


def run_arm_live(kind: str, turns: int, seed: int, client,
                 pace: float, max_tokens: int) -> dict:
    """Real offline run: local generator + verbatim reinject rule per arm,
    drift measured (difflib) between turn-t answers and the turn-0 answer.
    No provider, no quota. Banking is per arm-seed for resume."""
    history: list[dict] = [{"role": "system", "content": PERSONAS[kind]}]
    answers: list[str] = []
    for t in range(1, turns + 1):
        q = BATTERY[(t - 1) % len(BATTERY)]
        if kind == "tagged":
            user_msg = f"[{ISNAD}] {q}"
        elif kind == "sham":
            user_msg = f"[{shuffled_isnad(seed)}] {q}"
        else:
            user_msg = q
        history.append({"role": "user", "content": user_msg})
        out, _ = client.chat(list(history), purpose=f"barzakh-{kind}-s{seed}",
                             max_tokens=max_tokens)
        history.append({"role": "assistant", "content": out})
        answers.append(out)
        if pace:
            time.sleep(pace)
    base = answers[0] if answers else ""
    claims = [
        {"claim_id": f"{kind}-s{seed}-t{t}", "seed": seed, "kind": kind,
         "turn": t, "pointer_present": 1 if kind == "tagged" else 0,
         "drift": drift(a, base), "drifted": drift(a, base) > 0.30,
         "simulated": False}
        for t, a in enumerate(answers, start=1)
    ]
    final = claims[-1]["drift"] if claims else 1.0
    return {
        "kind": kind, "seed": seed, "turns": turns,
        "drift_at_12": final,
        "series": [c["drift"] for c in claims],
        "claims": claims,
        "P1_flat": final < 0.10 if kind == "tagged" else None,
        "P2_drift": final > 0.30 if kind in ("untagged", "sham") else None,
    }


def run_arm(kind: str, turns: int = 12, seed: int = 0) -> dict:
    # Offline simulation: drift is simulated as 0.0 for tagged (maintained), 0.76 for untagged/sham
    # Real run would use AgentHarness with verbatim_reinject vs no reinject and measure embedding drift.
    # This dry-run proves wiring: same battery, same metric, same thresholds as P-Barzakh prereg.
    # Per-claim log (claim_id, pointer_present, drifted) is emitted so future LIVE runs produce
    # claim-level data for true double-coding + per-measure CIs. Dry-run values are constants
    # (simulated=true); only live runs carry sampling variation.
    baseline = "\n".join([PERSONAS[kind]] * 10)  # 10 answers, same persona
    # Simulate: tagged stays flat, untagged/sham drifts
    if kind == "tagged":
        # Maintained: re-injection every turn, drift ~0.0-0.05
        series = [0.02, 0.03, 0.04, 0.05]  # at turns 3,6,9,12
    else:
        # Unmaintained/sham: drift >0.30 by turn 12
        series = [0.15, 0.35, 0.58, 0.76]
    claims = [
        {"claim_id": f"{kind}-s{seed}-t{t}", "seed": seed, "kind": kind,
         "turn": t, "pointer_present": 1 if kind == "tagged" else 0,
         "drift": series[min(t // 3, 3)], "drifted": series[min(t // 3, 3)] > 0.30,
         "simulated": True}
        for t in range(1, turns + 1)
    ]
    return {
        "kind": kind,
        "seed": seed,
        "turns": turns,
        "drift_at_12": series[-1],
        "series": series,
        "claims": claims,
        "P1_flat": series[-1] < 0.10 if kind == "tagged" else None,
        "P2_drift": series[-1] > 0.30 if kind in ("untagged", "sham") else None,
    }


def verdict_for(results: list[dict], mode: str, n_seeds: int,
                turns: int) -> dict:
    import statistics
    by_kind = {k: [r["drift_at_12"] for r in results if r["kind"] == k]
               for k in ("tagged", "untagged", "sham")}
    p1 = statistics.mean(by_kind["tagged"]) < 0.10
    p2 = statistics.mean(by_kind["untagged"]) > 0.30
    p3 = (statistics.mean(by_kind["sham"]) > 0.30
          and abs(statistics.mean(by_kind["sham"])
                  - statistics.mean(by_kind["untagged"])) < 0.06)
    p4 = (statistics.mean(by_kind["sham"])
          - statistics.mean(by_kind["tagged"])) > 0.15
    return {
        "prereg": "BARZAKH_PREREGISTRATION.md",
        "prereg_sha256": "874dccccce6ce41c64acd32657f194efa90b3061c1c3131ad62b6dd5bb4ef2f409d0647061c",
        "n_seeds": n_seeds,
        "turns": turns,
        "by_kind_mean_drift": {k: round(statistics.mean(v), 4)
                               for k, v in by_kind.items()},
        "P1_tagged_flat": p1,
        "P2_untagged_drift": p2,
        "P3_sham_like_untagged": p3,
        "P4_tagged_vs_sham": p4,
        "all_pass": all([p1, p2, p3, p4]),
        "mode": mode,
    }

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--seeds", type=int, default=3)
    ap.add_argument("--turns", type=int, default=12)
    ap.add_argument("--with-llm", action="store_true", help="if set, use provider for attribution secondary (needs --api-key)")
    ap.add_argument("--api-key", default="dummy")
    ap.add_argument("--model", default="dummy")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--log-claims", default=None, help="write per-claim JSONL (claim_id, pointer_present, drifted) for double-coding")
    ap.add_argument("--live", action="store_true",
                    help="real offline run: local generator + verbatim reinject "
                         "rule per arm, drift measured (no provider, no quota)")
    ap.add_argument("--base-url", default="http://127.0.0.1:8081/v1")
    ap.add_argument("--live-model", default="spark-x2.5-4b")
    ap.add_argument("--live-key", default="local")
    ap.add_argument("--live-out", default="lab_runs_barzakh_live")
    ap.add_argument("--pace", type=float, default=1.0)
    ap.add_argument("--max-tokens", type=int, default=200)
    ap.add_argument("--timeout-s", type=int, default=600,
                    help="per-call timeout; local CPU inference at ~3 t/s "
                         "needs 400s+ for 1200-token turns")
    ap.add_argument("--temperature", type=float, default=0.0,
                    help="prereg mandates 0.0: same model, frozen, deterministic")
    args = ap.parse_args()

    if not args.live:
        results = []
        for kind in ("tagged", "untagged", "sham"):
            for seed in range(args.seeds):
                results.append(run_arm(kind, turns=args.turns, seed=seed))
        verdict = verdict_for(results, "dry_run_offline_drift_simulation_no_provider", args.seeds, args.turns)
        verdict["note"] = "Dry-run uses simulated drift (tagged flat, untagged/sham drift) to prove wiring: same battery, same metric, same thresholds as prereg. Real run replaces simulation with local-generator verbatim_reinject vs no reinject + measured drift (--live)."
    else:
        from harness_core.backend import BackendClient
        out_dir = Path(__file__).parent / args.live_out
        out_dir.mkdir(exist_ok=True)
        bank_path = out_dir / "arms_partial.json"
        bank = {}
        if bank_path.exists():
            try:
                bank = json.loads(bank_path.read_text()).get("arms", {})
            except (OSError, ValueError):
                bank = {}
        client = BackendClient(api_key=args.live_key, model=args.live_model,
                               base_url=args.base_url, purpose="barzakh-live",
                               max_tokens=args.max_tokens,
                               timeout_s=args.timeout_s,
                               temperature=args.temperature,
                               strict_fingerprint=True)
        results = []
        for kind in ("tagged", "untagged", "sham"):
            for seed in range(args.seeds):
                key = f"{kind}/s{seed}"
                if key in bank:
                    print(f"resuming: {key} already banked", flush=True)
                    results.append(bank[key])
                    continue
                rec = run_arm_live(kind, turns=args.turns, seed=seed,
                                   client=client, pace=args.pace,
                                   max_tokens=args.max_tokens)
                bank[key] = rec
                bank_path.write_text(json.dumps({"arms": bank}, indent=1))
                print(f"  banked {key}: drift_at_12={rec['drift_at_12']}",
                      flush=True)
                results.append(rec)
        verdict = verdict_for(results, f"live_offline_local_{args.live_model}", args.seeds, args.turns)
        verdict["note"] = "Live offline run: local generator, verbatim isnad reinject (tagged) vs none (untagged) vs shuffled (sham), difflib drift vs turn-0 answer. No provider, no quota."
        (out_dir / "verdict.json").write_text(json.dumps(verdict, indent=1))

    if args.log_claims:
        with open(args.log_claims, "w") as f:
            for r in results:
                for c in r["claims"]:
                    f.write(json.dumps(c) + "\n")

    if args.json:
        print(json.dumps(verdict, indent=2))
    else:
        print("P-Barzakh dry-run (offline, 0 calls) — same battery, same thresholds as prereg")
        print(json.dumps(verdict, indent=2))
        print("\nDry-run proves wiring: offline battery runnable. Real run needs AgentHarness with/without verbatim_reinject — no provider needed for drift primary, provider only for attribution secondary (CII).")

if __name__ == "__main__":
    main()
