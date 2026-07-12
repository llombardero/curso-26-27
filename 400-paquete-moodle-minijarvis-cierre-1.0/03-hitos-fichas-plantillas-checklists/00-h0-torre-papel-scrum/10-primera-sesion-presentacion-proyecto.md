# Guía docente — Primera sesión de presentación del proyecto

## Programación + Entornos de Desarrollo — 1.º DAW — Curso 2026/2027

Versión: cierre curricular 1.0 — julio 2026

Documento para uso del profesorado.

Documentos relacionados:

- `../../00-mapa-maestro-curso-2026-2027.md`
- `03-primera-semana-scrum-torre-papel.md`
- `../../08-guia-alumnado-proyecto-agente-ia.md`
- `../../09-presentacion-alumnado-proyecto-agente-ia.md`
- `../../05-politica-uso-ia-semaforo-registro-defensa.md`

---

## 1. Propósito de la sesión

Esta primera sesión sirve para presentar al alumnado la lógica general del curso y abrir el proyecto anual:

```text
MiniJarvis: construcción progresiva de un pequeño agente IA propio.
```

No es una sesión para explicar toda la programación didáctica ni todos los RA/CE.

Es una sesión para que el alumnado entienda:

- qué vamos a construir;
- por qué el curso se organiza por hitos;
- cómo se trabajará en equipo;
- qué papel tendrá la IA;
- qué significa entregar evidencias defendibles;
- cómo empezaremos con Scrum y la torre de papel.

La sesión debe generar motivación, orientación y primeras evidencias diagnósticas.

---

## 2. Duración prevista

Duración recomendada:

```text
3 periodos de 45 minutos = 135 minutos
```

Corresponde a la primera sesión larga de Programación prevista en H0.

Si solo se dispone de 45 o 90 minutos, ver adaptaciones en el apartado 12.

---

## 3. Objetivos docentes de la sesión

Al terminar la sesión, el alumnado debería poder explicar con sus palabras:

1. Que el curso se articulará alrededor de un proyecto de agente IA.
2. Que el agente se construirá por versiones, no de golpe.
3. Que Java será el lenguaje principal.
4. Que Programación y Entornos trabajarán de forma coordinada.
5. Que habrá entregas de equipo e individuales.
6. Que la IA se puede usar, pero con registro, verificación y defensa.
7. Que una entrega debe poder ejecutarse, documentarse y defenderse.
8. Que la primera semana se dedicará a aprender Scrum mediante una simulación práctica.

---

## 4. Materiales necesarios

### Para el docente

- Proyector o pantalla.
- Documento breve para alumnado:

```text
09-presentacion-alumnado-proyecto-agente-ia.md
```

- Documento completo de referencia:

```text
08-guia-alumnado-proyecto-agente-ia.md
```

- Pizarra física o digital.
- Cronómetro.
- Lista de clase para observación inicial.
- Notas adhesivas físicas o tablero digital, si se quiere iniciar ya la dinámica Scrum.

### Para el alumnado

- Cuaderno o documento de notas.
- Acceso a Moodle si ya está disponible.
- No es imprescindible ordenador en esta sesión, aunque puede usarse si el grupo ya dispone de equipo.

---

## 5. Evidencias que conviene recoger

Esta sesión no debe tener una carga calificadora fuerte.

Sí conviene recoger evidencias diagnósticas:

| Evidencia | Responsable | Uso docente |
|---|---|---|
| Respuesta inicial: “¿Qué creo que es un agente IA?” | Individual | Detectar ideas previas. |
| Preguntas o expectativas del alumnado | Individual / grupo | Ajustar ejemplos y ritmo. |
| Miniactividad de visión de producto | Parejas o grupos pequeños | Observar comunicación y comprensión del reto. |
| Ticket de salida | Individual | Comprobar comprensión mínima. |
| Observación docente | Docente | Detectar liderazgo, bloqueo, inseguridad, nivel técnico inicial. |

Estas evidencias pueden alimentar el diagnóstico inicial de Programación y la preparación de H0 en Entornos.

---

## 6. Secuencia detallada de la sesión

### Vista global

