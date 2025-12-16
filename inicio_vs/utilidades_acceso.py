"""
Utilidades para acceso y navegación entre proyectos usando el registro central.
Permite a cualquier script o módulo localizar y acceder a cualquier proyecto o subcarpeta del ecosistema.
"""
import json
from pathlib import Path

REGISTRY = Path(__file__).parent.parent / "proyectos_registry.json"

def cargar_registro():
    with open(REGISTRY, "r", encoding="utf-8") as f:
        return json.load(f)

def obtener_ruta_proyecto(nombre):
    registro = cargar_registro()
    return registro.get(nombre, {}).get("ruta")

def listar_proyectos():
    registro = cargar_registro()
    return list(registro.keys())

def listar_subcarpetas(nombre):
    registro = cargar_registro()
    return registro.get(nombre, {}).get("subcarpetas", [])

# Ejemplo de uso
if __name__ == "__main__":
    print("Proyectos disponibles:", listar_proyectos())
    print("Ruta de modeloJarvis:", obtener_ruta_proyecto("modeloJarvis"))
