# Changelog

Human-readable summary of public-facing changes. Internal infra commits are not listed here.

## 2026-05-22

- ✨ Public docs repo published.
- 🎨 Admin panel skinned with Tabler (MIT). Dark mode, sticky topbar, modern cards.
- 📊 KPI / ROI dashboard at `/admin/web/kpi` with revenue / cost / margin per period.
- 🛡️ Atomic withdrawal flow — no double-spend on parallel sessions.
- 🛡️ Subscription re-check before hold release — workers who unsubscribe early no longer get paid (UI promise enforced).
- 💸 Advertiser cancel-task action with refund of remaining slots.
- 🔐 Web sessions moved to SQLite (survive redeploy, scale horizontally).
- ⚡ Mini App Tier-1 polish: haptic on every tap, native BackButton on bottom sheets, onboarding overlay, pull-to-refresh, skeleton loaders.
- 🧾 Provider webhook routes ready: Tegro, Lava, UnitPay, Heleket (HMAC verify + idempotent credit).
- 💲 Reseller pricing updated: `USD_PER_STAR=0.020` (Fragment retail). Subscribers via task-exchange → $25 / 1000.

## Earlier (chronological)

- Telegram Stars Transfer (manual fulfilment for posts and profiles).
- Subscribers by language (RU / Global) and Premium-mix subscribers.
- Premium boost pipeline.
- TON Connect manifest + browser wallet linking.
- Bot Mini App, web cabinet at `/app`, order history at `/app/orders`.
- Giveaway / Jackpot / Check / Lucky Spin mechanics inside the bot.
- Two-level referral programme.
- Admin web panel with services / withdrawals / providers / instructions.
