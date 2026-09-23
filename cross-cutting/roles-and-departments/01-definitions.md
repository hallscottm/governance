# Cross-Cutting: Roles & Departments — Definitions

Status: Draft — pending review
Ratified: No
Last updated: 2026-09-22
Provenance: see 00-qa.md in this directory

Third cross-cutting pillar, alongside Governance and Security
(00-framework/domain-axis-definition.md), established 2026-09-22 to
resolve the "provisional role vocabulary" carried as an open item by
every domain's Access Rules column since Infrastructure. Every domain's
Access Rules column references terms from here rather than restating
role labels locally.

Anchor convention: `ccrole-<slug>` (roles), `ccdept-<slug>`
(departments), `ccgov-<slug>` (governance bodies). See
00-framework/term-linking-convention.md.

**Scope boundary:** this registry owns *generic, reusable* role and
department vocabulary. It does not own domain-specific governance roles
that a domain already properly defines as part of its own subject matter
— e.g., Data Owner/Data Steward/Data Custodian/Data Governance Council
remain owned by 05-data-metadata/01-definitions.md, because they are
DAMA-DMBOK data-governance concepts tied specifically to Data Domain
governance, not generic organizational placeholders. This registry
references them rather than absorbing them (see Referenced Terms below).

---

## Referenced Terms (owned elsewhere)

- **Data Owner** — see [05-data-metadata/01-definitions.md#data-owner](../../05-data-metadata/01-definitions.md#data-owner)
- **Data Steward** — see [05-data-metadata/01-definitions.md#data-steward](../../05-data-metadata/01-definitions.md#data-steward)
- **Data Custodian** — see [05-data-metadata/01-definitions.md#data-custodian](../../05-data-metadata/01-definitions.md#data-custodian)
- **Data Governance Council** — see [05-data-metadata/01-definitions.md#data-governance-council](../../05-data-metadata/01-definitions.md#data-governance-council)

---

## Core Concepts

### Role {#ccrole-role}
A defined capacity in which a person or system actor acts — carrying
specific permissions, responsibilities, or approval authority within
this framework's Policies/Access Rules. Source: Common organizational
governance practice.

### Department {#ccdept-department}
An organizational unit grouping one or more Roles, typically aligned to
one or more of this framework's domains (see Department ↔ Domain
Alignment, 02-taxonomies.md). Source: Common organizational practice.

### Org Chart {#ccorg-org-chart}
The rolled-up structure of Departments and their Roles, generated from
this registry's Taxonomy — see `org-chart.md` in this directory (a
generated artifact, not hand-edited, same pattern as
00-framework/glossary-master.md and roadmap/roadmap.md).

### Reporting Line {#ccorg-reporting-line}
A defined accountability relationship between two Roles or Departments,
distinct from an approval relationship (which is transaction-scoped,
see Functional Role below) — a reporting line is a standing
organizational fact. Source: Common organizational practice.

### Governance Body {#ccgov-governance-body}
A cross-departmental group convened to make or ratify decisions spanning
multiple Departments — broader than any single Department's own internal
leadership. Source: Common organizational governance practice.

---

## Role Types

### Human Role {#ccrole-human-role}
A Role held by a person, as distinct from a System Actor. Source: Common
organizational governance practice.

### System Actor {#ccrole-system-actor}
A non-human entity (e.g., an AI agent/harness) that can hold defined
permissions and act within this framework's Policies/Access Rules, with
its own boundary distinct from any Human Role's. Source: Common practice
in AI governance frameworks (informal — no single formal standard cited).

### Positional Role {#ccrole-positional-role}
A Role tied to membership in a specific Department — the Role only
exists in the context of that Department (e.g., Infrastructure Admin
belongs to Platform Engineering). Source: Common organizational practice.

### Functional Role {#ccrole-functional-role}
A Role defined by the function performed in a specific transaction,
not by Department membership — the same person, from any Department,
can act as a Functional Role depending on context (e.g., anyone can be
a Requester; who is the Approver depends on the specific request).
Source: Common organizational practice; informed by separation-of-duties
principles already embedded in CCAR-2 (cross-cutting/access-rules.md).

---

## Generic Functional Roles

### Requester {#ccrole-requester}
Anyone requesting or initiating an action governed by this framework
(e.g., provisioning a resource, requesting data access) — a Functional
Role, not tied to any one Department. Source: Originally drafted as
Infrastructure's provisional "Requester" role (2026-09-22); formalized
as a cross-cutting Functional Role 2026-09-22.

### Approver {#ccrole-approver}
A Role, distinct from the Requester on the same transaction, authorized
to approve a specific governed action — a Functional Role; which
Positional Role or Department the Approver comes from is determined by
the specific Policy/Access Rule invoking it (e.g., CCAR-2, CCAR-3).
Source: Originally drafted as Infrastructure's provisional "Approver"
role (2026-09-22); formalized 2026-09-22.

---

## Generic Positional Roles

### Infrastructure Admin {#ccrole-infrastructure-admin}
Positional Role, member of Platform Engineering (ccdept-platform-
engineering), holding override/exception authority for hard-blocked
policies (CCAR-3) and standard Production provisioning approval
authority for Infrastructure and Networking resources. Source:
Originally drafted as Infrastructure's provisional "Infrastructure
Admin" role (2026-09-22); formalized 2026-09-22.

### Security/Compliance {#ccrole-security-compliance}
Positional Role, member of Security & Compliance (ccdept-security-
compliance), authorized to certify compliance-sensitive actions and
required as an additional sign-off for High-risk hard-block overrides
(CCAR-3) and other elevated-risk gates across domains (e.g., SAPOL-5,
DPOL-1-adjacent verification). Source: Originally drafted as
Infrastructure's provisional "Security/Compliance Role" (2026-09-22);
formalized 2026-09-22.

### Owning Team Lead {#ccrole-owning-team-lead}
Positional Role, the accountable lead for a specific service,
application, API, or database, as named in that entity's Owning Team
metadata field (03-system-architecture/04-metadata-standards.md).
Scoped narrowly — one team, one entity — not a blanket elevated-privilege
role like Infrastructure Admin; member of whichever Department owns that
service (typically Application Engineering, but not exclusively).
Source: Originally introduced in System Architecture's Access Rules
(2026-09-22); formalized as a cross-cutting Positional Role 2026-09-22.

### Data Architect {#ccrole-data-architect}
Positional Role, member of Data Governance & Engineering (ccdept-data-
governance-engineering), responsible for the *design* of Data Platform
resources — data models, database/warehouse/lakehouse structure,
technology selection for storage and streaming systems (04-data-
platform/01-definitions.md). Distinct from Data Engineer (below), which
builds and operates against that design, and distinct from Data Steward/
Owner/Custodian, which govern data's meaning and handling rather than its
structure. Co-owns Domain 4 (Data Platform) jointly with Data Engineer.
Source: Common organizational practice; added 2026-09-22 replacing
Application Engineering's prior co-ownership stake in Data Platform (see
00-qa.md Q7).

### Data Engineer {#ccrole-data-engineer}
Positional Role, member of Data Governance & Engineering (ccdept-data-
governance-engineering), responsible for *building and operating* Data
Platform resources against a Data Architect's design — implementing Data
Pipelines, ETL/ELT jobs, schema migrations, and the day-to-day operation
of databases, warehouses, lakehouses, and streaming platforms (04-data-
platform/01-definitions.md). Distinct from Data Architect (above), which
owns the design rather than the build/operate work. Co-owns Domain 4
(Data Platform) jointly with Data Architect. Source: Common
organizational practice; added 2026-09-22 replacing Application
Engineering's prior co-ownership stake in Data Platform (see 00-qa.md
Q7).

