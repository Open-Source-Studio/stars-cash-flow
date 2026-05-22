# Reseller API

`https://api-stars.ros.media/api` — JSON / form-encoded HTTP API drop-in compatible with the standard SMM-Panel API (JustAnotherPanel / SocPanel / AliPanel call signature).

> **TL;DR for existing SMM-panel resellers:** swap `URL` and `key` to ours, everything else works without changes.

## Authentication

Every request (except `services`) requires an `key` parameter — your personal API key, issued in the [web cabinet](https://api-stars.ros.media/app) or by the bot's "🔑 API ключ" button.

```bash
curl -X POST https://api-stars.ros.media/api \
  -d "key=YOUR_API_KEY" \
  -d "action=balance"
```

GET also works (query string), but POST is preferred for stable ordering with link parameters.

## Rate limits

- **60 requests per minute** per API key. 429 is returned when exceeded.
- **Order idempotency:** the same `service + link + quantity` from the same key within **120 seconds** returns the existing order id instead of creating a new one. Use this to safely retry after network failures.

## Actions

### `services` — list available services (public, no key)

```bash
curl "https://api-stars.ros.media/api?action=services"
```

Response: array of services with current pricing.

```json
[
  {
    "service": 1,
    "name": "Telegram Channel Subscribers (Task Exchange)",
    "type": "Default",
    "category": "Telegram / Subscribers",
    "rate": "25.0000",
    "min": "10",
    "max": "10000",
    "refill": false,
    "cancel": true,
    "description": "Real subscribers via task exchange. Bot must be admin in the channel.",
    "currency": "USD"
  },
  ...
]
```

`rate` is USD per 1000 units. See [`pricing.md`](pricing.md) for the underlying formula.

### `balance` — current balance

```bash
curl -X POST https://api-stars.ros.media/api -d "key=YOUR_API_KEY" -d "action=balance"
```

```json
{"balance": "10.5000", "currency": "USD"}
```

### `add` — create an order

```bash
curl -X POST https://api-stars.ros.media/api \
  -d "key=YOUR_API_KEY" \
  -d "action=add" \
  -d "service=1" \
  -d "link=https://t.me/your_channel" \
  -d "quantity=500"
```

```json
{"order": 12345}
```

Errors:
- `"Missing API key"` — no `key` parameter.
- `"Invalid API key"` — key not found or disabled.
- `"Incorrect service ID"` — service not in catalog.
- `"Service temporarily disabled"` — operations team paused this service.
- `"Quantity must be between {min} and {max}"` — outside service bounds.
- `"Insufficient balance"` — top up via `/app` or the bot.
- `"Link is required"` — service needs a link (most do).
- `"Rate limit exceeded. Max 60 requests per minute."` — back off.

### `status` — order status (single)

```bash
curl "https://api-stars.ros.media/api?action=status&key=YOUR_API_KEY&order=12345"
```

```json
{
  "charge": "10.0000",
  "start_count": "0",
  "status": "In progress",
  "remains": "500",
  "currency": "USD"
}
```

Possible statuses (compatible with SMM-Panel conventions):

| Status | Meaning |
|---|---|
| `Pending` | Order accepted, not yet started. |
| `In progress` | Workers are actively executing. |
| `Partial` | Paused / partially completed. |
| `Completed` | All slots filled. |
| `Canceled` | Order cancelled (yours or platform-side); leftover refunded to API balance. |

### `status` — multiple orders

```bash
curl "https://api-stars.ros.media/api?action=status&key=YOUR_API_KEY&orders=12345,12346,12347"
```

```json
{
  "12345": {"charge": "10.0000", "start_count": "0", "status": "In progress", "remains": "500", "currency": "USD"},
  "12346": {"charge": "5.0000", "start_count": "200", "status": "Completed", "remains": "0", "currency": "USD"},
  "12347": {"charge": "2.5000", "start_count": "50", "status": "Partial", "remains": "75", "currency": "USD"}
}
```

Up to 100 IDs per request.

### `cancel` — cancel one or several orders

```bash
curl -X POST https://api-stars.ros.media/api \
  -d "key=YOUR_API_KEY" \
  -d "action=cancel" \
  -d "orders=12345,12346"
```

```json
{"canceled": [12345, 12346]}
```

Refund of unfilled slots is credited to your `balance_usd` atomically. Already-completed orders are skipped (you stay charged for what was delivered).

## Errors

All errors return JSON with HTTP 200 (SMM-Panel convention):

```json
{"error": "Insufficient balance"}
```

Validate by checking for the `error` key first, then proceed with the success-shaped payload.

## Top-ups for the API balance

The API balance is in **USD**. Two ways to top up:

1. **From advertiser Stars balance** — open `/app`, choose "Конвертировать Stars → API USD", confirm. Uses the current `USD_PER_STAR` rate.
2. **From TON / fiat** — top up the **advertiser** balance first (Stars from Telegram, TON via CryptoBot, fiat via card providers — see [`pricing.md`](pricing.md)), then convert to API USD.

Direct USD top-up (Stripe / etc.) is on the roadmap.

## Future actions (roadmap)

- `refill` and `refill_status` — replenishment for dropoff (only for services where it makes sense).
- `add` with `runs` + `interval` — drip-feed.
- `add` with `comments` — text-content services.

Not implemented today. The fields will be added without breaking existing call signatures.
