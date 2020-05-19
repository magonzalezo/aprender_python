'''
Ejercicio 6: Mostrar todaslas tablas de multiplicar del 1 al 10.
             Mostrando el titulo de la tabla y luego las multiplicaciones del 1 al 10.
'''

for numero in range(1, 11):

    print(f"############################")
    print(f"####### TABLA DEL {numero} #######")
    print(f"############################")

    for numero_tabla in range(1, 11):
        print(f"{numero} X {numero_tabla} = {numero * numero_tabla}")
    
    print("\n")
