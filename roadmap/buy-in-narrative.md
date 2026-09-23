# Buy-In Narrative

Status: Draft — pending review
Ratified: No
Last updated: 2026-09-23

Leadership-facing version of the roadmap (roadmap/roadmap.md): same
phase structure, reframed around risk reduction and pace-of-adoption
rather than definitional detail. Authored, not generated — update this
by hand as the roadmap's phases change; do not attempt to mechanically
derive it from roadmap.md, since the reframing is the point.

---

## The one-sentence version

Every system this organization runs — infrastructure, networks,
applications, data, reporting, delivery pipelines, and now AI agents —
is now governed by the same, explicit set of rules for who can do what,
what has to be documented, and what gets extra scrutiny before it goes
live. That coverage did not exist as a single, consistent system before
this framework; pieces of it existed in different teams' heads, wikis,
and tribal knowledge, unevenly enforced and hard to audit as a whole.

## Why this matters now, not later

Three of the eight domains this framework covers — Data Platform,
Workflow/Process, and Harness (AI agents) — did not have a coherent,
written governance model before this effort. Harness in particular
covers exactly the kind of system (AI agents acting with real
permissions) that is hardest to govern after the fact, once agents are
already running in production with whatever ad hoc scope someone gave
them. Building the rules before wide AI agent adoption, rather than
retrofitting them afterward, is the difference between a designed
control and a cleanup project.

## What "done" means at this stage

**Every domain is fully specified — not yet signed off.** All 8 domains
(10 to 67 owned terms each, 351 terms total) and all 3 cross-cutting
concerns that cut across every domain (Governance & Security, Roles &
Departments, Sandbox testing) have a complete, written definition: what
things are called, who owns them, what must be documented, who can
approve what, what gets flagged as higher risk, and what class of tool
implements each piece — without naming a specific vendor, so the
framework survives a tool change.

What's still ahead is **review, not authorship** — each domain needs a
human owner (already assigned per domain in roadmap.md's Phase 0 table)
to read through and formally ratify it, the same way a policy document
gets sign-off before it's treated as binding rather than a draft.

## Risk reduction, concretely

A few examples of what this framework catches that ad hoc practice
typically doesn't:

- **No AI agent can be its own approver.** This is written as a hard
  rule (cross-cutting CCAR-1, restated at instance level in Harness's
  HAR-2) with zero exception — an agent can propose or request an
  action, but a human always signs off before anything production-scoped
  happens. This is exactly the kind of rule that's easy to skip when an
  agent is stood up quickly and easy to forget to add back later.
- **Every override is logged and reviewed after the fact**, whether it's
  a human bypassing a deployment gate in an emergency or an AI agent's
  guardrail being overridden — nothing gets silently skipped without an
  audit trail and a follow-up review within a defined window.
- **New AI agent capabilities are sandbox-tested before they touch
  production** — a rule this framework makes structural (HPOL-1), not
  optional guidance.
- **Risk scales the response.** A low-stakes change gets a lightweight
  path; a production change touching sensitive data or an agent with
  broad permissions gets more eyes on it. Nothing is one-size-fits-all,
  and nothing above a certain risk level moves without the right sign-off.

## Pace of adoption

This was built incrementally, one domain at a time, in a fixed order
(Infrastructure and Networking first, since everything else depends on
them; Harness last, since it depends on nearly everything else already
being defined). That same order is the recommended review order —
teams don't need to review all 8 domains and 3 cross-cutting pillars at
once. A team can start using its own domain's rules as soon as that
domain is reviewed and signed off, without waiting for every other
domain to finish review.

Nothing here requires a big-bang cutover. Every rule is written to be
enforced by ordinary tooling an organization already has or can
reasonably add (a CI/CD platform, an access-control system, a
ticketing/approval workflow) — no bespoke platform has to be built
first for any of this to start taking effect.

## What we're asking for

1. **A named reviewer for each domain** (candidates already suggested in
   roadmap.md's Phase 0 table, by department) to read their domain and
   either ratify it or flag specific changes.
2. **Agreement on review order** — we recommend the same build order
   (Infrastructure through Harness), so later domains' cross-references
   land on stable ground, but a team under time pressure for a
   particular domain (e.g., Harness, if AI agent rollout is imminent)
   can be prioritized out of order.
3. **No new tooling spend required to start** — ratification is a
   documentation/sign-off exercise; the tooling categories named
   throughout (column 10 of every domain) are capability descriptions,
   not purchase requests.

---

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — one narrative, six short sections, no jargon requiring the source files to parse
- [x] Modular — stands alone from roadmap.md; references it rather than duplicating its tables
- [x] Easy to update — hand-edited as phases change, explicitly not generated
- [x] Easy to maintain — reframes existing content (roadmap.md's phases, HAR-2, HPOL-1, CCAR-1) rather than introducing new claims to keep in sync
- [x] Easy to replace — no tooling/vendor dependency; the ask section is generic to any organization adopting this framework
