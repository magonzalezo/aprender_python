import mysql.connector as mc


def conectar():
    __configuracion = {
                    'user'    : 'root'            # Usuario con el que se conectara
                    ,'password': 'moka'            # Contraseña de autenticación
                    ,'host'    : 'localhost'       # Servidor donde se conecta
                    ,'port'    : 3306              # Puerto, aunque se puede omitir si es el default
                    ,'database': 'database_python' # Nombre de la base de datos a la que se conecta        
                    }

    database = mc.connect(**__configuracion)

    cursor = database.cursor(buffered=True)

    return [database, cursor]