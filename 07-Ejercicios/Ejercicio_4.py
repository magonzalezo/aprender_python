"""
Ejercicio 4: Pedir dos numero al usuario y hacer todas las operaciones 
             basicas de una calculadora y mostrarlo por pantalla.
"""

numero1 = int(input("Digite el primer numero: "))
numero2 = int(input("Digite el segundo numero: "))

print("\n######## Operaciones ########")
print(f"La suma entre {numero1} y {numero2} es {str(numero1 + numero2)}")
print(f"La resta entre {numero1} y {numero2} es {str((numero1 - numero2))}")
print(f"La multiplicacion entre {numero1} y {numero2} es {str(numero1 * numero2)}")
print(f"La division entre {numero1} y {numero2} es {str(numero1 / numero2)}")
