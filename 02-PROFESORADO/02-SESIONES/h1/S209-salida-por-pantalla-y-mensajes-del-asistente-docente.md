# H1.4 — Salida por pantalla y mensajes del asistente

| Dato | Valor |
|---|---|
| Hito | H1 — Primer asistente ejecutable |
| Duración prevista | 45 minutos |
| Fase HEXA del hito | Idear — proponer soluciones |
| Modalidad de trabajo | **PAREJAS → EQUIPO** |

> Basada en `00-GUION-DOCENTE-H1-COMPLETO.md`.

## Finalidad de la sesión

El alumnado diseña mensajes comprensibles antes de programarlos, compara alternativas y utiliza literales y concatenación para implementar la opción elegida. La consola se presenta como la primera interfaz de MiniJarvis: aunque sea textual, debe permitir entender qué ocurre, qué se pide y qué resultado se muestra.

Idea central para verbalizar:

> El mensaje está pensado para quien utiliza el programa, no para demostrar que sabemos Java.

MiniJarvis en H1 es un programa Java progresivo. Sus mensajes deben describir honestamente lo que ya hace, sin presentarlo como una inteligencia artificial completa.

## Antes de entrar en clase

- [ ] Preparar los cinco contrastes de mensajes sin revelar de entrada cuál funciona mejor.
- [ ] Probar los ejemplos de concatenación y tener clara su salida exacta.
- [ ] Preparar pizarra o papel para diseñar alternativas antes de abrir el IDE.
- [ ] Tener disponible el proyecto de H1 para la implementación de equipo.
- [ ] Reservar una lectura cruzada de consola sin mostrar el código.

## Apertura docente

Di en voz alta:

> Hoy estamos en Idear. Primero decidiremos qué debe entender la persona usuaria y después escribiremos el código. Un programa puede compilar y mostrar una salida técnicamente correcta, pero seguir comunicándose mal.

Pregunta:

> Si la consola muestra solo `5`, ¿el programa ha producido una salida correcta? ¿Puede una persona saber qué significa ese número?

Distingue desde el principio:

- **salida técnicamente correcta:** el programa muestra lo que el código ordena;
- **salida comprensible:** la persona usuaria entiende qué ocurre, qué se le pide o qué significa el resultado.

## Temporalización orientativa

| Tiempo | Acción |
|---|---|
| 0–5 min | Activar la diferencia entre salida correcta y salida comprensible. |
| 5–13 min | Analizar los cinco contrastes desde la perspectiva de la persona usuaria. |
| 13–21 min | Diseñar por parejas, sin IDE, dos alternativas de saludo, propósito y mensaje final. |
| 21–27 min | Predecir literales, concatenaciones, espacios, signos y el comportamiento contextual de `+`. |
| 27–36 min | Comparar en equipo, elegir, justificar, implementar y ejecutar la propuesta. |
| 36–41 min | Pedir a otra persona que lea solo la consola y explique qué entiende. |
| 41–45 min | Revisar mensajes, comprobar la salida y cerrar con la decisión final. |

## La consola como primera interfaz

`System.out.println` no se limita a «sacar texto». En H1 permite comunicarse con la persona que ejecuta MiniJarvis. Un mensaje útil aporta el contexto suficiente y evita vocabulario técnico interno que no ayuda a usar el programa.

Para cada contraste, pregunta:

- ¿qué entiende la persona?
- ¿qué información falta?
- ¿qué sobra?
- ¿qué alternativa sería más clara?

### Contraste 1: confirmación genérica

```text
correcto
```

Frente a:

```text
MiniJarvis se ha iniciado correctamente.
```

`correcto` puede ser una salida válida desde el punto de vista del código, pero no identifica qué ha ocurrido. La segunda opción comunica la acción confirmada.

Pregunta:

> Si la persona acaba de ejecutar el programa, ¿qué confirma exactamente cada mensaje?

### Contraste 2: petición vaga

```text
Dato:
```

Frente a:

```text
Escribe tu nombre:
```

La primera petición no permite saber qué dato se espera. La segunda aporta una acción y un contexto, aunque en clase deba usarse siempre un nombre ficticio.

