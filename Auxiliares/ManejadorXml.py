from tkinter.filedialog import askopenfilename
from xml.dom import minidom
from tkinter import Tk

from Clases.ClaseCiudad import Ciudad
from Clases.ClaseCasilla import Casilla
from Clases.ClaseChapinFighter import ChapinFighter
from Clases.ClaseChapinRescue import ChapinRescue

from Listas.ListaCiudades import ListaCiudades
from Listas.ListaRobots import ListaRobots

ListaCiudades = ListaCiudades()
ListaRobots = ListaRobots()


def PedirArchivoXml():
    Tk().withdraw()
    try:
        print("Seleccione un archivo en el explorador...")
        Archivo = askopenfilename(filetypes=[("Xml Files", "*.xml")])
        return Archivo
    except:
        print("Error al seleccionar el archivo...")
        return None


def LeerArchivoXml(Archivo):
    Archivo = minidom.parse(Archivo)
    Configuracion_Xml = Archivo.getElementsByTagName("configuracion")[0]
    ListaCiudades_Xml = Configuracion_Xml.getElementsByTagName("listaCiudades")[
        0]
    Ciudades_Xml = ListaCiudades_Xml.getElementsByTagName("ciudad")
    for Ciudad_Xml in Ciudades_Xml:
        Nombre_Xml = Ciudad_Xml.getElementsByTagName("nombre")[0]
        CantidadFilas_Xml = Nombre_Xml.getAttribute("filas")
        CantidadColumnas_Xml = Nombre_Xml.getAttribute("columnas")

        # Agregar Ciudades
        CiudadAgregada = ListaCiudades.AgregarCiudad(
            Ciudad(str(Nombre_Xml.firstChild.data), int(CantidadFilas_Xml), int(CantidadColumnas_Xml)))

        Filas_Xml = Ciudad_Xml.getElementsByTagName("fila")
        for Fila_Xml in Filas_Xml:
            NumFila_Xml = Fila_Xml.getAttribute("numero")

            # Agregar Casillas
            AgregarCasillas(CiudadAgregada, int(NumFila_Xml),
                            str(Fila_Xml.firstChild.data))

        UnidadesMilitares_Xml = Ciudad_Xml.getElementsByTagName(
            "unidadMilitar")
        for UnidadMilitar_Xml in UnidadesMilitares_Xml:
            FilaMilitar_Xml = UnidadMilitar_Xml.getAttribute("fila")
            ColumnaMilitar_Xml = UnidadMilitar_Xml.getAttribute("columna")

            CiudadAgregada.ListaCasillas.ConvertirUnidadMilitar(int(FilaMilitar_Xml), int(ColumnaMilitar_Xml), UnidadMilitar_Xml.firstChild.data)
            
    ListaRobots_Xml = Configuracion_Xml.getElementsByTagName("robots")[0]
    Robots_Xml = ListaRobots_Xml.getElementsByTagName("robot")
    for Robot_Xml in Robots_Xml:
        NombreRobot_Xml = Robot_Xml.getElementsByTagName("nombre")[0]
        TipoRobot_Xml = NombreRobot_Xml.getAttribute("tipo")
        if str(TipoRobot_Xml) == "ChapinFighter":
            CapacidadRobot_Xml = NombreRobot_Xml.getAttribute("capacidad")
            ListaRobots.AgregarRobot(ChapinFighter(
                NombreRobot_Xml.firstChild.data, TipoRobot_Xml, int(CapacidadRobot_Xml)))
        else:
            ListaRobots.AgregarRobot(ChapinRescue(
                NombreRobot_Xml.firstChild.data, TipoRobot_Xml))


def AgregarCasillas(Ciudad, Fila, Cadena):
    ContColumna = 0
    for Caracter in Cadena:
        if Caracter != '"':
            ContColumna += 1
            if Caracter == "*":
                Ciudad.ListaCasillas.AgregarCasilla(
                    Casilla(Fila, ContColumna, "Intransitable", 0))
            elif Caracter == " ":
                Ciudad.ListaCasillas.AgregarCasilla(
                    Casilla(Fila, ContColumna, "Transitable", 0))
            elif Caracter == "E":
                Ciudad.ListaCasillas.AgregarCasilla(
                    Casilla(Fila, ContColumna, "Entrada", 0))
            elif Caracter == "C":
                Ciudad.ListaCasillas.AgregarCasilla(
                    Casilla(Fila, ContColumna, "Unidad Civil", 0))
            elif Caracter == "R":
                Ciudad.ListaCasillas.AgregarCasilla(
                    Casilla(Fila, ContColumna, "Recurso", 0))
