"""
 Recomendacion 1: (Programacion estructurada) A pesar de que Python permite 
                  ejecutar funciones colocandolas donde queramos, es recomendable
                  colocarlas al inicio.
"""
print("####### Recomendacion 1 #######")

def holaMundo():
    print("Hola mundo")

def bienvenida():
    print("Bienvenido a este espacio!!")

holaMundo()
bienvenida()

"""
 Recomendacion 2: Tratar de que las funciones generen un retorno o devuelva un 
                  dato (Si corresponde).
"""
print("\n####### Recomendacion 2 #######")

def encabezado():
    return "--Encabezado--"

def detalle():
    return "--Detalle--"

print(encabezado())
print(detalle())

"""
 Recomendacion 3: Si la funcion usa variables globales, que estas variables esten
                  definidas antes de invocar la funcion
"""
print("\n####### Recomendacion 3 #######")

def concatenarNombreCompleto():
    return nombre + " " + apellido

nombre = "Miguel"
apellido = "Gonzalez"

print(concatenarNombreCompleto())

"""
 Recomendacion 4: Como buena practica es mejor pasar las variables por parametro
"""
print("\n####### Recomendacion 4 #######")
def obtenerNombreCompleto(p_nombre, p_apellido):
    return p_nombre + " " + p_apellido

nombre = "Miguel"
apellido = "Gonzalez"

print(obtenerNombreCompleto(nombre, apellido))