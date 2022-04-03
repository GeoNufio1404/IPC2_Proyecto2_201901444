import os
from pickle import NONE
from Nodos.NodoListaOrtogonal import NodoListaOrtogonal


class ListaCasillas:
    def __init__(self):
        self.Head = None
        self.Cont = 0
        self.Entradas = 0
        self.UnidadesCiviles = 0
        self.Recursos = 0

    def AgregarCasilla(self, Casilla):
        self.Cont += 1

        NuevoNodo = NodoListaOrtogonal(self.Cont, Casilla)

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

    def ComprobarEntrada(self, IndexEntrada):
        head = self.Head

        while head.Abajo != None:
            while head.Derecha != None:
                if IndexEntrada == head.Index:
                    if head.Clase.Tipo == "Entrada":
                        return True
                    else:
                        return False
                head = head.Derecha 
            if IndexEntrada == head.Index:
                if head.Clase.Tipo == "Entrada":
                    return True
                else:
                    return False
            while head.Izquierda != None:
                head = head.Izquierda
            head = head.Abajo
        while head.Derecha != None:
            if IndexEntrada == head.Index:
                if head.Clase.Tipo == "Entrada":
                    return True
                else:
                    return False
            head = head.Derecha 
        if IndexEntrada == head.Index:
            if head.Clase.Tipo == "Entrada":
                return True
            else:
                return False

    def ListarEntradas(self):
        head = self.Head
        while head.Abajo != None:
            if head.Clase.Tipo == "Entrada":
                print(
                    f"{head.Index}. [{head.Clase.Columna},{head.Clase.Fila}] {head.Clase.Tipo}")
            while head.Derecha != None:
                head = head.Derecha
                if head.Clase.Tipo == "Entrada":
                    print(
                        f"{head.Index}. [{head.Clase.Columna},{head.Clase.Fila}] {head.Clase.Tipo}")
            while head.Izquierda != None:
                head = head.Izquierda
            head = head.Abajo
        if head.Clase.Tipo == "Entrada":
            print(
                f"{head.Index} - [{head.Clase.Columna},{head.Clase.Fila}] {head.Clase.Tipo}")
        while head.Derecha != None:
            head = head.Derecha
            if head.Clase.Tipo == "Entrada":
                print(
                    f"{head.Index} - [{head.Clase.Columna},{head.Clase.Fila}] {head.Clase.Tipo}")

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
            print(
                f"[{head.Clase.Columna},{head.Clase.Fila}] {head.Clase.Tipo} - {head.Clase.Valor}")
            while head.Derecha != None:
                head = head.Derecha
                print(
                    f"[{head.Clase.Columna},{head.Clase.Fila}] {head.Clase.Tipo} - {head.Clase.Valor}")
            while head.Izquierda != None:
                head = head.Izquierda
            head = head.Abajo
        print(
            f"[{head.Clase.Columna},{head.Clase.Fila}] {head.Clase.Tipo} - {head.Clase.Valor}")
        while head.Derecha != None:
            head = head.Derecha
            print(
                f"[{head.Clase.Columna},{head.Clase.Fila}] {head.Clase.Tipo} - {head.Clase.Valor}")

    def GraficarCiudad(self, Titulo):

        head = self.Head
        with open(f"{Titulo}.dot", "w") as Archivo:
            Grid = '''digraph html {
    abc [shape=none, margin=0, label=<
        <TABLE BORDER="0" CELLBORDER="2" CELLSPACING="2" CELLPADDING="15">'''
            Grid += "<TR>"
            while head.Derecha != None:
                if head.Clase.Tipo == "Intransitable":
                    Grid += "<TD bgcolor='black'></TD>"
                elif head.Clase.Tipo == "Transitable":
                    Grid += "<TD bgcolor='white'></TD>"
                elif head.Clase.Tipo == "Camino":
                    Grid += "<TD bgcolor='yellow'></TD>"
                elif head.Clase.Tipo == "Entrada":
                    Grid += "<TD bgcolor='green'></TD>"
                elif head.Clase.Tipo == "Unidad Civil":
                    Grid += "<TD bgcolor='cyan'></TD>"
                elif head.Clase.Tipo == "Recurso":
                    Grid += "<TD bgcolor='gray39'></TD>"
                elif head.Clase.Tipo == "Unidad Militar":
                    Grid += "<TD bgcolor='red'></TD>"
                head = head.Derecha
            if head.Clase.Tipo == "Intransitable":
                Grid += "<TD bgcolor='black'></TD>"
            elif head.Clase.Tipo == "Transitable":
                Grid += "<TD bgcolor='white'></TD>"
            elif head.Clase.Tipo == "Camino":
                Grid += "<TD bgcolor='yellow'></TD>"
            elif head.Clase.Tipo == "Entrada":
                Grid += "<TD bgcolor='green'></TD>"
            elif head.Clase.Tipo == "Unidad Civil":
                Grid += "<TD bgcolor='cyan'></TD>"
            elif head.Clase.Tipo == "Recurso":
                Grid += "<TD bgcolor='gray39'></TD>"
            elif head.Clase.Tipo == "Unidad Militar":
                Grid += "<TD bgcolor='red'></TD>"
            Grid += "</TR>"
            while head.Izquierda != None:
                head = head.Izquierda
            while head.Abajo != None:
                head = head.Abajo
                Grid += "<TR>"
                while head.Derecha != None:
                    if head.Clase.Tipo == "Intransitable":
                        Grid += "<TD bgcolor='black'></TD>"
                    elif head.Clase.Tipo == "Transitable":
                        Grid += "<TD bgcolor='white'></TD>"
                    elif head.Clase.Tipo == "Camino":
                        Grid += "<TD bgcolor='yellow'></TD>"
                    elif head.Clase.Tipo == "Entrada":
                        Grid += "<TD bgcolor='green'></TD>"
                    elif head.Clase.Tipo == "Unidad Civil":
                        Grid += "<TD bgcolor='cyan'></TD>"
                    elif head.Clase.Tipo == "Recurso":
                        Grid += "<TD bgcolor='gray39'></TD>"
                    elif head.Clase.Tipo == "Unidad Militar":
                        Grid += "<TD bgcolor='red'></TD>"
                    head = head.Derecha
                if head.Clase.Tipo == "Intransitable":
                    Grid += "<TD bgcolor='black'></TD>"
                elif head.Clase.Tipo == "Transitable":
                    Grid += "<TD bgcolor='white'></TD>"
                elif head.Clase.Tipo == "Camino":
                    Grid += "<TD bgcolor='yellow'></TD>"
                elif head.Clase.Tipo == "Entrada":
                    Grid += "<TD bgcolor='green'></TD>"
                elif head.Clase.Tipo == "Unidad Civil":
                    Grid += "<TD bgcolor='cyan'></TD>"
                elif head.Clase.Tipo == "Recurso":
                    Grid += "<TD bgcolor='gray39'></TD>"
                elif head.Clase.Tipo == "Unidad Militar":
                    Grid += "<TD bgcolor='red'></TD>"
                Grid += "</TR>"
                while head.Izquierda != None:
                    head = head.Izquierda
            Grid += '''</TABLE>
    >]
}'''
            Archivo.write(Grid)
            Archivo.close()
        os.system(
            f"dot -Tpng {Titulo}.dot -o {Titulo}.png")
        os.remove(f"{Titulo}.dot")
        os.system(f"{Titulo}.png")

    def IrAlNodo(self,IndexEntrada):
        head = self.Head

        while head.Abajo != None:
            while head.Derecha != None:
                if IndexEntrada == head.Index:
                    return head
                head = head.Derecha 
            if IndexEntrada == head.Index:
                return head
            while head.Izquierda != None:
                head = head.Izquierda
            head = head.Abajo
        while head.Derecha != None:
            if IndexEntrada == head.Index:
                return head
            head = head.Derecha 
        if IndexEntrada == head.Index:
            return head

    def CumplirMision(self,IndexEntrada,Robot):
        print(f"{IndexEntrada} Robot: {Robot.Nombre}")
        Nodo = self.IrAlNodo(IndexEntrada)
        print(f"Fila:{Nodo.Clase.Fila} - Columna:{Nodo.Clase.Columna}")
