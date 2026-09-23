# Workflow/Process Domain — Policies

Status: Draft — pending review
Ratified: No
Last updated: 2026-09-22
Provenance: see _qa/06-policies.qa.md
Built on: 01-definitions.md, 04-metadata-standards.md, cross-cutting/policies.md, cross-cutting/risk-tiers.md

## Extends Cross-Cutting Policies

This domain's resources are subject to CCP-1 (Metadata Completeness),
CCP-2 (Cost Attribution), and CCP-3 (Production Provisioning Approval)
from cross-cutting/policies.md, applied to this domain's own entity types
(04-metadata-standards.md). Not restated here.

## Domain-Specific Policies

### WFPOL-1 — Branch Protection Required on Default Branch
**Rule:** A Repository's Default Branch (04-metadata-standards.md) must
have a Branch Protection Rule requiring at least one Code Review
(`sysarch-code-review`) approval and a passing Pipeline Run before a
Pull Request can merge.
**Applies to:** All environments, Repository entity type.
**Enforcement:** Hard block.
**Rationale:** This is the mechanism that makes SAPOL-1/SAPOL-3/SAPOL-4's
hard blocks (System Architecture) actually unbypassable in practice — a
policy requiring a passing test gate means nothing if the branch it
targets has no protection forcing that gate to run before merge.

### WFPOL-2 — Deployment Gate Required Before Production Promotion
**Rule:** A Pipeline cannot promote a Release Candidate to Production
without passing every Deployment Gate configured for that environment
transition (05-conventions.md's Environment Promotion Flow diagram).
**Applies to:** Production environment, Pipeline entity type.
**Enforcement:** Hard block.
**Rationale:** This is the general mechanism policy underneath every
other domain's Production-bound hard blocks that named Workflow/Process
as a forward reference — System Architecture's SAPOL-4, Data Platform's
DPPOL-1 (where a Database migration is involved), Business Intelligence
/ Reporting's BIPOL-1 (where a report deploy is involved). Those policies
define *what* must pass; this one defines that *something* must gate
Production promotion at all.

### WFPOL-3 — IaC Apply Requires a Reviewed Plan
**Rule:** An IaC Apply targeting Production cannot execute without a
corresponding IaC Plan having been generated and reviewed first — no
direct, unplanned apply against Production.
**Applies to:** Production environment, Infrastructure as Code entity
type (any resource provisioned via IaC, across Infrastructure,
Networking, or Data Platform).
**Enforcement:** Hard block.
**Rationale:** Mirrors CCP-3's Production provisioning approval
requirement, applied specifically to the IaC path — Drift Detection
(`wf-drift-detection`) exists precisely because an out-of-band apply
bypassing this rule is a real failure mode this policy exists to prevent.

### WFPOL-4 — Post-Incident Review Required (Scaled by Severity)
**Rule:** Incident Severity (04-metadata-standards.md) determines whether
a Post-Incident Review is required:
- **Sev3/Sev4 (Low/Moderate impact):** Post-Incident Review optional, at
  the Owning Team's discretion.
- **Sev1/Sev2 (High impact):** Post-Incident Review required within a
  defined window after Resolved status (05-conventions.md's Incident
  Lifecycle diagram).
**Applies to:** All environments, Incident entity type.
**Enforcement:** Approval gate — Incident cannot be marked fully closed
without the review at Sev1/Sev2.
**Rationale:** Scaled by severity rather than uniform, consistent with
this framework's established pattern (System Architecture's SAPOL-5,
Business Intelligence / Reporting's BIPOL-3) of reserving mandatory
process for the higher-consequence cases rather than imposing uniform
overhead.

### WFPOL-5 — Emergency Change Requires Post-Hoc Review
**Rule:** An Emergency Change Request (Change Request Type = Emergency,
04-metadata-standards.md) may be executed before approval, but requires
review and formal approval within 24 hours after execution — the ITIL
Emergency Change pattern (00-standards-alignment.md).
**Applies to:** Production environment, Change Request entity type where
Type = Emergency.
**Enforcement:** Approval gate, timing-scoped (post-hoc rather than
pre-execution) — the only policy in this framework whose approval gate
runs after the action it gates, rather than before.
**Rationale:** An Emergency Change exists precisely for situations where
waiting for pre-approval would make things worse (e.g., during an active
Sev1 Incident) — CCPROC-4's break-glass override already covers bypassing
a *hard block*; this policy covers the distinct case of bypassing a
*normal approval sequence* for a legitimate operational reason, with the
same audit-trail discipline CCPROC-4 established.

---

**Cross-references:**
- WFPOL-2 is the general mechanism three other domains' Production hard
  blocks already assumed existed — SAPOL-4, DPPOL-1, and BIPOL-1 all
  described *what* gates Production; this policy is *that a gate
  mechanism exists at all*, closing the loop those three domains left
  open.
- WFPOL-4 and WFPOL-5 both key off severity/type classifications this
  domain owns (Incident Severity, Change Request Type) — the same
  "classification drives escalation" pattern used throughout this
  framework (Sensitivity Level, Risk Tier).
- WFPOL-5 is structurally unusual (post-hoc approval) — flagged
  explicitly rather than silently treated like every other approval gate,
  since it's a genuine departure worth a future reviewer noticing.

**Open items:**
- Who qualifies as reviewer/approver for each of these five policies is
  deferred to Access Rules (column 7), next.
- WFPOL-5's 24-hour window is a generalized default (same treatment
  Data/Metadata's DPOL-4 gave its 30-day Right to Erasure SLA) —
  explicitly adjustable per an org's own incident/change management
  practice, not asserted as a universal requirement.

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — 5 domain-specific policies plus inherited cross-cutting ones
- [x] Modular — each WFPOL stands alone
- [x] Easy to update — cross-cutting rules update once, apply here automatically
- [x] Easy to maintain — every policy traces to a specific term/field; WFPOL-2 explicitly closes three other domains' forward references
- [x] Easy to replace — enforcement mechanisms deferred to Procedures/Tooling where tool-specific
