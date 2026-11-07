#!/usr/bin/env bash
# TownRent deploy + seed tariffs + fund agent — Base Sepolia stub
# Usage: scripts/deploy_town.sh --dry-run (default mock) | --live
set -euo pipefail
MODE="${1:---dry-run}"
CHAIN="Base Sepolia"
RPC="${BASE_SEPOLIA_RPC:-https://sepolia.base.org}"

if [ ! -f contracts/TownRent.sol ]; then
  echo "missing contracts/TownRent.sol" >&2
  exit 1
fi

if [ "$MODE" = "--dry-run" ]; then
  echo "[dry-run] chain=$CHAIN rpc=$RPC"
  echo "[dry-run] would compile contracts/TownRent.sol"
  echo "[dry-run] would deploy TownRent, set tariff 0.01e18 wei/sec"
  echo "[dry-run] would fund agent session key 100 tokens (equiv)"
  echo "[dry-run] update config/town_seed.json + bundles/dsh-skin-house/cordis.patch.yml"
  cat config/town_seed.json
  exit 0
fi

# Live path — requires landlord key offline. Never auto-generate master key.
if [ -z "${LANDLORD_PRIVATE_KEY:-}" ]; then
  echo "LANDLORD_PRIVATE_KEY not set. Refusing live deploy (safety)." >&2
  echo "Provide key via env or hardware wallet, then re-run --live" >&2
  exit 2
fi

if ! command -v forge >/dev/null 2>&1; then
  echo "forge not found. Install Foundry: https://getfoundry.sh" >&2
  exit 3
fi

echo "Deploying TownRent to $CHAIN via $RPC"
forge create contracts/TownRent.sol:TownRent \
  --rpc-url "$RPC" \
  --private-key "$LANDLORD_PRIVATE_KEY"
# Next steps (stub):
# 1. setTariff(10000000000000000)  # 0.01 ether/sec
# 2. fund agent session key from config/town_keys.json
# 3. update bundles/dsh-skin-house/cordis.patch.yml townContract to deployed address
# 4. re-run tools/validate_dsh_bundles.py
echo "live deploy stub completed — fill RPC + funding + config update before mainnet"
