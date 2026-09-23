# Implementation — GitHub Access for Agents

Status: Draft — pilot, not ratified
Ratified: No
Last updated: 2026-09-23

How an agent authenticates to GitHub and makes a real change to this
repo, safely. Companion to implementation/01-running-an-engagement.md -
that runbook covers the governance steps (Vetting -> Planning ->
Approval -> Task); this file covers the one new mechanical step those
Tasks now route through instead of the device bridge writing files
directly: a real branch, a real PR, a real human merge.

## What's set up (as of 2026-09-23)

- A GitHub App (`governance-factory-agent`), installed on exactly this
  repo (`hallscottm/governance`), with `Contents: Read & write`,
  `Pull requests: Read & write`, `Metadata: Read-only` and nothing
  else - the GitHub-enforced version of Tool Permission Scope.
- Branch protection on `main` (explicit name pattern, not "include
  default branch" - see the reasoning in this session's own
  discussion, worth keeping here for provenance): requires a pull
  request before merging, 1 approval. Direct pushes to `main` are not
  possible for anyone, agent or human, regardless of credential.
- The App's private key, stored outside this repo entirely
  (`C:\Users\halls\secrets\github-apps\`), permissions locked to the
  owning Windows account only (`icacls /inheritance:r` +
  `/grant:r <user>:R`).
- implementation/github-auth/mint-token.py - exchanges that private
  key for a short-lived (~1 hour) installation access token, without
  any script or agent ever holding the key itself.

## What's still needed before this is usable end to end

- The App's **Client ID** and **Installation ID** (both visible on the
  App's GitHub settings pages - neither is secret, both are just
  identifiers, safe to note here or hand to me directly). Needed as
  environment variables, not hardcoded anywhere. Note: GitHub's docs
  now recommend the Client ID (starts `Iv1.` or similar) over the
  older numeric App ID for this purpose - both technically work, but
  this was built fresh against the current recommendation, not the
  older path:
  ```
  GOVERNANCE_APP_CLIENT_ID=<Client ID>
  GOVERNANCE_APP_INSTALLATION_ID=<Installation ID>
  GOVERNANCE_APP_PEM_PATH=C:\Users\halls\secrets\github-apps\governance-factory-agent.2026-09-23.private-key.pem
  ```
  Set these in your own PowerShell profile or Windows environment
  variables (`setx GOVERNANCE_APP_ID "..."`, etc.) - not in any file
  that lives in this repo.
- A quick verification run once those are set:
  ```powershell
  python3 implementation\github-auth\mint-token.py
  ```
  Should print a single token string (starts with `ghs_`). If it
  errors, the message says which of the three env vars or the key
  file itself is the problem.

## The actual workflow, once a token can be minted

This replaces "the device bridge writes a file directly into the
working tree" for anything that should go through PR review (which,
per CCAR-1/CCAR-2, is any Factory Run's registration and any real Task
output - the pilot runs so far wrote directly because no GitHub App
existed yet; that was a known, stated gap, not the intended end state).

1. Mint a token (above).
2. Point the remote at a token-authenticated URL for this operation
   only - not a permanent change to `origin`:
   ```powershell
   git -C <repo path> -c http.extraHeader="Authorization: Bearer $token" fetch origin
   ```
   or, simpler for a one-off push, a temporary remote:
   ```powershell
   git -C <repo path> checkout -b factory/csv-summary-skill
   git -C <repo path> add <files>
   git -C <repo path> commit -m "<message>"
   git -C <repo path> push "https://x-access-token:$token@github.com/hallscottm/governance.git" factory/csv-summary-skill
   ```
3. Open the PR (via `gh pr create`, if the GitHub CLI is available and
   authenticated with the same token, or via GitHub's API
   `POST /repos/hallscottm/governance/pulls`).
4. **You** review and merge in GitHub's UI, signed in as yourself. That
   merge event - your real GitHub identity, a timestamp GitHub itself
   records - is what satisfies CCAR-4 for real, not a line in a YAML
   file.
5. Delete the branch after merge (GitHub can do this automatically on
   merge - a checkbox in repo settings, worth turning on).

## What this changes about how I work with this repo

Up to now, every change this session made went straight to your
working tree via the device bridge, and you ran `commit-session.ps1` +
`git push` yourself afterward - a workaround for a sandbox-specific git
lock issue, not a governance decision. Once the pieces above are
wired up and tested, the more correct pattern for anything that should
carry real PR review is: I write to a branch and open a PR instead of
writing directly to your working tree's tracked files, and you merge.
**Not switching to that automatically** - this file documents the
mechanism; whether/when to actually start using it (for everything, or
just for Factory Run registrations, or not yet at all while this is
still one person iterating quickly) is your call, not mine to assume.

## GitHub Actions setup (Tier 2 - implementation/04-agent-isolation-and-harnessing.md)

Built 2026-09-23, not yet exercised end to end. To actually run a
Factory Run through this pipeline instead of by hand:

1. **Add the workflow file yourself.** `.github/workflows/*` is
   blocked from remote-tool writes on purpose (it executes with repo
   secrets) - add `.github/workflows/factory-run.yml` directly, with
   the content handed to you separately from this doc.
2. **Add four repo secrets** (Settings -> Secrets and variables ->
   Actions -> New repository secret):
   - `GOVERNANCE_APP_CLIENT_ID` - same value as your local `$env:GOVERNANCE_APP_CLIENT_ID`
   - `GOVERNANCE_APP_INSTALLATION_ID` - same value as your local one
   - `GOVERNANCE_APP_PRIVATE_KEY` - the **full contents** of the `.pem`
     file (not a path - GitHub Actions secrets hold values, not files;
     the workflow writes this to a runner-local temp file itself)
   - `ANTHROPIC_API_KEY` - a real Anthropic API key, scoped to whatever
     billing/usage limits you're comfortable with a CI runner having
3. **Dispatch it manually** (Actions tab -> Factory Run -> Run
   workflow), naming the Task Document, the agent file
   (`implementation/agents/factory-agent.md`), and the write-scope
   prefix (`implementation/factory-runs/<slug>/sandbox/`).
4. It opens a PR, same review discipline as everything else here -
   run the candidate's Eval Suite and get real Sandbox/Approval sign-off
   before merging. **The PR existing is not approval of anything.**

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — one script, one env-var contract, one workflow
- [x] Modular — this file is independent of 01-running-an-engagement.md; either can change without the other
- [x] Easy to update — App ID/Installation ID are config, not code
- [x] Easy to maintain — token minting is one script, not spread across every Task
- [x] Easy to replace — standard GitHub App + installation-token pattern, no custom infrastructure
