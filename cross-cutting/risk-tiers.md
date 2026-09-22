# Cross-Cutting Risk Scale

Status: Draft — pending review
Ratified: No
Last updated: 2026-09-22
Standard: NIST FIPS 199 (Standards for Security Categorization of Federal
Information and Information Systems)

Authored registry holding the risk classification scale itself — genuinely
identical across every layer. A layer's own Risk Tiers column (column 9)
references this scale and adds only what's layer-specific: Determining
Factors (what triggers each tier for that layer's resource types) and any
Regulatory Mapping specific to that layer's exposure.

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
Determining Factor in the owning layer's Risk Tiers column (risk tier is
not averaged — one high-risk factor is enough to elevate the whole
resource). This averaging rule is itself cross-cutting, not layer-specific.

## Consequences by Tier (cross-cutting baseline)

| Tier | Baseline Implication |
|---|---|
| **Low** | Standard policies (cross-cutting and layer-specific) apply as written — no additional constraint. |
| **Moderate** | Standard policies apply as written. |
| **High** | CCAR-3's two-person sign-off requirement (Infrastructure Admin + Security/Compliance) applies to any break-glass override, per cross-cutting/access-rules.md. |

A layer may add its own tier-scaled policy consequences beyond this
baseline (e.g., Infrastructure's POL-2 scales Availability Tier minimums
by Risk Tier) — those remain layer-specific, documented in that layer's
own Policies column.

---

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — one scale, one baseline consequence table
- [x] Modular — layers add Determining Factors and extra consequences independently
- [x] Easy to update — one edit updates the scale for every referencing layer
- [x] Easy to maintain — "Originally drafted as" line preserves provenance
- [x] Easy to replace — standard-grounded (FIPS 199), not a custom scale
