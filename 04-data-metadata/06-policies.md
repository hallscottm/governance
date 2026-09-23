# Data/Metadata Layer — Policies

Status: Draft — pending review
Ratified: No
Last updated: 2026-09-22
Provenance: see _qa/06-policies.qa.md
Built on: 01-definitions.md, 04-metadata-standards.md, cross-cutting/policies.md, cross-cutting/risk-tiers.md

## Extends Cross-Cutting Policies

This layer's resources are subject to CCP-1 (Metadata Completeness),
CCP-2 (Cost Attribution), and CCP-3 (Production Provisioning Approval)
from cross-cutting/policies.md, applied to this layer's own entity types
(04-metadata-standards.md). Not restated here.

## Layer-Specific Policies

### DPOL-1 — PII/Restricted Data Protection Requirements
**Rule:** A Data Asset flagged Contains PII, or classified Restricted,
must use encryption at rest and restrict access to a defined
need-to-know group.
**Applies to:** All environments, any entity type where Contains PII is
true or Sensitivity Level is Restricted.
**Enforcement:** Hard block.
**Rationale:** Explicitly chosen as a hard block — consistent with
SAPOL-3's treatment of secrets and NPOL-2's treatment of encryption in
transit; PII/Restricted data is a well-understood, severe risk category.

### DPOL-2 — Data Retention Period Required; Disposal Enforced at Expiry
**Rule:** A Dataset cannot be provisioned without a Data Retention
Period. When that period expires and no Legal Hold applies, Data
Disposal is required, not merely recommended.
**Applies to:** All environments, Dataset entity type.
**Enforcement:** Hard block on missing retention period; expiry-disposal
is also enforced, not left as guidance.
**Rationale:** Explicitly chosen to enforce both halves — a retention
period that's never actually acted on at expiry provides no real
governance value, only the appearance of it.

### DPOL-3 — Data Owner Approval for New Access to Confidential/Restricted Data
**Rule:** Granting new access to Confidential or Restricted data requires
the Data Owner's approval. Applied identically to both tiers — not
further scaled.
**Applies to:** Data Owner role, Confidential and Restricted Sensitivity
Levels, any entity type.
**Enforcement:** Approval gate.
**Rationale:** Explicitly chosen as one uniform rule rather than a
further Security/Compliance escalation at Restricted — both tiers
already carry real, material disclosure risk; a Data Owner (the
accountable role for the domain) is judged sufficient at both.

### DPOL-4 — Right to Erasure Fulfillment SLA (Where Personal Data Is In Scope)
**Rule:** Where Personal Data is in regulatory scope for the
organization, a Right to Erasure request must be fulfilled within 30
days of a valid request, absent a Legal Hold or other lawful exception.
**Applies to:** Personal Data entity types, only where an organization
has determined Personal Data/regulatory scope applies — this framework
does not itself determine that scope (see 00-standards-alignment.md's
deferred GDPR/CCPA note).
**Enforcement:** SLA-based compliance tracking; specific mechanism
deferred to Procedures (column 8) and Tooling (column 10).
**Rationale:** 30 days adopted as a generalized, commonly-recognized
default (e.g., consistent with GDPR's own default) rather than left
unspecified — explicitly adjustable per an org's actual regulatory
determination, not asserted as this framework's legal conclusion for any
specific organization.

---

**Cross-references:**
- DPOL-1 and DPOL-3 both key off Sensitivity Level (04-metadata-standards.md)
  — DPOL-1 governs the technical protection required, DPOL-3 governs who
  approves new access, addressing different aspects of the same
  classification.
- DPOL-4 is explicitly scoped as conditional ("where Personal Data is in
  regulatory scope") rather than universally applied, consistent with
  this layer's Standards Alignment treating GDPR/CCPA/HIPAA as deferred,
  not assumed, for a generalized framework.

**Open items:**
- Who approves DPOL-3 access grants when the requester IS the Data Owner
  is deferred to Access Rules (column 7) — separation-of-duties question,
  same shape as CCAR-2's Requester/Approver distinction.
- DPOL-1's specific encryption mechanism and DPOL-4's SLA tracking
  mechanism are deferred to Procedures/Tooling (columns 8/10).

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — 4 layer-specific policies plus inherited cross-cutting ones
- [x] Modular — each DPOL stands alone
- [x] Easy to update — cross-cutting rules update once, apply here automatically
- [x] Easy to maintain — every policy traces to a specific term/field
- [x] Easy to replace — enforcement mechanisms deferred to Procedures/Tooling; DPOL-4's SLA is an adjustable default, not hardcoded law
