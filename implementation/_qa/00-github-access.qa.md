# Q&A Log — 02-github-access
# Append-only. Do not edit past entries; add new dated entries instead.

## 2026-09-23 — GitHub App set up live, walked through step by step in chat

**Bucket:** [Judgment]/User-confirmed — direct follow-up to "how can our
system manage github in a safe secure manner." User created a real
GitHub App (governance-factory-agent), installed on hallscottm/governance
only, Contents + Pull requests read/write, nothing else. Branch
protection added to main with an explicit name pattern (not "include
default branch" - deliberately chosen for auditability, matching this
framework's own explicit-over-implicit discipline, discussed directly
in chat before being applied). Private key downloaded, moved outside
the repo to a locked-down folder (icacls, owning account only),
original filename kept (embeds creation date, useful for future key
rotation) rather than renamed to something simpler.

**Answer:** implementation/02-github-access.md documents the setup and
the still-needed step (App ID/Installation ID as env vars).
implementation/github-auth/mint-token.py exchanges the private key for
a short-lived installation token via GitHub's API, without any script
or agent holding the key itself. .gitignore updated with a defense-in-
depth backstop (*.pem, *.p12, *.pfx, .env, **/secrets/**) in case a
credential ever lands in the repo folder by mistake - the real
protection is that the key lives outside this repo entirely.

**Explicitly not yet done:** actually using this to write a real
branch/PR - the workflow is documented, not yet exercised. Whether to
switch this session's own working pattern (device bridge writes
directly -> branch+PR instead) is left as the user's call, not assumed.

**Applied to:** .gitignore, implementation/02-github-access.md,
implementation/github-auth/mint-token.py.

**Status:** Pending explicit review; pending App ID/Installation ID to
actually test end to end.

## 2026-09-23 — Bootstrap checklist added

**Bucket:** [Judgment]/User-confirmed — "i need something part of this
process to initiate this conversation in regards to setting up github
whenever we set this up for entirely new client from scratch."

**Answer:** implementation/03-new-deployment-bootstrap.md - an ordered
checklist of what has to happen before any Engagement runs for real in
a new deployment, so the GitHub App conversation (and the still-unbuilt
IAM/SSO and notification-channel pieces) is a defined step, not
something that only happens because someone happened to ask this
session. Deliberately scoped narrower than #7 (multi-tenant
productization, still deferred) - this captures the concrete
access/infrastructure setup from doing it once for real, not a
speculative multi-tenant build.

**Applied to:** implementation/03-new-deployment-bootstrap.md,
implementation/_status.yaml.

**Status:** Pending explicit review.

## 2026-09-23 — Client ID, not App ID, per GitHub's current recommendation

**Bucket:** [External]/Provenance — user flagged a GitHub UI notice
mid-setup: "Using your App ID to get installation tokens? You can now
use your Client ID instead." Verified against GitHub's own docs before
changing anything (not taken on faith): confirmed Client ID is
GitHub's current recommendation for the JWT `iss` claim; App ID is not
deprecated, just no longer the primary recommendation.

**Answer:** implementation/github-auth/mint-token.py and
02-github-access.md updated to use GOVERNANCE_APP_CLIENT_ID in place of
GOVERNANCE_APP_ID before any real setup used the older path - caught
before, not after, the user set env vars.

**Status:** Applied.
