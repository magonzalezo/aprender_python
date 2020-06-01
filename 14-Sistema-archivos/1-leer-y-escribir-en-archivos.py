from io import open
import pathlib
import os

# Obtener ruta de trabajo

# Opcion 1: desde directorio de trabajo
#ruta = os.getcwd()

# Opcion 2: desde directorio de trabajo
#ruta = str(pathlib.Path().absolute()) + "/archivo_texto.txt" 

# Opcion 3: desde donse se esta ejecutando el script
ruta = str(pathlib.Path(__file__).parent.absolute()) + "/archivo_texto.txt"

#print(ruta)

"""
Apertura y escritura en archivos
"""

# Abrir archivo
archivo = open(ruta, "a+")

# Escribir

# Una linea
archivo.write("Texto escrito en una sola linea...\n")

# Ejemplo varias lineas
for i in range(10):
     archivo.write(f"Escribiendo linea {i} del ciclo...\n")

# Cerrar
archivo.close()

"""
Apertura y lectura en archivos
"""
# Abrir archivo en modo lectura
archivo_lectura = open(ruta, "r")

# Leer contenido total
#contenido = archivo_lectura.read()
# Mostrar contenido total
#print(contenido)

# Leer contenido total a lista
lista = archivo_lectura.readlines()
archivo_lectura.close()
# Mostrar texto lista
print(lista)
# Mostrar texto linea a linea
for linea in lista:
    print(linea)