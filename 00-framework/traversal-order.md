# Traversal Order

Status: Draft
Ratified: No
Last updated: 2026-09-22

## Row-major, with a reconciliation safeguard

Fill order: complete all columns for Domain 1 (Infrastructure) before
starting Domain 2 (Networking), and so on, in ascending # order per the
domain axis definition (00-framework/domain-axis-definition.md).

After each domain's Definitions column (column 1) is completed, run a
terminology reconciliation pass: compare the new domain's Definitions
against all previously completed domains' Definitions, flag collisions
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
  (correction vs. evolution, versioning scheme, dependent-domain
  re-validation flags)
- Migration path from file-based source of truth to a queryable
  structured store (e.g. for harness runtime consumption)
