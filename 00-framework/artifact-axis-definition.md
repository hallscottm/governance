# Artifact Axis Definition

Status: Draft
Ratified: No
Last updated: 2026-09-22

The column axis of the framework matrix. Columns are filled left-to-right
within a domain, since each artifact type depends on the one(s) before it.

| Order | Artifact Type | Captures | Depends on |
|---|---|---|---|
| 1 | Definitions | Core vocabulary/glossary | nothing (foundation) |
| 2 | Taxonomies | Classification/hierarchy of defined terms | Definitions |
| 3 | Ontologies | Relationships/rules between classified entities | Taxonomies |
| 4 | Metadata Standards | How real instances get tagged/described | Ontologies |
| 5 | Conventions | Naming, structure, scaffolding, formatting | Definitions + Taxonomy |
| 6 | Policies | Rules — required/allowed/forbidden | Definitions + Ontology |
| 7 | Access Rules | Who/what can see or act | Policies |
| 8 | Procedures (SOPs) | Step-by-step execution of a policy | Policies |
| 9 | Risk Tiers | Risk classification, regulatory mapping | Policies + Taxonomy |
| 10 | Tooling / Implementation | Tools/apps chosen to implement the above | all prior columns (filled last) |

A Standards Alignment reference panel (established external standards
relevant to the domain) is reviewed before column 1 and is not itself
'data' to fill in — it seeds columns 1-2 with existing vocabulary.
