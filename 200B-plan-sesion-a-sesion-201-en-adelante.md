# Plan sesión a sesión — Numeración 201 en adelante

## Programación orientada a objetos — MiniJarvis — Curso 2026/2027

Este documento desarrolla el curso sesión a sesión a partir de la guía integral `23-guia-docente-integral-plan-clases-scrum-hexa.md` y de los materiales existentes del itinerario MiniJarvis.

La numeración empieza en la sesión `201`, como se ha solicitado.

---

## 1. Cómo usar este documento

Cada sesión está pensada como un bloque docente flexible de entre 45 y 135 minutos.

Si un día hay varios periodos seguidos, se puede impartir una sesión completa. Si el ritmo del grupo es lento, una sesión puede dividirse en dos clases reales.

Estructura de cada sesión:

| Campo | Significado |
|---|---|
| Hito | Parte del proyecto en la que se encuadra. |
| Foco | Qué debe quedar aprendido o producido. |
| Explicar | Concepto clave que debe aparecer en ese momento. |
| Actividad | Qué hace el alumnado. |
| Evidencia | Qué debe quedar registrado, entregado o comprobado. |
| Cierre | Pregunta, revisión o microdefensa. |

Regla de uso:

```text
No avanzar a la siguiente sesión si la evidencia mínima de la sesión actual no existe o no es defendible.
```

---

## 2. Vista global de sesiones

| Rango | Bloque | Foco |
|---|---|---|
| 201-205 | H0 | Presentación, Scrum, torre de papel y equipos. |
| 206-215 | H1 | Java básico, IntelliJ, variables, constantes, entrada/salida y README. |
| 216-228 | H2 | Menú, bucles, condicionales, pruebas y depuración. |
| 229-241 | H3 | Colecciones, memoria temporal, casos límite y cierre C1. |
| 242-257 | H4 | Programación orientada a objetos, clases, responsabilidades y UML. |
| 258-274 | H5 | Extensibilidad, refactorización, Git, clean code y patrones iniciales. |
| 275-278 | C2 | Cierre segunda evaluación, defensa y recuperación. |
| 279-291 | H6 | Persistencia, ficheros, logs, reproducibilidad y seguridad. |
| 292-296 | H7 | IA responsable real o simulada. |
| 297-306 | HF | Portfolio final, demo, defensa, recuperación y mejora. |

---

## 3. Sesiones H0 — Bootcamp Scrum y torre de papel

### Sesión 201 — Presentación del curso y narrativa MiniJarvis

| Campo | Desarrollo |
|---|---|
| Hito | H0 |
| Foco | Entender que el curso se trabajará por proyecto, hitos, evidencias y defensa. |
| Explicar | MiniJarvis no será una IA completa desde el primer día; será un programa que crecerá por versiones. |
| Actividad | Ideas previas: qué creen que es un agente, qué debería hacer y qué riesgos tiene usar IA. |
| Evidencia | Ticket inicial individual con expectativas, miedos y conocimientos previos. |
| Cierre | Pregunta: ¿qué significa que una entrega sea defendible? |

### Sesión 202 — Reglas de trabajo, IA responsable y evidencias

| Campo | Desarrollo |
|---|---|
| Hito | H0 |
| Foco | Fijar normas del curso desde el inicio. |
| Explicar | Semáforo IA: verde, amarillo y rojo. Diferencia entre ayuda, copia y autoría oculta. |
| Actividad | Clasificar ejemplos de uso de IA en verde, amarillo o rojo. |
| Evidencia | Mini registro de IA simulado con objetivo, prompt, resultado, verificación y aprendizaje. |
| Cierre | Pregunta: ¿qué uso de IA invalidaría una evidencia? |

### Sesión 203 — Scrum vivido: preparación de la torre de papel

| Campo | Desarrollo |
|---|---|
| Hito | H0 |
| Foco | Formar equipos, roles y backlog inicial. |
| Explicar | Producto, sprint, backlog, rol, tarea, criterio de terminado y bloqueo. |
| Actividad | Crear equipos de 3-4, asignar roles y redactar al menos 5 tareas para construir la torre. |
| Evidencia | Tablero inicial del equipo y contrato breve de trabajo. |
| Cierre | Revisión rápida del tablero: ninguna tarea debe ser ambigua. |

### Sesión 204 — Sprint de torre de papel, review y retrospectiva

| Campo | Desarrollo |
|---|---|
| Hito | H0 |
| Foco | Experimentar Scrum en un reto físico. |
| Explicar | Review frente a retrospectiva: revisar producto no es lo mismo que revisar proceso. |
| Actividad | Construcción de torre, medición, review y retrospectiva. |
| Evidencia | Foto o descripción de torre, tablero final y retrospectiva. |
| Cierre | Cada equipo formula una mejora concreta para el siguiente sprint. |

### Sesión 205 — Transferencia de Scrum a MiniJarvis

| Campo | Desarrollo |
|---|---|
| Hito | H0 |
| Foco | Traducir la experiencia de la torre al proyecto software. |
| Explicar | Incremento funcional, demo, prueba, documentación y defensa. |
| Actividad | Crear primer tablero general de MiniJarvis y acordar normas de equipo. |
| Evidencia | Contrato de equipo definitivo y tablero base. |
| Cierre | Pregunta: ¿qué aprendimos de la torre que servirá al programar? |

---

## 4. Sesiones H1 — Primer asistente básico

### Sesión 206 — Presentar H1 y delimitar alcance

| Campo | Desarrollo |
|---|---|
| Hito | H1 |
| Foco | Comprender el producto mínimo H1. |
| Explicar | H1 será lineal: saludo, nombre, mensajes y constantes. No habrá menú ni bucles. |
| Actividad | Clasificar ideas en tres columnas: H1, más adelante, no adecuado. |
| Evidencia | Lista de requisitos H1 y lista de restricciones. |
| Cierre | Pregunta: ¿por qué no conviene empezar con IA real? |

### Sesión 207 — Entorno de trabajo: IntelliJ, proyecto y ejecución

| Campo | Desarrollo |
|---|---|
| Hito | H1 |
| Foco | Crear y ejecutar un proyecto Java mínimo. |
| Explicar | Código fuente, proyecto, JDK, compilación, ejecución y consola. |
| Actividad | Crear proyecto en IntelliJ, clase `Main` y primer `println`. |
| Evidencia | Captura o documento de primera ejecución. |
| Cierre | Cada alumno localiza dónde está `Main.java`. |

### Sesión 208 — Estructura mínima de un programa Java

