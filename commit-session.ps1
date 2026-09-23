# Run this from the repo root: .\commit-session.ps1

# 1. Clear the stale lock (safe if no other git process is actually running)
if (Test-Path ".git\index.lock") {
    Write-Host "Removing stale .git\index.lock..."
    Remove-Item ".git\index.lock" -Force
}

# 2. Show what changed since your last commit, before staging anything
Write-Host "=== Last commit ==="
git log -1 --format="%H  %ci  %s"
Write-Host " "
Write-Host "=== Files changed since then (summary) ==="
git diff --stat HEAD | Select-Object -Last 20
Write-Host " "
Write-Host "=== Full file list ==="
git status --short

# 3. Pause for a sanity check before staging/committing
Read-Host "Review the above. Press Enter to stage + commit everything, or Ctrl+C to abort"

# 4. Stage everything
git add -A

# 5. Write the commit message to a temp file, then commit from it
$commitMsg = @'
Add Business Function Departments (Marketing, Sales, Finance & Accounting, HR, Legal) with Data Owner authority

- Add five Business Function Departments to the Roles & Departments
  registry, distinct from the existing IT/technical departments: they
  hold Data Owner authority (already-defined role) over Data/Metadata's
  Business Glossary Terms and Metrics for their function, rather than
  owning a technical domain outright.
- Each carries a Standards note for AI understanding: GAAP/IFRS/SOX/
  ASC 606/XBRL (Finance & Accounting), EEOC/FLSA/ADA/FMLA/ISO 30414 (HR),
  EDRM/GDPR/CCPA (Legal), CAN-SPAM/GDPR-CCPA consent (Marketing).
- Legal becomes the retroactive Data Owner for Data/Metadata's
  previously-unowned Legal Hold term and Data Privacy & Regulatory
  subdomain.
- Resolves how a domain-specific report (Marketing/Sales/Finance report)
  traces its Calculated Fields back to an owned Metric: the Metric's
  Data Owner is now the business function, not Data Governance &
  Engineering, which remains the Data Steward (enforces quality, doesn't
  set the definition).
- Deliberately did not draw formal ontology edges from the generic
  Data Owner role to each new department (would misrepresent a shared
  role as exclusive); captured as prose + a dedicated alignment table
  instead. Logged as Q9 in the registry's Q&A log.
'@

$commitMsg | Out-File -FilePath ".git\COMMIT_MSG.tmp" -Encoding utf8

git commit -F ".git\COMMIT_MSG.tmp"

Remove-Item ".git\COMMIT_MSG.tmp"

# 6. Confirm
Write-Host " "
Write-Host "=== Done ==="
git log -1 --format="%H  %ci  %s"
git status --short
