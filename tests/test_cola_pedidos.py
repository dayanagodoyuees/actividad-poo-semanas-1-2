from modelos.cola_pedidos import ColaPedidos

def test_cola_inicia_vacia():
    cola = ColaPedidos()

    assert cola.esta_vacia() is True
    assert cola.tamanio() == 0

def test_encolar_pedidos():
    cola = ColaPedidos()

    cola.encolar("PED001")
    cola.encolar("PED002")

    assert cola.tamanio() == 2
    assert cola.esta_vacia() is False


def test_frente_devuelve_primer_pedido():
    cola = ColaPedidos()

    cola.encolar("PED001")
    cola.encolar("PED002")

    assert cola.frente() == "PED001"
    assert cola.tamanio() == 2


def test_desencolar_respeta_fifo():
    cola = ColaPedidos()

    cola.encolar("PED001")
    cola.encolar("PED002")
    cola.encolar("PED003")

    pedido = cola.desencolar()

    assert pedido == "PED001"
    assert cola.frente() == "PED002"
    assert cola.tamanio() == 2


def test_cola_vacia_devuelve_none():
    cola = ColaPedidos()

    assert cola.frente() is None
    assert cola.desencolar() is None