# Security Policy

## Responsible disclosure

If you discover a security vulnerability — please **do not** open a public GitHub issue.

Instead, contact us through one of these channels:

- **Email:** [security@ros.media](mailto:security@ros.media)
- **Telegram:** message [@StarsCashFlowbot](https://t.me/StarsCashFlowbot) → "Поддержка / Support" → mark the conversation as "Security".

We aim to acknowledge new reports within **48 hours** and provide a fix or remediation plan within **14 days** for confirmed issues.

## Scope

In scope:

- Telegram bot [@StarsCashFlowbot](https://t.me/StarsCashFlowbot) — money flows, hold logic, withdrawal, verification logic.
- Mini App and web cabinet on `https://api-stars.ros.media/`.
- Reseller API at `https://api-stars.ros.media/api`.
- TON Connect manifest and proof verification.
- Landing site at `https://stars.ros.media/`.

Out of scope:

- Best-practice findings without a concrete exploit (TLS hardening suggestions, header hardening, generic CSP recommendations).
- Volumetric DDoS, social-engineering of platform staff, spam-protection bypass for outbound notifications.
- Findings on subdomains not listed above.

## Safe harbour

If you act in good faith, follow this policy, and don't degrade availability or exfiltrate user data beyond proving the issue, we won't pursue legal action.

## Hall of fame

We're happy to credit reporters publicly in this file once a fix is shipped, unless you'd prefer anonymity.
