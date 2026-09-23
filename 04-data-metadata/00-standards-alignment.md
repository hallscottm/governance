# Data/Metadata Layer — Standards Alignment

Status: Draft — pending review
Ratified: No
Last updated: 2026-09-22

Reference panel for this layer, consulted before drafting Definitions.
Scope per 00-framework/layer-axis-definition.md: what the data means —
taxonomy, ontology, catalog — explicitly not the databases/applications
that store and serve it (System Architecture, layer 3) or how it moves
through pipelines (Workflow/Process, layer 5). This is also where two
standards flagged since early in this framework's build finally apply:
DAMA-DMBOK (flagged at the very start of the session) and the data
sensitivity Risk Tier factor left unpopulated across all three completed
layers.

| Standard | Body | Covers |
|---|---|---|
| **DAMA-DMBOK (Data Management Body of Knowledge)** | DAMA International | Comprehensive data management framework — data governance, quality, metadata management, master/reference data. The primary grounding reference for this layer's vocabulary. |
| **ISO/IEC 11179 (Metadata Registries)** | ISO/IEC | Formal standard for metadata registries and data element definitions — already used as informal grounding for every prior layer's Metadata Standards column; cited formally here since this layer governs metadata itself. |
| **ISO 8000 (Data Quality)** | ISO | Data quality dimensions, measurement, and provenance. |
| **DCAT (Data Catalog Vocabulary)** | W3C | Vocabulary for describing datasets and data catalogs, enabling interoperable catalog metadata. |
| **DCMI (Dublin Core Metadata Initiative)** | DCMI | Widely-used descriptive metadata element set (title, creator, date, etc.), a common baseline for resource description. |
| **FAIR Data Principles** | FORCE11 (community-originated, now broadly adopted including by funders/publishers) | Findable, Accessible, Interoperable, Reusable — a widely-cited framework for data stewardship quality. |
| **NIST SP 800-60** | NIST | Guide for mapping information types to security categories — directly informs this layer's contribution to the Data-sensitivity Risk Tier factor left unresolved in Infrastructure, Networking, and System Architecture. |
| **NIST FIPS 199** | NIST | Security categorization standard (already the basis of cross-cutting/risk-tiers.md) — reused here as the target this layer's data classification feeds into. |
| **ISO/IEC 27001 Annex A (A.5)** | ISO | Information classification and handling (overlaps with System Architecture's A.14 citation, different control family — A.5 specifically). |

**Noted but not cited as a formal standard:**
- **Schema.org** — a widely-adopted structured-data vocabulary
  (originated by major search engines), candidate source for this
  layer's Taxonomies/Ontologies if a generic entity vocabulary is useful,
  distinct in authority from the ISO/W3C standards above.

**Not yet consulted, candidate for future passes (regulatory, deferred
until an actual determination is needed, not assumed here):**
- **GDPR (EU General Data Protection Regulation)** — relevant if/when
  this framework's Risk Tiers surface personal-data scope for an EU
  context.
- **CCPA/CPRA (California)** — relevant if/when personal-data scope
  includes California residents.
- **HIPAA** — relevant only if/when health data is in scope; not assumed
  for a generalized framework.
- **PCI-DSS** — same deferred status as already noted in Networking's
  standards panel; applies here too if/when payment-card data is in
  scope.

**Note on citation confidence:** DAMA-DMBOK, ISO 8000, DCAT, and DCMI are
stable, well-established references — citations here are from general
knowledge and reliable without re-verification. FAIR Data Principles is a
community-originated framework, not an ISO/NIST standard — cited
distinctly in authority, consistent with how SemVer/OpenAPI were flagged
in System Architecture's panel.

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — one table, scoped to what this layer actually covers
- [x] Modular — independent of the three prior layers' panels, no forced overlap beyond the genuine ISO 27001 connection
- [x] Easy to update — new standard cited later just adds a row
- [x] Easy to maintain — will be reconciled against actual Definitions citations once column 1 is drafted, same check performed for every prior layer
- [x] Easy to replace — no single standard is load-bearing for the whole layer
