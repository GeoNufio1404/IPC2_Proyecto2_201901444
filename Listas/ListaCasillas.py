from Nodos.NodoListaOrtogonal import NodoListaOrtogonal


class ListaCasillas:
    def __init__(self):
        self.Head = None

    def AgregarCasilla(self, Casilla):
        NuevoNodo = NodoListaOrtogonal(Casilla)
        if not self.Head:
            self.Head = NuevoNodo
        else:
            head = self.Head
            if Casilla.Fila > head.Clase.Fila:
                while head.Abajo != None:
                    head = head.Abajo
                if head.Clase.Columna == Casilla.Columna:
                    head.Abajo = NuevoNodo
                    NuevoNodo.Arriba = head
                else:
                    head2 = head
                    head2 = head2.Arriba
                    while head.Derecha != None:
                        head = head.Derecha
                        head2 = head2.Derecha
                    head2 = head2.Derecha
                    head2.Abajo = NuevoNodo
                    NuevoNodo.Arriba = head2
                    head.Derecha = NuevoNodo
                    NuevoNodo.Izquierda = head
            else:
                while head.Derecha != None:
                    head = head.Derecha
                head.Derecha = NuevoNodo
                NuevoNodo.Izquierda = head

    def BuscarCasilla(self, Fila, Columna):
        head = self.Head
        while head.Clase.Fila != Fila:
            head = head.Abajo
            if head == None:
                return None
        while head.Clase.Columna != Columna:
            head = head.Derecha
            if head == None:
                return None
        return head.Clase
