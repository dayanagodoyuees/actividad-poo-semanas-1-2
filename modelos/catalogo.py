from modelos.producto import Producto


class Catalogo:

    def __init__(self):
        self.__productos: list[Producto] = []
        self.__productos_por_codigo: dict[str, Producto] = {}
        self.__codigos: set[str] = set()

    def agregar_producto(self, producto):
        codigo = producto.get_codigo()

        if codigo in self.__codigos:
            return False

        self.__productos.append(producto)
        self.__productos_por_codigo[codigo] = producto
        self.__codigos.add(codigo)

        return True

    def buscar_producto(self, codigo):
        return self.__productos_por_codigo.get(codigo)

    def listar_productos(self):
        return self.__productos.copy()

    def actualizar_producto(self, codigo, nombre, precio, stock):
        producto = self.buscar_producto(codigo)

        if producto is None:
            return False

        producto.set_nombre(nombre)
        producto.set_precio(precio)
        producto.set_stock(stock)

        return True

    def eliminar_producto(self, codigo):
        producto = self.buscar_producto(codigo)

        if producto is None:
            return False

        self.__productos.remove(producto)
        del self.__productos_por_codigo[codigo]
        self.__codigos.remove(codigo)

        return True