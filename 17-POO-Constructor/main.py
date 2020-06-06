from Carro import Carro

carro_1 = Carro("Blanco", "Ford", "Focus", 200, 100, 4)
carro_2 = Carro("Azul", "Renault", "Megane", 400, 50, 4)
carro_3 = Carro("Amarillo", "Chevrolet", "Camaro", 300, 250, 4)

print(carro_1.getInfo())
print("\n"+carro_2.getInfo())
print("\n"+carro_3.getInfo())

print('')

# Detertar tipo de objeto
if type(carro_2) == Carro:
    print("Es un objeto correcto!!")
else:
    print("No es objeto carro!!")

print('')

# Detectar instancia de objeto
if isinstance(carro_2, Carro):
    print("Es una instancia correcta!!")
else:
    print("No es instancia de carro!!")

# Visibilidad
print('')
carro_visibilidad = Carro("Gris", "Tesla", "Model 3", 200, 100, 4)
print(carro_visibilidad.publico)
print(carro_visibilidad.getPrivado())