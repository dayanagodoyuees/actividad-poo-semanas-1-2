from modelos.cliente import Cliente

class ClienteMayorista(Cliente):

    def __init__(self, cedula, nombre, telefono, estado):
        super().__init__(cedula, nombre, telefono, estado)

    def calcularDescuento(self, total):
        return total * 0.15