"""
Script de gestión de nomenclaturas de proyectos ejecutivos.
Permite añadir, modificar, eliminar y sincronizar nomenclaturas en los archivos .md y .json.
En el futuro, también actualizará el ADR central automáticamente.
"""
import json
from datetime import datetime
import os

NOMEN_JSON = os.path.join("modeloRagAtenas", "datos", "nomenclaturas_Atenas.json")
NOMEN_MD = os.path.join("modeloRagAtenas", "datos", "nomenclaturas_Atenas.md")
ADR_README = os.path.join("modeloRagAtenas", "adr.md")

# Funciones principales (esqueleto)
def cargar_nomenclaturas():
    with open(NOMEN_JSON, encoding="utf-8") as f:
        return json.load(f)

def guardar_nomenclaturas(data):
    with open(NOMEN_JSON, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def actualizar_md(data):
    tabla = "| Nomenclatura      | Nombre del Proyecto      | Descripción breve                  | Fecha de alta | Estado  |\n"
    tabla += "|-------------------|-------------------------|------------------------------------|--------------|---------|\n"
    for item in data:
        tabla += f"| {item['nomenclatura']} | {item['nombre']} | {item['descripcion']} | {item['fecha_alta']} | {item['estado']} |\n"
    with open(NOMEN_MD, "w", encoding="utf-8") as f:
        f.write("# Registro de Nomenclaturas de Proyectos\n\n" + tabla)

# Ejemplo de uso: añadir una nomenclatura
def agregar_nomenclatura(nomenclatura, nombre, descripcion, estado="Activo"):
    data = cargar_nomenclaturas()
    data.append({
        "nomenclatura": nomenclatura,
        "nombre": nombre,
        "descripcion": descripcion,
        "fecha_alta": datetime.now().strftime("%Y-%m-%d"),
        "estado": estado
    })
    guardar_nomenclaturas(data)
    actualizar_md(data)
    # En el futuro: actualizar_adr_readme(data)

if __name__ == "__main__":
    # Ejemplo: agregar_nomenclatura("002_informe_xyz", "Informe XYZ", "Descripción del informe XYZ")
    pass
