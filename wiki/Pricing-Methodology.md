# Pricing-Methodology

Two layers — formula-based and operator-set.

## Layer 1 — formula

For task-exchange services (where real workers fulfil tasks for a Stars reward):

```
rate_usd_per_1000 = reward_stars × (1 + platform_fee / 100) × USD_PER_STAR × 1000
```

Production defaults:

| Variable | Today |
|---|---|
| `USD_PER_STAR` | `0.020` (≈ Fragment retail) |
| `PLATFORM_FEE_PERCENT` | `25` |

Examples:

| Service | Reward per unit | Reseller pays |
|---|---|---|
| Channel subscribers (id=1) | 1 ⭐ | **$25 / 1000** |
| Channel boosts (id=2) | 2 ⭐ | **$50 / 1000** |
| Bot starts (id=3) | 1 ⭐ | **$25 / 1000** |

Changing either env variable in Coolify takes effect without a redeploy.

## Layer 2 — operator-set

Manual services (Stars Transfer, Premium Mix subscribers, Premium Boosts, RU/Global locale-targeted) have hand-priced `rate_usd` stored per service in the DB, edited via the admin panel without a deploy. Live values at [`/api?action=services`](https://api-stars.ros.media/api?action=services).

## Why is the rate at this level?

Our cost-per-acquisition is `reward × (1 + fee)` — the actual Stars we pay a live Telegram user to complete a task. Subscribers stay subscribed because they are paid through the platform on each verified action, and the platform re-checks subscription at the end of the hold (see [Hold and Refund Mechanics](Hold-and-Refund-Mechanics)).

In other words, the rate maps to a real action by a real account, and that's enforced on the platform side rather than promised in marketing copy.
