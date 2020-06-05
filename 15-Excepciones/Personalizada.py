# Excepcion personalizada o lanzar excepcion

nombre = input("Introduce el nombre: ")
edad = int(input("Introduce la edad: "))

try:

    if edad < 5 or edad > 110:
        raise ValueError("La edad introducida no es real")
    elif len(nombre) <= 1:
        raise ValueError("El nombre no está completo")
    else:
        print(f"Bienvenido {nombre}")

except ValueError:
    print("Introducir los datos correctamente")
except Exception as e:
    print("Ha ocurrido un error: ", e)