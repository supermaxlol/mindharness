#!/usr/bin/env bash
# Set TownRent tariff — landlord only
# Usage: scripts/set_tariff.sh --dry-run [price_wei] | --live
set -euo pipefail
MODE="${1:---dry-run}"
PRICE="${2:-10000000000000000}" # 0.01 ether/sec default
RPC="${BASE_SEPOLIA_RPC:-https://sepolia.base.org}"
CONTRACT="$(jq -r .town_contract config/town_seed.json 2>/dev/null || echo "0x6528c917fbe3f49d1cebbdc6752271315840edfb")"

if [ "$MODE" = "--dry-run" ]; then
  echo "[dry-run] setTariff(price=$PRICE wei/sec) on $CONTRACT"
  echo "[dry-run] requires LANDLORD_PRIVATE_KEY for --live"
  exit 0
fi

if [ -z "${LANDLORD_PRIVATE_KEY:-}" ]; then
  echo "LANDLORD_PRIVATE_KEY not set. Refusing." >&2
  exit 2
fi

if ! command -v cast >/dev/null 2>&1; then
  echo "cast not found (Foundry). Install: https://getfoundry.sh" >&2
  exit 3
fi

cast send "$CONTRACT" \
  --rpc-url "$RPC" \
  --private-key "$LANDLORD_PRIVATE_KEY" \
  "setTariff(uint256)" "$PRICE"

echo "tariff set to $PRICE wei/sec"
