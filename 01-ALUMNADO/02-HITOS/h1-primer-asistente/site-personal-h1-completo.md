# Página H1 del Site personal — Ana García

> Esta es la página H1 del Site personal. No es una copia del diario: es una selección de evidencias con explicación.

---

## El reto en mis palabras

H1 consiste en crear un asistente de consola llamado MiniJarvis que salude al usuario por su nombre, le pida un número, calcule su doble y muestre un mensaje diferente si el número es positivo o negativo. El programa no tiene menú, ni bucles, ni conexión con IA real. Es un ejercicio de programación básica: entrada, procesamiento y salida.

---

## Mi aportación personal

Yo me encargué del diseño del flujo principal del programa: la estructura de la clase, las constantes, las variables, la lógica de cálculo del doble y la condición `if/else` que decide qué mensaje mostrar. Escribí el código de `Main.java` desde la primera línea hasta la última, hice los commits de cada sesión y redacté las decisiones técnicas del README.

Mi compañara Carlos se encargó de la implementación de `Scanner` para la lectura de entrada y de las pruebas de conversión.

---

## Evidencia seleccionada

### Implementación de `if/else` (S213)

**Enlace:** [Commit ghi789](https://github.com/ejemplo/minijarvis-h1/commit/ghi789)

**Qué demuestra:**
Este commit implementa la lógica condicional del programa. Con `if (numero > 0)`, el programa decide si muestra el doble del número o un mensaje indicando que no es positivo. Probé ambos casos:
- numero = 5 → "El doble de 5 es 10." (rama if)
- numero = -3 → "El número no es positivo." (rama else)

**Por qué la selecciono:**
Es la evidencia donde más aprendí. Tuve que pensar en qué condición usar, cómo escribir el `if/else` correctamente y cómo probar ambos caminos. No usé IA para esto: lo hice yo.

---

## Concepto que ahora domino

### Variable vs constante

Antes de H1, confundía `final` con `static`. Ahora sé que:
- `final` significa que el valor no se puede cambiar.
- `static` significa que la variable pertenece a la clase, no a una instancia.
- Pueden combinarse (`static final`) pero son conceptos independientes.

**Ejemplo propio:**
```java
final String SALUDO = "Hola";  // No se puede cambiar
static int contador = 0;       // Pertenece a la clase
static final int MAX = 100;    // Constante de clase
```

---

## Decisión significativa

### El mensaje de saludo: "Hola" vs "Bienvenido"

En S209, discutimos si el saludo debía ser "Hola, " o "Bienvenido, ". Carlos prefería "Bienvenido" por ser más formal. Yo propuse "Hola" porque es más cercano, no asume género, y se alinea con la idea de un asistente amigable.

**Resultado:** Elegimos "Hola". Lo probamos con ambos mensajes y ambos funcionan. La diferencia es puramente estética y de tono. Aprendí que las decisiones de diseño no son solo técnicas: también son sobre la experiencia del usuario.

---

## Uso de IA

Usé IA en tres sesiones (S207, S210, S212) para entender la estructura base del programa, la diferencia entre `final` y `static`, y el comportamiento de `Integer.parseInt()`. En cada caso, validé la respuesta con el temario o con pruebas antes de aceptarla.

**Registro completo:** [Registro IA H1](https://github.com/ejemplo/minijarvis-h1/blob/h1-entrega/registro-ia-h1-completo.md)

---

## Próximo paso para H2

Implementar un menú con bucle `while` para que el usuario pueda hacer varias consultas sin reiniciar el programa. También quiero aprender a gestionar errores de entrada con `try/catch`.
