import mysql.connector as mc

# Conexion (Opcion 1)
"""
database = mc.connect(
                      host     = "localhost", # Servidor donde se conecta
                      port     = "3306",      # Puerto, aunque se puede omitir si es el default
                      user     = "root",      # Usuario con el que se conectara
                      passwd   = "moka",      # Contraseña de autenticación
                      database = "mysql"      # Nombre de la base de datos a la que se conecta                      
                     )
"""

# Conexion (Opcion 2)
configuracion = {
                 'user'    : 'root'          # Usuario con el que se conectara
                ,'password': 'moka'          # Contraseña de autenticación
                ,'host'    : 'localhost'     # Servidor donde se conecta
               #,'port'    : '3306'          # Puerto, aunque se puede omitir si es el default
                ,'database': 'miguel_python' # Nombre de la base de datos a la que se conecta        
                }
database = mc.connect(**configuracion)

# La conexion ha sido correcta
#print(database)

# Cursor de consultas
cursor = database.cursor(buffered=True)

# Crear base de datos 
cursor.execute("CREATE DATABASE IF NOT EXISTS miguel_python")
"""
cursor.execute("SHOW DATABASES")

print("\n--------Bases de datos que tengo--------")
for bd in cursor:
    print(bd)
"""

# Crear tablas
cursor.execute("""
               CREATE TABLE IF NOT EXISTS vehiculos(
                   id     int(10)     auto_increment not null,
                   marca  varchar(40)                not null,
                   modelo varchar(40)                not null,
                   precio float(10,2)                not null,
                   CONSTRAINT pk_vehiculo PRIMARY KEY (id)
               )
               """)

# Mostrar tablas
"""
cursor.execute("SHOW TABLES")
print("\n--------Tablas que tengo en base de datos--------")
for tabla in cursor:
    print(tabla)
"""

# Insertar valores (uno a uno)
cursor.execute("INSERT INTO vehiculos VALUES (null, 'Chevrolet', 'Camaro', 20500.50)")
database.commit()

# Insertar valores (masivo)
vehiculos = [
              ('Ford', 'Explorer', 14000)
             ,('Honda', 'Civic', 10000)
             ,('Mitsubishi', 'Lancer', 15000)
             ,('Citroen','Saxo',7000)
            ]
cursor.executemany("INSERT INTO vehiculos VALUES (null, %s,%s,%s)", vehiculos)
database.commit()

# Mostrar datos de tabla
cursor.execute("SELECT * FROM vehiculos")
print("\n--------Registros que tengo en tabla--------")
resultado = cursor.fetchall()
for fila in resultado:
    print(fila)

# Mostrar datos de tabla
cursor.execute("SELECT modelo, precio FROM vehiculos")
print("\n--------Registros que tengo en tabla (indicando columnas)--------")
resultado = cursor.fetchall()
for fila in resultado:
    print(fila[0], fila[1])

# Mostrar datos de tabla
cursor.execute("SELECT * FROM vehiculos WHERE precio > 10000")
print("\n--------Registros que tengo en tabla (Haciendo filtro)--------")
resultado = cursor.fetchall()
for fila in resultado:
    print(fila)

# Consultar el primer registro de la tabla y mostrarlo
print("\n--------Primer registro en la consulta--------")
cursor.execute("SELECT * FROM vehiculos")
vehiculo = cursor.fetchone()
print(vehiculo)

# Borrar elemento por filtro
print("\n--------Borrado de registros--------")
cursor.execute("DELETE FROM vehiculos WHERE marca = 'Ford'")
database.commit()
print(cursor.rowcount, "Borrados!!")

# Actualizar datos
print("\n--------Actualizado de registros--------")
cursor.execute("UPDATE vehiculos SET modelo = 'Spider' WHERE marca = 'Mitsubishi'")
database.commit()
print(cursor.rowcount, "Actualizados!!")

cursor.close()
database.close()