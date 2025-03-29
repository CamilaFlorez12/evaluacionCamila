from data import*
from paises import*
def informacion():
    music=abrirArchivo("musica")
    print("***bienvenido a registro de artistas***")

    nombre_artista=input("Ingrese el nombre del artista:")
    pais_origen=input("Ingrese pais de origen:")
    anios_actividad=input("Ingrese los años de actividad:")
    anio_lanzamiento=input("Ingrese el año del primer disco que llego a las listas:")
    genero_musical=input("Ingrese genero musical:")
    unidad_certificada=input("Ingrese unidades certificadas totales:")
    ventas=input("Ingrese ventas reclamadas:")
    estado_artista=input("Ingrese si esta activo o si esta inactivo:")
    for artista in music:
        if artista["nombre_artista"].lower()==nombre_artista.lower():
            print("Artista ya registrado")
            break
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
            #print("Artista registrado exitosamente")
            input("Press Enter.....")
            
            break
        else:
            print("Ingrese una opcion valida")
