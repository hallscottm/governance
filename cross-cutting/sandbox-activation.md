# Sandbox Activation

Status: Draft — pending review
Ratified: No
Last updated: 2026-09-22

Sandbox is not a domain — it is a constrained, safe-to-experiment copy of
the stack, one of this framework's three cross-cutting pillars alongside
Governance/Security and Roles & Departments
(00-framework/domain-axis-definition.md), expressed through the same
Policies/Access Rules/Risk Tiers columns every domain already uses rather
than through a row of its own. Deferred at the very start of this
framework's build ("no institutional knowledge yet to protect"),
resolved now that both Workflow/Process (domain 7) and Harness (domain
8) — the two domains whose resources most need something real to test
against before touching Production-adjacent systems — are being drafted.

## Definition

### Sandbox {#cc-sandbox}
An isolated, non-Production-adjacent replica of relevant resources
(Infrastructure, Data Platform, an Agent Harness) used to test a change
— a Pipeline Run, an IaC Plan, an Agent's Guardrail configuration —
without risk to a real system. A Sandbox's Environment
(`infra-environment-lifecycle`) is always its own value, distinct from
Dev/Staging/Production, and its Risk Tier ceiling is always Low
regardless of what it's a replica of (nothing in it is real, so no
factor can elevate it) — the one place in this framework where Risk Tier
is fixed rather than computed from Determining Factors. Source: Common
industry practice.

## Scope and Provisioning

A Sandbox is provisioned the same way any other resource is (CCPROC-1,
cross-cutting/procedures.md), with two differences from a normal
Production-track resource: its Risk Tier is fixed Low (above), and its
CCP-3 Production approval requirement doesn't apply (a Sandbox is
definitionally never Production). It still carries CCP-1 (Metadata
Completeness) and CCP-2 (Cost Attribution) — a Sandbox is still a real,
billed resource, even though it isn't a real system.

## Primary Uses

- **Workflow/Process:** testing an IaC Plan (`wf-iac-plan`) or a Pipeline
  change against a Sandbox before the change touches a real Environment —
  the "something real to test against" this pillar was originally
  deferred until.
- **Harness (domain 8, being drafted):** testing an Agent's configuration
  — Tool Permission Scope, Guardrails, Escalation Path — in a Sandbox
  before granting it Production-scoped Capability Scope. See
  08-harness/01-definitions.md for how Harness's own terms reference this.

---

**Open items:**
- No formal Metadata Standards field or naming convention for a Sandbox
  is defined here — a Sandbox is provisioned using whatever domain it's
  a replica of already defines (an Infrastructure Sandbox uses
  Infrastructure's own fields, tagged with Sandbox as its Environment
  value), rather than this pillar inventing a parallel field registry.

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — one definition, one fixed-Risk-Tier rule, no new column structure
- [x] Modular — reuses every domain's own Metadata Standards/Policies rather than duplicating them
- [x] Easy to update — Primary Uses grows as new domains find a reason to reference it
- [x] Easy to maintain — resolved once, at the point it became genuinely needed, rather than speculatively built early
- [x] Easy to replace — no tooling/vendor dependency; "isolated replica" is implementation-agnostic
