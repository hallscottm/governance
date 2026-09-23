# System Architecture Domain — Procedures

Status: Draft — pending review
Ratified: No
Last updated: 2026-09-22
Provenance: see _qa/08-procedures.qa.md
Built on: 06-policies.md, 07-access-rules.md, cross-cutting/procedures.md

## Extends Cross-Cutting Procedures

CCPROC-1 (Production Provisioning Request & Approval), CCPROC-2
(Metadata Completeness Validation), CCPROC-3 (Cost Attribution
Validation), and CCPROC-4 (Break-Glass Override) apply to this domain's
resources without restatement — see cross-cutting/procedures.md.

## Domain-Specific Procedures

### SAPROC-1 — Backward Compatibility Check (Production API Releases)
**Executes:** SAPOL-1
**Steps:**
1. At release time, a Production API change is checked against its prior
   version's API Schema/contract for breaking changes.
2. If a breaking change is detected and the release does not carry a
   MAJOR version increment, the release is rejected before deployment.
3. The only path past a failed check is CCPROC-4's break-glass override.

### SAPROC-2 — Schema Migration Review (Scaled by Risk Tier)
**Executes:** SAPOL-2, SAAR-1
**Steps:**
1. A schema migration targeting a Production database is submitted with
   its Risk Tier already determined (per 09-risk-tiers.md).
2. Low tier: routed to any peer reviewer; approval closes the step.
3. Moderate tier: routed to a peer reviewer, then to the database's
   Owning Team Lead (per SAAR-1) for sign-off.
4. High tier: as Moderate, plus the migration must include a documented
   rollback plan before Owning Team Lead sign-off is requested.
5. On approval, the migration is applied. On rejection, the Requester is
   notified with the reason; no migration is applied.

### SAPROC-3 — Managed Secret Storage Verification
**Executes:** SAPOL-3
**Steps:**
1. At build or provisioning time, source code and Build Artifacts/
   Container Images are scanned for embedded secrets (credentials, API
   keys, signing keys).
2. Any detected embedded secret halts the build/provisioning before it
   reaches Approver review — the specific scanning mechanism is deferred
   to Tooling (column 10).
3. The only path past a failed check is CCPROC-4's break-glass override.

### SAPROC-4 — Automated Test Gate (Production Deployment)
**Executes:** SAPOL-4
**Steps:**
1. Before a Release is deployed to Production, its associated Unit Test
   and Integration Test results are checked.
2. A Release with failing or missing required test results is rejected
   before deployment.
3. The only path past a failed check is CCPROC-4's break-glass override.
   The pipeline mechanism that runs these tests is a forward reference to
   Workflow/Process (domain 7, not yet built) — this procedure defines the
   gate, not the pipeline.

### SAPROC-5 — Public-Facing Security Baseline Verification (Scaled by Risk Tier)
**Executes:** SAPOL-5, SAAR-2
**Steps:**
1. A Service/API flagged for public exposure has its Risk Tier
   determined (per 09-risk-tiers.md).
2. Low tier: Owning Team Lead self-attests the service meets ASVS Level 1.
3. Moderate tier: Owning Team Lead self-attests ASVS Level 2, then
   Security/Compliance reviews and confirms.
4. High tier: Security/Compliance independently verifies ASVS Level 3 —
   Owning Team Lead self-attestation alone does not close this step.
5. This verification runs independently of, and in addition to,
   Networking's NPROC-3 (public exposure network-boundary approval) — a
   public-facing High-risk service requires both to close before it is
   exposed.

---

**Open items:** none for this pass — consistent with Networking's
Procedures column, this domain's procedures were designed to close the
open items surfaced during Policies/Access Rules (who reviews, who
verifies) rather than carry them forward.

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — 5 domain-specific procedures plus inherited cross-cutting ones
- [x] Modular — SAPROC-1 through 5 stand alone
- [x] Easy to update — cross-cutting procedures update once, apply here automatically
- [x] Easy to maintain — every procedure traces to a specific SAPOL-/SAAR- item
- [x] Easy to replace — scanning/pipeline mechanisms deferred to column 10 and Workflow/Process
