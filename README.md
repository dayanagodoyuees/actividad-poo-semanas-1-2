# Sistema de Pedidos y Catálogo de Productos - Programación Orientada a Objetos

## Descripción

Este proyecto fue desarrollado en Python como parte de las actividades de Programación Orientada a Objetos.

Durante las primeras semanas se desarrolló un sistema de pedidos utilizando clases como Cliente, Producto, Pedido y DetallePedido, aplicando conceptos de encapsulación, herencia, composición, clases abstractas y polimorfismo.

En las semanas 5 y 6 se amplió el proyecto mediante la implementación de un catálogo de productos utilizando colecciones de Python y una interfaz gráfica desarrollada con Flet.

El catálogo permite agregar, consultar, listar, actualizar y eliminar productos mediante una interfaz gráfica.

## Objetivo

Aplicar de forma práctica los conceptos de Programación Orientada a Objetos, colecciones, operaciones CRUD, interfaz gráfica y manejo de eventos mediante el desarrollo de un sistema de pedidos y un catálogo de productos.

## Funcionalidades principales

- Crear clientes mayoristas y minoristas.
- Crear productos normales y productos digitales.
- Crear pedidos asociados a un cliente.
- Agregar productos a un pedido.
- Calcular subtotales y el total de un pedido.
- Aplicar descuentos según el tipo de cliente.
- Administrar un catálogo de productos.
- Agregar productos al catálogo.
- Consultar productos mediante su código.
- Listar los productos registrados.
- Actualizar nombre, precio y stock de un producto.
- Eliminar productos.
- Evitar códigos de productos duplicados.
- Validar los datos ingresados por el usuario.
- Mostrar mensajes de éxito o error.
- Realizar las operaciones CRUD desde una interfaz gráfica desarrollada con Flet.

## Colecciones utilizadas

Para administrar el catálogo se utilizaron tres tipos de colecciones de Python:

- `list`: almacena los objetos de tipo `Producto` y permite recorrer y listar los productos registrados.
- `dict`: relaciona el código de cada producto con su objeto correspondiente y permite realizar búsquedas por código.
- `set`: almacena los códigos registrados y permite controlar que no existan códigos duplicados.

Las colecciones se encuentran definidas de la siguiente manera:

```python
self.__productos: list[Producto] = []
self.__productos_por_codigo: dict[str, Producto] = {}
self.__codigos: set[str] = set()
```

## Operaciones CRUD

El catálogo implementa las siguientes operaciones:

- **Create:** agregar un nuevo producto.
- **Read:** consultar un producto por código y listar los productos registrados.
- **Update:** actualizar los datos de un producto existente.
- **Delete:** eliminar un producto del catálogo.

## Interfaz gráfica

La interfaz gráfica fue desarrollada utilizando Flet.

La aplicación contiene campos para ingresar:

- Código.
- Nombre.
- Precio.
- Stock.

También contiene botones para:

- Agregar.
- Consultar.
- Actualizar.
- Eliminar.
- Listar.

Los botones utilizan eventos `on_click` para ejecutar las operaciones correspondientes sobre el catálogo.

## Validaciones

La interfaz valida que:

- Todos los campos obligatorios tengan información.
- El precio sea un valor numérico.
- El stock sea un número entero.
- El precio y el stock no sean negativos.
- No se registren productos con códigos duplicados.
- El producto exista antes de realizar determinadas operaciones.

La aplicación muestra mensajes al usuario cuando una operación se realiza correctamente o cuando existe un error.

## Estructura del proyecto

```text
ActividadSemana1/
│
├── modelos/
│   ├── catalogo.py
│   ├── cliente.py
│   ├── cliente_mayorista.py
│   ├── cliente_minorista.py
│   ├── detalle_pedido.py
│   ├── pedido.py
│   ├── producto.py
│   └── producto_digital.py
│
├── app.py
├── main.py
├── prueba_catalogo.py
├── README.md
└── .gitignore
```

La carpeta `modelos` contiene las clases utilizadas por el sistema.

El archivo `main.py` contiene las pruebas correspondientes al sistema de pedidos desarrollado durante las semanas anteriores.

El archivo `prueba_catalogo.py` contiene las pruebas de las operaciones del catálogo de productos.

El archivo `app.py` contiene la interfaz gráfica desarrollada con Flet para realizar las operaciones CRUD.

## Conceptos de Programación Orientada a Objetos

### Encapsulación

Los atributos de las clases se encuentran encapsulados y se utilizan métodos getters y setters para consultar o modificar sus valores.

### Herencia

`ClienteMayorista` y `ClienteMinorista` heredan de la clase abstracta `Cliente`.

`ProductoDigital` hereda de la clase `Producto`.

### Composición

Un `Pedido` contiene uno o varios objetos de tipo `DetallePedido`. Cada detalle se encuentra relacionado con un `Producto`.

### Clase abstracta

`Cliente` fue definida como una clase abstracta y establece el método `calcularDescuento()`, que debe ser implementado por sus clases hijas.

### Polimorfismo

`ClienteMayorista` y `ClienteMinorista` sobrescriben el método `calcularDescuento()`.

De esta manera, un pedido puede solicitar el cálculo del descuento mediante el mismo método, pero el resultado depende del tipo real de cliente.

- Cliente mayorista: descuento del 15 %.
- Cliente minorista: descuento del 5 %.

## Requisitos para ejecutar la aplicación

- Python 3.9 o superior.
- Flet.

