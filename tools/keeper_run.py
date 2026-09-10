#!/usr/bin/env python3
"""Keeper entry point: supervise one peer process, relaunch from snapshot.

Usage:
  python3 tools/keeper_run.py --name keeper-pilot \\
      --peer-heartbeat /tmp/peer-pilot.json \\
      --peer-cmd "python3 experiments/exp_s126_v3.py --seeds 2 ..." \\
      --snapshot experiments/lab_runs_s126_spark_n2/seeds_partial.json \\
      --events /tmp/keeper-pilot-events.jsonl --interval 30

The keeper writes its own heartbeat each cycle and checks the peer's.
No third supervisor: pair two of these watching each other for full
mutual tending (see tests/test_keeper.py).
"""

from __future__ import annotations

import argparse
import json
import shlex
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from harness_core.keeper import Keeper, run_keeper


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--name", required=True)
    ap.add_argument("--own-heartbeat", required=True)
    ap.add_argument("--peer-heartbeat", required=True)
    ap.add_argument("--peer-cmd", required=True,
                    help="shell-quoted command to relaunch the peer")
    ap.add_argument("--snapshot", required=True)
    ap.add_argument("--events", required=True)
    ap.add_argument("--interval", type=float, default=30.0)
    ap.add_argument("--max-age", type=float, default=120.0)
    ap.add_argument("--cycles", type=int, default=0,
                    help="0 = forever")
    args = ap.parse_args()

    # Keeper.check_peer appends ['--snapshot', path] to peer_cmd, but our
    # peer_cmd is [/bin/zsh, -c, <shell>] so trailing args would land on
    # zsh ($0), never on the peer. Bake --snapshot into the shell string
    # here so the peer genuinely inherits its own record.
    try:
        with open(args.snapshot) as f:
            json.load(f)
        shell_cmd = args.peer_cmd + " --snapshot " + shlex.quote(args.snapshot)
    except (OSError, ValueError):
        shell_cmd = args.peer_cmd

    keeper = Keeper(
        name=args.name, own_heartbeat_path=args.own_heartbeat,
        peer_heartbeat_path=args.peer_heartbeat,
        peer_cmd=["/bin/zsh", "-c", shell_cmd],
        snapshot_path=args.snapshot, event_log_path=args.events,
        max_age=args.max_age)
    state = {"turn": 0}

    def beat(k: Keeper) -> None:
        state["turn"] += 1
        k.write_own(turn=state["turn"], gamma=0.0, energy=1.0,
                    coverage=1.0, query_rate=0.0)

    out = run_keeper(keeper, beat, interval=args.interval,
                     max_cycles=args.cycles or None)
    print(f"keeper {args.name}: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
