from data import*
from paises import*
def informacion():
    existe=False
    music=abrirArchivo("musica")
    print("***bienvenido a registro de artistas***")
    nombre_artista=input("Ingrese el nombre del artista:")
    for artista in music:
        if artista["nombre_artista"].lower()==nombre_artista.lower():
            existe=True
    if existe==True:
        print("Artista ya registrado")
    elif existe==False:
        pais_origen=input("Ingrese pais de origen:")
        anios_actividad=int(input("Ingrese los años de actividad:"))
        anio_lanzamiento=int(input("Ingrese el año del primer disco que llego a las listas:"))
        genero_musical=input("Ingrese genero musical:")
        unidad_certificada=int(input("Ingrese unidades certificadas totales:"))
        ventas=int(input("Ingrese ventas reclamadas:"))
        estado_artista=input("Ingrese si esta activo o si esta inactivo:")
        nuevo_artista ={
            "nombre_artista":nombre_artista,
            "pais_origen":pais_origen,
            "anios_actividad":anios_actividad,
            "anio_lanzamiento":anio_lanzamiento,
            "genero_musical":genero_musical,
            "unidad_certificada":unidad_certificada,
            "ventas":ventas,
            "estado_artista":estado_artista
        }
        music.append(nuevo_artista)
        guardarArchivos("musica",music)
        print("Artista registrado exitosamente")
        while True:
            opc=input("Desea guardar mas artistas(S/N)").strip().upper()
            if opc=="S":
                informacion()
                break
            elif opc=="N":
                guardarArchivos("musica",music)
                print("Artista registrado exitosamente")
                
                
                break
            else:
                print("Ingrese una opcion valida")
def editar_informacion():
    music=abrirArchivo("musica")
    print("***Bienvenido a editar artistas***")
    nombre_artista=input("Ingrese el nombre del artista a editar:")
    existe=False
    for artista in music:
        for nom in artista.values(): 
            if nom==nombre_artista:
                existe=True
                indice=music.index(artista)
    if existe==True:
        info=[]
        seguir_ingresando=True
        while seguir_ingresando:
            pais_origen=input("Ingrese pais de origen:")
            anios_actividad=int(input("Ingrese los años de actividad:"))
            anio_lanzamiento=int(input("Ingrese el año del primer disco que llego a las listas:"))
            genero_musical=input("Ingrese genero musical:")
            unidad_certificada=int(input("Ingrese unidades certificadas totales:"))
            ventas=int(input("Ingrese ventas reclamadas:"))
            estado_artista=input("Ingrese si esta activo o si esta inactivo:")
            while True:
                opc=input("¿Quiere editar mas artistas?(S/N):").upper()
                if opc=="S":
                    atr_existe=None
                    nom2=input("Ingrese el nombre de artista:")
                    for artista in music:
                        if artista["nombre_artista"].lower()==nom2.lower():
                            atr_existe=True
                    if atr_existe==True:
                        pais_origen=input("Ingrese pais de origen:")
                        anios_actividad=int(input("Ingrese los años de actividad:"))
                        anio_lanzamiento=int(input("Ingrese el año del primer disco que llego a las listas:"))
                        genero_musical=input("Ingrese genero musical:")
                        unidad_certificada=int(input("Ingrese unidades certificadas totales:"))
                        ventas=int(input("Ingrese ventas reclamadas:"))
                        estado_artista=input("Ingrese si esta activo o si esta inactivo:")
                        editar={
                            "nombre_artista":nom2,
                            "pais_origen":pais_origen,
                            "anios_actividad":anios_actividad,
                            "anio_lanzamiento":anio_lanzamiento,
                            "genero_musical":genero_musical,
                            "unidad_certificada":unidad_certificada,
                            "ventas":ventas,
                            "estado_artista":estado_artista
                        }
                        info.append(editar)
                        music.append(info)
                        guardarArchivos("musica",music)
                        print("Artista registrado existosamente")
                        break
                    else:
                        print("Artista no registrado")    
                elif opc=="N":
                    music[indice]={
                        "nombre_artista":nombre_artista,
                        "pais_origen":pais_origen,
                        "anios_actividad":anios_actividad,
                        "anio_lanzamiento":anio_lanzamiento,
                        "genero_musical":genero_musical,
                        "unidad_certificada":unidad_certificada,
                        "ventas":ventas,
                        "estado_artista":estado_artista
                    }
                    guardarArchivos("musica",music)
                    print("Artista registrado exitosamnete")
                    seguir_ingresando=False
                    break
                else:
                    print("Ingrese una opcion valida")
    else:
        print("Artista no registrado")
def eliminar_artista():
    music=abrirArchivo("musica")
    print("***Bienvenido a eliminar artista***")
    nombre_artista=input("Ingrese el nombre del artista que desea eliminar:")
    existe=False
    for artista in music:
        if artista["nombre_artista"].lower()==nombre_artista.lower():
            music.remove(artista)
            existe=True
    if existe==True:
        guardarArchivos("musica",music)
        print("Artista eliminado exitosamente")
    else:
        print("Artista no registrado")

        
