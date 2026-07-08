$timestamp = Get-Date -Format "yyyyMMdd-HHmmss"
$reportDir = "test-reports"
$txtReport = "$reportDir/pytest-report-$timestamp.txt"
$xmlReport = "$reportDir/junit-report-$timestamp.xml"

New-Item -ItemType Directory -Force -Path $reportDir | Out-Null

Write-Host "Running UNOBIT test report..."
Write-Host "Text report: $txtReport"
Write-Host "JUnit XML:   $xmlReport"
Write-Host ""

pytest -vv --tb=long --junitxml="$xmlReport" 2>&1 | Tee-Object -FilePath "$txtReport"

Write-Host ""
Write-Host "Done."
Write-Host "Send this file back to AI:"
Write-Host $txtReport