### Analytics Engineer {#ccrole-analytics-engineer}
Positional Role, member of Data Governance & Engineering (ccdept-data-
governance-engineering), responsible for the transformation layer
between raw ingested data and consumption — building the models (e.g.,
dbt-style) that turn Data Engineer's raw ingested data into clean,
business-ready datasets, and building/maintaining the Semantic Layer
(`dp-semantic-layer`) that materializes Data/Metadata's official Metric
definitions (`data-metric`) for downstream reporting tools to query.
Third co-owner of Domain 4 (Data Platform), alongside Data Architect and
Data Engineer — distinct from both: narrower than Data Engineer's
ingestion/operations scope, more implementation-focused than Data
Architect's design scope. Source: Common organizational practice; added
2026-09-22 when Business Intelligence / Reporting was split out as its
own domain (see 00-qa.md Q8).

### Business Analyst / Report Builder {#ccrole-business-analyst-report-builder}
Positional Role, member of Business Intelligence & Analytics
(ccdept-business-intelligence-analytics), builds reports and dashboards
and — distinctly from a pure consumer — often builds a self-service
Report Data Model (`bi-report-data-model`) inside the report tool itself
(calculated fields, blended sources, extracts) to do so. This is the
role most likely to produce an undocumented or diverging model, which is
the core risk Business Intelligence / Reporting (domain 6) exists to
govern — not because the role is suspect, but because self-service
modeling is exactly what makes a BI tool useful, and exactly where
metric drift enters if left unchecked. Source: Common organizational
practice; added 2026-09-22 (see 00-qa.md Q8).

