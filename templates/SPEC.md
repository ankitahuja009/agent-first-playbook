# Spec: <feature name>

One page. An agent implements from it; a reviewer checks the PR against it.

## Problem
Who has it, what happens today, why it matters. Two or three sentences.

## Outcome
What is true when this is done, in terms a user would notice.

## Acceptance criteria
Each one testable by someone who did not write the code.
- [ ] Given <state>, when <action>, then <observable result>.
- [ ] ...

## Out of scope
What this change must not touch. Agents expand scope by default; this list is the brake.

## Constraints and traps
Data that must not be lost, systems that must not be called in test, time zone rules, rate limits, cost per call.

## How we will verify
The exact check against the running system: the screen to open, the row to read back, the file to play.

## Open questions
Anything a human must decide before an agent starts.
