#!/usr/bin/env python3
"""
mint-token.py

Mints a short-lived GitHub App installation access token, so an agent
can authenticate to GitHub without ever holding the App's private key
directly. This is the credential path implementation/02-github-access.md
describes: private key stays on disk, outside this repo, read only by
this script; everything downstream (git push, PR creation) uses the
token this prints, which GitHub expires on its own (~1 hour).

Reads three inputs, all from the environment - never hardcoded, never
passed as a plain command-line argument (those can leak into shell
history / process lists more easily than env vars):

  GOVERNANCE_APP_CLIENT_ID       - the GitHub App's Client ID (starts
                                    "Iv1." or similar - GitHub's current
                                    recommendation for the JWT `iss`
                                    claim, in place of the older numeric
                                    App ID; both work, Client ID is what
                                    GitHub's own docs now point to)
  GOVERNANCE_APP_INSTALLATION_ID - the numeric Installation ID (this
                                    App's installation on this one repo)
  GOVERNANCE_APP_PEM_PATH        - filesystem path to the private key
                                    (.pem) - kept outside this repo

Usage:
    python3 mint-token.py

Prints exactly one line to stdout: the installation access token.
Nothing else goes to stdout, so this is safe to capture directly, e.g.:

    $token = python3 mint-token.py

Requires: PyJWT, cryptography, requests (all already available in this
environment; on another machine: pip install pyjwt cryptography requests)
"""

import os
import sys
import time

try:
    import jwt
    import requests
except ImportError as e:
    print(f"Missing dependency: {e}. Run: pip install pyjwt cryptography requests", file=sys.stderr)
    sys.exit(1)


def die(msg: str) -> None:
    print(f"Error: {msg}", file=sys.stderr)
    sys.exit(1)


def main() -> int:
    client_id = os.environ.get("GOVERNANCE_APP_CLIENT_ID")
    installation_id = os.environ.get("GOVERNANCE_APP_INSTALLATION_ID")
    pem_path = os.environ.get("GOVERNANCE_APP_PEM_PATH")

    if not client_id:
        die("GOVERNANCE_APP_CLIENT_ID is not set")
    if not installation_id:
        die("GOVERNANCE_APP_INSTALLATION_ID is not set")
    if not pem_path:
        die("GOVERNANCE_APP_PEM_PATH is not set")
    if not os.path.isfile(pem_path):
        die(f"private key not found at {pem_path}")

    with open(pem_path, "r", encoding="utf-8") as f:
        private_key = f.read()

    # Step 1: build and sign a short-lived JWT identifying the App
    # itself (not the installation) - GitHub docs recommend backdating
    # `iat` by 60s to tolerate small clock drift, and keeping `exp`
    # well under the 10-minute hard limit.
    now = int(time.time())
    payload = {
        "iat": now - 60,
        "exp": now + (9 * 60),
        "iss": client_id,  # GitHub's current recommendation - Client ID, not App ID
    }
    app_jwt = jwt.encode(payload, private_key, algorithm="RS256")

    # Step 2: exchange the App-level JWT for an installation-scoped
    # access token - THIS is the credential that's actually scoped to
    # only this App's granted permissions on only this installation
    # (i.e. only this repo, only Contents + Pull requests).
    resp = requests.post(
        f"https://api.github.com/app/installations/{installation_id}/access_tokens",
        headers={
            "Authorization": f"Bearer {app_jwt}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        },
        timeout=30,
    )

    if resp.status_code != 201:
        die(f"token request failed ({resp.status_code}): {resp.text}")

    token = resp.json().get("token")
    if not token:
        die("response did not contain a token")

    print(token)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
