# Failure modes in agent-built production systems

Every item here happened in a real system I run. Names are removed; the patterns are not. Each one ends with the guardrail that now prevents it, and where that guardrail lives.

## 1. The success that changed nothing
An update ran, the client library returned 200, the agent reported success. A row-level permission policy had filtered the row out of the statement, so zero rows changed.
**Guardrail:** every write checks its returned row count. Lives in the context file's Traps and the PR template.

## 2. The transcript was right, the audio was wrong
A text-to-speech pipeline produced personalised audio. A duplicated node in the workflow generated the message twice, so the file played it twice. Every text-level check passed, because the text was correct.
**Guardrail:** verify the output in its own medium. For audio, check the duration against the expected length; for images, look at the image. Lives in the spec's "How we will verify".

## 3. "Today" in the wrong time zone
Date logic used the server's local clock. Near midnight, scheduled items went out a day early or late. It recurred three times, in different files, written by different sessions.
**Guardrail:** one written rule (compute in the business time zone, store UTC) in the context file, so every new session inherits it.

## 4. The run log lied
A batch job's log reported every item produced. Several files on disk were missing or corrupt.
**Guardrail:** audit from the artefacts, not from the log. A small script that checks what actually exists is cheaper than one bad release.

## 5. Two sources, one deployment slot
Two repositories each carried a copy of the same serverless function. Whichever was deployed last won, silently, on a live path.
**Guardrail:** one owner per deployable. The non-canonical copy is replaced by a stub that points to the owner, so an agent cannot edit or redeploy it by accident.

## 6. Parallel sessions, one working tree
Several agent sessions worked in the same repository. One committed another's half-finished files.
**Guardrail:** `git status` before every commit and "commit only what you touched", in the context file. An append-only STATE log so parallel sessions never conflict on the shared record.

## 7. The scheduled job that could not authenticate
A database cron job read its credential from a runtime setting that is empty inside the scheduler. Every run "succeeded" at making the call; every call was rejected. The run history showed green for weeks.
**Guardrail:** judge scheduled jobs by the response they received, not by the scheduler's run status.

## The pattern underneath
None of these were model failures. They were verification failures: something reported success and nobody checked the thing itself. Agent speed makes that gap wider, which is why the gate and the verification step are the core of the model, not an add-on.
