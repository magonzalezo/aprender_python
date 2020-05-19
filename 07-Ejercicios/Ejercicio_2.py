'''
Ejercicio 2: Escribir un script que nos muestre por pantalla todos 
             los numeros pares del 1 al 120
'''
cadena_numero = ""

for i in range(1, 121):
    if (i%2) == 0:
        cadena_numero += str(i) + ', '
else:
    cadena_numero = cadena_numero[0:(len(cadena_numero)-2)]
    
print(cadena_numero)