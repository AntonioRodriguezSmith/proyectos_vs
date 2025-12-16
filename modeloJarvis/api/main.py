"""
API REST para exponer el modelo J.A.R.V.I.S.
"""
from fastapi import FastAPI, Request
from src.jarvis_model import JarvisModel

app = FastAPI()
modelo = JarvisModel()

@app.post("/inferir")
async def inferir(request: Request):
    datos = await request.json()
    entrada = datos.get("entrada", "")
    respuesta = modelo.inferir(entrada)
    return {"respuesta": respuesta}

@app.get("/")
async def root():
    return {"mensaje": "API de J.A.R.V.I.S. operativa"}
