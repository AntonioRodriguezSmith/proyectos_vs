
# --- Lanzador automático con Python 3.14 si está disponible ---
import sys
import os
import json
from pathlib import Path

# Ruta al archivo __install__.json (ajustar si es necesario)
import getpass
import platform
def get_install_json_path():
    user = getpass.getuser()
    system = platform.system()
    if system == "Windows":
        # Busca en la carpeta AppData del usuario actual
        base = os.path.expandvars(r'%LOCALAPPDATA%')
        # Busca cualquier carpeta pythoncore-3.14-*
        python_dir = None
        for d in os.listdir(base + r'\Python') if os.path.exists(base + r'\Python') else []:
            if d.startswith('pythoncore-3.14-'):
                python_dir = os.path.join(base, 'Python', d)
                break
        if python_dir:
            path = os.path.join(python_dir, '__install__.json')
            if os.path.exists(path):
                return path
        # Fallback: ruta por defecto
        return os.path.join(base, 'Python', 'pythoncore-3.14-64', '__install__.json')
    else:
        # Para otros sistemas, ajustar si es necesario
        return ''
INSTALL_JSON = get_install_json_path()

def relanzar_con_python314():
    if sys.version_info[:2] == (3, 14):
        return  # Ya estamos en Python 3.14
    if os.path.exists(INSTALL_JSON):
        with open(INSTALL_JSON, encoding='utf-8') as f:
            data = json.load(f)
        # Buscar el alias python3.14.exe
        for alias in data.get('alias', []):
            if alias.get('name') == 'python3.14.exe':
                python314_path = os.path.join(os.path.dirname(INSTALL_JSON), alias['name'])
                if os.path.exists(python314_path):
                    # Relanzar el script con python3.14.exe
                    os.execv(python314_path, [python314_path] + sys.argv)
    # Si no se encuentra, continuar normalmente

relanzar_con_python314()

"""
J.A.R.V.I.S. - Asistente Personal Inteligente para Tony Stark

Enfoque principal:
1. Aprendizaje y adaptación a preferencias.
2. Integración con APIs y servicios.
3. Historial de interacciones y sugerencias.
4. Automatización de flujos.
5. Múltiples personalidades/modos.
10. Seguridad y privacidad.

Otros puntos: Panel de métricas, gamificación, multilingüe, interfaz, etc.
"""


import datetime
import json
import platform
import getpass
from pathlib import Path
try:
    import wikipedia
except ImportError:
    wikipedia = None


import requests
import certifi
try:
    import psutil
except ImportError:
    psutil = None



def cargar_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


