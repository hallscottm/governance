# Q&A Log — Access Rules (System Architecture)
# Append-only. Do not edit past entries; add new dated entries instead.

## 2026-09-22 — Q7.1: New role needed for app-layer approvals?

**Context:** SAPOL-2 and SAPOL-5 both need an approver role scoped to the
application/service layer. Infrastructure Admin (the existing override
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
