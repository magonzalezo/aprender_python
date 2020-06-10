import datetime as dt
import hashlib
import database.Conexion as cnn

connect = cnn.conectar()
database = connect[0]
cursor = connect[1]

class Usuario:
    
    def __init__(self, nombre, apellidos, email, password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password
    
    def registrar(self):
        fecha = dt.datetime.now()
        
        # Cifrar contraseña
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))

        sql = "INSERT INTO usuarios VALUES (NULL, %s, %s, %s, %s, %s)"
        usuario = (self.nombre, self.apellidos, self.email, cifrado.hexdigest(), fecha)

        try:
            cursor.execute(sql, usuario)
            database.commit()

            result [cursor.rowcount, self]
        except:
            result = [0, self]
        
        return result
        

    def identificar(self):

        # Consulta existencia
        sql = "SELECT * FROM usuarios WHERE email =%s AND password =%s"

        # Cifrar contraseña
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))

        # Datos para la consulta
        usuario = (self.email, cifrado.hexdigest())

        cursor.execute(sql, usuario)
        result = cursor.fetchone()

        return result 