from modelos.cliente_frecuente import ClienteFrecuente
from modelos.producto import Producto
from modelos.producto_digital import ProductoDigital
from modelos.detalle_pedido import DetallePedido
from modelos.pedido import Pedido


cliente1 = ClienteFrecuente(
    "1002",
    "Juan Pérez",
    "0982222222",
    "Activo",
    10
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


pedido1 = Pedido(
    "PED001",
    "22/08/2026",
    cliente1
)


pedido1.agregar_detalle(detalle1)
pedido1.agregar_detalle(detalle2)


pedido1.mostrar_pedido()