| Bloque | Tiempo | Finalidad |
|---|---:|---|
| 1. Apertura y encuadre | 10 min | Situar el curso y reducir incertidumbre. |
| 2. Activación de ideas previas | 15 min | Saber qué entiende el alumnado por IA, agente y programación. |
| 3. Presentación del proyecto MiniJarvis | 25 min | Explicar producto final y progresión por hitos. |
| 4. Cómo trabajaremos | 20 min | Introducir hitos, equipos, Scrum y evidencias. |
| 5. IA responsable | 15 min | Establecer reglas iniciales claras. |
| 6. Miniactividad: imaginar la primera versión | 25 min | Transformar la idea general en un producto mínimo. |
| 7. Puesta en común | 15 min | Compartir ideas y conectar con H0/H1. |
| 8. Cierre y ticket de salida | 10 min | Verificar comprensión y anunciar siguiente sesión. |

Total aproximado:

```text
135 minutos
```

---

## 7. Desarrollo docente paso a paso

### Bloque 1 — Apertura y encuadre

Tiempo:

```text
10 minutos
```

Objetivo:

- Dar seguridad.
- Presentar una narrativa clara del curso.
- Evitar que el alumnado piense que va a “programar una IA completa” desde el primer día.

Mensaje docente sugerido:

```text
Este curso vamos a aprender Programación y Entornos de Desarrollo construyendo un proyecto común: un pequeño agente IA propio.

No vamos a empezar usando IA real desde el primer día. Primero aprenderemos a programar, probar, depurar, documentar y trabajar en equipo.

La IA será una herramienta, no un sustituto de vuestro aprendizaje.
```

Errores a evitar:

- Prometer un producto final demasiado ambicioso.
- Presentar el proyecto como si ya tuvieran que saber IA.
- Empezar con RA/CE y porcentajes antes de explicar el sentido del curso.

---

### Bloque 2 — Activación de ideas previas

Tiempo:

```text
15 minutos
```

Dinámica:

1. Pregunta individual en papel, Moodle o cuaderno:

```text
¿Qué crees que es un agente IA?
```

2. Segunda pregunta:

```text
¿Qué tendría que hacer un asistente para que te pareciera útil en clase?
```

3. Tercera pregunta:

```text
¿Qué riesgos ves en usar IA para aprender programación?
```

Después, recoger 4-6 respuestas en voz alta.

Qué observar:

- Si confunden IA con buscador.
- Si creen que la IA debe hacerlo todo.
- Si aparecen miedos: “yo no sé programar”, “esto es muy difícil”.
- Si aparecen ideas útiles para futuros ejemplos del agente.

Intervención docente clave:

```text
Todas estas ideas nos sirven, pero durante el curso vamos a trabajar con una regla: todo lo que entreguemos debe poder entenderse, comprobarse y defenderse.
```

---

### Bloque 3 — Presentación del proyecto MiniJarvis

Tiempo:

```text
25 minutos
```

Usar como apoyo:

```text
09-presentacion-alumnado-proyecto-agente-ia.md
```

Explicar de forma breve:

- el proyecto será un asistente por consola en Java;
- empezará con mensajes simples;
- luego tendrá menú;
- luego memoria;
- luego clases;
- luego herramientas;
- luego persistencia;
- al final podrá tener IA real o simulada.

Pizarra recomendada:

```text
H1: saluda y responde algo simple
H2: menú y comandos
H3: memoria temporal
H4: clases y objetos
H5: herramientas internas
H6: ficheros y trazabilidad
H7: IA real o simulada, si procede
```

Mensaje docente sugerido:

```text
El proyecto final no es el punto de partida. El punto de partida será una versión muy pequeña que podamos entender completamente.

Cada hito añade una capacidad nueva. Si una versión pequeña está bien entendida, podremos hacer crecer el proyecto con seguridad.
```

Comprobación rápida:

Preguntar:

```text
¿Por qué creéis que no empezamos directamente conectando Gemini o Jarvis?
```

Respuestas esperables:

- porque primero hay que aprender Java;
- porque hay que saber validar;
- porque puede haber errores;
- porque no se deben usar datos sensibles;
- porque hay que entender el código.

