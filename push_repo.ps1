param(
  [string]$RepoUrl
)

# Ejecutar desde la raíz del repo: C:\Users\arodriguezsm\proyectos_vs
Set-Location $PSScriptRoot

if (-not $RepoUrl) {
  $RepoUrl = Read-Host "Introduce la URL HTTPS del repo remoto (ej: https://github.com/usuario/repo.git)"
}

Write-Host "Usando remoto:" $RepoUrl -ForegroundColor Cyan

# Añadir o actualizar origin
$exists = git remote | Select-String -Pattern "^origin$" -Quiet
if ($exists) {
  git remote set-url origin $RepoUrl
  Write-Host "Remote 'origin' actualizado." -ForegroundColor Green
} else {
  git remote add origin $RepoUrl
  Write-Host "Remote 'origin' añadido." -ForegroundColor Green
}

# Verificar remote
git remote -v

# Hacer push
try {
  git push -u origin main
  Write-Host "Push completado." -ForegroundColor Green
} catch {
  Write-Host "Error al hacer push: $_" -ForegroundColor Red
  Write-Host "Si hay problemas de autenticación, crea un PAT en GitHub y úsalo como contraseña o ejecuta 'gh auth login' para autenticar." -ForegroundColor Yellow
  exit 1
}
