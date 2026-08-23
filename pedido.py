class Pedido:

    def __init__(self, numero, fecha, cliente):
        self.__numero = numero
        self.__fecha = fecha
        self.__cliente = cliente
        self.__detalles = []

    def get_numero(self):
        return self.__numero

    def get_fecha(self):
        return self.__fecha

    def get_cliente(self):
        return self.__cliente

    def get_detalles(self):
        return self.__detalles

    def set_fecha(self, fecha):
        self.__fecha = fecha

    def agregar_detalle(self, detalle):
        self.__detalles.append(detalle)

    def mostrar_pedido(self):
        print("Número de pedido:", self.__numero)
        print("Fecha:", self.__fecha)

        print("\nCLIENTE")
        self.__cliente.mostrar_datos()

        print("\nDETALLES DEL PEDIDO")

        for detalle in self.__detalles:
            producto = detalle.get_producto()

            print("Producto:", producto.get_nombre())
            print("Cantidad:", detalle.get_cantidad())
            print("Precio unitario:", detalle.get_precio_unitario())
            print("Subtotal:", detalle.calcular_subtotal())
            print()