| Campo | Desarrollo |
|---|---|
| Hito | H1 |
| Foco | Entender clase `Main` y método `main`. |
| Explicar | `public class Main`, `public static void main(String[] args)` y orden de ejecución. |
| Actividad | Reescribir un programa mínimo y señalar dónde empieza. |
| Evidencia | Código que compila con varios mensajes por pantalla. |
| Cierre | Microdefensa: señalar en el código dónde empieza el programa. |

### Sesión 209 — Salida por pantalla y mensajes del asistente

| Campo | Desarrollo |
|---|---|
| Hito | H1 |
| Foco | Usar `System.out.println` y construir salida legible. |
| Explicar | Diferencia entre texto literal, concatenación y orden de mensajes. |
| Actividad | Diseñar el primer guion de presentación de MiniJarvis. |
| Evidencia | Programa que muestra saludo, propósito y curso. |
| Cierre | Revisar si la salida es comprensible para una persona usuaria. |

### Sesión 210 — Variables

| Campo | Desarrollo |
|---|---|
| Hito | H1 |
| Foco | Guardar datos en variables. |
| Explicar | Tipo, nombre, valor y uso de una variable `String`. |
| Actividad | Crear variable `userName` con un valor fijo y usarla en varios mensajes. |
| Evidencia | Código con variable usada correctamente. |
| Cierre | Pregunta: ¿qué cambia si modifico el valor de la variable? |

### Sesión 211 — Constantes

| Campo | Desarrollo |
|---|---|
| Hito | H1 |
| Foco | Diferenciar variable y constante. |
| Explicar | `final`, nombres claros y datos que no deberían cambiar. |
| Actividad | Añadir `ASSISTANT_NAME` y `COURSE_YEAR`. |
| Evidencia | Código con al menos una constante bien usada. |
| Cierre | Pregunta: ¿qué dato de nuestro programa debería ser constante? |

### Sesión 212 — Entrada por teclado con Scanner

| Campo | Desarrollo |
|---|---|
| Hito | H1 |
| Foco | Leer el nombre de la persona usuaria. |
| Explicar | `import`, `Scanner`, `nextLine()` y cierre del scanner. |
| Actividad | Pedir nombre por consola y responder usando ese dato. |
| Evidencia | Ejecución donde el programa saluda usando el nombre introducido. |
| Cierre | Microdefensa: explicar qué hace `scanner.nextLine()`. |

### Sesión 213 — Limpieza, nombres claros y simplicidad

| Campo | Desarrollo |
|---|---|
| Hito | H1 |
| Foco | Mejorar legibilidad sin añadir complejidad. |
| Explicar | Código limpio inicial: nombres, orden, comentarios útiles y ausencia de adornos. |
| Actividad | Revisar el código H1 con una checklist sencilla. |
| Evidencia | Código H1 limpio, simple y ejecutable. |
| Cierre | Pregunta: ¿qué parte sobra o no sabes explicar? |

### Sesión 214 — README y evidencia de ejecución

| Campo | Desarrollo |
|---|---|
| Hito | H1 |
| Foco | Documentar cómo ejecutar H1. |
| Explicar | README mínimo: qué hace, cómo se ejecuta, ejemplo de salida y limitaciones. |
| Actividad | Crear `README.md` y evidencia de ejecución. |
| Evidencia | README H1 y documento/captura de ejecución. |
| Cierre | Intercambio: otro equipo intenta entender el README. |

### Sesión 215 — Defensa y cierre H1

| Campo | Desarrollo |
|---|---|
| Hito | H1 |
| Foco | Validar comprensión individual. |
| Explicar | Cómo se defiende una entrega técnica breve. |
| Actividad | Defensa: `main`, variable, constante, `Scanner`, ejecución y límites de H1. |
| Evidencia | Plantilla de defensa H1 y portfolio individual. |
| Cierre | Decidir qué debe mejorar cada alumno antes de H2. |

---

## 5. Sesiones H2 — Decisiones, menú y depuración

### Sesión 216 — Presentar H2 desde H1

| Campo | Desarrollo |
|---|---|
| Hito | H2 |
| Foco | Entender la diferencia entre programa lineal e interactivo. |
| Explicar | H2 añade menú, comandos y repetición hasta `salir`. |
| Actividad | Comparar salida H1 con comportamiento esperado H2. |
| Evidencia | Tabla H1 frente a H2. |
| Cierre | Pregunta: ¿qué necesitamos para que el programa no termine? |

### Sesión 217 — Diseño de comandos antes de programar

| Campo | Desarrollo |
|---|---|
| Hito | H2 |
| Foco | Definir comportamiento comprobable. |
| Explicar | Un comando está bien definido si se puede probar. |
| Actividad | Completar tabla de comandos: `ayuda`, `saluda`, `estado`, `salir`, `otro`. |
| Evidencia | Tabla de comandos con respuesta esperada. |
| Cierre | Revisar si todos los comandos tienen criterio de aceptación. |

### Sesión 218 — Booleanos y variable de control

| Campo | Desarrollo |
|---|---|
| Hito | H2 |
| Foco | Controlar si el programa sigue o termina. |
| Explicar | Variable `boolean running = true`. |
| Actividad | Añadir variable de control al programa. |
| Evidencia | Código preparado para repetir ejecución. |
| Cierre | Pregunta: ¿cuándo debe cambiar `running` a `false`? |

### Sesión 219 — Bucle `while`

| Campo | Desarrollo |
|---|---|
| Hito | H2 |
| Foco | Repetir lectura de comandos. |
| Explicar | Estructura `while (running)` y flujo de repetición. |
| Actividad | Implementar bucle que pide comandos hasta una condición. |
| Evidencia | Programa que repite prompt `>`. |
| Cierre | Dibujar el flujo del bucle en pizarra o cuaderno. |

### Sesión 220 — Condicionales `if/else`

| Campo | Desarrollo |
|---|---|
| Hito | H2 |
| Foco | Ejecutar una respuesta según comando. |
| Explicar | `if`, `else if`, `else` y orden de evaluación. |
| Actividad | Implementar `ayuda`, `estado` y comando desconocido. |
| Evidencia | Menú parcial funcional. |
| Cierre | Pregunta: ¿qué rama se ejecuta con un comando inventado? |

### Sesión 221 — Comparación de textos en Java

| Campo | Desarrollo |
|---|---|
| Hito | H2 |
| Foco | Evitar el error de usar `==` con cadenas. |
| Explicar | `.equals()`, `trim()` y `toLowerCase()`. |
| Actividad | Corregir comparación de comandos y normalizar entrada. |
| Evidencia | Comandos funcionan con espacios o mayúsculas si se decide soportarlo. |
| Cierre | Microdefensa: explicar por qué no usamos `==`. |

### Sesión 222 — Comando `salir` y cierre controlado

