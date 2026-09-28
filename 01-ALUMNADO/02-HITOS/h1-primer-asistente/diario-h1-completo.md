# Diario individual H1 — completado (Ana García)

> Este documento simula las filas que se registrarían en el Sheet individual de diario. Cada sesión tiene una fila con: fecha, sesión, hit, objetivo, acción, prueba y resultado, evidencia enlazada, bloqueo (si aplica), uso de IA, y próximo paso.

---

## S206 — Definición del alcance de H1

- **Fecha:** 2026-09-29
- **Sesión:** S206
- **Hit:** H1
- **Objetivo:** Entender qué incluye y qué excluye H1. Crear el backlog inicial del equipo.
- **Acción:** Leí la descripción del hit H1. Escribí la frase de alcance: "H1 consiste en un asistente de consola que lee nombre y número, calcula el doble, y usa if/else para decidir la salida." Definimos qué entra (entrada, salida, variables, constantes, operaciones, comparaciones, if/else) y qué queda fuera (menú, bucles, IA real, credenciales).
- **Prueba y resultado:** El equipo acordó el alcance. Lo registré en el Scrum Sheet y en mi diario.
- **Evidencia enlazada:** [Scrum S206](https://sheets.example.com/scrum-h1#S206)
- **Bloqueo:** Ninguno.
- **Uso de IA:** No.
- **Próximo paso:** S207: crear la primera ejecución del programa.

---

## S207 — Primera ejecución

- **Fecha:** 2026-10-01
- **Sesión:** S207
- **Hit:** H1
- **Objetivo:** Hacer que el programa imprima algo por consola.
- **Acción:** Creé `Main.java` con la estructura mínima: `class Main`, `main`, `System.out.println("Hola Mundo")`. Compilé con `javac` y ejecuté con `java`.
- **Prueba y resultado:** El programa imprimió "Hola Mundo" por consola. Sé que se ha ejecutado porque vi el texto en la terminal.
- **Evidencia enlazada:** [Commit abc123](https://github.com/ejemplo/minijarvis-h1/commit/abc123)
- **Bloqueo:** Ninguno.
- **Uso de IA:** Sí. Pedí la estructura mínima a ChatGPT (ver registro IA S207).
- **Próximo paso:** S208: añadir la estructura completa con comentarios y entender cada parte.

---

## S208 — Estructura mínima y error corregido

- **Fecha:** 2026-10-03
- **Sesión:** S208
- **Hit:** H1
- **Objetivo:** Entender la estructura de la clase, el main, las instrucciones y los comentarios. Provocar y corregir un error.
- **Acción:** Añadí comentarios explicativos a `Main.java`. Provocué un error olvidando el `;` al final de `System.out.println("Hola")`. El compilador mostró el error y la línea exacta. Corregí el error añadiendo el `;`.
- **Prueba y resultado:** El programa compiló y ejecutó correctamente tras la corrección. Aprendí que cada instrucción en Java debe terminar con `;`.
- **Evidencia enlazada:** [Incidencia H1](https://github.com/ejemplo/minijarvis-h1/blob/h1-entrega/incidencia-h1-completo.md)
- **Bloqueo:** Error de compilación por falta de `;`. Resuelto en el acto.
- **Uso de IA:** No.
- **Próximo paso:** S209: decidir el mensaje de saludo del asistente.

---

## S209 — Decisión del mensaje de saludo

- **Fecha:** 2026-10-05
- **Sesión:** S209
- **Hit:** H1
- **Objetivo:** Decidir el mensaje de saludo y registrarlo en Scrum.
- **Acción:** Discutimos con Carlos si el saludo debía ser "Hola, " o "Bienvenido, ". Propuse "Hola" porque es más cercano y no asume género. Carlos aceptó. Implementé el mensaje en el código: `System.out.println("Hola, " + nombre);`.
- **Prueba y resultado:** Ejecuté con nombre = "Ana" → "Hola, Ana". Ejecuté con nombre = "Carlos" → "Hola, Carlos". Ambos funcionan.
- **Evidencia enlazada:** [Scrum S209](https://sheets.example.com/scrum-h1#S209)
- **Bloqueo:** Ninguno.
- **Uso de IA:** No.
- **Próximo paso:** S210: crear el plan de datos y definir las variables.

---

## S210 — Plan de datos y variables

- **Fecha:** 2026-10-08
- **Sesión:** S210
- **Hit:** H1
- **Objetivo:** Crear el plan de datos para H1 antes de escribir código.
- **Acción:** Creé la tabla de plan de datos:

| Dato | Tipo | Nombre | Cambia | Uso |
|---|---|---|---|---|
| Nombre del usuario | String | nombre | No | Guardar el nombre introducido |
| Número del usuario | int | numero | No | Guardar el número introducido |
| Doble del número | int | doble | No | Calcular numero * 2 |
| Mensaje de bienvenida | String | MENSAJE_BIENVENIDA | No | Mensaje fijo de bienvenida |

Implementé las variables en el código con nombres claros y descriptivos.
- **Prueba y resultado:** El programa declara y usa las variables correctamente. Puedo señalar cada variable, explicar su tipo, nombre y valor.
- **Evidencia enlazada:** [Scrum S210](https://sheets.example.com/scrum-h1#S210)
- **Bloqueo:** Confusión entre `final` y `static`. La aclaré con IA (ver registro IA S210).
- **Uso de IA:** Sí. Pregunté sobre `static final` vs `final` (ver registro IA S210).
- **Próximo paso:** S211: añadir constantes y operaciones aritméticas.

---

## S211 — Constantes, operaciones y predicción

- **Fecha:** 2026-10-10
- **Sesión:** S211
- **Hit:** H1
- **Objetivo:** Usar `final` para constantes y realizar operaciones aritméticas.
- **Acción:** Añadí `final String MENSAJE_BIENVENIDA = "Bienvenida a MiniJarvis.";` y `final int DOBLE_FACTOR = 2;`. Calculé `int doble = numero * DOBLE_FACTOR;`. Provocué un error intentando reasignar `DOBLE_FACTOR = 3;` y lo corregí eliminando la reasignación.
- **Prueba y resultado:** Predije que `5 * 2 = 10`. El resultado obtenido fue 10. Predije que `final int DOBLE_FACTOR = 2; DOBLE_FACTOR = 3;` daría error de compilación. El resultado fue `cannot assign a value to final variable DOBLE_FACTOR`.
- **Evidencia enlazada:** [Commit def456](https://github.com/ejemplo/minijarvis-h1/commit/def456), [Incidencia H1](https://github.com/ejemplo/minijarvis-h1/blob/h1-entrega/incidencia-h1-completo.md)
- **Bloqueo:** Error al reasignar constante. Resuelto.
- **Uso de IA:** No.
- **Próximo paso:** S212: implementar la lectura de entrada con Scanner.

---

## S212 — Entrada con Scanner y conversión

- **Fecha:** 2026-10-12
- **Sesión:** S212
- **Hit:** H1
- **Objetivo:** Leer entrada del usuario con `Scanner` y convertirla a entero.
- **Acción:** Carlos implementó `Scanner sc = new Scanner(System.in);`, `String nombre = sc.nextLine();`, y `int numero = Integer.parseInt(sc.nextLine());`. Probé con entrada válida ("5") y obtuve 5. Probé con entrada inválida ("abc") y obtuve `NumberFormatException`.
- **Prueba y resultado:** Entrada "5" → numero = 5 (correcto). Entrada "abc" → excepción (correcto, se documenta como limitación).
- **Evidencia enlazada:** [Commit jkl012](https://github.com/ejemplo/minijarvis-h1/commit/jkl012)
- **Bloqueo:** `NumberFormatException` con entrada no numérica. No se gestiona en H1; se documenta.
- **Uso de IA:** Sí. Pregunté por qué `Integer.parseInt("abc")` falla (ver registro IA S212).
- **Próximo paso:** S213: añadir comparaciones y if/else.

---

## S213 — Comparaciones y if/else

- **Fecha:** 2026-10-14
- **Sesión:** S213
- **Hit:** H1
- **Objetivo:** Implementar comparaciones y `if/else` para decidir la salida.
- **Acción:** Añadí `if (numero > 0) { System.out.println("El doble de " + numero + " es " + doble); } else { System.out.println("El número no es positivo."); }`. Probé con numero = 5 (rama if) y numero = -3 (rama else).
- **Prueba y resultado:**
  - Caso A (numero = 5): `5 > 0` → `true` → "El doble de 5 es 10." ✓
  - Caso B (numero = -3): `-3 > 0` → `false` → "El número no es positivo." ✓
- **Evidencia enlazada:** [Commit ghi789](https://github.com/ejemplo/minijarvis-h1/commit/ghi789)
- **Bloqueo:** Ninguno.
- **Uso de IA:** No. Trabajé de forma independiente.
- **Próximo paso:** S214: crear el README y completar las evidencias.

---

## S214 — README, evidencias y Sites

- **Fecha:** 2026-10-15
- **Sesión:** S214
- **Hit:** H1
- **Objetivo:** Crear el README H1, verificar evidencias, completar Sites.
- **Acción:** Redacté el README con: qué hace, requisitos, ejemplo reproducible, decisiones técnicas, microprácticas, limitaciones y versión evaluada. Verifiqué que todos los enlaces funcionen y tengan los permisos correctos. Completé mi página H1 en el Site personal.
- **Prueba y resultado:** El README está en la raíz del repositorio. Todos los enlaces son profundos y accesibles.
- **Evidencia enlazada:** [README-h1-completo.md](https://github.com/ejemplo/minijarvis-h1/blob/h1-entrega/README.md), [Portfolio H1](https://ana.ejemplo.com/h1)
- **Bloqueo:** Ninguno.
- **Uso de IA:** No.
- **Próximo paso:** S215: defensa, retrospectiva y entrega en Moodle.

---

## S215 — Defensa, retrospectiva y entrega final

- **Fecha:** 2026-10-17
- **Sesión:** S215
- **Hit:** H1
- **Objetivo:** Defender el producto, cerrar la retrospectiva y entregar en Moodle.
- **Acción:** Defendí el producto oralmente: señalé el punto de entrada, las variables, la constante, ejecuté con entrada ficticia, expliqué la conversión y el error, probé los dos casos de if/else. Completé la retrospectiva del equipo en Scrum. Entregué en Moodle con todos los enlaces.
- **Prueba y resultado:** Defensa superada. Entrega en Moodle completada.
- **Evidencia enlazada:** [Moodle H1](https://moodle.example.com/mod/assign/view.php?id=123), [Retrospectiva Scrum](https://sheets.example.com/scrum-h1#retrospectiva)
- **Bloqueo:** Ninguno.
- **Uso de IA:** No.
- **Próximo paso:** H2: implementar menú con bucles y gestión de errores.

---

## Resumen final H1

**Una cosa que ahora puedo hacer por mi cuenta:**
- Explicar y escribir código Java que usa variables, constantes, operaciones aritméticas, comparaciones e `if/else`. Puedo predecir el resultado de una ejecución antes de correrla.

**Una cosa que aún necesito apoyo con:**
- Gestión de errores con `try/catch`. No lo hemos visto en H1, pero sé que es necesario para manejar entradas inválidas de forma elegante.

**Una evidencia que demuestra mi capacidad:**
- [Commit ghi789](https://github.com/ejemplo/minijarvis-h1/commit/ghi789): implementé la lógica `if/else` desde cero, sin ayuda de IA, y la probé con ambos casos (true y false).

**Un próximo paso para H2:**
- Implementar un menú con bucle `while` para que el usuario pueda hacer varias consultas sin reiniciar el programa.
