
import os
import json
from conducta.agente import AgenteConducta

def test_carga_modos():
    agente = AgenteConducta()
    assert isinstance(agente.modos, dict)
    assert "La Jumpa" in agente.modos
    assert "Brains & Bytes" in agente.modos

def test_carga_patrones():
    agente = AgenteConducta()
    assert isinstance(agente.patrones, dict)
    assert "La Jumpa" in agente.patrones
    assert "Brains & Bytes" in agente.patrones

def test_carga_diccionario():
    # Ajuste de ruta: ahora src está dentro de modeloJarvis
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    recursos_dir = os.path.join(base_dir, 'src', 'conducta', 'recursos')
    diccionario_path = os.path.join(recursos_dir, 'diccionario.json')
    with open(diccionario_path, 'r', encoding='utf-8') as f:
        diccionario = json.load(f)
    assert isinstance(diccionario, dict)
    assert "duro" in diccionario
    assert "Narf" in diccionario
