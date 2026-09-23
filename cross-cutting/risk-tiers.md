# Cross-Cutting Risk Scale

Status: Draft — pending review
Ratified: No
Last updated: 2026-09-22
Standard: NIST FIPS 199 (Standards for Security Categorization of Federal
Information and Information Systems)

Authored registry holding the risk classification scale itself — genuinely
identical across every domain. A domain's own Risk Tiers column (column 9)
references this scale and adds only what's domain-specific: Determining
Factors (what triggers each tier for that domain's resource types) and any
Regulatory Mapping specific to that domain's exposure.

**Originally drafted as:** Infrastructure's Risk Scale (2026-09-22);
extracted to cross-cutting 2026-09-22 once Networking needed the
identical scale.

---

## Risk Scale

| Tier | FIPS 199 Definition | General Interpretation |
|---|---|---|
| **Low** | Limited adverse effect on operations/assets if compromised | Dev/Staging resources; non-sensitive data; loss of availability is an inconvenience, not a business event |
| **Moderate** | Serious adverse effect | Most Production resources; moderate data sensitivity; downtime has real but recoverable business impact |
| **High** | Severe or catastrophic adverse effect | Production resources handling regulated/highly sensitive data, or whose failure has severe business/safety/legal consequence |

A resource's Risk Tier is the **highest** tier triggered by any applicable
Determining Factor in the owning domain's Risk Tiers column (risk tier is
not averaged — one high-risk factor is enough to elevate the whole
resource). This averaging rule is itself cross-cutting, not domain-specific.

**Clarifying note (added 2026-09-23):** this maximum-of-factors rule does
not mean Environment=Production alone forces High. Each domain's own
Determining Factors table caps Environment at Moderate; High requires
Production combined with a separate High-triggering factor (data
sensitivity, public exposure, business-criticality, etc., depending on
domain). This is what makes "Most Production resources... Moderate"
(General Interpretation, above) actually true rather than aspirational.
An earlier version of every domain's table put Production directly in
the High column, which under this same maximum-of-factors rule made
every Production resource automatically High and contradicted this
file's own description of itself — corrected across all 8 domains'
09-risk-tiers.md files 2026-09-23; see each domain's own Environment
factor note for the specific fix.

## Consequences by Tier (cross-cutting baseline)

| Tier | Baseline Implication |
|---|---|
| **Low** | Standard policies (cross-cutting and domain-specific) apply as written — no additional constraint. |
| **Moderate** | Standard policies apply as written. |
| **High** | CCAR-3's two-person sign-off requirement (Infrastructure Admin + Security/Compliance) applies to any break-glass override, per cross-cutting/access-rules.md. |

A domain may add its own tier-scaled policy consequences beyond this
baseline (e.g., Infrastructure's POL-2 scales Availability Tier minimums
by Risk Tier) — those remain domain-specific, documented in that domain's
own Policies column.

---

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — one scale, one baseline consequence table
- [x] Modular — domains add Determining Factors and extra consequences independently
- [x] Easy to update — one edit updates the scale for every referencing domain
- [x] Easy to maintain — "Originally drafted as" line preserves provenance
- [x] Easy to replace — standard-grounded (FIPS 199), not a custom scale
