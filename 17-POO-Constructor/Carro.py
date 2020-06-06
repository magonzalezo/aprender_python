class Carro:

    #Atributos / propiedades (variables)
    color = "Rojo"
    marca = "Ferrari"
    modelo = "Spider"
    velocidad = 300
    caballaje = 500
    plazas = 2
    
    publico = "Hola soy un atributo publico"
    __privado = "Hola soy un atributo privado"

    # Constructor inicializando atributos
    def __init__(self, color, marca, modelo, velocidad, caballaje, plazas):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.caballaje = caballaje
        self.plazas = plazas

    # Métodos: Acciones que hace el objeto (Carro) [Funciones]
    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1
    
    # Getters y Setters    
    def getColor(self):
        return self.color
    
    def setColor(self, color):
        self.color = color

    def setMarca(self, marca):
        self.marca = marca
    
    def getMarca(self):
        return self.marca

    def setModelo(self, modelo):
        self.modelo = modelo
    
    def getModelo(self):
        return self.modelo
    
    def setVelocidad(self, velocidad):
        self.velocidad = velocidad

    def getVelocidad(self):
        return self.velocidad
    
    def setCaballaje(self, caballaje):
        self.caballaje = caballaje
    
    def getCaballaje(self):
        return self.caballaje
    
    def setPlazas(self, plazas):
        self.plazas = plazas
    
    def getPlazas(self):
        return self.plazas
    
    def getPrivado(self):
        return self.__privado

    # Retornar la informacion del objeto
    def getInfo(self):
        informacion = "---- Informacion del carro ----"
        informacion +="\n Color: " + self.getColor()
        informacion +="\n Marca: " + self.getMarca()
        informacion +="\n Modelo: " + self.getModelo()
        informacion +="\n Velocidad: " + str(self.getVelocidad())
        informacion +="\n Caballaje: " + str(self.getCaballaje())
        informacion +="\n Plazas: " + str(self.getPlazas())
        return informacion

# Fin definicion clase