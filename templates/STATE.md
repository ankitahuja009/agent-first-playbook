# State

Where this repo stands. **Append-only**: add a dated entry at the bottom for every change that ships, every decision, every discovered trap. Never rewrite an old entry; correct it with a new one.

Why append-only: several people and agents work in parallel. Appending never conflicts, and the history of *why* survives. The next session reads the last few entries and starts from facts.

## Rules

- One entry per change, newest last. Date first, in the team's time zone.
- Say what changed, why, and how it was verified. "Fixed X" is not an entry; "Fixed X, verified by Y" is.
- A decision recorded only here will not be found. If it changes how code must be written, also put it in the context file. If it changes what the product does, also update the spec.
- Unverified work is labelled as such.

## Entries

### YYYY-MM-DD: <one-line headline>
What changed, why, how it was verified. Links to the PR and any spec section.
