# Arquitectura e Integración del Ecosistema PROYECTOS_VS

## Diagrama de arquitectura (texto)

- orquestador_vs (inicio_vs)
  ├── modeloRagAlejandria (biblioteca central)
  ├── modeloJarvis (asistente IA)
  ├── modeloRagAtenas (contenedor de subproyectos)
  ├── modeloRagEsparta (contenedor de subproyectos)
  └── ... (futuros proyectos)

Todos los proyectos están conectados mediante el registro central (proyectos_registry.json) y pueden accederse entre sí usando utilidades_acceso.py.

## Flujo de integración
- Al crear/modificar un proyecto, ejecuta conexion_proyectos.py para actualizar el registro.
- Usa utilidades_acceso.py para localizar y comunicarte con cualquier proyecto.
- El orquestador_vs.py gestiona el arranque, backups, historial y sincronización.

## Automatizaciones implementadas
- Detección de entorno y perfil.
- Carga/creación de historial de sesión.
- Backup automático de J.A.R.V.I.S.
- Registro y acceso dinámico a todos los proyectos.
- Sincronización y verificación de integridad.

## Mejoras pendientes
- Sistema de notificaciones/alertas automáticas.
- Políticas de acceso y cifrado para datos sensibles.
- Revisión periódica de backups y sincronización.