---

### Bloque 4 — Cómo trabajaremos

Tiempo:

```text
20 minutos
```

Explicar tres ideas:

### 4.1. Hitos

Un hito es una versión parcial del producto.

Frase útil:

```text
No entregamos “todo el proyecto”. Entregamos versiones que demuestran aprendizaje concreto.
```

### 4.2. Equipos y Scrum

Explicar que durante la primera semana se vivirá Scrum con una actividad práctica: la torre de papel.

No explicar Scrum completo todavía. Solo vocabulario mínimo:

| Concepto | Explicación inicial |
|---|---|
| Sprint | Periodo corto de trabajo con un objetivo. |
| Backlog | Lista ordenada de tareas. |
| Tarea | Acción concreta que alguien puede realizar. |
| Review | Mostrar lo conseguido. |
| Retrospectiva | Pensar cómo mejorar el trabajo del equipo. |
| Bloqueo | Algo que impide avanzar. |

### 4.3. Evidencias

Explicar que se evaluará con evidencias:

- código;
- README;
- pruebas;
- portfolio;
- registro IA;
- diagramas;
- defensa;
- GitHub;
- observación y trabajo diario.

Mensaje docente sugerido:

```text
No basta con que exista un archivo. Debemos poder saber quién ha hecho qué, cómo se ha probado y si cada persona puede explicarlo.
```

---

### Bloque 5 — IA responsable

Tiempo:

```text
15 minutos
```

Objetivo:

- Establecer límites desde el primer día.
- Evitar tanto la prohibición total como el uso acrítico.

Explicar el semáforo de forma resumida:

| Color | Mensaje para alumnado |
|---|---|
| Verde | Puedes usar IA para entender, repasar, pedir ejemplos pequeños o revisar claridad. |
| Amarillo | Puedes usar IA para fragmentos, pruebas, refactorización o comparación, pero debes registrarlo y defenderlo. |
| Rojo | No puedes copiar soluciones completas, ocultar uso de IA, usar datos personales o entregar código que no entiendes. |

Frase clave:

```text
La IA puede ayudarte a aprender, pero no puede aprender por ti.
```

Mini-caso para comentar:

```text
Un alumno pide a una IA: “Hazme entero el H1 con menú, comandos, memoria y diseño avanzado”. Copia el código y lo entrega.

¿Está bien? ¿Qué problemas hay?
```

Respuestas esperables:

- no corresponde al nivel del hito;
- no demuestra aprendizaje;
- quizá no lo entiende;
- no está registrado;
- puede contener errores;
- puede impedir la defensa.

Cierre del bloque:

```text
Usaremos IA, pero con trazabilidad, seguridad y defensa.
```

---

### Bloque 6 — Miniactividad: imaginar la primera versión

Tiempo:

```text
25 minutos
```

Agrupamiento:

- parejas o grupos de 3.

Producto de la miniactividad:

```text
Boceto de MiniJarvis H1 sin código.
```

Instrucciones para alumnado:

```text
Imaginad la primera versión mínima de vuestro asistente.
Todavía no programamos.
Solo definimos qué podría hacer en una versión muy básica.
```

Preguntas guía:

1. ¿Cómo se llamaría vuestro asistente?
2. ¿Qué saludo inicial mostraría?
3. ¿Qué dato pediría al usuario?
4. ¿Qué respuesta sencilla daría?
5. ¿Qué NO debería hacer todavía en H1?
6. ¿Qué tendría que poder explicar cualquier persona del equipo?

Restricción importante:

```text
H1 no tendrá menú, bucles, switch, memoria ni IA real.
```

Ejemplo de respuesta aceptable:

```text
Nombre: MiniJarvis Granada
Pide: nombre del usuario
Responde: saludo personalizado y mensaje de bienvenida al curso
No hace todavía: menú, memoria, conexión con IA ni comandos avanzados
```

Qué observar:

- si proponen soluciones demasiado avanzadas;
- si entienden la idea de versión mínima;
- si aparecen nombres o contextos motivadores;
- si hay alumnado que no participa;
- si surgen miedos o bloqueos.

---

### Bloque 7 — Puesta en común

