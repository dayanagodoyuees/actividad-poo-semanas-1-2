import flet as ft

from modelos.catalogo import Catalogo
from modelos.producto import Producto


def main(page: ft.Page):
    page.title = "Catálogo de Productos"

    catalogo = Catalogo()

    titulo = ft.Text(
        "Catálogo de Productos",
        size=24,
        weight=ft.FontWeight.BOLD
    )

    codigo = ft.TextField(label="Código")
    nombre = ft.TextField(label="Nombre")
    precio = ft.TextField(label="Precio")
    stock = ft.TextField(label="Stock")

    mensaje = ft.Text("")
    lista_productos = ft.Column()

    def agregar(e):
        codigo_ingresado = codigo.value
        nombre_ingresado = nombre.value
        precio_ingresado = precio.value
        stock_ingresado = stock.value

        if not codigo_ingresado or not nombre_ingresado or not precio_ingresado or not stock_ingresado:
            mensaje.value = "Todos los campos son obligatorios"
            page.update()
            return

        try:
            precio_numero = float(precio_ingresado)
            stock_numero = int(stock_ingresado)
        except ValueError:
            mensaje.value = "Precio y stock deben ser números"
            page.update()
            return

        if precio_numero < 0 or stock_numero < 0:
            mensaje.value = "Precio y stock no pueden ser negativos"
            page.update()
            return

        producto = Producto(
            codigo_ingresado,
            nombre_ingresado,
            precio_numero,
            stock_numero
        )

        resultado = catalogo.agregar_producto(producto)

        if resultado:
            mensaje.value = "Producto agregado correctamente"

            codigo.value = ""
            nombre.value = ""
            precio.value = ""
            stock.value = ""
        else:
            mensaje.value = "Ya existe un producto con ese código"

        page.update()

    def consultar(e):
        codigo_ingresado = codigo.value

        if not codigo_ingresado:
            mensaje.value = "Ingrese un código para buscar"
            page.update()
            return

        producto = catalogo.buscar_producto(codigo_ingresado)

        if producto is None:
            mensaje.value = "Producto no encontrado"
        else:
            nombre.value = producto.get_nombre()
            precio.value = str(producto.get_precio())
            stock.value = str(producto.get_stock())
            mensaje.value = "Producto encontrado"

        page.update()

    def actualizar(e):
        codigo_ingresado = codigo.value
        nombre_ingresado = nombre.value
        precio_ingresado = precio.value
        stock_ingresado = stock.value

        if not codigo_ingresado or not nombre_ingresado or not precio_ingresado or not stock_ingresado:
            mensaje.value = "Todos los campos son obligatorios"
            page.update()
            return

        try:
            precio_numero = float(precio_ingresado)
            stock_numero = int(stock_ingresado)
        except ValueError:
            mensaje.value = "Precio y stock deben ser números"
            page.update()
            return

        if precio_numero < 0 or stock_numero < 0:
            mensaje.value = "Precio y stock no pueden ser negativos"
            page.update()
            return

        resultado = catalogo.actualizar_producto(
            codigo_ingresado,
            nombre_ingresado,
            precio_numero,
            stock_numero
        )

        if resultado:
            mensaje.value = "Producto actualizado correctamente"
        else:
            mensaje.value = "Producto no encontrado"

        page.update()

    def eliminar(e):
        codigo_ingresado = codigo.value

        if not codigo_ingresado:
            mensaje.value = "Ingrese un código para eliminar"
            page.update()
            return

        resultado = catalogo.eliminar_producto(codigo_ingresado)

        if resultado:
            mensaje.value = "Producto eliminado correctamente"

            codigo.value = ""
            nombre.value = ""
            precio.value = ""
            stock.value = ""
        else:
            mensaje.value = "Producto no encontrado"

        page.update()

    def listar(e):
        lista_productos.controls.clear()

        productos = catalogo.listar_productos()

        if not productos:
            lista_productos.controls.append(
                ft.Text("No hay productos registrados")
            )
        else:
            for producto in productos:
                lista_productos.controls.append(
                    ft.Text(
                        f"{producto.get_codigo()} | "
                        f"{producto.get_nombre()} | "
                        f"${producto.get_precio()} | "
                        f"Stock: {producto.get_stock()}"
                    )
                )

        page.update()

    boton_agregar = ft.ElevatedButton(
        "Agregar",
        on_click=agregar
    )

    boton_consultar = ft.ElevatedButton(
        "Consultar",
        on_click=consultar
    )

    boton_actualizar = ft.ElevatedButton(
        "Actualizar",
        on_click=actualizar
    )

    boton_eliminar = ft.ElevatedButton(
        "Eliminar",
        on_click=eliminar
    )

    boton_listar = ft.ElevatedButton(
        "Listar",
        on_click=listar
    )

    fila_botones = ft.Row(
        [
            boton_agregar,
            boton_consultar,
            boton_actualizar,
            boton_eliminar,
            boton_listar
        ]
    )

    subtitulo_lista = ft.Text(
        "Productos registrados",
        size=18,
        weight=ft.FontWeight.BOLD
    )

    page.add(
        titulo,
        codigo,
        nombre,
        precio,
        stock,
        fila_botones,
        mensaje,
        subtitulo_lista,
        lista_productos
    )


ft.app(target=main)