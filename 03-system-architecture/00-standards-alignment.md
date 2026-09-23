# System Architecture Domain — Standards Alignment

Status: Draft — pending review
Ratified: No
Last updated: 2026-09-22

Reference panel for this domain, consulted before drafting Definitions.
Scope per 00-framework/domain-axis-definition.md: databases, applications,
and services built on the substrate — explicitly not physical/virtual
compute (Infrastructure) or connectivity/segmentation (Networking). This
domain is about what runs and how it's built/versioned/secured, not the
data's meaning (Data/Metadata, domain 5) or how it's deployed via
pipelines (Workflow/Process, domain 7).

| Standard | Body | Covers |
|---|---|---|
| **ISO/IEC/IEEE 42010:2011** | ISO/IEC/IEEE | Architecture description — conceptual framework for describing system/software architecture (viewpoints, views, stakeholders, rationale) |
| **ISO/IEC 25010:2011 (SQuaRE)** | ISO/IEC | Software product quality model — the 8 quality characteristics (functional suitability, performance efficiency, compatibility, usability, reliability, security, maintainability, portability) used as a shared vocabulary for non-functional requirements |
| **OWASP ASVS (Application Security Verification Standard)** | OWASP | Application-domain security requirements and verification levels — the app-domain counterpart to Infrastructure/Networking's NIST/CIS coverage |
| **OWASP Top 10** | OWASP | Most critical web application security risk categories — widely adopted reference vocabulary for application risk |
| **OpenAPI Specification (OAI)** | OpenAPI Initiative | Machine-readable API interface description — informs this domain's Conventions and Metadata Standards for service interfaces |
| **Semantic Versioning 2.0.0 (SemVer)** | semver.org (community spec, de facto industry standard) | Version-numbering convention for APIs/services/packages — relevant to this domain's Conventions column |
| **NIST SP 800-53** | NIST | Security control catalog (overlaps with Infrastructure's citation, different control families apply here: e.g., SC — System and Communications Protection, SI — System and Information Integrity, at the application layer) |
| **NIST SP 800-190** | NIST | Application Container Security Guide — relevant if/when containerized services are in scope |
| **ISO/IEC 27001 Annex A (A.14)** | ISO | System acquisition, development and maintenance (overlaps with Networking's Annex A citation, different control family — A.14 specifically) |
| **ANSI/ISO SQL:2016** | ANSI/ISO/IEC | Relational database language standard — baseline vocabulary for this domain's database-related definitions |
| **CIS Benchmarks (application/database platforms)** | Center for Internet Security | Configuration hardening baselines for common application servers, database engines, and container runtimes |

**Noted but not cited as a formal standard:**
- **The Twelve-Factor App** — a widely-adopted industry methodology for
  building services (config, statelessness, disposability, etc.), not
  issued by a standards body. Flagged as a candidate source of
  vocabulary/conventions for this domain's Conventions column, cited
  distinctly from the formal standards above if and when it's actually
  used to inform a definition.

**Not yet consulted, candidate for future passes:**
- **DAMA-DMBOK** — not applicable to this domain (data governance content
  belongs to Data/Metadata, domain 5); remains flagged for that domain.
- **ISO/IEC 42001, NIST AI RMF** — not applicable to this domain (AI
  management system / AI risk content); remains flagged for the Harness
  domain where AI-specific governance is more directly relevant.

**Note on citation confidence:** SemVer, OpenAPI, and OWASP publications
are actively maintained community/industry standards, not government or
ISO standards — cited here as the de facto references practitioners use,
distinct in authority from ISO/NIST citations. ISO/IEC 25010 and
42010 are formal ISO standards but less universally known than, e.g.,
ISO 27001 — verify against the current published edition before
ratifying if this becomes load-bearing for a compliance context.

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — one table, scoped to what this domain actually covers
- [x] Modular — independent of Infrastructure's and Networking's standards
      panels, no forced overlap beyond the genuine ISO 27001 connection
- [x] Easy to update — new standard cited later just adds a row
- [x] Easy to maintain — will be reconciled against actual Definitions
      citations once column 1 is drafted (same check performed
      retroactively for Infrastructure, done proactively for Networking)
- [x] Easy to replace — no single standard is load-bearing for the whole
      domain
