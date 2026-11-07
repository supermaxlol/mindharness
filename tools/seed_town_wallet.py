"""Seed Town wallet (mock) + set tariffs.

Usage: python3 tools/seed_town_wallet.py [--reset]

Generates landlord + agent session keys and a mock Town contract address.
Stores keys in config/town_keys.json (mode 600), config in config/town_seed.json.
This is a local simulation — no real funds moved. For testnet, swap in real keys.
"""

from __future__ import annotations

import json
import hashlib
import secrets
import stat
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
CONFIG = REPO / "config"


def mock_address(prefix_bytes: bytes) -> str:
    h = hashlib.sha3_256(prefix_bytes + secrets.token_bytes(32)).hexdigest()
    return "0x" + h[-40:]


def new_key(seed_label: str) -> dict:
    priv = secrets.token_hex(32)
    addr = mock_address(seed_label.encode() + priv.encode())
    return {"address": addr, "private_key_hex": priv}


def main(reset: bool = False) -> None:
    CONFIG.mkdir(parents=True, exist_ok=True)
    keys_path = CONFIG / "town_keys.json"
    seed_path = CONFIG / "town_seed.json"

    if keys_path.exists() and not reset:
        keys = json.loads(keys_path.read_text())
        seed = json.loads(seed_path.read_text())
        print(f"already seeded: agent={seed['agent_address']} contract={seed['town_contract']}")
        return

    landlord = new_key("landlord")
    agent = new_key("agent")
    town = {"address": mock_address(b"town-rent-contract")}

    keys = {"landlord": landlord, "agent_session": agent}
    keys_path.write_text(json.dumps(keys, indent=1))
    keys_path.chmod(0o600)

    seed = {
        "town_contract": town["address"],
        "landlord_address": landlord["address"],
        "agent_address": agent["address"],
        "tariff_per_second": 0.01,  # $0.01 / GPU-sec ~ $0.60/min
        "initial_balance": 100.0,   # $100 seed capital
        "daily_limit": 50.0,
        "per_action_limit": 5.0,
        "floor_reserve": 10.0,
    }
    seed_path.write_text(json.dumps(seed, indent=1))
    seed_path.chmod(0o644)

    # Prove loop closes: create wallet, seed, pay 10 sec rent
    import sys
    sys.path.insert(0, str(REPO))
    from tools.harness_core.skin_house import Wallet

    w = Wallet(
        town_contract=seed["town_contract"],
        daily_limit=seed["daily_limit"],
        per_action_limit=seed["per_action_limit"],
        balance=seed["initial_balance"],
    )
    w.pay_rent(0.1, 10, "memory_lookup")  # 10 sec at tariff
    print(json.dumps({
        "agent": seed["agent_address"],
        "contract": seed["town_contract"],
        "tariff_per_second": seed["tariff_per_second"],
        "initial_balance": seed["initial_balance"],
        "after_10s_rent_balance": w.balance,
        "keys_file": str(keys_path),
        "seed_file": str(seed_path),
    }, indent=1))


if __name__ == "__main__":
    import sys
    main(reset="--reset" in sys.argv)
