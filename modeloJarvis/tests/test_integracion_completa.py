
from jarvis_model import JarvisModel

def test_integracion_completa():
    modelo = JarvisModel()
    entradas = [
        "Hola, ¿quién eres?",
        "Activa La Jumpa",
        "Quiero el modo Brains & Bytes",
        "Esto no activa ningún modo"
    ]
    for entrada in entradas:
        respuesta = modelo.inferir(entrada)
        assert isinstance(respuesta, str)
        assert respuesta != ""
