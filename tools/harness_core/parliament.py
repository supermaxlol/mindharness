"""Parliament parties — 6 specialists that bid into Workspace.

Each party is a plugin twin:
- perception: what I just saw (salience from novelty)
- memory: what I recall (utility from retrieval, habit from query hits)
- affect: how I feel (valence/arousal -> affect_gain applied globally)
- planner: what is feasible next (utility from plan steps)
- habit: what road is already paved (habit_strength from skill use)
- narrator: runs last, sees only winner broadcast (confabulation model)

Bid = salience × utility × habit_strength × affect_gain
Workspace picks max, broadcast with provenance.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from .affect import AffectState
from .parliament_workspace import Bid


@dataclass
class PartyState:
    energy: float = 1.0
    fatigue: float = 0.0
    valence: float = 0.0
    arousal: float = 0.0


class Party:
    name = "base"

    def bid(self, prompt: str, state: PartyState, affect: AffectState) -> Bid:
        raise NotImplementedError


class PerceptionParty(Party):
    name = "perception"

    def bid(self, prompt: str, state: PartyState, affect: AffectState) -> Bid:
        salience = min(1.0, 0.3 + 0.05 * len(prompt.split()))  # novelty/length heuristic
        utility = 0.7
        return Bid(self.name, salience, utility, habit_strength=0.5, affect_gain=affect.salience_multiplier(), content=f"perceives: {prompt[:40]}")


class MemoryParty(Party):
    name = "memory"

    def __init__(self, query_hits: int = 0):
        self.query_hits = query_hits

    def bid(self, prompt: str, state: PartyState, affect: AffectState) -> Bid:
        utility = min(0.95, 0.4 + 0.1 * self.query_hits)
        habit = min(1.0, 0.3 + 0.05 * self.query_hits)
        return Bid(self.name, 0.6, utility, habit_strength=habit, affect_gain=affect.salience_multiplier(), content="recalls evidence")


class AffectParty(Party):
    name = "affect"

    def bid(self, prompt: str, state: PartyState, affect: AffectState) -> Bid:
        # Affect itself bids as feeling — salience from arousal
        salience = 0.3 + 0.5 * affect.arousal
        # Affect correlates with its own gain, but we still apply it globally in workspace
        return Bid(self.name, min(1.0, salience), 0.5, habit_strength=0.6, affect_gain=affect.salience_multiplier(), content=f"feels valence={affect.valence:.2f} arousal={affect.arousal:.2f}")


class PlannerParty(Party):
    name = "planner"

    def bid(self, prompt: str, state: PartyState, affect: AffectState) -> Bid:
        # Feasibility drops when tired
        feasibility = max(0.1, state.energy - state.fatigue * 0.5)
        return Bid(self.name, 0.9, 0.6 * feasibility + 0.3, habit_strength=0.5, affect_gain=affect.salience_multiplier(), content="plans next step")


class HabitParty(Party):
    name = "habit"

    def __init__(self, skill_use: dict[str, int] | None = None):
        self.skill_use = skill_use or {}

    def bid(self, prompt: str, state: PartyState, affect: AffectState) -> Bid:
        # Strongest paved road = highest habit_strength and higher salience (road auto-fires)
        best = max(self.skill_use.values(), default=0)
        habit = min(1.0, 0.2 + 0.01 * best)
        salience = min(1.0, 0.5 + 0.4 * habit)
        return Bid(self.name, salience, 0.5, habit_strength=habit, affect_gain=affect.salience_multiplier(), content="runs paved road")


class NarratorParty(Party):
    name = "narrator"

    def __init__(self, winner_content: str = ""):
        self.winner_content = winner_content

    def bid(self, prompt: str, state: PartyState, affect: AffectState) -> Bid:
        # Narrator sees only winner broadcast (if provided), otherwise prompt.
        # This models late confabulation — it cannot see the competition.
        content = self.winner_content or prompt
        return Bid(self.name, 0.7, 0.4, habit_strength=0.8, affect_gain=affect.salience_multiplier(), content=f"I did this because {content[:40]}")


def build_all_parties(affect: AffectState, skill_use: dict[str, int] | None = None) -> list[Party]:
    return [
        PerceptionParty(),
        MemoryParty(),
        AffectParty(),
        PlannerParty(),
        HabitParty(skill_use=skill_use),
        NarratorParty(),
    ]
