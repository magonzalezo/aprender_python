"""
Ejercicio 12: Se desea recibir un listado de numeros y luego organizarlos 
              en orden ascendente, la lista resultante debe ser tipo entero
"""

x_string = input("Ingrese un grupo de numeros separados por espacio: \n")

x_str_list = x_string.split()
y_int_list = [int(i) for i in x_str_list]
y_int_list.sort()
print(y_int_list)