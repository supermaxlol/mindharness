"""Town wallet — Python mirror for offline tests.

Master key never here. Session key only. Whitelist enforced.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Wallet:
    town_contract: str
    daily_limit: int = 100
    per_action_limit: int = 10
    balance: float = 0.0
    spent_today: float = 0.0
    log: list = field(default_factory=list)

    def __post_init__(self):
        if not self.town_contract:
            raise ValueError("skin_house: town_contract required")

    def earn(self, amount: float, source: str) -> dict:
        self.balance += amount
        entry = {"to": "self", "amount": amount, "source": source}
        self.log.append(entry)
        return entry

    def pay_rent(self, amount: float, seconds: int, source: str) -> dict:
        if amount > self.per_action_limit:
            raise ValueError("skin_house: per-action limit")
        if self.spent_today + amount > self.daily_limit:
            raise ValueError("skin_house: daily limit")
        if amount > self.balance:
            raise ValueError("skin_house: insufficient balance")
        self.balance -= amount
        self.spent_today += amount
        entry = {"to": self.town_contract, "amount": amount, "seconds": seconds, "source": source}
        self.log.append(entry)
        return entry

    def spend_log(self) -> list:
        return list(self.log)


def guard_decision(earnings: float, spend: float, turns_below_floor: int, floor: float) -> str:
    if turns_below_floor >= 5:
        return "dissolve"
    if earnings < spend:
        return "cheap-mode"
    if earnings - spend < floor:
        return "shrink"
    return "ok"
