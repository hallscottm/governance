# Q&A Log — Ontologies
# Append-only. Do not edit past entries; add new dated entries instead.

## Q3.1 — Bulk-draft relationships, including cross-layer
- Type: Fact/Judgment mix · Bulk-draft-and-veto · AI-draftable
- ~26 relationships drafted across 7 groupings, including 3 genuine
  cross-layer relationships into Infrastructure (net-load-balancer and
  net-reverse-proxy runs-on infra-compute-unit; net-bandwidth constrains
  infra-throughput)
- Human answer: pending explicit review
- Decision-weight: Low (per-relationship); Medium (structural pass)
- Date answered: 2026-09-22 (drafted; awaiting explicit human review)

## Q3.2 — Reverse pointers for cross-layer ontology relationships
- Type: Judgment (structural) · Required · Human-only
- Options presented: add reverse pointers as a standard framework rule /
  one-directional is fine
- AI recommendation: add reverse pointers — same discipline as
  Definitions' "Referenced by" tag
- Human answer: accepted recommended default
- Decision-weight: High (governs ontology structure for all future
  cross-layer relationships, not just this instance)
- Resolution: 00-framework/relation-types.md updated with the rule;
  01-infrastructure/03-ontologies.md updated with actual reverse pointers
- Date answered: 2026-09-22

## Q3.1 — Confirmation
- Date: 2026-09-22
- Human accepted all ~26 relationships as drafted, no line-by-line vetoes.
- Decision-weight: Low (now closed)
