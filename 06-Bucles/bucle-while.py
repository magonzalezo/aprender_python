"""
# Bucle While
Estructura de control que itera o repite la ejecucion de una serie de instrucciones tantas veces como sea necesario, hasta que deje de cumplirse la condicion

while condicion:
    bloque de instrucciones
    actualizacion de contador

"""

print("########## EJEMPLO 1 ##########")
contador = 1

while contador <= 100:
    print(f"Estoy en el numero: {contador}")
    contador +=1

print("\n########## EJEMPLO 2 ##########")

contador = 1
concatenar = str(0)

while contador <= 100:
    concatenar +=", "+str(contador)
    contador +=1

print(concatenar)

print("\n########## EJEMPLO 3 ##########")

numero_usuario = int(input("¿De que número quieres la tabla?: "))

if numero_usuario < 1:
    numero_usuario = 1

print(f"\n### Tabla del {numero_usuario} ###")

contador = 1

while contador <= 10:
    print(f"{numero_usuario} x {contador} = {numero_usuario * contador}")
    contador += 1
else:
    print("\nTabla terminada.")