# System Architecture Layer — Tooling / Implementation

Status: Draft — pending review
Ratified: No
Last updated: 2026-09-22
Provenance: see _qa/10-tooling.qa.md
Built on: all prior columns (00-09)

Same posture as Infrastructure and Networking: capability categories only,
no specific product/vendor recommendations — deferred entirely per
explicit choice, confirmed again for this layer.

## Capability Categories

### API Gateway / Management
Enforces API versioning (SAPOL-1), exposes API Contracts, and is the
natural place to apply rate limiting and authentication for public
Endpoints. Overlaps functionally with Networking's Load Balancer/Reverse
Proxy tooling (10-tooling.md) — likely the same product family, not
independently selected.

### Database Platform & Migration Tooling
Runs Schema Migrations (SAPROC-2) and enforces the review gate before a
migration reaches Production. Category is deliberately broad (relational,
document, key-value engines all need this) rather than one relational-
only recommendation.

### Secrets Management
Provides the managed secret storage required by SAPOL-3, and the scanning
capability that detects secrets embedded in source or Build Artifacts
(SAPROC-3). Cross-layer note: secrets management is typically one
organization-wide tool, not selected per layer — flagged the same way
Networking flagged its IaC tooling likely being shared with Infrastructure.

### Application Security Testing (SAST / DAST / Dependency Scanning)
Verifies the OWASP ASVS level required by SAPOL-5, scaled by Risk Tier.
Static analysis, dynamic scanning, and dependency vulnerability scanning
are grouped as one category here since they typically integrate into the
same pipeline stage, even when provided by different tools.

### Container Image Registry & Build Artifact Repository
Stores and versions Container Images and other Build Artifacts
(SemVer-tagged). Direct dependency on Infrastructure's Container Runtime/
Orchestrator (01-infrastructure/10-tooling.md) — an image registry choice
is constrained by what the target runtime can pull from.

### Automated Test Execution & Gating
Runs Unit Tests and Integration Tests and enforces the SAPOL-4 gate before
Production deployment. This category's actual execution mechanism is a
forward reference to Workflow/Process (layer 5, not yet built) — listed
here because the gate itself (what must pass) is owned by this layer, even
though the pipeline that runs it is not.

---

**Cross-category dependency notes:**
- API Gateway/Management should likely be the same tool family as
  Networking's Load Balancer/Reverse Proxy selection, not chosen
  independently — third instance of this kind of cross-layer tooling
  dependency (after Infrastructure/Networking's IaC-platform note).
- Container Image Registry choice is constrained by Infrastructure's
  Container Runtime/Orchestrator choice — must be pullable by whatever
  runtime Infrastructure selects.
- Secrets Management is very likely one org-wide tool spanning all
  layers, not a per-layer selection — flagged, not resolved, since no
  layer "owns" org-wide tooling decisions in this framework's current
  design.

**Open items:**
- Automated Test Execution & Gating's actual mechanism depends on
  Workflow/Process (layer 5), not yet built — same forward reference
  already flagged in 06-policies.md (SAPOL-4) and 08-procedures.md
  (SAPROC-4).

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — 6 capability categories, no product lock-in
- [x] Modular — each category maps to a specific Policy/Procedure it implements
- [x] Easy to update — a category can be filled in with a specific product later without touching this structure
- [x] Easy to maintain — cross-category dependencies documented explicitly, not left implicit
- [x] Easy to replace — no product named, so no migration cost baked into the framework itself
