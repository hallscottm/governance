# Q&A Log — Definitions (Data/Metadata)
# Append-only. Do not edit past entries; add new dated entries instead.

## 2026-09-22 — Q1.1: Full-sweep coverage of Data/Metadata vocabulary

**Context:** Full sweep from the start, consistent with the lesson
learned at Infrastructure and applied proactively at Networking and
System Architecture.

**Bucket:** [Standard]/AI-draftable.

**Drafted:** 66 owned terms across 10 subdomains — Data Governance Roles
& Structures, Data Classification & Sensitivity, Data Quality, Metadata
Types, Data Catalog & Discovery, Data Modeling Concepts, Master &
Reference Data, Data Lineage & Provenance, Data Lifecycle & Retention,
Data Privacy & Regulatory — plus 4 referenced (not owned) terms: Database
Schema and Database from System Architecture; Archive and Environment
(lifecycle) from Infrastructure. Reverse "Referenced by:" tags added to
all 4 source definitions.

**Design notes on same-word-different-scope terms:**
- "Physical Data Model" is explicitly not separately defined — it's
  System Architecture's Database Schema by another name, referenced
  rather than duplicated.
- "Entity" and "Relationship" (data-modeling senses) are flagged as
  distinct from this framework's own Ontology relation-types vocabulary
  and Taxonomy's use of "entity" — different scope, same word, per
  00-framework/term-linking-convention.md.
- "Business Glossary" is flagged as distinct from this framework's own
  Definitions columns (business-language glossary vs. governance
  vocabulary).

**This is also where the Data-sensitivity Risk Tier factor (left
unpopulated in Infrastructure, Networking, System Architecture) gets its
real definitions**: Sensitivity Level, Data Classification, PII, and the
four-tier Public/Internal/Confidential/Restricted scale — to be wired
into 09-risk-tiers.md as this domain's own Risk Tiers column is drafted.

**Status:** Pending explicit review.
