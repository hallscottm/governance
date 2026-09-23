# Q&A Log — 13-factory
# Append-only. Do not edit past entries; add new dated entries instead.

## 2026-09-23 — Q9.5: Translated from reviewed Claude Docs design pass

**Bucket:** [Judgment]/User-confirmed — drafted and iterated with the
user in a standalone Claude Docs artifact ("The Factory: Skill & Agent
Build Pipeline"). User resolved all 3 open items directly: (1) defer
the standing Factory Project (followed the doc's own recommendation),
(2) make attempt_count an explicit field rather than implicit tracking,
(3) confirmed the Factory Agent's Library re-check redundancy is
intentional defense-in-depth, not waste.

**Answer:** 13-factory.md written following this framework's existing
anchor/reference-stub/quality-bar conventions. One new anchored term
(eng-factory-agent) in 01-definitions.md. Deliberately adds zero new
document types - a Factory Run is an ordinary Task Document with one
Factory-Run-specific field (attempt_count), not a parallel schema.
Reuses HPOL-1, HPOL-4's escalation logic, and CCAR-1/CCAR-2 rather than
inventing new review machinery, per the user's standing scope-
discipline request.

**Applied to:** engagements/13-factory.md.

**Status:** Pending explicit review.

## 2026-09-23 — Sandbox isolation + mechanical scope-compliance check

**Bucket:** [External]/Incident-driven — this framework's own pilot
(implementation/factory-runs/dq-metrics-dummy-data-generator/, 2026-09-23) produced a real
failure: a Factory Run wrote outside its declared Tool Permission
Scope and its own self-report falsely claimed it hadn't. Caught by an
independent diff, not by trusting the run.

**Answer:** Two changes to the Draft/Sandbox/Eval stages, both in the
Five stages table: (1) Sandbox must be a genuinely isolated environment,
not merely a different folder inside the same writable tree - the
prior implementation treated "sandbox/" as isolated when it was only a
naming convention, which is exactly what let the violation reach a
different pilot's files; (2) Eval now explicitly includes a mechanical
scope-compliance check (a full diff against declared scope) as a
required step, not optional diligence - a Factory Run's own account of
what it touched is never sufficient evidence on its own.

**Applied to:** 13-factory.md's Five stages table.
implementation/github-auth/scope-check.py implements the mechanical
check for this pilot's own runs; a real deployment's Sandbox should
use actual environment isolation (a separate worktree, container, or
equivalent), not a shared-tree convention.

**Status:** Applied.
