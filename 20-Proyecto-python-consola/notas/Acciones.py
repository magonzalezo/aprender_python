import notas.Nota as modelo

class Acciones:

    def crear(self, usuario):
        print(f"\nOk {usuario[1]} Vamos a crear una nueva nota...")
        
        titulo = input("Introduce el titulo de tu nota: ")
        descripcion = input("Introduce el contenido de tu nota: ")
        
        nota = modelo.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()

        if guardar[0] >= 1:
            print(f"\nPerfecto has guardado la nota: {nota.titulo}")
        else:
            print(f"\nNo se ha guardado la nota: {usuario[1]}")
    
    def mostrar(self, usuario):
        print(f"\nVale {usuario[1]}!! Aqui tienes tus notas:")

        nota = modelo.Nota(usuario[0])
        notas = nota.listar()

        for registro in notas:
            print("\n********************************")
            print(f"ID: [{registro[0]}]")
            print(f"Titulo: {registro[2]}")
            print(f"Descripcion: {registro[3]}")
    
    def eliminar(self, usuario):
        print(f"\nOk {usuario[1]}!! vamos a borrar notas")

        titulo = input("Introduce el titulo de la nota a borrar: ")

        nota = modelo.Nota(usuario[0], titulo)

        eliminar = nota.eliminar(usuario)

        if eliminar[0] >= 1:
            print(f"Hemos borrado la nota: {nota.titulo}")
        else:
            print("No hemos borrado la nota, Intenta mas tarde")