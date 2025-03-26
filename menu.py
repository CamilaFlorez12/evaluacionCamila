from data import*
from artistas import*
from paises import*
menu_principal="""
Bienvenido al menu principal
1.Registrar datos de artistas musicales
2.Registro de informacion de los paises
3.Registro generos musicales
4.Salir
"""
menu_registrar_artistas="""
Bienvenido al registro de artistas
1.Registrar artistas
2.Gestionar informacion
3.Salir
"""
menu_paises="""
Bienvenido al registro de paises
1.Registrar pais
2.Gestionar informcion
3.Salir
"""
menu_musica="""
Bienvenido al registro de generos musicales
1.Registrar informcaion del genero
2.Gestionar informcion
3.Salir 
"""
def pedir_opc():
    return input("Ingrese una opcion")

def registrar_artistas():
    print(menu_registrar_artistas)
    opc=pedir_opc()
    if opc=="1":
        informacion()
    if opc=="2":
        pasises()
    if opc=="3":
        input("press Enter---------")
        
    else:
        print("Ingres euna opcion valida")
registrar_artistas()