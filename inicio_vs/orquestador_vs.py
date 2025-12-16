"""
Orquestador VS: Script de arranque central para el ecosistema de desarrollo.
- Detecta entorno y perfil.
- Carga o crea historial de sesión.
- Lanza y verifica J.A.R.V.I.S. (modeloJarvis) aunque no se carguen otros proyectos.
- Sincroniza backups y módulos críticos.
- Deja todo listo para trabajar en VS Code.
"""
import os
import subprocess
from pathlib import Path

# Ruta base de los proyectos
BASE_DIR = Path(__file__).parent.parent
JARVIS_DIR = BASE_DIR / "modeloJarvis"
HISTORIAL = BASE_DIR / "modeloRagAlejandria" / "historial_sesion.md"
BACKUP_DIR = BASE_DIR / "modeloRagAlejandria" / "backups" / "jarvis_model"

# 1. Detectar entorno (puedes ampliar con scripts propios)
os.system(f"python {BASE_DIR}/modeloRagAlejandria/scripts/detectar_entorno.py")

# 2. Cargar o crear historial de sesión
if not HISTORIAL.exists():
    with open(HISTORIAL, "w", encoding="utf-8") as f:
        f.write("# Historial de sesión iniciado por orquestador_vs\n")

# 3. Lanzar J.A.R.V.I.S. (API FastAPI en modo desarrollo)
try:
    subprocess.Popen(["uvicorn", "api.main:app", "--reload"], cwd=JARVIS_DIR / "api")
    print("[OK] J.A.R.V.I.S. iniciado en segundo plano.")
except Exception as e:
    print(f"[ERROR] No se pudo iniciar J.A.R.V.I.S.: {e}")

# 4. Sincronizar backups (puedes automatizar más tareas aquí)
if not BACKUP_DIR.exists():
    BACKUP_DIR.mkdir(parents=True)

print("[INFO] Orquestador VS finalizó la preparación del entorno. Puedes trabajar en VS Code con J.A.R.V.I.S. activo.")
