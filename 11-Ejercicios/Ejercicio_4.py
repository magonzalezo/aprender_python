"""
Ejercicio 4: Crear un Script que tenga 4 variables: Lista, String, Entero y Booleano.
             Que imprima un mensaje segun el tipo de dato de cada variable.
             - Usar funciones.
"""
def traducirTipo(tipo):
    result = None

    if tipo == list:
        result = "Lista"
    elif tipo == str:
        result = "Cadena de texto"
    elif tipo == int:
        result = "Entero"
    elif tipo == bool:
        result = "Booleano"    
    
    return result

def comprobarTipo(dato, tipo):
    
    comprobar = isinstance(dato, tipo)
    resultado = "";

    if comprobar:
        #resultado = f"Este dato es del tipo {type(dato)}"
        resultado = f"Este dato es del tipo {traducirTipo(type(dato))}"
    else:
        resultado = "El tipo de dato no es correcto"

    return resultado 

lista_comun = []
cadena = "Hola"
numero = 0
flag = True

print(comprobarTipo(lista_comun, list))
print(comprobarTipo(cadena, str))
print(comprobarTipo(numero, int))
print(comprobarTipo(flag, bool))