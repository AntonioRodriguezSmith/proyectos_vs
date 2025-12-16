# Ejemplo de integración

Para consumir el modelo J.A.R.V.I.S. vía API REST:

```python
import requests

entrada = {"entrada": "¿Cuál es tu función?"}
resp = requests.post("http://localhost:8000/inferir", json=entrada)
print(resp.json())
```
