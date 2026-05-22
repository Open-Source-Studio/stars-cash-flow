"""
Minimal Python client for the Stars Cash Flow reseller API.
Standard library only — no third-party deps.

Usage:
    export STARS_API_KEY="your-key"
    python python.py services
    python python.py balance
    python python.py add 1 https://t.me/your_channel 500
    python python.py status 12345
    python python.py cancel 12345
"""

import json
import os
import sys
import urllib.parse
import urllib.request

API_URL = os.environ.get("STARS_API_URL", "https://api-stars.ros.media/api")
API_KEY = os.environ.get("STARS_API_KEY", "")


def call(action: str, **params) -> dict:
    payload = {"action": action, **params}
    if action != "services":
        if not API_KEY:
            raise SystemExit("Set STARS_API_KEY first.")
        payload["key"] = API_KEY
    body = urllib.parse.urlencode(payload).encode()
    req = urllib.request.Request(
        API_URL,
        data=body,
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=20) as resp:
        return json.loads(resp.read().decode())


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 1
    cmd = sys.argv[1]
    if cmd == "services":
        out = call("services")
    elif cmd == "balance":
        out = call("balance")
    elif cmd == "add" and len(sys.argv) == 5:
        out = call("add", service=int(sys.argv[2]), link=sys.argv[3], quantity=int(sys.argv[4]))
    elif cmd == "status" and len(sys.argv) == 3:
        out = call("status", order=int(sys.argv[2]))
    elif cmd == "cancel" and len(sys.argv) == 3:
        out = call("cancel", orders=sys.argv[2])
    else:
        print(__doc__)
        return 1
    print(json.dumps(out, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
