# Data Platform Domain — Risk Tiers

Status: Draft — pending review
Ratified: No
Last updated: 2026-09-22
Provenance: see _qa/09-risk-tiers.qa.md
Built on: 02-taxonomies.md, 04-metadata-standards.md, 06-policies.md, cross-cutting/risk-tiers.md

## Risk Scale

**Extends:** cross-cutting/risk-tiers.md (FIPS 199-aligned Low/Moderate/
High scale — not restated here).

## Determining Factors

A resource's Risk Tier is the **highest** tier triggered by any applicable
factor (cross-cutting maximum rule, per cross-cutting/risk-tiers.md).

| Factor | Low | Moderate | High |
|---|---|---|---|
| Environment (referenced from Infrastructure) | Dev | Staging/QA, Production | — (Environment alone never reaches High; see note below) |
| Sensitivity Level / Contains PII (referenced from Data/Metadata, `data-sensitivity-level`, `data-pii`) | Public or Internal, no PII | Confidential | Restricted, or Contains PII = true |
| Service Tier / Criticality (referenced from System Architecture — the criticality of the Service(s) this entity backs) | Non-critical, internal tooling | Business-important, moderate user impact if down | Business-critical, severe impact if down |
| Public exposure (Vector Database or Streaming Platform reachable via a public Endpoint, e.g. a RAG API) | Internal-only | N/A — this factor has no Moderate value | Publicly internet-facing |

**Note on Environment factor (corrected 2026-09-23):** Production alone
caps this factor at Moderate, matching cross-cutting/risk-tiers.md's own
stated interpretation ("Most Production resources... Moderate"). An
earlier version of this table put Production directly in the High
column, which combined with the cross-domain "highest tier wins" rule
meant every Production resource in every domain was automatically High
regardless of any other factor — contradicting cross-cutting's own
description of itself. High still requires Production *plus* another
High-triggering factor from this table (data sensitivity, public
exposure, business-criticality, etc., depending on domain) — Environment
alone is never sufficient.

**Note on Sensitivity Level/PII factor:** sourced identically to how
Infrastructure, Networking, and System Architecture each source it —
this domain's entities (Database, Warehouse, Lake, Lakehouse, Vector
Database) are exactly the kind of resource Data/Metadata's Sensitivity
Level exists to classify, so this factor is central here, not incidental.

**Note on Public exposure factor:** narrower than System Architecture's
equivalent factor — most Data Platform resources aren't directly
public-facing (a Database sits behind a Service, per
`sysarch-service --[requires]--> dp-connection-pool`), but a Vector
Database or Streaming Platform exposed for direct external query (e.g. a
RAG retrieval API) is a real, increasingly common pattern this framework
should account for, not assume away.

## Consequences by Tier

**Extends:** cross-cutting/risk-tiers.md's baseline (two-person sign-off
for High risk, via CCAR-3).

**Domain-specific additions beyond the baseline (already defined in full
in 06-policies.md/07-access-rules.md — summarized here for visibility):**

| Tier | Data Platform-Specific Policy Implication |
|---|---|
| **Low** | DPPOL-1 migration review: peer review only. DPPOL-4 table-format change: Data Engineer review only. |
| **Moderate** | DPPOL-1: peer review + Data Engineer sign-off. |
| **High** | DPPOL-1: peer review + Data Engineer + Data Architect sign-off + documented rollback plan. DPPOL-4: Data Engineer + Data Architect sign-off. DPPOL-2, DPPOL-3 hard blocks apply uniformly at every tier (not scaled) — same treatment System Architecture's SAPOL-1/SAPOL-3/SAPOL-4 established for its own hard blocks. DPPOL-5 is likewise uniform — Certified-Metric-via-Semantic-Layer isn't a matter of degree. |

---

**Open items:**
- (Resolved 2026-09-23) Environment factor corrected: Production alone
  now caps at Moderate, not High — see the note under Determining Factors.
- Public exposure factor's real-world frequency (how often a Vector
  Database/Streaming Platform is genuinely public-facing vs. always
  sitting behind a Service) isn't asserted here — included because it's
  a real pattern, not because this framework has evidence it's common;
  same epistemic caution used for every "included but not weighted as
  certain" factor elsewhere in this framework.
- Service Tier/Criticality inheritance (a Database inheriting its
  dependent Service's criticality rather than being scored independently)
  is asserted as the default; an organization whose databases are shared
  across many services with different criticalities may need to define
  its own aggregation rule — flagged, not resolved, same posture as the
  Data volume/scale factor Data/Metadata left qualitative.

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — 4 determining factors, reusing the cross-cutting scale
- [x] Modular — domain-specific factors independent of every other domain's
- [x] Easy to update — cross-cutting scale updates once, applies here automatically
- [x] Easy to maintain — factors derived from existing Definitions/Metadata Standards
- [x] Easy to replace — standard-grounded (FIPS 199, inherited)
