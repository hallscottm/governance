# Q&A Log — Metadata Standards
# Append-only. Do not edit past entries; add new dated entries instead.

## Q4.1 — Schema shape: shared registry vs. per-entity-type schemas
- Type: Judgment (structural) · Required · AI-draftable
- Options presented: shared field registry + applicability matrix / separate
  full schema per entity type
- AI recommendation: shared registry + matrix (DRY, consistent with the
  rest of the framework)
- Human answer: accepted recommended default
- Decision-weight: Medium (governs metadata-standards structure for all
  future domains)
- Date answered: 2026-09-22

## Q4.2 — Field registry and entity-type matrix content
- Type: Fact/Judgment mix · Bulk-draft-and-veto · AI-draftable
- 14 fields defined, referencing existing Definitions-column terms; 4
  entity types (Compute Unit general, AI-Specific Compute, Storage
  Instance, Physical Asset) mapped to required/optional fields
- Human answer: pending explicit review (drafted, not yet vetted line-by-line)
- Decision-weight: Low (per-field); Medium (as a structural pass)
- Open items flagged inline: Networking-domain metadata explicitly out of
  scope; enforcement mechanism deferred to Policies column (6)
- Date answered: 2026-09-22 (drafted; awaiting explicit human review)

## Q4.2 — Confirmation
- Date: 2026-09-22
- Human accepted the field registry and entity-type matrix as drafted, no
  line-by-line vetoes. Open items (Networking scope, enforcement deferral
  to Policies) remain flagged, not resolved.
- Decision-weight: Low (now closed)
