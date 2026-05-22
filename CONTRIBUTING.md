# Contributing

Thanks for taking interest. This repository hosts public **docs and examples** for the Stars Cash Flow platform — the production code is closed-source and lives elsewhere. That means the surface we accept contributions to is small but well-defined:

| Welcome | Not in scope here |
|---|---|
| Doc fixes (typos, broken links, clarifications). | Feature requests for the bot / API itself — open an issue, we'll triage. |
| New examples in `examples/` (other languages, frameworks, edge cases). | Pull requests against private platform code (we'll close — those go to the operator). |
| Wiki page improvements. | Anything that requires reading the production source (we don't ship it). |
| README polish, banner / logo improvements. | Pricing changes — pricing is operator-set, not negotiable via PRs. |

## How to contribute

1. **For a typo / small doc fix** — just open a pull request. No issue needed.
2. **For a new example** — drop the file in `examples/<lang>/` with a short header comment explaining how to run it. Keep dependencies minimal (standard library preferred).
3. **For a larger doc / Wiki rework** — open an issue first so we agree on scope.
4. **For a security report** — please **don't open a public issue**. See [SECURITY.md](SECURITY.md).

## Style

- Docs are in English, second-person ("you create an order", not "the user creates an order").
- Code in examples is `black`-formatted (Python), `shfmt`-formatted (shell). No project-wide linter is enforced — keep it readable.
- API examples target the real endpoint at `https://api-stars.ros.media/api` and should be runnable as written (use `YOUR_API_KEY` as the placeholder).
- Mermaid diagrams are preferred for sequence / flow visuals — GitHub renders them natively.

## Commit style

Conventional-ish: `docs: …`, `examples: …`, `chore: …`. One concern per commit. Squash on merge is fine.

## Code of conduct

Be polite. Be specific. Argue with the idea, not the person. If you wouldn't say it across the table to a colleague, don't say it here.

We follow the [Contributor Covenant 2.1](https://www.contributor-covenant.org/version/2/1/code_of_conduct/) for moderation. Contact: `security@ros.media`.
