"""
Ejercicio 8: ¿Cuanto es el X porciento de X numero?
             Ejemplo 30% de 120
"""

numero = int(input("Introducir el numero: "))
porcentaje = int(input(f"¿Que porcentaje desea sacar de {numero}?: "))

operacion = (numero * (porcentaje / 100))

print(f"El {porcentaje}% de {numero} es {operacion}")