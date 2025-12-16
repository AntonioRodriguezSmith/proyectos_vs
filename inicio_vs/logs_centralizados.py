"""
Sistema de logs centralizados para PROYECTOS_VS.
Registra eventos y actividad de todos los proyectos en un log común.
"""
def registrar_evento(mensaje, nivel="INFO"):
    with open("logs_centralizados.log", "a", encoding="utf-8") as f:
        f.write(f"[{nivel}] {mensaje}\n")
    print(f"[{nivel}] {mensaje}")

# Ejemplo de uso
if __name__ == "__main__":
    registrar_evento("Inicio de sesión en el ecosistema.")