| Campo | Desarrollo |
|---|---|
| Hito | H2 |
| Foco | Terminar el programa correctamente. |
| Explicar | Salida controlada, mensaje final y cambio de estado. |
| Actividad | Implementar `salir` modificando `running`. |
| Evidencia | El programa termina solo cuando se escribe `salir`. |
| Cierre | Prueba oral: ¿qué línea provoca la salida? |

### Sesión 223 — `switch` como alternativa controlada

| Campo | Desarrollo |
|---|---|
| Hito | H2 |
| Foco | Conocer alternativa a `if/else` sin obligarla. |
| Explicar | `switch` para múltiples opciones. |
| Actividad | Comparar versión `if/else` y versión `switch` en ejemplo pequeño. |
| Evidencia | Decisión documentada: mantener `if/else` o usar `switch`. |
| Cierre | Pregunta: ¿cuál entiendes mejor y por qué? |

### Sesión 224 — Pruebas manuales

| Campo | Desarrollo |
|---|---|
| Hito | H2 |
| Foco | Comprobar comportamiento antes de entregar. |
| Explicar | Caso de prueba, entrada, resultado esperado, resultado obtenido e incidencia. |
| Actividad | Crear plan de pruebas para todos los comandos. |
| Evidencia | `docs/pruebas-h2.md`. |
| Cierre | Ejecutar al menos un caso delante de otro equipo. |

### Sesión 225 — Depuración con breakpoint

| Campo | Desarrollo |
|---|---|
| Hito | H2 |
| Foco | Observar el programa mientras se ejecuta. |
| Explicar | Breakpoint, variables observadas y ejecución paso a paso. |
| Actividad | Poner breakpoint tras leer `command` y observar `command`, `running`, `userName`. |
| Evidencia | `docs/depuracion-h2.md` con captura o descripción. |
| Cierre | Pregunta: ¿qué valor tenía `command` antes de entrar en el condicional? |

### Sesión 226 — Incidencias y corrección de errores

| Campo | Desarrollo |
|---|---|
| Hito | H2 |
| Foco | Documentar un fallo real y su solución. |
| Explicar | Una incidencia no es un fracaso; es evidencia de aprendizaje. |
| Actividad | Registrar un error encontrado, causa, solución y prueba posterior. |
| Evidencia | `docs/incidencia-h2.md`. |
| Cierre | Compartir una incidencia útil con la clase. |

### Sesión 227 — Comparación Java-Python H2

| Campo | Desarrollo |
|---|---|
| Hito | H2 |
| Foco | Comparar control de flujo entre Java y Python. |
| Explicar | La comparación busca comprensión, no memorizar Python. |
| Actividad | Analizar versión Python generada o guiada y señalar equivalencias. |
| Evidencia | `docs/comparacion-java-python-h2.md`. |
| Cierre | Pregunta: ¿dónde está el equivalente del `while`? |

### Sesión 228 — Demo, defensa y cierre H2

| Campo | Desarrollo |
|---|---|
| Hito | H2 |
| Foco | Validar menú, pruebas y depuración. |
| Explicar | La defensa puede pedir modificar un comando en directo. |
| Actividad | Demo por equipo y defensa individual breve. |
| Evidencia | Defensa H2, README actualizado y registro IA si procede. |
| Cierre | Lista de condiciones para poder empezar H3. |

---

## 6. Sesiones H3 — Memoria temporal y colecciones

### Sesión 229 — Presentar H3: MiniJarvis empieza a recordar

| Campo | Desarrollo |
|---|---|
| Hito | H3 |
| Foco | Comprender memoria temporal. |
| Explicar | H2 responde, pero no recuerda. H3 guardará datos mientras el programa está abierto. |
| Actividad | Probar H2 y detectar qué información se pierde. |
| Evidencia | Lista de necesidades de memoria. |
| Cierre | Pregunta: ¿qué debe recordar MiniJarvis en H3? |

### Sesión 230 — Elegir qué información guardar

| Campo | Desarrollo |
|---|---|
| Hito | H3 |
| Foco | Definir memoria antes de codificar. |
| Explicar | No se elige colección sin saber qué datos se necesitan. |
| Actividad | Decidir si se guardan recuerdos, preferencias, mensajes o historial simple. |
| Evidencia | Documento breve de decisión de memoria. |
| Cierre | Cada equipo justifica qué información guardará. |

### Sesión 231 — Introducción a `ArrayList`

| Campo | Desarrollo |
|---|---|
| Hito | H3 |
| Foco | Guardar varios elementos en orden. |
| Explicar | Lista, índice, añadir, recorrer y tamaño. |
| Actividad | Mini-reto fuera del proyecto: lista de tareas o palabras. |
| Evidencia | Ejemplo pequeño de `ArrayList` que compila. |
| Cierre | Pregunta: ¿por qué una variable simple no basta? |

### Sesión 232 — Introducción a `HashMap`

| Campo | Desarrollo |
|---|---|
| Hito | H3 |
| Foco | Entender almacenamiento por clave y valor. |
| Explicar | Diferencia entre lista ordenada y mapa por clave. |
| Actividad | Mini-reto: guardar preferencias por clave. |
| Evidencia | Comparación `ArrayList` frente a `HashMap`. |
| Cierre | Decidir qué colección usará el equipo y por qué. |

### Sesión 233 — Crear comando `recuerda`

| Campo | Desarrollo |
|---|---|
| Hito | H3 |
| Foco | Guardar información introducida por usuario. |
| Explicar | Añadir elementos a colección y confirmar acción. |
| Actividad | Implementar comando `recuerda`. |
| Evidencia | MiniJarvis guarda al menos un recuerdo. |
| Cierre | Probar guardar dos recuerdos seguidos. |

### Sesión 234 — Crear comando `memoria`

| Campo | Desarrollo |
|---|---|
| Hito | H3 |
| Foco | Consultar información guardada. |
| Explicar | Recorrer colección y mostrar datos. |
| Actividad | Implementar comando `memoria`. |
| Evidencia | MiniJarvis muestra los recuerdos guardados. |
| Cierre | Pregunta: ¿qué ocurre si no hay recuerdos? |

### Sesión 235 — Caso límite: memoria vacía

| Campo | Desarrollo |
|---|---|
| Hito | H3 |
| Foco | Gestionar ausencia de datos. |
| Explicar | Caso límite y mensaje útil para usuario. |
| Actividad | Implementar respuesta para memoria vacía. |
| Evidencia | Prueba de `memoria` antes de guardar nada. |
| Cierre | Añadir caso al plan de pruebas. |

### Sesión 236 — Caso límite: entrada vacía y repetidos

| Campo | Desarrollo |
|---|---|
| Hito | H3 |
| Foco | Validar datos antes de guardarlos. |
| Explicar | Entrada vacía, espacios y duplicados. |
| Actividad | Evitar guardar recuerdos vacíos y decidir qué hacer con repetidos. |
| Evidencia | Pruebas de entrada vacía y repetida. |
| Cierre | Pregunta: ¿qué decisión tomaste y por qué? |

