"""
Locales: Declaradas dentro de una funcion y solo se pueden usar 
         dentro de la funcion y no por fuera

Globales: Declaradas fuera de la funcion y pueden ser usadas tanto
          dentro como fuera de la funcion
"""

# Ejemplo 1: Declarar variable global y local e imprimirla
print("######### EJEMPLO 1 #########")

# Variable global
cadena = "Texto global"

def holaMundo():
    # Variable local
    cadena = "Hola mundo"
    print(cadena)

def imprimirGlobal():
    # Usa variable global
    print(cadena)

holaMundo()
imprimirGlobal()

# Ejemplo 2: Convertir una variable local en global
print("\n######### EJEMPLO 2 #########")

variableGlobal = "Soy global"

def accionLocal():
    
    print(variableGlobal)

    variableLocal = "Soy local"
    print(variableLocal)

    global generica 
    generica = "Estoy en todo el codigo"
    print("Dentro: " + generica)

accionLocal()
print("Fuera: " + generica)