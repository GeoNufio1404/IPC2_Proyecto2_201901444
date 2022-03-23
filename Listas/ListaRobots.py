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
        print(f"{head.Index}. - Nombre: {head.Clase.Nombre} - Tipo: {head.Clase.Tipo} - Capacidad: {head.Clase.Capacidad}")
        while head.Siguiente != None:
            head = head.Siguiente
            print(f"{head.Index}. - Nombre: {head.Clase.Nombre} - Tipo: {head.Clase.Tipo} - Capacidad: {head.Clase.Capacidad}")