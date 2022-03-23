import os
from Auxiliares import ManejadorXml

os.system("cls")
while (True):
    print("\n============================================")
    print("====           Menu Principal           ====")
    print("============================================")
    print("====  1. Cargar Archivo De Entrada      ====")
    print("====  2.  ====")
    print("====  3.       ====")
    print("====  4. Salir                          ====")
    print("============================================")
    print("\nIngrese el numero de la opcion que desea escoger: \n")
    menu = input(">> ")
    if menu == "":
        menu = 0
    menu = int(menu)
    if menu == 1:
        Archivo = ManejadorXml.PedirArchivoXml()
        if Archivo != None:
            ManejadorXml.LeerArchivoXml(Archivo)
    elif menu == 2:
        pass
    elif menu == 3:
        pass
    elif menu == 4:
        print("Saliendo de la aplicacion...")
        break
    else:
        print("Comando no reconocido")
    input("Presione Enter para continuar...")
