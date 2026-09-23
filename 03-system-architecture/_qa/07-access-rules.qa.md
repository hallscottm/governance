# Q&A Log — Access Rules (System Architecture)
# Append-only. Do not edit past entries; add new dated entries instead.

## 2026-09-22 — Q7.1: New role needed for app-domain approvals?

**Context:** SAPOL-2 and SAPOL-5 both need an approver role scoped to the
application/service domain. Infrastructure Admin (the existing override
role) has no natural authority over application code or database schema
decisions specific to a team's own service.

**Bucket:** [Org-decision]/Human-only.

**Options presented:** (a) introduce "Owning Team Lead," a new
provisional role scoped to the Owning Team metadata field [Recommended];
(b) reuse Infrastructure Admin/Security-Compliance with no new role.

**Answer:** (a) Introduce "Owning Team Lead."

**Resulting rules:** SAAR-1 (schema migration review, scaled by Risk
Tier) and SAAR-2 (public-facing security baseline verification, scaled by
Risk Tier) both use Owning Team Lead, escalating to mandatory
Security/Compliance review at higher tiers.

**Status:** Pending explicit review.

## 2026-09-22 — Retrofit: Owning Team Lead ownership transferred to cross-cutting

**Context:** Same session as Infrastructure's/Networking's retrofit.
Owning Team Lead was originally introduced locally in this domain
(Q7.1, above) as a provisional role. Roles & Departments becoming a
cross-cutting pillar meant this role could be formalized immediately
rather than waiting for Interface/Human.

**Change:** Ownership of ccrole-owning-team-lead transferred to
cross-cutting/roles-and-departments/01-definitions.md. This file's
section now points there instead of locally defining the role. SAAR-1
and SAAR-2's rules are unchanged.
