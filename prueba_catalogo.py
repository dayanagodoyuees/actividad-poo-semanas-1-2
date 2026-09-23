from modelos.catalogo import Catalogo
from modelos.producto import Producto

catalogo = Catalogo()

producto1 = Producto("P001", "Teclado", 25.50, 10)
producto2 = Producto("P002", "Mouse", 15.50, 20)
producto3 = Producto("P003", "Monitor", 180.50, 5)



print("AGREGAR PRODUCTOS")

print(catalogo.agregar_producto(producto1))
print(catalogo.agregar_producto(producto2))
print(catalogo.agregar_producto(producto3))

producto_duplicado = Producto("P001", "Otro teclado", 30.00, 5)

print("\nINTENTO DE PRODUCTO DUPLICADO")
print(catalogo.agregar_producto(producto_duplicado))


print("\nBUSCAR PRODUCTO")

producto_encontrado = catalogo.buscar_producto("P002")

if producto_encontrado is not None:
    print("Producto encontrado:")
    producto_encontrado.mostrar_datos()

else:
    print("Producto no encontrado")

print("\nLISTAR PRODUCTOS")

for producto in catalogo.listar_productos():
    producto.mostrar_datos()
    print("--------------------")


print("\nACTUALIZAR PRODUCTO")

resultado = catalogo.actualizar_producto(
    "P002",
    "Mouse inalámbrico",
    22.50,
    15
)

print("¿Se actualizó?", resultado)

producto_actualizado = catalogo.buscar_producto("P002")

if producto_actualizado is not None:
    producto_actualizado.mostrar_datos()


print("\nELIMINAR PRODUCTO")

resultado = catalogo.eliminar_producto("P001")

print("¿Se eliminó?", resultado)

print("\nPRODUCTOS DESPUÉS DE ELIMINAR")

for producto in catalogo.listar_productos():
    producto.mostrar_datos()
    print("--------------------")