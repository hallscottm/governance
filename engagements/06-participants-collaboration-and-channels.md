# Engagements — Participants, Collaboration & Channels

Status: Draft — pending review
Ratified: No
Last updated: 2026-09-23

Covers `eng-participant`, `eng-collaboration-log`, and `eng-channel`
(01-definitions.md).

## Participants

Every human and Agent working an Engagement is named on its
Participants list (the `participants:` field in 03/04's templates) with
a Role and a RACI tag:

- **Responsible** — does the work
- **Accountable** — answers for the outcome; exactly one per Engagement; human-only at High risk tier — see 07-planning-and-advisory-agents.md's Accountability Boundary and CCP-4 (cross-cutting/policies.md)
- **Consulted** — input sought before/during
- **Informed** — kept updated

Humans and Agents sit in the same list, addressed the same way — no
separate "system" field. Multiple Consulted/Informed entries are
normal; exactly one Accountable is not optional.

## Collaboration Log

Rather than a new mechanism, an Engagement Document's discussion reuses
this framework's own review-document pattern: threaded comments,
anchored to a specific passage, open to any Participant (human or
Agent) to post or reply. Gives:

- A discussion tied to the actual point in the document it's about, not a side channel that loses context
- The same append-only, who-said-what-when discipline the Approval log already has, generalized from sign-offs to ongoing discussion
- No new tooling to build

## Channels

A Channel — chat, email, a ticketing system, Slack, voice/transcription
— is not a new concept to govern. It is a registered Tool under an
Agent's Tool Permission Scope (`harness-tool-permission-scope`,
08-harness/01-definitions.md), exactly like any other Tool. This keeps
Channels scalable by construction: adding a new Channel means
registering a new Tool through Harness's existing Tooling column
(08-harness/10-tooling.md) and scoping it in the relevant Agent's Tool
Permission Scope — no change to this file, the Engagement Document
schema, or any Agent's Capability Scope is required.

What's fixed: every Channel an Agent or human uses on an Engagement is a
named, permissioned Tool — never an undocumented side-channel. What's
dynamic: which specific Channels are in use, and for which Engagements
— that list grows in Harness's Tooling registry, not here.

**Quality bar check:**
- [x] Simple — Participants is one list, Collaboration Log reuses existing tooling, Channels reuse an existing concept
- [x] Modular — a new Channel never touches this file
- [x] Easy to update — RACI and Participants entries are additive per Engagement, no schema versioning needed
- [x] Easy to maintain — Channels inherit Harness's Tool Permission Scope governance rather than a second permission model
- [x] Easy to replace — plain YAML list + the existing comment substrate
