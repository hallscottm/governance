# Infrastructure Domain — Standards Alignment

Status: Draft — pending review
Ratified: No
Last updated: 2026-09-22

Reference panel for this domain, consulted before drafting Definitions and
Taxonomies. Not itself "data" to fill in — it seeds vocabulary so later
columns align to existing standards rather than inventing new terms.
Compiled from the citations actually used in 01-definitions.md.

| Standard | Body | Covers | Used for |
|---|---|---|---|
| **NIST SP 800-53** | NIST | Security & privacy controls (CM = Configuration Management, CP = Contingency Planning families used here) | Maintenance Window, Redundancy |
| **NIST SP 800-88** | NIST | Media sanitization | Decommissioning |
| **NIST SP 800-34** | NIST | Contingency planning for information systems | Disaster Recovery (DR) Tier |
| **TIA-942** | TIA | Data center design/tiering standard | Data Center, Rack, Power Draw, Cooling |
| **Uptime Institute Tier Classification** | Uptime Institute | Data center reliability tiers (I–IV) | Availability Tier I–IV |
| **Green Grid / Uptime Institute (PUE)** | Green Grid | Power Usage Effectiveness metric | PUE |
| **ISO/IEC 27001 Annex A** | ISO | Asset management, physical/environmental controls | Asset Tag |
| **OCI (Open Container Initiative)** | OCI | Container image/runtime standards | Container, Container Runtime |
| **FinOps Foundation** | FinOps Foundation | Cloud financial management terminology | Cost Center Tag, Chargeback Unit |
| **NIST SP 500-292 (Cloud Reference Architecture)** | NIST | IaaS/PaaS/SaaS service-model boundaries | Added 2026-09-22 (see 00-framework/ea-framework-alignment.md) — clarifies what a given Compute Unit or environment actually is when service-model boundary matters |
| **Common cloud provider practice** | AWS / Azure / GCP (de facto, not a formal body) | Widely-adopted terminology not codified by a standards org but consistent across major providers | vCPU, Instance Type, Reserved Capacity, Durability Class |
| **Common industry practice** | — (no single body) | Terms in general technical use, not owned by any one standard | Majority of compute/storage/virtualization/scaling terms |

**Not yet consulted, candidate for future passes:**
- **DAMA-DMBOK** — relevant once Data/Metadata domain is drafted, not Infrastructure
- **ISO/IEC 42001** — AI management systems; likely relevant once Governance-related (cross-cutting) terms appear in later domains, not needed for pure hardware/substrate vocabulary
- **NIST AI RMF** — same reasoning as above; flagged for Harness/Governance-adjacent work, not Infrastructure

**Note on citation confidence:** NIST, ISO, TIA, Uptime Institute, OCI, and
FinOps Foundation are stable, well-established bodies — citations here are
from general knowledge and can be treated as reliable without
re-verification. If any of these are load-bearing for a compliance or
audit context, verify against the current published standard text before
ratifying, since standards do get revised.

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — one table, no redundant detail
- [x] Modular — additions/removals don't affect Definitions column directly
- [x] Easy to update — new standard cited later just adds a row
- [x] Easy to maintain — derived directly from what 01-definitions.md
      actually cites, not a separate parallel list to keep in sync by hand
- [x] Easy to replace — no single standard is load-bearing for the whole
      domain
