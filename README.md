# Sistema de Pedidos y Catálogo de Productos - Programación Orientada a Objetos

## Descripción

Este proyecto fue desarrollado en Python como parte de las actividades de Programación Orientada a Objetos.

Durante las primeras semanas se desarrolló un sistema de pedidos utilizando clases como `Cliente`, `Producto`, `Pedido` y `DetallePedido`, aplicando conceptos de encapsulación, herencia, composición, clases abstractas y polimorfismo.

En las semanas 5 y 6 se amplió el proyecto mediante la implementación de un catálogo de productos utilizando colecciones de Python y una interfaz gráfica desarrollada con Flet.

El catálogo permite agregar, consultar, listar, actualizar y eliminar productos mediante una interfaz gráfica.

En la Semana 7 se incorporó una cola de pedidos implementada manualmente, el patrón de diseño Repository y pruebas unitarias utilizando pytest.

Además, el proyecto incorpora persistencia de datos mediante un archivo JSON. Los productos registrados desde la interfaz gráfica se almacenan de forma permanente y son recuperados automáticamente cuando la aplicación vuelve a ejecutarse.

Para separar la lógica de almacenamiento de la lógica principal de la aplicación, se utiliza la clase `ProductoRepository`, encargada de guardar y recuperar los productos desde el archivo `datos/productos.json`.

---

## Objetivo

Aplicar de forma práctica los conceptos de Programación Orientada a Objetos, colecciones, operaciones CRUD, interfaz gráfica, manejo de eventos, tipos de datos abstractos lineales, patrones de diseño, pruebas unitarias y persistencia de datos mediante el desarrollo de un sistema de pedidos y un catálogo de productos.

---

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
- Almacenar los productos de forma persistente en un archivo JSON.
- Recuperar automáticamente los productos almacenados al iniciar nuevamente la aplicación.
- Mantener los cambios realizados al agregar, actualizar o eliminar productos después de cerrar la aplicación.
- Administrar pedidos pendientes mediante una cola implementada manualmente.
- Procesar pedidos respetando el principio FIFO (First In, First Out).
- Utilizar el patrón Repository para separar el manejo de los datos de la lógica principal.
- Comprobar el funcionamiento de la cola y del Repository mediante pruebas unitarias con pytest.

---

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

---

## Operaciones CRUD

El catálogo implementa las siguientes operaciones:

- **Create:** agregar un nuevo producto.
- **Read:** consultar un producto por código y listar los productos registrados.
- **Update:** actualizar los datos de un producto existente.
- **Delete:** eliminar un producto del catálogo.

Las operaciones que modifican la información también actualizan el archivo utilizado para la persistencia de datos.

---

## Interfaz gráfica

La interfaz gráfica fue desarrollada utilizando **Flet**.

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

De esta manera, la interfaz gráfica se encuentra integrada con las operaciones CRUD implementadas en la clase `Catalogo`.

---

## Validaciones

La interfaz valida que:

- Todos los campos obligatorios tengan información.
- El precio sea un valor numérico.
- El stock sea un número entero.
- El precio y el stock no sean negativos.
- No se registren productos con códigos duplicados.
- El producto exista antes de realizar determinadas operaciones.

La aplicación muestra mensajes al usuario cuando una operación se realiza correctamente o cuando existe un error.

---

## Persistencia de datos

El proyecto implementa persistencia de datos mediante un archivo JSON.

Los productos se almacenan en:

```text
datos/productos.json
```

Para separar la lógica de almacenamiento de la lógica principal se implementó la clase:

```text
repositorios/producto_repository.py
```

La clase `ProductoRepository` contiene las operaciones necesarias para guardar y recuperar los productos.

### Guardar productos

Cuando se agrega, actualiza o elimina un producto, el catálogo utiliza `ProductoRepository` para actualizar el archivo `productos.json`.

Los objetos de tipo `Producto` son transformados en datos que pueden almacenarse en formato JSON.

Por ejemplo:

