# Sistema de Pedidos - Programación Orientada a Objetos

## Descripción

Este proyecto consiste en un sistema sencillo de pedidos desarrollado en Python como parte de las actividades de Programación Orientada a Objetos.

El sistema permite crear diferentes tipos de clientes, productos y pedidos. También permite agregar productos a un pedido, calcular subtotales, obtener el total y aplicar un descuento de acuerdo con el tipo de cliente.

El proyecto integra los conceptos estudiados hasta la Semana 3: clases y objetos, encapsulación, herencia, composición, clases abstractas, sobrescritura de métodos y polimorfismo.

## Objetivo

El objetivo del proyecto es aplicar de forma práctica los principales conceptos de Programación Orientada a Objetos estudiados durante las tres primeras semanas, mediante el desarrollo de un sistema de pedidos.

## Principales funcionalidades

- Crear clientes mayoristas y minoristas.
- Crear productos normales y productos digitales.
- Crear pedidos asociados a un cliente.
- Agregar diferentes detalles a un pedido.
- Calcular el subtotal de cada detalle según la cantidad y el precio unitario.
- Calcular el total de un pedido.
- Calcular descuentos diferentes según el tipo de cliente.
- Calcular el total final después de aplicar el descuento.
- Utilizar una clase abstracta `Cliente` como estructura común para los diferentes tipos de clientes.
- Aplicar polimorfismo mediante el método `calcularDescuento()`.

## Estructura del proyecto

```text
ActividadSemana1/
│
├── modelos/
│   ├── cliente.py
│   ├── cliente_mayorista.py
│   ├── cliente_minorista.py
│   ├── producto.py
│   ├── producto_digital.py
│   ├── detalle_pedido.py
│   └── pedido.py
│
├── main.py
├── README.md
└── .gitignore
```

La carpeta `modelos` contiene las clases utilizadas por el sistema.

El archivo `main.py` contiene la creación de los objetos y las pruebas necesarias para comprobar el funcionamiento del programa.

## Conceptos de POO utilizados

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

## Ejecución

Para ejecutar el proyecto en Windows se debe tener Python instalado.

Desde la carpeta principal del proyecto ejecutar:

```bash
py main.py
```

El programa mostrará en la terminal los datos de los pedidos, sus productos, cantidades, subtotales, total, descuento aplicado y total final.

## Lenguaje utilizado

**Python**