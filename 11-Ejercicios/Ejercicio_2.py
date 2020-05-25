"""
Ejercicio 2: Escribir un programa que añada valores a una lista mientras que 
             su longitud sea menor a 20 y luego mostrar la lista.
             Usar While y For.
"""
# FOR
print(" -------- Ejercicio con for --------")
lista_numeros = []

for elemento in range(0,20):
    lista_numeros.append(elemento)
    print(f"Mostrando elemento agregado: {lista_numeros[elemento]}")
print(lista_numeros)

# WHILE
print("\n -------- Ejercicio con while --------")
lista_numeros = []
contador = 0

while contador < 20:
    lista_numeros.append(contador)
    print(f"Mostrando elemento agregado: {lista_numeros[contador]}")
    contador += 1
print(lista_numeros)