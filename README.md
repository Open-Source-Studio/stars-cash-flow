# ✨ Stars Cash Flow

> Telegram Stars CPA platform — Mini App, bot and reseller API around the new Telegram payment stack.

[![Bot](https://img.shields.io/badge/Telegram-%40StarsCashFlowbot-26A5E4?logo=telegram&logoColor=white)](https://t.me/StarsCashFlowbot)
[![Mini App](https://img.shields.io/badge/Mini%20App-Open-2563eb)](https://t.me/StarsCashFlowbot/app)
[![Site](https://img.shields.io/badge/stars.ros.media-Landing-0ea5e9)](https://stars.ros.media)
[![API](https://img.shields.io/badge/API-api--stars.ros.media-22c55e)](https://api-stars.ros.media)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

This repository contains **public documentation, integration guides and examples** for the Stars Cash Flow platform. Production code lives in a private repository.

---

## What it is

A Telegram-native CPA platform:

- **Advertisers** create tasks (channel subscribe / boost / bot start) and pay rewards in Telegram **Stars** or **TON**.
- **Workers** execute tasks inside Telegram and earn the reward, withdrawn to their Telegram account (Stars) or TON wallet.
- **Resellers** integrate over a standard SMM-Panel-compatible HTTP API — drop-in compatible with the JustAnotherPanel / SocPanel / AliPanel call signature.

The platform owns the worker pool, anti-cheat (hold periods + subscription re-checks), and the billing rails. Everything is built around the real Telegram Stars economy — no fake balances, no synthetic followers.

## Entry points

| Where | What |
|---|---|
| **Bot** | [@StarsCashFlowbot](https://t.me/StarsCashFlowbot) — full UI for advertisers and workers, deposits / withdrawals, task management. |
| **Mini App** | [t.me/StarsCashFlowbot/app](https://t.me/StarsCashFlowbot/app) — same product as a Telegram Web App: balance, KPI, staking, giveaways. |
| **Web cabinet** | [api-stars.ros.media/app](https://api-stars.ros.media/app) — browser cabinet with Telegram Login, order history. |
| **Reseller API** | [api-stars.ros.media/api](https://api-stars.ros.media/api) — SMM-Panel-compatible JSON API. See [docs/api.md](docs/api.md). |
| **Site** | [stars.ros.media](https://stars.ros.media) — public landing with FAQ and pricing. |

## Documentation

| Doc | What |
|---|---|
| [`docs/api.md`](docs/api.md) | Reseller API reference — actions, params, response shapes, error codes, rate limits. |
| [`docs/bot.md`](docs/bot.md) | End-user guide for advertisers and workers (commands, deposit flows, withdrawal). |
| [`docs/miniapp.md`](docs/miniapp.md) | Mini App feature tour and Telegram WebApp integration notes. |
| [`docs/pricing.md`](docs/pricing.md) | Pricing model, conversion (Stars↔USD), volume tiers, refund rules. |
| [`docs/architecture.md`](docs/architecture.md) | High-level architecture, components, lifecycle of a task, hold mechanics. |
| [`SECURITY.md`](SECURITY.md) | Responsible disclosure policy. |
| [`CHANGELOG.md`](CHANGELOG.md) | Release notes. |

## Quickstart for resellers

```bash
# 1. Get an API key (top up balance in /app or via the bot first)
# 2. Inspect the catalog
curl "https://api-stars.ros.media/api?action=services"

# 3. Create an order
curl -X POST https://api-stars.ros.media/api \
  -d "key=YOUR_API_KEY" \
  -d "action=add" \
  -d "service=1" \
  -d "link=https://t.me/your_channel" \
  -d "quantity=500"
# → {"order": 12345}

# 4. Poll status
curl "https://api-stars.ros.media/api?action=status&key=YOUR_API_KEY&order=12345"
# → {"charge": "10.00", "start_count": "0", "status": "In progress", "remains": "500", "currency": "USD"}
```

More examples in [`examples/`](examples/).

## Status

| Component | State |
|---|---|
| Telegram bot | ✅ Production |
| Mini App | ✅ Production (Tier-1: haptic, native back button, onboarding) |
| Web cabinet | ✅ Production |
| Reseller API | ✅ Production — services, balance, add, status, cancel |
| TON Connect | ✅ Manifest live |
| Stars deposits | ✅ Telegram Stars native |
| TON deposits | ✅ via CryptoBot |
| Card / fiat top-ups | 🚧 Routes ready, providers pending integration |
| Refill API action | ⏳ Planned |

## Support

- Bot: write to [@StarsCashFlowbot](https://t.me/StarsCashFlowbot) and choose "Поддержка / Support".
- Security: see [SECURITY.md](SECURITY.md).
- General: open an issue in this repository.

## License

[MIT](LICENSE) — public docs and example code.
The platform's production code is proprietary and lives elsewhere.
