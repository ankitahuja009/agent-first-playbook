# Rolling this out in an existing team: 30 days

The measure is what is different at day 30, not how many templates were copied. Pick one repository and one team. Spread only what worked.

## Days 1 to 5: see the real environment
- Sit with the engineers on real tickets. Note where agents are already used, where they are banned, and why.
- Find the last three incidents. Each one is a candidate trap for the context file.
- Agree one metric the team already cares about: lead time, review wait, escaped defects, or rework.

## Days 6 to 10: write the constitution together
- Draft the context file **with** the team, starting from their incidents. A file written for them is ignored; a file written by them is read.
- Add the PR template. Keep it to what reviewers actually check.
- Start STATE.md with one entry: today's baseline for the chosen metric.

## Days 11 to 20: one feature, end to end, agent-first
- Pick a real, bounded feature. Write the one-page spec before any code.
- Let the agent implement. Review against the spec, verify against the running system.
- Every mistake the agent repeats becomes a trap entry the same day.

## Days 21 to 30: make it theirs
- A team member, not the facilitator, runs the second feature.
- Wire the session hook so STATE is checked automatically.
- Compare the metric with day 1. Write the result, good or bad, in STATE.

## What usually goes wrong
- **"Agents write sloppy code."** Often true without a context file. Answer with the first repeated mistake that disappears once it is written down.
- **"The docs will rot."** The context file only holds traps and rules, not tutorials. Traps do not rot; they get added to.
- **"This slows us down."** For the first feature, yes. Measure the second.
- **Scope creep under deal pressure.** The spec's "out of scope" list exists for this. Protect it.

## Leaving it behind
The engagement is done when the team adds a trap to the context file without being asked.