class Jarvis:
    def ejemplo_patron(self, nombre):
        """Devuelve un ejemplo de patrón según el nombre, usando patrones.json."""
        if not hasattr(self, 'patrones') or self.patrones is None:
            return "No se han cargado patrones."
        patron = self.patrones.get(nombre)
        if patron:
            if isinstance(patron, dict) and 'ejemplo' in patron:
                return patron['ejemplo']
            elif isinstance(patron, str):
                return patron
            else:
                return f"Ejemplo de patrón para '{nombre}': {patron}"
        else:
            return f"No se encontró un patrón llamado '{nombre}'."

    def traducir_texto(self, texto, dest="en", src="es"):
        """Traduce texto usando la API gratuita de MyMemory."""
        import requests
        import certifi
        url = "https://api.mymemory.translated.net/get"
        params = {"q": texto, "langpair": f"{src}|{dest}"}
        try:
            response = requests.get(url, params=params, timeout=10, verify=certifi.where())
            if response.status_code == 200:
                data = response.json()
                return data.get("responseData", {}).get("translatedText", "[Sin traducción]")
            else:
                return f"Error HTTP: {response.status_code}"
        except Exception as e:
            return f"Error al traducir: {e}"
    def comprobar_acceso_url(self, url):
        """Comprueba si se permite el acceso a una URL bajo el perfil actual. Registra bloqueos en logs de seguridad."""
        perfil = self.obtener_perfil()
        # Lista de URLs restringidas en DXC (puedes ampliarla)
        urls_restringidas = [
            "openai.com", "github.com", "api.stackexchange.com", "duckduckgo.com", "uselessfacts.jsph.pl", "official-joke-api.appspot.com"
        ]
        if perfil == "DXC":
            for restringida in urls_restringidas:
                if restringida in url:
                    self.guardar_log("seguridad", f"Bloqueo de acceso a URL restringida en DXC: {url}")
                    return False, f"Acceso bloqueado a {url} por política de seguridad DXC."
        return True, "Acceso permitido."
    def esta_conectado_vpn(self):
        """Devuelve 'sí' si la VPN corporativa está activa y el perfil DXC ha sido activado automáticamente, 'no' en caso contrario."""
        vpn_activa, detalle_vpn = self.detectar_vpn()
        if vpn_activa and ("DXC" in detalle_vpn or "Appgate" in detalle_vpn):
            return "sí"
        return "no"

    # --- Detección de VPN corporativa ---
    def detectar_vpn(self):
        """Detecta si Jarvis está operando bajo una VPN corporativa (DXC, Appgate SDP, etc.) usando heurísticas de red, variables de entorno o procesos."""
        import os, socket
        # psutil puede ser None si no está instalado
        # Heurística 1: Variable de entorno personalizada
        if os.environ.get("VPN_DXC_ACTIVA") == "1":
            self.guardar_log("seguridad", "VPN DXC detectada por variable de entorno.")
            return True, "VPN DXC detectada por variable de entorno."
        if os.environ.get("APPGATE_SDP") == "1":
            self.guardar_log("seguridad", "VPN Appgate SDP detectada por variable de entorno.")
            return True, "VPN Appgate SDP detectada por variable de entorno."
        # Heurística 2: Rango de IP típico de la VPN (ejemplo ficticio)
        try:
            ip_local = socket.gethostbyname(socket.gethostname())
            if ip_local.startswith("10.200.") or ip_local.startswith("172.30."):
                self.guardar_log("seguridad", f"VPN DXC detectada por IP local: {ip_local}")
                return True, f"VPN DXC detectada por IP local: {ip_local}"
            if ip_local.startswith("100.64."):
                self.guardar_log("seguridad", f"VPN Appgate SDP detectada por IP local: {ip_local}")
                return True, f"VPN Appgate SDP detectada por IP local: {ip_local}"
        except Exception:
            pass
        # Heurística 3: DNS corporativo
        try:
            dominio = socket.getfqdn()
            if "dxc" in dominio.lower() or "sabadell" in dominio.lower():
                self.guardar_log("seguridad", f"VPN DXC detectada por dominio: {dominio}")
                return True, f"VPN DXC detectada por dominio: {dominio}"
            if "appgate" in dominio.lower():
                self.guardar_log("seguridad", f"VPN Appgate SDP detectada por dominio: {dominio}")
                return True, f"VPN Appgate SDP detectada por dominio: {dominio}"
        except Exception:
            pass
        # Heurística 4: Proceso Appgate SDP activo
        if psutil:
            try:
                for proc in psutil.process_iter(['name']):
                    if proc.info['name'] and "appgate" in proc.info['name'].lower():
                        self.guardar_log("seguridad", "VPN Appgate SDP detectada por proceso activo.")
                        return True, "VPN Appgate SDP detectada por proceso activo."
            except Exception:
                pass
        return False, "No se detectó VPN corporativa activa."
    # --- Especialización DXC para BANCO SABADELL ---
    def info_banco_sabadell(self):
                                        """Devuelve información clave y advertencias de seguridad para el contexto DXC - BANCO SABADELL."""
                                        perfil = self.obtener_perfil()
                                        if perfil != "DXC":
                                            return "Funcionalidad solo disponible en perfil DXC."
                                        advertencia = "[ALTA SEGURIDAD] Todas las acciones y consultas están sujetas a auditoría y restricción según las políticas de DXC y BANCO SABADELL."
                                        info = "Contexto: Operando bajo perfil DXC para BANCO SABADELL. Prioriza la protección de datos, cumplimiento normativo y registro de toda interacción."
                                        return f"{advertencia}\n{info}"

    def consultar_conocimiento_banco_sabadell(self, clave=None):
                                        """Consulta conocimientos almacenados sobre BANCO SABADELL en perfil DXC."""
                                        perfil = self.obtener_perfil()
                                        if perfil != "DXC":
                                            return "Funcionalidad solo disponible en perfil DXC."
                                        resultados = {k: v for k, v in self.conocimientos.items() if k.startswith('BANCO_SABADELL')}
                                        if clave:
                                            return resultados.get(clave, "No se encontró información para esa clave.")
                                        return resultados

    def registrar_interaccion_banco_sabadell(self, mensaje, respuesta):
                                        """Registra interacciones específicas de BANCO SABADELL bajo perfil DXC con métrica de seguridad."""
                                        perfil = self.obtener_perfil()
                                        if perfil != "DXC":
                                            return "Funcionalidad solo disponible en perfil DXC."
                                        self.registrar_interaccion(mensaje, respuesta)
                                        self.registrar_metrica("interaccion_banco_sabadell", f"{mensaje} -> {respuesta}")
                                        return "Interacción registrada bajo contexto de alta seguridad."
    # --- Gestión de perfiles (DXC, MTP, ASR) ---
    def detectar_perfil(self):
                                    """Detecta automáticamente el perfil activo (DXC, MTP, ASR) según configuración, entorno o heurística."""
                                    # Aquí puedes mejorar la lógica según variables de entorno, archivos, etc.
                                    # Por ahora, se asume DXC como perfil por defecto.
                                    perfil = self.obtener_configuracion("perfil_activo")
                                    if perfil:
                                        self.perfil = perfil
                                    else:
                                        self.perfil = "DXC"
                                        self.guardar_configuracion("perfil_activo", "DXC")
                                    return self.perfil

    def cambiar_perfil(self, nuevo_perfil):
                                    """Cambia el perfil activo y actualiza la configuración."""
                                    self.perfil = nuevo_perfil
                                    self.guardar_configuracion("perfil_activo", nuevo_perfil)
                                    return f"Perfil cambiado a {nuevo_perfil}"

    def obtener_perfil(self):
                                    """Devuelve el perfil activo actual."""
                                    return getattr(self, 'perfil', self.detectar_perfil())

    def comportamiento_seguro(self, accion, usuario=None):
                                    """Evalúa si una acción es segura según el perfil y aplica restricciones si es necesario. Registra logs de seguridad en caso de intento restringido."""
                                    perfil = self.obtener_perfil()
                                    if perfil == "DXC":
                                        acciones_restringidas = ["eliminar", "modificar_config_critica", "exportar_datos"]
                                        if accion in acciones_restringidas:
                                            self.guardar_log("seguridad",
                                                f"Intento de acción restringida: {accion} | Usuario: {usuario if usuario else 'desconocido'} | Perfil: DXC")
                                            return False, f"Acción '{accion}' restringida en perfil DXC por seguridad."
                                    return True, "Acción permitida."
    def acceso_dato_sensible(self, clave, usuario=None):
        """Permite acceso a datos sensibles solo si el perfil y permisos lo autorizan. Registra log de acceso."""
        perfil = self.obtener_perfil()
        if perfil != "DXC":
            self.guardar_log("seguridad", f"Intento de acceso a dato sensible '{clave}' fuera de perfil DXC | Usuario: {usuario if usuario else 'desconocido'}")
            return "Acceso denegado: solo disponible en perfil DXC."
        if not self.verificar_permiso(usuario, "acceso_dato_sensible"):
            self.guardar_log("seguridad", f"Acceso denegado a dato sensible '{clave}' | Usuario: {usuario if usuario else 'desconocido'}")
            return "Acceso denegado: permiso insuficiente."
        self.guardar_log("seguridad", f"Acceso autorizado a dato sensible '{clave}' | Usuario: {usuario if usuario else 'desconocido'}")
        return self.conocimientos.get(clave, "Dato sensible no encontrado.")
    def actualizar_configuracion_segura(self, clave, valor, usuario=None):
        """Actualiza configuración solo si el perfil y permisos lo permiten. Registra log de seguridad."""
        perfil = self.obtener_perfil()
        if perfil != "DXC":
            self.guardar_log("seguridad", f"Intento de modificar configuración '{clave}' fuera de perfil DXC | Usuario: {usuario if usuario else 'desconocido'}")
            return "Modificación denegada: solo disponible en perfil DXC."
        if not self.verificar_permiso(usuario, "modificar_config_critica"):
            self.guardar_log("seguridad", f"Modificación denegada de configuración '{clave}' | Usuario: {usuario if usuario else 'desconocido'}")
            return "Modificación denegada: permiso insuficiente."
        self.guardar_log("seguridad", f"Configuración '{clave}' modificada por usuario autorizado: {usuario if usuario else 'desconocido'}")
        return self.guardar_configuracion(clave, valor)

    def aprender_banco_sabadell(self, info):
                                    """Aprende información relevante sobre BANCO SABADELL solo si el perfil es DXC."""
                                    perfil = self.obtener_perfil()
                                    if perfil == "DXC":
                                        clave = f"BANCO_SABADELL_{len([k for k in self.conocimientos if k.startswith('BANCO_SABADELL')]) + 1}"
                                        self.conocimientos[clave] = info
                                        self.registrar_metrica("aprendizaje_banco_sabadell", info)
                                        return f"Conocimiento sobre BANCO SABADELL almacenado bajo clave: {clave}"
                                    else:
                                        return "Solo se permite aprender sobre BANCO SABADELL en perfil DXC."

    def aprender_dxc(self, info):
                                    """Aprende información relevante sobre DXC solo si el perfil es DXC."""
                                    perfil = self.obtener_perfil()
                                    if perfil == "DXC":
                                        clave = f"DXC_{len([k for k in self.conocimientos if k.startswith('DXC_')]) + 1}"
                                        self.conocimientos[clave] = info
                                        self.registrar_metrica("aprendizaje_dxc", info)
                                        return f"Conocimiento sobre DXC almacenado bajo clave: {clave}"
                                    else:
                                        return "Solo se permite aprender sobre DXC en perfil DXC."

    # Inicializar perfil al crear instancia
    def inicializar_perfil(self):
                                    # Detectar VPN y adaptar perfil automáticamente
                                    vpn_activa, detalle_vpn = self.detectar_vpn()
                                    if vpn_activa and ("DXC" in detalle_vpn or "Appgate" in detalle_vpn):
                                        self.cambiar_perfil("DXC")
                                        self.guardar_log("seguridad", f"Perfil DXC activado automáticamente por detección de VPN: {detalle_vpn}")
                                    else:
                                        self.detectar_perfil()

    # --- Sistema de permisos y roles ---
    def asignar_permiso(self, usuario, permiso):
                                """Asigna un permiso a un usuario y lo almacena en la base de datos."""
                                try:
                                    import sqlite3
                                    conn = sqlite3.connect(self.db_path)
                                    c = conn.cursor()
                                    c.execute('''CREATE TABLE IF NOT EXISTS permisos (
                                        usuario TEXT,
                                        permiso TEXT,
                                        PRIMARY KEY (usuario, permiso)
                                    )''')
                                    c.execute('REPLACE INTO permisos (usuario, permiso) VALUES (?, ?)', (usuario, permiso))
                                    conn.commit()
                                    conn.close()
                                    return f"Permiso '{permiso}' asignado a {usuario}."
                                except Exception as e:
                                    return f"Error al asignar permiso: {e}"

    def verificar_permiso(self, usuario, permiso):
                                """Verifica si un usuario tiene un permiso específico."""
                                try:
                                    import sqlite3
                                    conn = sqlite3.connect(self.db_path)
                                    c = conn.cursor()
                                    c.execute('SELECT 1 FROM permisos WHERE usuario=? AND permiso=?', (usuario, permiso))
                                    resultado = c.fetchone()
                                    conn.close()
                                    return bool(resultado)
                                except Exception as e:
                                    return f"Error al verificar permiso: {e}"

    def revocar_permiso(self, usuario, permiso):
                                """Revoca un permiso de un usuario en la base de datos."""
                                try:
                                    import sqlite3
                                    conn = sqlite3.connect(self.db_path)
                                    c = conn.cursor()
                                    c.execute('DELETE FROM permisos WHERE usuario=? AND permiso=?', (usuario, permiso))
                                    conn.commit()
                                    conn.close()
                                    return f"Permiso '{permiso}' revocado de {usuario}."
                                except Exception as e:
                                    return f"Error al revocar permiso: {e}"

    def listar_permisos(self, usuario):
                                """Lista todos los permisos asignados a un usuario."""
                                try:
                                    import sqlite3
                                    conn = sqlite3.connect(self.db_path)
                                    c = conn.cursor()
                                    c.execute('SELECT permiso FROM permisos WHERE usuario=?', (usuario,))
                                    permisos = [row[0] for row in c.fetchall()]
                                    conn.close()
                                    return permisos
                                except Exception as e:
                                    return f"Error al listar permisos: {e}"
    # --- Integración general OpenAI/Copilot ---
    def openai_consulta(self, prompt, api_key=None, modelo="gpt-3.5-turbo", max_tokens=150):
        try:
            import requests
            if not api_key:
                return "Se requiere una API key de OpenAI."
            url = "https://api.openai.com/v1/chat/completions"
            headers = {
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            }
            data = {
                "model": modelo,
                "messages": [
                    {"role": "user", "content": prompt}
                ],
                "max_tokens": max_tokens
            }
            r = requests.post(url, headers=headers, json=data, verify=certifi.where())
            if r.status_code == 200:
                resultado = r.json()
                return resultado["choices"][0]["message"]["content"].strip()
            else:
                return f"Error en consulta OpenAI: {r.text}"
        except Exception as e:
            return f"Error en consulta OpenAI: {e}"

    def set_openai_api_key(self, api_key):
                            """Guarda la API key de OpenAI en la configuración avanzada."""
                            return self.guardar_configuracion("openai_api_key", api_key)

    def get_openai_api_key(self):
                            """Obtiene la API key de OpenAI desde la configuración avanzada."""
                            return self.obtener_configuracion("openai_api_key")
    # --- Asistente de código (OpenAI Codex/Copilot) ---
    def asistente_codigo(self, instruccion, lenguaje="python", api_key=None, modelo="gpt-3.5-turbo", max_tokens=150):
        try:
            import requests
            if not api_key:
                return "Se requiere una API key de OpenAI para el asistente de código."
            url = "https://api.openai.com/v1/chat/completions"
            headers = {
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            }
            prompt = f"Eres un asistente experto en {lenguaje}. {instruccion}"
            data = {
                "model": modelo,
                "messages": [
                    {"role": "system", "content": f"Eres un asistente experto en {lenguaje}. Responde solo con el código solicitado, sin explicaciones."},
                    {"role": "user", "content": instruccion}
                ],
                "max_tokens": max_tokens
            }
            r = requests.post(url, headers=headers, json=data, verify=certifi.where())
            if r.status_code == 200:
                resultado = r.json()
                return resultado["choices"][0]["message"]["content"].strip()
            else:
                return f"Error en asistente de código: {r.text}"
        except Exception as e:
            return f"Error en asistente de código: {e}"
    # --- Métodos avanzados de base de datos (CRUD) ---
    def guardar_log(self, tipo, mensaje):
                    """Guarda un log en la base de datos."""
                    try:
                        import sqlite3
                        conn = sqlite3.connect(self.db_path)
                        c = conn.cursor()
                        c.execute('''CREATE TABLE IF NOT EXISTS logs (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            fecha TEXT,
                            tipo TEXT,
                            mensaje TEXT
                        )''')
                        c.execute('INSERT INTO logs (fecha, tipo, mensaje) VALUES (?, ?, ?)',
                                  (datetime.datetime.now().isoformat(), tipo, mensaje))
                        conn.commit()
                        conn.close()
                        return "Log guardado."
                    except Exception as e:
                        return f"Error al guardar log: {e}"

    def obtener_logs(self, tipo=None, limite=10):
                    """Obtiene logs almacenados, filtrando por tipo si se indica."""
                    try:
                        import sqlite3
                        conn = sqlite3.connect(self.db_path)
                        c = conn.cursor()
                        if tipo:
                            c.execute('SELECT fecha, tipo, mensaje FROM logs WHERE tipo=? ORDER BY fecha DESC LIMIT ?', (tipo, limite))
                        else:
                            c.execute('SELECT fecha, tipo, mensaje FROM logs ORDER BY fecha DESC LIMIT ?', (limite,))
                        resultados = c.fetchall()
                        conn.close()
                        return resultados
                    except Exception as e:
                        return f"Error al obtener logs: {e}"

    def guardar_configuracion(self, clave, valor):
                    """Guarda una configuración avanzada en la base de datos."""
                    try:
                        import sqlite3
                        conn = sqlite3.connect(self.db_path)
                        c = conn.cursor()
                        c.execute('''CREATE TABLE IF NOT EXISTS configuraciones (
                            clave TEXT PRIMARY KEY,
                            valor TEXT
                        )''')
                        c.execute('REPLACE INTO configuraciones (clave, valor) VALUES (?, ?)', (clave, str(valor)))
                        conn.commit()
                        conn.close()
                        return "Configuración guardada."
                    except Exception as e:
                        return f"Error al guardar configuración: {e}"

    def obtener_configuracion(self, clave):
                    """Obtiene una configuración avanzada de la base de datos."""
                    try:
                        import sqlite3
                        conn = sqlite3.connect(self.db_path)
                        c = conn.cursor()
                        c.execute('SELECT valor FROM configuraciones WHERE clave=?', (clave,))
                        resultado = c.fetchone()
                        conn.close()
                        if resultado:
                            return resultado[0]
                        return None
                    except Exception as e:
                        return f"Error al obtener configuración: {e}"
    # --- Resúmenes automáticos ---
    def resumir_texto(self, texto, api_key=None, modelo="gpt-3.5-turbo", max_tokens=150):
        try:
            import requests
            if not api_key:
                return "Se requiere una API key de OpenAI para resumir textos."
            url = "https://api.openai.com/v1/chat/completions"
            headers = {
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            }
            data = {
                "model": modelo,
                "messages": [
                    {"role": "system", "content": "Resume el siguiente texto de forma concisa en español."},
                    {"role": "user", "content": texto}
                ],
                "max_tokens": max_tokens
            }
            r = requests.post(url, headers=headers, json=data, verify=certifi.where())
            if r.status_code == 200:
                resultado = r.json()
                return resultado["choices"][0]["message"]["content"].strip()
            else:
                return f"Error al resumir texto: {r.text}"
        except Exception as e:
            return f"Error al resumir texto: {e}"
    # --- Generación de imágenes ---
    def generar_imagen(self, prompt, api_key=None, modelo="dalle", tamano="512x512"):
        try:
            import requests
            if modelo == "dalle":
                if not api_key:
                    return "Se requiere una API key de OpenAI para generación de imágenes."
                url = "https://api.openai.com/v1/images/generations"
                headers = {
                    "Authorization": f"Bearer {api_key}",
                    "Content-Type": "application/json"
                }
                data = {
                    "prompt": prompt,
                    "n": 1,
                    "size": tamano
                }
                r = requests.post(url, headers=headers, json=data, verify=certifi.where())
                if r.status_code == 200:
                    resultado = r.json()
                    return resultado["data"][0]["url"]
                else:
                    return f"Error al generar imagen: {r.text}"
            # Aquí se pueden agregar otros modelos (Stable Diffusion, etc.)
            return f"Modelo de generación '{modelo}' no implementado aún."
        except Exception as e:
            return f"Error al generar imagen: {e}"
    def __init__(self, usuario="Tony", historial_path="historial.json"):
        self.usuario = usuario
        self.modo = "Brains & Bytes"
        self.historial_path = Path(historial_path)
        self.historial = self.cargar_historial()
        self.metricas = []  # Inicializar como lista para registrar métricas
        self.sugerencias = []
        # Cargar recursos externos
        base = Path(__file__).parent
        self.diccionario = cargar_json(base / "diccionario.json")
        self.modos = cargar_json(base / "modos_trabajo.json")
        self.patrones = cargar_json(base / "patrones.json")
        self.conocimientos = {}  # Aprendizaje dinámico
        # Inicializar ruta de base de datos SQLite
        self.db_path = str(base / "jarvis.db")
    # --- Integración con Wikipedia ---
    def buscar_wikipedia(self, consulta, lang="es"):
        if not wikipedia:
            return "La librería 'wikipedia' no está instalada. Ejecuta 'pip install wikipedia' para habilitar esta función."
        wikipedia.set_lang(lang)
        url = f"https://{lang}.wikipedia.org"
        permitido, msg = self.comprobar_acceso_url(url)
        if not permitido:
            return msg
        try:
            resumen = wikipedia.summary(consulta, sentences=2)
            return resumen
        except Exception as e:
            return f"No se pudo obtener información de Wikipedia: {e}"



    # --- Búsqueda web (DuckDuckGo Instant Answer API) ---
    def buscar_web(self, consulta):
        try:
            url = f"https://api.duckduckgo.com/?q={consulta}&format=json&no_redirect=1&no_html=1"
            permitido, msg = self.comprobar_acceso_url(url)
            if not permitido:
                return msg
            r = requests.get(url, verify=certifi.where())
            data = r.json()
            if data.get("AbstractText"):
                return data["AbstractText"]
            elif data.get("RelatedTopics"):
                return data["RelatedTopics"][0].get("Text", "Sin resultados relevantes.")
            else:
                return "Sin resultados relevantes."
        except Exception as e:
            return f"Error en búsqueda web: {e}"

    # --- GitHub (búsqueda de repositorios públicos) ---
    def buscar_github(self, consulta):
        try:
            url = f"https://api.github.com/search/repositories?q={consulta}"
            permitido, msg = self.comprobar_acceso_url(url)
            if not permitido:
                return msg
            r = requests.get(url, verify=certifi.where())
            data = r.json()
            if data.get("items"):
                repo = data["items"][0]
                return f"{repo['full_name']}: {repo['html_url']}\nDescripción: {repo.get('description', 'Sin descripción')}"
            else:
                return "No se encontraron repositorios."
        except Exception as e:
            return f"Error al buscar en GitHub: {e}"

    # --- Stack Overflow (Stack Exchange API) ---
    def buscar_stackoverflow(self, consulta):
        try:
            url = f"https://api.stackexchange.com/2.3/search/advanced?order=desc&sort=relevance&q={consulta}&site=stackoverflow"
            permitido, msg = self.comprobar_acceso_url(url)
            if not permitido:
                return msg
            r = requests.get(url, verify=certifi.where())
            data = r.json()
            if data.get("items"):
                pregunta = data["items"][0]
                return f"{pregunta['title']}\n{pregunta['link']}"
            else:
                return "No se encontraron resultados en Stack Overflow."
        except Exception as e:
            return f"Error al buscar en Stack Overflow: {e}"

    # --- Chistes y datos curiosos (Official Joke API) ---
    def obtener_chiste(self):
        try:
            url = "https://official-joke-api.appspot.com/random_joke"
            permitido, msg = self.comprobar_acceso_url(url)
            if not permitido:
                return msg
            r = requests.get(url, verify=certifi.where())
            data = r.json()
            return f"{data['setup']} {data['punchline']}"
        except Exception as e:
            return f"Error al obtener chiste: {e}"

    def obtener_dato_curioso(self):
        try:
            url = "https://uselessfacts.jsph.pl/random.json?language=es"
            permitido, msg = self.comprobar_acceso_url(url)
            if not permitido:
                return msg
            r = requests.get(url, verify=certifi.where())
            data = r.json()
            return data.get("text", "No se pudo obtener un dato curioso.")
        except Exception as e:
            return f"Error al obtener dato curioso: {e}"

    # --- Base para bots/servicios externos (Discord/Telegram) ---
    def enviar_mensaje_discord(self, webhook_url, mensaje):
        try:
            data = {"content": mensaje}
            r = requests.post(webhook_url, json=data, verify=certifi.where())
            if r.status_code == 204:
                return "Mensaje enviado a Discord."
            else:
                return f"Error al enviar mensaje a Discord: {r.text}"
        except Exception as e:
            return f"Error al conectar con Discord: {e}"

    def enviar_mensaje_telegram(self, bot_token, chat_id, mensaje):
        try:
            url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
            data = {"chat_id": chat_id, "text": mensaje}
            r = requests.post(url, data=data, verify=certifi.where())
            if r.status_code == 200:
                return "Mensaje enviado a Telegram."
            else:
                return f"Error al enviar mensaje a Telegram: {r.text}"
        except Exception as e:
            return f"Error al conectar con Telegram: {e}"

    # --- Aprendizaje dinámico ---
    def aprender(self, clave, valor):
        self.conocimientos[clave] = valor
        return f"Nuevo conocimiento aprendido: {clave} => {valor}"

    def consultar_conocimiento(self, clave):
        return self.conocimientos.get(clave, "No tengo información sobre eso todavía.")

    # --- Estructura modular para futuras bibliotecas externas ---
    def consultar_externa(self, fuente, consulta):
            if fuente == "wikipedia":
                return self.buscar_wikipedia(consulta)
            if fuente == "traducir":
                return self.traducir(consulta)
            if fuente == "web":
                return self.buscar_web(consulta)
            if fuente == "github":
                return self.buscar_github(consulta)
            if fuente == "stackoverflow":
                return self.buscar_stackoverflow(consulta)
            if fuente == "chiste":
                return self.obtener_chiste()
            if fuente == "dato_curioso":
                return self.obtener_dato_curioso()
            return f"Fuente externa '{fuente}' no implementada aún."

    def cargar_historial(self):
        if self.historial_path.exists():
            with open(self.historial_path, "r", encoding="utf-8") as f:
                return json.load(f)
        return []

    def guardar_historial(self):
        with open(self.historial_path, "w", encoding="utf-8") as f:
            json.dump(self.historial, f, ensure_ascii=False, indent=2)

    def registrar_interaccion(self, mensaje, respuesta):
        entrada = {
            "fecha": datetime.datetime.now().isoformat(),
            "modo": self.modo,
            "mensaje": mensaje,
            "respuesta": respuesta
        }
        self.historial.append(entrada)
        self.guardar_historial()

    def cambiar_modo(self, nuevo_modo):
        self.modo = nuevo_modo
        return f"Modo cambiado a {nuevo_modo}"

    def sugerir(self, sugerencia):
        self.sugerencias.append(sugerencia)
        return f"Sugerencia registrada: {sugerencia}"

    def mostrar_historial(self, n=5):
        return self.historial[-n:]

    def mostrar_sugerencias(self):
        return self.sugerencias

    def automatizar(self, tarea):
        # Aquí puedes integrar scripts, APIs, etc.
        return f"Automatizando: {tarea} (funcionalidad en desarrollo)"

    def saludo(self, nombre=None, pc=None):
        # Saludo breve
        mensaje1 = "Buenas, Señor Stark"
        mensaje2 = "DXC - BANCO SABADELL"
        ancho = 60
        print("\n" + mensaje1.center(ancho))
        print(mensaje2.center(ancho) + "\n")
        # Mensaje largo del terminal (información de entorno y DXC)
        usuario = getpass.getuser()
        sistema = platform.system()
        version = platform.version()
        maquina = platform.node()
        print("--- INFORMACION DEL PC ---")
        print(f"Usuario: {usuario}")
        print(f"Sistema operativo: {sistema}")
        print(f"Versión del sistema: {version}")
        print(f"Nombre del equipo: {maquina}")
        print("\n+--------------------------------------------------+")
        print("|           DXC Technology Company                |")
        print("+--------------------------------------------------+")
        print("| Sede : Ashburn, Virginia, Estados Unidos        |")
        print("| CEO  : Raul J. Fernandez                       |")
        print("| Desde: 2017 (fusion de CSC y HPE Services)      |")
        print("+--------------------------------------------------+")

    def info_pc(self):
        usuario = getpass.getuser()
        sistema = platform.system()
        version = platform.version()
        maquina = platform.node()
        print(f"Usuario: {usuario}")
        print(f"Sistema operativo: {sistema}")
        print(f"Versión del sistema: {version}")
        print(f"Nombre del equipo: {maquina}")

    def comprobaciones(self):
        print("[Comprobaciones globales pendientes de implementar]")

    def guardar_info_local(self):
        base = Path(__file__).parent
        perfil = self.obtener_perfil()
        config_path = base / f"config_{perfil.lower()}.json"
        usuario = getpass.getuser()
        sistema = platform.system()
        version = platform.version()
        maquina = platform.node()
        datos = {
            "usuario": usuario,
            "sistema": sistema,
            "version": version,
            "maquina": maquina
        }
        if not config_path.exists():
            with open(config_path, "w", encoding="utf-8") as f:
                json.dump(datos, f, ensure_ascii=False, indent=2)
            print(f"[J.A.R.V.I.S] Información local guardada en {config_path}")
        else:
            print(f"[J.A.R.V.I.S] Configuración local ya existe: {config_path}")

    def mostrar_info_local(self):
        base = Path(__file__).parent
        perfil = self.obtener_perfil()
        config_path = base / f"config_{perfil.lower()}.json"
        if config_path.exists():
            with open(config_path, "r", encoding="utf-8") as f:
                datos = json.load(f)
            print("[J.A.R.V.I.S] Datos locales del equipo:")
            for k, v in datos.items():
                print(f"  {k}: {v}")
        else:
            print(f"[J.A.R.V.I.S] No hay datos locales guardados para {perfil}.")

    def iniciar_entorno(self):
        print("[J.A.R.V.I.S] Inicializando entorno...")
        self.saludo()
        self.info_pc()
        self.comprobaciones()
        self.guardar_info_local()
        self.mostrar_info_local()
        print("\n" + "="*60)
        print("   J.A.R.V.I.S INICIADO CORRECTAMENTE - ENTORNO LISTO   ".center(60))
        print("="*60 + "\n")

    def registrar_metrica(self, tipo, valor):
        """Registra una métrica de uso/interacción en la base de datos y en memoria."""
        try:
            if not hasattr(self, 'metricas') or not isinstance(self.metricas, list):
                self.metricas = []
            metrica = {
                "fecha": datetime.datetime.now().isoformat(),
                "tipo": tipo,
                "valor": valor
            }
            self.metricas.append(metrica)
            # Guardar en base de datos SQLite
            import sqlite3
            conn = sqlite3.connect(self.db_path)
            c = conn.cursor()
            c.execute('''CREATE TABLE IF NOT EXISTS metricas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                fecha TEXT,
                tipo TEXT,
                valor TEXT
            )''')
            c.execute('INSERT INTO metricas (fecha, tipo, valor) VALUES (?, ?, ?)',
                      (metrica["fecha"], tipo, str(valor)))
            conn.commit()
            conn.close()
            print(f"[J.A.R.V.I.S] Métrica registrada: {tipo} -> {valor}")
            return "Métrica registrada."
        except Exception as e:
            print(f"[J.A.R.V.I.S] Error al registrar métrica: {e}")
            return f"Error al registrar métrica: {e}"


    def consultar_diccionario(self, termino):
        """Consulta un término en el diccionario cargado y devuelve su definición o un mensaje si no existe."""
        if not hasattr(self, 'diccionario') or self.diccionario is None:
            return "El diccionario no está cargado."
        definicion = self.diccionario.get(termino.lower())
        if definicion:
            return f"{termino}: {definicion}"
        else:
            return f"El término '{termino}' no se encuentra en el diccionario."



