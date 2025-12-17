# Archivo formateado desde tareas_central.md

## Ideas y próximos pasos

## Tarea global prioritaria

# 3. Tarea global prioritaria Tareas y estado actual del sistema#

- Si necesitas más automatismos, documenta el flujo y el script asociado.

## Estado actual

## Tareas git y migración de estructura

Repositorio remoto: https://github.com/AntonioRodriguezSmith

Revisar y limpiar la estructura local: dejar solo archivos y carpetas que se quieran conservar y versionar.

1. Mantener actualizados los archivos de tareas locales y centralizados.
2. Revisar y mejorar la organización y nomenclatura de carpetas y archivos en todos los proyectos.
3. Documentar y transferir cualquier cambio relevante a Alejandría para trazabilidad.
4. Planificar la automatización de la sincronización de tareas y la creación de nuevos proyectos en el futuro.

## Ideas y próximos pasos

- Automatizar la sincronización de tareas entre proyectos y la carpeta central.
- Diseñar un script maestro para la creación de nuevos proyectos, copiando plantillas y estructura desde Alejandría.
- Documentar el flujo ideal de creación y gestión de proyectos en README y knowledge_base.
- Consolidar y simplificar la estructura de carpetas para evitar duplicidades y facilitar la escalabilidad.
- Añadir tests automáticos para los modos especiales y el uso del diccionario en Jarvis.
- Centralizar la gestión de configuraciones compartidas (como el diccionario) en un módulo o servicio común.
- Mejorar la documentación de integración entre asistentes (Jarvis, Arcangel, etc.).

## Tareas por proyecto

---
Cada proyecto debe mantener su propio archivo de tareas actualizado y enlazado aquí para facilitar la gestión y trazabilidad.
---

1. Documentar en README y en Alejandría los cambios recientes y la estructura final.
2. Validar que el script Atenas.py funcione correctamente con la nueva ubicación de los datos (modeloRagAtenas/datos/nomenclaturas_Atenas.*).
3. Revisar y actualizar cualquier referencia en scripts o documentación a las rutas antiguas de nomenclaturas.
4. Realizar una copia de seguridad de la estructura final y los datos clave.

### Acciones realizadas

### Observaciones
- El control de versiones con git está inactivo, por lo que este archivo sirve como registro manual de cambios y tareas.
- Mantener este archivo actualizado hasta que git vuelva a estar operativo.

---

2. Inicializar git en la raíz correcta (ya hecho en proyectos_vs).
3. Añadir todos los archivos al control de versiones: git add .
4. Hacer un commit inicial: git commit -m "Estructura base alineada y lista para migración a ASR"
5. Configurar el repositorio remoto de ASR: git remote add origin <URL-del-repo-ASR>
6. Hacer push de todos los cambios: git push -u origin main
7. Verificar en ASR que la estructura y los archivos subidos son los correctos.
8. Realizar cualquier cambio mayor (reorganización, migración, etc.) ya bajo control de versiones.

Actualiza o elimina esta sección una vez completada la migración.
