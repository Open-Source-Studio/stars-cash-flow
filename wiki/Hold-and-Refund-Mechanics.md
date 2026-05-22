# Hold-and-Refund-Mechanics

## Why holds at all?

Telegram's own rule: a bot that *receives* Stars can only spend them 21 days after receipt. If we pay a worker out of our pocket today and the advertiser charges back tomorrow, we're left with negative Stars float for three weeks.

We mirror Telegram's window on the worker side. Workers see the reward as **frozen** with a precise release date; if they violate the deal (e.g., unsubscribe from the channel) before that date, the reward is voided.

For TON tasks the default hold is 48 hours — long enough to catch obvious chargeback-style fraud, short enough not to annoy honest workers.

## The sweeper

A background task runs every 5 minutes. It:

1. Selects `completions` with `status='hold' AND release_at <= now`.
2. For each row with `task.type = 'subscribe'`:
   - Calls `bot.get_chat_member(target, worker_id)`.
   - If the worker's status is `left / kicked / banned` → mark the completion `rejected_unsub` and **refund the advertiser** with `reward × (1 + fee/100)`.
   - If the verify call fails (chat private, bot kicked, parse error) — skip this row, retry next sweep. We never punish a worker because *we* couldn't verify.
3. Atomically claims each row that survived (`UPDATE completions SET status='released' WHERE id=? AND status='hold'`) and credits the worker only if the claim won. Two parallel sweeper invocations can never double-credit.

The credit always writes a `payments` row with a **unique** `payload = hold_release_{id}` — a third defence on top of the claim, in case admin tooling triggers a re-run.

## Refund types

| Type | When | Refund destination |
|---|---|---|
| `task_refund` | Advertiser cancels a task with leftover slots. | Advertiser balance (Stars or TON), atomically. |
| `unsub_refund` | Worker unsubscribed before hold release. | Advertiser balance, atomically. Worker gets `rejected_unsub`. |
| Reseller `cancel` action | API cancellation of unfilled units. | `api_keys.balance_usd`. |

All refunds are `INSERT ... ON CONFLICT(payload) DO NOTHING` — idempotent on the unique payload, so a retried sweeper does not double-credit.
