"""
Listas (arrays): Colecciones o conjuntos de datos/valores, bajo un unico nombre.
                 Para acceder a esos valores podemos usar un indice númerico.
"""

# Definir lista
peliculas = ["Matrix", "Chappie", "Trascendente"]
cantantes = list(('Juanes', 'Ilona', 'Andrea Echeverry'))
years = list(range(2020, 2050))
variada = ["Miguel", 20, 7.7, True]

'''
print(peliculas)
print(cantantes)
print(years)
print(variada)
'''

# Indices
print(peliculas[1])
print(peliculas[-2])
print(cantantes[0:2])
print(peliculas[1:])

# Modificar valores con los indices
peliculas[1] = "Transformers"
print(peliculas)

# Añadir elementos elementos a lista
peliculas.append("Ex Machina")
print(peliculas)

# Recorrer lista
print("\n######## LISTADO DE PELICULAS ########")
for pelicula in peliculas:
    print(f"{peliculas.index(pelicula) + 1} - {pelicula}")

# Recorrer lista alimentada por usuario
nueva_pelicula = ""
while nueva_pelicula != 'parar':
    nueva_pelicula = input("Introduce la nueva pelicula: ")
    if nueva_pelicula != 'parar':
        peliculas.append(nueva_pelicula)

print("\n######## LISTADO DE PELICULAS ########")
for pelicula in peliculas:
    print(f"{peliculas.index(pelicula) + 1} - {pelicula}")

# Listas multidimensionales
print("\n************** Listado de contactos **************")
contactos = [
               [
                   'Pepito',
                   'petito@cualquierdominio.com'
               ],
               [
                   'Fulano',
                   'fulano@cualquierdominio.com'
               ],
               [
                   'Juanito',
                   'juanito@cualquierdominio.com'
               ]
            ]

'''           
print(contactos)
print(contactos[1][1])
'''

for contacto in contactos:
    for elemento in contacto:
        if contacto.index(elemento) == 0:
            print("Nombre: " + elemento)
        else:
            print("Email: " + elemento)
    print("\n")