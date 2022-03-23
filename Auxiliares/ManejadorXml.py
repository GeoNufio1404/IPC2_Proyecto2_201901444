from tkinter.filedialog import askopenfilename
from xml.dom import minidom
from tkinter import Tk


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
    Configuracion = Archivo.getElementsByTagName("configuracion")[0]
    ListaCiudades = Configuracion.getElementsByTagName("listaCiudades")[0]
    Ciudades = ListaCiudades.getElementsByTagName("ciudad")
    for Ciudad in Ciudades:
        Nombre = Ciudad.getElementsByTagName("nombre")[0]
        CantidadFilas = Nombre.getAttribute("filas")
        CantidadColumnas = Nombre.getAttribute("columnas")
        print(
            f"Nombre: {Nombre.firstChild.data} - Filas: {CantidadFilas} - Columnas: {CantidadColumnas}")
        Filas = Ciudad.getElementsByTagName("fila")
        for Fila in Filas:
            NumFila = Fila.getAttribute("numero")
            print(f"Numero: {NumFila} - Fila: {Fila.firstChild.data}")
        UnidadesMilitares = Ciudad.getElementsByTagName("unidadMilitar")
        for UnidadMilitar in UnidadesMilitares:
            FilaMilitar = UnidadMilitar.getAttribute("fila")
            ColumnaMilitar = UnidadMilitar.getAttribute("columna")
            print(f"Unidad militar - Valor: {UnidadMilitar.firstChild.data} - Fila: {FilaMilitar} - Columna: {ColumnaMilitar}")
    ListaRobots = Configuracion.getElementsByTagName("robots")[0]
    Robots = ListaRobots.getElementsByTagName("robot")
    for Robot in Robots:
        NombreRobot = Robot.getElementsByTagName("nombre")[0]
        TipoRobot = NombreRobot.getAttribute("tipo")
        if str(TipoRobot) == "ChapinFighter":
            CapacidadRobot = NombreRobot.getAttribute("capacidad")
            print(f"Nombre Robot: {NombreRobot.firstChild.data} - Tipo: {TipoRobot} - Capacidad: {CapacidadRobot}")
        else: 
            print(f"Nombre Robot: {NombreRobot.firstChild.data} - Tipo: {TipoRobot}")