### BI Analyst/Developer {#ccrole-bi-analyst-developer}
Positional Role, member of Business Intelligence & Analytics
(ccdept-business-intelligence-analytics), builds and maintains the more
formal, broadly-distributed reports/dashboards and is typically the role
that reviews and promotes a Business Analyst's self-service model from
Draft to Certified status once it has a documented source-to-target
mapping. Distinct from Analytics Engineer (which builds the official
Semantic Layer inside Data Platform, upstream of this role's work).
Source: Common organizational practice; added 2026-09-22 (see 00-qa.md
Q8).

---

## System Actor Types

### AI Agent/Harness {#ccrole-ai-agent-harness}
A System Actor: an AI system acting within a defined harness scope, with
its own permission boundary distinct from any Human Role's — may draft
or request actions on a human's behalf but, per CCAR-1, never itself
holds final Production approval authority. Not affiliated with any
Department (system actors sit outside the human org chart), though its
scope of operation is typically defined by the AI/ML Platform department
(ccdept-ai-ml-platform, once Harness/domain 8 is drafted) once that
Department exists. Source: Originally drafted as Infrastructure's
provisional "AI Agent/Harness" role (2026-09-22); formalized 2026-09-22.

---

## Departments

Department↔Domain alignment is many-to-many by design (confirmed
2026-09-22) — a Department may span multiple domains, and this framework
does not force a strict 1:1 mapping. See 02-taxonomies.md for the full
alignment table.

### Platform Engineering {#ccdept-platform-engineering}
Owns Infrastructure and Networking domain resources — compute, storage,
network boundaries, connectivity. Home Department for the Infrastructure
Admin role. Source: Common organizational practice (a combined
"platform" team spanning compute and network is a realistic, common
structure, not forced apart to match domain boundaries 1:1).

### Application Engineering {#ccdept-application-engineering}
Owns System Architecture domain resources — services, applications, APIs.
Home Department for the Owning Team Lead role (though Owning Team Lead
can also belong to other Departments owning a given service). No longer
holds a Data Platform ownership stake as of 2026-09-22 (see 00-qa.md
Q7) — a Service references a Database as a consumer, the same way it
references Infrastructure/Networking terms, without an ownership claim
on it. Source: Common organizational practice.

### Data Governance & Engineering {#ccdept-data-governance-engineering}
Owns Data/Metadata domain resources — data classification, quality,
cataloging, lineage — and, as of 2026-09-22, co-owns Data Platform
domain resources — databases, warehouses, lakehouses, vector stores,
streaming (see 00-qa.md Q7) — jointly held by its Data Architect, Data
Engineer, and (added 2026-09-22, see 00-qa.md Q8) Analytics Engineer
roles. Home Department for Data Owner, Data Steward, and Data Custodian
(referenced from Data/Metadata, not redefined here), plus Data Architect,
Data Engineer, and Analytics Engineer (defined here, under Generic
Positional Roles). Source: Common organizational practice; DAMA-DMBOK.

### Business Intelligence & Analytics {#ccdept-business-intelligence-analytics}
Owns Business Intelligence / Reporting domain resources — reports,
dashboards, self-service report-level data models, calculated fields
(domain 6, not yet drafted). Home Department for Business Analyst /
Report Builder and BI Analyst/Developer (defined here, under Generic
Positional Roles). Distinct from Data Governance & Engineering's
Analytics Engineer — Analytics Engineer builds the official Semantic
Layer inside Data Platform; this department's roles build and consume
reports downstream of it, and are the ones capable of creating the
undocumented, diverging models the domain exists to govern. Source:
Common organizational practice; added 2026-09-22 (see 00-qa.md Q8).

### DevOps / Release Engineering {#ccdept-devops-release-engineering}
Owns Workflow/Process domain resources — CI/CD, repository standards,
release management (domain 7, not yet drafted). Ownership model under revision as of 2026-09-22 (single-department
ownership of a cross-department domain is being reconsidered — see
00-qa.md); treat as provisional.
Source: Common organizational practice.

### AI/ML Platform {#ccdept-ai-ml-platform}
Owns Harness domain resources — AI/ML tooling, harness scope definitions,
model governance (domain 8, not yet drafted). Defines the operational
boundary AI Agent/Harness system actors act within. Source: Common
organizational practice.

### Security & Compliance {#ccdept-security-compliance}
Cross-cutting Department — not aligned to a single domain or a subset of
domains, but to the Security cross-cutting concern itself
(00-framework/domain-axis-definition.md), spanning every domain's Policies/
Access Rules/Risk Tiers columns. Home Department for the
Security/Compliance role. Source: Common organizational practice.

### IT Training & Change Management {#ccdept-training-change-management}
Owns Interface/Human domain resources — training, adoption, change
management, end-user support (domain 9, not yet drafted). Source: Common
organizational practice.

---

## Governance Bodies

### Governance Council {#ccgov-governance-council}
A generic, cross-departmental decision-making body convened for
decisions spanning multiple Departments — distinct from, and broader
than, Data/Metadata's own Data Governance Council (which is scoped
specifically to data governance decisions, referenced above, not a
Positional/Functional Role itself). An organization adopting this
framework may staff one Governance Council covering everything, or
several scoped bodies (data, security, AI) — this framework doesn't
prescribe which. Source: Common organizational governance practice.

---

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — 22 terms, grouped into 6 subdomains, no forced granularity
- [x] Modular — Data/Metadata's own governance roles referenced, not
      duplicated; every domain's Access Rules links here rather than
      restating role labels
- [x] Easy to update — a new Department or Role appends to its subdomain
- [x] Easy to maintain — anchors are stable slugs (`ccrole-`/`ccdept-`/
      `ccgov-`), safe to link to from every domain
- [x] Easy to replace — no term depends on a specific org's actual
      structure; Department↔Domain alignment is a stated example, not a
      hardcoded assumption an adopting org must keep