```json
{
    "codigo": "P001",
    "nombre": "Teclado",
    "precio": 25.5,
    "stock": 10
}
```

### Recuperar productos

Cuando se crea el catálogo al iniciar la aplicación, `ProductoRepository` lee el archivo `productos.json`.

Los datos almacenados son utilizados para volver a crear los objetos `Producto` y cargarlos en las colecciones del catálogo.

El flujo general de la persistencia es:

```text
Interfaz gráfica
       ↓
    Catalogo
       ↓
ProductoRepository
       ↓
productos.json
```

De esta manera, los productos registrados no se pierden cuando la aplicación se cierra.

Al ejecutar nuevamente la aplicación, los productos almacenados son recuperados automáticamente.

---

## Estructura del proyecto

```text
ActividadSemana1/
│
├── datos/
│   └── productos.json
│
├── modelos/
│   ├── catalogo.py
│   ├── cliente.py
│   ├── cliente_mayorista.py
│   ├── cliente_minorista.py
│   ├── cola_pedidos.py
│   ├── detalle_pedido.py
│   ├── pedido.py
│   ├── producto.py
│   └── producto_digital.py
│
├── repositorios/
│   ├── pedido_repository.py
│   └── producto_repository.py
│
├── tests/
│   ├── test_cola_pedidos.py
│   └── test_pedido_repository.py
│
├── app.py
├── main.py
├── prueba_catalogo.py
├── prueba_cola.py
├── prueba_repository.py
├── README.md
└── .gitignore
```

### Organización

La carpeta `modelos` contiene las principales clases utilizadas por el sistema.

La carpeta `repositorios` contiene las clases encargadas de separar el manejo y acceso a los datos de la lógica principal.

La carpeta `datos` contiene el archivo JSON utilizado para almacenar los productos de forma persistente.

La carpeta `tests` contiene las pruebas unitarias desarrolladas con pytest.

El archivo `app.py` contiene la interfaz gráfica desarrollada con Flet.

El archivo `main.py` contiene las pruebas correspondientes al sistema de pedidos desarrollado durante las primeras semanas.

El archivo `prueba_catalogo.py` permite comprobar las operaciones del catálogo desde la terminal.

---

## Conceptos de Programación Orientada a Objetos

### Encapsulación

Los atributos de las clases se encuentran encapsulados y se utilizan métodos getters y setters para consultar o modificar sus valores.

### Herencia

`ClienteMayorista` y `ClienteMinorista` heredan de la clase abstracta `Cliente`.

`ProductoDigital` hereda de la clase `Producto`.

### Composición

Un `Pedido` contiene uno o varios objetos de tipo `DetallePedido`.

Cada detalle se encuentra relacionado con un `Producto`.

### Clase abstracta

`Cliente` fue definida como una clase abstracta y establece el método `calcularDescuento()`, que debe ser implementado por sus clases hijas.

### Polimorfismo

`ClienteMayorista` y `ClienteMinorista` sobrescriben el método `calcularDescuento()`.

De esta manera, un pedido puede solicitar el cálculo del descuento mediante el mismo método, pero el resultado depende del tipo real de cliente.

- Cliente mayorista: descuento del 15 %.
- Cliente minorista: descuento del 5 %.

---

## Semana 7: Cola de Pedidos, Patrón Repository y Pruebas Unitarias

### Problema seleccionado

Para la Semana 7 se seleccionó como caso práctico la administración de pedidos pendientes.

Los pedidos deben ser procesados en el mismo orden en el que fueron recibidos.

Por este motivo se implementó una estructura de datos tipo cola, que utiliza el principio **FIFO (First In, First Out)**, es decir, el primer pedido que ingresa es el primero en ser procesado.

Por ejemplo:

```text
PED001 → PED002 → PED003
```

El primer pedido que será procesado es `PED001`.

---

### Implementación de la cola

Se creó la clase `ColaPedidos` en:

```text
modelos/cola_pedidos.py
```

