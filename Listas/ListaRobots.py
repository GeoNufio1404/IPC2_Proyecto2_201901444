from Nodos.NodoListaSimple import NodoListaSimple


class ListaRobots:
    def __init__(self):
        self.Head = None
        self.ContChapinRescue = 0
        self.ContChapinFighter = 0
        self.Cont = 0

    def AgregarRobot(self, Robot):
        self.Cont += 1

        if Robot.Tipo == "ChapinRescue":
            self.ContChapinRescue += 1
        elif Robot.Tipo == "ChapinFighter":
            self.ContChapinFighter += 1

        NuevoNodo = NodoListaSimple(self.Cont, Robot)
        if not self.Head:
            self.Head = NuevoNodo
        else:
            head = self.Head
            while head.Siguiente != None:
                head = head.Siguiente
            head.Siguiente = NuevoNodo
        return Robot

    def ObtenerUnicoChapinRescue(self):
        head = self.Head
        if head.Clase.Tipo == "ChapinRescue":
            return head.Clase
        else:
            while head.Siguiente != None:
                head = head.Siguiente
                if head.Clase.Tipo == "ChapinRescue":
                    return head.Clase
            return None

    def ObtenerUnicoChapinFighter(self):
        head = self.Head
        if head.Clase.Tipo == "ChapinFighter":
            return head.Clase
        else:
            while head.Siguiente != None:
                head = head.Siguiente
                if head.Clase.Tipo == "ChapinFighter":
                    return head.Clase
            return None

    def ObtenerChapinRescue(self,Pos):
        head = self.Head
        if Pos == head.Index and head.Clase.Tipo == "ChapinRescue":
            return head.Clase
        else:
            while head.Siguiente != None:
                head = head.Siguiente
                if Pos == head.Index and head.Clase.Tipo == "ChapinRescue":
                    return head.Clase
            return None
    
    def ObtenerChapinFighter(self,Pos):
        head = self.Head
        if Pos == head.Index and head.Clase.Tipo == "ChapinFighter":
            return head.Clase
        else:
            while head.Siguiente != None:
                head = head.Siguiente
                if Pos == head.Index and head.Clase.Tipo == "ChapinFighter":
                    return head.Clase
            return None

    def ObtenerRobot(self, Pos):
        head = self.Head
        if Pos == head.Index:
            return head.Clase
        else:
            while head.Siguiente != None:
                head = head.Siguiente
                if Pos == head.Index:
                    return head.Clase
            return None

    def ListarChapinRescues(self):
        head = self.Head
        if head.Clase.Tipo == "ChapinRescue":
            print(
                f"{head.Index}. - Nombre: {head.Clase.Nombre} - Tipo: {head.Clase.Tipo}")
        while head.Siguiente != None:
            head = head.Siguiente
            if head.Clase.Tipo == "ChapinRescue":
                print(
                    f"{head.Index}. - Nombre: {head.Clase.Nombre} - Tipo: {head.Clase.Tipo}")

    def ListarChapinFighter(self):
        head = self.Head
        if head.Clase.Tipo == "ChapinFighter":
            print(
                f"{head.Index}. - Nombre: {head.Clase.Nombre} - Tipo: {head.Clase.Tipo} - Capacidad: {head.Clase.Capacidad}")
        while head.Siguiente != None:
            head = head.Siguiente
            if head.Clase.Tipo == "ChapinFighter":
                print(
                f"{head.Index}. - Nombre: {head.Clase.Nombre} - Tipo: {head.Clase.Tipo} - Capacidad: {head.Clase.Capacidad}")

    def ListarRobots(self):
        head = self.Head
        if head.Clase.Tipo == "ChapinFighter":
            print(
                f"{head.Index}. - Nombre: {head.Clase.Nombre} - Tipo: {head.Clase.Tipo} - Capacidad: {head.Clase.Capacidad}")
        elif head.Clase.Tipo == "ChapinRescue":
            print(
                f"{head.Index}. - Nombre: {head.Clase.Nombre} - Tipo: {head.Clase.Tipo}")
        while head.Siguiente != None:
            head = head.Siguiente
            if head.Clase.Tipo == "ChapinFighter":
                print(
                    f"{head.Index}. - Nombre: {head.Clase.Nombre} - Tipo: {head.Clase.Tipo} - Capacidad: {head.Clase.Capacidad}")
            elif head.Clase.Tipo == "ChapinRescue":
                print(
                    f"{head.Index}. - Nombre: {head.Clase.Nombre} - Tipo: {head.Clase.Tipo}")
