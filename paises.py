from data import*
def paises():
    paises=abrirArchivo("informe")
    pais={}
    indice=paises.items(pais)
    for clave,valor in paises:
        nombre_pais=input("Ingrese el nombre del pais:")
        codigo=input("Ingrese el codigo ISO del pais:")
        codigo3=input("Ingrese el codigo ISO3 del pais:")
        pais_origen=[indice("pais_origen")]
        pais={
            "nombre_pais":nombre_pais,
            "codigo":codigo,
            "codigo3":codigo3,
            "pais_origen":pais
        }
        guardarArchivos("paises",pais)
def musica():
    musica={}
    musica=abrirArchivo("musica")
    for clave,valor in musica:
        indice=musica.index(musica)
        id_genero=input("Ingrese el id del genero:")
        descipcion=input("Ingrese la descripcion del genero:")
        genero_musical=[indice("genero_musical")]
        musica={
            "id_genero":id_genero,
            "id_genero":id_genero,
            "genero_musical":musica
        }
        guardarArchivos("paises",musica)