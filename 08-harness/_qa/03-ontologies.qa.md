# Q&A Log — Ontologies
# Append-only. Do not edit past entries; add new dated entries instead.

## 2026-09-23 — Q8.5: Cross-domain relationships and reverse pointers

**Bucket:** [Standard]/AI-draftable, following the established
reverse-pointer discipline (00-framework/relation-types.md).

**Answer:** 21 relationships drawn (grouped by subdomain), 5 cross-domain
edges outbound (Infrastructure x3 — Model-Serving Node, Inference
Workload x2; Data Platform x1 — Database as a Retrieval Source backing
store), plus 1 inbound edge from Workflow/Process
(`wf-postmortem --[consumes]--> harness-agent-incident`, added
retroactively to 07-workflow-process/03-ontologies.md). Reverse pointers
added to 01-infrastructure/03-ontologies.md and
04-data-platform/03-ontologies.md's Cross-Domain References sections.
Deliberately did *not* draw an edge from `harness-agent` to
`ccrole-ai-agent-harness` — two views of the same thing, kept as a
reference-stub boundary rather than an ontology relationship, same
treatment Database's usage/ownership split received.

**Applied to:** 03-ontologies.md; 01-infrastructure/03-ontologies.md;
04-data-platform/03-ontologies.md; 07-workflow-process/03-ontologies.md.

**Status:** Pending explicit review.