Pregunta:

> ¿Qué tendría que adivinar la persona ante `Dato:`? ¿Qué información añade la alternativa?

### Contraste 3: resultado aislado

```text
5
```

Frente a:

```text
Horas de estudio registradas: 5
```

El número aislado carece de significado visible. La alternativa relaciona el dato con aquello que representa.

Pregunta:

> ¿El número es una cantidad, un código o una opción? ¿Qué palabras eliminan esa ambigüedad?

### Contraste 4: detalle técnico interno

```text
String nombreUsuario initialized successfully.
```

Frente a:

```text
Hola, Laura.
```

El primer mensaje describe una operación interna útil para quien programa, pero no para quien usa MiniJarvis. La segunda salida emplea el dato para comunicarse.

Pregunta:

> ¿Necesita la persona saber que existe un `String`, o necesita comprender el efecto visible del programa?

### Contraste 5: promesa que excede H1

```text
Analizando tus datos con inteligencia artificial...
```

Frente a:

```text
Hola, soy MiniJarvis. Esta es mi primera versión por consola.
```

La primera salida atribuye al programa una capacidad que H1 no demuestra. La segunda presenta su identidad y alcance de forma honesta.

Pregunta:

> ¿Qué expectativa crea cada versión? ¿Cuál puede demostrarse con el programa actual?

Corta también promesas como `Puedo recordar todo` si H1 todavía no tiene memoria.

## Literales y concatenación

### Literal textual

```java
System.out.println("Hola");
```

Pregunta:

> ¿Qué parte de esta instrucción ha escrito literalmente quien programa y qué aparecerá en la consola?

El texto entre comillas dobles es un literal textual. Se muestra tal como está escrito, incluidos espacios y signos interiores.

### Concatenación con un nombre

```java
String nombreUsuario = "Laura";
System.out.println("Hola, " + nombreUsuario);
```

Salida esperada:

```text
Hola, Laura
```

Antes de ejecutar, pide señalar:

- el literal fijo;
- el dato variable;
- el espacio después de la coma;
- la salida completa.

### Concatenación con el nombre del asistente

```java
String nombreUsuario = "Laura";
String nombreAsistente = "MiniJarvis";
System.out.println("Hola, " + nombreUsuario + ". Soy " + nombreAsistente + ".");
```

Pregunta:

> ¿Dónde se introducen los espacios y los puntos? ¿Qué ocurriría si desapareciera el espacio después de la coma o antes de `Soy`?

No basta con que todos los datos aparezcan: la frase resultante debe poder leerse con naturalidad.

### Concatenación con un número

```java
int horasEstudio = 4;
System.out.println("Has estudiado " + horasEstudio + " horas.");
```

Pregunta:

> ¿Qué texto permanece fijo, qué dato cambia y qué contexto permite interpretar el número?

## El significado contextual de `+`

Presenta esta predicción antes de ejecutar:

```java
System.out.println(2 + 3);
System.out.println("Resultado: " + 2 + 3);
```

Pide escribir o verbalizar las dos salidas esperadas. Después ejecuta y contrasta:

```text
5
Resultado: 23
```

En la primera línea, los operandos son números y `+` suma. En la segunda, la evaluación ya está construyendo texto: concatena `2` y después `3` con el literal inicial.

No desarrolles aquí una teoría extensa de precedencia. La cuestión de H1.4 es qué mensaje aparecerá y por qué. La profundización en operaciones corresponde a H1.6.

Pregunta:

> ¿Qué operandos encuentra `+` en cada paso y cuándo el resultado empieza a ser texto?

## Actividad central

La secuencia de trabajo es:

```text
idear → comparar → elegir → implementar → ejecutar → revisar
```

### Diseño sin IDE — PAREJAS

Di explícitamente:

> Todavía no abráis el IDE. Primero plantead dos versiones de saludo, propósito y mensaje final. Comparadlas, elegid una y justificadla. Solo después programaréis.

Cada pareja debe:

1. detectar al menos un mensaje vago;
2. proponer dos alternativas reales;
3. anticipar qué verá exactamente la persona usuaria;
4. revisar contexto, honestidad, espacios y signos;
5. elegir una alternativa y explicar por qué es más comprensible.

