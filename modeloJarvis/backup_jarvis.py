# Automatización de backup de JarvisModel

import shutil
from pathlib import Path
import datetime

SRC = Path(__file__).parent.parent / "modeloJarvis" / "src"
BACKUP = Path(__file__).parent.parent / "modeloRagAlejandria" / "backups" / "jarvis_model"


def backup_jarvis():
    BACKUP.mkdir(parents=True, exist_ok=True)
    fecha = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    for archivo in SRC.glob("*.py"):
        destino = BACKUP / archivo.name
        shutil.copy2(archivo, destino)
    print(f"Backup de JarvisModel realizado en {BACKUP} ({fecha})")

if __name__ == "__main__":
    backup_jarvis()
