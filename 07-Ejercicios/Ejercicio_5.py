'''
Ejercicio 5: Hacer un programa que muestre todos los numero entre dos numeros numero que diga el usuario
'''

numero_1 = int(input("Ingrese el numero menor: "))
numero_2 = int(input("Ingrese el numero mayor: "))

if numero_1 < numero_2:
    for numero_secuencia in range(numero_1, numero_2+1):
        print(numero_secuencia)
else:
    print("El numero 1 debe ser menor al numero 2")