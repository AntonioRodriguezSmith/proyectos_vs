# Perfil DXC para BANCO SABADELL en J.A.R.V.I.S.

## Descripción
Este perfil activa un modo de alta seguridad y especialización para operaciones relacionadas con BANCO SABADELL bajo el entorno DXC. Todas las acciones están sujetas a auditoría y restricciones estrictas.

## Funcionalidades principales
- **info_banco_sabadell()**: Muestra advertencias de seguridad y contexto operativo.
- **aprender_banco_sabadell(info)**: Permite almacenar conocimientos relevantes sobre BANCO SABADELL (solo en perfil DXC).
- **consultar_conocimiento_banco_sabadell(clave=None)**: Consulta los conocimientos almacenados sobre BANCO SABADELL.
- **registrar_interaccion_banco_sabadell(mensaje, respuesta)**: Registra interacciones específicas bajo contexto de alta seguridad.

## Ejemplo de uso
```python
jarvis = Jarvis()
jarvis.inicializar_perfil()
print(jarvis.info_banco_sabadell())
print(jarvis.aprender_banco_sabadell("Procedimiento seguro de onboarding digital para clientes empresariales."))
print(jarvis.consultar_conocimiento_banco_sabadell())
print(jarvis.registrar_interaccion_banco_sabadell(
    "¿Cómo se realiza el onboarding digital?",
    "Se sigue el procedimiento seguro de onboarding digital para clientes empresariales."
))
```

## Seguridad
- Acciones sensibles restringidas automáticamente.
- Todo aprendizaje y consulta sobre BANCO SABADELL solo es posible en perfil DXC.
- Cada interacción queda registrada y auditada.

## Extensión
Para otros perfiles (MTP, ASR), añade lógica y documentación similar cuando cambies de contexto.
