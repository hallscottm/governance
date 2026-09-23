# Harness Domain — Procedures (SOPs)

Status: Draft — pending review
Ratified: No
Last updated: 2026-09-23
Provenance: see _qa/08-procedures.qa.md
Built on: 06-policies.md, 07-access-rules.md, cross-cutting/procedures.md

## Extends Cross-Cutting Procedures

CCPROC-1 (Production Provisioning Request & Approval), CCPROC-2
(Metadata Completeness Validation), CCPROC-3 (Cost Attribution
Validation), and CCPROC-4 (Break-Glass Override) apply to this domain's
resources without restatement — see cross-cutting/procedures.md.

## Domain-Specific Procedures

### HPROC-1 — Production Tool Permission Scope Widening
**Executes:** HPOL-1, HAR-1
**Steps:**
1. A requested Tool Permission Scope change adding a Production-scoped
   grant is defined against the Agent's current Capability Scope.
2. The exact combination is exercised in a Sandbox (`cc-sandbox`); its
   Sandbox Tested Flag (04-metadata-standards.md) is set only on a
   successful run.
3. An Eval Suite Run is executed against that combination; results are
   recorded as the Agent's Latest Eval Suite Run Reference.
4. On a passing Sandbox test and Eval Suite Run, the change is routed to
   Owning Team Lead (plus Security/Compliance at High Risk Tier) per
   HAR-1 for approval.
5. On approval, the Tool Permission Scope grant takes effect in
   Production; on rejection, the Requester is notified with the reason
   and the Agent's Production-scoped grant remains unchanged.

### HPROC-2 — Model Version Pin Change
**Executes:** HPOL-2
**Steps:**
1. A new Model Version Pin is proposed for an Agent.
2. An Eval Suite Run executes against the new version, producing fresh
   Eval Metric results.
3. For a Production-environment Agent, the change is blocked (HPOL-2)
   until the Eval Suite Run passes; for Dev/Staging, the change may
   proceed with the run flagged as recommended-but-incomplete.
4. On a passing run, the Model Version Pin updates and the Behavioral
   Drift baseline resets against the new version's Eval Metric results.

### HPROC-3 — Human-in-the-Loop Gate Resolution
**Executes:** HPOL-3, HAR-2
**Steps:**
1. An Autonomous- or Multi-Agent-type Agent proposes an action.
2. Its Risk Tier is computed (09-risk-tiers.md); at High Risk Tier, the
   action routes to a Human-in-the-Loop Gate via the Agent's Escalation
   Path before executing (HPOL-3).
3. The gate is resolved by the Owning Team Lead (plus Security/
   Compliance at High tier, per HAR-2) — never by the Agent itself,
   under any circumstance (CCAR-1, HAR-2).
4. An approval produces a recorded Approval Gate entry
   (`harness-approval-gate`) and the action executes; a denial is logged
   and the action does not execute.

### HPROC-4 — Guardrail Violation Response
**Executes:** HPOL-4
**Steps:**
1. A Guardrail (Content Filter or Action Allowlist/Denylist) detects a
   violation during an Agent Run.
2. The Agent's Rate Limit automatically tightens (HPOL-4) — this step
   requires no human approval, since it is a containment action, not a
   capability grant.
3. The violation is logged to the Agent Trace/Transcript and flagged for
   Owning Team Lead review.
4. On review, the Owning Team Lead either restores the prior Rate Limit
   (false positive or resolved cause) or escalates to a Capability Scope
   revocation (a heavier action than this procedure covers, routed
   through HPROC-1's reverse case).
5. If the violation is also classified as an Agent-Caused Incident
   (`harness-agent-incident`), it feeds Workflow/Process's Post-Incident
   Review (`wf-postmortem --[consumes]--> harness-agent-incident`,
   03-ontologies.md) and this domain's own Eval Suite as a candidate new
   test case.

### HPROC-5 — Guardrail Override and Post-Hoc Review
**Executes:** HPOL-5, HAR-3
**Steps:**
1. A situation is identified where an Agent's Guardrail must be bypassed
   immediately (e.g., a time-critical action a Human-in-the-Loop Gate is
   too slow to resolve).
2. Infrastructure Admin and Security/Compliance jointly authorize the
   Override/Break-glass (HAR-3/CCAR-3 — no single-approver path exists
   for this override, unlike other domains' break-glass patterns).
3. The override executes immediately; it is logged with which Guardrail
   was bypassed, who approved it, and the stated reason, same audit
   discipline as CCPROC-4.
4. Within 24 hours (HPOL-5's window), the override is submitted for
   post-hoc review; the review outcome (confirmed appropriate, or
   flagged for Capability Scope/Guardrail follow-up) is logged.

---

**Open items:** none for this pass — consistent with every other
domain's Procedures column, these were designed to close the open items
surfaced during Policies/Access Rules rather than carry them forward.

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — 5 domain-specific procedures plus inherited cross-cutting ones
- [x] Modular — HPROC-1 through 5 stand alone
- [x] Easy to update — cross-cutting procedures update once, apply here automatically
- [x] Easy to maintain — every procedure traces to a specific HPOL-/HAR- item, and to 05-conventions.md's Escalation Flow diagram
- [x] Easy to replace — no tooling specifics baked in; execution mechanisms deferred to Tooling (column 10)
