# Harness Domain — Policies

Status: Draft — pending review
Ratified: No
Last updated: 2026-09-23
Provenance: see _qa/06-policies.qa.md
Built on: 01-definitions.md, 04-metadata-standards.md, cross-cutting/policies.md, cross-cutting/access-rules.md, cross-cutting/risk-tiers.md

## Extends Cross-Cutting Policies and Access Rules

This domain's resources are subject to CCP-1 (Metadata Completeness),
CCP-2 (Cost Attribution), and CCP-3 (Production Provisioning Approval)
from cross-cutting/policies.md, applied to this domain's own entity types
(04-metadata-standards.md). Not restated here.

This domain is also where CCAR-1 (AI Agent/Harness Provisioning
Authority) — an AI agent/harness may never itself grant final approval
for a Production resource — is exercised most directly: every Agent this
domain governs *is* the actor CCAR-1 constrains. HPOL-3 below is this
domain's own mechanism implementing that cross-cutting rule at
instance-level, Risk-Tier-scaled granularity.

## Domain-Specific Policies

### HPOL-1 — Production Tool Permission Requires Prior Sandbox Testing
**Rule:** An Agent's Tool Permission Scope cannot include a
Production-scoped Tool grant until that exact Capability Scope/Tool
Permission Scope combination has been exercised in a Sandbox
(`cc-sandbox`) and passed a corresponding Eval Suite Run.
**Applies to:** Production environment, Agent entity type.
**Enforcement:** Hard block.
**Rationale:** The specific case cross-cutting/sandbox-activation.md's
Primary Uses section named as the reason Sandbox was resolved when it
was — "testing an Agent's configuration... in a Sandbox before granting
it Production-scoped Capability Scope."

### HPOL-2 — Model Version Pin Change Requires a Passing Eval Suite Run
**Rule:** An Agent's Model Version Pin cannot change (for a
Production-environment Agent) without a passing Eval Suite Run against
the new version first — a Behavioral Drift baseline reset, not just a
version bump.
**Applies to:** Production environment (hard block); Dev/Staging
(recommended, not blocking).
**Enforcement:** Hard block (Production); recommended elsewhere.
**Rationale:** Mirrors HPOL-1's logic applied to a version change rather
than a scope change — an untested model version is exactly as
unvalidated as an untested Capability Scope.

### HPOL-3 — Human-in-the-Loop Gate Required for High Risk Tier Actions
**Rule:** An Autonomous- or Multi-Agent-type Agent's proposed action at
High Risk Tier (09-risk-tiers.md) must pass a Human-in-the-Loop Gate
before executing. Assistant-type Agents are exempt from this specific
policy — a human already initiated the request that led to the action,
so the human-in-the-loop requirement is satisfied by the request itself,
not a separate gate.
**Applies to:** Autonomous, Multi-Agent Agent Types; High Risk Tier;
Production environment.
**Enforcement:** Approval gate.
**Rationale:** This is the domain-specific, Risk-Tier-scaled mechanism
implementing CCAR-1's blanket rule that an Agent can never be its own
final Production approver — CCAR-1 says an AI agent may never grant
itself final approval; this policy says precisely when a human approval
step is required to exist at all for an autonomous Agent's action.

### HPOL-4 — Guardrail Violation Triggers Automatic Rate Limit Escalation
**Rule:** A detected Guardrail violation (a Content Filter match, or an
Action Allowlist/Denylist violation) automatically tightens that Agent's
Agent Rate Limit until a human review (HPROC-4, 08-procedures.md)
clears it — a safety circuit-breaker, distinct from a permanent
Capability Scope revocation, which is a separate, heavier decision.
**Applies to:** All environments, Agent entity type.
**Enforcement:** Automatic control (not itself approval-gated; the
review that follows is).
**Rationale:** OWASP Top 10 for LLM Applications' Unbounded
Consumption/Excessive Agency categories (00-standards-alignment.md) —
an automatic, immediate throttle is the fastest available containment
for a misbehaving Agent, faster than routing through a full
Human-in-the-Loop Gate first.

### HPOL-5 — Guardrail Override Requires Post-Hoc Review Within 24 Hours
**Rule:** Using Override/Break-glass to bypass an Agent's Guardrail
requires post-hoc review within 24 hours — the same window and pattern
Workflow/Process's WFPOL-5 established for Emergency Change — and every
such override is automatically classified High Risk Tier
(09-risk-tiers.md) regardless of what was overridden.
**Applies to:** All environments, Agent entity type, any Override/
Break-glass event.
**Enforcement:** Approval gate, timing-scoped (post-hoc rather than
pre-execution), same structural pattern as WFPOL-5.
**Rationale:** CCPROC-4's break-glass override already covers bypassing
a hard block generally; this policy is the domain-specific instance of
that pattern applied to an Agent's Guardrail specifically, with the
same audit-trail discipline.

---

**Cross-references:**
- HPOL-3 is this domain's implementation of CCAR-1's blanket "no AI
  self-approval" rule — CCAR-1 defines the constraint, HPOL-3 defines
  when the corresponding human gate must exist.
- HPOL-1 and HPOL-2 both depend on `cc-sandbox` and `harness-eval-suite`
  respectively — the two mechanisms this domain's Standards Alignment and
  Definitions columns flagged as central to a safe Production promotion
  path.
- HPOL-5 deliberately reuses Workflow/Process's WFPOL-5 shape (post-hoc
  approval window) rather than inventing a new one — same judgment this
  framework applied whenever a genuinely equivalent pattern already
  existed elsewhere (WFAR-1 reusing CCAR-3's escalation shape).

**Open items:**
- Who qualifies as reviewer/approver for each of these five policies is
  deferred to Access Rules (column 7), next.
- HPOL-5's 24-hour window is a generalized default, explicitly
  adjustable per an org's own incident/change management practice — same
  treatment WFPOL-5's window received.

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — 5 domain-specific policies plus inherited cross-cutting ones
- [x] Modular — each HPOL stands alone
- [x] Easy to update — cross-cutting rules update once, apply here automatically
- [x] Easy to maintain — every policy traces to a specific term/field; HPOL-3 explicitly implements CCAR-1
- [x] Easy to replace — enforcement mechanisms deferred to Procedures/Tooling where tool-specific
