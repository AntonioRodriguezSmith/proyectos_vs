
import re
from collections import defaultdict

INPUT_FILE = "c:/Users/rodri/proyectos_vs/modeloRagAlejandria/knowledge_base/tareas/tareas_central.md"
OUTPUT_FILE = "c:/Users/rodri/proyectos_vs/modeloRagAlejandria/knowledge_base/tareas/tareas_central_formateada_OK.md"

def agrupar_y_formatear(input_path, output_path):
    with open(input_path, encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]

    tareas_por_fecha = defaultdict(list)
    fecha_actual = None
    tarea_set = set()

    # Expresión para fechas tipo [2025-12-17]
    re_fecha = re.compile(r"\[(\d{4}-\d{2}-\d{2})\]")

    for line in lines:
        m = re_fecha.match(line)
        if m:
            fecha_actual = m.group(1)
            continue
        if fecha_actual:
            # Elimina duplicados exactos
            if line not in tarea_set:
                tareas_por_fecha[fecha_actual].append(line)
                tarea_set.add(line)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("# Tareas Centralizadas\n\n")
        for fecha in sorted(tareas_por_fecha.keys(), reverse=True):
            f.write(f"## {fecha}\n\n")
            for idx, tarea in enumerate(tareas_por_fecha[fecha], 1):
                f.write(f"{idx}. {tarea}\n")
            f.write("\n")

if __name__ == "__main__":
    agrupar_y_formatear(INPUT_FILE, OUTPUT_FILE)
    print(f"Archivo agrupado y formateado guardado en: {OUTPUT_FILE}")
