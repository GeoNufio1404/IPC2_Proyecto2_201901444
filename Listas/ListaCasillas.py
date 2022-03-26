from Nodos.NodoListaOrtogonal import NodoListaOrtogonal


class ListaCasillas:
    def __init__(self):
        self.Head = None
        self.Entradas = 0
        self.UnidadesCiviles = 0
        self.Recursos = 0

    def AgregarCasilla(self, Casilla):

        NuevoNodo = NodoListaOrtogonal(Casilla)

        if Casilla.Tipo == "Entrada":
            self.Entradas += 1
        elif Casilla.Tipo == "Unidad Civil":
            self.UnidadesCiviles += 1
        elif Casilla.Tipo == "Recurso":
            self.Recursos += 1

        if not self.Head:
            self.Head = NuevoNodo
        else:
            head = self.Head
            if head.Clase.Fila == Casilla.Fila:
                while head.Derecha != None:
                    head = head.Derecha
                head.Derecha = NuevoNodo
                NuevoNodo.Izquierda = head
            else:
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
                    head.Derecha = NuevoNodo
                    NuevoNodo.Izquierda = head
                    head2.Abajo = NuevoNodo
                    NuevoNodo.Arriba = head2
        return Casilla

    def ConvertirUnidadMilitar(self, Fila, Columna, Valor):
        head = self.Head
        while head.Clase.Columna != Columna:
            head = head.Derecha
        while head.Clase.Fila != Fila:
            head = head.Abajo
        head.Clase.Tipo = "Unidad Militar"
        head.Clase.Valor = Valor


    def ImprimirCasillas(self):
        head = self.Head
        while head.Abajo != None:
            print(f"[{head.Clase.Columna},{head.Clase.Fila}] {head.Clase.Tipo} - {head.Clase.Valor}")
            while head.Derecha != None:
                head = head.Derecha
                print(f"[{head.Clase.Columna},{head.Clase.Fila}] {head.Clase.Tipo} - {head.Clase.Valor}")
            while head.Izquierda != None:
                head = head.Izquierda
            head = head.Abajo
        print(f"[{head.Clase.Columna},{head.Clase.Fila}] {head.Clase.Tipo} - {head.Clase.Valor}")
        while head.Derecha != None:
            head = head.Derecha
            print(f"[{head.Clase.Columna},{head.Clase.Fila}] {head.Clase.Tipo} - {head.Clase.Valor}")
        


        

