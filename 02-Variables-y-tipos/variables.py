# Variable de texto-cadena
texto = "Master en Python"
print(texto)

print("------------------")
# Numero
numero = 5
print(numero)

print("------------------")
# Decimal
decimal = 6.9
print(decimal)

print("------------------")
# Sustituir valores
texto = "Nuevo texto"
numero = 10
decimal = 8.3
print(texto)
print(numero)
print(decimal)

print("------------------")
# Concatenacion
cadena1 = "Miguel"
cadena2 = "Gonzalez"
cadena3 = "Desarrollador"
# Comun
print("Concatenacion comun: "+cadena1+" "+cadena2+" - "+cadena3)
# Interpolar
print(f"Texto con interpolar: {cadena1} {cadena2} - {cadena3}")
# Format
print("Texto concatenado con format: {} {} - {}".format(cadena1, cadena2, cadena3))
# Print con parametros variables por parametro "No recomendable"
print(cadena1, cadena2, cadena3)