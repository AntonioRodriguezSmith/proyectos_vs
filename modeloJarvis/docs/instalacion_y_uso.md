# Instalación y uso de modeloJarvis

## 1. Instalación de dependencias

Desde la raíz del proyecto, ejecuta:

```bash
pip install -r requirements.txt
```

## 2. Ejecución de la API REST

Lanza el servidor FastAPI con Uvicorn:

```bash
uvicorn api.main:app --reload
```

La API estará disponible en http://localhost:8000

## 3. Prueba de inferencia

Puedes probar la inferencia con un cliente HTTP o usando el ejemplo de docs/integracion.md:

```python
import requests
entrada = {"entrada": "¿Cuál es tu función?"}
resp = requests.post("http://localhost:8000/inferir", json=entrada)
print(resp.json())
```

## 4. Ejecutar tests

Para lanzar las pruebas unitarias:

```bash
pytest tests/
```

## 5. Estructura del proyecto

- src/: Lógica del modelo J.A.R.V.I.S.
- api/: API REST para exponer el modelo
- data/: Datos de entrenamiento y pruebas
- tests/: Pruebas unitarias y de integración
- docs/: Documentación y ejemplos

---

Para cualquier integración o ampliación, consulta los archivos en docs/ y el README principal.
