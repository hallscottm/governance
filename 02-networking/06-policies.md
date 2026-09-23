# Networking Domain — Policies

Status: Draft — pending review
Ratified: No
Last updated: 2026-09-22
Provenance: see _qa/06-policies.qa.md
Built on: 01-definitions.md, 04-metadata-standards.md, cross-cutting/policies.md

## Extends Cross-Cutting Policies

This domain's resources are subject to CCP-1 (Metadata Completeness),
CCP-2 (Cost Attribution), and CCP-3 (Production Provisioning Approval)
from cross-cutting/policies.md, applied to Networking's own entity types
(04-metadata-standards.md). Not restated here — see the cross-cutting
file for the rule text.

## Domain-Specific Policies

### NPOL-1 — Default-Deny Ingress (Production)
**Rule:** Production network boundaries default to denying all ingress
traffic; traffic is permitted only via explicit rule (`net-acl`,
`net-security-group`, or `net-firewall` entries).
**Applies to:** Production environment only.
**Enforcement:** Hard block on any Production security boundary
configuration that defaults to allow.
**Rationale:** Standard security best practice — explicitly chosen over
default-allow.

### NPOL-2 — Encryption in Transit Required (Production)
**Rule:** All Production network traffic must use encryption in transit
(`net-encryption-in-transit`, typically via `net-tls`).
**Applies to:** Production environment, all traffic (not narrowed to only
cross-boundary traffic).
**Enforcement:** Hard block — a Production resource/connection lacking
`net-encryption-in-transit` is non-compliant.
**Rationale:** Explicitly chosen as the strongest option — consistent
with this domain's zero-trust-adjacent Definitions/Ontology grounding
(NIST SP 800-207), which doesn't assume internal traffic is inherently
safe.

### NPOL-3 — Public Exposure Requires Additional Approval
**Rule:** Making a resource publicly internet-facing requires a distinct,
explicit approval step beyond the standard CCP-3 Production provisioning
approval.
**Applies to:** Any resource being configured for public/internet-facing
access, any environment (not limited to Production — a public-facing
Dev/Staging resource is still a real exposure risk).
**Enforcement:** Approval gate, distinct from CCP-3/CCAR-2 (who grants
this specific approval: deferred to this domain's Access Rules, column 7).
**Rationale:** Explicitly chosen — public exposure is a categorically
different risk than ordinary Production provisioning and deserves its own
checkpoint rather than being folded into general approval.

---

**Cross-references:**
- NPOL-1, NPOL-2 are hard blocks alongside the inherited CCP-1/CCP-2 —
  this domain now has more hard-block policies than any single one alone,
  consistent with networking's role as a security boundary domain.
- NPOL-3 deliberately does NOT scope to Production only, unlike NPOL-1/
  NPOL-2 — public exposure risk doesn't track environment tier the way
  other network policies do.

**Open items:**
- Who grants the NPOL-3 public-exposure approval is deferred to Access
  Rules (column 7) — addressed next, not left unresolved across sessions
  this time.
- Enforcement mechanism for NPOL-1/NPOL-2 (how a default-deny/encryption
  requirement is technically verified) deferred to Procedures (column 8)
  and/or Tooling (column 10), same boundary as Infrastructure.

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — 3 domain-specific policies plus inherited cross-cutting ones, no duplication
- [x] Modular — NPOL-1/2/3 stand alone from each other and from CCP-1/2/3
- [x] Easy to update — cross-cutting rules update once, apply here automatically
- [x] Easy to maintain — every policy traces to a specific term/field
- [x] Easy to replace — enforcement mechanism deferred, policy intent survives tooling changes
