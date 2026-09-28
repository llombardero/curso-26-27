# Mi aportación verificable — H1 (Ana García)

## Mi aportación verificable

- **Qué hice yo:** Diseñé el flujo principal del programa: estructura de la clase, constantes, variables, lectura de entrada, cálculo del doble, y la lógica `if/else` para decidir la salida según si el número es positivo o no. Escribí el código de `Main.java` desde cero, hice los commits de cada sesión (S207 a S213), y redacté la sección de decisiones técnicas del README.
- **Resultado observable:** El programa lee un nombre y un número, calcula el doble del número y muestra un mensaje diferente si el número es positivo o negativo. Funciona correctamente con entradas válidas.
- **Enlace profundo al commit, prueba o fila Scrum:**
  - Commit S207 (primera ejecución): [abc123](https://github.com/ejemplo/minijarvis-h1/commit/abc123)
  - Commit S211 (constante final): [def456](https://github.com/ejemplo/minijarvis-h1/commit/def456)
  - Commit S213 (if/else): [ghi789](https://github.com/ejemplo/minijarvis-h1/commit/ghi789)
  - Fila Scrum S210 (plan de datos): [Scrum S210](https://sheets.example.com/scrum-h1#S210)

## Concepto del Tema 1

- **Concepto que ahora puedo explicar:** La diferencia entre variable y constante. Una variable puede cambiar su valor durante la ejecución (`int numero = 5; numero = 10;`), mientras que una constante declarada con `final` no puede reasignarse (`final String SALUDO = "Hola";`).
- **Ejemplo propio:**
  ```java
  final String SALUDO = "Hola";  // No se puede cambiar
  String nombre = "Ana";         // Se puede cambiar: nombre = "Carlos";
  ```
- **Error o confusión que resolví:** Al principio confundía `final` con `static`. `static` significa que pertenece a la clase; `final` significa que no se puede reasignar. Pueden combinarse (`static final`) pero son conceptos independientes. Lo aclaré en la fila S211 del diario.

## Prueba seleccionada

- **Entrada o caso:** Nombre = "Ana", Número = 5
- **Resultado esperado:**
  ```
  Hola, Ana. Bienvenida a MiniJarvis.
  El doble de 5 es 10.
  ```
- **Resultado obtenido:**
  ```
  Hola, Ana. Bienvenida a MiniJarvis.
  El doble de 5 es 10.
  ```
- **Qué demuestra:** Que el programa lee entrada por teclado, almacena datos en variables, realiza una operación aritmética (`numero * 2`), y ejecuta la rama `if` cuando la condición `numero > 0` es `true`.
- **Enlace a README, código o diario:**
  - README: [Ejemplo reproducible](https://github.com/ejemplo/minijarvis-h1/blob/h1-entrega/README.md#ejemplo-reproducible)
  - Código: [Main.java línea 20-24](https://github.com/ejemplo/minijarvis-h1/blob/ghi789/src/Main.java#L20-L24)
  - Diario: [Fila S213](https://sheets.example.com/diario-h1#S213)

## Decisión o bloqueo significativo

- **Qué ocurrió:** En S209, discutimos si el mensaje de saludo debía ser `"Bienvenido, " + nombre` o `"Hola, " + nombre`. Mi compañara Carlos prefería "Bienvenido" por ser más formal.
- **Qué predije o decidí:** Propuse "Hola" porque es más cercano, no asume género, y se alinea con la idea de un asistente amigable. Argumenté que en un asistente de consola, la cercanía importa más que la formalidad.
- **Qué prueba hice:** Probamos ambos mensajes ejecutando el programa con cada versión. Ambos funcionan igual; la diferencia es puramente estética y de tono.
- **Enlace a las filas del diario; no copies aquí el registro completo:**
  - Diario S209: [Fila de decisión de mensaje](https://sheets.example.com/diario-h1#S209)
  - Scrum S209: [Decisión registrada](https://sheets.example.com/scrum-h1#S209)

## IA, solo si fue relevante

- **Enlace a la fila del diario donde registré petición, cambio y validación:**
  - Diario S210: [Uso de IA para entender tipos](https://sheets.example.com/diario-h1#S210)
- **Qué parte puedo defender sin ayuda:**
  - Puedo explicar por qué `String` se usa para texto y `int` para números.
  - Puedo justificar por qué elegí `nombre` como variable en lugar de `x` o `dato1`.
  - Puedo ejecutar el programa, modificar una entrada y predecir el resultado.

## Próximo paso

- **Mejora concreta para H2:** Implementar un menú con bucle `while` para que el usuario pueda hacer varias consultas sin reiniciar el programa.

## Comprobación

- [x] He seleccionado evidencias, no copiado el diario.
- [x] Todos los enlaces son profundos y abren con permisos restringidos.
- [x] No aparecen secretos, datos personales ni calificaciones.
- [x] Puedo ejecutar, explicar y modificar la parte enlazada.
