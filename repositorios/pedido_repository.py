from modelos.cola_pedidos import ColaPedidos

class PedidoRepository:

    def __init__(self):
        self.__cola = ColaPedidos()

    def agregar_pedido(self, pedido):
        self.__cola.encolar(pedido)

    def obtener_siguiente_pedido(self):
        return self.__cola.frente()

    def procesar_siguiente_pedido(self):
        return self.__cola.desencolar()

    def esta_vacio(self):
        return self.__cola.esta_vacia()

    def cantidad_pedidos(self):
        return self.__cola.tamanio()

    