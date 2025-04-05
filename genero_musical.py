from data import*
def genero_musica():
    existe=False
    generos=abrirArchivo("genero")
    print("***bienvenido a registro de generos musicales***")
    id_genero=input("Ingrese el ID del genero:")
    for genero in generos:
        if genero["id_genero"]==id_genero:
            existe=True
    if existe==True:
            print("Genero ya registrado")
    elif existe==False:
        descripcion=input("Ingrese la descripcion del genero:")
    nuevo_genero ={
        "id_genero":id_genero,
        "descripcion_genero":descripcion
    }
    generos.append(nuevo_genero)
    guardarArchivos("genero",generos)
    print("Genero registrado exitosamente")
    while True:
        opc=input("Desea guardar mas generos(S/N)").strip().upper()
        if opc=="S":
            genero_musica()
            break
        elif opc=="N":
            guardarArchivos("genero",generos)
            input("Press Enter.....")
            break
        else:
            print("Ingrese una opcion valida")
def editar_genero():
    genero=abrirArchivo("genero")
    print("***Bienvendido a editar generos musicales***")
    id_genero=input("Ingrese le ID del genero a editar:")
    existe=False
    for musica in genero:
        for nom in musica.values():
            if nom.lower()==id_genero.lower():
                existe=True
                indice=genero.index(musica)
    if existe==True:
        info=[]
        seguir_ingresando=True
        while seguir_ingresando:
            descripcion_genero=input("Ingrese la descripcion del genero")
            while True:
                opc=input("Desea editar mas generos(S/N):").upper()
                if opc=="S":
                    gen_existe=None
                    nom_gen=input("Ingrese el ID del genero a editar:")
                    for musica in genero:
                        if musica["id_genero"]==nom_gen:
                            gen_existe=True
                    if gen_existe==True:
                        descripcion_genero2=input("Ingrese la descripcion del genero")
                        genero2={
                                "id_genero":nom_gen,
                                "descripcion_genero":descripcion_genero2
                            }
                        info.append(genero2)
                        genero.append(info)
                        guardarArchivos("genero",genero)
                        print("Genero editado existosamente")
                        break
                    else:
                        print("Genero no registrado")
                elif opc=="N":
                    genero[indice]={
                            "id_genero":id_genero,
                            "descripcion_genero":descripcion_genero
                        }
                    guardarArchivos("genero",genero)
                    print("Genero editado exitosamente")
                    seguir_ingresando=False
                    break
                else:
                    print("Ingrese una opcion valida")
    else:
        print("Genero no existe")
def eliminar_genero():
    genero=abrirArchivo("genero")
    print("***Bienvenido a eliminar genros musicales***")
    id_genero=input("Ingrese el ID del genero a eliminar:")
    existe=False
    for musica in genero:
        if musica["id_genero"]==id_genero:
            genero.remove(musica)
            existe=True
    if existe==True:
        guardarArchivos("genero",genero)
        print("Genero eliminado existosamente")
    else:
        print("Genero no existe")
       
