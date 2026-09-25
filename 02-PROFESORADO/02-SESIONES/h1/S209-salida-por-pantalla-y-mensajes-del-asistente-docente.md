# S209 — Guía docente

## Diseñar mensajes claros por consola

| Dato | Valor |
|---|---|
| Hito | H1 — Primer MiniJarvis |
| Duración | 2 periodos; checkpoint proyectable de 45 minutos y taller asociado |
| Fase HEXA | Idear — proponer soluciones |
| Agrupamiento | Individual con contraste por parejas o equipo cuando la práctica lo requiera |
| Resultado observable | Idear la salida de MiniJarvis antes de programarla y usar concatenación cuando sea necesaria. |
| Evidencia mínima | Quede trazabilidad de la ideación. |

## Propósito

Idear la salida de MiniJarvis antes de programarla y usar concatenación cuando sea necesaria.

El concepto se incorpora al Tema 1, pero solo pasa a `Main.java` cuando mejora el producto mínimo. Las demás prácticas se conservan como microejercicios defendibles.

## Material imprescindible

- presentación de S209;
- IntelliJ y JDK cuando haya práctica de código;
- proyecto o microarchivo de prueba;
- diario individual y tablero Scrum del equipo;
- datos ficticios.

## Secuencia de aula

| Tiempo / diap. | Tipo y actuación | Alumnado | Observa | Puerta de avance | Si hay retraso |
|---|---|---|---|---|---|
| 00:00–00:05 / D1 | IDEAR: Pide elegir y justificar por claridad. | Compara. | Criterios de claridad y orden. | aparezcan criterios propios. | 3 minutos. |
| 00:05–00:10 / D2 | PÍLDORA BREVE: Conecta diseño de mensajes con experiencia de usuario sin introducir teoría extra. | Propone un criterio de claridad. | Mensajes técnicos o ambiguos. | tengan 2–3 criterios. | 2 minutos. |
| 00:10–00:20 / D3 | ACTIVIDAD DE IDEACIÓN: Impide que salten directamente al IDE. Facilita con preguntas. | Genera y compara alternativas. | Si idean de verdad o copian la primera ocurrencia. | haya al menos dos opciones y una decisión justificada. | una alternativa + mejora de la original. |
| 00:20–00:26 / D4 | PÍLDORA DOCENTE 1/1: Explica literal de texto y concatenación solo porque ahora necesitan insertar un dato. | Predice la salida. | Confusión entre + como suma y concatenación. | puedan predecir el mensaje. | 4 minutos. |
| 00:26–00:40 / D5 | ACTIVIDAD: Circula y pide justificar decisiones. | Programa, prueba e itera. | Mensajes que prometen funciones aún inexistentes. | la salida sea legible y coherente con H1. | omite el intercambio y haz revisión rápida por parejas. |
| 00:40–00:45 / D6 | CIERRE: Pide un registro breve en el diario individual. | Documenta decisión y mejora. | Capacidad de justificar. | quede trazabilidad de la ideación. | respuesta oral + anotación posterior. |

## Qué debes explicar

- **PÍLDORA BREVE:** Conecta diseño de mensajes con experiencia de usuario sin introducir teoría extra.
- **PÍLDORA DOCENTE 1/1:** Explica literal de texto y concatenación solo porque ahora necesitan insertar un dato.

## Ejemplo o demostración preparada

**D1 · Dos salidas, ¿cuál ayuda más? —** A: MJ v1<br>
2026<br>
ok \| B: Hola, soy MiniJarvis.<br>
Estoy en mi primera versión por consola.<br>
Curso de trabajo: 2026.

**D2 · La consola también es una interfaz —** Aunque solo sea texto, alguien debe entender qué ocurre, qué se le pide y qué resultado obtiene.

**D3 · Generad alternativas antes de programar —** Cada equipo propone al menos 2 versiones de:<br>
• saludo<br>
• propósito<br>
• mensaje final<br>
<br>
Todavía NO programéis.

**D4 · Literal y concatenación —** String userName = "Laura";<br>
System.out.println("Hola, " + userName + ".");

**D5 · Construye y mejora la salida elegida —** 1. Implementa los mensajes.<br>
2. Ejecuta.<br>
3. Pide a otra persona que lea solo la consola.<br>
4. Mejora una frase si hace falta.

**D6 · Registra la decisión de diseño —** ¿Qué mensaje elegiste?<br>
¿Por qué?<br>
¿Qué cambiaste después de verlo ejecutado?

## Consigna que se entrega al alumnado

1. Predice antes de ejecutar cuando haya código.
2. Realiza la micropráctica o modificación prevista.
3. Prueba el caso normal y, cuando exista una decisión o conversión, también el caso alternativo o erróneo.
4. Conserva el código o resultado en el repositorio o espacio indicado.
5. Registra una sola entrada en el diario individual; no crees un informe paralelo.

## Qué observar mientras trabajan

- Criterios de claridad y orden.
- Mensajes técnicos o ambiguos.
- Si idean de verdad o copian la primera ocurrencia.
- Confusión entre + como suma y concatenación.
- Mensajes que prometen funciones aún inexistentes.
- Capacidad de justificar.

## Criterios para considerar cerrada la sesión

- Aparezcan criterios propios.
- Tengan 2–3 criterios.
- Haya al menos dos opciones y una decisión justificada.
- Puedan predecir el mensaje.
- La salida sea legible y coherente con H1.
- Quede trazabilidad de la ideación.
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
