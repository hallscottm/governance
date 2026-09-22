# Q&A Log — Procedures
# Append-only. Do not edit past entries; add new dated entries instead.

## Process note
- Procedures were bulk-drafted, not asked as individual questions — these
  are mechanical derivations of already-decided Policies (column 6) and
  Access Rules (column 7), not new judgment calls. Consistent with the
  two-bucket model established during Definitions: [Standard]/derived
  content gets bulk-drafted-and-vetoed, genuine org-decisions get asked
  directly (as Policies and Access Rules were).

## Q8.1 — Six procedures drafted
- Type: Fact/derived · Bulk-draft-and-veto · AI-draftable
- Procedures: PROC-1 (Production provisioning), PROC-2 (metadata
  validation), PROC-3 (tier verification), PROC-4 (decommissioning
  sanitization), PROC-5 (break-glass override), PROC-6 (untagged resource
  handling)
- Human answer: pending explicit review (drafted, not yet vetted)
- Decision-weight: Low (per-procedure, since each derives mechanically
  from already-approved policies); Medium (as a structural pass)
- Open items flagged inline: PROC-3 makes a working assumption (Requester
  sets DR Tier) pending the unresolved Access Rules gap; approval SLA and
  notification mechanism deferred to Tooling (column 10)
- Date answered: 2026-09-22 (drafted; awaiting explicit human review)

## Q8.2 — Review: who sets DR Tier?
- Type: Judgment (org-decision) · Required · Human-only
- Options presented: Requester proposes, Approver confirms (folds into
  PROC-1) / Requester self-declares, no review / Infrastructure Admin
  sets independently
- AI recommendation: Requester proposes, Approver confirms — no new
  role/process needed
- Human answer: accepted recommended default
- Decision-weight: Medium
- Resolution: PROC-1 and PROC-3 updated — DR Tier is proposed at
  submission, confirmed/adjusted during existing Approver review
- Date answered: 2026-09-22

## Q8.3 — Review: SLA/notification scope
- Type: Judgment (structural) · Required · Human-only
- Options presented: keep deferred to Tooling (column 10) / define here
  in Procedures regardless of tooling
- AI recommendation: keep deferred — avoids a sync burden if tooling changes
- Human answer: accepted recommended default
- Decision-weight: Low
- Resolution: confirmed as intentional boundary, not an oversight — open
  items note in 08-procedures.md updated to reflect this
- Date answered: 2026-09-22

## Q-cc.1 — Retrofit: PROC-1/PROC-2/PROC-5/PROC-6 converted to extend cross-cutting procedures
- Date: 2026-09-22
- Context: same retrofit pattern as Policies/Access Rules — closing the
  open item logged when cross-cutting/policies.md was first created,
  which flagged Procedures as the next candidate once a second layer
  needed the same steps.
- Resolution: cross-cutting/procedures.md created (CCPROC-1 through
  CCPROC-4); PROC-1, PROC-2, PROC-5, PROC-6 updated to "Extends: CCPROC-X".
  PROC-3 (tier verification) and PROC-4 (decommissioning) remain
  layer-specific.
- Decision-weight: High (governs Procedures structure for all future layers)
- Date answered: 2026-09-22
