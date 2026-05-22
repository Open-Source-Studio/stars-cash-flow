# Money-Safety-Invariants

What the platform guarantees at the SQL layer, not just in business logic.

## 1. One transaction = one balance change

Every debit / credit lives inside a `BEGIN IMMEDIATE` block. SQLite's advisory lock makes the read-modify-write atomic with respect to any other writer.

## 2. Conditional UPDATE guards every debit

A negative delta uses
```sql
UPDATE users SET balance = balance - ?
  WHERE id = ? AND balance >= ?
```
and checks `rowcount`. **Overdraft is impossible at the SQL layer.** Even a buggy caller cannot drive a balance negative.

## 3. Withdrawal is atomic with row creation

The balance debit and the `INSERT INTO withdrawals` happen in the same transaction. A user hammering the "Withdraw" button on two devices cannot create two payout rows against the same funds — the second one is rejected with `rowcount==0`.

## 4. Idempotent payments

`payments.payload TEXT UNIQUE`. Replayed webhooks, retried Telegram callbacks, re-runs of the hold sweeper — all no-op once the row is in.

## 5. Unique invoice payloads for Telegram Stars top-ups

When we issue an invoice, we append a `secrets.token_urlsafe(8)` nonce to the payload. Two top-ups of the same amount by the same user no longer collide on the UNIQUE constraint and never get silently dropped.

## 6. Cancel + refund is atomic

`cancel_task_with_refund` flips status and credits the advertiser balance in one transaction, with a guaranteed `task_refund_{id}` UNIQUE so re-running cancel is a no-op.

## 7. Capacity guard on task fulfilment

`UPDATE tasks SET done_slots = done_slots + 1 WHERE id = ? AND done_slots < total_slots`. A race past the quota is rejected; we never pay for a slot the advertiser hasn't reserved.

## 8. No float on monetary state

Stars are integers. TON is `REAL` but always rounded at boundaries; we never accumulate fractional drift inside the platform.

## 9. CSPRNG for lotteries

Giveaway picker, jackpot winner picker, Lucky Spin all use `secrets.SystemRandom`. Mersenne Twister is deterministic from its seed and unsuitable for payouts.

## 10. Initdata replay protection

Telegram Mini App `initData` is HMAC-verified **and** has a 24h freshness check on `auth_date`. A stolen `initData` blob cannot replay financial endpoints (`/miniapp/api/jackpot/buy`, `/miniapp/api/staking/open`, ...) past its expiry.
