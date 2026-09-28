# H1 — Guion de defensa individual (completado)

> La defensa es una comprobación oral y práctica; no es otro documento que debas entregar.

## 1. Ejecutar la versión identificada

**Tag o commit:** `h1-entrega` (commit `abc123def456`)

**Comando de ejecución:**
```bash
java -cp src Main
```

**Resultado esperado:** El programa pide un nombre, lo saluda, pide un número, calcula su doble o indica que no es positivo, y termina.

---

## 2. Explicar `class`, `main`, instrucciones, comentarios y flujo

**`class Main`:**
- Señalo: `public class Main {` en `src/Main.java` línea 1.
- Explico: `class` define una clase en Java. Todo código Java debe estar dentro de una clase. `Main` es el nombre de la clase que contiene el punto de entrada del programa.

**`public static void main(String[] argumentos)`:**
- Señalo: `public static void main(String[] argumentos) {` en `src/Main.java` línea 3.
- Explico: `main` es el método que Java ejecuta automáticamente al arrancar el programa. `public` significa accesible desde fuera. `static` significa que pertenece a la clase, no a una instancia. `void` significa que no devuelve valor. `String[] argumentos` contiene los argumentos pasados por línea de comandos (no se usan en H1).

**Instrucciones:**
- Señalo: `System.out.println("Hola, " + nombre);` en `src/Main.java` línea 10.
- Explico: `System.out.println()` imprime texto por consola y salta de línea. El operador `+` concatena cadenas.

**Comentarios:**
- Señalo: `// Lee el nombre del usuario` en `src/Main.java` línea 8.
- Explico: Los comentarios con `//` son ignorados por el compilador. Sirven para documentar el código.

**Flujo:**
1. Se define la constante `MENSAJE_BIENVENIDA`.
2. Se crea el `Scanner` para leer entrada.
3. Se pide y lee el nombre (`nextLine()`).
4. Se pide y lee el número (`Integer.parseInt(nextLine())`).
5. Se calcula el doble (`numero * 2`).
6. Se evalúa `if (numero > 0)` para decidir la salida.
7. Se imprime el resultado.
8. Se cierra el `Scanner`.

---

## 3. Señalar tipos, variables, constante, literal y operador

**Constante (`final`):**
- Señalo: `final String MENSAJE_BIENVENIDA = "Bienvenida a MiniJarvis.";` en `src/Main.java` línea 8.
- Explico: `final` significa que no se puede reasignar. `String` es el tipo. `MENSAJE_BIENVENIDA` es el nombre. El valor `"Bienvenida a MiniJarvis."` es un literal de cadena.

**Variable `nombre`:**
- Señalo: `String nombre = sc.nextLine();` en `src/Main.java` línea 10.
- Explico: `String` es el tipo. `nombre` es el nombre. Se inicializa con `sc.nextLine()` que lee la entrada del usuario.

**Variable `numero`:**
- Señalo: `int numero = Integer.parseInt(sc.nextLine());` en `src/Main.java` línea 15.
- Explico: `int` es el tipo (entero). `numero` es el nombre. Se inicializa con la conversión de la cadena leída a entero.

**Variable `doble`:**
- Señalo: `int doble = numero * 2;` en `src/Main.java` línea 18.
- Explico: `int` es el tipo. `doble` es el nombre. Se asigna el resultado de `numero * 2`.

**Literal:**
- Señalo: `"Hola, "` en `src/Main.java` línea 10.
- Explico: `"Hola, "` es un literal de cadena: un valor de texto escrito directamente en el código.

**Operador:**
- Señalo: `+` en `src/Main.java` línea 10.
- Explico: `+` es el operador de concatenación de cadenas. Une `"Hola, "` con el valor de `nombre`.

---

## 4. Predecir una conversión o división antes de ejecutarla

**Predicción:**
Si el usuario introduce `"abc"` como número, `Integer.parseInt("abc")` lanzará `NumberFormatException`.

