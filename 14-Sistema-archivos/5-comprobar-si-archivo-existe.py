import os.path

# Para probarlo, ejecutar primero el script 1-leer-y-escribir-en-archivos.py

# Ruta absoluta
ruta_archivo = os.path.dirname(__file__) + "/archivo_texto.txt"

if os.path.isfile(ruta_archivo):
    print("El archivo existe")
else:
    print("El archivo no existe")
