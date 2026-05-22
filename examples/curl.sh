#!/usr/bin/env bash
# Quick smoke-test of the reseller API with curl only.
# Set STARS_API_KEY first.
set -euo pipefail

API="${STARS_API_URL:-https://api-stars.ros.media/api}"
KEY="${STARS_API_KEY:?Set STARS_API_KEY first}"

echo "── services ──"
curl -s "$API?action=services" | head -c 400; echo

echo "── balance ──"
curl -s -X POST "$API" -d "key=$KEY" -d "action=balance"; echo

echo "── add ──"
ORDER_JSON=$(curl -s -X POST "$API" -d "key=$KEY" -d "action=add" \
  -d "service=1" -d "link=https://t.me/your_channel" -d "quantity=10")
echo "$ORDER_JSON"
ORDER_ID=$(echo "$ORDER_JSON" | python3 -c 'import json,sys;print(json.load(sys.stdin).get("order",""))')

if [[ -n "$ORDER_ID" ]]; then
  echo "── status $ORDER_ID ──"
  curl -s "$API?action=status&key=$KEY&order=$ORDER_ID"; echo

  echo "── cancel $ORDER_ID ──"
  curl -s -X POST "$API" -d "key=$KEY" -d "action=cancel" -d "orders=$ORDER_ID"; echo
fi
