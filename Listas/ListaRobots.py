from Nodos.NodoListaSimple import NodoListaSimple

class ListaRobots:
    def __init__(self):
        self.Head = None
        self.Cont = 0

    def AgregarRobot(self,Robot):
        self.Cont += 1
        NuevoNodo = NodoListaSimple(self.Cont,Robot)
        if not self.Head:
            self.Head = NuevoNodo
        else:
            head = self.Head
            while head.Siguiente != None:
                head = head.Siguiente
            head.Siguiente = NuevoNodo
        return Robot

    def ListarRobots(self):
        head = self.Head
        if head.Clase.Tipo == "ChapinFighter":
            print(f"{head.Index}. - Nombre: {head.Clase.Nombre} - Tipo: {head.Clase.Tipo} - Capacidad: {head.Clase.Capacidad}")
        elif head.Clase.Tipo == "ChapinRescue":
            print(f"{head.Index}. - Nombre: {head.Clase.Nombre} - Tipo: {head.Clase.Tipo}")   
        while head.Siguiente != None:
            head = head.Siguiente
            if head.Clase.Tipo == "ChapinFighter":
                print(f"{head.Index}. - Nombre: {head.Clase.Nombre} - Tipo: {head.Clase.Tipo} - Capacidad: {head.Clase.Capacidad}")
            elif head.Clase.Tipo == "ChapinRescue":
                print(f"{head.Index}. - Nombre: {head.Clase.Nombre} - Tipo: {head.Clase.Tipo}")