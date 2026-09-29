from modelos.cola_pedidos import ColaPedidos

cola = ColaPedidos()

print("¿La cola está vacía?", cola.esta_vacia())
print("Cantidad incial:", cola.tamanio())

cola.encolar("PED001")
cola.encolar("PED002")
cola.encolar("PED003")

print("\nDespués de agregar tres pedidos:")
print("Cantidad:", cola.tamanio())
print("Siguiente pedido:", cola.frente())

pedido_procesado = cola.desencolar()

print("\nPedido procesado:", pedido_procesado)
print("Nuevo siguiente pedido:", cola.frente())
print("Cantidad restante:", cola.tamanio())