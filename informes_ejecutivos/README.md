
# Proyecto INFORMES EJECUTIVOS

Este proyecto centraliza la generación, gestión y automatización de informes ejecutivos para todos los proyectos del workspace.

## Estructura general
- `/informes/NNN_informe_xxx/`: Cada informe ejecutivo tiene su carpeta propia, identificada por nomenclatura única (ejemplo: `001_informe_dxc`).
- `/RAG/modeloRagAtenas/`: Carpeta para el modelo RAG central y subproyectos relacionados con Alejandría.
- `/datos/imagenes/NNN_imagenes/`, `/datos/fuentes_externas/NNN_fuentes_externas/`, `/datos/backups/NNN_backups/`: Recursos globales indexados por nomenclatura.
- `/adr/`: Architecture Decision Records globales y del proyecto.

## Lógica de nomenclaturas
Cada informe/proyecto se identifica mediante una nomenclatura única: `NNN_informe_nombre`. Esta nomenclatura es el índice principal para automatizar la creación de carpetas, archivos y recursos asociados.

### Ejemplo de nomenclatura
- `001_informe_dxc`: Primer informe ejecutivo sobre IA en DXC.
- `002_informe_xyz`: Segundo informe, etc.

## Automatización
El script central `Atenas.py` gestiona:
- Registro y control de nomenclaturas.
- Creación automática de la estructura de carpetas y archivos para cada nuevo informe.
- Sincronización de recursos y actualización de índices.

## Responsabilidad de los README
- Este README (raíz): Documentación global, lógica de organización y automatización.
- `/RAG/modeloRagAtenas/README.md`: Solo para subproyectos RAG/Alejandría.
- `/informes/NNN_informe_xxx/README.md`: Documentación y ADR específicos de cada informe.

## Buenas prácticas
- Mantén la nomenclatura y los índices actualizados.
- No dupliques información entre README.
- Centraliza la lógica y automatización en Atenas.py.

---
