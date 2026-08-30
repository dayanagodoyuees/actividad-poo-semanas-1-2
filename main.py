from modelos.cliente_mayorista import ClienteMayorista
from modelos.cliente_minorista import ClienteMinorista
from modelos.producto import Producto
from modelos.producto_digital import ProductoDigital
from modelos.detalle_pedido import DetallePedido
from modelos.pedido import Pedido


cliente_mayorista = ClienteMayorista(
    "1001",
    "Ana Torres",
    "0991111111",
    "Activo"
)


cliente_minorista = ClienteMinorista(
    "1002",
    "Luis Pérez",
    "0982222222",
    "Activo"
)


producto1 = Producto(
    "P001",
    "Teclado",
    25.50,
    10
)


producto2 = ProductoDigital(
    "P002",
    "Curso de Python",
    30.00,
    100,
    "PDF"
)


detalle1 = DetallePedido(
    producto1,
    2,
    producto1.get_precio()
)


detalle2 = DetallePedido(
    producto2,
    1,
    producto2.get_precio()
)


pedido_mayorista = Pedido(
    "PED001",
    "29/08/2026",
    cliente_mayorista
)

pedido_mayorista.agregar_detalle(detalle1)
pedido_mayorista.agregar_detalle(detalle2)


pedido_minorista = Pedido(
    "PED002",
    "29/08/2026",
    cliente_minorista
)

pedido_minorista.agregar_detalle(detalle1)
pedido_minorista.agregar_detalle(detalle2)


print("PEDIDO CLIENTE MAYORISTA")
pedido_mayorista.mostrar_pedido()

print("\n------------------------------\n")

print("PEDIDO CLIENTE MINORISTA")
pedido_minorista.mostrar_pedido()