**Ejecución:**
```
Entrada: abc
Resultado: Exception in thread "main" java.lang.NumberFormatException: For input string: "abc"
```

**Explicación:**
`Integer.parseInt()` solo acepta cadenas que representen números enteros válidos. `"abc"` no es un número, por lo que el método lanza una excepción de ejecución.

---

## 5. Explicar una comparación, una expresión booleana y un `if/else` básico

**Comparación:**
- Señalo: `if (numero > 0)` en `src/Main.java` línea 20.
- Explico: `numero > 0` es una comparación que evalúa si `numero` es mayor que 0. El resultado es `true` o `false`.

**Expresión booleana:**
- Señalo: `numero > 0` en `src/Main.java` línea 20.
- Explico: Es una expresión que produce un valor booleano (`true` o `false`). Si numero = 5, la expresión es `true`. Si numero = -3, es `false`.

**`if/else`:**
- Señalo: `if (numero > 0) { ... } else { ... }` en `src/Main.java` líneas 20-24.
- Explico: Si la condición es `true`, se ejecuta el bloque `if` (muestra el doble). Si es `false`, se ejecuta el bloque `else` (muestra "El número no es positivo.").

---

## 6. Diferenciar el producto principal de las microprácticas

**Producto principal:**
- `Main.java` completo: lee nombre y número, calcula el doble, aplica `if/else`. Es el programa funcional que se entrega.

**Microprácticas:**
- Ejemplos mínimos en el README (sección "Microprácticas del Tema 1") que demuestran conceptos individuales: tipos, constantes, conversión, comparaciones, `if/else`. No son parte del producto funcional; son ejercicios de aprendizaje que se enlazan desde el README.

---

## 7. Modificar una entrada, mensaje, operación o condición y volver a probar

**Modificación realizada:**
Cambié el mensaje de bienvenida de `"Bienvenida a MiniJarvis."` a `"Hola, " + nombre + ". ¿Qué tal?"` en `src/Main.java` línea 8.

**Resultado:**
```
Entrada: Ana
Salida: Hola, Ana. ¿Qué tal?
El doble de 5 es 10.
```

**Explicación:**
Al modificar el literal en `MENSAJE_BIENVENIDA`, el mensaje impreso cambia. La modificación se refleja inmediatamente porque `MENSAJE_BIENVENIDA` se usa en la línea 10 con `System.out.println(MENSAJE_BIENVENIDA)`.

---

## 8. Localizar en el README la prueba y en el diario una decisión

**Prueba en README:**
- Sección "Ejemplo reproducible → Caso normal" del `README-h1-completo.md`.
- Muestra entrada, salida esperada y salida obtenida para el caso Ana/5.

**Decisión en diario:**
- Fila S209 del diario individual: decisión de usar `"Hola, " + nombre` en lugar de `"Bienvenido, " + nombre` porque "Hola" es más cercano y no asume género.

---

## 9. Explicar cualquier uso de IA y su validación

**Uso de IA:**
- Fila S212 del diario individual: pedí ayuda para entender `Integer.parseInt()` y su diferencia con `Integer.valueOf()`.
- Validación: probé ambos métodos con la entrada `"5"`. Ambos funcionan, pero `parseInt()` devuelve `int` (primitivo) y `valueOf()` devuelve `Integer` (objeto). Para H1, `parseInt()` es suficiente.

---

## Lo que puedo defender sin ayuda

- Explicar el flujo completo del programa.
- Señalar cada variable, su tipo, nombre y valor.
- Explicar por qué `final` hace que una variable sea constante.
- Predecir y explicar el resultado de `if/else` con cualquier entrada.
- Explicar qué pasa si la entrada no es un número.
- Modificar un mensaje o valor y predecir el efecto.

## Lo que necesito reforzar

- Manejo de errores de entrada (try/catch) → se abordará en H2.
- Bucles y menú → se abordará en H2.
- Operadores lógicos `&&`, `||`, `!` → se practicaron en S213 pero se usarán más en H2.
