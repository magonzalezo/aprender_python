from io import open
import pathlib
import shutil

# Para probar, ejecutar el script 1-leer-y-escribir-en-archivos.py
ruta_original = str(pathlib.Path(__file__).parent.absolute()) + "/archivo_texto.txt"
ruta_nueva = str(pathlib.Path(__file__).parent.absolute()) + "/archivo_texto_nuevo.txt"
shutil.move(ruta_original, ruta_nueva)