import os
from Auxiliares import ManejadorXml

def CargarArchivoEntrada():
    Archivo = ManejadorXml.PedirArchivoXml()
    if Archivo != None:
        ManejadorXml.LeerArchivoXml(Archivo)

def MostrarInformacion():
    CiudadSeleccionada = SeleccionarCiudad()
    CiudadSeleccionada.ListaCasillas.GraficarCiudad(CiudadSeleccionada.Nombre)
    print("\n============================================")
    print("====               Robots               ====")
    print("============================================")
    ManejadorXml.ListaRobots.ListarRobots()

def SeleccionarCiudad():
    print("\n============================================")
    print("====              Ciudades              ====")
    print("============================================")
    ManejadorXml.ListaCiudades.ListarCiudades()
    print(
        "Ingrese el numero de la ciudad que desea seleccionar...")
    menu = input(">> ")
    if menu == "":
        menu = 0
    menu = int(menu)
    if menu != 0:
        return ManejadorXml.ListaCiudades.ObtenerCiudad(menu)

def SeleccionarTipoMision():
    print("\n=================================================")
    print("====             Tipo de Mision              ====")
    print("=================================================")
    print("====  1. Mision de rescate                   ====")
    print("====  2. Mision de extraccion de recursos    ====")
    print("=================================================")
    print("\nIngrese el numero de la opcion que desea escoger: \n")
    mision = input(">> ")
    if mision == "" or mision == " ":
        mision = 0
    mision = int(mision)
    if mision == 1:
        if ManejadorXml.ListaRobots.ContChapinRescue > 1:
            print("\n============================================")
            print("====  Robots Disponibles para la mision ====")
            print("============================================")
            ManejadorXml.ListaRobots.ListarChapinRescues()
            print("\nIngrese el numero de la opcion que desea escoger: \n")
            mision = input(">> ")
            if mision == "" or mision == " ":
                mision = 0
            mision = int(mision)
            RobotElegido = ManejadorXml.ListaRobots.ObtenerChapinRescue(mision)
            if RobotElegido != None:
                return RobotElegido
            else:
                print("Robot no encontrado, intente de nuevo...")
        elif ManejadorXml.ListaRobots.ContChapinRescue == 1:
            print("\n============================================")
            print("====     Unico Robot para la mision     ====")
            print("============================================")
            ManejadorXml.ListaRobots.ListarChapinRescues()
            RobotElegido = ManejadorXml.ListaRobots.ObtenerUnicoChapinRescue()
            return RobotElegido
        else:
            print("\n==================================================")
            print("==== No hay ningun ChapinRescue para la mision ====")
            print("===================================================")
    elif mision == 2:
        if ManejadorXml.ListaRobots.ContChapinFighter > 1:
            print("\n============================================")
            print("====  Robots Disponibles para la mision ====")
            print("============================================")
            ManejadorXml.ListaRobots.ListarChapinFighter()
            print("\nIngrese el numero de la opcion que desea escoger: \n")
            mision = input(">> ")
            if mision == "" or mision == " ":
                mision = 0
            mision = int(mision)
            RobotElegido = ManejadorXml.ListaRobots.ObtenerChapinFighter(mision)
            if RobotElegido != None:
                return RobotElegido
            else:
                print("Robot no encontrado, intente de nuevo...")
        elif ManejadorXml.ListaRobots.ContChapinFighter == 1:
            print("\n============================================")
            print("====     Unico Robot para la mision     ====")
            print("============================================")
            ManejadorXml.ListaRobots.ListarChapinFighter()
            RobotElegido = ManejadorXml.ListaRobots.ObtenerUnicoChapinFighter()
            return RobotElegido
        else:
            print("\n===================================================")
            print("==== No hay ningun ChapinFighter para la mision ====")
            print("====================================================")

def SeleccionarEntrada(CiudadElegida):
    print("\n=================================================")
    print("====           Seleccionar Entrada           ====")
    print("=================================================")
    CiudadElegida.ListaCasillas.ListarEntradas()
    print("Ingrese el numero de la entrada que desea seleccionar...")
    IndexEntrada = input(">> ")
    if IndexEntrada == "" or IndexEntrada == " ":
        IndexEntrada = 0
    IndexEntrada = int(IndexEntrada)
    if bool(CiudadElegida.ListaCasillas.ComprobarEntrada(IndexEntrada)):
        return IndexEntrada
    else:
        print("Entrada no disponible...")

def SeleccionarRecurso(CiudadElegida):
    print("\n=================================================")
    print("====           Seleccionar Recurso           ====")
    print("=================================================")
    CiudadElegida.ListaCasillas.ListarRecursos()
    print("Ingrese el numero de el recurso que desea seleccionar...")
    Index = input(">> ")
    if Index == "" or Index == " ":
        Index = 0
    Index = int(Index)
    if bool(CiudadElegida.ListaCasillas.ComprobarRecurso(Index)):
        return Index
    else:
        print("Recurso no disponible...")

def SeleccionarUnidadCivil(CiudadElegida):
    print("\n=================================================")
    print("====         Seleccionar Unidad Civil        ====")
    print("=================================================")
    CiudadElegida.ListaCasillas.ListarUnidadesCiviles()
    print("Ingrese el numero de la Unidad Civil que desea seleccionar...")
    Index = input(">> ")
    if Index == "" or Index == " ":
        Index = 0
    Index = int(Index)
    if bool(CiudadElegida.ListaCasillas.ComprobarUnidadCivil(Index)):
        return Index
    else:
        print("Recurso no disponible...")

def RealizarMision():
    RobotElegido = SeleccionarTipoMision()
    if RobotElegido != None:
        CiudadElegida = SeleccionarCiudad()
        if CiudadElegida != None:
            IndexEntrada = SeleccionarEntrada(CiudadElegida)
            if RobotElegido.Tipo == "ChapinRescue":
                IndexFin = SeleccionarUnidadCivil(CiudadElegida)
                CiudadElegida.ListaCasillas.CumplirMisionUnidadCivil(IndexEntrada,RobotElegido,IndexFin)
            elif RobotElegido.Tipo == "ChapinFighter":
                IndexFin = SeleccionarRecurso(CiudadElegida)
                CiudadElegida.ListaCasillas.CumplirMisionRecursos(IndexEntrada,RobotElegido,IndexFin)
        else:
            print("Ciudad no encontrada, intente de nuevo...")
    else:
        print("Robot no encontrado...")

def MenuPrincipal():
    os.system("cls")
    while (True):
        print("\n============================================")
        print("====           Menu Principal           ====")
        print("============================================")
        print("====  1. Cargar Archivo De Entrada      ====")
        print("====  2. Mostrar Informacion Cargada    ====")
        print("====  3. Realizar una mision            ====")
        print("====  4. Salir                          ====")
        print("============================================")
        print("\nIngrese el numero de la opcion que desea escoger: \n")
        menu = input(">> ")
        if menu == "":
            menu = 0
        menu = int(menu)
        if menu == 1:
            CargarArchivoEntrada()
        elif menu == 2:
            MostrarInformacion()
        elif menu == 3:
            RealizarMision()
        elif menu == 4:
            print("Saliendo de la aplicacion...")
            break
        else:
            print("Comando no reconocido")
        input("Presione Enter para continuar...")

MenuPrincipal()