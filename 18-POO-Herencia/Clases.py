"""
 Herencia: Es la posibilidad de compartir atributos y metodos entre clases. Ademas
           de que diferentes clases hereden de otras
"""
# Clase padre
class Persona:
    """
    nombres
    apellidos
    altura
    edad
    """
    
    # Definicion de Getters Y Setters
    def getNombres(self):
        return self.nombres
    
    def setNombres(self, nombres):
        self.nombres = nombres

    def getApellidos(self):
        return self.apellidos
    
    def setApellidos(self, apellidos):
        self.apellidos = apellidos

    def getAltura(self):
        return self.altura
    
    def setAltura(self, altura):
        self.altura = altura
    
    def getEdad(self):
        return self.edad
    
    def setEdad(self, edad):
        self.edad = edad
    
    # Acciones
    def hablar(self):
        return "Estoy hablando..."
    
    def dormir(self):
        return "Estoy durmiendo..."
    
    def caminar(self):
        return "Estoy caminando..."

# Clase hija
class Informatico (Persona):
    """
    lenguajes
    experiencia
    """
    
    def __init__(self):
        self.lenguajes = "HMTL, CSS, JavaScript, PHP"
        self.experiencia = 5

    def getLenguajes(self):
        return self.lenguajes
    
    def aprender(self, lenguajes):
        self.lenguajes = lenguajes
        return self.lenguajes
    
    def programar(self):
        return "Estoy programando..."
    
    def repararPC(self):
        return "He reparado el PC!!"

class TecnicoRedes(Informatico):

    def __init__(self):
        super().__init__()
        self.auditarRedes = 'Experto'
        self.experienciaRedes = 15
    
    def auditoria(self):
        return "Estoy auditando una red"