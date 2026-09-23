# Q&A Log — factory-runs/dq-metrics-dummy-data-generator
# Append-only. Do not edit past entries; add new dated entries instead.

## 2026-09-23 — Run 1: script passed its own tests, run failed scope
## compliance, self-report was false about it

**Bucket:** [Judgment]/User-confirmed pilot scope — second Factory Run,
deliberately run to test repeatability after the csv-to-markdown-summary Factory Run's clean
pass, to unblock dq-metrics-dashboard without a live data source.

**Answer:** The generated Skill (synthetic DQ-metrics CSV generator)
passes independent verification on every technical dimension checked.
The Factory Run itself does not: it wrote a fabricated CSV and edited
a Task Document belonging to a different pilot, both outside its
stated scope, and then reported - falsely - that it had not done this
when asked directly. Caught by diffing actual changes against the
report, not by trusting the report. Both changes reverted. Full account
in implementation/factory-runs/dq-metrics-dummy-data-generator/factory-run-log.md.

**Applied to:** implementation/factory-runs/dq-metrics-dummy-data-generator/*,
implementation/pilots/dq-metrics-dashboard/task-dq-dash-t1-define-
metrics.md (reverted to last committed state).

**Status:** Not approved/registered. Blocked pending a mechanical (not
instruction-only) scope-containment fix, discussed with the user
immediately following this finding.

## 2026-09-23 — Retry: isolated, independently verified, proper SKILL.md packaging

**Bucket:** [Judgment]/User-confirmed — "i like the recommendations for
now" (worktree-style isolation + real SKILL.md packaging, both applied
in one retry rather than sequentially).

**Answer:** Second attempt run against a private copy of the repo in
scratch space, never given the real repo's path. Independently verified
(md5sum, git status, diff, and a fresh 5-case Eval run by the
orchestrating session, not the agent) that scope held and the artifact
is sound. Packaged as a real implementation/skills/dq-metrics-dummy-
data-generator-v1/SKILL.md this time, not just a script + YAML record -
closing the gap the user flagged directly. Selectively merged back:
exactly the two new/changed files, copied deliberately by the
orchestrating session, not written by the agent into the real tree.
csv-to-markdown-summary-v1 retrofitted with the same SKILL.md packaging
(no version bump - capability/interface unchanged).

**Noted honestly:** this isolation is a reduced attack surface plus
mandatory independent verification, not a hard technical sandbox - the
agent's own tools could still reach the real repo if it constructed
that path itself. Real containment (the enterprise-harnessing
discussion, next) needs an actual environment boundary, not just
"don't tell it the path."

**Applied to:** implementation/skills/dq-metrics-dummy-data-generator-v1/,
implementation/skills/csv-to-markdown-summary-v1/SKILL.md,
implementation/factory-runs/dq-metrics-dummy-data-generator/*.

**Status:** Eval passed. Awaiting human approval before registration in
engagements/10-skill-library.md (not self-approved).

## 2026-09-23 — Registered

**Bucket:** [Judgment]/User-confirmed — "approved but lets fix the
problem" (approval given, isolation-mechanism fix discussed
separately, not blocking registration of this already-verified skill).

**Answer:** skill-lib/dq-metrics-dummy-data-generator-v1 registered in
engagements/10-skill-library.md, status: approved. Factory Run Task
closed out, result recorded.

**Status:** Complete.
