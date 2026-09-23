# Q&A Log — Access Rules
# Append-only. Do not edit past entries; add new dated entries instead.

## AR-Q1 — AI agent/harness provisioning authority
- Type: Judgment (org-decision, AI-safety relevant) · Required · Human-only
- Options presented: AI may only request, human approval always required /
  AI may autonomously provision Dev/Staging only, never Production /
  AI has no provisioning capability, read-only/advisory only
- AI recommendation: AI may only request; human approval always required
  for Production — no special AI exemption from POL-5
- Human answer: explicitly selected recommended default
- Decision-weight: High (directly relevant to the project's core purpose
  — safe AI enablement, not just infrastructure documentation)
- Resulting rule: AR-1
- Date answered: 2026-09-22

## AR-Q2 — Hard-block override authority
- Type: Judgment (org-decision) · Required · Human-only
- Options presented: Infrastructure Admin only / Any designated Approver /
  No override permitted
- AI recommendation: Infrastructure Admin role only — narrow, auditable
- Human answer: explicitly selected recommended default
- Decision-weight: High
- Resulting rule: AR-2
- Date answered: 2026-09-22

## AR-Q3 — Production provisioning approver
- Type: Judgment (org-decision) · Required · Human-only
- Options presented: Designated Approver role (separate from Requester) /
  Infrastructure Admin only
- AI recommendation: Designated Approver role — separation of duties
- Human answer: explicitly selected recommended default
- Decision-weight: High
- Resulting rule: AR-3
- Date answered: 2026-09-22

## AR-Q4 — Decommissioning sanitization sign-off
- Type: Judgment (org-decision) · Required · Human-only
- Options presented: Infrastructure Admin or Security/Compliance role /
  Any Approver / Self-certified by Requester
- AI recommendation: Infrastructure Admin or Security/Compliance role
- Human answer: explicitly selected recommended default
- Decision-weight: Medium
- Resulting rule: AR-4
- Date answered: 2026-09-22

## Q9.y — Cross-column revision: AR-2 two-person sign-off for High risk
- Date: 2026-09-22
- Context: Risk Tiers (column 9) introduced a two-person sign-off
  requirement for High-risk break-glass overrides, contradicting AR-2's
  original "Infrastructure Admin alone" rule.
- Human answer: confirmed — update AR-2 to add the two-person rule
- Resolution: AR-2 now requires Infrastructure Admin alone for Low/
  Moderate risk, Infrastructure Admin + Security/Compliance for High risk
- Decision-weight: High
- Date answered: 2026-09-22

## Q-cc.1 — Retrofit: AR-1/AR-2/AR-3 converted to extend cross-cutting access rules
- Date: 2026-09-22
- Context: same retrofit as Policies (see 06-policies.qa.md Q-cc.1) —
  AR-1 (AI agent authority), AR-2 (break-glass override), AR-3 (provisioning
  approval separation of duties) are genuinely universal.
- Resolution: cross-cutting/access-rules.md created (CCAR-1, CCAR-2,
  CCAR-3); AR-1, AR-2, AR-3 updated to "Extends: CCAR-X". AR-4
  (decommissioning sign-off) remains domain-specific.
- Decision-weight: High
- Date answered: 2026-09-22

## 2026-09-22 — Retrofit: Roles & Departments established as cross-cutting pillar

**Context:** User paused before Workflow/Process to vet the role-vocabulary
gap. Roles & Departments became a third cross-cutting pillar (alongside
Governance, Security) instead of waiting for the Interface/Human domain.

**Change:** The "Provisional Role Vocabulary" table replaced with links
to cross-cutting/roles-and-departments/01-definitions.md's real anchored
terms (Requester, Approver, Infrastructure Admin, Security/Compliance,
AI Agent/Harness). No change to AR-1 through AR-4's rules themselves.
