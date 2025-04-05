from data import*
from artistas import*
from paises import*
from genero_musical import*
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
2.Editar informacion
3.Eliminar artista
4.Salir
"""
menu_paises="""
Bienvenido al registro de paises
1.Registrar pais
2.Editar informacion
3.Eliminar pais
4.Salir
"""
menu_musica="""
Bienvenido al registro de generos musicales
1.Registrar informcaion del genero
2.Editar informacion
3.Eliminar genero
4.Salir
"""
def mostrar_menu():
    print(menu_principal)
def pedir_opc():
    return input("Ingrese una opcion")

def registrar_artistas():
    while True:
        try:
            print(menu_registrar_artistas)
            opc=pedir_opc()
            if opc=="1":
                informacion()
            elif opc=="2":
                editar_informacion()
            elif opc=="3":
                eliminar_artista()
            elif opc=="4":
                input("Presione enter.......")
                break
            else:
                print("Ingres euna opcion valida")
        except Exception:
            print("ERROR")
def registrar_paises():
    while True:
        try:
            print(menu_paises)
            opc=pedir_opc()
            if opc=="1":
                paises()
            elif opc=="2":
                editar_pais()
            elif opc=="3":
                eliminar_pais()
            elif opc=="4":
                input("Presione enter........")
                break
            else:
                print("Ingres euna opcion valida")
        except Exception:
            print("ERROR")
def genero_musical():
    while True:
        try:
            print(menu_musica)
            opc=pedir_opc()
            if opc=="1":
                genero_musica()
            elif opc=="2":
                editar_genero()
            elif opc=="3":
                eliminar_genero() 
            elif opc=="4":
                input("Presione Enter.......")
                break
            else:
                print("Ingres euna opcion valida")
        except Exception:
            print("ERROR")
def funcion():
    print("BIENVENIDO AL SISTEMA DE REGISTRO DE ARTISTAS MUSICALES")
    while True:
        mostrar_menu()
        try:
            opc=pedir_opc()
            if opc=="1":
                        registrar_artistas()
            elif opc=="2":
                        registrar_paises()
            elif opc=="3":
                        genero_musical()
            elif opc=="4":
                        print("QUE TENGAS UN LINDO DIA!!!")
                        input("Press Enter.......")
                        break
            else:
                        print("Ingrese una opcion valida")
        except Exception:
            print("ERROR")
funcion()