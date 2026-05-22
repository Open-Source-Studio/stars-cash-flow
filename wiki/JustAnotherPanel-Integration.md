# JustAnotherPanel-Integration

If you're already running an SMM panel that calls JustAnotherPanel / SocPanel / AliPanel — you can switch the upstream to Stars Cash Flow without code changes.

## Three things to change

1. **Endpoint URL**
   ```
   OLD: https://justanotherpanel.com/api/v2
   NEW: https://api-stars.ros.media/api
   ```
2. **API key** — get yours from the [web cabinet](https://api-stars.ros.media/app).
3. **Service IDs** — our IDs are smaller and curated. Map them via the table below.

## Service mapping (suggested)

| Your panel calls | Set service= |
|---|---|
| Telegram subscribers (real / mixed) | `1` (task-exchange) or `12` (RU manual) or `13` (Global manual) |
| Telegram subscribers premium-mix | `14` |
| Telegram boosts | `2` (task-exchange) or `15` (Premium manual) |
| Telegram bot starts / referrals | `3` |
| Stars transfer (post) | `10` |
| Stars transfer (user) | `11` |

Always check live rates and limits with `action=services` — they may be tuned by operators.

## Currency

Our API balance is in **USD** (4 decimals). Top up advertiser Stars via Telegram Stars or TON via CryptoBot, then convert in `/app`.

## Statuses

Compatible with SMM-Panel conventions: `Pending`, `In progress`, `Partial`, `Completed`, `Canceled`.

## Cancellation

`action=cancel&orders=12345,12346` refunds unused slots back to your USD balance, atomically. Already-delivered units stay billed.

## Idempotency

Same `service + link + quantity` within 120 s returns the same `order_id` — safe to retry on transient errors.

## Worked example

```python
import requests
API = "https://api-stars.ros.media/api"
KEY = "your_key_here"

# 1. Services
print(requests.get(API, params={"action": "services"}).json())

# 2. Add
r = requests.post(API, data={"key": KEY, "action": "add", "service": 1, "link": "https://t.me/your_channel", "quantity": 500}).json()
order_id = r["order"]

# 3. Status
print(requests.post(API, data={"key": KEY, "action": "status", "order": order_id}).json())
```
