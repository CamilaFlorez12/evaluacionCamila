import json
def abrirArchivo(archivo):
    with open(f"{archivo}.json","r") as archivoAbrir:
        musica = json.load(archivoAbrir)
    return musica
def guardarArchivos(archivo,diccionario):
    objetoJson=json.dumps(diccionario,indent=4)
    with open(f"{archivo}.json","w") as archivoAbrir:
        archivoAbrir.write(objetoJson)
