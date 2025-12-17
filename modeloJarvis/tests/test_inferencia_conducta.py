
from jarvis_model import JarvisModel

# Test de inferencia de conducta (modos y patrones)
def test_inferencia_modo_lajumpa():
    modelo = JarvisModel()
    entrada = "Activa La Jumpa"
    respuesta = modelo.inferir(entrada)
    assert "La Jumpa" in respuesta
    assert "Modo especial activado" in respuesta

def test_inferencia_modo_brainsbytes():
    modelo = JarvisModel()
    entrada = "Quiero el modo Brains & Bytes"
    respuesta = modelo.inferir(entrada)
    assert "Brains & Bytes" in respuesta
    assert "Modo especial activado" in respuesta

# Test de inferencia AGR (respuesta por defecto)
def test_inferencia_agr():
    modelo = JarvisModel()
    entrada = "Esto no activa ningún modo"
    respuesta = modelo.inferir(entrada)
    assert "AGR" in respuesta or "Respuesta generada" in respuesta
