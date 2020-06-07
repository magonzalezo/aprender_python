import Clases as cp

# Objeto padre
print(' ---- Objeto Padre ----')
persona = cp.Persona()

persona.setNombres("Pepito")
persona.setApellidos("Perez")
persona.setAltura("200cm")
persona.setEdad("1000 años")

print(f"La persona es: {persona.getNombres()} {persona.getApellidos()}")
print(persona.hablar())

# Objeto hijo
print('\n ---- Objeto Hijo ----')
informatico = cp.Informatico()

informatico.setNombres("Miguel")
informatico.setApellidos("Gonzalez")
informatico.setAltura("150cm")
informatico.setEdad("100 años")

print(f"El informatico es: {informatico.getNombres()} {informatico.getApellidos()}")
print(informatico.hablar())
print(informatico.programar())
print(informatico.getLenguajes())

# Otro objeto hijo
print('\n ---- Objeto Hijo ----')
tecnico = cp.TecnicoRedes()
tecnico.setNombres("Goku")

print(tecnico.auditarRedes, tecnico.getNombres(), tecnico.getLenguajes())