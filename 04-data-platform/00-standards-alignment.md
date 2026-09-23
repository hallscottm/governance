# Data Platform Domain — Standards Alignment

Status: Draft — pending review
Ratified: No
Last updated: 2026-09-22

Reference panel for this domain, consulted before extending Definitions.
Scope per 00-framework/domain-axis-definition.md: databases, data lakes/
lakehouses/warehouses, vector stores, and streaming — where data
physically lives and runs. Explicitly not what the data means
(Data/Metadata, domain 5) or how it's built into a downstream report
(Business Intelligence / Reporting, domain 6). Definitions/Taxonomies/
Ontologies were already drafted before this column, so this panel is
written retroactively, same treatment Infrastructure's Standards
Alignment received.

| Standard | Body | Covers |
|---|---|---|
| **ANSI/ISO SQL:2016** | ANSI/ISO/IEC | Relational database language standard — already cited as the grounding source for `dp-database`, `dp-table`, `dp-transaction`, `dp-acid` in 01-definitions.md. |
| **ISO/IEC 27040:2015 (Storage Security)** | ISO/IEC | Storage-specific security guidance (encryption at rest, sanitization, access control for storage systems) — the storage-layer counterpart to Infrastructure's and System Architecture's more general security citations. |
| **NIST SP 800-53 (SC, SI families)** | NIST | Security control catalog — overlaps with Infrastructure's and System Architecture's citations; the SC-28 (Protection of Information at Rest) control specifically applies to this domain's Database/Warehouse/Lake storage. |
| **NIST SP 800-88** | NIST | Media sanitization guidance — already cited by Infrastructure for physical/virtual resource decommissioning; relevant here too where Data/Metadata's Data Disposal (DPOL-2) is executed against this domain's storage. |
| **CIS Benchmarks (Database Platforms)** | Center for Internet Security | Configuration hardening baselines for common database engines — already cited by System Architecture; reused here since this domain now owns database engine selection/configuration directly. |
| **Apache Iceberg / Delta Lake / Apache Hudi table format specifications** | Respective open-source projects (not a formal standards body) | Open table-format specifications underlying most Data Lakehouse implementations — cited as the de facto reference vocabulary for `dp-data-lakehouse`, distinct in authority from the ISO/NIST citations above, same treatment System Architecture gave SemVer/OpenAPI. |
| **DAMA-DMBOK** | DAMA International | Primary grounding reference for Data/Metadata (domain 5), not this domain — flagged here only to note the boundary: this domain owns *where* data lives, DAMA-DMBOK's governance vocabulary owns *what it means*. |

**Noted but not cited as a formal standard:**
- **Kimball / Inmon data warehousing methodology** — the two dominant,
  competing methodologies for dimensional data warehouse design
  (already referenced informally in `dp-data-warehouse`'s definition).
  Not a standards-body publication; noted as the source of this domain's
  "star/snowflake schema" vocabulary if that vocabulary is ever expanded.
- **Apache Kafka wire protocol** — the de facto reference implementation
  most Streaming Platform products are compatible with; not issued by a
  standards body, noted the same way SemVer was in System Architecture.

**Not yet consulted, candidate for future passes:**
- **PCI-DSS** — relevant if/when payment-card data is stored in a
  Database/Warehouse in scope; same deferred status Networking and
  Data/Metadata already flagged.
- **HIPAA** — relevant only if/when health data is in scope.

**Note on citation confidence:** the Iceberg/Delta Lake/Hudi and Kafka
citations are open-source project specifications, not government or ISO
standards — cited as the de facto references practitioners use, distinct
in authority from the ANSI/ISO/NIST citations above, consistent with how
System Architecture and Data/Metadata each flagged their own
community-originated citations (Twelve-Factor App, FAIR Data Principles).

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — one table, scoped to what this domain actually covers
- [x] Modular — independent of the other domains' panels, no forced overlap beyond genuine connections (ANSI/ISO SQL already used, CIS Benchmarks/NIST SP 800-88 already cited elsewhere for the same underlying reason)
- [x] Easy to update — new standard cited later just adds a row
- [x] Easy to maintain — written retroactively against 01-definitions.md's actual citations, same reconciliation already done for Infrastructure
- [x] Easy to replace — no single standard is load-bearing for the whole domain
