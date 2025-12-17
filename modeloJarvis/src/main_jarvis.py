"""
Punto de entrada principal para el agente J.A.R.V.I.S.
Permite interactuar por consola usando la arquitectura modular actual.
"""

from jarvis_model import JarvisModel

if __name__ == "__main__":
    jarvis = JarvisModel()
    print("J.A.R.V.I.S. iniciado. Escribe tu mensaje (Ctrl+C para salir):")
    while True:
        try:
            entrada = input("Usuario: ")
            respuesta = jarvis.inferir(entrada)
            print("JARVIS:", respuesta)
        except KeyboardInterrupt:
            print("\nSaliendo de J.A.R.V.I.S.")
            break
