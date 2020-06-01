from io import open
import pathlib
import shutil

ruta_original = str(pathlib.Path(__file__).parent.absolute()) + "/archivo_texto.txt"
ruta_nueva = str(pathlib.Path(__file__).parent.absolute()) + "/archivo_texto_copia.txt"
shutil.copyfile(ruta_original, ruta_nueva)