# Q&A Log — Metadata Standards
# Append-only. Do not edit past entries; add new dated entries instead.

## Process note
- Reused Infrastructure's established shape (shared field registry +
  entity-type applicability matrix) without re-asking — already decided
  as the standard approach.
- First instance of cross-domain field reuse: Resource ID, Cost Center Tag,
  Compute Environment, Environment (lifecycle) referenced from
  Infrastructure rather than redefined. Caught and fixed a broken link
  during drafting (Metadata Standards has no field-level anchors of its
  own; corrected to point at the underlying Definitions anchor instead).
  Flagged as a framework-level gap (no reverse-pointer mechanism at the
  Metadata Standards field level), not resolved — lower urgency than the
  Ontology reverse-pointer gap since it's discoverable but not yet causing
  real confusion.

## Q4.1 — Field registry and entity-type matrix content
- Type: Fact/Judgment mix · Bulk-draft-and-veto · AI-draftable
- 6 new fields defined (CIDR Block, Associated VPC, Network Zone, Trust
  Boundary Classification, DNS Zone Name, Connectivity Type), 3 fields
  referenced from Infrastructure, 6 entity types mapped
- Human answer: pending explicit review
- Decision-weight: Low (per-field); Medium (structural pass)
- Date answered: 2026-09-22 (drafted; awaiting explicit human review)
