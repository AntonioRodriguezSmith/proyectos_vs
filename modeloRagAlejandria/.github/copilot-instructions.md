# Instrucciones para agentes de IA en modeloRagAlejandria

## Visión general y arquitectura
- Este repositorio es el "centro de conocimiento" para un sistema RAG (Retrieval-Augmented Generation) multi-proyecto, inspirado en la Biblioteca de Alejandría.
- Cada subproyecto es una "ciudad histórica" (ej: modeloRagAtenas, modeloRagEsparta) y sigue la convención de estar bajo control de versiones y documentado en el índice central (INDEX.md).
- El archivo INDEX.md es el punto de partida para recursos, decisiones técnicas y enlaces a subproyectos.
- El asistente principal es J.A.R.V.I.S., con modos de personalidad y seguridad adaptativos según el entorno (DXC, ARS, MTP).

## Flujos y convenciones clave
- Antes de crear/modificar archivos o estructuras, **siempre pide confirmación al usuario**.
- Usa los iconos y etiquetas de personalidad definidos en DICCIONARIO.md e INDEX.md para marcar el tono de mensajes, commits y documentación.
- Los modos de trabajo y patrones de humor/seriedad están en asistente_jarvis/modos_trabajo.json y patrones.json.
- El perfil DXC activa restricciones y auditoría especial (ver asistente_jarvis/PERFIL_DXC_BANCO_SABADELL.md).
- Configuraciones y datos sensibles se gestionan en archivos JSON dentro de asistente_jarvis/.

## Ejemplos de patrones y estilos
- Ejemplo de commit: `🚨 [IMPORTANTE] Refactoriza el flujo de autenticación para mayor seguridad`
- Ejemplo de saludo: `¡Hola Tony! ¿Listo para conquistar Visual Studio?`
- Ejemplo de advertencia: `👹 No tocar este script sin backup previo`

## Dependencias y herramientas
- Python >= 3.10, Git, Markdown, Visual Studio Code
- Extensiones VS Code recomendadas: ms-python.python, ms-toolsai.jupyter, yzhang.markdown-all-in-one, eamodio.gitlens, esbenp.prettier-vscode

## Archivos clave
- README.md: Descripción general y pautas
- INDEX.md: Índice central y recursos
- DICCIONARIO.md: Jerga, iconos y nomenclatura
- asistente_jarvis/main_jarvis.py: Lógica principal de J.A.R.V.I.S.
- asistente_jarvis/modos_trabajo.json: Modos de personalidad
- asistente_jarvis/patrones.json: Patrones de humor y frases
- asistente_jarvis/PERFIL_DXC_BANCO_SABADELL.md: Seguridad DXC

## Notas finales
- Documenta toda decisión relevante en INDEX.md.
- Si cambias de entorno o perfil, actualiza la documentación y los archivos de configuración.
- Mantén la coherencia en iconos, etiquetas y tono en todo el proyecto.
