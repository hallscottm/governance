# Q&A Log — Conventions
# Append-only. Do not edit past entries; add new dated entries instead.

## 2026-09-22 — Q7.6: Naming conventions and scaffolding diagrams

**Bucket:** [Org-decision]/Human-only for the diagram approach itself
(confirmed with the user before drafting — Mermaid embedded in markdown,
not separate image files or an external tool); [Standard]/AI-draftable
for the diagram content and naming patterns within that agreed approach.

**Answer:** Repository naming reuses System Architecture's Service
pattern exactly (a Repository typically holds one Service). Four Mermaid
diagrams: CI/CD Pipeline Flow, Environment Promotion Flow, an
illustrative Data Pipeline Orchestration DAG, and an Incident Lifecycle
state diagram — each tied explicitly to specific Definitions/Policies
anchors rather than standing as generic illustrations, so a rename stays
a find-and-replace rather than a redraw. Repository Scaffolding shown as
a plain fenced-code directory tree rather than forced into Mermaid,
since a tree structure renders more clearly as plain text.

**Status:** Pending explicit review.
