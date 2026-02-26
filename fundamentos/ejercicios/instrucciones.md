# Ejercicios de práctica

## BLOQUE 1 — Variables y Tipos de Datos (Ejercicios 1–5)

### Ejercicio 1 — Ficha de empleado

- Declarar variables para almacenar el nombre, apellido, edad, salario y si está activo en la empresa (boolean).
- Luego imprimir cada una con su tipo de dato usando `type()`.

### Ejercicio 2 — Conversión de tipos

- Recibir por input el precio de un producto (como string) y la cantidad comprada.
- Convertirlos al tipo correcto y calcular el total. Mostrar el resultado indicando el tipo final de cada variable.

### Ejercicio 3 — Inventario básico

Tenés un producto con nombre (str), precio unitario (float), stock disponible (int) y si está disponible para venta (bool).

- Asignar valores y mostrar una ficha de producto formateada con `print()`.

### Ejercicio 4 — Swap de variables

En un sistema de turnos, el turno A y el turno B necesitan intercambiar sus horarios de entrada.

- Realizá el swap sin usar una variable auxiliar (Python permite esto de forma nativa). Mostrar antes y después.

### Ejercicio 5 — Detectar tipo de dato recibido

Simular una validación básica:

- recibir un valor por input e intentar convertirlo a `int`, luego a `float`.
- Mostrar qué tipo de dato es realmente lo que el usuario ingresó.
- **Pista:** usá un bloque `try/except` básico, aunque aún no lo hayas visto formalmente. Investigarlo es parte del ejercicio.

---

## BLOQUE 2 — Operadores Aritméticos (Ejercicios 6–10)

### Ejercicio 6 — Calculadora de sueldo neto

- Ingresar sueldo bruto.
- Aplicar un descuento del 11% para jubilación y 3% para obra social.
- Calcular y mostrar cada descuento por separado y el sueldo neto final.

### Ejercicio 7 — Conversor de temperatura

- Pedir una temperatura y la escala de origen (Celsius, Fahrenheit o Kelvin).
- Convertirla a las otras dos escalas.
- Mostrar los tres valores.

- Fórmulas:
  - °F = (°C × 9/5) + 32
  - K = °C + 273.15

### Ejercicio 8 — Calculadora de IMC

- Pedir peso (kg) y altura (m).
- Calcular el IMC y mostrar el resultado con dos decimales junto con la categoría correspondiente (Bajo peso / Normal / Sobrepeso / Obesidad).

### Ejercicio 9 — División con resto

En un depósito hay 500 unidades de un producto. Se deben empaquetar en cajas de 24 unidades.

- Calcular cuántas cajas completas se pueden armar y cuántas unidades sobran.
- Usar operadores `//` y `%`.

### Ejercicio 10 — Calculadora de propina

- Ingresar el monto de una cuenta en restaurante y el porcentaje de propina deseado.
- Mostrar el monto de la propina, el total a pagar y cuánto le toca a cada persona si el gasto se divide entre N comensales (también ingresado por input).

---

## BLOQUE 3 — Operadores de Comparación y Lógicos (Ejercicios 11–15)

### Ejercicio 11 — Validador de acceso

Simular el login de un sistema interno.

- Definir un usuario y contraseña correctos en el código.
- Pedir los datos al usuario y mostrar si el acceso fue concedido o denegado usando operadores de comparación.

### Ejercicio 12 — Elegibilidad para un puesto

Una empresa requiere que el candidato tenga entre 25 y 45 años, más de 2 años de experiencia y no tener otro empleo activo.

- Pedir los datos e informar si el candidato es elegible.
- Usar operadores `and`, `or`, `not`.

### Ejercicio 13 — Clasificador de notas

- Ingresar una nota numérica del 1 al 10.
- Determinar y mostrar si el estudiante aprobó, está en recuperatorio (entre 4 y 5) o reprobó.
- Contemplar si la nota ingresada está fuera del rango válido.

### Ejercicio 14 — Verificador de año bisiesto

- Ingresar un año y determinar si es bisiesto.
- Regla: divisible por 4, excepto los divisibles por 100, salvo que también sean divisibles por 400.
- Mostrar el resultado con una explicación del criterio que aplicó.

### Ejercicio 15 — Comparador de precios

- Ingresar el precio de un mismo producto en tres tiendas distintas.
- Usando solo operadores de comparación y lógicos (sin listas ni funciones built-in como `min()`), determinar cuál tienda tiene el precio más bajo y mostrarlo.

---

## BLOQUE 4 — `Input/Output`, `f-strings` y `format()` (Ejercicios 16–20)

### Ejercicio 16 — Recibo de pago formateado

- Generar un recibo de pago con nombre del empleado, cargo, sueldo bruto, descuentos y sueldo neto.
- Todo alineado y formateado prolijamente usando `f-strings`.
- Los números deben mostrarse con separador de miles y dos decimales.

### Ejercicio 17 — Tabla de conversión de moneda

- Ingresar un monto en pesos argentinos y un tipo de cambio.
- Mostrar la conversión a USD, EUR y BRL en una tabla formateada con columnas alineadas usando `format()` o `f-strings` con especificadores de ancho.

### Ejercicio 18 — Generador de mail corporativo

- Pedir nombre y apellido de un nuevo empleado y el dominio de la empresa.
- Generar automáticamente su mail corporativo en formato nombre.apellido@empresa.com (todo en minúsculas, sin espacios).
- Mostrar un mensaje de bienvenida usando `f-string` multilínea.

### Ejercicio 19 — Resumen de ventas del día

- Ingresar las ventas de 3 productos distintos (nombre y monto).
- Calcular el total del día, el promedio por producto y cuál fue el más vendido.
- Mostrar un reporte final bien presentado usando `f-strings`.

### Ejercicio 20 — Simulador de cotización

Una pequeña empresa necesita generar cotizaciones.

- Pedir: nombre del cliente, descripción del servicio, precio base, cantidad de horas estimadas y costo por hora adicional.
- Calcular el total y mostrar una cotización profesional formateada con todos los datos, incluyendo fecha actual (investigar `datetime.date.today()`).
