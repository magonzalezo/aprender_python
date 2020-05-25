"""
Funciones que ya trae consigo Python
"""

nombre = "Miguel Gonzalez"

##### Generales

# Imprimir por pantalla
print(nombre)

# Indicar tipo de variable 
print("")
print(type(nombre))

# Detectar tipo
print("")
comprobar = isinstance(nombre, str)
if comprobar:
    print("La variable es un String")
else:
    print("La variable no es un String")

# Limpiar espacios
print("")
frase = "     cadena que contiene espacios a los lados        "
print(frase)
print(frase.strip())

# Borrar variables
print("")
variable = "Texto con lo que sea"
print(variable)
del variable
#print(variable)

# Comprobar variable vacia
print("")
texto = " texto"

if len(texto) <= 0:
    print("La variable esta vacia")
else:
    print("La variable tiene contenido:", len(texto))

# Encontar caracteres
print("")
frase = "La belleza esta en el ojo del observador"
print(frase.find("esta"))

# Reemplazar palabras en un String
print("")
frase_original = "Los dioses estan locos"
nueva_frase = frase_original.replace("locos", "gordos")
print(frase_original)
print(nueva_frase)

# Mayusculas y Minusculas
print("")
print("MaYusCuLa".upper())
print("MiNuScUlA".lower())