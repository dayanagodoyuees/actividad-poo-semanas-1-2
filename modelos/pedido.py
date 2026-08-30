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

    def calcular_total(self):
        total = 0

        for detalle in self.__detalles:
            total += detalle.calcular_subtotal()

        return total

    def calcular_total_con_descuento(self):
        total = self.calcular_total()

        descuento = self.__cliente.calcularDescuento(total)

        return total - descuento

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

        total = self.calcular_total()
        descuento = self.__cliente.calcularDescuento(total)
        total_final = self.calcular_total_con_descuento()

        print("Total:", total)
        print("Descuento:", descuento)
        print("Total final:", total_final)