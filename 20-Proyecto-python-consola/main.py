"""
Proyecto Python (Consola) y MySql:
   - Abrir asistente
   - Login o registro
   - Si abrimos registro, creará un usuario en la base de datos
   - Si elegimos login, identificara al usuario y nos preguntará:
     - Crear nota, mostrar notas, borrar notas
"""

from usuarios import Acciones as ac

print("""
Acciones disponibles:
    - registro
    - login
      """)

accionUsuario = ac.Acciones()

accion = input("¿Qué quieres hacer?: ")

if accion == "registro":
  accionUsuario.registro()
elif accion == "login":
  accionUsuario.login()