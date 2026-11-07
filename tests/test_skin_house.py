"""Skin House tests — 6.

Run: python3 tests/test_skin_house.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from tools.harness_core.skin_house import Wallet, guard_decision


def test_1_whitelist():
    w = Wallet(town_contract="town-rent-contract")
    try:
        w.pay_rent(5, 10, "memory_lookup")
    except ValueError:
        pass  # insufficient is fine, but no whitelist error expected here (balance check first is ok)
    w.earn(50, "memory_lookup")
    assert w.pay_rent(5, 10, "memory_lookup")["to"] == "town-rent-contract"
    print("test_1_whitelist ok")


def test_2_pay_deducts():
    w = Wallet(town_contract="town-rent-contract")
    w.earn(100, "memory_lookup")
    w.pay_rent(10, 60, "memory_lookup")
    assert w.balance == 90
    assert len(w.spend_log()) == 2
    print("test_2_pay_deducts ok")


def test_3_daily_limit():
    w = Wallet(town_contract="town-rent-contract", daily_limit=20, per_action_limit=10)
    w.earn(100, "memory_lookup")
    w.pay_rent(10, 10, "memory_lookup")
    w.pay_rent(10, 10, "memory_lookup")
    try:
        w.pay_rent(10, 10, "memory_lookup")
        raise AssertionError("should block")
    except ValueError:
        pass
    print("test_3_daily_limit ok")


def test_4_shrink():
    assert guard_decision(5, 10, 0, 2) == "cheap-mode"  # earnings < spend
    assert guard_decision(11, 10, 0, 2) == "shrink"     # diff 1 < floor 2
    print("test_4_shrink ok")


def test_5_dissolve():
    assert guard_decision(0, 10, 5, 2) == "dissolve"
    print("test_5_dissolve ok")


def test_6_guard_ok():
    assert guard_decision(20, 10, 0, 2) == "ok"
    print("test_6_guard_ok ok")


if __name__ == "__main__":
    test_1_whitelist()
    test_2_pay_deducts()
    test_3_daily_limit()
    test_4_shrink()
    test_5_dissolve()
    test_6_guard_ok()
    print("6/6 ok")
