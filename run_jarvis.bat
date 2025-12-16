@echo off
REM Lanzador universal de J.A.R.V.I.S. desde cualquier carpeta principal del monorepo
cd /d %~dp0\modeloJarvis
C:\Users\arodriguezsm\AppData\Local\Python\pythoncore-3.14-64\python.exe -m uvicorn api.main:app --reload
