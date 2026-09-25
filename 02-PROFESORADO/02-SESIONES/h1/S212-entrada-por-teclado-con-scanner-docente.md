# S212 — Guía docente

## Scanner y conversiones

| Dato | Valor |
|---|---|
| Hito | H1 — Primer MiniJarvis |
| Duración | 3 periodos; checkpoint proyectable de 45 minutos y taller asociado |
| Fase HEXA | Ejecutar — crear |
| Agrupamiento | Individual con contraste por parejas o equipo cuando la práctica lo requiera |
| Resultado observable | Leer entrada, convertir tipos y reconocer errores de conversión. |
| Evidencia mínima | Quede diagnóstico. |

## Propósito

Leer entrada, convertir tipos y reconocer errores de conversión.

El concepto se incorpora al Tema 1, pero solo pasa a `Main.java` cuando mejora el producto mínimo. Las demás prácticas se conservan como microejercicios defendibles.

## Material imprescindible

- presentación de S212;
- IntelliJ y JDK cuando haya práctica de código;
- proyecto o microarchivo de prueba;
- diario individual y tablero Scrum del equipo;
- datos ficticios.

## Secuencia de aula

| Tiempo / diap. | Tipo y actuación | Alumnado | Observa | Puerta de avance | Si hay retraso |
|---|---|---|---|---|---|
| 00:00–00:05 / D1 | MICROINVESTIGACIÓN: No expliques Scanner aún. Genera necesidad. | Propone formas de entrada. | Si distinguen entrada/salida. | aparezca “teclado/consola”. | 3 minutos. |
| 00:05–00:11 / D2 | PÍLDORA DOCENTE 1/4: Explica import, lectura y variable destino. No introduzcas todo Scanner. | Señala qué devuelve y dónde se guarda. | Que sepan que nextLine devuelve String. | puedan verbalizar el flujo. | 5 minutos. |
| 00:11–00:17 / D3 | ACTIVIDAD: Circula sin añadir teoría. | Programa y prueba. | Salida que no usa la variable leída. | la entrada afecte a la salida. | una ejecución basta. |
| 00:17–00:20 / D4 | CONFLICTO: Plantea una operación con el texto y pregunta qué falta. | Distingue String/int. | Confusión por el aspecto visual de las cifras. | aparezca necesidad de convertir. | 2 minutos. |
| 00:20–00:25 / D5 | PÍLDORA DOCENTE 2/4: Explica parseo como conversión desde String compatible. | Predice tipos resultantes. | Guardar el resultado del parseo. | puedan explicar para qué sirve parseInt. | prioriza parseInt y parseDouble. |
| 00:25–00:29 / D6 | EXPERIMENTO: Ejecuta con dos entradas válidas. | Predice y prueba. | Orden del flujo. | comprendan la cadena completa. | una entrada válida. |
| 00:29–00:33 / D7 | PÍLDORA DOCENTE 3/4: Presenta la idea pequeño→grande como en Tema 1, sin memorizar toda la jerarquía. | Identifica origen/destino. | Confundir con parseo. | distingan conversión numérica de String→número. | 2 minutos. |
| 00:33–00:37 / D8 | PÍLDORA DOCENTE 4/4: Explica que no redondea en este ejemplo; pierde parte decimal. | Predice antes de ejecutar. | Interpretarlo como redondeo. | puedan explicar la pérdida. | 3 minutos. |
| 00:37–00:40 / D9 | ERROR ÚTIL: Haz predecir compilación y ejecución. No introduzcas try-catch. | Observa el error en ejecución. | Diferencia compile-time/runtime. | puedan nombrar cuándo falla. | hazlo solo como demo. |
| 00:40–00:43 / D10 | ACTIVIDAD: Pide evidencia concreta. | Documenta prueba. | Solo una captura sin contexto. | quede trazabilidad. | una entrada válida + explicación oral de inválida. |
| 00:43–00:45 / D11 | CIERRE: Haz preguntas rápidas. | Responde sobre su código. | Confusiones para S213. | quede diagnóstico. | dos preguntas. |

## Qué debes explicar

