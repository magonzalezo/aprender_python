# Programación orientada a objetos (POO ó OOP)

# Definir una clase (molde para crear mas objetos de ese tipo
# [Carro] con caracteristicas similares) 

# Nombre clase
class Carro:

    #Atributos / propiedades (variables)
    color = "Rojo"
    marca = "Ferrari"
    modelo = "Spider"
    velocidad = 300
    caballaje = 500
    plazas = 2

    # Métodos: Aciones que hace el objeto (Carro) [Funciones]
    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1
    
    def getVelocidad(self):
        return self.velocidad

    def setColor(self, color):
        self.color = color
    
    def getColor(self):
        return self.color
    
    def setMarca(self, marca):
        self.marca = marca
    
    def getMarca(self):
        return self.marca

    def setModelo(self, modelo):
        self.modelo = modelo
    
    def getModelo(self):
        return self.modelo

# Fin definicion clase

# Crear objetos / Instanciar la clase
carro = Carro()

# Imprimir el  objeto

print("Carro 1")
print(carro)
# Imprimir atributos del objeto
print(carro.marca, carro.color)

print('\n-------- Separador --------------\n')

# Lanzar metodos del objeto e imprimir resultados
print(f"Velocidad actual: {carro.getVelocidad()}")
carro.acelerar()
carro.acelerar()
carro.acelerar()
carro.frenar()
carro.acelerar()
print(f"Velocidad final: {carro.getVelocidad()}")

print('\n-------- Separador --------------\n')

# Anteriores valores predefinidos en el objeto
print(carro.color, carro.modelo)
# Modificacion de atributos
carro.setColor("Verde")
carro.setModelo("Roma")
# Nuevos valores
print(carro.color, carro.modelo)

print('\n-------- Separador --------------\n')

# Crear mas objetos

print("Carro 2")
carro_2 = Carro()
carro_2.setMarca("Lamborghini")
carro_2.setColor("Plateado")
carro_2.setModelo("Gallardo")
print(carro_2.getMarca(), carro_2.getModelo(), carro_2.getColor())

print('\n-------- Separador --------------\n')

print("Carro 3")
carro_3 = Carro()
carro_3.setMarca("Chevrolet")
carro_3.setColor("Azul")
carro_3.setModelo("Camaro")
print(carro_3.getMarca(), carro_3.getModelo(), carro_3.getColor())