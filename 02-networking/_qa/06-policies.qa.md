# Q&A Log — Policies
# Append-only. Do not edit past entries; add new dated entries instead.

## Process note
- Before drafting, surfaced and resolved a structural question: should
  universal policies (metadata completeness, cost tag, provisioning
  approval) be cross-cutting rather than redrafted per layer? Human
  confirmed yes — see cross-cutting/policies.md and the retrofit logged
  in 01-infrastructure/_qa/06-policies.qa.md (Q-cc.1).
- This layer's Policies column therefore extends CCP-1/CCP-2/CCP-3
  without restating them, and adds only genuinely Networking-specific
  policies.

## NQ1 — Default network posture for Production
- Type: Judgment (org-decision) · Required · Human-only
- Options presented: Default-deny / Default-allow
- AI recommendation: Default-deny — standard security best practice
- Human answer: explicitly selected recommended default
- Decision-weight: High
- Resulting policy: NPOL-1
- Date answered: 2026-09-22

## NQ2 — Encryption in transit requirement
- Type: Judgment (org-decision) · Required · Human-only
- Options presented: Required for all Production traffic / Required only
  cross-boundary / Recommended, not required
- AI recommendation: Required for all Production traffic
- Human answer: explicitly selected recommended default
- Decision-weight: High
- Resulting policy: NPOL-2
- Date answered: 2026-09-22

## NQ3 — Public exposure additional approval
- Type: Judgment (org-decision) · Required · Human-only
- Options presented: Yes, additional approval required / No, covered by
  standard CCP-3
- AI recommendation: Yes — public exposure is categorically different risk
- Human answer: explicitly selected recommended default
- Decision-weight: High
- Resulting policy: NPOL-3
- Date answered: 2026-09-22
