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

    def ComprobarUnidadCivil(self, Index):
        head = self.Head

        while head.Abajo != None:
            while head.Derecha != None:
                if Index == head.Index:
                    if head.Clase.Tipo == "Unidad Civil":
                        return True
                    else:
                        return False
                head = head.Derecha
            if Index == head.Index:
                if head.Clase.Tipo == "Unidad Civil":
                    return True
                else:
                    return False
            while head.Izquierda != None:
                head = head.Izquierda
            head = head.Abajo
        while head.Derecha != None:
            if Index == head.Index:
                if head.Clase.Tipo == "Unidad Civil":
                    return True
                else:
                    return False
            head = head.Derecha
        if Index == head.Index:
            if head.Clase.Tipo == "Unidad Civil":
                return True
            else:
                return False

    def ListarUnidadesCiviles(self):
        head = self.Head
        while head.Abajo != None:
            if head.Clase.Tipo == "Unidad Civil":
                print(
                    f"{head.Index}. [{head.Clase.Columna},{head.Clase.Fila}] {head.Clase.Tipo}")
            while head.Derecha != None:
                head = head.Derecha
                if head.Clase.Tipo == "Unidad Civil":
                    print(
                        f"{head.Index}. [{head.Clase.Columna},{head.Clase.Fila}] {head.Clase.Tipo}")
            while head.Izquierda != None:
                head = head.Izquierda
            head = head.Abajo
        if head.Clase.Tipo == "Unidad Civil":
            print(
                f"{head.Index}. [{head.Clase.Columna},{head.Clase.Fila}] {head.Clase.Tipo}")
        while head.Derecha != None:
            head = head.Derecha
            if head.Clase.Tipo == "Unidad Civil":
                print(
                    f"{head.Index}. [{head.Clase.Columna},{head.Clase.Fila}] {head.Clase.Tipo}")

    def ComprobarRecurso(self, Index):
        head = self.Head

        while head.Abajo != None:
            while head.Derecha != None:
                if Index == head.Index:
                    if head.Clase.Tipo == "Recurso":
                        return True
                    else:
                        return False
                head = head.Derecha
            if Index == head.Index:
                if head.Clase.Tipo == "Recurso":
                    return True
                else:
                    return False
            while head.Izquierda != None:
                head = head.Izquierda
            head = head.Abajo
        while head.Derecha != None:
            if Index == head.Index:
                if head.Clase.Tipo == "Recurso":
                    return True
                else:
                    return False
            head = head.Derecha
        if Index == head.Index:
            if head.Clase.Tipo == "Recurso":
                return True
            else:
                return False

    def ListarRecursos(self):
        head = self.Head
        while head.Abajo != None:
            if head.Clase.Tipo == "Recurso":
                print(
                    f"{head.Index}. [{head.Clase.Columna},{head.Clase.Fila}] {head.Clase.Tipo}")
            while head.Derecha != None:
                head = head.Derecha
                if head.Clase.Tipo == "Recurso":
                    print(
                        f"{head.Index}. [{head.Clase.Columna},{head.Clase.Fila}] {head.Clase.Tipo}")
            while head.Izquierda != None:
                head = head.Izquierda
            head = head.Abajo
        if head.Clase.Tipo == "Recurso":
            print(
                f"{head.Index}. [{head.Clase.Columna},{head.Clase.Fila}] {head.Clase.Tipo}")
        while head.Derecha != None:
            head = head.Derecha
            if head.Clase.Tipo == "Recurso":
                print(
                    f"{head.Index}. [{head.Clase.Columna},{head.Clase.Fila}] {head.Clase.Tipo}")

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
                f"{head.Index}. [{head.Clase.Columna},{head.Clase.Fila}] {head.Clase.Tipo}")
        while head.Derecha != None:
            head = head.Derecha
            if head.Clase.Tipo == "Entrada":
                print(
                    f"{head.Index}. [{head.Clase.Columna},{head.Clase.Fila}] {head.Clase.Tipo}")

    def ConvertirUnidadMilitar(self, Fila, Columna, Valor):
        head = self.Head
        while head.Clase.Columna != Columna:
            head = head.Derecha
        while head.Clase.Fila != Fila:
            head = head.Abajo
        head.Clase.Tipo = "Unidad Militar"
        head.Clase.Valor = Valor

    def RetornarCasillas(self):
        head = self.Head
        while head.Abajo != None:
            if head.Clase.Tipo == "Camino":
                head.Clase.Tipo = "Transitable"
            elif head.Clase.Tipo == "Camino - Unidad Civil":
                head.Clase.Tipo = "Unidad Civil"
            elif head.Clase.Tipo == "Camino - Entrada":
                head.Clase.Tipo = "Entrada"
            while head.Derecha != None:
                head = head.Derecha
                if head.Clase.Tipo == "Camino":
                    head.Clase.Tipo = "Transitable"
                elif head.Clase.Tipo == "Camino - Unidad Civil":
                    head.Clase.Tipo = "Unidad Civil"
                elif head.Clase.Tipo == "Camino - Entrada":
                    head.Clase.Tipo = "Entrada"
            while head.Izquierda != None:
                head = head.Izquierda
            head = head.Abajo
        if head.Clase.Tipo == "Camino":
            head.Clase.Tipo = "Transitable"
        elif head.Clase.Tipo == "Camino - Unidad Civil":
            head.Clase.Tipo = "Unidad Civil"
        elif head.Clase.Tipo == "Camino - Entrada":
            head.Clase.Tipo = "Entrada"
        while head.Derecha != None:
            head = head.Derecha
            if head.Clase.Tipo == "Camino":
                head.Clase.Tipo = "Transitable"
            elif head.Clase.Tipo == "Camino - Unidad Civil":
                head.Clase.Tipo = "Unidad Civil"
            elif head.Clase.Tipo == "Camino - Entrada":
                head.Clase.Tipo = "Entrada"

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

    def GraficarMision(self, Titulo, Robot):

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
                elif head.Clase.Tipo == "Entrada" or head.Clase.Tipo == "Camino - Entrada":
                    Grid += "<TD bgcolor='green'></TD>"
                elif head.Clase.Tipo == "Unidad Civil" or head.Clase.Tipo == "Camino - Unidad Civil":
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
            elif head.Clase.Tipo == "Entrada" or head.Clase.Tipo == "Camino - Entrada":
                Grid += "<TD bgcolor='green'></TD>"
            elif head.Clase.Tipo == "Unidad Civil" or head.Clase.Tipo == "Camino - Unidad Civil":
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
                    elif head.Clase.Tipo == "Entrada" or head.Clase.Tipo == "Camino - Entrada":
                        Grid += "<TD bgcolor='green'></TD>"
                    elif head.Clase.Tipo == "Unidad Civil" or head.Clase.Tipo == "Camino - Unidad Civil":
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
                elif head.Clase.Tipo == "Entrada" or head.Clase.Tipo == "Camino - Entrada":
                    Grid += "<TD bgcolor='green'></TD>"
                elif head.Clase.Tipo == "Unidad Civil" or head.Clase.Tipo == "Camino - Unidad Civil":
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
    Desc [shape=none, margin=0, label=<
        <TABLE BORDER="0" CELLBORDER="2" CELLSPACING="2" CELLPADDING="15">
            <TR>
                <TD>'''
            if Robot.Tipo == "ChapinRescue":
                Grid += f'Robot: {Robot.Nombre}</TD></TR><TR><TD>Tipo: {Robot.Tipo}'
            elif Robot.Tipo == "ChapinFighter":
                Grid += f'Robot: {Robot.Nombre} </TD></TR><TR><TD>Tipo: {Robot.Tipo}</TD></TR><TR><TD>Capacidad: {Robot.Capacidad}'
            Grid += '''</TD>
            </TR>
        </TABLE>
    >] 
}'''
            Archivo.write(Grid)
            Archivo.close()
        os.system(
            f"dot -Tpng {Titulo}.dot -o {Titulo}.png")
        os.remove(f"{Titulo}.dot")
        os.system(f"{Titulo}.png")

    def ObtenerNodoPorIndex(self, Index):
        head = self.Head

        while head.Abajo != None:
            while head.Derecha != None:
                if Index == head.Index:
                    return head
                head = head.Derecha
            if Index == head.Index:
                return head
            while head.Izquierda != None:
                head = head.Izquierda
            head = head.Abajo
        while head.Derecha != None:
            if Index == head.Index:
                return head
            head = head.Derecha
        if Index == head.Index:
            return head

    def CumplirMisionRecursos(self, IndexEntrada, Robot, IndexFinal):
        NodoInicio = self.ObtenerNodoPorIndex(IndexEntrada)
        NodoFin = self.ObtenerNodoPorIndex(IndexFinal)

    def CumplirMisionUnidadCivil(self, IndexEntrada, Robot, IndexFinal):
        Intentos = 2500
        NodoInicio = self.ObtenerNodoPorIndex(IndexEntrada)
        NodoFin = self.ObtenerNodoPorIndex(IndexFinal)
        while True:
            Intentos -= 1
            NodoInicio = self.AvanzarChapinRescue(NodoInicio)
            if NodoInicio.Index == NodoFin.Index:
                break
            elif Intentos == 0:
                print("Mision Imposible de cumplir...")
                break
        self.GraficarMision(f"[MisionRescate-Fallida]{Robot.Nombre}", Robot)
        self.RetornarCasillas()

    def AvanzarChapinRescue(self, NodoInicio):
        print(
            f"Fila:{NodoInicio.Clase.Fila} - Columna: {NodoInicio.Clase.Columna}")
        if NodoInicio.Arriba != None and NodoInicio.Arriba.Clase.Tipo == "Unidad Civil":
            NodoInicio = NodoInicio.Arriba
            NodoInicio.Clase.Tipo = "Camino - Unidad Civil"
        elif NodoInicio.Derecha != None and NodoInicio.Derecha.Clase.Tipo == "Unidad Civil":
            NodoInicio = NodoInicio.Derecha
            NodoInicio.Clase.Tipo = "Camino - Unidad Civil"
        elif NodoInicio.Abajo != None and NodoInicio.Abajo.Clase.Tipo == "Unidad Civil":
            NodoInicio = NodoInicio.Abajo
            NodoInicio.Clase.Tipo = "Camino - Unidad Civil"
        elif NodoInicio.Izquierda != None and NodoInicio.Izquierda.Clase.Tipo == "Unidad Civil":
            NodoInicio = NodoInicio.Izquierda
            NodoInicio.Clase.Tipo = "Camino - Unidad Civil"
        elif NodoInicio.Arriba != None and NodoInicio.Arriba.Clase.Tipo == "Transitable":
            NodoInicio = NodoInicio.Arriba
            NodoInicio.Clase.Tipo = "Camino"
        elif NodoInicio.Derecha != None and NodoInicio.Derecha.Clase.Tipo == "Transitable":
            NodoInicio = NodoInicio.Derecha
            NodoInicio.Clase.Tipo = "Camino"
        elif NodoInicio.Abajo != None and NodoInicio.Abajo.Clase.Tipo == "Transitable":
            NodoInicio = NodoInicio.Abajo
            NodoInicio.Clase.Tipo = "Camino"
        elif NodoInicio.Izquierda != None and NodoInicio.Izquierda.Clase.Tipo == "Transitable":
            NodoInicio = NodoInicio.Izquierda
            NodoInicio.Clase.Tipo = "Camino"
        elif NodoInicio.Arriba != None and NodoInicio.Arriba.Clase.Tipo == "Entrada":
            NodoInicio = NodoInicio.Arriba
            NodoInicio.Clase.Tipo = "Camino - Entrada"
        elif NodoInicio.Derecha != None and NodoInicio.Derecha.Clase.Tipo == "Entrada":
            NodoInicio = NodoInicio.Derecha
            NodoInicio.Clase.Tipo = "Camino - Entrada"
        elif NodoInicio.Abajo != None and NodoInicio.Abajo.Clase.Tipo == "Entrada":
            NodoInicio = NodoInicio.Abajo
            NodoInicio.Clase.Tipo = "Camino - Entrada"
        elif NodoInicio.Izquierda != None and NodoInicio.Izquierda.Clase.Tipo == "Entrada":
            NodoInicio = NodoInicio.Izquierda
            NodoInicio.Clase.Tipo = "Camino - Entrada"
        elif NodoInicio.Izquierda != None and (NodoInicio.Izquierda.Clase.Tipo == "Camino" or NodoInicio.Izquierda.Clase.Tipo == "Camino - Unidad Civil" or NodoInicio.Izquierda.Clase.Tipo == "Camino - Entrada"):
            NodoInicio = NodoInicio.Izquierda
        elif NodoInicio.Abajo != None and (NodoInicio.Abajo.Clase.Tipo == "Camino" or NodoInicio.Abajo.Clase.Tipo == "Camino - Unidad Civil" or NodoInicio.Abajo.Clase.Tipo == "Camino - Entrada"):
            NodoInicio = NodoInicio.Abajo
        elif NodoInicio.Derecha != None and (NodoInicio.Derecha.Clase.Tipo == "Camino" or NodoInicio.Derecha.Clase.Tipo == "Camino - Unidad Civil" or NodoInicio.Derecha.Clase.Tipo == "Camino - Entrada"):
            NodoInicio = NodoInicio.Derecha
        elif NodoInicio.Arriba != None and (NodoInicio.Arriba.Clase.Tipo == "Camino" or NodoInicio.Arriba.Clase.Tipo == "Camino - Unidad Civil" or NodoInicio.Arriba.Clase.Tipo == "Camino - Entrada"):
            NodoInicio = NodoInicio.Arriba
        return NodoInicio
