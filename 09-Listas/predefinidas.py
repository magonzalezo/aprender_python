'''
Funciones predefinidas para las listas
'''
cantantes = ['Juanes', 'Andres Cepeda', 'Ilona', 'Andrea Echeverry', 'Fonseca']
numeros = [1, 2, 5, 8, 3, 4]

# Ordenar
print('----------- Ordenamiento de listas -----------')
print("Orden natural: ", numeros)
numeros.sort()
print("Lista ordenada: ", numeros)
numeros.sort(reverse = True)
print("Lista ordenada descendiente: ", numeros)

# Añadir elementos
print('\n----------- Añadir elementos en listas -----------')
print(cantantes)
cantantes.append("Shakira")
print(cantantes)
cantantes.insert(2,"Cabas")
print(cantantes)

# Eliminar elementos 
print('\n----------- Eliminar elementos en listas -----------')
cantantes.pop(2)
print(cantantes)
cantantes.remove("Shakira")
print(cantantes)

# Dar la vuelta
print('\n----------- Dar la vuelta a una lista -----------')
print("Lista original: ", numeros)
numeros.reverse()
print("Lista reversa: ", numeros)

# Buscar dentro de una lista
print('\n----------- Buscar dentro de una lista -----------')
print('Juanes' in cantantes)

# Contar elementos
print('\n----------- Contar elementos en una lista -----------')
print(len(cantantes))

# Cuantas veces aparece un elemento
print('\n----------- Cantidad de ocurrecias de elemento en lista -----------')
numeros.append(8)
print(numeros.count(8))

# Conseguir indice 
print('\n----------- Conseguir indice de elementos en lista -----------')
print(cantantes.index("Fonseca"))

# Unir listas
print('\n----------- Unir listas -----------')
print(cantantes)
cantantes.extend(numeros)
print(cantantes)