Tiempo:

```text
15 minutos
```

Dinámica:

- 3 o 4 parejas/grupos comparten su boceto.
- El docente anota en pizarra ideas repetidas.
- Se clasifican en:

```text
Sirve para H1
Mejor para hitos posteriores
No es adecuado o necesita seguridad
```

Ejemplos:

| Idea del alumnado | Clasificación docente |
|---|---|
| Pedir nombre y saludar | H1. |
| Menú con varios comandos | H2. |
| Recordar preferencias | H3. |
| Crear clases Agente y Memoria | H4. |
| Conectar Gemini | H7 o simulación. |
| Guardar contraseñas | No adecuado / riesgo de seguridad. |

Mensaje docente clave:

```text
Una buena idea no tiene por qué hacerse en el primer hito. Muchas ideas se guardan para después.
```

---

### Bloque 8 — Cierre y ticket de salida

Tiempo:

```text
10 minutos
```

Ticket de salida individual:

Pedir que respondan en papel, Moodle o formulario breve:

```text
1. ¿Qué vamos a construir durante el curso?
2. ¿Por qué el proyecto se hará por hitos?
3. Escribe un uso permitido de IA.
4. Escribe un uso no permitido de IA.
5. ¿Qué significa que una entrega sea defendible?
6. ¿Qué duda te queda para la próxima sesión?
```

Uso docente:

- revisar rápidamente antes de la siguiente sesión;
- detectar malentendidos;
- ajustar la explicación de Scrum y H0;
- identificar alumnado que necesita apoyo inicial.

Cierre oral sugerido:

```text
En la próxima sesión vamos a vivir Scrum de forma práctica. No empezaremos programando todavía: primero aprenderemos cómo organizarnos como equipo.
```

---

## 8. Guion breve para el docente

Este guion puede usarse como apoyo directo en clase.

```text
Hoy no vamos a aprender toda la programación del curso de golpe.

Hoy vamos a entender el reto que nos acompañará durante el año: construir un pequeño agente IA propio.

Lo construiremos poco a poco. Primero será un programa muy simple en Java. Después tendrá menú, memoria, clases, herramientas, ficheros y quizá una integración con IA real o simulada.

La IA no será una forma de evitar aprender. Será una herramienta que tendremos que usar con criterio, registro y defensa.

En este curso una entrega válida debe poder ejecutarse, estar documentada y poder explicarse.

Durante la primera semana aprenderemos Scrum con una actividad práctica. Después aplicaremos esa forma de trabajo al proyecto del agente.
```

---

## 9. Lista de observación docente

Durante la sesión, conviene anotar evidencias rápidas.

| Alumno/a | Participa | Tiene ideas previas | Muestra inseguridad | Comprende IA responsable | Observaciones |
|---|---|---|---|---|---|
| | Sí / No / Parcial | Alta / Media / Baja | Sí / No | Sí / Parcial / No | |
| | Sí / No / Parcial | Alta / Media / Baja | Sí / No | Sí / Parcial / No | |
| | Sí / No / Parcial | Alta / Media / Baja | Sí / No | Sí / Parcial / No | |

No usar esta tabla para etiquetar de forma rígida al alumnado.

Uso recomendado:

- ajustar apoyos;
- detectar quién necesita más estructura;
- identificar alumnado con liderazgo positivo;
- preparar agrupamientos equilibrados.

---

## 10. Atención a la diversidad y DUA

### Representación

Ofrecer la información de varias formas:

- explicación oral;
- esquema en pizarra;
- documento breve `09`;
- tabla de hitos;
- ejemplos concretos de H1.

### Acción y expresión

Permitir distintas formas de responder:

- oralmente;
- por escrito;
- en pareja;
- mediante esquema;
- con frases cortas.

### Implicación

Reducir ansiedad inicial:

- insistir en que no se requiere saber IA ni Java avanzado;
- explicar que el primer hito será muy básico;
- valorar preguntas y dudas;
- separar ideas futuras de requisitos inmediatos.

Frase útil:

```text
No necesito que hoy sepáis programar el agente. Necesito que entendáis cómo vamos a empezar a construirlo.
```

---

