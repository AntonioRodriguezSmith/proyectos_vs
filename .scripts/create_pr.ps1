$ErrorActionPreference = 'Stop'
if (-not $env:GITHUB_PAT) {
  Write-Host 'ERROR: $env:GITHUB_PAT no está configurado en esta sesión.' -ForegroundColor Red
  exit 1
}
$payload = @{
  title = 'Cleaned: remove generated files'
  head  = 'cleaned'
  base  = 'main'
  body  = 'Limpieza: se eliminaron archivos generados y se actualizó .gitignore.'
}
$body = $payload | ConvertTo-Json -Depth 6
$headers = @{ Authorization = "token $($env:GITHUB_PAT)"; Accept = 'application/vnd.github+json' }
try {
  $resp = Invoke-RestMethod -Method Post -Uri 'https://api.github.com/repos/AntonioRodriguezSmith/proyectos_vs/pulls' -Headers $headers -Body $body -ErrorAction Stop
  if ($resp -and $resp.html_url) {
    Write-Host 'PR_CREATED:' $resp.html_url
  } else {
    Write-Host 'PR_CREATED but no URL returned' -ForegroundColor Yellow
  }
} catch {
  Write-Host 'PR_ERROR:' $_.Exception.Message -ForegroundColor Red
  if ($_.Exception.Response -ne $null) {
    try { $_.Exception.Response | Get-Member -Name Content -ErrorAction SilentlyContinue | Out-Null; $_.Exception.Response.GetResponseStream() | Out-Null } catch {}
  }
  exit 2
} finally {
  Remove-Item Env:GITHUB_PAT -ErrorAction SilentlyContinue
  Write-Host 'GITHUB_PAT removed from session.'
}
