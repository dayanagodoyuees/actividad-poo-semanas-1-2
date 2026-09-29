from repositorios.pedido_repository import PedidoRepository


def test_repository_inicia_vacio():
    repository = PedidoRepository()

    assert repository.esta_vacio() is True
    assert repository.cantidad_pedidos() == 0

def test_agregar_pedidos_repository():
    repository = PedidoRepository()

    repository.agregar_pedido("PED001")
    repository.agregar_pedido("PED002")

    assert repository.cantidad_pedidos() == 2
    assert repository.esta_vacio() is False


def test_obtener_siguiente_pedido_repository():
    repository = PedidoRepository()

    repository.agregar_pedido("PED001")
    repository.agregar_pedido("PED002")

    assert repository.obtener_siguiente_pedido() == "PED001"
    assert repository.cantidad_pedidos() == 2


def test_procesar_pedidos_repository_respeta_fifo():
    repository = PedidoRepository()

    repository.agregar_pedido("PED001")
    repository.agregar_pedido("PED002")
    repository.agregar_pedido("PED003")

    pedido_procesado = repository.procesar_siguiente_pedido()

    assert pedido_procesado == "PED001"
    assert repository.obtener_siguiente_pedido() == "PED002"
    assert repository.cantidad_pedidos() == 2