# --- Bloque principal de ejecución ---
if __name__ == "__main__":
    # Mostrar mensaje largo de bienvenida e info DXC por consola
    print("\n--- INFORMACION DEL PC ---")
    import getpass
    import platform
    usuario = getpass.getuser()
    sistema = platform.system()
    version = platform.version()
    maquina = platform.node()
    print(f"Usuario: {usuario}")
    print(f"Sistema operativo: {sistema}")
    print(f"Version del sistema: {version}")
    print(f"Nombre del equipo: {maquina}")
    print("\n+--------------------------------------------------+")
    print("|           DXC Technology Company                |")
    print("+--------------------------------------------------+")
    print("| Sede : Ashburn, Virginia, Estados Unidos        |")
    print("| CEO  : Raul J. Fernandez                       |")
    print("| Desde: 2017 (fusion de CSC y HPE Services)      |")
    print("+--------------------------------------------------+")

    # Comprobaciones técnicas
    import subprocess
    import sys
    import os
    import socket
    resultados = []
    version_requerida = (3, 8)
    version_actual = sys.version_info[:3]
    if version_actual >= version_requerida:
        resultados.append("✔ Python versión correcta: {}.{}.{}".format(*version_actual))
    else:
        resultados.append("✖ Python versión insuficiente: {}.{}.{} (se requiere >= 3.8)".format(*version_actual))
    if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        resultados.append("✔ Entorno virtual (.venv) activado")
    elif 'VIRTUAL_ENV' in os.environ:
        resultados.append("✔ Entorno virtual (.venv) activado")
    else:
        resultados.append("✖ Entorno virtual (.venv) NO activado")
    try:
        result = subprocess.run([
            'powershell',
            '-Command',
            'Get-ExecutionPolicy -Scope CurrentUser'
        ], capture_output=True, text=True, timeout=5)
        policy = result.stdout.strip()
        if policy.lower() in ["remotesigned", "unrestricted", "bypass"]:
            resultados.append("✔ PowerShell permite ejecución de scripts: {}".format(policy))
        else:
            resultados.append("✖ PowerShell NO permite scripts: {}".format(policy))
            resultados.append("  Ejecuta como admin: Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned")
    except Exception as e:
        resultados.append(f"✖ No se pudo comprobar política PowerShell: {e}")
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        resultados.append("✔ Conexión a Internet OK")
    except Exception:
        resultados.append("✖ Sin conexión a Internet")
    vpn_ok = False
    try:
        socket.gethostbyname("intranet.dxc.com")
        vpn_ok = True
    except Exception:
        vpn_ok = False
    if vpn_ok:
        resultados.append("✔ VPN corporativa activa (intranet accesible)")
    else:
        resultados.append("✖ VPN corporativa NO detectada (intranet no accesible)")
    print("\nComprobaciones de entorno:\n")
    for r in resultados:
        print(r)

    jarvis = Jarvis()
    jarvis.inicializar_perfil()
    jarvis.iniciar_entorno()
    print(f"Perfil activo: {jarvis.obtener_perfil()}")
    # --- Detección de VPN corporativa ---
    vpn_activa, detalle_vpn = jarvis.detectar_vpn()
    print(f"VPN corporativa activa: {vpn_activa} | Detalle: {detalle_vpn}")
    if vpn_activa and ("DXC" in detalle_vpn or "Appgate" in detalle_vpn):
        print("sí")
    else:
        print("no")
    # --- Ejemplo de uso DXC/BANCO SABADELL ---
    print("\n--- [BANCO SABADELL DXC] ---")
    print(jarvis.info_banco_sabadell())
    print(jarvis.aprender_banco_sabadell("Procedimiento seguro de onboarding digital para clientes empresariales."))
    print(jarvis.consultar_conocimiento_banco_sabadell())
    print(jarvis.registrar_interaccion_banco_sabadell(
        "¿Cómo se realiza el onboarding digital?",
        "Se sigue el procedimiento seguro de onboarding digital para clientes empresariales."
    ))
    print(jarvis.saludo())
    print(jarvis.consultar_diccionario("duro"))
    print(jarvis.ejemplo_patron("broma"))
    jarvis.registrar_interaccion("¿Qué vamos a hacer esta noche, J.A.R.V.I.S.?", jarvis.ejemplo_patron("broma"))
    print(jarvis.mostrar_historial())
    print(jarvis.cambiar_modo("La Jumpa"))
    print(jarvis.saludo())
    print(jarvis.ejemplo_patron("broma"))
    print(jarvis.sugerir("Integrar API de chistes"))
    print(jarvis.mostrar_sugerencias())
    print(jarvis.automatizar("Enviar informe semanal"))
    # Ejemplos de integraciones externas
    print("\nConsulta Wikipedia sobre 'Iron Man':")
    print(jarvis.buscar_wikipedia("Iron Man"))

    print("\nBúsqueda web sobre 'Python programming':")
    print(jarvis.buscar_web("Python programming"))
    print("\nBuscar en GitHub 'copilot':")
    print(jarvis.buscar_github("copilot"))
    print("\nBuscar en Stack Overflow 'python list comprehension':")
    print(jarvis.buscar_stackoverflow("python list comprehension"))
    print("\nObtener chiste:")
    print(jarvis.obtener_chiste())
    print("\nObtener dato curioso:")
    print(jarvis.obtener_dato_curioso())
    # Ejemplo de integración con Wikipedia
    print("\nConsulta Wikipedia sobre 'Iron Man':")
    print(jarvis.buscar_wikipedia("Iron Man"))
    # Ejemplo de aprendizaje dinámico
    print(jarvis.aprender("color favorito de Tony", "rojo y dorado"))
    print(jarvis.consultar_conocimiento("color favorito de Tony"))
    # Ejemplo de estructura modular para futuras fuentes
    print(jarvis.consultar_externa("wikipedia", "J.A.R.V.I.S."))
