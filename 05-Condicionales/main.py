"""
# Condicional IF

SI se_cumple_esta_condicion
    Ejecutar grupo de instrucciones
SI NO
    Ejecutar otro grupo de instrucciones

if condicion:
    intrucciones
else:
    otras instrucciones

# Operadores de comparacion
== igual
!= diferente
< menor que
> mayor
<= menor o igual que
>= mayor o igual que

# Operadores logicos
and Y
or O
! negacion
not no

"""

# Ejemplo 1
print("\n############### Ejemplo 1 ##############")

color = "rojo"

if color == "rojo":
    print("El color es rojo")
else:
    print("El color no es rojo")

# Ejemplo 2
print("\n############### Ejemplo 2 ##############")

year = 2020

if year >= 2021:
    print("Estamos de 2021 en adelante")
else:
    print("Es un año anterior a 2021")

# Ejemplo 3
print("\n############### Ejemplo 3 ##############")

nombre = "Miguel Gonzalez"
ciudad = "Colombia"
continente = "America"
edad = 60
mayoria_Edad = 18

if edad >= mayoria_Edad:
    
    print(f"{nombre} es mayor de edad")
    
    if continente != "America":
        print("El usuario no es americano")
    else:
        print(f"Es americano y de {ciudad}")

else:
    print(f"{nombre} no es mayor de edad")

# Ejemplo 4
print("\n############### Ejemplo 4 ##############")

dia = 7

if dia == 1:
    print("Es lunes")
elif dia == 2:
    print("Es martes")
elif dia == 3:
    print("Es miercoles")
elif dia == 4:
    print("Es jueves")
elif dia == 5:
    print("Es viernes")
elif dia == 6:
    print("Es sabado")
elif dia == 7:
    print("Es domingo")
else:
    print("Dia no valido")

# Ejemplo 5
print("\n############### Ejemplo 5 ##############")

edad_minima = 18
edad_maxima = 65
edad_oficial = 17

if edad_oficial >= 18 and edad_oficial <= 65:
    print("Esta en edad de trabajar!!")
else:
    print("No está en edad de trabajar")

# Ejemplo 6
print("\n############### Ejemplo 6 ##############")

pais = 'Alemania'

if pais == "Mexico" or pais == "España" or pais == "Colombia":
    print(f"{pais} es un pais de habla hispana")
else:
    print(f"{pais} no es un pais de habla hispana")

# Ejemplo 7
print("\n############### Ejemplo 7 ##############")

pais = 'España'

if not (pais == "Mexico" or pais == "España" or pais == "Colombia"):
    print(f"{pais} no es un pais de habla hispana")
else:
    print(f"{pais} es un pais de habla hispana")

# Ejemplo 8
print("\n############### Ejemplo 8 ##############")

pais = 'USA'

if pais != "Mexico" and pais != "España" and pais != "Colombia":
    print(f"{pais} no es un pais de habla hispana!!")
else:
    print(f"{pais} es un pais de habla hispana :)")