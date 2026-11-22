#!/usr/bin/env python3
"""Live server for the Lab ERP workbench, for the review days.

Serves ../workbench.html and keeps the shared model in data/model.json.
Everyone who opens the page edits the same model. Changes show up for the
others within a few seconds; edits to different things never collide.
Python standard library only, nothing to install.

Run on the Tower: copy the repo folder (at least workbench.html and server/)
to /mnt/user/appdata/lab-erp, then

  docker run -d --name lab-erp --restart unless-stopped -p 8787:8787 \
    -v /mnt/user/appdata/lab-erp:/app -w /app python:3.12-alpine python server/server.py

and point the Cloudflare tunnel at http://<tower-ip>:8787.
There is no login here, so put Cloudflare Access in front of it.

First start     data/model.json is created from the data inside workbench.html.
New app code    replace workbench.html, reload the page. The live data stays.
Start over      stop the container, delete data/model.json, start it again.
Into the repo   "Download copy" in the page gives a complete workbench.html.
Safety copies   data/history/ gets a copy of the model at most every 10 minutes.
"""
import json, os, re, threading, time
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

HERE = os.path.dirname(os.path.abspath(__file__))
PAGE = os.environ.get("WB_PAGE", os.path.join(HERE, "..", "workbench.html"))
DATA = os.environ.get("WB_DATA", os.path.join(HERE, "data"))
PORT = int(os.environ.get("PORT", "8787"))
MODEL = os.path.join(DATA, "model.json")
HIST = os.path.join(DATA, "history")

lock = threading.Lock()
db = {"rev": 0, "state": None}
last_copy = 0.0


def data_from_page():
    with open(PAGE, encoding="utf-8") as f:
        m = re.search(r'<script type="application/json" id="model-data">\s*(.*?)\s*</script>', f.read(), re.S)
    return json.loads(m.group(1))


def write_model():
    global last_copy
    tmp = MODEL + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(db, f, ensure_ascii=False, indent=1)
    os.replace(tmp, MODEL)
    if time.time() - last_copy > 600:
        last_copy = time.time()
        with open(os.path.join(HIST, time.strftime("model-%Y%m%d-%H%M%S.json")), "w", encoding="utf-8") as f:
            json.dump(db, f, ensure_ascii=False)


def load():
    os.makedirs(HIST, exist_ok=True)
    if os.path.exists(MODEL):
        with open(MODEL, encoding="utf-8") as f:
            db.update(json.load(f))
    else:
        db.update(rev=1, state=data_from_page())
        write_model()


class Handler(BaseHTTPRequestHandler):
    def reply(self, code, body, ctype="application/json; charset=utf-8"):
        if not isinstance(body, bytes):
            body = json.dumps(body, ensure_ascii=False).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        url = urlparse(self.path)
        if url.path in ("/", "/workbench.html"):
            with open(PAGE, "rb") as f:
                return self.reply(200, f.read(), "text/html; charset=utf-8")
        if url.path == "/api/state":
            since = parse_qs(url.query).get("since", [None])[0]
            with lock:
                body = {"rev": db["rev"]} if since == str(db["rev"]) else db
                body = json.dumps(body, ensure_ascii=False).encode("utf-8")
            return self.reply(200, body)
        self.reply(404, {"error": "not found"})

    def do_PUT(self):
        if urlparse(self.path).path != "/api/state":
            return self.reply(404, {"error": "not found"})
        size = int(self.headers.get("Content-Length") or 0)
        if size <= 0 or size > 20_000_000:
            return self.reply(413, {"error": "bad size"})
        try:
            body = json.loads(self.rfile.read(size))
            base, state = body["base"], body["state"]
            assert isinstance(state, dict) and isinstance(state.get("entities"), list)
        except Exception:
            return self.reply(400, {"error": "bad request"})
        with lock:
            if base != db["rev"]:
                # someone saved first: send the newest model, the page merges and sends again
                out = (409, json.dumps(db, ensure_ascii=False).encode("utf-8"))
            else:
                db["rev"] += 1
                db["state"] = state
                write_model()
                out = (200, {"rev": db["rev"]})
        self.reply(*out)

    def log_message(self, *args):
        pass


if __name__ == "__main__":
    load()
    print(f"Lab ERP workbench on port {PORT}, model rev {db['rev']}, data in {DATA}", flush=True)
    ThreadingHTTPServer(("0.0.0.0", PORT), Handler).serve_forever()
