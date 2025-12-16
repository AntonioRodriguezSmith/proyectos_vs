"""
Gestión de perfiles de entorno para modeloJarvis.
"""
import json
from pathlib import Path

CONFIG_PATH = Path(__file__).parent.parent / "config.json"

def cargar_configuracion():
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def obtener_perfil_activo():
    config = cargar_configuracion()
    return config.get("perfil_activo", "DXC")

def restricciones_perfil(perfil=None):
    config = cargar_configuracion()
    perfil = perfil or config.get("perfil_activo", "DXC")
    return config["restricciones"].get(perfil, {})
