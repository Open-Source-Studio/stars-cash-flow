# Bot guide

Bot username: [@StarsCashFlowbot](https://t.me/StarsCashFlowbot).

Two user types share the same bot: **advertiser** (creates tasks, pays Stars / TON) and **worker** (does tasks, earns Stars / TON). A single Telegram account can be both — the menu lets you switch context.

## Quick start — advertiser

1. `/start` → choose **«Рекламодатель / Advertiser»** in the language picker.
2. Tap **💎 Пополнить баланс**.
   - Telegram Stars: native Stars invoice, you pay in Telegram, balance credits instantly.
   - TON via CryptoBot: opens an invoice link, scan-and-pay, balance credits after blockchain confirmation.
3. Tap **➕ Создать задание**.
   - Type: subscribe (channel) / boost / bot start.
   - Target: `@channel`, post URL, bot username.
   - Reward per worker (Stars or TON) and number of slots.
   - Confirm — the cost is the reward × slots × `(1 + platform fee %)`. Balance is reserved atomically.
4. Watch progress in **📋 Мои задания** — pause / resume / cancel.
   - Cancel returns leftover reservation to your advertiser balance.

### Stars hold window

Telegram Stars rewards delivered to workers go through a **21-day hold** (Telegram-side anti-fraud rule). During the hold:
- Worker sees the reward as "frozen" with a release date.
- If the worker leaves the channel before release — the reward is voided and refunded to the advertiser.

TON rewards default to a **48-hour hold** (anti-chargeback). Both windows are configurable on the platform side.

## Quick start — worker

1. `/start` → choose **«Воркер / Worker»**.
2. **🎯 Задания** — list of available tasks (sorted by reward, filtered by your eligibility).
3. Tap a task → follow the instruction (subscribe, boost, start the target bot) → tap **✅ Готов**.
4. Bot verifies and writes a completion. Reward enters the hold state and releases automatically.
5. **💰 Мой баланс** → **⭐ Вывести Stars** or **💎 Вывести TON**:
   - Stars are paid out manually by an operator to your Telegram account (`@username` or numeric ID).
   - TON is paid out manually to the TON address you provide. Minimums configured platform-side; see the dialog.

### Eligibility & verification

- One worker can take each task once.
- Subscription is re-checked at the end of the hold — leaving early voids the reward.
- Referral bonuses ignore self-invites.
- Premium-only tasks are gated by Telegram Premium status.

## Common commands

- `/start` — main menu.
- `/admin` — only visible to user IDs listed in `ADMIN_IDS`. Opens the in-bot admin shortcut.
- `/lang` — switch UI language (RU / EN).

The full UI is built around inline keyboards, so the command surface is intentionally small.

## Referral programme

Two levels:
- **L1**: 10% of every reward the person you invited earns (configurable).
- **L2**: 3% of every reward that L1's invitee earns.

Bonuses are credited **instantly** (not subject to the 21-day hold) and shown in **🤝 Рефералы**.

## Withdrawals

- Stars: minimum 1000 ⭐ per request. Operator processes within 24 hours.
- TON: minimum 5 💎 per request. Operator processes within 24 hours.

Balance is debited at the moment of the request (atomically). If you spam two requests at the same time, only one will pass.

## Support

In the bot → **🆘 Поддержка** → write your question. Operator response usually within a few hours.
