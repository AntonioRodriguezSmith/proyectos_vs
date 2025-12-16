"""
Script para revisión periódica de backups y sincronización de módulos críticos.
"""
import os
from pathlib import Path

BACKUP_DIR = Path(__file__).parent.parent / "modeloRagAlejandria" / "backups" / "jarvis_model"

if BACKUP_DIR.exists():
    archivos = list(BACKUP_DIR.glob("*.py"))
    print(f"[INFO] Archivos en backup de J.A.R.V.I.S.: {[a.name for a in archivos]}")
else:
    print("[ALERTA] No existe el directorio de backup de J.A.R.V.I.S.")
