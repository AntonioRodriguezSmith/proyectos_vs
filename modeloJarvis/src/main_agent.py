from conducta.agente import AgenteConducta
from conducta.memoria import MemoriaConducta
from agr.agr_agent import AGRAgent

class AgenteUnificado:
    def __init__(self):
        self.memoria = MemoriaConducta()
        self.conducta = AgenteConducta(self.memoria)
        self.agr = AGRAgent(self.memoria)

    def procesar(self, entrada):
        # 1. Percepción y preprocesado
        percepcion = self.conducta.percibir(entrada)
        # 2. Decisión de conducta: ¿hay modo especial, patrón, o delegar a AGR?
        if self.conducta.es_modo_especial(percepcion):
            respuesta = self.conducta.responder_modo(percepcion)
        elif self.conducta.delegar_a_agr(percepcion):
            respuesta = self.agr.procesar(percepcion)
        else:
            respuesta = self.conducta.responder(percepcion)
        # 3. Actualizar memoria/contexto
        self.memoria.actualizar(percepcion, respuesta)
        return respuesta

# Ejemplo de uso
if __name__ == "__main__":
    agente = AgenteUnificado()
    while True:
        entrada = input("Usuario: ")
        print("Agente:", agente.procesar(entrada))
