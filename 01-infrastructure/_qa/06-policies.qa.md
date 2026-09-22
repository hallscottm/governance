# Q&A Log — Policies
# Append-only. Do not edit past entries; add new dated entries instead.

## Process note
- Unlike Definitions/Taxonomies/Ontologies/Metadata Standards/Conventions,
  Policies questions were NOT bulk-drafted-and-vetoed. Each was asked as a
  real judgment question with bounded options, since these are genuine
  org risk-tolerance decisions, not standards lookups.
- Human explicitly confirmed before answering that this Q&A process (the
  questions, the options presented, the chosen answer) is documented in
  this file, not just discussed in conversation. Confirmed: yes, this is
  standard practice for every column in this framework.

## P1 — Metadata completeness enforcement (Production)
- Type: Judgment (org-decision) · Required · Human-only
- Options presented: Hard block / Soft warn / No enforcement yet
- AI recommendation: Hard block, for Production only
- Human answer: accepted recommended default (Hard block)
- Decision-weight: High
- Resulting policy: POL-1
- Date answered: 2026-09-22

## P2 — Minimum Availability Tier for Production
- Type: Judgment (org-decision) · Required · Human-only
- Options presented: Tier III minimum / Tier II minimum / No minimum, case-by-case
- AI recommendation: Tier III minimum
- Human answer: "[No preference]" — treated as accepting recommended default (Tier III)
- Decision-weight: High
- Resulting policy: POL-2
- Date answered: 2026-09-22

## P3 — DR Tier requirement for Production
- Type: Judgment (org-decision) · Required · Human-only
- Options presented: Required for all Production / Required only for
  critical workloads / Optional, recommended only
- AI recommendation: Required for all Production (avoids needing an
  undefined criticality classification)
- Human answer: "[No preference]" — treated as accepting recommended
  default (Required for all Production)
- Decision-weight: High
- Resulting policy: POL-3
- Date answered: 2026-09-22

## P4 — Decommissioning sanitization standard
- Type: Judgment (org-decision) · Required · Human-only
- Options presented: NIST SP 800-88 compliant / Basic deletion / Not yet defined
- AI recommendation: NIST SP 800-88 compliant (consistent with Definitions citation)
- Human answer: "[No preference]" — treated as accepting recommended
  default (NIST SP 800-88)
- Decision-weight: Medium
- Resulting policy: POL-4
- Date answered: 2026-09-22

## P5 — Provisioning approval requirement
- Type: Judgment (org-decision) · Required · Human-only
- Options presented: Production requires approval, others self-service /
  All environments require approval / Self-service everywhere, audited after
- AI recommendation: Production requires approval, others self-service —
  explicitly noted as balancing safety against the project's anti-burnout goal
- Human answer: explicitly selected recommended default (not a "no
  preference" — directly chosen)
- Decision-weight: High
- Resulting policy: POL-5
- Date answered: 2026-09-22

## P6 — Cost Center Tag enforcement
- Type: Judgment (org-decision) · Required · Human-only
- Options presented: Blocked if untagged / Allowed but flagged / No enforcement
- AI recommendation: Blocked if untagged — keeps consistency with Metadata
  Standards' existing "Required — always" designation
- Human answer: explicitly selected recommended default
- Decision-weight: High
- Resulting policy: POL-6
- Date answered: 2026-09-22

## Q9.x — Cross-column revision: POL-2/POL-3 scaled by Risk Tier
- Date: 2026-09-22
- Context: drafting Risk Tiers (column 9) surfaced that POL-2/POL-3's
  flat "all Production" rules didn't differentiate risk levels.
- Human answer: confirmed — update POL-2/POL-3 to scale with Risk Tier
- Resolution: POL-2 now Tier II/III/IV minimum by Low/Moderate/High risk;
  POL-3 now Recommended/Required/Required by Low/Moderate/High risk
- Decision-weight: High
- Date answered: 2026-09-22
