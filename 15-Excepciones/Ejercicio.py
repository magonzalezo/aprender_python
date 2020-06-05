"""
Ejercicio 1: Hacer un programa que tenga una lista de 8 numeros enteros. Y que haga:
             -Recorrer la lista y mostrarla.
             -Hacer una funcion que recorra listas de strings y devuelva un string
             -Ordenarla y mostrarla
             -Mostrar su longitud.
             -Buscar algun elemento (Que el usuario pida por teclado). 

"""
# Definimos la lista
lista_numeros = [1, 987, 69, 5, 3, 77, 14, 44]

# Punto 1
print('------- Punto 1: Recorrer y mostrar -------')
for numero in lista_numeros:
    print(numero)

# Punto 2
print('\n------- Punto 2: Recorrer y mostrar (Con funcion) -------')
def recorrer_lista(lista):
    cadena_numeros = ""
    for numero in lista:
        cadena_numeros += str(numero) + ", "
    cadena_numeros = cadena_numeros[0:len(cadena_numeros)-2]
    return cadena_numeros

print(recorrer_lista(lista_numeros))

# Punto 3
print('\n------- Punto 3: Ordenar y mostrar -------')
lista_numeros.sort()
print(lista_numeros)

# Punto 4
print('\n------- Punto 4: Mostrar longitud -------')
print(f"La longitud de la lista es de {len(lista_numeros)} elementos")

# Punto 5
print('\n------- Punto 4: Buscar elemento indicado por usuario -------')
try:
    numero_a_buscar = int(input("Ingrese numero a buscar: "))

    comprobar = isinstance(numero_a_buscar, int)

    while not comprobar or numero_a_buscar <= 0:
        numero_a_buscar = int(input("Ingrese numero a buscar: "))
    else:
        print(f"Has introducido el {numero_a_buscar}")

    busqueda = lista_numeros.index(numero_a_buscar)
    print(f"El número {numero_a_buscar} se encuentra en la lista en el indice {busqueda}")
except:
    print(f"Ha ocurrido un error!!")