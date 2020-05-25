"""
DICCIONARIO: Tipo de dato almacena un conjunto de datos en formato clave valor.
             Parecido a un array asociativo u objeto JSON.
"""

persona = {
           "nombres": "Miguel"
          ,"apellidos": "Gonzalez"
          ,"Direccion": "Evergreen 123"
          }

print(type(persona))
print(persona)
print(persona["apellidos"])

# Lista con diccionarios
contactos = [
              {
                  'nombre': 'Miguel'
                 ,'email': 'miguel@cualquierdominio.com'
              }
             ,{
                  'nombre': 'Pepito'
                 ,'email': 'pepito@cualquierdominio.com'
              }
             ,{
                  'nombre': 'Fulano'
                 ,'email': 'fulano@cualquierdominio.com'
              }
            ]

print(contactos)
print(contactos[0]["nombre"])

print('\nListado de contactos')
print("-------------------------")

for contacto in contactos:
    print(f"Nombre del contacto: {contacto['nombre']}")
    print(f"Email del contacto: {contacto['email']}")
    print("-------------------------")
