# Run this from the repo root: .\commit-session.ps1

# 1. Clear the stale lock (safe if no other git process is actually running)
if (Test-Path ".git\index.lock") {
    Write-Host "Removing stale .git\index.lock..."
    Remove-Item -Force ".git\index.lock"
}

# 2. Show context before committing
Write-Host "`n--- Last commit ---"
git log -1
Write-Host "`n--- Diff stat (last 20 lines) ---"
git diff --stat HEAD | Select-Object -Last 20
Write-Host "`n--- Status ---"
git status --short

Read-Host "`nReview the above. Press Enter to stage and commit, or Ctrl+C to abort"

# 3. Stage everything
git add -A

# 4. Write commit message to a temp file (avoids PowerShell quoting issues)
@'
Resolve DevOps/Workflow-Process ownership; fold Interface/Human into Roles & Departments

DevOps / Release Engineering becomes a cross-cutting standards/platform
owner for Workflow/Process (domain 7), not its sole owner -- Platform
Engineering, Application Engineering, Data Governance & Engineering,
Business Intelligence & Analytics, and AI/ML Platform each instantiate
their own pipeline/repo instance against DevOps's shared standard,
mirroring the earlier Data Platform ownership fix. See 00-qa.md Q10.

Interface/Human (domain 9) folded into the Roles & Departments
cross-cutting pillar rather than kept as a domain -- it never had
technical artifacts of its own. Replaced by a new Training Requirement
mechanism (ccorg-training-requirement), attached directly to the Role or
Department it gates and referenced from each domain's Access Rules
column. IT Training & Change Management becomes the cross-cutting owner
of this mechanism, the same shape Security & Compliance and DevOps now
have. 09-interface-human/ (stub files only) removed; domain-axis
definition, EA alignment notes, term-linking prefixes, and setup.sh
updated to match. See 00-qa.md Q11.

Also fixed two stale forward-references (Infrastructure Access Rules,
System Architecture Metadata Standards) that were waiting on the
now-folded Interface/Human domain.
'@ | Out-File -Encoding utf8 ".git\COMMIT_MSG.tmp"

git commit -F ".git\COMMIT_MSG.tmp"
Remove-Item ".git\COMMIT_MSG.tmp"

# 5. Confirm
Write-Host "`n--- New commit ---"
git log -1
Write-Host "`n--- Status after commit ---"
git status --short

Write-Host "`nDone. Run 'git push' separately to push to GitHub."
