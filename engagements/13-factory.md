# Engagements — The Factory

Status: Draft — pending review
Ratified: No
Last updated: 2026-09-23

Covers `eng-factory-agent` (01-definitions.md) and how a new Skill
Library or Agent Library entry actually gets built — the piece every
registry so far (10, 11) assumed exists. Reviewed with the user in a
standalone design pass before being written here.

**Design goal:** add no new document type or schema. A Factory Run
turns out to be an ordinary Task Document; building the Factory means
naming one more Agent role and describing how existing fields (Task
lifecycle status, `approval_required`, Sandbox, Eval Suite) get used
for this specific case.

## Factory Agent

One role, fields mirror Harness's Agent schema exactly — same
discipline as the Vetting Agent and Engagement Planning Agent.

| Field | Value |
|---|---|
| Agent Type | Assistant — responds to a routed escalation, never initiates a build on its own |
| Capability Scope | Draft a candidate Skill or Agent Template (schema fields, prompt/logic) in `status: draft` only. Excludes: approving its own work, writing to Production, editing an existing `approved` Library entry in place — that's a new version, not an edit |
| Tool Permission Scope | Read: entire Anchor layer, the existing Skill/Agent Library (re-checks "close enough" wasn't missed — deliberate defense-in-depth against a missed Lookup, not wasted work), Sandbox (write, for testing). Write: Library store, `draft` status only |
| Escalation Path | Two consecutive Sandbox or Eval failures on the same candidate (see Failure & Retry, below) → escalate to a human: is the capability genuinely needed, or was the request itself off |
| Own Risk Tier | Low (drafting only, no Production execution) |
| Sandbox Tested | Required before org-wide trust, same as any Agent |
| Approval boundary | Drafts only. A human Approver signs off (CCAR-1/CCAR-2) before `status` flips to `approved` — never self-approves |

Pre-built like the Vetting Agent and Engagement Planning Agent — a
deliberate Build-on-Demand exception (10-skill-library.md), since it's
domain-agnostic infrastructure every build routes through, not a guess
about domain-specific work.

## Five stages, zero new schema

A Factory Run is an ordinary Task Document (`eng-task-document`) —
`task_id: factory-run-<slug>`, `engagement_type: Request / Ad Hoc`. The
requesting Task (the one that hit a Library gap) adds this Task's id to
its own `dependencies` list — already exactly how Task Document
expresses "blocked on." No `triggered_by` field needed.

| Stage | How it maps onto existing fields |
|---|---|
| **Draft** | Task `status: proposed` -> `in-progress`. `assigned_agent` = Factory Agent. Candidate Skill/Agent Template entry created with `status: draft` in the relevant Library. |
| **Sandbox** | Reuses HPOL-1 as-is (08-harness/06-policies.md) — the candidate's Capability Scope/Tool Permission Scope is exercised in Sandbox (`cc-sandbox`) before any Production-scoped grant. Result recorded in the Library entry. |
| **Eval** | An Eval Suite Run (`harness-eval-suite`) against the candidate. Reference recorded in the Skill Library entry's `eval_suite` field, or the Agent Library entry's `sandbox_tested` flag. |
| **Approve** | Task's own `approval_required: true`, `approved_by: <ccrole-approver instance>` fields — used exactly as designed. Factory Agent never fills `approved_by` itself. |
| **Register** | Library entry `status: draft` -> `approved`. Task `status: complete`, `result.output_location` = the new `skill-lib/...` or `agent-lib/...` id, `result.outcome_summary` = one line. |

**Standing Factory Project:** deferred, not created now. Consistent
with Build-on-Demand — a Maintenance-type wrapper Project can group
Factory Run Tasks for aggregate visibility whenever there's enough
volume to justify it; a standalone Factory Run Task works fine on its
own until then.

## Failure & retry

A Factory Run Task carries one additional field, specific to this
Engagement Type (not added to the generic Task Document template —
Factory Runs are the only Task that needs it):

```yaml
attempt_count: <N>   # increments on each Sandbox or Eval failure for this candidate
```

First failure: Factory Agent revises the draft and retries — ordinary
iteration, `attempt_count: 1`, no escalation. Second consecutive
failure (`attempt_count: 2`): Escalation Path trips — stop retrying,
ask a human whether the underlying need is real. Mirrors HPOL-4's
automatic-tightening logic (repeated failure -> escalate) without a new
mechanism, just an explicit counter instead of an implicit one.

Approver rejection (distinct from a Sandbox/Eval failure — it passed
the automated gates but a human says no): Task goes to `status:
blocked`, not `complete`. Library entry stays `draft`, never
auto-promoted. Same one-way gate as everywhere else in this framework —
nothing reaches `approved` without a human signing off.

## Worked example

Before `skill-lib/build-bi-report-v3` existed (referenced in
08-worked-example.md), it had to be built once:

```yaml
task_id: factory-run-build-bi-report-v1
parent_project: null
engagement_type: Request / Ad Hoc
status: complete
assigned_agent:
  role_name: Factory Agent
  capability_scope: draft Skill candidates only
attempt_count: 1
dependencies: []
approval_required: true
approved_by: <ccrole-approver instance>
result:
  output_location: skill-lib/build-bi-report-v3
  completed_date: <date>
  outcome_summary: Registered after 1 Sandbox pass, 1 Eval Suite pass, human approval
```

The original BI report Task that needed this listed
`factory-run-build-bi-report-v1` in its own `dependencies` and waited.
Once registered, every Project since — including `dq-metrics-dashboard`
— just references `skill-lib/build-bi-report-v3` directly. No second
Factory Run unless a new version is genuinely needed.

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — one Agent role, one Task-Document convention, one new field
- [x] Modular — Sandbox/Eval/Approve stages are each an existing, independently-owned mechanism
- [x] Easy to update — a new Library entry is additive; nothing here regenerates
- [x] Easy to maintain — reuses HPOL-1, HPOL-4's logic, CCAR-1/CCAR-2, and Task Document's own lifecycle rather than inventing parallel review machinery
- [x] Easy to replace — plain YAML convention on an existing document type, no tooling dependency
