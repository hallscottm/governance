# Run this from the repo root: .\commit-session.ps1

if (Test-Path ".git\index.lock") {
    Write-Host "Removing stale .git\index.lock..."
    Remove-Item -Force ".git\index.lock"
}

Write-Host "`n--- Last commit ---"
git --no-pager log -1
Write-Host "`n--- Diff stat (last 20 lines) ---"
git diff --stat HEAD | Select-Object -Last 20
Write-Host "`n--- Status ---"
git status --short

Read-Host "`nReview the above. Press Enter to stage and commit, or Ctrl+C to abort"

git add -A

@'
Build out Workflow/Process domain (all 11 columns) and resolve forward references across five other domains

Workflow/Process (domain 7) built fresh across six subdomains: Source
Control, CI/CD Pipelines, Data Pipeline Orchestration, Infrastructure as
Code, Operational SOPs, and Release Management -- 29 owned terms, 26
internal relationships plus 7 cross-domain edges.

Conventions includes four Mermaid diagrams embedded directly in the
markdown (GitHub-native rendering, no external tool or image file): CI/CD
Pipeline Flow, Environment Promotion Flow, an illustrative Data Pipeline
Orchestration DAG, and an Incident Lifecycle state diagram, each tied to
specific Definitions/Policies anchors.

Policies: WFPOL-1 (branch protection) is the mechanism that makes every
other domain's hard-block test/scan policies actually enforceable at
merge time. WFPOL-2 (deployment gate before Production) is the general
mechanism System Architecture's SAPOL-4, Data Platform's DPPOL-1, and
Business Intelligence / Reporting's BIPOL-1 all assumed existed --
closes that loop for all three at once. WFPOL-3 governs IaC apply.
WFPOL-4 scales post-incident review by severity. WFPOL-5 is this
framework's first post-hoc (rather than pre-) approval gate, for
emergency changes.

Access Rules deliberately introduce no new role -- all three route
authority through roles other domains already own.

Risk Tiers introduces two process-based factors (Change Request Type,
break-glass/override usage) -- the first factors in this framework scored
on how a change was made rather than a property of the resource itself.

Tooling resolves forward references left open across five other domains:
System Architecture's Repository Reference field and SAPOL-4/SAPROC-4's
pipeline mechanism, Data Platform's Orchestration Reference field and
DPPROC-5's detection mechanism, and Infrastructure's/Networking's IaC
Platform categories. All affected files (System Architecture x5,
Data Platform x2, Infrastructure x2, Networking x1, Data/Metadata x1,
plus reverse-pointer updates in Infrastructure/System
Architecture/Data Platform/Cross-Cutting Roles & Departments' ontologies)
updated in this same pass to record the resolutions.

All 11 columns of Workflow/Process (domain 7) are now drafted.
'@ | Out-File -Encoding utf8 ".git\COMMIT_MSG.tmp"

git commit -F ".git\COMMIT_MSG.tmp"
Remove-Item ".git\COMMIT_MSG.tmp"

Write-Host "`n--- New commit ---"
git --no-pager log -1
Write-Host "`n--- Status after commit ---"
git status --short

Write-Host "`nDone. Run 'git push' separately to push to GitHub."
