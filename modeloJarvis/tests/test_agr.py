
from agr.agente_agr import AgenteAGR

def test_inicializacion_agr():
    agr = AgenteAGR()
    assert agr is not None

def test_inferencia_agr():
    agr = AgenteAGR()
    entrada = "¿Cuál es la capital de Francia?"
    respuesta = agr.inferir(entrada)
    assert isinstance(respuesta, str)
    assert "AGR" in respuesta or "Respuesta generada" in respuesta