### Sesión 237 — Comando `estado` con memoria

| Campo | Desarrollo |
|---|---|
| Hito | H3 |
| Foco | Usar información interna para responder. |
| Explicar | Tamaño de colección y mensajes derivados del estado. |
| Actividad | Actualizar `estado` para indicar número de recuerdos. |
| Evidencia | `estado` muestra información coherente. |
| Cierre | Probar `estado` antes y después de guardar. |

### Sesión 238 — Pruebas de memoria

| Campo | Desarrollo |
|---|---|
| Hito | H3 |
| Foco | Validar comportamiento de colecciones. |
| Explicar | Pruebas específicas de memoria: guardar, listar, vacío, repetidos y entradas inválidas. |
| Actividad | Completar `docs/pruebas-memoria-h3.md`. |
| Evidencia | Plan de pruebas H3 ejecutado. |
| Cierre | Cada equipo muestra un caso que falló y fue corregido. |

### Sesión 239 — Comparación Java-Python H3

| Campo | Desarrollo |
|---|---|
| Hito | H3 |
| Foco | Comparar colecciones Java con `list` y `dict`. |
| Explicar | Java exige tipos y clases concretas; Python es más flexible. |
| Actividad | Relacionar `ArrayList` con `list` y `HashMap` con `dict`. |
| Evidencia | `docs/comparacion-java-python-h3.md`. |
| Cierre | Pregunta: ¿qué estructura se parece más a tu solución? |

### Sesión 240 — Portfolio y defensa H3

| Campo | Desarrollo |
|---|---|
| Hito | H3 |
| Foco | Defender memoria temporal y elección de colección. |
| Explicar | Una elección técnica debe poder justificarse. |
| Actividad | Preparar portfolio y defensa H3. |
| Evidencia | Portfolio H3 y defensa individual. |
| Cierre | Pregunta de defensa: ¿por qué esa colección y no otra? |

### Sesión 241 — Cierre C1: demo parcial y recuperación

| Campo | Desarrollo |
|---|---|
| Hito | C1 |
| Foco | Consolidar H1-H3 antes de POO. |
| Explicar | Antes de entrar en clases, hay que dominar estructura, control de flujo y colecciones. |
| Actividad | Demo parcial, revisión de evidencias y recuperación individual. |
| Evidencia | Checklist C1 con RA pendientes y plan de mejora. |
| Cierre | Cada alumno identifica qué sabe defender y qué debe recuperar. |

---

## 7. Sesiones H4 — Programación orientada a objetos

### Sesión 242 — Presentar H4: por qué necesitamos POO

| Campo | Desarrollo |
|---|---|
| Hito | H4 |
| Foco | Motivar POO desde un problema real. |
| Explicar | Todo en `Main` empieza a ser difícil de mantener. |
| Actividad | Revisar H3 y marcar responsabilidades mezcladas. |
| Evidencia | Lista de problemas del código H3. |
| Cierre | Pregunta: ¿qué responsabilidades distintas aparecen en nuestro programa? |

### Sesión 243 — Clase y objeto

| Campo | Desarrollo |
|---|---|
| Hito | H4 |
| Foco | Entender la diferencia entre clase y objeto. |
| Explicar | Clase como plantilla; objeto como instancia concreta. |
| Actividad | Ejemplos fuera de MiniJarvis y luego dentro del proyecto. |
| Evidencia | Definición propia de clase y objeto con ejemplo. |
| Cierre | Pregunta: ¿MiniJarvis podría ser un objeto? |

### Sesión 244 — Atributos y métodos

| Campo | Desarrollo |
|---|---|
| Hito | H4 |
| Foco | Separar qué sabe y qué hace una clase. |
| Explicar | Atributos como estado; métodos como comportamiento. |
| Actividad | Diseñar tarjeta CRC simple de `Agent` y `Memory`. |
| Evidencia | Tabla: clase, atributos, métodos y responsabilidad. |
| Cierre | Pregunta: ¿qué sabe `Memory` y qué hace `Memory`? |

### Sesión 245 — Constructor y estado inicial

| Campo | Desarrollo |
|---|---|
| Hito | H4 |
| Foco | Crear objetos correctamente inicializados. |
| Explicar | Constructor, parámetros y estado válido. |
| Actividad | Crear clase `Memory` con constructor. |
| Evidencia | `Memory` inicializada sin romper comandos existentes. |
| Cierre | Microdefensa: ¿cuándo se ejecuta el constructor? |

### Sesión 246 — Encapsulación

| Campo | Desarrollo |
|---|---|
| Hito | H4 |
| Foco | Proteger datos internos. |
| Explicar | `private`, métodos públicos y acceso controlado. |
| Actividad | Hacer privada la colección de memoria y acceder mediante métodos. |
| Evidencia | Código sin acceso directo innecesario a atributos. |
| Cierre | Pregunta: ¿por qué no dejamos la lista pública? |

### Sesión 247 — Extraer clase `Memory`

| Campo | Desarrollo |
|---|---|
| Hito | H4 |
| Foco | Pasar de colección suelta a objeto con responsabilidad. |
| Explicar | Refactorizar sin cambiar comportamiento observable. |
| Actividad | Mover operaciones de memoria a la clase `Memory`. |
| Evidencia | Comandos `recuerda`, `memoria` y `estado` siguen funcionando. |
| Cierre | Prueba de regresión manual. |

### Sesión 248 — Extraer clase `Agent`

| Campo | Desarrollo |
|---|---|
| Hito | H4 |
| Foco | Sacar flujo principal de `Main`. |
| Explicar | `Main` arranca; `Agent` coordina. |
| Actividad | Crear `Agent` con método de ejecución. |
| Evidencia | `Main` queda reducido a crear y lanzar el agente. |
| Cierre | Pregunta: ¿qué responsabilidad conserva `Main`? |

### Sesión 249 — Relaciones entre clases

| Campo | Desarrollo |
|---|---|
| Hito | H4 |
| Foco | Entender colaboración entre objetos. |
| Explicar | Un objeto puede usar otro objeto para cumplir su responsabilidad. |
| Actividad | Analizar relación `Agent` -> `Memory`. |
| Evidencia | Descripción textual de relaciones del diseño. |
| Cierre | Pregunta: ¿quién debe guardar recuerdos, `Agent` o `Memory`? |

### Sesión 250 — Diagrama de clases I

| Campo | Desarrollo |
|---|---|
| Hito | H4 |
| Foco | Representar diseño en UML básico. |
| Explicar | Clase, atributo, método y relación en diagrama. |
| Actividad | Dibujar diagrama de clases actual. |
| Evidencia | `docs/diagrama-clases-h4.md` versión inicial. |
| Cierre | Revisar si el diagrama coincide con el código. |

