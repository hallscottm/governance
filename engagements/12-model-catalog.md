# Engagements — Model Catalog

Status: Draft — pending review
Ratified: No
Last updated: 2026-09-23

Covers `eng-model-catalog-entry` (01-definitions.md). Resolves
09-open-decisions.md #8 (Harness already has Model Version Pin per
Agent, but not the decision rubric it should be set from).

Worth being precise about a difference from the Skill/Agent Library
(10, 11): Skills and Agent Templates are things this organization
*builds* (via the Factory, eventually). Models are not built in-house —
this is a curated list of externally available options, closer in
spirit to Harness's own Tooling column (08-harness/10-tooling.md) than
to a Factory output. Grouped alongside the other two registries because
it's the same shape of problem (a registry plus a lookup rule feeding
`model_version_pin`), not because it's built the same way.

## Model Catalog entry

```yaml
model_id: <slug>
provider: <frontier API | self-hosted/local>
capability_tier: frontier | mid | small
cost_profile: <ties to harness-cost-per-task tracking>
context_window: <ties to harness-context-window-budget>
data_residency: vendor-hosted | on-prem | other
approved_for: [risk tiers / domains this entry is cleared for]
status: approved | restricted | deprecated
```

## Selection Criteria

The decision rubric an Agent's `model_version_pin` is set from, not
asserted freehand: given an Engagement/Task's Risk Tier, data
sensitivity, and cost/latency budget, which Catalog entry fits. A
rubric (a small decision table), not code — kept in this file, reviewed
on the same cadence as the Catalog itself. No match → same Escalation
Path discipline as everything else in this framework: ask a human,
don't guess a model.

## Keeping the Catalog current

Three separate triggers, none of them "someone remembers to check":

- **Add** — same Build-on-Demand logic as Skills/Agents: a Selection
  Criteria lookup that finds no fit is the primary trigger
  (demand-driven), same Escalation Path discipline. A periodic review
  (quarterly, owned by Security/Compliance — see below) is the
  secondary, proactive trigger — catches a new frontier release before
  an Engagement stumbles on the gap.
- **Update** (a version bump on an already-approved model) — reuses
  Harness's own HPOL-2 (08-harness/06-policies.md) as-is: a Model
  Version Pin change requires a passing Eval Suite Run first, applied
  here to the Catalog entry itself rather than only a single Agent's
  pin. No new mechanism.
- **Deprecate** — three named triggers, never a hard delete
  (append-only, same discipline as `_qa` logs and Skill versioning): a
  provider-forced retirement (hard trigger, human executes on notice);
  a Behavioral Drift or repeated Eval Suite failure on a Catalog entry
  (parallels HPOL-4's automatic tightening — auto-flags for review,
  doesn't auto-remove); or superseded-and-unused (a newer entry exists
  and `used_by` is empty — safe, low-urgency cleanup). `status:
  deprecated` stops new Selection Criteria matches; Engagements that
  already reference it keep their historical record.

## Approver

`ccrole-security-compliance` approves new Catalog entries — consistent
with CCAR-3, where Security/Compliance sign-off is already required for
High-risk overrides. `ccrole-infrastructure-admin` is Consulted for
cost, not Approver, since data-residency/compliance is the dominant
risk, not spend.

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — one registry, one rubric, three named upkeep triggers
- [x] Modular — Catalog changes don't touch Skill/Agent Library mechanics
- [x] Easy to update — Add/Update/Deprecate each reuse an existing framework mechanism (Escalation Path, HPOL-2, HPOL-4) rather than inventing new ones
- [x] Easy to maintain — one approver role, one review cadence
- [x] Easy to replace — plain YAML + a decision table, no tooling dependency
