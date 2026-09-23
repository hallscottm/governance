# Q&A Log — Access Rules
# Append-only. Do not edit past entries; add new dated entries instead.

## 2026-09-22 — Q4.5: Domain-specific access rules, including a migration and the first Business Function Department-routed rule

**Bucket:** [Org-decision]/Human-only for role assignment; [Standard]/
AI-draftable for structure, mirroring System Architecture's Access Rules.

**Answers:**
- DPPAR-1 (migrated from SAAR-1): authority updated from Owning Team Lead
  to Data Engineer (Moderate+)/Data Architect (High), reflecting Data
  Architect/Data Engineer's design/build split (00-qa.md Q7 in
  cross-cutting/roles-and-departments/).
- DPPAR-2 (lakehouse table format change authority): Data Engineer (all
  tiers), Data Architect additionally at High.
- DPPAR-3 (semantic layer change authority): Analytics Engineer for
  mechanics; Metric's Data Owner notified (not blocking) for
  meaning-altering changes — the first Access Rule in this framework to
  route through a Business Function Department's Data Owner rather than a
  purely technical role, a concrete instance of Q9's resolution actually
  being exercised.

**Status:** Pending explicit review.
