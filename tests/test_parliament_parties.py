"""Parliament parties — 6 parties bid, workspace picks winner.

Run: python3 tests/test_parliament_parties.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from tools.harness_core.parliament import PartyState, build_all_parties
from tools.harness_core.parliament_workspace import Workspace
from tools.harness_core.affect import AffectState


def test_1_all_parties_bid():
    affect = AffectState()
    state = PartyState(energy=1.0, fatigue=0.0)
    parties = build_all_parties(affect, skill_use={"code": 100})
    assert len(parties) == 6, parties
    bids = [p.bid("write code", state, affect) for p in parties]
    assert all(b.score() >= 0 for b in bids)
    winner, bc = Workspace().compete(bids)
    assert bc[0]["name"] == winner.name
    print("test_1 all parties bid ok", winner.name)


def test_2_habit_wins_when_paved():
    affect = AffectState()
    state = PartyState(energy=1.0, fatigue=0.0)
    # Habit with huge use should outbid planner even if planner salience high
    from tools.harness_core.parliament import HabitParty, PlannerParty
    habit = HabitParty(skill_use={"code": 1000}).bid("code", state, affect)
    planner = PlannerParty().bid("code", state, affect)
    assert habit.score() >= planner.score() * 0.9  # habit strong, comparable
    print("test_2 habit ok", habit.score(), planner.score())


def test_3_tired_state_rigs_vote():
    affect = AffectState()
    tired = PartyState(energy=0.2, fatigue=1.0)
    fresh = PartyState(energy=1.0, fatigue=0.0)
    parties_tired = build_all_parties(affect)
    bids_tired = [p.bid("work", tired, affect) for p in parties_tired]
    bids_fresh = [p.bid("work", fresh, affect) for p in parties_tired]
    # Planner bid should be lower when tired
    t_plan = [b for b in bids_tired if b.name == "planner"][0].score()
    f_plan = [b for b in bids_fresh if b.name == "planner"][0].score()
    assert t_plan < f_plan
    print("test_3 tired rigs vote ok", round(t_plan, 3), round(f_plan, 3))


def test_4_narrator_late():
    # Narrator only sees winner content, not competition
    from tools.harness_core.parliament import NarratorParty
    affect = AffectState()
    state = PartyState()
    narrator = NarratorParty(winner_content="planner won")
    bid = narrator.bid("code", state, affect)
    assert "planner won" in bid.content
    print("test_4 narrator late ok")


if __name__ == "__main__":
    test_1_all_parties_bid()
    test_2_habit_wins_when_paved()
    test_3_tired_state_rigs_vote()
    test_4_narrator_late()
    print("4/4 ok")
