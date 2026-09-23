# Q&A Log — Ontologies (System Architecture)
# Append-only. Do not edit past entries; add new dated entries instead.

## 2026-09-22 — Q3.1: Relationship coverage, including cross-domain edges

**Context:** Same 9-type relation vocabulary as Infrastructure and
Networking. System Architecture sits above both prior domains, so several
genuine cross-domain relationships exist in both directions: this domain
runs-on/requires things Infrastructure and Networking own, and one
Infrastructure term (Availability Tier) constrains a System Architecture
term (Availability) from below.

**Bucket:** [Standard]/AI-draftable.

**Drafted:** 50 relationships across the 10 Definitions subdomains, 8 of
them cross-domain (5 pointing into Infrastructure: infra-compute-unit x2,
infra-container x2, infra-block-storage, infra-horizontal-scaling x2,
infra-environment-lifecycle, infra-redundancy; 1 pointing into Networking:
net-encryption-in-transit; 1 pointing FROM Infrastructure into this domain:
infra-availability-tier --[constrains]--> sysarch-availability). Reverse
pointers added to both 01-infrastructure/03-ontologies.md and
02-networking/03-ontologies.md's "Cross-Domain References" sections per
the standing rule in 00-framework/relation-types.md. Networking's
ontology file didn't have a "Cross-Domain References" section yet (it had
only been on the giving end of cross-domain relationships before) — added
one for the first time.

**Status:** Pending explicit review.
