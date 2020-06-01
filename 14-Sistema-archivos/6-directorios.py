import os, shutil
from io import open

nombre_directorio = "carpeta"
ruta = os.path.dirname(__file__) + "/" + nombre_directorio

# Crear carpeta
if not os.path.isdir(ruta):
    os.mkdir(ruta)
    #Crear archivos para alimentar la carpeta
    archivo_1 = open(ruta + "/archivo_1.txt", "a+")
    archivo_1.close()
    archivo_2 = open(ruta + "/archivo_2.txt", "a+")
    archivo_2.close()
    archivo_3 = open(ruta + "/archivo_3.txt", "a+")
    archivo_3.close()
else:
    print("Ya existe el directorio")

# Copiar carpeta
ruta_copia = os.path.dirname(__file__) + "/carpeta_copia"
shutil.copytree(ruta, ruta_copia)

# Eliminar si el directorio esta vacio
#os.rmdir(ruta_copia)

# Eliminar si el directorio tiene archivos
shutil.rmtree(ruta_copia)

# Listar contenido en directorio
print(f"\nContenido en el directorio '{nombre_directorio}'")
contenido = os.listdir(ruta)

for elemento in contenido:
    print("- "+elemento)