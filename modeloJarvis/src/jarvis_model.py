"""
Módulo principal del modelo J.A.R.V.I.S.
Incluye la clase base y métodos para entrenamiento e inferencia.
"""

class JarvisModel:
    def __init__(self):
        # Modos especiales: clave -> nombre del modo
        self.modos = {
            "arrebatao": "la jumpa (Arcangel)"
            # Añadir aquí más palabras clave y modos en el futuro
        }
        self.modo_activo = None

    def entrenar(self, datos):
        """Entrena el modelo con los datos proporcionados."""
        pass

    def inferir(self, entrada):
        """Realiza inferencia sobre una entrada dada. Detecta modos especiales por palabra clave."""
        for clave, modo in self.modos.items():
            if clave in entrada.lower():
                self.modo_activo = modo
                return f"[Modo especial activado: {modo}] ¡Aquí Arcangel, en modo 'la jumpa'! ¿Qué necesitas?"
        self.modo_activo = None
        return "[Respuesta generada por J.A.R.V.I.S.]"
