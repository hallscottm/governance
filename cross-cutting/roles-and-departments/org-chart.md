# Org Chart (GENERATED)

Status: Generated 2026-09-22
Last updated: 2026-09-22
Generated from: 01-definitions.md, 02-taxonomies.md (Department ↔ Domain
Alignment table)

Do not edit directly — regenerate from source files. Same pattern as
00-framework/glossary-master.md and roadmap/roadmap.md.

---

## Governance Council (#ccgov-governance-council)
Cross-departmental body, convened from representatives of every
department below.

├── **Platform Engineering** (#ccdept-platform-engineering)
│   ├── Owns: Domain 1 (Infrastructure), Domain 2 (Networking)
│   └── Positional Role: Infrastructure Admin (#ccrole-infrastructure-admin)
│
├── **Application Engineering** (#ccdept-application-engineering)
│   ├── Owns: Domain 3 (System Architecture)
│   └── Positional Role: Owning Team Lead (#ccrole-owning-team-lead) — typical home, not exclusive
│
├── **Data Governance & Engineering** (#ccdept-data-governance-engineering)
│   ├── Owns: Domain 4 (Data Platform), Domain 5 (Data/Metadata)
│   ├── Positional Roles: Data Architect (#ccrole-data-architect), Data
│   │   Engineer (#ccrole-data-engineer), Analytics Engineer
│   │   (#ccrole-analytics-engineer) — co-own Domain 4 jointly (design /
│   │   build-operate / transform-and-semantic-layer split; added
│   │   2026-09-22, see 00-qa.md Q7/Q8, replacing Application
│   │   Engineering's earlier co-ownership stake)
│   └── Positional Roles (owned by Data/Metadata, referenced here):
│       Data Owner, Data Steward, Data Custodian
│       — see 05-data-metadata/01-definitions.md
│
├── **Business Intelligence & Analytics** (#ccdept-business-intelligence-analytics)
│   ├── Owns: Domain 6 (Business Intelligence / Reporting) — not yet drafted
│   ├── Positional Roles: Business Analyst / Report Builder
│   │   (#ccrole-business-analyst-report-builder), BI Analyst/Developer
│   │   (#ccrole-bi-analyst-developer)
│   └── Added 2026-09-22 (see 00-qa.md Q8) when Business Intelligence /
│       Reporting was split out as its own domain, to govern the risk
│       that report-level self-service models diverge from Data
│       Platform's official Semantic Layer / Data/Metadata's Metrics
│
├── **DevOps / Release Engineering** (#ccdept-devops-release-engineering)
│   ├── Ownership of Domain 7 (Workflow/Process) under revision (2026-09-22) — see
│   │   00-qa.md; each domain department is expected to own its own
│   │   workflow/CI-CD instance, with DevOps's coordinating role (if any)
│   │   not yet decided. Domain 7 itself not yet drafted.
│   └── Positional Roles: none defined yet
│
├── **AI/ML Platform** (#ccdept-ai-ml-platform)
│   ├── Owns: Domain 8 (Harness) — not yet drafted
│   └── Defines the operational boundary for System Actor: AI Agent/Harness (#ccrole-ai-agent-harness)
│
├── **Security & Compliance** (#ccdept-security-compliance)
│   ├── Cross-cutting reviewer/approver across Domains 1–9 (not an owner of any one domain)
│   └── Positional Role: Security/Compliance (#ccrole-security-compliance)
│
└── **IT Training & Change Management** (#ccdept-training-change-management)
    ├── Owns: Domain 9 (Interface/Human) — not yet drafted
    └── Positional Roles: none defined yet

**Business Function Departments** (added 2026-09-22, see 00-qa.md Q9) —
hold Data Owner authority over Data/Metadata's Business Glossary Terms/
Metrics for their function, rather than owning a technical domain:

- **Marketing** (#ccdept-marketing) — Marketing Data Domain (campaigns, leads, attribution)
- **Sales** (#ccdept-sales) — Sales Data Domain (pipeline, opportunities)
- **Finance & Accounting** (#ccdept-finance-accounting) — Finance Data Domain (revenue, cost, margin); GAAP/IFRS/SOX/ASC 606
- **Human Resources** (#ccdept-human-resources) — HR/Employee Data Domain; EEOC/FLSA/ADA/FMLA/ISO 30414
- **Legal** (#ccdept-legal) — Legal/Regulatory Data Domain; now the Data Owner for Data/Metadata's Legal Hold (#data-legal-hold) and Data Privacy & Regulatory terms; EDRM/GDPR/CCPA

**Generic Functional Roles** (not department-fixed — context-dependent,
per transaction): Requester (#ccrole-requester), Approver
(#ccrole-approver).

**System Actors** (outside the human org chart): AI Agent/Harness
(#ccrole-ai-agent-harness), scoped by the AI/ML Platform department once
Harness (domain 8) is drafted.

---

**Illustrative, not prescriptive** — see 02-taxonomies.md's Department ↔
Domain Alignment note. An adopting organization substitutes its own actual
department names/groupings; the Role↔Domain relationships are the
load-bearing part this framework asserts.