Si abren directamente el IDE, vuelve a la pregunta: «¿Qué queréis que entienda la persona antes de decidir cómo escribirlo?».

### Decisión e implementación — EQUIPO

El equipo:

1. compara las propuestas de las parejas;
2. acuerda los mensajes del incremento;
3. explica la alternativa elegida y el motivo;
4. implementa la opción seleccionada;
5. ejecuta el programa;
6. lee literalmente la salida;
7. mejora la formulación si aparecen uniones, espacios, signos o promesas problemáticas.

La implementación debe incluir al menos un literal textual y una concatenación con un dato. No convierte la sesión en una práctica general de variables u operaciones.

## Validación con otra persona

Pide a una persona de otra pareja o equipo que lea únicamente la consola, sin mirar el código ni recibir una explicación previa.

Debe poder decir:

- qué pide el programa;
- qué significa el resultado;
- qué hace MiniJarvis en esta versión;
- qué mensaje necesita más contexto.

El equipo escucha, contrasta la interpretación con su intención y revisa el texto cuando sea necesario. Esta validación es una conversación breve, no un formulario ni una ficha.

## Evidencia que permanece

- **GitHub:** código con los mensajes finalmente implementados y ejecutables.
- **Scrum:** alternativa elegida y motivo solo si constituye una decisión de diseño relevante para el trabajo posterior.
- **Diario individual:** únicamente si cambiar o defender una decisión produjo aprendizaje significativo.
- **README / Moodle / Drive / Site:** sin actualización o entrega específica en H1.4.

No se crea captura, documento paralelo, ficha de validación ni microentrega. La alternativa descartada puede explicarse durante la actividad; solo necesita persistir si ayuda al equipo a comprender una decisión real.

## Observación docente

Mientras trabajan, comprueba específicamente:

- que distinguen salida técnicamente correcta de salida comprensible;
- que razonan desde la perspectiva de la persona usuaria;
- que proponen alternativas antes de programar;
- que justifican la opción seleccionada;
- que predicen las concatenaciones antes de ejecutar;
- que explican cuándo `+` suma y cuándo concatena en los ejemplos trabajados;
- que revisan espacios, signos y separación entre literal y dato;
- que contrastan la salida real con lo diseñado;
- que pueden explicar por qué el mensaje final es mejor que la alternativa descartada;
- que describen MiniJarvis sin atribuirle capacidades inexistentes.

## Andamiaje ante bloqueos

No proporciones inmediatamente el mensaje final. Utiliza preguntas específicas:

- **Mensaje demasiado genérico:** «¿Qué información necesita la persona para entender qué ha ocurrido?»
- **Dato aislado:** «¿Qué significa ese número?»
- **Salida técnica:** «¿Una persona ajena al código entendería este mensaje?»
- **Concatenación incorrecta:** separa los operandos y pide predecir cada unión.
- **Espacios o signos incorrectos:** pide leer literalmente la salida esperada.
- **El equipo abre directamente el IDE:** exige primero dos alternativas escritas.
- **No saben elegir:** compara claridad, contexto y honestidad.
- **Prometen demasiado:** pregunta qué capacidad puede demostrar el programa actual.

## Comprobación y cierre

Pregunta al equipo:

> ¿Qué verá exactamente la persona usuaria, por qué el mensaje final es mejor que la alternativa descartada y qué cambiasteis después de ejecutar o de escuchar a otra persona?

Cierra en voz alta:

> Hoy hemos ideado antes de programar. La salida de consola no se improvisa al final: se diseña, se ejecuta y se revisa para que alguien comprenda qué ocurre.

## Límites de H1.4

Esta sesión no desarrolla operaciones aritméticas, constantes, `Scanner`, decisiones ni clean code como temas centrales. Se concentra en diseñar mensajes, usar literales y concatenar datos para construir la primera interfaz de MiniJarvis.

## Al terminar

Anota solo lo necesario para la continuidad docente: dificultad común de comunicación, pareja o equipo que necesita apoyo, decisión pendiente o ajuste temporal para la siguiente aplicación.