Para instalar Flet ejecutar:

```bash
py -m pip install flet
```

## Ejecución de la interfaz gráfica

Desde la carpeta principal del proyecto ejecutar:

```bash
py app.py
```

Se abrirá la interfaz gráfica del catálogo de productos.

## Ejecución de las pruebas del catálogo

Para comprobar desde la terminal las operaciones de agregar, buscar, listar, actualizar, eliminar y evitar duplicados ejecutar:

```bash
py prueba_catalogo.py
```

## Ejecución del sistema de pedidos

Para ejecutar las pruebas correspondientes al sistema de pedidos de las semanas anteriores:

```bash
py main.py
```

## Lenguaje y tecnología utilizados

- Python
- Flet

---

## Semana 7: Cola de Pedidos, Patrón Repository y Pruebas Unitarias

### Descripción

Durante la Semana 7 se amplió el proyecto mediante la implementación de un tipo de dato abstracto lineal, el patrón de diseño Repository y pruebas unitarias utilizando pytest.

Para esta actividad se seleccionó como caso práctico la administración de pedidos pendientes mediante una cola.

### Problema seleccionado

Los pedidos deben ser procesados en el mismo orden en el que fueron recibidos.

Por este motivo se implementó una estructura de datos tipo cola, que utiliza el principio FIFO (First In, First Out), es decir, el primer pedido que ingresa es el primero en ser procesado.

Por ejemplo:

```text
PED001 → PED002 → PED003
```

El primer pedido que será procesado es `PED001`.

### Implementación de la cola

Se creó la clase `ColaPedidos` en:

```text
modelos/cola_pedidos.py
```

La cola fue implementada manualmente utilizando una lista como almacenamiento interno, sin utilizar implementaciones de pila o cola proporcionadas por bibliotecas de Python.

La clase contiene las siguientes operaciones:

- `encolar(pedido)`: agrega un pedido al final de la cola.
- `desencolar()`: elimina y devuelve el primer pedido de la cola.
- `frente()`: consulta el siguiente pedido sin eliminarlo.
- `esta_vacia()`: verifica si la cola se encuentra vacía.
- `tamanio()`: devuelve la cantidad de elementos almacenados.

De esta manera se implementan las operaciones fundamentales requeridas para una cola y se mantiene el comportamiento FIFO.

### Patrón Repository

Se implementó el patrón de diseño Repository mediante la clase `PedidoRepository`, ubicada en:

```text
repositorios/pedido_repository.py
```

El Repository actúa como intermediario entre la aplicación y la estructura de datos.

La aplicación utiliza `PedidoRepository` para administrar los pedidos, mientras que el Repository utiliza internamente la clase `ColaPedidos`.

Las operaciones implementadas en el Repository son:

- `agregar_pedido()`: agrega un pedido.
- `obtener_siguiente_pedido()`: consulta el siguiente pedido.
- `procesar_siguiente_pedido()`: procesa y elimina el siguiente pedido.
- `esta_vacio()`: verifica si existen pedidos pendientes.
- `cantidad_pedidos()`: devuelve la cantidad de pedidos almacenados.

De esta forma se separa el acceso y manejo de los datos de la lógica principal de la aplicación.

### Pruebas unitarias

Para comprobar el correcto funcionamiento de la solución se implementaron pruebas unitarias utilizando `pytest`.

Las pruebas se encuentran en:

```text
tests/test_cola_pedidos.py
tests/test_pedido_repository.py
```

Las pruebas permiten comprobar:

- Que una cola nueva se encuentre vacía.
- La incorporación de pedidos a la cola.
- La cantidad de elementos almacenados.
- La consulta del primer pedido sin eliminarlo.
- La eliminación de pedidos respetando el principio FIFO.
- El comportamiento de la cola cuando se encuentra vacía.
- La incorporación de pedidos mediante el Repository.
- La consulta del siguiente pedido mediante el Repository.
- El procesamiento de pedidos mediante el Repository respetando FIFO.

En total se implementaron 9 pruebas unitarias.

### Instalación de pytest

Para instalar pytest se debe ejecutar:

```bash
py -m pip install pytest
```

### Ejecución de las pruebas unitarias

Desde la carpeta principal del proyecto ejecutar:

```bash
py -m pytest -v
```

Si todas las pruebas se ejecutan correctamente, pytest mostrará que las 9 pruebas fueron aprobadas:

```text
9 passed
```

### Pruebas manuales

También se incluyeron archivos para comprobar manualmente el funcionamiento de la cola y del Repository.

Para probar la cola:

```bash
py prueba_cola.py
```

Para probar el Repository:

```bash
py prueba_repository.py
```

### Estructura incorporada en la Semana 7

```text
ActividadSemana1/
│
├── modelos/
│   ├── cola_pedidos.py
│   └── ...
│
├── repositorios/
│   └── pedido_repository.py
│
├── tests/
│   ├── test_cola_pedidos.py
│   └── test_pedido_repository.py
│
├── prueba_cola.py
├── prueba_repository.py
├── app.py
├── main.py
├── README.md
└── .gitignore
```

### Conceptos aplicados en la Semana 7

En esta actividad se aplicaron los siguientes conceptos:

- Tipos de datos abstractos lineales.
- Implementación manual de una cola.
- Principio FIFO (First In, First Out).
- Encapsulación.
- Patrón de diseño Repository.
- Separación de responsabilidades.
- Pruebas unitarias.
- Uso de pytest.