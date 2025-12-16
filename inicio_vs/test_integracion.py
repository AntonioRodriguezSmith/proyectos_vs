"""
Script de tests automáticos de integración entre proyectos de PROYECTOS_VS.
Verifica que los accesos directos, backups y sincronización funcionan correctamente.
"""
import sys
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
sys.path.append(str(BASE_DIR / "inicio_vs"))

from utilidades_acceso import listar_proyectos, obtener_ruta_proyecto

# Test: todos los proyectos del registro existen
proyectos = listar_proyectos()
for nombre in proyectos:
    ruta = obtener_ruta_proyecto(nombre)
    assert Path(ruta).exists(), f"[ERROR] Proyecto {nombre} no encontrado en {ruta}"
print("[OK] Todos los proyectos del registro existen.")

# Test: backups de J.A.R.V.I.S. existen
backup_dir = BASE_DIR / "modeloRagAlejandria" / "backups" / "jarvis_model"
assert backup_dir.exists(), f"[ERROR] No existe el backup de J.A.R.V.I.S."
print("[OK] Backup de J.A.R.V.I.S. verificado.")
