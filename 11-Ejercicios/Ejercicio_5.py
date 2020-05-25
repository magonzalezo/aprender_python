"""
Ejercicio 5: Crear una lista con el contenido de esta tabla:
             Tabla = platos de comida

                   SOPAS             ENSALADAS       BANDEJAS
             Ajiaco con pollo    Mixta           Bagre en salsa          
             Mondongo            Caprece         Mamona
             Mute                Waldorf         Bandeja paisa
             Cocido boyasence    Oliver          Cazuela de mariscos

             -Crear un diccionario con lo anterior.
             -Mostrar la informacion ordenada.
"""
tabla = [
            {
                "categoria": "SOPAS",
                "platos": ["Ajiaco con pollo", "Mondongo", "Mute", "Cocido boyasence"]
            }
           ,{
                "categoria": "ENSALADAS",
                "platos": ["Mixta", "Caprece", "Waldorf", "Oliver"]
            }
           ,{
                "categoria": "BANDEJAS",
                "platos": ["Bagre en salsa", "Mamona", "Bandeja paisa", "Cazuela de mariscos"]
            }
        ]

for categoria in tabla:
    print(f" --------------- {categoria['categoria']} ---------------")
    for elemento in categoria['platos']:
        print(f"-{elemento}")