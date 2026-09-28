# Página H1 del Site de equipo — MiniJarvis

> Esta es la página H1 del Site de equipo. Comunica el incremento del equipo: qué hace MiniJarvis, qué decisiones tomamos, qué pruebas hicimos y qué aprendimos.

---

## Incremento logrado en H1

MiniJarvis es un asistente de consola que:
1. Pide un nombre al usuario y lo saluda con un mensaje personalizado.
2. Pide un número entero al usuario.
3. Calcula el doble del número introducido.
4. Muestra el resultado si el número es positivo, o un mensaje indicando que no lo es.

**Lo que hace:** Entrada → procesamiento → salida. Lee datos, los almacena en variables, realiza una operación aritmética y aplica una condición para decidir la salida.

**Lo que NO hace (y por qué):**
- No tiene menú: queda fuera del alcance de H1. Se abordará en H2 con bucles `while`.
- No tiene bucles: el programa se ejecuta una vez y termina. Los bucles se verán en H2.
- No tiene conexión con IA real: el nombre "Jarvis" es temático. No usa APIs ni modelos de lenguaje.
- No gestiona errores de entrada: si el usuario introduce texto donde se espera un número, el programa se detiene con `NumberFormatException`. Esto se documenta como limitación y se abordará con `try/catch` en H2.

---

## Decisiones del equipo

### 1. Mensaje de saludo: "Hola" vs "Bienvenido"

**Decisión:** "Hola, " + nombre

**Alternativas descartadas:** "Bienvenido, " + nombre; "Hey, " + nombre

**Motivo:** "Hola" es más cercano, no asume género, y se alinea con la idea de un asistente amigable. La formalidad no es prioritaria para un asistente de consola.

**Responsable:** Ana propuso, Carlos aceptó.

---

### 2. Nombres de variables: claros y descriptivos

**Decisión:** `String nombre`, `int numero`, `int doble`, `final String MENSAJE_BIENVENIDA`

**Alternativas descartadas:** `x`, `dato1`, `valor`, `a`, `b`

**Motivo:** Nombres claros y descriptivos facilitan la comprensión y el mantenimiento del código. En H1 ya estamos escribiendo código que debe ser legible.

**Responsable:** Ana propuso, Carlos aceptó.

---

### 3. Lectura de entrada: `Scanner` con `nextLine()` + `Integer.parseInt()`

**Decisión:** Usar `Scanner` para leer cadenas y `Integer.parseInt()` para convertirlas a entero.

**Alternativas descartadas:** `BufferedReader`, `Console.readLine()`

**Motivo:** `Scanner` es más sencillo para principiantes y está en el temario del Tema 1.

**Responsable:** Carlos implementó.

---

### 4. Condición: `if (numero > 0)`

**Decisión:** `if (numero > 0)` → muestra doble; `else` → "no es positivo"

**Alternativas descartadas:** `if (numero >= 0)`, `if (numero != 0)`

**Motivo:** `>` es la comparación más directa para "positivo". `>= 0` incluiría el cero como positivo, lo cual es debatible.

**Responsable:** Ana decidió.

---

## Pruebas realizadas

| Caso | Entrada | Salida esperada | Salida obtenida | ¿Pasa? |
|---|---|---|---|---|
| Nombre válido, número positivo | Ana, 5 | "Hola, Ana... El doble de 5 es 10." | "Hola, Ana... El doble de 5 es 10." | ✓ |
| Nombre válido, número negativo | Carlos, -3 | "Hola, Carlos... El número no es positivo." | "Hola, Carlos... El número no es positivo." | ✓ |
| Nombre válido, número cero | María, 0 | "Hola, María... El número no es positivo." | "Hola, María... El número no es positivo." | ✓ |
| Entrada no numérica | Ana, abc | Exception: NumberFormatException | Exception: NumberFormatException | ✓ (documentado) |

---

## Revisión: ¿el incremento cumple el alcance definido en S206?

**Alcance de S206:** "Un asistente de consola que lee nombre y número, calcula el doble, y usa if/else para decidir la salida."

**Cumplimiento:**
- [x] Lee nombre: Sí, con `Scanner.nextLine()`
- [x] Lee número: Sí, con `Integer.parseInt()`
- [x] Calcula el doble: Sí, `numero * 2`
- [x] Usa if/else: Sí, `if (numero > 0)`
- [x] Sin menú: Sí
- [x] Sin bucles: Sí
- [x] Sin IA real: Sí

**Conclusión:** El incremento cumple el alcance definido en S206. Todo lo que prometimos en H1 está implementado y probado.

---

## Retrospectiva del equipo

### ¿Qué funcionó bien?
- La división de tareas: Ana se centró en la lógica y estructura; Carlos en la entrada y pruebas.
- Los commits frecuentes y con mensajes descriptivos.
- El uso del Scrum Sheet para registrar decisiones y bloqueos.
- Las pruebas de ambos ramas (if y else) antes de considerar una funcionalidad como "done".

### ¿Qué no funcionó bien?
- Tardamos más de lo esperado en entender `final` vs `static`.
- No probamos suficientes casos de prueba en S213: solo probamos el caso positivo primero. Tuvimos que volver atrás para probar el caso negativo.
- La gestión de errores de entrada quedó pendiente: sabemos que es necesaria pero no la implementamos en H1.

### ¿Qué mantendremos en H2?
- Commits frecuentes con mensajes descriptivos.
- Registro de decisiones en Scrum.
- Pruebas de ambos ramas (if y else) antes de considerar una funcionalidad como "done".
- Documentar las limitaciones del código en el README desde el inicio.

### ¿Qué cambiaremos en H2?
- Empezar con más casos de prueba antes de implementar.
- Implementar `try/catch` para gestionar errores de entrada desde el inicio, no como añadido posterior.
- Revisar los enlaces de Moodle antes de entregar para evitar errores de permisos.
