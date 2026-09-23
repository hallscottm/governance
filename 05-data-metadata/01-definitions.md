# Data/Metadata Domain — Definitions

Status: Draft — pending review
Ratified: No
Last updated: 2026-09-22

Scope: what data *means* — classification, quality, catalog, lineage,
governance — as distinct from where it's stored (System Architecture's
Database/Schema, domain 3) and how it moves through pipelines
(Workflow/Process, domain 7, built 2026-09-22). This domain is also where the
Data-sensitivity Risk Tier factor, left unpopulated in Infrastructure,
Networking, and System Architecture, gets a real home.

Anchor convention: `data-<term-slug>`. See
00-framework/term-linking-convention.md for the DRY/anti-drift rules this
file follows.

---

## Referenced Terms (owned elsewhere)

- **Database Schema** — owned by Data Platform (moved from System Architecture 2026-09-22) → [04-data-platform/01-definitions.md#dp-database-schema](../04-data-platform/01-definitions.md#dp-database-schema)
- **Database** — owned by Data Platform (moved from System Architecture 2026-09-22) → [04-data-platform/01-definitions.md#dp-database](../04-data-platform/01-definitions.md#dp-database)
- **Archive** — see [01-infrastructure/01-definitions.md#infra-archive](../01-infrastructure/01-definitions.md#infra-archive)
- **Environment (lifecycle)** — see [01-infrastructure/01-definitions.md#infra-environment-lifecycle](../01-infrastructure/01-definitions.md#infra-environment-lifecycle)

---

## Data Governance Roles & Structures

### Data Governance {#data-governance}
The overall system of decision rights, accountability, and processes by
which an organization manages its data as an asset. Source: DAMA-DMBOK.

### Data Domain {#data-domain}
A logical grouping of data assets sharing a common business subject area
(e.g., "Customer," "Orders"), used as the primary unit of governance
accountability. Source: DAMA-DMBOK.

### Data Owner {#data-owner}
The accountable individual or role for a Data Domain's definition,
quality, and access rules — makes governance decisions, as distinct from
Data Steward, who executes them day to day. Typically held by a Business
Function Department (Marketing, Sales, Finance & Accounting, Human
Resources, Legal — cross-cutting/roles-and-departments/01-definitions.md,
added 2026-09-22) for its own Data Domain, not by Data Governance &
Engineering itself. Source: DAMA-DMBOK.
Referenced by: Roles & Departments (Business Function Departments)

### Data Steward {#data-steward}
The individual or role responsible for the day-to-day application of
governance rules to a Data Domain — data quality monitoring, glossary
maintenance, classification tagging. Source: DAMA-DMBOK.

### Data Custodian {#data-custodian}
The role responsible for the technical storage, security, and
infrastructure of a data asset, as distinct from the Data Owner
(business accountability) and Data Steward (governance execution).
Source: DAMA-DMBOK.

### Data Governance Council {#data-governance-council}
A cross-functional body that sets data governance policy, resolves
cross-domain conflicts, and ratifies changes to shared data definitions.
Source: DAMA-DMBOK.

---

## Data Classification & Sensitivity

### Data Classification {#data-classification}
The act of assigning a data asset to a defined Sensitivity Level based on
its content and regulatory exposure. Source: ISO/IEC 27001 Annex A.5;
NIST SP 800-60.

### Sensitivity Level {#data-sensitivity-level}
A defined tier (this framework uses Public, Internal, Confidential,
Restricted, below) describing how a data asset must be handled. Directly
feeds this domain's contribution to the cross-cutting Risk Tier
determination (09-risk-tiers.md). Source: Common industry practice;
informed by NIST FIPS 199's Low/Moderate/High categorization pattern.

### Public {#data-classification-public}
Sensitivity Level: no confidentiality requirement; disclosure carries no
material risk. Source: Common industry practice.

### Internal {#data-classification-internal}
Sensitivity Level: not for external disclosure, but broad internal access
is acceptable; disclosure risk is low. Source: Common industry practice.

### Confidential {#data-classification-confidential}
Sensitivity Level: access restricted to a defined need-to-know group;
disclosure risk is material. Source: Common industry practice.

### Restricted {#data-classification-restricted}
Sensitivity Level: highest tier — access tightly controlled and logged;
disclosure risk is severe (regulatory, legal, or safety consequence).
Source: Common industry practice; aligned with FIPS 199 High.

### PII (Personally Identifiable Information) {#data-pii}
Data that can identify a specific individual, alone or combined with
other data. A trigger for Confidential or Restricted classification.
Source: NIST SP 800-122 (Guide to Protecting PII, referenced via NIST SP
800-60's classification lineage).

### PHI (Protected Health Information) {#data-phi}
Health-related data tied to an identifiable individual — a specialized,
higher-sensitivity subset of PII, relevant only if health data is
actually in scope (see Standards Alignment's HIPAA note). Source: Common
industry/regulatory usage; not assumed in scope by default.

### Data Handling Requirement {#data-handling-requirement}
The concrete controls (encryption, access logging, retention limits)
mandated by a data asset's Sensitivity Level — the operational
consequence of classification. Source: Common industry practice; ties to
06-policies.md.

---

## Data Quality

### Data Quality {#data-quality}
The degree to which data is fit for its intended use, assessed across
defined dimensions (below). Source: ISO 8000; DAMA-DMBOK.

### Accuracy {#data-quality-accuracy}
Data Quality dimension: the degree to which data correctly describes the
real-world object or event it represents. Source: ISO 8000.

### Completeness {#data-quality-completeness}
Data Quality dimension: the degree to which all required data is present.
Source: ISO 8000.

### Consistency {#data-quality-consistency}
Data Quality dimension: the degree to which data agrees with itself or
other data across systems. Source: ISO 8000.

### Timeliness {#data-quality-timeliness}
Data Quality dimension: the degree to which data is available and
current when needed. Source: ISO 8000.

### Validity {#data-quality-validity}
Data Quality dimension: the degree to which data conforms to its defined
format, type, and range. Source: ISO 8000.

### Uniqueness {#data-quality-uniqueness}
Data Quality dimension: the degree to which a real-world entity is
represented once, without unintended duplication. Source: ISO 8000.

### Data Quality Rule {#data-quality-rule}
A defined, checkable condition (e.g., a Validity range, a Completeness
requirement) used to measure one or more Data Quality dimensions for a
specific data asset. Source: DAMA-DMBOK.

### Data Profiling {#data-profiling}
The process of examining a dataset to determine its actual structure,
content, and quality characteristics, typically to establish or verify
Data Quality Rules. Source: DAMA-DMBOK.

---

## Metadata Types

### Metadata {#data-metadata}
Data that describes other data — its structure, meaning, lineage, or
usage. Source: ISO/IEC 11179.

### Business Metadata {#data-business-metadata}
Metadata describing a data asset's business meaning — its Business
Glossary term, Data Owner, Data Domain. Source: DAMA-DMBOK.

### Technical Metadata {#data-technical-metadata}
Metadata describing a data asset's technical structure — data type,
format, Database Schema mapping. Source: DAMA-DMBOK.

### Operational Metadata {#data-operational-metadata}
Metadata describing a data asset's operational history — when it was
last updated, by which process, how often it's accessed. Source:
DAMA-DMBOK.

### Metadata Registry {#data-metadata-registry}
A managed system of record for an organization's metadata, structured per
a formal metadata standard. Source: ISO/IEC 11179.

### Metadata Repository {#data-metadata-repository}
The storage system implementing a Metadata Registry — distinct from the
registry itself, which is the structure/standard, not the storage.
Source: ISO/IEC 11179.

---

## Data Catalog & Discovery

### Data Catalog {#data-catalog}
A searchable inventory of an organization's data assets, combining
Technical, Business, and Operational Metadata to make data discoverable.
Source: DCAT (Data Catalog Vocabulary).

### Data Asset {#data-asset}
Any identifiable, managed unit of data with recognized business value —
a Dataset, a Database, a report, or a Business Glossary term can each be
a Data Asset. Source: DAMA-DMBOK.

### Dataset {#data-dataset}
A specific, identifiable collection of data treated as a single unit for
cataloging and access purposes. Source: DCAT.

### Business Glossary {#data-business-glossary}
An organization's curated, authoritative set of business term
definitions, distinct from this framework's own Definitions columns —
the Business Glossary defines terms in business language for a general
audience; this framework's Definitions define governance vocabulary.
Source: DAMA-DMBOK.

### Glossary Term {#data-glossary-term}
A single defined entry in a Business Glossary, typically linked to the
Data Assets it describes. Source: DAMA-DMBOK.

### Data Dictionary {#data-dictionary}
A structured reference describing a specific dataset's fields — names,
types, allowed values — narrower in scope than a Business Glossary
(which covers business concepts, not just one dataset's fields). Source:
DAMA-DMBOK; ISO/IEC 11179.

### Semantic Domain {#data-semantic-domain}
An abstraction that maps technical data structures to business-friendly
names and relationships, typically used by analytics/reporting tools.
Source: DAMA-DMBOK.

### Metric {#data-metric}
A named, authoritative, business-meaningful measure with a defined
formula, aggregation method, and grain (e.g., "Monthly Active Users" —
count of distinct users with ≥1 session in a calendar month). The
*definition* of the measure — owned here as the single source of truth
a report's Calculated Field should trace back to. Distinct from Business
Intelligence / Reporting's Calculated Field (`bi-calculated-field`),
which is a report-level formula that may or may not match this
definition, and from Data Platform's Semantic Layer
(`dp-semantic-layer`), which is where a Metric gets materialized into a
queryable object. Added 2026-09-22 when Business Intelligence /
Reporting was split out as its own domain — see 00-framework/
ea-framework-alignment.md. Source: Common industry practice (metrics-
layer/semantic-layer tooling such as dbt Semantic Layer, LookML).

---

## Data Modeling Concepts

### Conceptual Data Model {#data-conceptual-model}
A high-level model of an organization's key business entities and their
relationships, independent of any specific technology. Source: DAMA-DMBOK.

### Logical Data Model {#data-logical-model}
A model detailing entities, attributes, and relationships in full,
technology-independent detail — more specific than a Conceptual Data
Model, less specific than a Physical Data Model. Source: DAMA-DMBOK.

### Physical Data Model {#data-physical-model}
The technology-specific implementation of a Logical Data Model. Not
separately defined here — this is System Architecture's Database Schema
by another name; see the Referenced Terms section above.

### Entity (Data Modeling) {#data-entity}
A distinct business object or concept represented in a data model (e.g.,
"Customer," "Order"). Distinct from Ontology's use of "entity" as a
general term for anything classified in a Taxonomy — this is the
specific data-modeling sense. Source: DAMA-DMBOK.

### Attribute (Data Modeling) {#data-attribute}
A single characteristic or property of an Entity in a data model (e.g.,
"Customer Email"). Source: DAMA-DMBOK.

### Relationship (Data Modeling) {#data-relationship}
An association between two Entities in a data model. Distinct from this
framework's own Ontology relation-types vocabulary
(00-framework/relation-types.md), which governs relationships between
*governance terms*, not business data entities — same-word,
different-scope distinction, flagged per
00-framework/term-linking-convention.md. Source: DAMA-DMBOK.

---

## Master & Reference Data

### Master Data {#data-master-data}
Core business data (customers, products, locations) shared and reused
across multiple systems, requiring a single, trusted definition. Source:
DAMA-DMBOK.

### Reference Data {#data-reference-data}
A defined, typically small and stable set of permissible values used to
classify or categorize other data (e.g., country codes, status codes).
Source: DAMA-DMBOK.

### Golden Record {#data-golden-record}
The single, trusted, de-duplicated version of a Master Data entity,
produced by reconciling multiple source records. Source: DAMA-DMBOK.

### System of Record {#data-system-of-record}
The authoritative source system for a given Data Domain — the system
whose data is treated as ground truth when other systems disagree.
Source: DAMA-DMBOK.

### Data Deduplication {#data-deduplication}
The process of identifying and merging or eliminating duplicate
representations of the same real-world entity. Source: DAMA-DMBOK.

### Survivorship Rule {#data-survivorship-rule}
A defined rule for which source value wins when reconciling duplicate or
conflicting records into a Golden Record. Source: DAMA-DMBOK.

---

## Data Lineage & Provenance

### Data Lineage {#data-lineage}
The traceable record of a data asset's origin and the transformations it
has undergone from source to current state. Source: DAMA-DMBOK.

### Data Provenance {#data-provenance}
The documented history of a data asset's ownership, source, and
custody — broader than Data Lineage's transformation-focused record;
provenance includes who has been accountable for the data over time.
Source: DAMA-DMBOK.

### Data Transformation {#data-transformation}
A defined operation that converts data from one form to another,
recorded as a step in its Data Lineage. Source: DAMA-DMBOK; general
usage (specific transformation mechanics are a Workflow/Process concern).

### Source System {#data-source-system}
The system where a given piece of data originates, the starting point of
its Data Lineage. Source: DAMA-DMBOK.

### Downstream Consumer {#data-downstream-consumer}
A system, service, or report that consumes data from a Source System or
intermediate system, forming a node in that data's Data Lineage. Source:
DAMA-DMBOK.

---

## Data Lifecycle & Retention

### Data Retention Period {#data-retention-period}
The defined length of time a data asset must be kept before it becomes
eligible for disposal, driven by legal, regulatory, or business need.
Source: DAMA-DMBOK; informed by NIST SP 800-60's information-type
lifecycle guidance.

### Data Lifecycle Stage {#data-lifecycle-stage}
A defined stage in a data asset's life — creation, active use, archival,
disposal — distinct from Infrastructure's Environment lifecycle, which
describes deployment stage, not data's own age/use stage. Source:
DAMA-DMBOK.

### Data Archival {#data-archival}
Moving a data asset out of active use into long-term, lower-cost storage
while preserving it, per its Data Retention Period. Realized physically
via Infrastructure's Archive; see Referenced Terms. Source: DAMA-DMBOK.

### Data Disposal {#data-disposal}
The permanent, irreversible destruction of a data asset once its Data
Retention Period expires and no Legal Hold applies. Distinct from
Infrastructure's Decommissioning (which retires compute/storage
resources) — this term is about the data itself, which may outlive or be
disposed of independently of any specific resource. Source: DAMA-DMBOK;
NIST SP 800-88 (media sanitization, already cited at Infrastructure,
referenced here for the disposal mechanism).

### Legal Hold {#data-legal-hold}
A directive suspending the normal Data Retention Period and Data
Disposal process for specific data subject to litigation, audit, or
investigation. Data Owner authority for this term and this subdomain's
Data Privacy & Regulatory terms (Consent, Right to Erasure, Cross-Border
Data Transfer) sits with Legal (cross-cutting/roles-and-departments/
01-definitions.md#ccdept-legal, added 2026-09-22), which had no assigned
business owner before then. Source: Common legal/records-management
practice; EDRM.
Referenced by: Roles & Departments (Legal)

---

## Data Privacy & Regulatory

### Personal Data {#data-personal-data}
Data relating to an identified or identifiable individual — the broader,
regulatory-framing term that PII is the practical/operational
counterpart to. Source: Common regulatory usage (e.g., GDPR's framing);
noted as a deferred regulatory area per Standards Alignment.

### Data Subject {#data-subject}
The individual to whom Personal Data relates. Source: Common regulatory
usage.

### Consent {#data-consent}
A Data Subject's affirmative, informed agreement to a specific Data
Processing Purpose. Source: Common regulatory usage.

### Right to Erasure {#data-right-to-erasure}
A Data Subject's right to request deletion of their Personal Data,
subject to Legal Hold and retention exceptions. Source: Common regulatory
usage (e.g., GDPR's framing).

### Data Processing Purpose {#data-processing-purpose}
The specific, defined reason Personal Data is collected and used —
required to be stated and limited to under most privacy regulatory
frameworks. Source: Common regulatory usage.

### Data Minimization {#data-minimization}
The principle of collecting and retaining only the Personal Data
necessary for a stated Data Processing Purpose. Source: Common regulatory
usage.

### Cross-Border Data Transfer {#data-cross-border-transfer}
The movement of Personal Data across national/jurisdictional boundaries,
subject to additional regulatory requirements in many frameworks. Source:
Common regulatory usage.

---

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — terms grouped into 10 subdomains, each independently scannable
- [x] Modular — cross-domain references (Database Schema, Database, Archive, Environment lifecycle) are links, not restatements
- [x] Easy to update — new terms append to the relevant subdomain section
- [x] Easy to maintain — anchors are stable slugs (`data-<term>`), safe to link to
- [x] Easy to replace — no term depends on a specific vendor or product; regulatory terms explicitly flagged as deferred-scope, not load-bearing
