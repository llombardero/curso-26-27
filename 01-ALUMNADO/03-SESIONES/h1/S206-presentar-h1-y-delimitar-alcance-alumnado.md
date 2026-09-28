# S206 — Presentar H1 y delimitar su alcance

## Objetivo

Comprender qué vas a construir en H1, distinguir lo imprescindible de lo opcional y justificar qué funciones quedan para hitos posteriores.

## 1. El reto H1

H1 consiste en crear una primera versión pequeña y ejecutable de MiniJarvis en Java. No será todavía un asistente completo: será un programa de consola que permita demostrar los fundamentos del Tema 1.

El producto mínimo debe:

- arrancar desde `main`;
- mostrar una presentación clara;
- pedir al menos un dato ficticio mediante `Scanner`;
- guardar datos en variables con tipos adecuados;
- utilizar una constante con `final`;
- realizar una operación sencilla;
- mostrar una respuesta que combine texto y datos;
- compilar y ejecutarse de forma repetible.

El menú, los bucles, la memoria, los ficheros, las clases propias complejas y la conexión con una IA real llegarán en hitos posteriores.

## 2. Tres criterios para valorar un programa

### Correcto

Hace lo que se ha pedido y produce el resultado esperado. Un programa que compila, pero muestra una respuesta equivocada, no es correcto.

### Eficiente

Resuelve el problema sin pasos o repeticiones innecesarias. En H1 no buscamos optimizaciones avanzadas: basta con evitar código duplicado y cálculos que no se usan.

### Mantenible

Se puede leer y modificar con facilidad. Ayudan los nombres claros, la indentación coherente, las constantes para datos estables y los comentarios que explican decisiones no evidentes.

Ejemplo:

```java
final String NOMBRE_ASISTENTE = "MiniJarvis";
String nombreUsuario = "Laura";
System.out.println("Hola, " + nombreUsuario + ". Soy " + NOMBRE_ASISTENTE + ".");
```

Este fragmento usa nombres que explican la intención y evita repetir el nombre del asistente como un literal disperso.

## 3. Clasifica el alcance

Coloca cada propuesta en una de estas categorías:

| Entra en H1 | Puede ser micropráctica | Queda para después |
|---|---|---|
| saludo inicial | conversión de texto a número | menú repetitivo |
| nombre ficticio por teclado | comparación y `if/else` básico | memoria entre ejecuciones |
| cálculo sencillo | prueba de entrada no convertible | lectura de ficheros |
| salida clara | casting como ampliación | conexión con una API o IA real |

Clasifica también estas ideas y justifica cada decisión:

- calcular minutos a partir de horas;
- recordar conversaciones anteriores;
- mostrar si se alcanza un objetivo;
- guardar información en un fichero;
- ofrecer diez comandos distintos.

## 4. Define vuestro incremento

Redactad una decisión de alcance con este formato:

```text
Nuestro H1 hará:
- ...
- ...

No hará todavía:
- ...
- ...

Lo dejamos fuera porque:
- ...
```

Ejemplo:

```text
Nuestro H1 saludará, pedirá un nombre ficticio y unas horas de estudio,
calculará los minutos y mostrará si se alcanza un objetivo.
No tendrá menú ni memoria porque esas funciones necesitan contenidos de H2
y de hitos posteriores.
```

## 5. Evidencia verificable

Conserva en el Scrum del equipo:

- la lista de funciones que entran;
- la lista de funciones que quedan fuera;
- una justificación concreta;
- el enlace a la tarea o decisión correspondiente.

No hace falta crear un documento paralelo. En tu diario individual registra solo tu aportación, un aprendizaje o un bloqueo significativo.

## Errores frecuentes

- Confundir «compila» con «cumple el reto».
- Prometer memoria o inteligencia artificial que H1 no implementa.
- Añadir demasiadas funciones antes de tener un programa mínimo ejecutable.
- Escribir «lo dejamos para después» sin explicar por qué.

## Autoevaluación

Antes de cerrar la sesión, comprueba que puedes:

- explicar H1 en una frase;
- enumerar al menos cuatro elementos que sí entran;
- identificar tres funciones que no pertenecen todavía a H1;
- justificar una exclusión por los contenidos necesarios;
- distinguir un programa correcto, eficiente y mantenible.

## Seguridad y uso de IA

Usa siempre datos ficticios. No publiques nombres reales, contraseñas, claves ni tokens. Si empleas IA de forma sustantiva, registra para qué la usaste, qué propuesta recibiste, qué cambiaste y cómo comprobaste el resultado.
