# Q&A Log — Ontologies
# Append-only. Do not edit past entries; add new dated entries instead.

## Q3.1 — Relationship type vocabulary
- Type: Judgment (structural) · Required · AI-draftable
- Options presented: 9-type core set / smaller essentials-only set / custom
- AI recommendation: 9-type core set (runs-on, contains, located-in,
  requires, constrains, measured-by, consumes/produces, scales-via,
  has-lifecycle-state)
- Human answer: accepted recommended default
- Decision-weight: High (governs ontology structure for all 7 layers)
- Resulting artifact: 00-framework/relation-types.md
- Date answered: 2026-09-22

## Q3.2 — Bulk-draft relationships for Infrastructure
- Type: Fact/Judgment mix · Bulk-draft-and-veto · AI-draftable
- ~35 relationships drafted across 8 groupings (Virtualization & Compute
  Stack, Compute Hardware Composition, AI-Specific Compute, Placement/
  Facility, Capacity & Scaling, Storage, Resilience & Availability,
  Lifecycle, Cost/FinOps)
- Human answer: pending review (not yet explicitly vetted line-by-line)
- Decision-weight: Low (per-relationship); Medium (as a structural pass)
- Open items flagged inline: conditional truth of compute-unit/rack
  relationship (public cloud vs. on-prem), and Availability Tier II/III/IV
  redundancy relationships noted once rather than four times
- Date answered: 2026-09-22 (drafted; awaiting explicit human review)

## Q3.2 — Confirmation
- Date: 2026-09-22
- Human accepted the ~35 drafted relationships as-is, no line-by-line
  vetoes. Open items (rack conditional truth, Tier II-IV redundancy
  shorthand) remain flagged in 03-ontologies.md for future revisit, not
  resolved.
- Decision-weight: Low (now closed)
