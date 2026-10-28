# <Repo name>: context for agents

Every agent session reads this file first. Keep it short enough to read in a minute.
It holds what is true of **this repo only**. Cross-repo rules live one level up.
If this file and the spec disagree, the spec wins. Say so and stop; do not quietly pick one.

## What this repo is

One paragraph: what it does, who uses it, where it runs, how it deploys.

## How to run it

```bash
npm install
npm run dev        # local
npm test           # must pass before a PR
```

## Conventions

- Language, framework, folder layout, naming.
- Where business logic lives, and where it must not.
- How dates and time zones are handled (write the rule down; it will break otherwise).
- What "done" means here: tests, types, a screenshot, a row read back.

## Traps (the most valuable section)

Each trap is something that already went wrong once. One line for the symptom, one for the rule.

- **Writes that silently do nothing.** A permission policy can filter a row out of an update, so the call "succeeds" and changes nothing. *Rule: check the returned row count on every write.*
- **"Today" computed in the server's time zone.** *Rule: compute dates in the business time zone explicitly; store UTC, render local.*
- **<your trap>** *Rule: <the check that prevents it>.*

## Never

- Push to the branch that deploys to production. Branch, PR, review.
- Commit secrets. Public keys are fine; service or admin keys never.
- Edit generated files or migrations by hand. Use the tool that generates them.
- Report "done" without verifying against the running system.

## Before you commit

1. `git status`. Commit only what you touched; other sessions may be working here too.
2. Append one dated line to `docs/STATE.md`.
3. Open a PR with the template filled in.
