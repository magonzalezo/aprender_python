"""
Ejercicio 3: Escribir un programa que muestre los cuadrados de los primeros 60 numeros naturales.
    -Resolverlo con FOR
    -Resolverlo con WHILE
"""
#WHILE

print('############ WHILE ############')

numero = 0

while (numero <=60):
    print(f"El cuadrado de {numero} es {numero * numero}")
    numero += 1

#FOR

print('############ FOR ############')

for i in range (61):
    print(f"El cuadrado de {i} es {i * i}")