"""
# FOR

elementos_iterables
-Listas
-Rangos
-Tuplas
-etc

for variable in elemento_iterable
    Bloque de instrucciones


Para interrumpir el bucle for se puede usar la instruccion break

"""

# Ejemplo 1
print("\n############### Ejemplo 1 ##############")

#contador = 0
resultado = 0

for contador in range(0, 10):
    print(f"Voy por el {str(contador)}")
    resultado +=contador

print(f"\nEl resultado es {str(resultado)}")

# Ejemplo 2
print("\n############### Ejemplo 2 ##############\n")

numero_usuario = int(input("¿De que número quieres la tabla?: "))

if numero_usuario < 1:
    numero_usuario = 1

print(f"\n#### Tabla del multiplicar del número {numero_usuario} ####")

for numero_tabla in range(1,11): # Recordar que el rango llega al limite que le coloquemo -1, por ello hay que colocarlo un numero despues
    print(f"{numero_usuario} x {numero_tabla} = {numero_usuario * numero_tabla}")
else:
    print("Tabla finalizada.")

# Ejemplo 3
# Interrumpir un bloque for
print("\n############### Ejemplo 3 ##############\n")

numero_interrupcion = int(input("¿Cual es el numero de interrupcion?: "))

for contador_local in range(1,11): # Recordar que el rango llega al limite que le coloquemo -1, por ello hay que colocarlo un numero despues
    
    if contador_local >= numero_interrupcion:
        break

    print(f"Voy por el {str(contador_local)}")
else:
    print("Ciclo finalizado.")