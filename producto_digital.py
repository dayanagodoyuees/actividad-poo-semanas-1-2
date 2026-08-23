from producto import Producto


class ProductoDigital(Producto):

    def __init__(self, codigo, nombre, precio, stock, formato):
        super().__init__(codigo, nombre, precio, stock)
        self.__formato = formato

    def get_formato(self):
        return self.__formato

    def set_formato(self, formato):
        self.__formato = formato

    def mostrar_datos(self):
        super().mostrar_datos()
        print("Formato:", self.__formato)