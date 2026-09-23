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

### SAPOL-2 — Database Schema Migration Review (Scaled by Risk Tier)
**Rule:** A schema migration (`dp-schema-migration`, owned by Data
Platform as of 2026-09-22 — kept here as a System Architecture policy
since it governs a deployment/release gate on a Service's database
dependency, not database mechanics themselves; candidate for moving to
Data Platform's own Policies column in a future pass) targeting a
Production database requires review before being applied, scaled by the
database entity's Risk Tier (09-risk-tiers.md, extending
cross-cutting/risk-tiers.md):
- **Low:** peer review sufficient.
- **Moderate:** peer review + Owning Team lead sign-off.
- **High:** peer review + lead sign-off + a documented rollback plan on
  file before the migration is applied.
**Applies to:** Production environment, Database entity type.
**Enforcement:** Approval gate, scaled as above. Who qualifies as
reviewer/lead is deferred to this domain's Access Rules (column 7).
**Rationale:** Explicitly chosen to scale by Risk Tier — mirrors
Infrastructure's POL-2/POL-3 pattern, established once Risk Tiers existed
and applied here proactively rather than needing a later retrofit.

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
asserts the requirement only — the mechanism that enforces it (a CI
pipeline gate) belongs to Workflow/Process (domain 7, not yet built).
**Applies to:** Production environment, Service/Application/API entity
types.
**Enforcement:** Hard block, mechanism deferred to Workflow/Process and/or
this domain's Tooling (column 10).
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
- SAPOL-2 and SAPOL-5 both scale by Risk Tier, applied proactively from
  the start (unlike Infrastructure's POL-2/POL-3, which were retrofitted
  after Risk Tiers was drafted) — Risk Tiers already existed as a
  cross-cutting concept by the time this column was drafted.

**Open items:**
- Who qualifies as "Owning Team lead" (SAPOL-2) and who performs the
  SAPOL-5 verification are deferred to Access Rules (column 7), next.
- SAPOL-4's enforcement mechanism is a genuine forward reference to
  Workflow/Process (domain 7) — flagged, not resolved here.

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — 5 domain-specific policies plus inherited cross-cutting ones, no duplication
- [x] Modular — each SAPOL stands alone; Risk Tier scaling is declared, not duplicated per tier as separate policies
- [x] Easy to update — cross-cutting rules update once, apply here automatically
- [x] Easy to maintain — every policy traces to a specific term/field
- [x] Easy to replace — enforcement mechanisms deferred to Procedures/Tooling, policy intent survives tooling changes
