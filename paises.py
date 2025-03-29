from data import*

def paises():
    paisees=abrirArchivo("paises")
    paisees=[]
    pais_origen=input("Ingrese el nombre del pais:")
    codigo=input("Ingrese el codigo ISO del pais:")
    codigo3=input("Ingrese el codigo ISO3 del pais:")
    for paiss in paisees:
        if paiss["pais_origen"].lower()==pais_origen.lower():
            print("Pais ya registrado")
            break
    nuevo_pais={
            "nombre_pais":pais_origen,
            "codigo":codigo,
            "codigo3":codigo3
        }
    paisees.append(nuevo_pais)
    guardarArchivos("paises",paisees)
    print("Pais registrado con exito")
    while True:
        opc=input("Desea guardar mas paises(S/N)").strip().upper()
        if opc=="S":
            paises()
            break
        elif opc=="N":
            guardarArchivos("paises",paisees)
            input("Press Enter.....")
            break
        else:
            print("Ingrese una opcion valida")
        
