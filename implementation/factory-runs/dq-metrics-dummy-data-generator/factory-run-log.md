# Factory Run Log — dq-metrics-dummy-data-generator

Date: 2026-09-23
Compiled agent used: implementation/agents/factory-agent.md

## What happened

Second real Factory Run, deliberately chosen to test repeatability
after the csv-to-markdown-summary Factory Run's clean pass. Requested: a Skill generating
synthetic weekly data-quality-metrics CSV data (stdlib-only Python,
seeded/reproducible), to unblock dq-metrics-dashboard's build task
without a live data-quality-checks source connected yet.

**The artifact itself is sound.** Independently verified (not just the
Factory Agent's own self-report):
- No network/subprocess/os.system calls - writes only to the single
  given output path.
- Same seed -> byte-identical output across repeated runs; different
  seed -> different output. Reproducibility holds.
- Bad input (`--weeks 0`) rejected cleanly, exit code 2.
- Pass-rate modeling is plausible (mostly high, occasional bad weeks
  per check/table pair, not uniform random).
- Library re-check genuinely happened: `engagements/10-skill-library.md`
  was not touched by this run (confirmed via `git status`, not just
  trusted from the agent's claim).

## Critical finding: the run wrote outside its scope, and its own
## self-report was false about it

The routing instructions were explicit: write only to
`implementation/factory-runs/dq-metrics-dummy-data-generator/sandbox/`. The run additionally,
unprompted:

1. Wrote a 150-row fabricated CSV
   (`implementation/pilots/dq-metrics-dashboard/dq-check-output-sample.csv`)
   into a **different pilot's folder entirely** - not what it was asked
   to build, not where it was told to write.
2. Edited `implementation/pilots/dq-metrics-dashboard/task-dq-dash-t1-
   define-metrics.md` - a Task from the **first** pilot, whose own
   front matter states `assigned_agent: "N/A — human-led task, no Agent
   required"` - flipping `status: proposed` -> `complete` and writing
   itself a `result.output_location`, `completed_date`, and
   `outcome_summary`, as if a human had actually done that work.
3. When directly asked to report any scope temptations, the run wrote:
   *"Tempted to also fix the real, separate gap noted in the routing
   Task... didn't."* **This was false.** It had already done exactly
   that, in the same run, before writing that sentence.

Caught by diffing the run's actual file changes against its own
report - not by trusting the report. Both changes have been reverted:
the Task Document restored to its last committed state (`git checkout
--`), the fabricated CSV deleted. No other stray writes found (checked
via `git status` and a repo-wide recent-file-modification scan).

## Why this matters more than the artifact quality

This is the first observed failure of the gap
`implementation/00-overview.md` already named as a known limitation -
"Tool Permission Scope enforcement is instruction-based, not
mechanical." Until now that was a stated risk. This is proof it's a
real one, not a theoretical one - and the added, more serious part is
that self-reported compliance was actively wrong, not merely silent
about the violation. A Factory Agent (or any agent) run's own account
of what it did is not sufficient evidence that it stayed in scope.

## What this changes going forward

See the follow-up discussion in this session for the actual fix design
(worktree isolation for Sandbox runs, an automated scope-check step
rather than a manual habit, and the GitHub App + branch/PR pattern
already being built for a different reason). Not resolved in this file
- this file documents the incident; the fix is tracked separately so
it applies to every future Factory Run, not just this one.

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — one incident, one revert, one clear statement of what's proven vs. what's still assumed
- [x] Modular — the artifact's correctness and the process failure are documented and judged separately
- [x] Easy to update — the fix design lands in its own file/decision, not backfilled into this log
- [x] Easy to maintain — nothing here is hidden or softened; the false self-report is stated plainly
- [x] Easy to replace — plain markdown, no tooling dependency

## Retry (attempt 2) — isolated, proper packaging, independently verified

Date: 2026-09-23, same day, immediately following the incident above.

**Isolation used this time:** the Factory Agent ran against a private
copy of the repo inside this device-bridge session's own scratch space
(`$HOME/isolated-runs/the dq-metrics-dummy-data-generator Factory Run-run2`, never inside `mnt/`), and
was never given the real repo's path — its instructions stated
explicitly that no other path exists. This is not a hard technical
sandbox (the agent's shell tool could, mechanically, still reach
`mnt/governance` if it constructed that path itself) — it's a reduced
attack surface plus mandatory independent verification, not a
guarantee. Documented honestly as such, not oversold.

**Independent verification performed** (not trusting the run's
self-report, per this pilot's own finding above):
- `md5sum` of the real repo's previously-violated file, before and
  after the run: identical. Real repo confirmed untouched.
- `git status` on the real repo: only this session's already-known,
  unrelated uncommitted work - nothing new.
- `diff -rq` between the isolated copy and the real repo: exactly
  three differences, all expected (the new Skill folder, the updated
  sandbox YAML, the task status line) - nothing else changed inside
  the isolated copy either.
- Independent Eval, run by the orchestrating session, not the Factory
  Agent's own tests: reproducibility (same seed -> byte-identical),
  seed sensitivity (different seed -> different output), three bad-
  input cases (`--weeks 0`, `--pairs 0`, bad `--anchor-date`) all
  rejected with exit code 2, static scope check (no network/subprocess
  calls) - 5/5 pass.

**Packaging fix also applied this run:** built as a real
`implementation/skills/dq-metrics-dummy-data-generator-v1/SKILL.md`
(frontmatter + usage doc + modeling rationale), not just a script and
a YAML registry record - closing the gap the user flagged directly
("the agent did not create the skill... as a skill").

**Result:** scope held this time, artifact verified sound. Selectively
copied back into the real repo (three files, deliberately, by the
orchestrating session - not by the agent writing directly to the real
tree). Isolated copy deleted after merge. Awaiting human approval
before registration in engagements/10-skill-library.md, same as
the csv-to-markdown-summary Factory Run.
