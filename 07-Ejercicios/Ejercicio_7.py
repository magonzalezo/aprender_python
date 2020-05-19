"""
Ejercicio 7: Mostrar todos lo numeros impares entre dos numeros que decida el usuario
"""

numero_1 = int(input("Ingrese primer numero: "))
numero_2 = int(input("Ingrese segundo numero: "))

if numero_1 < numero_2:
    for secuencia in range(numero_1, numero_2+1):
        if secuencia%2 != 0:
            print(f"{secuencia} es IMPAR")
        else:
            print(f"{secuencia} es PAR")
else:
    print("El numero 1 es menor al numero 2")