### Sesión 251 — Diagrama de clases II: relación código-diagrama

| Campo | Desarrollo |
|---|---|
| Hito | H4 |
| Foco | Evitar UML inventado. |
| Explicar | Todo elemento del diagrama debe poder localizarse en el código o justificarse como diseño pendiente. |
| Actividad | Completar relación diagrama-código. |
| Evidencia | `docs/relacion-diagrama-codigo-h4.md`. |
| Cierre | Señalar una relación del diagrama en el código real. |

### Sesión 252 — Diagrama de comportamiento

| Campo | Desarrollo |
|---|---|
| Hito | H4 |
| Foco | Explicar un flujo real del agente. |
| Explicar | Flujo de un comando desde entrada hasta respuesta. |
| Actividad | Dibujar flujo de `recuerda` o `memoria`. |
| Evidencia | `docs/diagrama-comportamiento-h4.md`. |
| Cierre | Pregunta: ¿qué objeto actúa primero y cuál después? |

### Sesión 253 — Revisión de responsabilidades

| Campo | Desarrollo |
|---|---|
| Hito | H4 |
| Foco | Evitar clases decorativas o mezcladas. |
| Explicar | Una clase debe tener una responsabilidad clara. |
| Actividad | Revisar cada clase con preguntas: qué sabe, qué hace, qué no debe hacer. |
| Evidencia | Lista de ajustes de diseño. |
| Cierre | Eliminar o corregir una responsabilidad mal ubicada. |

### Sesión 254 — Comparación Java-Python H4

| Campo | Desarrollo |
|---|---|
| Hito | H4 |
| Foco | Comparar clases Java con clases Python. |
| Explicar | Visibilidad, constructor y convenciones en ambos lenguajes. |
| Actividad | Analizar equivalencias de una clase simple. |
| Evidencia | `docs/comparacion-java-python-h4.md`. |
| Cierre | Pregunta: ¿qué diferencia ves en encapsulación? |

### Sesión 255 — Pruebas de regresión H4

| Campo | Desarrollo |
|---|---|
| Hito | H4 |
| Foco | Asegurar que refactorizar a clases no rompió comportamiento. |
| Explicar | Refactorizar no debe cambiar lo que el usuario observa, salvo decisión explícita. |
| Actividad | Reejecutar pruebas de H3 sobre diseño H4. |
| Evidencia | Checklist de pruebas H4. |
| Cierre | Registrar un fallo provocado por el rediseño si aparece. |

### Sesión 256 — README, portfolio y registro IA H4

| Campo | Desarrollo |
|---|---|
| Hito | H4 |
| Foco | Documentar diseño OO. |
| Explicar | README debe explicar clases principales y cómo ejecutar. |
| Actividad | Actualizar README, portfolio y registro IA. |
| Evidencia | README H4, portfolio y registro IA. |
| Cierre | Otro equipo revisa si entiende el diseño leyendo el README. |

### Sesión 257 — Defensa H4

| Campo | Desarrollo |
|---|---|
| Hito | H4 |
| Foco | Validar comprensión de POO. |
| Explicar | En POO se defiende diseño, no solo código que funciona. |
| Actividad | Defensa individual sobre clase, objeto, atributo, método, constructor, encapsulación y relaciones. |
| Evidencia | Defensa H4. |
| Cierre | Decidir si el equipo está preparado para extensibilidad H5. |

---

## 8. Sesiones H5 — Extensibilidad, clean code y patrones iniciales

### Sesión 258 — Presentar H5: añadir sin romper

| Campo | Desarrollo |
|---|---|
| Hito | H5 |
| Foco | Entender extensibilidad. |
| Explicar | Un diseño extensible permite añadir comandos con bajo impacto. |
| Actividad | Preguntar qué archivos habría que tocar para añadir una herramienta. |
| Evidencia | Diagnóstico de rigidez del diseño H4. |
| Cierre | Pregunta: ¿qué cambio se repite cada vez que añadimos comando? |

### Sesión 259 — Clean code I: nombres y duplicación

| Campo | Desarrollo |
|---|---|
| Hito | H5 |
| Foco | Detectar problemas de legibilidad. |
| Explicar | Nombres claros, duplicación y métodos demasiado largos. |
| Actividad | Revisar código con checklist de clean code. |
| Evidencia | Lista de mejoras priorizadas. |
| Cierre | Elegir una mejora concreta para aplicar. |

### Sesión 260 — Refactorización controlada

| Campo | Desarrollo |
|---|---|
| Hito | H5 |
| Foco | Mejorar estructura sin cambiar comportamiento. |
| Explicar | Antes/después, motivo y prueba posterior. |
| Actividad | Aplicar una refactorización pequeña. |
| Evidencia | `docs/informe-refactorizacion-h5.md` inicial. |
| Cierre | Ejecutar prueba que demuestre que no se rompió. |

### Sesión 261 — Herramientas internas

| Campo | Desarrollo |
|---|---|
| Hito | H5 |
| Foco | Separar comandos como herramientas. |
| Explicar | Una herramienta tiene nombre, descripción y ejecución. |
| Actividad | Diseñar lista de herramientas: ayuda, recordar, memoria, estado. |
| Evidencia | Tabla de herramientas y responsabilidad. |
| Cierre | Pregunta: ¿qué herramienta añadirías sin tocar memoria? |

### Sesión 262 — Interfaz `Tool`

| Campo | Desarrollo |
|---|---|
| Hito | H5 |
| Foco | Introducir contrato común si el grupo está preparado. |
| Explicar | Interfaz como conjunto de métodos que una clase promete implementar. |
| Actividad | Crear `Tool` con métodos simples como `name()` y `execute()`. |
| Evidencia | Primera herramienta implementa `Tool`. |
| Cierre | Microdefensa: ¿qué obliga a hacer la interfaz? |

### Sesión 263 — Implementar `HelpTool`

| Campo | Desarrollo |
|---|---|
| Hito | H5 |
| Foco | Separar ayuda del flujo principal. |
| Explicar | Delegación: `Agent` no tiene que saber todos los detalles. |
| Actividad | Crear `HelpTool`. |
| Evidencia | Comando ayuda funciona mediante herramienta. |
| Cierre | Pregunta: ¿qué código salió de `Agent`? |

### Sesión 264 — Implementar `RememberTool`

| Campo | Desarrollo |
|---|---|
| Hito | H5 |
| Foco | Herramienta que colabora con `Memory`. |
| Explicar | Composición: una clase usa otra para cumplir su tarea. |
| Actividad | Crear `RememberTool` usando `Memory`. |
| Evidencia | Comando recordar funciona como herramienta. |
| Cierre | Revisar dependencias: qué necesita `RememberTool`. |

