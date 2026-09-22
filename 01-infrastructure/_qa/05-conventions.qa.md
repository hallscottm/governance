# Q&A Log — Conventions
# Append-only. Do not edit past entries; add new dated entries instead.

## Q5.1 — Resource naming pattern
- Type: Judgment (org-decision) · Required · Human-only
- Options presented: <env>-<compute-env>-<service>-<seq> / UUID + separate
  display-name tag / custom
- AI recommendation: <env>-<compute-env>-<service>-<seq>, citing common
  cloud provider guidance (AWS tagging strategy, Azure CAF)
- Human answer: accepted recommended default
- Decision-weight: High (becomes the standard for all future resource
  naming; hard to change retroactively once resources are named)
- Resulting artifact: 05-conventions.md, Resource Naming Convention section
- Date answered: 2026-09-22

## Q5.2 — Tag key format, abbreviation registry, scope boundary
- Type: Fact/Judgment mix · Bulk-draft-and-veto · AI-draftable
- Drafted: tag key naming rules (kebab-case, locked to Metadata Standards
  registry), abbreviation registry (9 entries), explicit scope boundary
  excluding code/repo conventions (deferred to Workflow/Process layer)
- Human answer: pending explicit review (drafted, not yet vetted)
- Decision-weight: Low (per-item); Medium (scope-boundary decision)
- Open items flagged inline: <service> vocabulary left org-specific;
  AI-compute naming distinction deferred
- Date answered: 2026-09-22 (drafted; awaiting explicit human review)

## Q5.2 — Confirmation
- Date: 2026-09-22
- Human accepted tag-key rules and abbreviation registry as drafted, no
  line-by-line vetoes. Open items (service vocabulary, AI-compute naming
  distinction) remain flagged, not resolved.
- Decision-weight: Low (now closed)
