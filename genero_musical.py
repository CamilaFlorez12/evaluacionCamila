from data import*
def genero_musica():
    generos=abrirArchivo("genero")
    generos=[]
    print("***bienvenido a registro de generos musicales***")
    id_genero=input("Ingrese el ID del genero:")
    descripción_genero=input("Ingrese la descripcion del genro")
    for genero in generos:
        if genero["id_genero"].lower()==id_genero.lower():
            print("Artista ya registrado")
            break
    nuevo_genero ={
        "id_genero":id_genero,
        "descripcion_genero":descripción_genero
    }
    generos.append(nuevo_genero)
    guardarArchivos("genero",generos)
    print("Artista registrado exitosamente")
    while True:
        opc=input("Desea guardar mas artistas(S/N)").strip().upper()
        if opc=="S":
            genero_musica()
            break
        elif opc=="N":
            guardarArchivos("genero",generos)
            input("Press Enter.....")
            break
        else:
            print("Ingrese una opcion valida")

        