"""
Capturar excepciones y manera errores en código susceptible a fallo/errores
"""
try:
    nombre = input("¿Cúal es tu nombre?: ")
    if len(nombre) > 1:
        mensaje = "El nombre es: " + nombre 
    print(mensaje)
except:
    print("Ha ocurrido un error, ingrese el nombre correctamente")
else:
    print("Todo ha funcionado correctamente")
finally:
    print("Fin de la iteracion!!")