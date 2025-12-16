"""
Script para automatizar la generación y actualización de documentación en PROYECTOS_VS.
- Actualiza índices y listas de archivos en cada proyecto.
- Genera un resumen de estructura y dependencias.
- Puede ampliarse para actualizar diagramas o docs específicos.
"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
proyectos = [p for p in BASE_DIR.iterdir() if p.is_dir() and not p.name.startswith(('.', 'venv', 'vscode'))]

for proyecto in proyectos:
    readme = proyecto / "README.md"
    index_lines = [f"# Índice de archivos en {proyecto.name}\n\n"]
    for root, dirs, files in os.walk(proyecto):
        for file in files:
            if file.endswith(('.py', '.md', '.json')):
                rel_path = Path(root).relative_to(proyecto)
                index_lines.append(f"- {rel_path / file}\n")
    index_path = proyecto / "INDEX_AUTO.md"
    with open(index_path, "w", encoding="utf-8") as f:
        f.writelines(index_lines)
    print(f"[OK] Índice automático actualizado en {index_path}")