### Sesión 265 — Implementar `MemoryTool` y `StatusTool`

| Campo | Desarrollo |
|---|---|
| Hito | H5 |
| Foco | Completar herramientas principales. |
| Explicar | Repetir estructura permite detectar abstracción útil. |
| Actividad | Extraer memoria y estado a herramientas separadas. |
| Evidencia | Agente funciona con varias herramientas. |
| Cierre | Pregunta: ¿qué se repite entre herramientas? |

### Sesión 266 — Registro de herramientas en `Agent`

| Campo | Desarrollo |
|---|---|
| Hito | H5 |
| Foco | Orquestar herramientas sin condicional gigante. |
| Explicar | Mapa o lista de herramientas, búsqueda por nombre y ejecución. |
| Actividad | Registrar herramientas y ejecutar según comando. |
| Evidencia | Añadir herramienta requiere bajo impacto. |
| Cierre | Probar añadir una herramienta mínima nueva. |

### Sesión 267 — Patrón Command simplificado

| Campo | Desarrollo |
|---|---|
| Hito | H5 |
| Foco | Nombrar el patrón solo si el diseño lo justifica. |
| Explicar | Command: encapsular una acción como objeto. |
| Actividad | Comparar herramientas del proyecto con idea del patrón Command. |
| Evidencia | `docs/registro-patron-h5.md`: usar o descartar patrón. |
| Cierre | Pregunta: ¿qué problema resuelve aquí? |

### Sesión 268 — Git profesional I: commits y ramas

| Campo | Desarrollo |
|---|---|
| Hito | H5 |
| Foco | Mejorar trazabilidad. |
| Explicar | Commit pequeño, mensaje claro, rama de trabajo y autoría. |
| Actividad | Crear evidencia de commits o registro equivalente si no hay GitHub. |
| Evidencia | `docs/evidencia-git-h5.md`. |
| Cierre | Revisar un commit: qué cambia y por qué. |

### Sesión 269 — Git profesional II: revisión de código

| Campo | Desarrollo |
|---|---|
| Hito | H5 |
| Foco | Revisar código de forma constructiva. |
| Explicar | Revisión no es criticar personas; es mejorar producto. |
| Actividad | Revisión cruzada por equipos con checklist. |
| Evidencia | `docs/revision-codigo-h5.md`. |
| Cierre | Cada equipo acepta o rechaza una sugerencia justificando. |

### Sesión 270 — Comparación Java-Python H5

| Campo | Desarrollo |
|---|---|
| Hito | H5 |
| Foco | Comparar interfaz, herencia, composición y duck typing. |
| Explicar | Java formaliza contratos; Python puede usar convenciones. |
| Actividad | Comparar una herramienta Java con equivalente Python. |
| Evidencia | `docs/comparacion-java-python-h5.md`. |
| Cierre | Pregunta: ¿qué pierde y qué gana cada lenguaje? |

### Sesión 271 — Pruebas tras refactorización

| Campo | Desarrollo |
|---|---|
| Hito | H5 |
| Foco | Verificar que la extensibilidad no rompe H4. |
| Explicar | Toda refactorización necesita comprobación posterior. |
| Actividad | Ejecutar pruebas de comandos y memoria. |
| Evidencia | Checklist de pruebas H5. |
| Cierre | Registrar una regresión si aparece. |

### Sesión 272 — README y documentación técnica H5

| Campo | Desarrollo |
|---|---|
| Hito | H5 |
| Foco | Documentar diseño extensible. |
| Explicar | README debe explicar cómo añadir una herramienta. |
| Actividad | Actualizar README con estructura, herramientas y ejecución. |
| Evidencia | README H5. |
| Cierre | Otro equipo intenta entender cómo añadir una herramienta. |

### Sesión 273 — Portfolio y registro IA H5

| Campo | Desarrollo |
|---|---|
| Hito | H5 |
| Foco | Documentar aprendizaje y uso de IA. |
| Explicar | La IA puede sugerir refactorizaciones, pero deben verificarse y defenderse. |
| Actividad | Completar portfolio y registro IA. |
| Evidencia | Portfolio H5 y registro IA. |
| Cierre | Pregunta: ¿qué sugerencia de IA rechazaste o modificaste? |

### Sesión 274 — Demo y defensa H5

| Campo | Desarrollo |
|---|---|
| Hito | H5 |
| Foco | Defender extensibilidad, refactorización, Git y patrón. |
| Explicar | No se evalúa usar patrón, sino decidir con criterio. |
| Actividad | Demo, defensa individual y revisión de evidencias. |
| Evidencia | Defensa H5 completa. |
| Cierre | Preparar lista de pendientes para C2. |

---

## 9. Sesiones C2 — Cierre segunda evaluación

### Sesión 275 — Revisión técnica H4-H5

| Campo | Desarrollo |
|---|---|
| Hito | C2 |
| Foco | Consolidar POO y extensibilidad. |
| Explicar | Antes de persistir datos, el diseño debe ser entendible. |
| Actividad | Revisión de clases, herramientas, README, Git y pruebas. |
| Evidencia | Checklist C2. |
| Cierre | Identificar RA pendientes por alumno/a. |

### Sesión 276 — Defensa individual C2

| Campo | Desarrollo |
|---|---|
| Hito | C2 |
| Foco | Verificar comprensión individual. |
| Explicar | La evidencia de equipo no sustituye la defensa individual. |
| Actividad | Preguntas sobre clases, interfaces, refactorización, commits y pruebas. |
| Evidencia | Registro de defensa individual. |
| Cierre | Marcar recuperación o mejora. |

### Sesión 277 — Recuperación específica C2

| Campo | Desarrollo |
|---|---|
| Hito | C2 |
| Foco | Recuperar evidencias incompletas. |
| Explicar | Recuperar no es repetir todo; es demostrar el RA pendiente. |
| Actividad | Tarea individual dirigida según carencia. |
| Evidencia | Evidencia de recuperación. |
| Cierre | Validación rápida con pregunta técnica. |

### Sesión 278 — Preparación para persistencia

| Campo | Desarrollo |
|---|---|
| Hito | C2 |
| Foco | Anticipar H6. |
| Explicar | La memoria temporal desaparece al cerrar; la persistencia resuelve eso. |
| Actividad | Diseñar qué debe guardarse en disco. |
| Evidencia | Boceto de persistencia H6. |
| Cierre | Pregunta: ¿qué riesgos aparecen al guardar datos? |

---

## 10. Sesiones H6 — Persistencia y trazabilidad

### Sesión 279 — Presentar H6: memoria persistente

