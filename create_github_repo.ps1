param(
  [string]$RepoName = "proyectos_vs",
  [string]$Visibility = "public"
)

# Script para crear un repo en GitHub con gh CLI y enlazar el remoto
# Requiere gh instalado y autenticado (gh auth login)

Set-Location $PSScriptRoot

Write-Host "Crear repo en GitHub: $RepoName (visibilidad: $Visibility)" -ForegroundColor Cyan

# Comando gh para crear el repo y empujar el contenido actual
$cmd = "gh repo create $RepoName --$Visibility --source=. --remote=origin --push"
Write-Host "Ejecutando: $cmd" -ForegroundColor Yellow

Invoke-Expression $cmd

if ($LASTEXITCODE -eq 0) {
  Write-Host "Repositorio creado y push completado." -ForegroundColor Green
} else {
  Write-Host "Hubo un error creando el repo. Asegúrate de que gh está instalado y autenticado (gh auth login)." -ForegroundColor Red
  exit 1
}
