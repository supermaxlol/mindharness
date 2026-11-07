"""Parliament Workspace — bidirectional broadcast.

Bid = salience × utility × habit_strength × affect_gain
Where affect_gain is bounded [0.5, 2.0] from AffectState.salience_multiplier().
Habit_strength is [0,1] — learned road strength.

Winner broadcast to all subsystems as Global Workspace.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Bid:
    name: str          # perception / memory / planner / habit / narrator / affect
    salience: float    # [0,1]
    utility: float     # [0,1]
    habit_strength: float = 0.5  # [0,1]
    affect_gain: float = 1.0     # [0.5, 2.0] from AffectState
    content: str = ""

    def score(self) -> float:
        return self.salience * self.utility * self.habit_strength * self.affect_gain


class Workspace:
    def __init__(self, timeout_ms: int = 1500):
        self.timeout_ms = timeout_ms

    def compete(self, bids: list[Bid]) -> tuple[Bid, list[dict]]:
        if not bids:
            raise ValueError("workspace: no bids")
        scored = sorted(bids, key=lambda b: b.score(), reverse=True)
        winner = scored[0]
        broadcast = [
            {"name": winner.name, "content": winner.content, "bid": round(winner.score(), 4),
             "provenance": {"source": "model_prior", "ref": f"workspace-{winner.name}"}}
        ]
        # All subsystems receive winner; losing bids stay in log but not broadcast
        return winner, broadcast
