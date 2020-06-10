import usuarios.Usuario as modelo
import notas.Acciones

class Acciones:
    
    def registro(self):
        print("\nOk!! Vamos a registrate en el sistema...")

        nombre = input("¿Cual es tu nombre?: ")
        apellidos = input("¿Cuales son tus apellidos?: ")
        email = input("Introduce tu email: ")
        password = input("Introduce tu contraseña: ")

        usuario = modelo.Usuario(nombre,apellidos, email, password)
        registro = usuario.registrar()

        if registro[0] >= 1:
            print(f"\nPerfecto {registro[1].nombre} te has registrado con el email {registro[1].email}")
        else:
            print("\nNo te has registrado correctamente")
    
    def login(self):
        print("\nVale!! Identificate en el sistema...")
        try:
            email = input("Introduce tu email: ")
            password = input("Introduce tu contraseña: ")

            usuario = modelo.Usuario('','',email,password)
            login = usuario.identificar()

            if email == login[3]:
                print(f"\nBienvenido {login[1]}, te has registrado en el sistema {login[5]}")
                self.proximasAcciones(login)

        except Exception as e:
            #print(type(e))
            #print(type(e).__name__)
            print("Login incorrecto!! Intentalo mas tarde")
    
    def proximasAcciones(self, usuario):
        print("""
        Acciones disponibles:
        - Crear nota (crear)
        - Mostrar tus nota (mostrar)
        - Eliminar nota (eliminar)
        - Salir (salir)
              """)
        
        accion = input("¿Qué quieres hacer?: ")

        accionNota = notas.Acciones.Acciones()

        if accion == "crear":
            #print("Vamos a crear!!")
            accionNota.crear(usuario)
            self.proximasAcciones(usuario)
        elif accion == "mostrar":
            #print("Vamos a mostrar!!")
            accionNota.mostrar(usuario)
            self.proximasAcciones(usuario)
        elif accion == "eliminar":
            #print("Vamos a eliminar!!")
            accionNota.eliminar(usuario)
            self.proximasAcciones(usuario)
        elif accion == "salir":
            print(f"Ok {usuario[1]} hasta pronto!!\n")
            exit()
