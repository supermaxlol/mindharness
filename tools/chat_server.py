"""Minimal local chat for the cognitive harness (interim UI).

Serves a single page that talks to one persistent CognitiveHarness over
the llama backend (local llama-server). No auth, localhost only.
Usage: python3 tools/chat_server.py [--port 8181]
"""

from __future__ import annotations

import argparse
import json
import os
import socket
import sys
import threading
import time
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from cognitive_harness import CognitiveHarness

STATE_DEFAULT = "/Users/shehzad/Desktop/mindharness/harness_state.json"


def parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser()
    ap.add_argument("--port", type=int, default=8181)
    ap.add_argument("--snapshot", default=STATE_DEFAULT,
                    help="harness state file to load on start and save per turn")
    ap.add_argument("--heartbeat", default=None,
                    help="keeper heartbeat file: background tick verifies the "
                         "port accepts connections and reports turn count")
    return ap.parse_args()


ARGS = parse_args()

HARNESS = CognitiveHarness(
    backend="llama", base_url="http://127.0.0.1:8081/v1",
    model="spark-x2.5-4b", name="shehzad-loop")
if os.path.exists(ARGS.snapshot):
    HARNESS.load_state(ARGS.snapshot)
LOCK = threading.Lock()
LAST_TURN_OK = {"ok": True}


def heartbeat_tick(port: int, path: str) -> None:
    time.sleep(5)
    last_turn = 0
    while True:
        try:
            with socket.create_connection(("127.0.0.1", port), timeout=5):
                serving = True
        except OSError:
            serving = False
        # Non-blocking read: a slow inference turn may hold LOCK for
        # minutes; the heartbeat must keep proving liveness through that.
        if LOCK.acquire(blocking=False):
            try:
                last_turn = HARNESS.turn_count
            finally:
                LOCK.release()
        coverage = 1.0 if (serving and LAST_TURN_OK["ok"]) else 0.0
        hb = {"name": "chat-server", "pid": os.getpid(), "ts": time.time(),
              "turn": last_turn, "gamma": 0.0, "energy": 1.0,
              "coverage": coverage, "query_rate": 0.0}
        tmp = path + ".tmp"
        try:
            with open(tmp, "w") as f:
                json.dump(hb, f)
            os.replace(tmp, path)
        except OSError:
            pass
        time.sleep(30)


if ARGS.heartbeat:
    threading.Thread(target=heartbeat_tick,
                     args=(ARGS.port, ARGS.heartbeat), daemon=True).start()

PAGE = """<!doctype html><html><head><meta charset="utf-8">
<title>mindharness chat (local)</title>
<style>body{font-family:system-ui;max-width:720px;margin:2em auto;padding:0 1em}
#log{border:1px solid #ccc;min-height:300px;padding:1em;white-space:pre-wrap}
.me{color:#036}.harness{color:#060}.row{display:flex;gap:.5em;margin-top:1em}
input{flex:1;padding:.5em}</style></head><body>
<h2>mindharness — local chat (spark-x2.5-4b)</h2>
<div id="log"></div>
<div class="row"><input id="box" placeholder="talk to the loop…">
<button onclick="send()">send</button></div>
<script>
async function send(){
  const box=document.getElementById('box'), log=document.getElementById('log');
  const text=box.value.trim(); if(!text) return; box.value='';
  log.innerHTML+=`<div class="me">you> ${text}</div>`;
  const r=await fetch('/api/chat',{method:'POST',
    headers:{'Content-Type':'application/json'},
    body:JSON.stringify({message:text})});
  const j=await r.json();
  log.innerHTML+=`<div class="harness">harness> ${j.reply}</div>`;
  log.scrollTop=log.scrollHeight;
}
document.getElementById('box').addEventListener('keydown',e=>{if(e.key==='Enter')send()});
</script></body></html>"""


class Handler(BaseHTTPRequestHandler):
    def _send(self, body: bytes, ctype: str = "text/html") -> None:
        self.send_response(200)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:  # noqa: N802
        if self.path == "/api/state":
            with LOCK:
                body = json.dumps({
                    "turn": HARNESS.turn_count,
                    "confidence": HARNESS.internal.confidence,
                    "memories": len(HARNESS.memory.episodic),
                }).encode()
            self._send(body, "application/json")
        else:
            self._send(PAGE.encode())

    def do_POST(self) -> None:  # noqa: N802
        if self.path != "/api/chat":
            self.send_response(404)
            self.end_headers()
            return
        length = int(self.headers.get("Content-Length", 0))
        try:
            msg = json.loads(self.rfile.read(length) or b"{}")["message"]
        except (ValueError, KeyError):
            msg = ""
        with LOCK:
            try:
                reply = HARNESS.process_turn(str(msg)[:2000])
                HARNESS.save_state(ARGS.snapshot)
                LAST_TURN_OK["ok"] = True
            except Exception as e:
                LAST_TURN_OK["ok"] = False
                reply = f"harness turn failed: {e}"
        self._send(json.dumps({"reply": reply}).encode(),
                   "application/json")

    def log_message(self, *args) -> None:
        pass


if __name__ == "__main__":
    HTTPServer(("127.0.0.1", ARGS.port), Handler).serve_forever()
