from Listas.ListaCasillas import ListaCasillas


class Ciudad:
    def __init__(self, Nombre, Filas, Columnas):
        self.Nombre = Nombre
        self.Filas = Filas
        self.Columnas = Columnas
        self.ListaCasillas = ListaCasillas()
