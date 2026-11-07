#!/usr/bin/env bash
# Fund agent session key — landlord pays seed capital
# Usage: scripts/fund_agent.sh --dry-run [amount_eth] | --live
set -euo pipefail
MODE="${1:---dry-run}"
AMOUNT="${2:-100}" # default $100 equiv in ETH testnet units
RPC="${BASE_SEPOLIA_RPC:-https://sepolia.base.org}"
AGENT="$(jq -r .agent_address config/town_seed.json 2>/dev/null || echo "0xfcfaacdcaefec0dd04cfa4e423c1a2a39a3b058a")"

if [ "$MODE" = "--dry-run" ]; then
  echo "[dry-run] fund agent $AGENT with $AMOUNT wei"
  echo "[dry-run] requires LANDLORD_PRIVATE_KEY for --live"
  cat config/town_seed.json
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

cast send "$AGENT" \
  --value "$AMOUNT" \
  --rpc-url "$RPC" \
  --private-key "$LANDLORD_PRIVATE_KEY"

echo "funded $AGENT with $AMOUNT wei"
