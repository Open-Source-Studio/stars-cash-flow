# FAQ

## What does the platform actually do?

It mediates between three parties on Telegram:

- **Advertisers** want subscribers / boosts / bot starts on their channel or bot.
- **Workers** want to earn Stars or TON.
- **Resellers** want a wholesale source of real engagement they can resell to their own customers via an existing SMM-panel UI.

We hold the user base of workers, the verification logic, the billing rails, and the API. Advertisers pay, workers earn, resellers integrate.

## Is the API actually compatible with JustAnotherPanel?

Yes, for the common subset:

- `services` / `balance` / `add` / `status` / `cancel` — same query format.
- Same statuses (`Pending`, `In progress`, `Partial`, `Completed`, `Canceled`).
- Same response shape (`charge`, `start_count`, `status`, `remains`, `currency`).
- Errors are returned with HTTP 200 and an `error` key (SMM-Panel convention).

What's missing today: `refill`, `refill_status`, drip-feed `runs/interval`, custom `comments`. Roadmap.

## Why is there a 21-day hold on Stars?

Telegram's own rule: a bot that receives Stars can only spend them 21 days after receipt. To avoid paying workers out of pocket while their funds are still escrowed, we mirror the hold. See [Hold and Refund Mechanics](Hold-and-Refund-Mechanics).

## What happens if a worker unsubscribes before the hold ends?

The hold sweeper re-checks subscription via `bot.get_chat_member()` right before paying. If the worker left / was kicked / was banned, the completion flips to `rejected_unsub` and the advertiser is refunded automatically. The worker gets a notification explaining the void.

## Who performs the actions?

Live Telegram users from the worker pool. A reward is credited only after a Bot-API-verified subscription that survives the hold window. Eligibility checks before paying out include premium gating, single-task-per-user, referral self-invite filter and subscription re-checks.

## How are prices set?

Two layers — formula-based and operator-set. Full breakdown in [Pricing Methodology](Pricing-Methodology).

## Can I deposit in fiat?

Webhook routes are ready and signature-verified for Tegro.Money, Lava.ru, UnitPay and Heleket. They activate as we wire each provider in. For now top-ups are via Telegram Stars (native) and TON (via CryptoBot).

## What about TON Connect?

The manifest is live at `https://api-stars.ros.media/tonconnect-manifest.json`. Wallet linking from the Mini App is on the roadmap; today you paste the address manually at withdrawal time.

## How is the production code licensed?

Production code is proprietary. This repo (public docs and examples) is MIT.

## How do I report a bug?

- Docs / examples bug → [open an issue](https://github.com/Open-Source-Studio/stars-cash-flow/issues/new/choose).
- Platform bug → [@StarsCashFlowbot](https://t.me/StarsCashFlowbot) → "Support".
- Security issue → see [SECURITY.md](https://github.com/Open-Source-Studio/stars-cash-flow/blob/main/SECURITY.md).
