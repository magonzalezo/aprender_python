# Multiples excepciones

try:
    numero = int(input("Indicar numero para elevar al cuadrado: "))
    print("El cuadrado es: "+str(numero * numero))
except TypeError:
    print("Debes convertir tus cadenas a enteros!!")
except ValueError:
    print("Debes introducir un número correcto!!")
except Exception as e:
    print(type(e))
    print(f"Ha ocurrido un error: {type(e).__name__}")