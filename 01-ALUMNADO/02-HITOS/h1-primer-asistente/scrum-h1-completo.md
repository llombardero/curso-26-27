# Scrum H1 — Sheet de equipo completado (MiniJarvis)

## Equipo

- **Nombre del equipo:** MiniJarvis Team
- **Miembros:**
  - Ana García (ana.garcia@ejemplo.com)
  - Carlos López (carlos.lopez@ejemplo.com)

---

## Backlog H1

| ID | Tarea | Responsable | Estado | Sesión | Enlace a evidencia |
|---|---|---|---|---|---|
| 1 | Entender alcance H1 | Ana, Carlos | Done | S206 | [Diario S206](https://sheets.example.com/diario-h1#S206) |
| 2 | Definir que entra en H1 | Ana, Carlos | Done | S206 | [Scrum S206](https://sheets.example.com/scrum-h1#S206) |
| 3 | Definir que queda fuera de H1 | Ana, Carlos | Done | S206 | [Scrum S206](https://sheets.example.com/scrum-h1#S206) |
| 4 | Escribir requisitos comprobables | Ana, Carlos | Done | S206 | [Scrum S206](https://sheets.example.com/scrum-h1#S206) |
| 5 | Primera ejecución por consola | Ana | Done | S207 | [Commit abc123](https://github.com/ejemplo/minijarvis-h1/commit/abc123) |
| 6 | Estructura mínima de la clase | Ana | Done | S208 | [Commit abc123](https://github.com/ejemplo/minijarvis-h1/commit/abc123) |
| 7 | Corregir error de sintaxis | Ana | Done | S208 | [Incidencia H1](https://github.com/ejemplo/minijarvis-h1/blob/h1-entrega/incidencia-h1-completo.md) |
| 8 | Decidir mensaje de saludo | Ana, Carlos | Done | S209 | [Scrum S209](https://sheets.example.com/scrum-h1#S209) |
| 9 | Implementar mensaje de saludo | Ana | Done | S209 | [Commit def456](https://github.com/ejemplo/minijarvis-h1/commit/def456) |
| 10 | Crear plan de datos | Ana, Carlos | Done | S210 | [Scrum S210](https://sheets.example.com/scrum-h1#S210) |
| 11 | Implementar variables y tipos | Ana | Done | S210 | [Commit def456](https://github.com/ejemplo/minijarvis-h1/commit/def456) |
| 12 | Implementar constante final | Ana | Done | S211 | [Commit def456](https://github.com/ejemplo/minijarvis-h1/commit/def456) |
| 13 | Implementar operación aritmética | Ana | Done | S211 | [Commit def456](https://github.com/ejemplo/minijarvis-h1/commit/def456) |
| 14 | Registrar predicción y resultado | Ana | Done | S211 | [Diario S211](https://sheets.example.com/diario-h1#S211) |
| 15 | Implementar Scanner para lectura | Carlos | Done | S212 | [Commit jkl012](https://github.com/ejemplo/minijarvis-h1/commit/jkl012) |
| 16 | Implementar conversión de entrada | Carlos | Done | S212 | [Commit jkl012](https://github.com/ejemplo/minijarvis-h1/commit/jkl012) |
| 17 | Probar conversión con entrada válida | Carlos | Done | S212 | [Diario S212](https://sheets.example.com/diario-h1#S212) |
| 18 | Probar conversión con entrada inválida | Carlos | Done | S212 | [Diario S212](https://sheets.example.com/diario-h1#S212) |
| 19 | Implementar comparación y if/else | Ana | Done | S213 | [Commit ghi789](https://github.com/ejemplo/minijarvis-h1/commit/ghi789) |
| 20 | Probar rama if (true) | Ana | Done | S213 | [Diario S213](https://sheets.example.com/diario-h1#S213) |
| 21 | Probar rama else (false) | Ana | Done | S213 | [Diario S213](https://sheets.example.com/diario-h1#S213) |
| 22 | Crear README H1 | Ana, Carlos | Done | S214 | [README-h1-completo.md](https://github.com/ejemplo/minijarvis-h1/blob/h1-entrega/README.md) |
| 23 | Verificar permisos de enlaces | Ana, Carlos | Done | S214 | [Moodle H1](https://moodle.example.com/mod/assign/view.php?id=123) |
| 24 | Completar Sites personales H1 | Ana, Carlos | Done | S214-S215 | [Portfolio Ana](https://ana.ejemplo.com/h1), [Portfolio Carlos](https://carlos.ejemplo.com/h1) |
| 25 | Completar Site de equipo H1 | Ana, Carlos | Done | S215 | [Site equipo](https://equipo.ejemplo.com/h1) |
| 26 | Entrega oficial en Moodle | Ana, Carlos | Done | S215 | [Moodle H1](https://moodle.example.com/mod/assign/view.php?id=123) |

---

## Decisiones del equipo

| Sesión | Decisión | Alternativas descartadas | Motivo | Responsable |
|---|---|---|---|---|
| S206 | H1 consiste en: un asistente de consola que lee nombre y número, calcula el doble, y usa if/else para decidir la salida. | Menú con opciones, bucles, conexión con IA real | Mantener el alcance mínimo para H1; lo demás va en H2 | Ana, Carlos |
| S209 | Mensaje de saludo: "Hola, " + nombre | "Bienvenido, " + nombre; "Hey, " + nombre | "Hola" es más cercano, no asume género, y se alinea con la idea de un asistente amigable | Ana (decidió), Carlos (aceptó) |
| S210 | Variables: `String nombre`, `int numero`, `int doble`, `final String MENSAJE_BIENVENIDA` | Nombres genéricos como `x`, `dato1`, `valor` | Nombres claros y descriptivos facilitan la comprensión y el mantenimiento del código | Ana (propuso), Carlos (aceptó) |
| S212 | Usar `Scanner` con `nextLine()` + `Integer.parseInt()` | `BufferedReader`, `Console.readLine()` | `Scanner` es más sencillo para principiantes y está en el temario del Tema 1 | Carlos (implementó) |
| S213 | `if (numero > 0)` → muestra doble; `else` → "no es positivo" | `if (numero >= 0)`, `if (numero != 0)` | `>` es la comparación más directa para "positivo". `>= 0` incluiría el cero como positivo, lo cual es debatible | Ana (decidió) |

---

## Bloqueos registrados

| Sesión | Bloqueo | Resolución | Responsable |
|---|---|---|---|
| S208 | Error de compilación: olvidé el `;` al final de `System.out.println("Hola")` | Añadí el `;`. El compilador indica la línea exacta del error. | Ana |
| S211 | Error al reasignar constante `final int DOBLE_FACTOR = 2; DOBLE_FACTOR = 3;` | Eliminé la reasignación. `final` no permite cambios. | Ana |
| S212 | `NumberFormatException` al introducir "abc" como número | No se gestiona en H1. Se documenta como limitación en el README. Se abordará con `try/catch` en H2. | Carlos |

---

## Mini-revisión (S214)

**¿Qué hemos logrado en H1?**
- Un programa funcional que lee entrada, procesa datos y produce salida.
- Uso correcto de variables, constantes, operaciones, comparaciones e `if/else`.
- Código documentado con comentarios y README completo.
- Evidencias en GitHub, diario individual, Scrum y Sites.

**¿Qué nos ha costado?**
- Entender la diferencia entre `final` y `static`.
- Gestionar errores de conversión (quedó fuera de H1).
- Coordinar los commits entre miembros del equipo.

---

## Retrospectiva final (S215)

**¿Qué funcionó bien?**
- La división de tareas: Ana se centró en la lógica y estructura; Carlos en la entrada y pruebas.
- Los commits frecuentes y con mensajes descriptivos.
- El uso del Scrum Sheet para registrar decisiones y bloqueos.

**¿Qué no funcionó bien?**
- Tardamos más de lo esperado en entender `final` vs `static`.
- No probamos suficientes casos de prueba en S213 (solo probamos el caso positivo primero).

**¿Qué mantendremos en H2?**
- Commits frecuentes con mensajes descriptivos.
- Registro de decisiones en Scrum.
- Pruebas de ambos ramas (if y else) antes de considerar una funcionalidad como "done".

**¿Qué cambiaremos en H2?**
- Empezar con más casos de prueba antes de implementar.
- Documentar las limitaciones del código en el README desde el inicio, no al final.
- Revisar los enlaces de Moodle antes de entregar para evitar errores de permisos.
