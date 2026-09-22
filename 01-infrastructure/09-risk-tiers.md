# Infrastructure Layer — Risk Tiers

Status: Draft — pending review
Ratified: No
Last updated: 2026-09-22
Provenance: see _qa/09-risk-tiers.qa.md
Built on: 02-taxonomies.md, 06-policies.md
Standard: NIST FIPS 199 (Standards for Security Categorization of Federal
Information and Information Systems)

---

## Risk Scale

| Tier | FIPS 199 Definition | Infrastructure Interpretation |
|---|---|---|
| **Low** | Limited adverse effect on operations/assets if compromised | Dev/Staging resources; non-sensitive data; loss of availability is an inconvenience, not a business event |
| **Moderate** | Serious adverse effect | Most Production resources; moderate data sensitivity; downtime has real but recoverable business impact |
| **High** | Severe or catastrophic adverse effect | Production resources handling regulated/highly sensitive data, or whose failure has severe business/safety/legal consequence |

## Determining Factors

A resource's Risk Tier is the **highest** tier triggered by any applicable
factor below (risk tier is not averaged — one high-risk factor is enough
to elevate the whole resource).

| Factor | Low | Moderate | High |
|---|---|---|---|
| Environment (`infra-environment-lifecycle`) | Dev | Staging/QA | Production |
| Availability Tier (`infra-availability-tier-*`) | Tier I–II | Tier III | Tier IV |
| Data sensitivity | Non-sensitive/public | Internal-use | Regulated/PII/confidential — **see open item below** |
| Workload type | General compute | — | AI Training/Inference on regulated data (`infra-training-workload`, `infra-inference-workload`) |

**Data sensitivity note:** this factor genuinely belongs to the Data/
Metadata layer (not yet drafted), which will own the actual data
classification taxonomy. Referenced here provisionally, same pattern as
the role vocabulary in 07-access-rules.md — flagged for ownership
transfer once that layer exists.

## Regulatory Mapping (generalized — org fills in applicable regimes)

This framework is generalized and doesn't presume any org's specific
regulatory exposure. The table below is a placeholder structure — an org
adopting this framework fills in which regimes apply to which Risk Tier.

| Regime (example, not exhaustive) | Typical trigger | Applies at Risk Tier |
|---|---|---|
| HIPAA | Protected health information present | High (typically) |
| PCI-DSS | Payment card data present | High (typically) |
| GDPR / state privacy law | EU or covered-state personal data present | Moderate–High depending on data volume/sensitivity |
| SOX | Financial reporting systems | Moderate–High depending on materiality |
| (org-specific / none) | — | — |

## Consequences by Tier

| Tier | Policy Implication |
|---|---|
| **Low** | Existing Policies (column 6) apply as written — no additional constraint. |
| **Moderate** | Existing Policies apply as written — this framework does not currently differentiate Moderate from the flat "Production" rules in POL-2/POL-3. See open item below. |
| **High** | Existing Policies apply, **plus**: break-glass override (AR-2) requires two-person sign-off (Infrastructure Admin + Security/Compliance role) rather than Infrastructure Admin alone. |

---

**Open items:**
- (Resolved 2026-09-22) POL-2/POL-3 updated in 06-policies.md to scale
  with Risk Tier instead of applying flatly to all Production.
- (Resolved 2026-09-22) AR-2 in 07-access-rules.md updated to require
  two-person sign-off (Infrastructure Admin + Security/Compliance) for
  High-risk break-glass overrides.
- Data sensitivity factor is provisional pending Data/Metadata layer.
- Regulatory mapping table is intentionally a template, not filled with
  real determinations — an org applying this framework completes it for
  their actual regulatory exposure.

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — 3-tier scale, one determining-factor table, one consequence table
- [x] Modular — regulatory mapping is a fill-in template, doesn't hardcode assumptions
- [x] Easy to update — new determining factors are new table rows
- [x] Easy to maintain — tier is derived from existing terms (Environment,
      Availability Tier), not a new parallel classification
- [x] Easy to replace — standard-grounded (FIPS 199), not a custom scale
