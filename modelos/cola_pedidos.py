class ColaPedidos:

    def __init__(self):
        self.__elementos = []

    def encolar(self, pedido):
        self.__elementos.append(pedido)

    def desencolar(self):
        if self.esta_vacia():
            return None
        
        return self.__elementos.pop(0)

    def frente(self):
        if self.esta_vacia():
            return None

        return self.__elementos[0]

    def esta_vacia(self):
        return len(self.__elementos) == 0

    def tamanio(self):
        return len(self.__elementos)