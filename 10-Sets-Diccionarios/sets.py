"""
SET: es un tipo de dato, para tener una coleccion de valores, pero no tiene ni indice
     ni orden
"""

personas = {"Miguel", "Pepito", "Fulano"}
personas.add("Paco")
personas.remove("Pepito")

print(type(personas))
print(personas)