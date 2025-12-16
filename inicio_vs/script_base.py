import platform
import getpass

# Saludo personalizado (puedes personalizar el nombre desde cada script de PC)
def saludo(nombre, pc):
    print(f"Bienvenido, {nombre}, al entorno de trabajo {pc}.")

# Datos básicos del PC
def info_pc():
    usuario = getpass.getuser()
    sistema = platform.system()
    version = platform.version()
    maquina = platform.node()
    print(f"Usuario: {usuario}")
    print(f"Sistema operativo: {sistema}")
    print(f"Versión del sistema: {version}")
    print(f"Nombre del equipo: {maquina}")

# Espacio reservado para comprobaciones futuras
def comprobaciones():
    print("[Comprobaciones pendientes de implementar]")

# Para lanzar J.A.R.V.I.S. desde cualquier ubicación del monorepo, usa el script run_jarvis.bat en la raíz.
# Ejemplo:
#   ./run_jarvis.bat
