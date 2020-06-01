"""
Definicion: Funcionalidades ya hechas para reutilizar.
            Consultar en https://docs.python.org/3/py-modindex.html
"""
# Importar modulo propio
# import miguelmodulo
# from miguelmodulo import holaMundo
from miguelmodulo import *

print(holaMundo("Miguel"))
print(calculadora(1,3, True))

# Modulo fechas
import datetime

print(datetime.date.today())

fecha_completa = datetime.datetime.now()
print(fecha_completa)
print(fecha_completa.year)
print(fecha_completa.month)
print(fecha_completa.day)

fecha_personalizada = fecha_completa.strftime("%d/%m/%Y, %H:%M:%S")
print("Mi fecha personalizada",fecha_personalizada)

print(datetime.datetime.now().timestamp())

# Modulo matematicas
import math

print("Raiz cuadrada de 9:", math.sqrt(9))
print("Número pi:",math.pi)
print("Redondear por encima:",math.ceil(7.645654654))
print("Redondear por debajo:",math.floor(7.645654654))

# Import modulo random
import random

print("Número aleatorio entre 15 y 99:", random.randint(15,99))