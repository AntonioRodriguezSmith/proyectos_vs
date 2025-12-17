from conducta.utilidades_texto import comprimir_texto

def test_comprimir_texto_resumen():
    texto = "palabra " * 100
    resumen = comprimir_texto(texto, max_palabras=10)
    assert resumen.count("palabra") == 10
    assert resumen.endswith("...")

def test_comprimir_texto_corto():
    texto = "esto es corto"
    resumen = comprimir_texto(texto, max_palabras=10)
    assert resumen == texto
