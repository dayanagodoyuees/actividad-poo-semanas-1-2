import json

from modelos.producto import Producto


class ProductoRepository:

    def __init__(self, archivo="datos/productos.json"):
        self.__archivo = archivo

    def guardar_productos(self, productos):
        datos = []

        for producto in productos:
            datos.append({
                "codigo": producto.get_codigo(),
                "nombre": producto.get_nombre(),
                "precio": producto.get_precio(),
                "stock": producto.get_stock()
            })

        with open(self.__archivo, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)

    def cargar_productos(self):
        try:
            with open(self.__archivo, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)

            productos = []

            for dato in datos:
                producto = Producto(
                    dato["codigo"],
                    dato["nombre"],
                    dato["precio"],
                    dato["stock"]
                )

                productos.append(producto)

            return productos

        except (FileNotFoundError, json.JSONDecodeError):
            return []