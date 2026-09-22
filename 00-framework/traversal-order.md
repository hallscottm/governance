# Traversal Order

Status: Draft
Ratified: No
Last updated: 2026-09-22

## Row-major, with a reconciliation safeguard

Fill order: complete all columns for Layer 1 (Infrastructure) before
starting Layer 2 (Networking), and so on, bottom-to-top per the layer
axis definition.

After each layer's Definitions column (column 1) is completed, run a
terminology reconciliation pass: compare the new layer's Definitions
against all previously completed layers' Definitions, flag collisions
or near-duplicate terms.

## Q&A provenance rule

Each cell's '_qa/<column>.qa.md' record is append-only: once a question
is answered, that record is not edited in place. A later change in
understanding is logged as a new, dated entry rather than overwriting
the original — the output document (e.g. '01-definitions.md') is what
gets updated/versioned normally; the Q&A file is the historical record
of how it got there.

## Open items (future phases, not yet designed)

- State/history management for ratified content that changes later
  (correction vs. evolution, versioning scheme, dependent-layer
  re-validation flags)
- Migration path from file-based source of truth to a queryable
  structured store (e.g. for harness runtime consumption)
