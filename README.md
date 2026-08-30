# Actividad de Programación Orientada a Objetos

Este proyecto fue desarrollado en Python como parte de las actividades de Programación Orientada a Objetos.

Durante las primeras semanas se implementaron conceptos como clases, objetos, encapsulación, herencia y composición. En la Semana 3 se amplió la solución para aplicar clases abstractas, sobrescritura de métodos y polimorfismo.

## Descripción

El proyecto representa un sistema sencillo de pedidos que permite trabajar con clientes y productos.

La clase `Cliente` se definió como una clase abstracta y establece el método `calcularDescuento()`.

A partir de esta clase se crearon dos tipos de clientes:

- `ClienteMayorista`: aplica un descuento del 15 %.
- `ClienteMinorista`: aplica un descuento del 5 %.

Cada clase implementa su propia versión de `calcularDescuento()`, permitiendo aplicar polimorfismo.

La clase `Pedido` trabaja con un objeto de tipo `Cliente` y utiliza su método `calcularDescuento()` sin necesitar comprobar si el cliente es mayorista o minorista.

## Estructura del proyecto

- `modelos/cliente.py`: clase abstracta Cliente.
- `modelos/cliente_mayorista.py`: clase ClienteMayorista.
- `modelos/cliente_minorista.py`: clase ClienteMinorista.
- `modelos/producto.py`: clase Producto.
- `modelos/producto_digital.py`: clase ProductoDigital.
- `modelos/detalle_pedido.py`: clase DetallePedido.
- `modelos/pedido.py`: clase Pedido.
- `main.py`: archivo principal para probar el funcionamiento del programa.

## Conceptos aplicados

- Clases y objetos
- Encapsulación
- Getters y setters
- Herencia
- Composición
- Clases abstractas
- Sobrescritura de métodos
- Polimorfismo

## Ejecución

Para ejecutar el programa:

```bash
py main.py