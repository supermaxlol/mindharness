#!/bin/zsh
# Single-instance launcher for the keeper-tended chat server.
# Kills the previous instance (by pidfile, never by pattern: the keeper's
# own command line contains this script's arguments) then starts one peer.
# Extra args (e.g. --snapshot from the keeper) are forwarded.
PIDFILE=/tmp/chat-server.pid
if [[ -f "$PIDFILE" ]]; then
  OLD=$(cat "$PIDFILE" 2>/dev/null)
  if [[ -n "$OLD" ]] && kill -0 "$OLD" 2>/dev/null; then
    kill "$OLD" 2>/dev/null
    sleep 2
  fi
fi
echo $$ > "$PIDFILE"
exec /usr/bin/python3 /Users/shehzad/Desktop/mindharness/tools/chat_server.py \
  --port 8181 --heartbeat /tmp/keeper-chat-peer.json "$@"
