# Pricing

Public reference for our pricing model. Numbers track production env; if anything in this doc disagrees with `api?action=services`, the API is the source of truth.

## Two pricing layers

### Layer 1 — formula-based (task-exchange services)

For services where the platform routes real Telegram users from our worker pool:

```
rate_usd_per_1000 = reward_stars × (1 + platform_fee / 100) × USD_PER_STAR × 1000
```

Current production constants:

| Constant | Value |
|---|---|
| `USD_PER_STAR` | `0.020` (≈ Fragment retail) |
| `PLATFORM_FEE_PERCENT` | `25` |

That gives:

| ID | Service | Reward / unit | Reseller pays |
|---|---|---|---|
| `1` | Telegram channel subscribers (task exchange) | 1 ⭐ | **$25.00 / 1000** |
| `2` | Telegram channel boosts (task exchange) | 2 ⭐ | **$50.00 / 1000** |
| `3` | Telegram bot starts (task exchange) | 1 ⭐ | **$25.00 / 1000** |

You can change `USD_PER_STAR` or `PLATFORM_FEE_PERCENT` via env in Coolify — formulas re-evaluate without a deploy.

### Layer 2 — operator-set (manual services)

For services that the operations team fulfils manually, the rate is stored per-service and editable in the admin panel without a deploy (`/admin/web` → Services → `rate_usd`).

| ID | Service | Reseller pays |
|---|---|---|
| `10` | Telegram Stars Transfer (to Post) | **$9.50 / 1000** |
| `11` | Telegram Stars Transfer (to Profile) | **$9.50 / 1000** |
| `12` | Telegram Subscribers RU locale | **$11.00 / 1000** |
| `13` | Telegram Subscribers Global locale | **$9.50 / 1000** |
| `14` | Telegram Premium Users (Subscribers Mix) | **$17.00 / 1000** |
| `15` | Telegram Boosts Premium (Manual) | **$28.00 / 1000** |

Always query `action=services` for the live rate — operators tune these based on supply.

## Conversions

- **Stars → USD on the API balance:** rate = `USD_PER_STAR`. No conversion fee right now.
- **Stars → TON / TON → Stars:** not supported by the platform. Convert externally if needed.

## Withdrawal fees

Withdrawals are **0% fee** today. Minimums apply:

| Currency | Min withdrawal |
|---|---|
| Stars | 1000 ⭐ |
| TON | 5 💎 |

## Hold windows

Telegram Stars charge-back protection runs **21 days** (Telegram rule). Workers see rewards as "frozen" with a release date. TON holds **48 hours** by default.

If a worker unsubscribes from the target channel before the hold release — the reward is voided and the advertiser is refunded automatically.

## Refunds

- **Cancel-task** by the advertiser: leftover `(total_slots − done_slots) × reward × (1 + fee/100)` returns to the advertiser balance atomically.
- **Order cancel** via reseller API: leftover slots refund to `api_keys.balance_usd`.
- **Worker unsub** during hold: reward returns to the original advertiser balance.

## Volume / wholesale

Per-client wholesale tiers (different `rate_usd` for specific API keys) are not implemented today. Contact us if you need a custom contract for >$5k/month volume.
