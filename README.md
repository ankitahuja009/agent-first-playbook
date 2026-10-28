# Agent-first engineering playbook

How to run a codebase where AI coding agents (Cursor, Claude Code, and the rest) write most of the code, and humans still own what ships.

This is the operating model I use on my own production systems: several mobile and web apps, a Postgres backend and a handful of integrations, built and run largely through agents. The tools change every quarter. What does not change is the set of decisions a team has to make about where the human stays in the loop. This repo writes those decisions down as templates you can drop into a repository today.

## The model in five rules

1. **The spec is the artefact humans own.** Agents implement; people write the problem, the acceptance criteria and the "do not" list. A change without a spec is a guess.
2. **One context file per repo is the constitution.** Every agent session reads it first. It holds conventions and, more importantly, the traps: the things that already broke once. When an agent repeats a mistake, the fix goes in this file, not in a chat.
3. **State is written down, append-only.** A dated log of what changed and why. Parallel sessions (human or agent) can all append to it without conflict, and the next session starts from facts instead of memory.
4. **Production has a gate the agent cannot skip.** No direct pushes to a branch that deploys. Short-lived branch, pull request, review, merge. Agent speed is only useful if review keeps up, so the gate is a design constraint, not bureaucracy.
5. **Verify against the running system, not the agent's report.** "Tests pass" and "done" are claims. Open the app, read the row back, play the audio file. The most expensive bugs I have seen were reported as successes.

## What's in here

| Path | What it is |
|---|---|
| [`templates/CONTEXT.md`](templates/CONTEXT.md) | The repo constitution. Rename to `CLAUDE.md`, `AGENTS.md`, or a Cursor rule (see below). |
| [`templates/STATE.md`](templates/STATE.md) | Append-only change log, with the rules that keep it useful. |
| [`templates/SPEC.md`](templates/SPEC.md) | One-page spec an agent can implement from and a reviewer can check against. |
| [`.github/pull_request_template.md`](.github/pull_request_template.md) | The PR checklist that encodes rule 4 and rule 5. |
| [`examples/cursor-rules/project.mdc`](examples/cursor-rules/project.mdc) | The same constitution as a Cursor project rule. |
| [`hooks/state_check.py`](hooks/state_check.py) | Session hook: prints branch, uncommitted files and the last STATE entry at start; warns at stop if files changed but STATE did not. |
| [`docs/failure-modes.md`](docs/failure-modes.md) | Real failure patterns from agent-built production systems, and the guardrail for each. |
| [`docs/adoption-30-days.md`](docs/adoption-30-days.md) | How to roll this out inside an existing engineering team, measured at day 30. |

## Quick start

```bash
# in your repository
cp templates/CONTEXT.md ./CLAUDE.md          # or AGENTS.md, or .cursor/rules/project.mdc
cp templates/STATE.md   ./docs/STATE.md
mkdir -p .github && cp .github/pull_request_template.md .github/
python hooks/state_check.py start            # try the hook by hand
```

Fill in the context file's **Traps** section first. If you cannot think of one, wait a week; you will have three.

## Wiring the hook into Claude Code

```json
{
  "hooks": {
    "SessionStart": [{ "hooks": [{ "type": "command", "command": "python hooks/state_check.py start" }] }],
    "Stop":         [{ "hooks": [{ "type": "command", "command": "python hooks/state_check.py stop" }] }]
  }
}
```

Put this in `.claude/settings.json`. In Cursor, keep the same text in a project rule and run the script from a task or pre-commit hook.

## Why this exists

Most AI pilots that stall do not stall on the model. They stall because nobody agreed what done looks like, the agent could not see the context it needed, and there was no gate between a confident answer and production. These templates are the smallest set of habits I have found that fixes all three.

## Licence

MIT. Use it, change it, send improvements.
