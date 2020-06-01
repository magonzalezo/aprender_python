'''
Ejercicio 13: Generar un cuadro con secuencia de puntos dado como:
              ***********
              *    *    *
              *         *
              *    *    *
              ***********
              *    *    *
              *         *
              *    *    *
              *********** 
'''
import math

num = int(input("Indique la cantidad de lineas de puntos del cuadro?: "))

print()

for i in range(1,(num+1)):
    if i == 1 or i == (num) or i == (math.ceil(num/2)):
        print("*"*(num+2))
    elif (i < num and (i%2==0)):
        print("*"+((" "*((math.floor(num/2)))+"*")*2))
    else:
        print("*"+(" "*(num)+"*"))
        
print()