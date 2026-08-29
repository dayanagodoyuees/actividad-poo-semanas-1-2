from modelos.cliente import Cliente


class ClienteFrecuente(Cliente):

    def __init__(self, cedula, nombre, telefono, estado, descuento):
        super().__init__(cedula, nombre, telefono, estado)
        self.__descuento = descuento

    def get_descuento(self):
        return self.__descuento

    def set_descuento(self, descuento):
        self.__descuento = descuento

    def mostrar_datos(self):
        super().mostrar_datos()
        print("Descuento:", self.__descuento, "%")