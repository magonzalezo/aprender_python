import os
import pathlib

# Para probar, ejecutar el script 1-leer-y-escribir-en-archivos.py
ruta = str(pathlib.Path(__file__).parent.absolute()) + "/archivo_texto.txt"
os.remove(ruta)