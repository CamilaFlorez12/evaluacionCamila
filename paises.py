from data import*

def paises():
    existe=False
    pais=abrirArchivo("paises")
    print("***Bienvendio a registro de paises***")
    pais_origen=input("Ingrese el nombre del pais:")
    for paises2 in pais:
        if paises2["nombre_pais"].lower()==pais_origen.lower():
            existe=True
    if existe==True:
        print("Pais ya registrado")
    elif existe==False:
        codigo=input("Ingrese el codigo ISO del pais:")
        codigo3=input("Ingrese el codigo ISO3 del pasi:")
    nuevo_pais={
            "nombre_pais":pais_origen,
            "codigo":codigo,
            "codigo3":codigo3
        }
    pais.append(nuevo_pais)
    guardarArchivos("paises",pais)
    print("Pais registrado con exito")
    while True:
        opc=input("Desea guardar mas paises(S/N)").strip().upper()
        if opc=="S":
            paises()
            break
        elif opc=="N":
            guardarArchivos("paises",pais)
            print("Pais registrado exitosamente")
            break
        else:
            print("Ingrese una opcion valida")
def editar_pais():
    pais=abrirArchivo("paises")
    print("***Bienvenido a editar paises***")
    nombre_pais=input("Ingrese el nombre del pais a editar:")
    existe=False 
    for paises in pais:
        for nom in paises.values():
            if nom.lower()==nombre_pais.lower():
                existe=True
                indice=pais.index(paises)
    if existe==True:
        info=[]
        seguir_ingresando=True
        while seguir_ingresando:
            codigo=input("Ingrese el codigo ISO del pais:")
            codigo3=input("Ingrese el codigo ISO3 del pais:")
            while True:
                opc=input("Desea editar mas paises(S/N)").upper()
                if opc=="S":
                    paiss=None
                    nombre=input("Ingrese el nombre del pais a editar:")
                    for paises in pais:
                        if paises["nombre_pais"].lower()==nombre.lower():
                            existe=True
                    if existe==True:
                        codigo=input("Ingrese el codigo ISO del pais:")
                        codigo3=input("Ingrese el codigo ISO3 del pais:")
                        paiss={
                            "nombre_pais":nombre,
                            "codigo":codigo,
                            "codigo3":codigo3
                        }
                        info.append(paiss)
                        pais.append(info)
                        guardarArchivos("paises",pais)
                        print("Pais editado exitosamente")
                        break
                elif opc=="N":
                    pais[indice]={
                        "nombre_pais":nombre_pais,
                        "codifo":codigo,
                        "codigo3":codigo3
                    }
                    guardarArchivos("paises",pais)
                    print("Pais editado exitosamente")
                    seguir_ingresando=False
                    break
                else:
                    print("Ingrese una opcion valida")
                    
    else:
        print("Pais no registrado")
def eliminar_pais():
    pais=abrirArchivo("paises")
    print("***Bienvenido a eliminar paises***")
    nombre_pais=input("Ingrese el nombre del pais a eliminar:")
    existe=False
    for paises in pais:
        if paises["nombre_pais"].lower()==nombre_pais.lower():
            pais.remove(paises)
            existe=True
    if existe==True:
        guardarArchivos("paises",pais)
        print("Pais eliminado exitosamnte")
    else:
        print("Pais no registrado")