| Campo | Desarrollo |
|---|---|
| Hito | H6 |
| Foco | Comprender persistencia. |
| Explicar | Diferencia entre memoria temporal y fichero. |
| Actividad | Ejecutar MiniJarvis, guardar recuerdo, cerrar y comprobar pérdida actual. |
| Evidencia | Necesidad documentada de persistencia. |
| Cierre | Pregunta: ¿qué debe sobrevivir entre ejecuciones? |

### Sesión 280 — Formato de fichero

| Campo | Desarrollo |
|---|---|
| Hito | H6 |
| Foco | Decidir cómo guardar datos. |
| Explicar | Formato simple, legible y suficiente: una línea por recuerdo. |
| Actividad | Diseñar `data/recuerdos.txt`. |
| Evidencia | Documento de formato. |
| Cierre | Revisar si el formato puede leerse después. |

### Sesión 281 — Escritura de ficheros

| Campo | Desarrollo |
|---|---|
| Hito | H6 |
| Foco | Guardar recuerdos en disco. |
| Explicar | Escritura de fichero y creación de carpeta `data/`. |
| Actividad | Implementar guardado básico. |
| Evidencia | `data/recuerdos.txt` generado con datos ficticios. |
| Cierre | Verificar el contenido del fichero. |

### Sesión 282 — Lectura de ficheros

| Campo | Desarrollo |
|---|---|
| Hito | H6 |
| Foco | Cargar recuerdos al iniciar. |
| Explicar | Leer líneas y reconstruir memoria. |
| Actividad | Implementar carga inicial o comando de carga. |
| Evidencia | Recuerdos recuperados tras reiniciar. |
| Cierre | Prueba: guardar, cerrar, abrir y consultar. |

### Sesión 283 — Clase `PersistentMemory`

| Campo | Desarrollo |
|---|---|
| Hito | H6 |
| Foco | Separar persistencia de memoria de negocio. |
| Explicar | La persistencia es una responsabilidad distinta. |
| Actividad | Crear o ajustar `PersistentMemory`. |
| Evidencia | Persistencia encapsulada en clase propia. |
| Cierre | Pregunta: ¿por qué no ponemos todo en `Agent`? |

### Sesión 284 — Errores de fichero

| Campo | Desarrollo |
|---|---|
| Hito | H6 |
| Foco | Gestionar problemas previsibles. |
| Explicar | Carpeta inexistente, fichero vacío, permisos y errores de lectura. |
| Actividad | Probar fallo controlado y documentar respuesta. |
| Evidencia | Incidencia H6 o prueba de error. |
| Cierre | Pregunta: ¿qué verá el usuario si falla la carga? |

### Sesión 285 — Logs e historial

| Campo | Desarrollo |
|---|---|
| Hito | H6 |
| Foco | Registrar eventos simples. |
| Explicar | Log no es base de datos; es trazabilidad básica. |
| Actividad | Crear `logs/historial.log` con eventos simples. |
| Evidencia | Log generado sin datos sensibles. |
| Cierre | Revisar que el log no contiene información personal real. |

### Sesión 286 — Seguridad de datos

| Campo | Desarrollo |
|---|---|
| Hito | H6 |
| Foco | Evitar secretos y datos personales. |
| Explicar | No subir `.env` real, tokens, claves ni datos personales. |
| Actividad | Revisar repositorio y ficheros de ejemplo. |
| Evidencia | `docs/seguridad-h6.md`. |
| Cierre | Checklist de seguridad pasado. |

### Sesión 287 — README reproducible

| Campo | Desarrollo |
|---|---|
| Hito | H6 |
| Foco | Que otra persona pueda ejecutar desde cero. |
| Explicar | Reproducible significa seguir pasos y obtener resultado. |
| Actividad | Redactar README H6 con estructura, ejecución y pruebas. |
| Evidencia | README H6 probado por otro equipo. |
| Cierre | Si otro equipo no puede ejecutar, README incompleto. |

### Sesión 288 — Pruebas de persistencia

| Campo | Desarrollo |
|---|---|
| Hito | H6 |
| Foco | Verificar guardar y cargar. |
| Explicar | La prueba clave de persistencia exige segunda ejecución. |
| Actividad | Completar pruebas: guardar, cerrar, abrir, consultar, fichero vacío y error. |
| Evidencia | `docs/pruebas-persistencia-h6.md`. |
| Cierre | Ejecutar prueba completa delante del docente o de otro equipo. |

### Sesión 289 — Comparación Java-Python H6

| Campo | Desarrollo |
|---|---|
| Hito | H6 |
| Foco | Comparar ficheros, JSON/logs o lectura simple. |
| Explicar | Diferencias entre APIs de fichero en Java y Python. |
| Actividad | Analizar versión Python equivalente. |
| Evidencia | `docs/comparacion-java-python-h6.md`. |
| Cierre | Pregunta: ¿qué parte es más sencilla en Python y por qué? |

### Sesión 290 — Portfolio y registro IA H6

| Campo | Desarrollo |
|---|---|
| Hito | H6 |
| Foco | Documentar decisiones, seguridad y uso de IA. |
| Explicar | La IA puede ayudar con ficheros, pero hay que verificar rutas, errores y seguridad. |
| Actividad | Completar portfolio y registro IA. |
| Evidencia | Portfolio H6 y registro IA. |
| Cierre | Pregunta: ¿qué riesgo de seguridad has evitado? |

### Sesión 291 — Demo y defensa H6

| Campo | Desarrollo |
|---|---|
| Hito | H6 |
| Foco | Defender persistencia, logs y reproducibilidad. |
| Explicar | El proyecto debe quedar cerrado en versión base antes de FFEOE. |
| Actividad | Demo de guardar, cerrar, abrir y consultar. Defensa individual. |
| Evidencia | Defensa H6. |
| Cierre | Decidir si el grupo puede abordar H7 o debe ir a cierre. |

---

## 11. Sesiones H7 — IA responsable real o simulada

### Sesión 292 — Decidir alcance H7

| Campo | Desarrollo |
|---|---|
| Hito | H7 |
| Foco | Elegir integración real o simulación robusta. |
| Explicar | La simulación robusta es válida si evita fragilidad o riesgos de claves. |
| Actividad | Evaluar preparación del equipo y decidir alcance. |
| Evidencia | Decisión H7 documentada. |
| Cierre | Pregunta: ¿qué opción es más segura y defendible para tu equipo? |

### Sesión 293 — Caso de uso IA y seguridad de prompts

| Campo | Desarrollo |
|---|---|
| Hito | H7 |
| Foco | Definir uso limitado y seguro de IA. |
| Explicar | No enviar datos personales, secretos ni información sensible. |
| Actividad | Diseñar caso: sugerencia de estudio o explicación breve. |
| Evidencia | `docs/riesgos-ia-h7.md` inicial. |
| Cierre | Revisar qué datos recibe la IA o simulación. |

