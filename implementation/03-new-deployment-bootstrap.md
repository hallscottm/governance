# Implementation — New Deployment Bootstrap Checklist

Status: Draft — pilot, not ratified
Ratified: No
Last updated: 2026-09-23

Answers a question raised directly: when this framework gets stood up
for an entirely new client/org from scratch, what has to happen before
any real Engagement can run - so it's a defined step in the process,
not something that only happens because someone happened to ask.
**Not** the multi-tenant productization effort itself
(engagements/09-open-decisions.md #7, still explicitly deferred) - this
is narrower: the concrete access/infrastructure setup one specific new
deployment needs, captured from doing it once for real here, not a
speculative build for hypothetical future clients.

## Before any Engagement runs for real, in order

1. **Repo exists, this framework's content is in it** (fork, template,
   or copy - mechanism not decided here, deliberately out of scope
   until #7 is picked up for real).

2. **GitHub access for agents** — implementation/02-github-access.md,
   done step by step: GitHub App created (scoped to Contents +
   Pull requests only), installed on that client's repo only, branch
   protection on the default branch (explicit name pattern, require PR
   + 1 approval), private key generated and stored **outside** the
   repo with restricted file permissions, App ID/Installation ID set
   as environment variables. Nothing here is client-specific content -
   it's identical mechanics, different repo/App/key each time.

3. **An identity provider (IAM/SSO) for real Approver identity** —
   CCAR-4 requires this; not yet built anywhere in this framework
   (implementation/00-overview.md's "Honest limits"). Until this
   exists for a given deployment, CCAR-4 is satisfied in its weakest
   form: a GitHub-authenticated merge (see 02-github-access.md step 4)
   is real authentication, just not yet the AAL2/AAL3 step-up CCAR-4
   asks for at High risk tier. Flag this gap explicitly to whoever owns
   the new deployment rather than silently accepting the weaker form
   forever.

4. **A notification channel for approval/clarification requests** —
   `eng-channel` (engagements/06-participants-collaboration-and-
   channels.md) names the concept; nothing wires it to a real Slack
   app, email sender, or ticketing system yet. Without this, a human
   has to remember to go check for open PRs/Intake gaps rather than
   being told. Not built - first real need should build it
   (Build-on-Demand), not this checklist speculatively.

5. **Whatever domain-specific systems the first real Engagement
   actually touches** — e.g. dq-metrics-dashboard needed a real data-
   quality-checks source; that's specific to that Engagement, not
   something this checklist can anticipate generically.

## What this checklist deliberately does NOT cover

- Multi-tenant mechanics (one framework instance serving several
  clients) - #7's territory, still deferred.
- Anything client-specific in the governance content itself (domains,
  policies, org chart) - that's the actual framework build, covered by
  everything outside `implementation/`.
- A "run this script and it's done" automation of steps 2-4 above -
  each involves real account/security decisions (which permissions,
  which identity provider) that shouldn't be templated blindly. This
  is a checklist a human works through with an agent, per step 2's
  worked example in this very conversation, not a one-shot script.

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — one ordered checklist, each item pointing to its own real doc where one exists
- [x] Modular — each step stands alone; #3 and #4 being unbuilt doesn't block #1/#2/#5
- [x] Easy to update — a new required step is an additive list item
- [x] Easy to maintain — items 3/4's "not built yet" status is stated plainly, not hidden
- [x] Easy to replace — plain markdown checklist, no tooling dependency
