"""
Ejercicio 3: Programa que compruebe si una variable está vacia y si está vacia
             llenarla con un texto en minusculas y mostrarlo en mayusculas
"""
variable = ""

if len(variable.strip()) == 0:
    variable = "estaba vacia"  
    print(variable.upper())
else:
    print(f"La variable tenia contenido: {variable}")