from Nodos.NodoListaSimple import NodoListaSimple

class ListaCiudades:
    def __init__(self):
        self.Head = None
        self.Cont = 0

    def AgregarCiudad(self,Ciudad):
        self.Cont += 1
        NuevoNodo = NodoListaSimple(self.Cont,Ciudad)
        if not self.Head:
            self.Head = NuevoNodo
        else:
            head = self.Head
            while head.Siguiente != None:
                head = head.Siguiente
            head.Siguiente = NuevoNodo
        return Ciudad

    def ListarCiudades(self):
        head = self.Head
        print(f"{head.Index}. - Nombre: {head.Clase.Nombre} - Filas: {head.Clase.Filas} - Columnas: {head.Clase.Columnas}")
        head.Clase.ListaCasillas.ImprimirCasillas()
        while head.Siguiente != None:
            head = head.Siguiente
            print(f"{head.Index}. - Nombre: {head.Clase.Nombre} - Filas: {head.Clase.Filas} - Columnas: {head.Clase.Columnas}")
            head.Clase.ListaCasillas.ImprimirCasillas()
