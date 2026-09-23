# Networking Domain — Tooling / Implementation

Status: Draft — pending review
Ratified: No
Last updated: 2026-09-22
Provenance: see _qa/10-tooling.qa.md
Built on: all prior columns (00-09)

Same posture as Infrastructure's Tooling column, confirmed rather than
re-derived: names required capabilities per category, no products
recommended or ranked.

---

## Category 1 — Network Provisioning / IaC

**Must satisfy:** the resource naming convention in 05-conventions.md;
must integrate with the same IaC platform chosen for Infrastructure
(Category 2 there) since network and compute resources are typically
provisioned together.
**Capability needed:** declarative network resource definition (VPCs,
subnets, security groups), compatible with Infrastructure's provisioning
workflow.
**Status:** Not selected.

## Category 2 — Policy Enforcement (Network-Specific)

**Must satisfy:** NPOL-1 (default-deny verification), NPOL-2 (encryption
in transit verification), plus the inherited cross-cutting hard blocks
(CCP-1, CCP-2).
**Capability needed:** pre-provisioning validation for network
configuration posture, ideally the same policy-as-code engine used for
Infrastructure's Category 3, extended with network-specific rules.
**Status:** Not selected.

## Category 3 — DNS Management

**Must satisfy:** the DNS Zone entity type in 04-metadata-standards.md.
**Capability needed:** DNS record management, ideally integrated with the
metadata catalog (Infrastructure's Category 1) for consistent tagging.
**Status:** Not selected.

## Category 4 — Firewall / Security Group Management

**Must satisfy:** NPOL-1's default-deny posture and the Security Boundary
entity type's metadata requirements.
**Capability needed:** centralized rule management, ideally with change
tracking that feeds the audit trail required by CCPROC-4 (break-glass
override logging).
**Status:** Not selected.

## Category 5 — Public Exposure Monitoring

**Must satisfy:** NPOL-3 (public exposure requires additional approval) —
needs a way to detect when a resource becomes publicly reachable,
independent of whether that exposure was properly approved via NPROC-3.
**Capability needed:** continuous scanning/detection of internet-facing
resources, to catch exposure that bypassed the approval process (not just
enforce it at provisioning time).
**Status:** Not selected.

---

**Cross-category dependency note:** Category 1 (Network IaC) and
Infrastructure's Category 2 (Infrastructure IaC) should very likely be
the same tool/platform, not two separate ones — network and compute
resources are typically defined in the same IaC codebase. This is a
stronger coupling than any Infrastructure/Networking Tooling relationship
so far.

**Open items:**
- No tools selected in any category — same as Infrastructure, this is
  the expected/acceptable state per artifact-axis-definition.md.
- Category 5 (Public Exposure Monitoring) is the one category without a
  clear Infrastructure-domain analog — it's a genuinely new capability
  type, not a network-specific instance of something Infrastructure
  already needed. Worth noting when this framework eventually reaches a
  Harness or Interface domain discussion of continuous monitoring more
  broadly.

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — capability requirements only, no premature tool lock-in
- [x] Modular — each category independently fillable
- [x] Easy to update — "Status: Not selected" becomes a tool name with no structural change
- [x] Easy to maintain — every category traces to specific columns/policies
- [x] Easy to replace — no product named/endorsed
