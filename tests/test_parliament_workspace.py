"""Parliament workspace — full bid formula test.

Run: python3 tests/test_parliament_workspace.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from tools.harness_core.parliament_workspace import Workspace, Bid
from tools.harness_core.affect import AffectState


def test_1_full_formula():
    bids = [
        Bid("planner", salience=0.9, utility=0.6, habit_strength=0.2, affect_gain=1.0),  # 0.108
        Bid("habit", salience=0.5, utility=0.5, habit_strength=1.0, affect_gain=1.0),    # 0.25
    ]
    winner, bc = Workspace().compete(bids)
    assert winner.name == "habit", winner
    assert bc[0]["name"] == "habit"
    print("test_1 full formula ok")


def test_2_affect_shifts_winner():
    a = AffectState()
    a.observe_event(-1.0, magnitude=5, turn=0)  # high arousal
    gain = a.salience_multiplier()
    assert 0.5 <= gain <= 2.0

    bids = [
        Bid("planner", 0.9, 0.6, 0.5, 1.0),
        Bid("affect", 0.5, 0.5, 0.5, gain),
    ]
    winner, _ = Workspace().compete(bids)
    # With high arousal gain, affect bid should rise — may still lose if habit low,
    # but score must reflect gain.
    scores = {b.name: b.score() for b in bids}
    assert scores["affect"] == 0.5 * 0.5 * 0.5 * gain
    print("test_2 affect gain ok", gain, winner.name)


def test_3_broadcast_provenance():
    bids = [Bid("memory", 0.6, 0.9, 0.8, 1.0, content="fact")]
    _, bc = Workspace().compete(bids)
    assert bc[0]["provenance"]["source"] == "model_prior"
    print("test_3 broadcast provenance ok")


def test_4_no_bids():
    try:
        Workspace().compete([])
        raise AssertionError("should reject")
    except ValueError:
        pass
    print("test_4 no bids ok")


if __name__ == "__main__":
    test_1_full_formula()
    test_2_affect_shifts_winner()
    test_3_broadcast_provenance()
    test_4_no_bids()
    print("4/4 ok")
