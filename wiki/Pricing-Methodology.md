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

## Why not match the cheapest competitor on bot followers?

Because our workers are real Telegram users who get paid in Stars. Cost-per-acquisition is `reward × (1 + fee)`, not the marginal compute cost of spinning up another bot account. Cheaper providers ship bots that drop off in days; ours stay subscribed because the worker earns from the platform, not from a one-off bot click.

The hold + subscription re-check at release time enforces this on the platform side, not just in marketing copy. See [Hold and Refund Mechanics](Hold-and-Refund-Mechanics).