La cola fue implementada manualmente utilizando una lista como almacenamiento interno, sin utilizar directamente una implementación de pila o cola proporcionada por una biblioteca de Python.

La clase contiene las siguientes operaciones:

- `encolar(pedido)`: agrega un pedido al final de la cola.
- `desencolar()`: elimina y devuelve el primer pedido de la cola.
- `frente()`: consulta el siguiente pedido sin eliminarlo.
- `esta_vacia()`: verifica si la cola se encuentra vacía.
- `tamanio()`: devuelve la cantidad de elementos almacenados.

De esta manera se implementan las operaciones fundamentales requeridas para una cola y se mantiene el comportamiento FIFO.

---

## Patrón Repository

El proyecto utiliza el patrón Repository para separar el acceso y manejo de los datos de la lógica principal de la aplicación.

Se implementaron dos clases relacionadas con este patrón.

### PedidoRepository

La clase se encuentra en:

```text
repositorios/pedido_repository.py
```

`PedidoRepository` utiliza internamente la clase `ColaPedidos` para administrar los pedidos.

El flujo es:

```text
Aplicación
    ↓
PedidoRepository
    ↓
ColaPedidos
```

Las operaciones implementadas son:

- `agregar_pedido()`: agrega un pedido.
- `obtener_siguiente_pedido()`: consulta el siguiente pedido.
- `procesar_siguiente_pedido()`: procesa y elimina el siguiente pedido.
- `esta_vacio()`: verifica si existen pedidos pendientes.
- `cantidad_pedidos()`: devuelve la cantidad de pedidos almacenados.

### ProductoRepository

La clase se encuentra en:

```text
repositorios/producto_repository.py
```

`ProductoRepository` se encarga de guardar y recuperar los productos almacenados en el archivo JSON.

Esto permite separar la lógica de persistencia de las operaciones principales realizadas por el catálogo.

---

## Pruebas unitarias

Para comprobar el correcto funcionamiento de la cola y del Repository se implementaron pruebas unitarias utilizando **pytest**.

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
- La eliminación de pedidos respetando FIFO.
- El comportamiento de la cola cuando se encuentra vacía.
- La incorporación de pedidos mediante el Repository.
- La consulta del siguiente pedido mediante el Repository.
- El procesamiento de pedidos mediante el Repository respetando FIFO.

En total se implementaron **9 pruebas unitarias**.

---

## Requisitos para ejecutar la aplicación

Para ejecutar el proyecto se requiere:

- Python 3.9 o superior.
- Flet.
- pytest.

Para instalar Flet y pytest:

```bash
py -m pip install flet pytest
```

---

## Ejecución de la interfaz gráfica

Desde la carpeta principal del proyecto ejecutar:

```bash
py app.py
```

Se abrirá la interfaz gráfica del catálogo de productos.

Al iniciar la aplicación, los productos almacenados previamente en `datos/productos.json` serán recuperados automáticamente.

---

## Ejecución de las pruebas unitarias

Para ejecutar todas las pruebas unitarias:

```bash
py -m pytest -v
```

Si todas las pruebas funcionan correctamente, pytest mostrará:

```text
9 passed
```

---

## Ejecución de las pruebas del catálogo

Para comprobar desde la terminal las operaciones del catálogo ejecutar:

```bash
py prueba_catalogo.py
```

---

## Ejecución de las pruebas manuales de la cola

Para probar manualmente la cola:

```bash
py prueba_cola.py
```

Para probar manualmente el Repository:

```bash
py prueba_repository.py
```

---

## Ejecución del sistema de pedidos

Para ejecutar el sistema de pedidos desarrollado durante las primeras semanas:

```bash
py main.py
```

---

## Lenguaje y tecnologías utilizadas

- **Lenguaje:** Python.
- **Interfaz gráfica:** Flet.
- **Persistencia:** JSON.
- **Pruebas unitarias:** pytest.
- **Control de versiones:** Git y GitHub.