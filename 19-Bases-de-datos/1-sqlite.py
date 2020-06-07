# Importa modulos
import sqlite3
import pathlib

# Ruta del archivo .db (Se incluye pathlib para que lo guarde en la carpeta del ejercicio)
ruta = str(pathlib.Path(__file__).parent.absolute()) + "/pruebas.db"

# Conexion
conexion = sqlite3.connect(ruta)

# Crear cursor
cursor = conexion.cursor()

# Crear tabla
cursor.execute("""CREATE TABLE IF NOT EXISTS productos(
               id integer primary key autoincrement, 
               titulo VARCHAR(255), 
               descripcion text, 
               precio int(255) 
              ) """)

# Guardar cambios
conexion.commit()

# Insertar datos
cursor.execute("INSERT INTO productos VALUES (null, 'Producto 1', 'Descripcion producto 1', 1000)")
cursor.execute("INSERT INTO productos VALUES (null, 'Producto 2', 'Descripcion producto 2', 250)")
cursor.execute("INSERT INTO productos VALUES (null, 'Producto 3', 'Descripcion producto 3', 5500)")
conexion.commit()

# Listar de datos
cursor.execute("SELECT * FROM productos")
productos = cursor.fetchall()
# Listar todo el elemento con sus sub-elementos
print('********** [ Imprimir datos de la consulta ] ********** ')
print('\n---------Imprimir todo de una vez--------')
print(productos)
print('\n---------Imprimir elemento por elemento--------')
# Para listar elemento por elemento
for producto in productos:
    print("\n-----------------------------------------")
    print("Imprimir en una linea: ",producto,"\n")
    print("Imprimir columna o elemento independiente de la linea:")
    print("Id:          ",producto[1])
    print("Titulo:      ",producto[1])
    print("Descripción: ",producto[2])
    print("Precio:      ",producto[3])

# Listar el primer elemento
cursor.execute("SELECT * FROM productos")
primerProducto = cursor.fetchone()
print('\n********** [ Obtener e imprimir primer elemento de consulta ] **********')
print(primerProducto)

# Borrar elementos de la tabla
cursor.execute("DELETE FROM productos")
conexion.commit()
consultaBorrado = cursor.fetchall()
print('\n********** [ Borrar y tratar de mostrar registros ] **********')
print(consultaBorrado)

# Insertar varios datos en una sola ejecucion
print('\n********** [ Insertar varios registros a la vez e imprimir todo de una vez ] **********')
productos_sentencia = [
                        ("Samsumg S10", "Smartphone", 1000),
                        ("Kalley 55", "Smart TV de 55 pulgadas", 2500),
                        ("Lenovo YQ", "Tablet para niños", 500),
                      ]
cursor.executemany("INSERT INTO productos VALUES (null,?,?,?)", productos_sentencia)
conexion.commit()
cursor.execute("SELECT * FROM productos")
productos = cursor.fetchall()
print(productos)

# Listar cumpliendo condicion
print("\n********** [ Imprimir lista de productos bajo determinada condicion ] **********")
cursor.execute("SELECT * FROM productos WHERE precio >= 1000")
productos = cursor.fetchall()
print(productos)

# Actualizar productos
print("\n********** [ Actualizar y mostar producto ]**********")
cursor.execute("SELECT * FROM productos WHERE descripcion = 'Smartphone'")
productos = cursor.fetchall()
print("\n-----------Productos antes del cambio-----------")
print(productos)

cursor.execute("UPDATE productos SET precio = 1111 WHERE descripcion = 'Smartphone'")
conexion.commit()
cursor.execute("SELECT * FROM productos WHERE descripcion = 'Smartphone'")
productos = cursor.fetchall()
print("\n-----------Productos despues del cambio-----------")
print(productos)

# Cerrar conexion
conexion.close()