## 11. Riesgos de la sesión y cómo mitigarlos

| Riesgo | Señal | Mitigación |
|---|---|---|
| El alumnado piensa que hará una IA completa desde cero | Preguntas sobre redes neuronales, ChatGPT propio o modelos | Reencuadrar: agente educativo pequeño, progresivo y por consola. |
| El alumnado cree que la IA hará los ejercicios | Comentarios tipo “se lo pido a Gemini” | Introducir defensa, registro y semáforo desde el primer día. |
| Exceso de información | Caras de bloqueo o silencio | Volver a tres ideas: proyecto, hitos, defensa. |
| Miedo a no saber programar | “Yo no sé nada” | Recordar que H1 empieza desde estructura básica. |
| Ideas demasiado avanzadas | APIs, bases de datos, web, móvil | Aparcarlas para hitos futuros. |
| Falta de participación | Solo habla una parte del grupo | Usar respuestas individuales y parejas antes de puesta en común. |

---

## 12. Adaptaciones según duración disponible

### Si solo hay 45 minutos

Priorizar:

1. Apertura y narrativa del proyecto.
2. Tabla de hitos muy resumida.
3. Semáforo básico de IA.
4. Ticket de salida.

Posponer:

- miniactividad de boceto;
- explicación más amplia de Scrum;
- puesta en común.

### Si hay 90 minutos

Mantener:

1. Apertura.
2. Ideas previas.
3. Presentación de hitos.
4. IA responsable.
5. Miniactividad reducida.
6. Ticket de salida.

Reducir:

- puesta en común;
- detalles de entregables.

### Si hay 135 minutos

Realizar la secuencia completa propuesta.

---

## 13. Producto docente esperado tras la sesión

Al terminar la sesión, el docente debería tener:

- impresión inicial del grupo;
- dudas frecuentes del alumnado;
- primeras ideas de agente propuestas por el alumnado;
- tickets de salida;
- señales de posibles agrupamientos;
- aspectos que conviene reforzar antes de la torre de papel.

---

## 14. Preparación de la siguiente sesión

Antes de la siguiente sesión, revisar:

1. Tickets de salida.
2. Dudas sobre IA responsable.
3. Ideas equivocadas sobre el alcance del proyecto.
4. Posibles agrupamientos para la torre de papel.
5. Materiales necesarios para H0.

La siguiente sesión debería conectar con:

```text
03-primera-semana-scrum-torre-papel.md
```

Objetivo de la siguiente sesión:

```text
Vivir un sprint corto mediante la torre de papel y traducirlo al modo de trabajo del proyecto MiniJarvis.
```

---

## 15. Criterio de éxito de esta primera sesión

La sesión habrá funcionado si la mayoría del alumnado puede decir:

```text
Este curso construiremos un agente paso a paso.
No tengo que saber IA avanzada desde el primer día.
La IA se puede usar, pero con responsabilidad.
Las entregas deben poder ejecutarse, documentarse y defenderse.
Empezaremos aprendiendo a trabajar por hitos y con Scrum.
```

<!-- AJUSTE-COBERTURA-CONCEPTOS-32 -->

## Ajuste curricular — cobertura de conceptos de Programación

Este hito queda alineado con el mapa `32-lista-conceptos-programacion-por-tema.md`.

```text
Hito: H0
Temas de referencia: base transversal de Entornos; no introduce todavía conceptos técnicos de Programación evaluables
Foco: preparación metodológica: Scrum de aula, evidencias, roles, comunicación técnica y primer backlog de MiniJarvis
```

Conceptos que deben trabajarse o, como mínimo, quedar conectados con evidencias del alumnado:

- problema
- requisito
- backlog
- evidencia
- review
- retrospectiva
- defensa oral

Criterio docente de cierre:

- El alumnado no solo entrega el producto; debe poder señalar dónde aparece cada concepto en su código, README, pruebas o defensa.
- Si un concepto se marca como ampliación, no penaliza al alumnado que alcance el mínimo, pero sí orienta mejora, recuperación o enriquecimiento.
- La defensa debe incluir al menos una pregunta de comprensión sobre los conceptos nuevos del hito.

