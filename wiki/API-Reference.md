# API Reference

Full reseller API documentation. For quickstart see the repo [`docs/api.md`](https://github.com/Open-Source-Studio/stars-cash-flow/blob/main/docs/api.md).

Endpoint: `https://api-stars.ros.media/api`

## Authentication

Every action except `services` requires `key` — the API key issued in the [web cabinet](https://api-stars.ros.media/app).

```bash
curl -X POST https://api-stars.ros.media/api \
  -d "key=YOUR_API_KEY" -d "action=balance"
```

## Actions

| action | params | what |
|---|---|---|
| `services` | _(none)_ | List services with current rates. Public. |
| `balance` | `key` | Your USD balance. |
| `add` | `key, service, link, quantity` | Create an order. Returns `{order}`. |
| `status` | `key, order` _or_ `key, orders=1,2,3` | Order status (single or multi, up to 100). |
| `cancel` | `key, orders=1,2,3` | Cancel orders, refund unfilled slots. |

## Response format

Success — JSON object. Errors — JSON `{"error": "Message"}` with HTTP 200 (SMM-Panel convention).

## Rate limits

- 60 requests / minute / key. 429 on overrun.
- Order idempotency: same `service + link + quantity` from one key within 120 s returns the same order id (safe retry).

## Compatibility

Drop-in with **JustAnotherPanel**, **SocPanel**, **AliPanel**. Swap URL + key and the rest of your integration works unchanged. Same statuses (`Pending / In progress / Partial / Completed / Canceled`), same shape (`charge / start_count / remains / currency`).
