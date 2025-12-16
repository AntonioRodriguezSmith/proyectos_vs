"""
Script de conexión automática entre proyectos del ecosistema PROYECTOS_VS.
- Detecta todos los proyectos y subcarpetas.
- Registra rutas y metadatos en un archivo central (proyectos_registry.json).
- Permite a cualquier módulo acceder a los demás usando este registro.
- Al crear un nuevo proyecto, actualiza automáticamente el registro.
"""
import os
import json
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
REGISTRY = BASE_DIR / "proyectos_registry.json"

# Detectar proyectos (carpetas de primer nivel, excluyendo utilitarios)
proyectos = {}
for item in BASE_DIR.iterdir():
    if item.is_dir() and not item.name.startswith(('.', 'inicio_vs', 'backups', 'venv', 'vscode')):
        proyectos[item.name] = {
            "ruta": str(item.resolve()),
            "subcarpetas": [sub.name for sub in item.iterdir() if sub.is_dir()]
        }

# Guardar registro central
with open(REGISTRY, "w", encoding="utf-8") as f:
    json.dump(proyectos, f, indent=2, ensure_ascii=False)

print(f"[OK] Registro de proyectos actualizado en {REGISTRY}")
