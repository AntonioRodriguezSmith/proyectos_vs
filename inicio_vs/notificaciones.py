"""
Sistema básico de notificaciones/alertas para el ecosistema PROYECTOS_VS.
Puede ampliarse para enviar emails, logs o mensajes a otros sistemas.
"""
def notificar(mensaje, nivel="INFO"):
    with open("notificaciones.log", "a", encoding="utf-8") as f:
        f.write(f"[{nivel}] {mensaje}\n")
    print(f"[{nivel}] {mensaje}")

# Ejemplo de uso
if __name__ == "__main__":
    notificar("Prueba de alerta automática.", nivel="ALERTA")
