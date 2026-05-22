# Mini App

Open inside Telegram: [t.me/StarsCashFlowbot/app](https://t.me/StarsCashFlowbot/app).

The Mini App is the same product as the bot, presented as a native Telegram Web App. Use whichever surface fits the moment — the data is shared and updates in real time.

## What's inside

| Section | What it does |
|---|---|
| **Профиль** | Telegram avatar + ID, current language, plain-text status. |
| **Баланс** | Advertiser Stars + TON, Worker Stars + TON, API USD — at a glance. |
| **Стейкинг** | Open a fixed-term deposit (1–12 months). APR set by admin, scales with duration. Principal + interest returns to the same balance at maturity. |
| **API** | Live preview of the public services catalog with current rates. |
| **Giveaways** | Browse, join, or (for owners) create / publish / draw giveaways without leaving Telegram. |
| **Checks** | Open or claim Stars cheques (similar to CryptoBot's checks but Stars-native). |
| **Jackpot** | Buy tickets for the live jackpot; winners drawn cryptographically (`secrets.SystemRandom`). |

## Tier-1 polish (2026-05-22)

- ✅ Haptic feedback on every tap (`HapticFeedback.impactOccurred`).
- ✅ Native TG `BackButton` on every bottom sheet — closes the sheet instead of the whole Mini App.
- ✅ Pull-to-refresh on the main screen.
- ✅ 3-slide onboarding overlay on first open (localStorage-gated `scf_onb_v1`).
- ✅ Skeleton loaders during initial fetch.
- ✅ Safe-area-inset padding (notch / home indicator).
- ✅ Light / dark theme follows Telegram's `colorScheme` and updates on the fly.

## Telegram WebApp integration notes

- `initData` is verified server-side with HMAC over `BOT_TOKEN`'s WebApp secret. Stale data (older than 24h) is rejected — no replay.
- `tg.expand()` + `tg.disableVerticalSwipes()` are called on init so the Mini App feels like a full app, not a draggable sheet.
- Header / background / bottom-bar colours are locked to the current theme for a cohesive look.
- All financial endpoints (`/miniapp/api/jackpot/buy`, `/miniapp/api/staking/open`, `/miniapp/api/giveaways/join`, ...) re-validate `initData` on every call.

## Open in a browser

The Mini App is also reachable as a plain HTTPS page: [api-stars.ros.media/miniapp](https://api-stars.ros.media/miniapp). Outside Telegram you'll see a stub asking you to open it via the bot — `initData` is not available without Telegram.

For a browser-only cabinet (with Telegram Login Widget instead of `initData`), use [api-stars.ros.media/app](https://api-stars.ros.media/app).
