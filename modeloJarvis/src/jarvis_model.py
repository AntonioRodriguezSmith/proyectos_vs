"""
Módulo principal del modelo J.A.R.V.I.S.
Integra la lógica de conducta (modos, patrones, personalidad) y el razonamiento generativo (AGR).
Permite procesar entradas, decidir la mejor estrategia de respuesta y mantener el contexto del agente.
"""

from conducta.agente import AgenteConducta
from agr.agente_agr import AgenteAGR

class JarvisModel:
    def __init__(self):
        """
        Inicializa los módulos de conducta y AGR.
        """
        self.conducta = AgenteConducta()
        self.agr = AgenteAGR()
        self.modo_activo = None

    def entrenar(self, datos):
        """
        Entrena el modelo de aprendizaje (AGR) con los datos proporcionados.
        """
        self.agr.entrenar(datos)

    def inferir(self, entrada):
        """
        Procesa una entrada:
        1. Intenta responder usando modos o patrones de conducta.
        2. Si no hay modo especial, delega la inferencia al razonamiento generativo (AGR).
        Devuelve la respuesta generada y actualiza el modo activo.
        """
        respuesta_conducta, modo = self.conducta.inferir(entrada)
        if modo:
            self.modo_activo = modo
            return respuesta_conducta
        self.modo_activo = None
        return self.agr.inferir(entrada)
