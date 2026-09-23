# Data/Metadata Domain — Conventions

Status: Draft — pending review
Ratified: No
Last updated: 2026-09-22
Provenance: see _qa/05-conventions.qa.md
Built on: 01-definitions.md, 04-metadata-standards.md

Scope: naming conventions for Data Assets, Datasets, and Business
Glossary Terms. Does not cover repository/pipeline conventions
(Workflow/Process, domain 7, not yet drafted).

---

## Data Asset / Dataset Naming Convention

**Pattern:** `<domain>-<asset-name>` (kebab-case)

Follows the same design decision already made for System Architecture's
Service Naming (05-conventions.md): stable, environment-agnostic identity.
Environment is tracked via the Environment metadata field
(04-metadata-standards.md), not the name — a dataset is conceptually the
same asset whether its data currently lives in Dev, Staging, or
Production.

**Example:** `orders-customer-orders`, `billing-invoice-history`

**Rules:** lowercase, hyphen-separated, globally unique — Data Asset ID
is used as the join key for Lineage Reference and Business Glossary
Reference fields, so collisions break traceability the same way Service
Name collisions would in System Architecture.

## Data Domain Naming Convention

**Pattern:** free-text, Title Case (e.g., `Customer`, `Orders`, `Billing`)

Deliberately distinct in casing convention from asset identifiers — a
Data Domain is a business-facing governance concept referenced in the
Data Governance Council and Business Glossary contexts, not a technical
identifier, so it uses natural business naming rather than kebab-case.

## Business Glossary Term Naming Convention

**Pattern:** free-text, natural business language, no enforced casing

Glossary terms are explicitly NOT identifiers — they're meant to read as
plain business language ("Customer Lifetime Value," not
"customer-lifetime-value"). This is a deliberate departure from every
naming convention elsewhere in this framework, worth calling out
explicitly rather than silently applying kebab-case where it doesn't fit
the actual use case (a business person reading a glossary entry).

## Sensitivity Level Tag Convention

Tag key: `sensitivity-level`, values restricted to the four defined tiers
(`public`, `internal`, `confidential`, `restricted`), lowercase — same
tag-key kebab-case rule as prior domains' Tag Key Naming Convention,
applied to this domain's single most load-bearing tag.

---

**Open items:**
- Data Domain and Business Glossary Term conventions deliberately break
  from kebab-case, an explicit design choice rather than an oversight —
  flagged here so a future reviewer doesn't "fix" it into consistency
  with the rest of the framework.

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — four small conventions, each scoped to a distinct entity type
- [x] Modular — Environment stays a metadata concern, consistent with System Architecture's precedent
- [x] Easy to update — add a new entity type's convention as a new section
- [x] Easy to maintain — Data Asset ID uniqueness rule keeps it usable as a join key
- [x] Easy to replace — pattern is a convention, no tooling dependency
