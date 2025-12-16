---
- [ ] Modularizar y centralizar todas las dependencias externas y servicios del monorepo en módulos reutilizables y mantenibles (tarea global, afecta a todos los proyectos)
---
## Checklist de funcionamiento y dependencias para main_jarvis.py

- [ ] Python 3.14 instalado (o versión compatible ≥ 3.8 si no usas relanzador).
- [ ] El entorno virtual está activado (opcional pero recomendable).
- [ ] El script se ejecuta desde el directorio correcto o usa rutas relativas a __file__.
- [ ] Existen los archivos: diccionario.json, modos_trabajo.json, patrones.json en el mismo directorio que main_jarvis.py.
- [ ] Existen los archivos de configuración y base de datos (se crean automáticamente si no existen).
- [ ] requests instalado
- [ ] certifi instalado
- [ ] sqlite3 disponible (incluida en Python estándar)
- [ ] psutil instalado (opcional, solo para detección avanzada de VPN)
- [ ] wikipedia instalado (opcional, solo para búsquedas en Wikipedia)
- [ ] Permisos de lectura y escritura en el directorio del script.
- [ ] Conexión a Internet para funciones externas (traducción, OpenAI, Wikipedia, APIs, etc).
# Tareas pendientes para modeloJarvis

- [ ] Analizar la posibilidad de ejecutar Jarvis (API) con un solo comando desde cualquier ubicación del monorepo (por ejemplo, usando un script o ajustando PYTHONPATH).
- [ ] Documentar la mejor práctica para lanzar el asistente y evitar errores de importación.
- [ ] Documentar y explicar el patrón de gestión de rutas y acceso a recursos en main.py y jarvis_model.py.
- [ ] Centralizar la carga de configuraciones (config.json, diccionario.json) en un módulo utilitario.
- [ ] Añadir validaciones de entrada en la API para robustez y seguridad.
- [ ] Implementar manejo de errores y logs claros en la API y el modelo.
- [ ] Modularizar la gestión de modos especiales, permitiendo añadir nuevos modos fácilmente (posible carga desde archivo).
- [ ] Añadir y mejorar pruebas automáticas para modos especiales, perfiles y acceso a recursos.
- [ ] Documentar en README y scripts el patrón de acceso a recursos y cómo adaptar el código si cambia la estructura.
- [ ] Limpiar y depurar el código: eliminar comentarios obsoletos, funciones sin uso y asegurar docstrings claros.

---
---

## Checklist git y control de versiones

- [ ] Revisar y limpiar la estructura local: dejar solo archivos y carpetas que se quieran conservar y versionar.
- [ ] Inicializar git en la raíz correcta (ya hecho en proyectos_vs).
- [ ] Añadir todos los archivos al control de versiones: `git add .`
- [ ] Hacer un commit inicial: `git commit -m "Estructura base alineada y lista para migración/cambio de estructura"`
- [ ] Configurar el repositorio remoto: `git remote add origin https://github.com/AntonioRodriguezSmith/<nombre-repo>`
- [ ] Hacer push de todos los cambios: `git push -u origin main`
- [ ] Crear una rama de backup del estado actual: `git checkout -b backup-2025`
- [ ] Subir la rama de backup: `git push -u origin backup-2025`
- [ ] Crear una rama experimental para la nueva estructura: `git checkout -b experimental-2025`
- [ ] Trabajar en la rama experimental y realizar commits frecuentes.
- [ ] Si la nueva estructura es válida, renombrar ramas o actualizar la rama principal en GitHub.
- [ ] Documentar en README y tareas cualquier cambio relevante en la gestión de ramas.

---
**Norma:** Las tareas propias de este proyecto deben mantenerse en este archivo local. El directorio central de tareas solo debe contener tareas globales o enlaces a este archivo. No mezclar tareas globales y locales.