- **PÍLDORA DOCENTE 1/4:** Explica import, lectura y variable destino. No introduzcas todo Scanner.
- **PÍLDORA DOCENTE 2/4:** Explica parseo como conversión desde String compatible.
- **PÍLDORA DOCENTE 3/4:** Presenta la idea pequeño→grande como en Tema 1, sin memorizar toda la jerarquía.
- **PÍLDORA DOCENTE 4/4:** Explica que no redondea en este ejemplo; pierde parte decimal.

## Ejemplo o demostración preparada

**D1 · Hasta ahora los datos los decide quien programa —** ¿Cómo hacemos para que los escriba la persona que ejecuta MiniJarvis?

**D2 · Scanner: pedir → leer → guardar —** import java.util.Scanner;<br>
<br>
Scanner scanner = new Scanner(System.in);<br>
String userName = scanner.nextLine();<br>
scanner.close();

**D3 · Pide un nombre y úsalo —** Ejecuta dos veces con nombres ficticios distintos.<br>
<br>
¿Qué cambia? ¿Qué no?

**D4 · Tengo "5". ¿Tengo el número 5? —** "5" es texto si procede de nextLine().<br>
5 es un entero.

**D5 · Parsear texto a un tipo básico —** int hours = Integer.parseInt(text);<br>
double score = Double.parseDouble(text);<br>
boolean ok = Boolean.parseBoolean(text);

**D6 · Leer → convertir → calcular —** Scanner scanner = new Scanner(System.in);<br>
String text = scanner.nextLine();<br>
int hours = Integer.parseInt(text);<br>
int minutes = hours \* 60;<br>
System.out.println(minutes);<br>
scanner.close();

**D7 · Conversión implícita —** int whole = 7;<br>
double wider = whole;<br>
<br>
// no hace falta casting

**D8 · Casting: forzar puede perder información —** double price = 12.75;<br>
int wholePrice = (int) price;<br>
// wholePrice vale 12

**D9 · ¿Compila? ¿Y al ejecutar? —** String text = "hola";<br>
int number = Integer.parseInt(text);

**D10 · Evidencia de conversión —** Guarda:<br>
• una entrada válida<br>
• resultado esperado<br>
• resultado obtenido<br>
• qué ocurre con una entrada no convertible

**D11 · Microdefensa de tipos —** ¿Qué devuelve nextLine()?<br>
¿Por qué necesitamos parseInt?<br>
¿Qué diferencia hay con un casting?

## Consigna que se entrega al alumnado

1. Predice antes de ejecutar cuando haya código.
2. Realiza la micropráctica o modificación prevista.
3. Prueba el caso normal y, cuando exista una decisión o conversión, también el caso alternativo o erróneo.
4. Conserva el código o resultado en el repositorio o espacio indicado.
5. Registra una sola entrada en el diario individual; no crees un informe paralelo.

## Qué observar mientras trabajan

- Si distinguen entrada/salida.
- Que sepan que nextLine devuelve String.
- Salida que no usa la variable leída.
- Confusión por el aspecto visual de las cifras.
- Guardar el resultado del parseo.
- Orden del flujo.
- Confundir con parseo.
- Interpretarlo como redondeo.
- Diferencia compile-time/runtime.
- Solo una captura sin contexto.
- Confusiones para S213.

## Criterios para considerar cerrada la sesión

- Aparezca “teclado/consola”.
- Puedan verbalizar el flujo.
- La entrada afecte a la salida.
- Aparezca necesidad de convertir.
- Puedan explicar para qué sirve parseInt.
- Comprendan la cadena completa.
- Distingan conversión numérica de String→número.
- Puedan explicar la pérdida.
- Puedan nombrar cuándo falla.
- Quede trazabilidad.
- Quede diagnóstico.
- La persona puede señalar la evidencia y explicar qué demuestra.

## Seguridad y uso de IA

- Trabajar con datos ficticios.
- No publicar credenciales, tokens, claves ni información personal.
- Si la IA interviene de forma sustantiva, registrar propuesta, cambios propios y validación; no aceptar código que no pueda defenderse.

## Comprobación final

**¿Qué puedes señalar, explicar, predecir o modificar para demostrar el aprendizaje de esta sesión?**

## Anotación docente al terminar

- alumnado que necesita reentrada;
- evidencia pendiente;
- error común;
- ajuste temporal necesario sin eliminar el núcleo conceptual.
