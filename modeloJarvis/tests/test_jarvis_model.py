from src.jarvis_model import JarvisModel

def test_inferencia_basica():
    modelo = JarvisModel()
    entrada = "Hola, ¿quién eres?"
    respuesta = modelo.inferir(entrada)
    assert isinstance(respuesta, str)
    assert "J.A.R.V.I.S." in respuesta or respuesta != ""
