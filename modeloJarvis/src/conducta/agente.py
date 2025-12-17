"""
Módulo: agente.py
Clase principal para la gestión de la conducta del agente Jarvis.
Incluye la lógica de modos, patrones y personalidad.
"""

class AgenteConducta:
    def __init__(self):
        """
        Inicializa los modos y patrones de conducta cargando desde archivos JSON.
        """
        import os
        import json
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        recursos_dir = os.path.join(base_dir, 'asistente_jarvis')
        # Cargar modos
        modos_path = os.path.join(recursos_dir, 'modos_trabajo.json')
        patrones_path = os.path.join(recursos_dir, 'patrones.json')
        self.modos = {}
        self.patrones = {}
        try:
            with open(modos_path, 'r', encoding='utf-8') as f:
                self.modos = json.load(f)
        except Exception as e:
            print(f"[AgenteConducta] Error cargando modos: {e}")
        try:
            with open(patrones_path, 'r', encoding='utf-8') as f:
                self.patrones = json.load(f)
        except Exception as e:
            print(f"[AgenteConducta] Error cargando patrones: {e}")
        self.modo_activo = None

    def inferir(self, entrada):
        """
        Procesa la entrada y determina si se debe activar un modo especial.
        Devuelve (respuesta, modo) donde modo es None si no se activa ninguno.
        """
        entrada_lower = entrada.lower()
        for modo_nombre, modo_info in self.modos.items():
            if modo_nombre.lower() in entrada_lower:
                self.modo_activo = modo_nombre
                # Buscar patrón asociado
                patron = self.patrones.get(modo_nombre, {})
                broma = patron.get('broma') if isinstance(patron, dict) else None
                respuesta = f"[Modo especial activado: {modo_nombre}] "
                if broma:
                    respuesta += broma
                else:
                    respuesta += modo_info.get('saludo', f"¡Modo {modo_nombre} activado!")
                return (respuesta, modo_nombre)
        self.modo_activo = None
        return (None, None)
