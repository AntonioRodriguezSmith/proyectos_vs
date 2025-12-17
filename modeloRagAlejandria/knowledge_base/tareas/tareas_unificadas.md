# Tareas unificadas de knowledge_base/tareas (modeloRagAlejandria)

---

## Tareas globales y migración de estructura

- Revisar y limpiar la estructura local: dejar solo archivos y carpetas que se quieran conservar y versionar.
- Inicializar git en la raíz correcta (ya hecho en proyectos_vs).
- Añadir todos los archivos al control de versiones: `git add .`
- Hacer un commit inicial: `git commit -m "Estructura base alineada y lista para migración/cambio de estructura"`
- Configurar el repositorio remoto: `git remote add origin https://github.com/AntonioRodriguezSmith/<nombre-repo>`
- Hacer push de todos los cambios: `git push -u origin main`
- Crear una rama de backup del estado actual: `git checkout -b backup-2025`
- Subir la rama de backup: `git push -u origin backup-2025`
- Crear una rama experimental para la nueva estructura: `git checkout -b experimental-2025`
- Trabajar en la rama experimental y realizar commits frecuentes.
- Si la nueva estructura es válida, renombrar ramas o actualizar la rama principal en GitHub.
- Documentar en README y tareas cualquier cambio relevante en la gestión de ramas.

### Ideas y próximos pasos
- Automatizar la sincronización de tareas entre proyectos y la carpeta central.
- Diseñar un script maestro para la creación de nuevos proyectos, copiando plantillas y estructura desde Alejandría.
- Documentar el flujo ideal de creación y gestión de proyectos en README y knowledge_base.
- Consolidar y simplificar la estructura de carpetas para evitar duplicidades y facilitar la escalabilidad.
- Implementar endpoints en la API de Jarvis para consultar o modificar el diccionario de expresiones.
- Añadir tests automáticos para los modos especiales y el uso del diccionario en Jarvis.
- Centralizar la gestión de configuraciones compartidas (como el diccionario) en un módulo o servicio común.
- Mejorar la documentación de integración entre asistentes (Jarvis, Arcangel, etc.).

---

## Tareas principales del workspace

- Informe DXC (informe para Manuel): completar y entregar el informe ejecutivo solicitado.
- Reestructurar directorio: organizar carpetas y proyectos para mayor claridad y mantenimiento.
- Terminar proyecto inicio: finalizar y documentar el script de inicio general del workspace.
- Terminar proyecto Jarvis: completar el asistente y su lógica principal.
- Terminar proyecto Alejandría: finalizar el modelo, documentación y ADRs globales.
- Sincronizar y hacer backup automático de JarvisModel cada día a las 03:00 (tarea programada Windows)
- Sincronizar métodos clave entre main_jarvis.py y jarvis_model.py tras cada actualización
- Revisar y actualizar documentación de modos y patrones tras cada cambio relevante

---

## Tareas de informes_ejecutivos

1. Documentar en README y en Alejandría los cambios recientes y la estructura final.
2. Validar que el script Atenas.py funcione correctamente con la nueva ubicación de los datos (modeloRagAtenas/datos/nomenclaturas_Atenas.*).
3. Revisar y actualizar cualquier referencia en scripts o documentación a las rutas antiguas de nomenclaturas.
4. Realizar una copia de seguridad de la estructura final y los datos clave.

### Acciones realizadas
- Eliminadas carpetas y archivos duplicados o innecesarios (002, 001 duplicados, presentaciones vacías, gestor_nomenclaturas.py).
- Renombrados y reubicados los archivos de nomenclaturas como nomenclaturas_Atenas.json y nomenclaturas_Atenas.md en modeloRagAtenas/datos.
- Actualizados y reorganizados todos los README según su responsabilidad.
- Validada la estructura y limpieza de informes_ejecutivos.

### Observaciones
- El control de versiones con git está inactivo, por lo que este archivo sirve como registro manual de cambios y tareas.
- Mantener este archivo actualizado hasta que git vuelva a estar operativo.

---

## Tareas pendientes para modeloJarvis

- Analizar la posibilidad de ejecutar Jarvis (API) con un solo comando desde cualquier ubicación del monorepo (por ejemplo, usando un script o ajustando PYTHONPATH).
- Documentar la mejor práctica para lanzar el asistente y evitar errores de importación.

---

## Tareas temporales para migración a ASR

1. Revisar y limpiar la estructura local: dejar solo archivos y carpetas que se quieran conservar y versionar.
2. Inicializar git en la raíz correcta (ya hecho en proyectos_vs).
3. Añadir todos los archivos al control de versiones: git add .
4. Hacer un commit inicial: git commit -m "Estructura base alineada y lista para migración a ASR"
5. Configurar el repositorio remoto de ASR: git remote add origin <URL-del-repo-ASR>
6. Hacer push de todos los cambios: git push -u origin main
7. Verificar en ASR que la estructura y los archivos subidos son los correctos.
8. Realizar cualquier cambio mayor (reorganización, migración, etc.) ya bajo control de versiones.

---

## Tareas de validacion-icaria

- Utilizar modelos para proyecto DXC

---

(Archivo generado automáticamente el 16 de diciembre de 2025, unificando todas las tareas de knowledge_base/tareas)
