"""
Ejercicio 10: El programa tiene que pedir cuantos alumnos procesara y por cada uno
              solicitara la nota y sacar por pantalla cuantos han aprobado 
              y cuantos han suspendido. Aprueba si la nota es mayor o igual a 5
"""
aprobaron = 0
reprobaron = 0

alumnos = int(input(f"Ingrese la cantidad de alumnos a procesar: "))

print(' ')

for alumno in range(1,alumnos +1):
    nota = int(input(f"Ingrese la nota del alumno {alumno}: "))
    if nota >= 5:
        aprobaron += 1
    else:
        reprobaron += 1

print(f"\nAlumnos aprobados: {aprobaron}")
print(f"Alumnos reprobados: {reprobaron}")