### Sesión 294 — Implementar simulación o integración

| Campo | Desarrollo |
|---|---|
| Hito | H7 |
| Foco | Añadir modo IA controlado. |
| Explicar | `AiAssistant`, `SimulatedAiAssistant`, `AiTool` y validación. |
| Actividad | Implementar clase simulada o integración segura. |
| Evidencia | Modo IA funcional o simulación robusta. |
| Cierre | Probar respuesta válida y respuesta rechazada. |

### Sesión 295 — Registro de prompts y validación humana

| Campo | Desarrollo |
|---|---|
| Hito | H7 |
| Foco | Trazar y validar respuestas. |
| Explicar | La IA no se acepta sin revisión humana. |
| Actividad | Completar registro de prompts y validación. |
| Evidencia | `docs/registro-prompts-h7.md` y validación humana. |
| Cierre | Pregunta: ¿qué respuesta podría ser incorrecta o peligrosa? |

### Sesión 296 — Demo y defensa H7

| Campo | Desarrollo |
|---|---|
| Hito | H7 |
| Foco | Defender límites, seguridad y funcionamiento. |
| Explicar | La IA debe estar limitada, validada y documentada. |
| Actividad | Demo H7 y defensa individual. |
| Evidencia | Defensa H7 y configuración segura. |
| Cierre | Congelar versión base para HF. |

---

## 12. Sesiones HF — Presentación final, recuperación y mejora

### Sesión 297 — Reentrada tras FFEOE y diagnóstico final

| Campo | Desarrollo |
|---|---|
| Hito | HF |
| Foco | Retomar proyecto y detectar estado real. |
| Explicar | No se abren grandes funcionalidades nuevas; se cierra, recupera y mejora. |
| Actividad | Revisar repositorio, evidencias y RA pendientes. |
| Evidencia | Diagnóstico final por alumno/a y equipo. |
| Cierre | Plan de cierre individual. |

### Sesión 298 — Preparar demo final

| Campo | Desarrollo |
|---|---|
| Hito | HF |
| Foco | Diseñar una demo clara y realista. |
| Explicar | Una demo debe mostrar evolución, no solo resultado final. |
| Actividad | Preparar guion de demo: H1, H2, H3, H4, H5, H6 y H7 si procede. |
| Evidencia | Guion de demo final. |
| Cierre | Ensayo rápido de 3 minutos por equipo. |

### Sesión 299 — Portfolio final

| Campo | Desarrollo |
|---|---|
| Hito | HF |
| Foco | Organizar evidencias de aprendizaje. |
| Explicar | Portfolio no es una carpeta de archivos; es relato técnico con evidencias. |
| Actividad | Completar portfolio final individual. |
| Evidencia | `portfolio-final.md`. |
| Cierre | Revisar si cada afirmación tiene evidencia. |

### Sesión 300 — README final y reproducibilidad

| Campo | Desarrollo |
|---|---|
| Hito | HF |
| Foco | Dejar el proyecto ejecutable por otra persona. |
| Explicar | README final debe incluir requisitos, ejecución, estructura, comandos, límites y seguridad. |
| Actividad | Actualizar README final y probar desde cero. |
| Evidencia | README final validado. |
| Cierre | Otro equipo intenta seguir instrucciones. |

### Sesión 301 — Registro IA final y seguridad

| Campo | Desarrollo |
|---|---|
| Hito | HF |
| Foco | Cerrar trazabilidad de IA. |
| Explicar | Todo uso de IA evaluable debe quedar declarado. |
| Actividad | Revisar registros IA de todos los hitos y completar faltantes. |
| Evidencia | Registro IA final. |
| Cierre | Pregunta: ¿qué parte del proyecto no podrías defender si no registras IA? |

### Sesión 302 — Recuperación específica I

| Campo | Desarrollo |
|---|---|
| Hito | HF |
| Foco | Recuperar RA técnicos pendientes. |
| Explicar | La recuperación debe atacar exactamente la carencia detectada. |
| Actividad | Tareas individuales: variable, bucle, colección, clase, fichero o prueba según caso. |
| Evidencia | Evidencia de recuperación específica. |
| Cierre | Pregunta técnica individual. |

### Sesión 303 — Recuperación específica II

| Campo | Desarrollo |
|---|---|
| Hito | HF |
| Foco | Recuperar evidencias de Entornos. |
| Explicar | Entornos se demuestra con IDE, Git, pruebas, depuración, UML, documentación y reproducibilidad. |
| Actividad | Completar README, prueba, depuración, diagrama, Git o seguridad según pendiente. |
| Evidencia | Evidencia de recuperación Entornos. |
| Cierre | Validación con checklist. |

### Sesión 304 — Ensayo de defensa individual

| Campo | Desarrollo |
|---|---|
| Hito | HF |
| Foco | Preparar defensa final sin memorizar. |
| Explicar | Defender es razonar sobre código, decisiones, errores y aprendizaje. |
| Actividad | Simulación de preguntas por parejas o tríos. |
| Evidencia | Plantilla de defensa final. |
| Cierre | Cada alumno anota tres preguntas que debe preparar mejor. |

### Sesión 305 — Presentaciones finales

| Campo | Desarrollo |
|---|---|
| Hito | HF |
| Foco | Presentar producto y proceso. |
| Explicar | La presentación debe equilibrar demo, decisiones técnicas, pruebas, IA y aprendizaje. |
| Actividad | Demo final por equipos. |
| Evidencia | Rúbrica de presentación final y demo. |
| Cierre | Feedback breve del docente y compañeros. |

### Sesión 306 — Defensa final, cierre y retrospectiva del curso

| Campo | Desarrollo |
|---|---|
| Hito | HF |
| Foco | Cerrar aprendizaje y evaluación. |
| Explicar | Sin comprensión defendible, no hay evidencia completa. |
| Actividad | Defensa individual, retrospectiva final y plan personal de mejora. |
| Evidencia | Defensa final, autoevaluación y retrospectiva. |
| Cierre | Pregunta final: ¿qué sabes construir, probar, documentar y defender ahora que no sabías al empezar? |

---

## 13. Regla final de aplicación

Este plan no debe utilizarse como una lista rígida de tareas para correr. Debe usarse como una secuencia de aprendizaje.

Si el grupo va más lento:

```text
Reducir ampliaciones, mantener mínimos y proteger defensa.
```

Si el grupo va más rápido:

```text
Profundizar en pruebas, Git, revisión, automatización, Docker guiado o integración IA real, sin saltarse evidencias.
```

Prioridad absoluta:

```text
Producto funcional + proceso trazable + comprensión defendible.
```
