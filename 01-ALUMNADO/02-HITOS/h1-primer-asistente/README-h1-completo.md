# MiniJarvis H1 — Primer asistente por consola

## Qué hace

MiniJarvis es un asistente de consola que pide un nombre al usuario, lo saluda con un mensaje personalizado y aplica una operación simple (dobla el valor de un número introducido). Lee entrada por teclado, usa variables, constantes, comparaciones y `if/else` para decidir la salida. No tiene menú, ni bucles, ni conexión con IA real.

## Requisitos y ejecución

- JDK utilizado: JDK 17 (o superior)
- IDE opcional: IntelliJ IDEA, VS Code con extensión Java, o Eclipse
- Clase principal: `Main.java`

```text
1. Clonar o abrir el repositorio en el IDE.
2. Abrir el archivo src/Main.java.
3. Compilar: javac src/Main.java
4. Ejecutar: java -cp src Main
5. Introducir un nombre cuando se solicite.
6. Introducir un número entero cuando se solicite.
7. Observar la salida por consola.
```

## Ejemplo reproducible

### Caso normal

```text
Entrada:
Nombre: Ana
Número: 5

Salida esperada:
Hola, Ana. Bienvenida a MiniJarvis.
El doble de 5 es 10.

Salida obtenida:
Hola, Ana. Bienvenida a MiniJarvis.
El doble de 5 es 10.
```

### Caso alternativo o error básico

```text
Entrada:
Nombre: Carlos
Número: abc

Predicción:
El programa lanza NumberFormatException porque "abc" no se puede convertir a entero.

Resultado obtenido:
Exception in thread "main" java.lang.NumberFormatException: For input string: "abc"

Explicación:
Integer.parseInt("abc") falla porque "abc" no es un número válido. El programa no gestiona este error en H1; se detiene con una excepción de ejecución.
```

## Decisiones técnicas

| Decisión | Motivo | Enlace a código/commit |
|---|---|---|
| Usar `Scanner` con `nextLine()` para el nombre | Permite leer cadenas con espacios, necesario para nombres completos | [commit S212](https://github.com/ejemplo/minijarvis-h1/commit/abc123) |
| Usar `Integer.parseInt()` para convertir la entrada numérica | Convierte la cadena leída a entero para realizar operaciones aritméticas | [commit S212](https://github.com/ejemplo/minijarvis-h1/commit/abc123) |
| Usar `final` para `MENSAJE_BIENVENIDA` | Es un valor fijo que no cambia durante la ejecución; `final` previene modificaciones accidentales | [commit S211](https://github.com/ejemplo/minijarvis-h1/commit/def456) |
| Usar `if/else` para verificar si el número es positivo | Muestra un mensaje diferente si el número es negativo o cero | [commit S213](https://github.com/ejemplo/minijarvis-h1/commit/ghi789) |
| No implementar menú ni bucles | Queda fuera del alcance de H1; se abordará en H2 | — |

## Microprácticas del Tema 1

No fuerces todo dentro del producto. Enlaza ejemplos mínimos que puedas ejecutar y explicar.

| Concepto | Archivo o commit | Prueba o salida |
|---|---|---|
| Tipos, variables y asignación | `Main.java` línea 12-15 | `String nombre = "Ana";` → salida: `Hola, Ana` |
| Constantes, literales y operadores | `Main.java` línea 8 | `final String MENSAJE_BIENVENIDA = "Bienvenida a MiniJarvis.";` → no se puede reasignar |
| Conversión y casting | `Main.java` línea 20 | `Integer.parseInt("5")` → `5` (int); `(double) 5 / 2` → `2.5` |
| Comparaciones y booleanos | `Main.java` línea 25 | `numero > 0` → `true` si numero=5, `false` si numero=-3 |
| `if/else` y `?:` básicos | `Main.java` línea 25-28 | Si `numero > 0` → "El doble es X"; else → "El número no es positivo" |

## Limitaciones deliberadas

- Sin menú.
- Sin bucle.
- Sin credenciales, datos personales ni conexión con IA real.
- Sin gestión de errores de entrada (excepto la que se demuestra con `NumberFormatException`).
- Sin persistencia de datos (no guarda ni recupera información entre ejecuciones).

## Versión evaluada

- Tag `h1-entrega` o commit: `h1-entrega` (commit `abc123def456`)
- Fecha: 2026-10-15
- Integrantes y aportación verificable:
  - Ana García: diseño del flujo principal, variables, constantes, `if/else` (commits `abc123`, `def456`, `ghi789`)
  - Carlos López: implementación de `Scanner`, conversión de entrada, pruebas de ejecución (commits `jkl012`, `mno345`)
