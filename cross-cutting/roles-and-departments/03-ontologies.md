# Cross-Cutting: Roles & Departments — Ontologies

Status: Draft — pending review
Ratified: No
Last updated: 2026-09-22
Provenance: see 00-qa.md in this directory
Relation vocabulary: 00-framework/relation-types.md
Built on: 01-definitions.md, 02-taxonomies.md

Department↔Domain alignment is recorded as a table in 02-taxonomies.md,
not here — domains aren't anchored Definitions terms, so they can't
participate in a `--[relation]-->` edge. Everything below relates Roles,
Departments, and Governance Bodies to each other.

---

## Core Structure

- `ccorg-org-chart` --[contains]--> `ccdept-department`
  Rationale: the org chart is composed of the departments within it (conceptual — see Taxonomy for the actual department list, not repeated as individual edges here).
- `ccdept-department` --[contains]--> `ccrole-positional-role`
  Rationale: a department is composed of the positional roles that belong to it.
- `ccgov-governance-body` --[contains]--> `ccdept-department`
  Rationale: a governance body is convened from representatives of multiple departments.

## Role Types

- `ccrole-role` --[contains]--> `ccrole-human-role`
  Rationale: Human Role is one of the two Role Type values.
- `ccrole-role` --[contains]--> `ccrole-system-actor`
  Rationale: System Actor is the other Role Type value.
- `ccrole-role` --[contains]--> `ccrole-positional-role`
  Rationale: Positional Role is one of the two Role membership models.
- `ccrole-role` --[contains]--> `ccrole-functional-role`
  Rationale: Functional Role is the other Role membership model.
- `ccrole-positional-role` --[requires]--> `ccdept-department`
  Rationale: a positional role only exists in the context of a specific department membership.
- `ccrole-functional-role` --[constrains]--> `ccrole-requester`
  Rationale: the Functional Role concept is what defines Requester as context-dependent rather than department-fixed.
- `ccrole-functional-role` --[constrains]--> `ccrole-approver`
  Rationale: same reasoning — Approver is a functional, not positional, role.

## Positional Role → Department Membership

- `ccrole-infrastructure-admin` --[requires]--> `ccdept-platform-engineering`
  Rationale: Infrastructure Admin only exists as a member of Platform Engineering.
- `ccrole-security-compliance` --[requires]--> `ccdept-security-compliance`
  Rationale: Security/Compliance only exists as a member of the Security & Compliance department.
- `ccrole-owning-team-lead` --[requires]--> `ccdept-application-engineering`
  Rationale: Owning Team Lead's typical home department, per Definitions (though not exclusive — flagged there).
- `ccrole-data-architect` --[requires]--> `ccdept-data-governance-engineering`
  Rationale: Data Architect only exists as a member of Data Governance & Engineering.
- `ccrole-data-engineer` --[requires]--> `ccdept-data-governance-engineering`
  Rationale: Data Engineer only exists as a member of Data Governance & Engineering.
- `ccrole-data-architect` --[constrains]--> `ccrole-data-engineer`
  Rationale: added 2026-09-22 (see 00-qa.md Q7) — the two roles co-own Data Platform but with distinct scope: Architect defines the design a Engineer builds/operates against, so Architect decisions bound what Engineer implements. Not a separation-of-duties rule like Approver/Requester — both roles can be held by the same person on a small team; this only captures the design-precedes-build relationship.
- `ccrole-analytics-engineer` --[requires]--> `ccdept-data-governance-engineering`
  Rationale: added 2026-09-22 (see 00-qa.md Q8) — Analytics Engineer only exists as a member of Data Governance & Engineering.
- `ccrole-business-analyst-report-builder` --[requires]--> `ccdept-business-intelligence-analytics`
  Rationale: added 2026-09-22 (see 00-qa.md Q8) — Business Analyst/Report Builder only exists as a member of Business Intelligence & Analytics.
- `ccrole-bi-analyst-developer` --[requires]--> `ccdept-business-intelligence-analytics`
  Rationale: added 2026-09-22 (see 00-qa.md Q8) — BI Analyst/Developer only exists as a member of Business Intelligence & Analytics.
- `ccrole-analytics-engineer` --[requires]--> `dp-semantic-layer`
  Rationale: cross-domain, added 2026-09-22 — Analytics Engineer's defining responsibility is building/maintaining the Semantic Layer; the role doesn't make sense without that artifact existing.
- `ccrole-bi-analyst-developer` --[constrains]--> `ccrole-business-analyst-report-builder`
  Rationale: added 2026-09-22 (see 00-qa.md Q8) — BI Analyst/Developer is typically who reviews and promotes a Business Analyst's self-service model to Certified status; not a hard separation-of-duties rule, but the same "design/review precedes build" shape as Data Architect constraining Data Engineer above.

## Business Function Department → Data Owner Authority

No formal ontology edges drawn here, by design — added 2026-09-22 (see
00-qa.md Q9). Each Business Function Department's Data Owner authority is
scoped to its own Data Domain (Marketing's authority over the Marketing
Data Domain, Finance's over the Finance Data Domain, etc.), and
`data-owner` is a single generic role instantiated per-domain, not one
department's exclusive property — forcing a `requires` edge from
`data-owner` to any one department would misrepresent it as exclusive.
Consistent with the "not every term needs a relationship" scope note
(00-framework/relation-types.md) — the department-to-domain mapping is
captured as prose in 01-definitions.md and the alignment table in
02-taxonomies.md instead.

## Separation of Duties

- `ccrole-approver` --[constrains]--> `ccrole-requester`
  Rationale: the same actor cannot hold both roles on a single transaction (CCAR-2's separation-of-duties rule) — the Approver role definitionally constrains who may simultaneously be the Requester.

## System Actor Boundary

- `ccrole-ai-agent-harness` --[constrains]--> `ccrole-approver`
  Rationale: per CCAR-1, an AI Agent/Harness may never itself hold final Production approval authority — its System Actor status constrains it out of the Approver role for that class of decision.

## Cross-Domain References (relationships pointing into this registry)

Per 00-framework/relation-types.md's reverse-pointer rule.

- `ccrole-approver`
  Referenced by (cross-domain relationships), added 2026-09-22:
  - Workflow/Process: `wf-change-request --[requires]--> ccrole-approver`

---

**Open items:**
- `ccrole-owning-team-lead --[requires]--> ccdept-application-engineering`
  states the *typical* home department, even though Definitions notes
  Owning Team Lead isn't exclusive to one department — kept as the
  primary relation since the ontology vocabulary has no "usually, but
  not exclusively" qualifier; the exception is documented in prose in
  01-definitions.md instead.

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — 24 relationships, no forced edges per individual department/role
- [x] Modular — each relationship stands alone
- [x] Easy to update — anchor-ID based, survives renames
- [x] Easy to maintain — grouped by subdomain, matches Definitions/Taxonomy
- [x] Easy to replace — relation-type vocabulary shared across all domains and this registry
