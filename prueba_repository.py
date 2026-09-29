from repositorios.pedido_repository  import PedidoRepository

repository = PedidoRepository()

print("¿Repository vacío?", repository.esta_vacio())

repository.agregar_pedido("PED001")
repository.agregar_pedido("PED002")
repository.agregar_pedido("PED003")

print("\nDespués de agregar pedidos:")
print("Cantidad:", repository.cantidad_pedidos())
print("Siguiente pedido:", repository.obtener_siguiente_pedido())

pedido_procesado = repository.procesar_siguiente_pedido()

print("\nPedido procesado:", pedido_procesado)
print("Nuevo siguiente:", repository.obtener_siguiente_pedido())
print("Cantidad restante:", repository.cantidad_pedidos())