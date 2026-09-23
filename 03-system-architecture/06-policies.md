# System Architecture Domain — Policies

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

### SAPOL-1 — Backward Compatibility Required (Production APIs)
**Rule:** A Production API cannot ship a breaking change (per
`sysarch-backward-compatibility`) without a corresponding MAJOR version
increment (`sysarch-semver`) and a new version identifier
(05-conventions.md's `/v<major>/` pattern).
**Applies to:** Production environment, API entity type.
**Enforcement:** Hard block.
**Rationale:** Explicitly chosen as a hard block — an undetected breaking
change in Production is a direct consumer-facing failure, the same
severity class as Networking's NPOL-1/NPOL-2.

### SAPOL-2 — Database Schema Migration Review (moved 2026-09-22)
**Moved to Data Platform** as DPPOL-1 (04-data-platform/06-policies.md) —
the "candidate for moving" flagged when this policy was first drafted has
now happened, in the same pass that built out Data Platform's remaining
columns. A Service's Production deployment still depends on its
Database's migrations passing this gate (see SAPOL-4/SAPROC-4's test
gate, which is a separate, sequential concern) — this domain references
DPPOL-1 rather than restating it.

### SAPOL-3 — Managed Secret Storage Required
**Rule:** Application Secrets (`sysarch-application-secret`) must be
stored and retrieved via managed secret storage; embedding a secret in
source code, a Build Artifact, or a Container Image is prohibited.
**Applies to:** All environments (a Dev secret leaked in source control
is still a real exposure), Service/API/Database entity types.
**Enforcement:** Hard block.
**Rationale:** Explicitly chosen as a hard block — consistent with OWASP
ASVS baseline requirements and Networking's NPOL-2 precedent for
well-understood, severe risk categories.

### SAPOL-4 — Automated Tests Must Pass Before Production Deployment
**Rule:** A Release (`sysarch-release`) cannot be deployed to Production
unless its associated automated tests (Unit Test, Integration Test —
`sysarch-unit-test`, `sysarch-integration-test`) have passed. This policy
asserts the requirement only — the mechanism that enforces it is
Workflow/Process's Deployment Gate (`wf-deployment-gate`), specifically
its own WFPOL-2 general Production-promotion gate requirement
(07-workflow-process/06-policies.md).
**Applies to:** Production environment, Service/Application/API entity
types.
**Enforcement:** Hard block, mechanism resolved 2026-09-22 — see
Workflow/Process's Tooling column (07-workflow-process/10-tooling.md,
CI/CD Pipeline Platform category).
**Rationale:** Explicitly chosen as a hard block — consistent with
SAPOL-1's treatment of Production-bound changes; a specific test coverage
threshold is deliberately not set here (no bounded, defensible number
without org-specific input), left to Workflow/Process or the Owning Team.

### SAPOL-5 — Public-Facing Service Security Baseline (Scaled by Risk Tier)
**Rule:** A publicly internet-facing Service or API must meet an OWASP
ASVS verification level scaled by its Risk Tier (09-risk-tiers.md):
- **Low:** ASVS Level 1.
- **Moderate:** ASVS Level 2.
- **High:** ASVS Level 3.
**Applies to:** Any environment, Service/API entity types configured for
public exposure (cross-reference: Networking's NPOL-3 public-exposure
approval gate applies to the same resources from the network-boundary
side).
**Enforcement:** Approval/verification gate — specific verification
method (manual review, automated scan) deferred to Procedures (column 8)
and Tooling (column 10).
**Rationale:** Explicitly chosen to scale by Risk Tier, mirroring OWASP
ASVS's own tiered design and SAPOL-2/Infrastructure's precedent, rather
than a single uniform baseline.

---

**Cross-references:**
- SAPOL-5 and Networking's NPOL-3 both govern public-facing exposure,
  from different domains — SAPOL-5 covers the service's own security
  posture, NPOL-3 covers the network-boundary approval to expose it at
  all. Neither restates the other.
- SAPOL-5 scales by Risk Tier, applied proactively from the start
  (unlike Infrastructure's POL-2/POL-3, which were retrofitted after Risk
  Tiers was drafted) — Risk Tiers already existed as a cross-cutting
  concept by the time this column was drafted. SAPOL-2 (now DPPOL-1,
  moved to Data Platform 2026-09-22) shared this same proactive-scaling
  treatment at the time it was drafted here.

**Open items:**
- Who performs the SAPOL-5 verification is deferred to Access Rules
  (column 7), next. (Who qualifies as reviewer for the former SAPOL-2 is
  now Data Platform's Access Rules question — see
  04-data-platform/07-access-rules.md's DPPAR-1.)
- (Resolved 2026-09-22) SAPOL-4's enforcement mechanism is
  Workflow/Process's Deployment Gate/WFPOL-2 and CI/CD Pipeline Platform
  category — see 07-workflow-process/06-policies.md and 10-tooling.md.

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — 5 domain-specific policies plus inherited cross-cutting ones, no duplication
- [x] Modular — each SAPOL stands alone; Risk Tier scaling is declared, not duplicated per tier as separate policies
- [x] Easy to update — cross-cutting rules update once, apply here automatically
- [x] Easy to maintain — every policy traces to a specific term/field
- [x] Easy to replace — enforcement mechanisms deferred to Procedures/Tooling, policy intent survives tooling changes
