"""
Script general para detectar información básica del entorno y sesión.
Guarda los datos en un archivo info_entorno.json para uso de J.A.R.V.I.S. y otros módulos.
"""
import platform
import getpass
import socket
import os
import json
from datetime import datetime

info = {
    "usuario": getpass.getuser(),
    "sistema": platform.system(),
    "version": platform.version(),
    "maquina": platform.node(),
    "ip_local": socket.gethostbyname(socket.gethostname()),
    "directorio_actual": os.getcwd(),
    "fecha_hora": datetime.now().isoformat()
}

with open("info_entorno.json", "w", encoding="utf-8") as f:
    json.dump(info, f, indent=2, ensure_ascii=False)
