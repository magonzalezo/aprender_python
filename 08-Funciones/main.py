"""
FUNCIONES: Conjunto de instrucciones agrupadas bajo un nombre concreto 
           que pueden reutilizarse invocandola tabtas veces como sea
           necesario.

def nombreDeLaFuncion( parametros ):
    # Bloque de codigo / Conjunto de instrucciones

# Invocacion(es)
nombreDeLafuncion( parametros )
nombreDeLafuncion( parametros )
nombreDeLafuncion( parametros )
"""

# Ejemplo 1
print("############ Ejemplo 1 ############")

# Definir funcion
def muestraNombres():
    print("Miguel")
    print("Pedro")
    print("Mariana")
    print("Camila")
    print("")

# Invocar funcion
muestraNombres()
muestraNombres()
muestraNombres()

# Ejemplo 2
print("\n############ Ejemplo 2 ############")

def mostrarNombre(nombre, edad):
    print(f"Tu nombre es {nombre}")

    if edad > 18:
        print("Y eres mayor de edad")

nombre = input("Ingresar tu nombre: ")
edad = int(input("Ingresar tu edad: "))
mostrarNombre(nombre, edad)

# Ejemplo 3
print("\n############ Ejemplo 3 ############")

def tabla(numero):
    print(f"La tabla de multiplicar del número: {numero}")

    for factor in range(1, 11):
        operacion = numero * factor
        print(f"{numero} X {factor} = {operacion}")
    else:
        print("\n")

tabla(5)
tabla(9)
tabla(2)

# Ejemplo 3.1
print("\n############ Ejemplo 3.1 ############")
for numero in range(1, 11):
    tabla(numero)

# Ejemplo 4
print("\n############ Ejemplo 4 ############")

# Parametros opcionales

def getEmpleado(nombre, dni = None):
    print("EMPLEADO")
    print(f"Nombre: {nombre}")

    if dni != None:
        print(f"DNI: {dni}")

getEmpleado("Miguel Gonzalez", 12345678)
getEmpleado("Pepito Perez")

# Ejemplo 5
print("\n############ Ejemplo 5 ############")

#Return o devolver datos
def saludame(nombre):
    saludo = f"Hola, saludos {nombre}"
    return saludo

print(saludame("Miguel Gonzalez"))

# Ejemplo 6
print("\n############ Ejemplo 6 ############")

def calculadora(numero_1, numero_2, basicas = False):
    
    suma = numero_1 + numero_2
    resta = numero_1 - numero_2
    multiplicacion = numero_1 * numero_2
    division = numero_1 / numero_2

    cadena = ""

    if basicas == True:
        cadena += "Suma: " + str(suma)
        cadena += "\n"
        cadena += "Resta: " + str(resta)
        cadena += "\n"
    else:
        cadena += "Multiplicacion: " + str(multiplicacion)
        cadena += "\n"
        cadena += "Division: " + str(division)
        cadena += "\n"

    return cadena

print(calculadora(2,5))
print(calculadora(9,5,True))

# Ejemplo 7
print("\n############ Ejemplo 7 ############")

def getNombre(nombre):
    texto = f"El nombre es: {nombre}"
    return texto

def getApellidos(apellidos):
    texto = f"Los apellidos son: {apellidos}"
    return texto

def devuelveTodo(nombre, apellidos):
    texto = getNombre(nombre) + "\n" + getApellidos(apellidos)
    return texto

print(devuelveTodo("Miguel", "Gonzalez"))

# Ejemplo 8
print("\n############ Ejemplo 8 ############")

# Funcion Lamnda
dime_el_year = lamnda year: f"El año es {year}"
print(dime_el_year(2020))