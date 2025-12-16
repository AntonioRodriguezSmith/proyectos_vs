"""
Plantilla para crear y conectar automáticamente un nuevo proyecto en PROYECTOS_VS.
- Crea la carpeta, README y estructura base.
- Actualiza el registro central de proyectos.
"""
import sys
from pathlib import Path
import subprocess

BASE_DIR = Path(__file__).parent.parent
nombre = sys.argv[1] if len(sys.argv) > 1 else "nuevoProyecto"
proyecto_dir = BASE_DIR / nombre
proyecto_dir.mkdir(exist_ok=True)

# Crear README
with open(proyecto_dir / "README.md", "w", encoding="utf-8") as f:
    f.write(f"# {nombre}\n\nProyecto creado automáticamente.\n")

# Crear archivo de tareas local con la norma
with open(proyecto_dir / "tareas_pendientes.md", "w", encoding="utf-8") as f:
    f.write(f"""# Tareas de {nombre}\n\nEste archivo contiene las tareas propias del proyecto.\n\n---\n**Norma:** Las tareas propias de este proyecto deben mantenerse en este archivo local. El directorio central de tareas solo debe contener tareas globales o enlaces a este archivo. No mezclar tareas globales y locales.\n""")

# Actualizar registro central
subprocess.run(["python", str(BASE_DIR / "inicio_vs" / "conexion_proyectos.py")])
print(f"[OK] Proyecto {nombre} creado y registrado.")
