from data import*
from paises import*
def informacion():
    music=abrirArchivo("musica")
    nombre_artista=input("Ingrese el nombre del artista:")
    pais_origen=input("INgrese pais de origen:")
    anios_actividad=input("Ingrese los años de actividad:")
    anio_lanzamiento=input("Ingrese el año del primer disco que llego a las listas:")
    genero_musical=input("Ingrese genero musical:")
    unidad_certificada=input("Ingrese unidades certificadas totales:")
    ventas=input("Ingrese ventas reclamadas:")
    estado_artista=input("Ingrese si esta activo o si esta inactivo:")
    music =[{
        "nombre_artista":nombre_artista,
        "pais_origen":pais_origen,
        "anios_actividad":anios_actividad,
        "anio_lanzamiento":anio_lanzamiento,
        "genero_musical":genero_musical,
        "unidad_certificada":unidad_certificada,
        "ventas":ventas,
        "estado_artista":estado_artista
    }]
    opc=input("Desea guadar mas artistas ingrese S/N")
    musica=False
    for musica in musica:
        if musica==opc:
            musica==True
            print("Ya esta registrado ese artista")
        elif musica==False:
            while True:
                if opc=="S":
                    music =[{
                    "nombre_artista":nombre_artista,
                    "pais_origen":pais_origen,
                    "anios_actividad":anios_actividad,
                    "anio_lanzamiento":anio_lanzamiento,
                    "genero_musical":genero_musical,
                    "unidad_certificada":unidad_certificada,
                    "ventas":ventas,
                    "estado_artista":estado_artista
                }]
                elif opc=="N":
                    print("Artista registrado exitosamente")
                    guardarARchivos("musica",music).update
                guardarArchivos("musica",music).update
            else:
                print("Ingrese una opcion valida")
    else:
        print("Ingrese una opcion valida")

    