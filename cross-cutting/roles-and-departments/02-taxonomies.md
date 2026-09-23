# Cross-Cutting: Roles & Departments — Taxonomies

Status: Draft — pending review
Ratified: No
Last updated: 2026-09-22
Provenance: see 00-qa.md in this directory
Built on: 01-definitions.md (29 owned terms)

Structure: strict single-parent tree, consistent with every domain's
Taxonomies column. Only terms owned by this registry are classified here
— the 4 referenced Data/Metadata terms are not re-classified.

---

## Roles & Departments
├── Core Concepts
│   ├── Role (#ccrole-role)
│   ├── Department (#ccdept-department)
│   ├── Org Chart (#ccorg-org-chart)
│   ├── Reporting Line (#ccorg-reporting-line)
│   └── Governance Body (#ccgov-governance-body)
│
├── Role Types
│   ├── Human Role (#ccrole-human-role)
│   ├── System Actor (#ccrole-system-actor)
│   ├── Positional Role (#ccrole-positional-role)
│   └── Functional Role (#ccrole-functional-role)
│
├── Generic Functional Roles
│   ├── Requester (#ccrole-requester)
│   └── Approver (#ccrole-approver)
│
├── Generic Positional Roles
│   ├── Infrastructure Admin (#ccrole-infrastructure-admin)
│   ├── Security/Compliance (#ccrole-security-compliance)
│   ├── Owning Team Lead (#ccrole-owning-team-lead)
│   ├── Data Architect (#ccrole-data-architect)
│   ├── Data Engineer (#ccrole-data-engineer)
│   ├── Analytics Engineer (#ccrole-analytics-engineer)
│   ├── Business Analyst / Report Builder (#ccrole-business-analyst-report-builder)
│   └── BI Analyst/Developer (#ccrole-bi-analyst-developer)
│
├── System Actor Types
│   └── AI Agent/Harness (#ccrole-ai-agent-harness)
│
├── Departments
│   ├── Platform Engineering (#ccdept-platform-engineering)
│   ├── Application Engineering (#ccdept-application-engineering)
│   ├── Data Governance & Engineering (#ccdept-data-governance-engineering)
│   ├── Business Intelligence & Analytics (#ccdept-business-intelligence-analytics)
│   ├── DevOps / Release Engineering (#ccdept-devops-release-engineering)
│   ├── AI/ML Platform (#ccdept-ai-ml-platform)
│   ├── Security & Compliance (#ccdept-security-compliance)
│   └── IT Training & Change Management (#ccdept-training-change-management)
│
└── Governance Bodies
    └── Governance Council (#ccgov-governance-council)

---

## Department ↔ Domain Alignment

Not a formal Ontology relation — domains are rows defined in
00-framework/domain-axis-definition.md, not anchored Definitions terms, so
they can't be linked the way term-to-term relationships are in
03-ontologies.md. This table is the authoritative record of the
alignment instead. Many-to-many by design (confirmed 2026-09-22) — a
Department may span multiple domains, and a domain's resources may involve
more than one Department in practice (e.g., a Security & Compliance
reviewer touches every domain without owning any of them).

| Department | Primary Domain(s) | Alignment Type |
|---|---|---|
| Platform Engineering | 1 (Infrastructure), 2 (Networking) | Owns |
| Application Engineering | 3 (System Architecture) | Owns |
| Data Governance & Engineering | 4 (Data Platform), 5 (Data/Metadata) | Owns both — Data Platform (4) jointly via its Data Architect, Data Engineer, and Analytics Engineer roles (2026-09-22, replacing Application Engineering's earlier co-ownership stake, see 00-qa.md Q7/Q8); Data/Metadata (5) outright |
| Business Intelligence & Analytics | 6 (Business Intelligence / Reporting) | Owns — via Business Analyst/Report Builder and BI Analyst/Developer roles; added 2026-09-22 (see 00-qa.md Q8) |
| DevOps / Release Engineering | 7 (Workflow/Process) | Under revision — see 00-qa.md; the single-owner model shown here is being reconsidered in favor of each domain department owning its own workflow/CI-CD instance, with DevOps's exact role (cross-cutting standards owner vs. folded into Platform Engineering vs. no coordinating department) not yet decided |
| AI/ML Platform | 8 (Harness) | Owns |
| Security & Compliance | 1–9 (all domains) | Cross-cutting reviewer/approver, not an owner of any domain |
| IT Training & Change Management | 9 (Interface/Human) | Owns |

**This table is illustrative, not prescriptive:** an organization adopting
this framework may combine, split, or rename these Departments to match
its actual structure — the Roles and the domains they act on are the
load-bearing part; the specific Department groupings are a reasonable
generalized default (same posture as every other generalized/illustrative
content in this framework, e.g., the Regulatory Mapping template in every
domain's Risk Tiers column).

---

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — one tree, mirrors the 6 Definitions subdomains 1:1, plus one alignment table
- [x] Modular — referenced (not owned) terms excluded from the tree
- [x] Easy to update — a new term appends under its existing subdomain; a new Department↔Domain row appends to the alignment table
- [x] Easy to maintain — single-parent, no cross-branch duplication
- [x] Easy to replace — Department↔Domain alignment explicitly flagged as illustrative, not a hardcoded assumption
