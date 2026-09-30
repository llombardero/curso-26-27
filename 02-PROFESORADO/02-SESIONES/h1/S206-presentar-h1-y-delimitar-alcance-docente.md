# S206 — Presentar H1 y delimitar su alcance

| Dato | Valor |
|---|---|
| Hito | H1 — Primer asistente ejecutable |
| Duración prevista | 45 minutos |
| Fase HEXA del hito | Activar — entender el reto |
| Modalidad de trabajo | **INDIVIDUAL → EQUIPO** |

## Finalidad de la sesión

S206 abre H1. La sesión permite seguir este recorrido:

```text
entender el reto
→ delimitar qué entra
→ delimitar qué queda fuera
→ comprender cómo sabremos que H1 funciona
```

MiniJarvis se presenta como una primera versión Java pequeña, clara, ejecutable y defendible, no como una IA completa. Hoy se acuerda el alcance; no se realiza todavía una implementación extensa.

## Antes de entrar en clase

- [ ] Preparar las tres columnas de clasificación: `entra en H1`, `más adelante` y `fuera del reto`.
- [ ] Tener disponible el ejemplo Java para proyectarlo sin convertirlo en una práctica larga.
- [ ] Localizar el Scrum de los equipos para registrar únicamente decisiones y tareas reales.
- [ ] Recordar que solo se utilizarán datos ficticios: nunca datos personales, contraseñas, tokens, claves API o credenciales.

## Apertura docente

Di en voz alta:

> Hoy empieza H1, el primer MiniJarvis ejecutable. No vamos a construir una IA completa. Vamos a construir una primera versión pequeña, clara, ejecutable y defendible. El éxito no consiste en hacer muchas cosas, sino en hacer las necesarias, entenderlas y poder comprobarlas.

Explica brevemente que **Activar** significa comprender el reto antes de construir. Un alcance confuso conduce a implementar funciones que todavía no corresponden o a aceptar resultados que no demuestran nada.

## Activación — INDIVIDUAL

Antes de escuchar el acuerdo del equipo, cada persona formula su propio criterio. Puede hacerlo oralmente o en un borrador de trabajo; no se crea una ficha nueva.

Debe concretar:

- una frase breve: `H1 consiste en...`;
- qué cree que entra en H1;
- qué cree que queda fuera por ahora;
- una duda real de alcance, si la tiene;
- una forma observable de saber que H1 funciona.

No se busca acertar una lista memorizada. Esta respuesta inicial permite comparar criterios y evita que una sola persona decida por todo el grupo.

## Alcance técnico de H1

H1 recorre fundamentos suficientes para construir, comprobar y explicar un primer programa:

- entorno, proyecto y ejecución;
- estructura básica de Java;
- salida por consola;
- variables y constantes;
- operaciones sencillas;
- entrada mediante `Scanner`;
- conversiones;
- comparación;
- una decisión sencilla;
- explicación y defensa de lo construido.

No todo debe aparecer necesariamente dentro de un único `Main.java`. Algunas partes pueden trabajarse mediante microprácticas para aprender los conceptos, comprobarlos y poder defenderlos.

Quedan fuera del alcance actual:

- menú de comandos, bucle principal y `switch`;
- memoria y colecciones;
- ficheros y persistencia;
- arquitectura o clases complejas;
- integración con una API de IA o una IA real.

Estas exclusiones no significan que nunca se trabajarán. Permiten mantener H1 pequeño y comprensible sin adelantar contenidos posteriores.

Pregunta:

> ¿Por qué empezar directamente con una API o una IA completa dificultaría explicar y defender los fundamentos Java de esta primera versión?

## Calidad de un primer programa

Estas tres ideas sirven para juzgar el alcance, no para abrir una clase teórica de calidad de software.

### Correcto

El programa realiza el comportamiento esperado y ese comportamiento puede comprobarse. Que no aparezca un error de compilación es necesario, pero no demuestra por sí solo que haga lo pedido.

> Compilar no basta para decir que es correcto. Falta comprobar comportamiento.

Pregunta:

> ¿Qué entrada y qué resultado permitirían comprobar el comportamiento que afirmáis haber construido?

### Eficiente

En H1 no significa optimización avanzada ni máxima velocidad. Significa resolver el reto sin añadir complejidad innecesaria.

### Mantenible

El programa puede entenderse y modificarse sin introducir dificultad innecesaria. Los nombres claros y un alcance pequeño ayudan a conseguirlo.

## Ejemplo Java para analizar

Proyecta el bloque sin convertirlo en una explicación detallada de sintaxis:

```java
final String NOMBRE_ASISTENTE = "MiniJarvis";
String nombreUsuario = "Laura";
System.out.println("Hola, soy " + NOMBRE_ASISTENTE + ".");
System.out.println("Encantado, " + nombreUsuario + ".");
```

Pregunta al alumnado:

- ¿qué comportamiento visible aporta cada línea?;
- ¿qué requisito permite comprobar?;
- ¿qué elementos ayudan a comprender el programa?;
- ¿qué parte sería innecesaria si excediera el alcance de H1?

El ejemplo ayuda a razonar sobre alcance, comportamiento y claridad. La estructura y la sintaxis se desarrollan después.

## Actividad de clasificación — EQUIPO

Después de la activación individual, el equipo compara los criterios y clasifica exactamente estas propuestas:

- saludar;
- pedir un nombre ficticio;
- guardar horas de estudio;
- calcular minutos;
- hacer un menú;
- recordar conversaciones;
- guardar en fichero;
- usar una API de IA;
- mostrar un mensaje final;
- decidir si se ha alcanzado un objetivo.

Columnas:

```text
entra en H1 | más adelante | fuera del reto
```

El equipo debe:

1. escuchar primero los criterios individuales;
2. clasificar cada propuesta usando el alcance, no el gusto personal;
3. justificar al menos dos decisiones significativas, incluida una exclusión;
4. acordar una frase común `H1 consiste en...`;
5. concretar cómo podrá comprobarse el resultado;
6. separar el núcleo de H1 de posibles ampliaciones futuras.

Una clasificación distinta puede ser discutible si está respaldada por los límites del reto. La finalidad es comprender y justificar el alcance.

## Acuerdo y Scrum del equipo

Definir el alcance y el backlog inicial es trabajo real. El equipo conserva en Scrum solo lo que vaya a utilizar después:

- frase común de alcance;
- requisitos comprobables;
- elementos incluidos y excluidos;
- justificación de una decisión relevante;
- tareas iniciales reales;
- bloqueo real, si aparece.

Modelo orientativo:

```text
Alcance H1:
H1 es una primera versión de MiniJarvis en consola para practicar y demostrar fundamentos de Java.

Incluye:
Comportamientos y conceptos que el equipo podrá comprobar y explicar.

Queda fuera por ahora:
Funciones que ampliarían el reto más allá de H1.

Decisión y motivo:
...

Primeras tareas reales:
...
```

No se añaden tareas ni campos para demostrar que S206 ocurrió. Una frase como `hacer que funcione` no es suficiente: debe indicar un comportamiento comprobable.

## Persistencia mínima

- **Scrum:** conserva el alcance, backlog, decisión o bloqueo real del equipo.
- **Diario individual:** solo interviene si surge un aprendizaje, duda, bloqueo o cambio de criterio personal significativo; no hay fila S206 obligatoria.
- **GitHub:** solo recibe un artefacto técnico si el equipo lo crea realmente dentro del flujo del proyecto; el ejemplo docente no genera una entrega de código.
- **Moodle:** no hay entrega en S206.
- **Drive y Sites:** no se crean ni actualizan; tampoco se producen capturas o documentos paralelos.
- **IA:** H1 no integra servicios ni API de IA en MiniJarvis y no genera un registro separado por defecto. Nunca se introducen claves, tokens, credenciales ni datos personales reales.

## Observación docente

Comprueba específicamente si el alumnado:

- formula un criterio propio antes del acuerdo;
- distingue compilar de funcionar correctamente;
- comprende `correcto`, `eficiente` y `mantenible` en el nivel de H1;
- diferencia el núcleo de H1 de ampliaciones posteriores;
- explica por qué una funcionalidad queda fuera;
- entiende que MiniJarvis crecerá progresivamente;
- evita atribuir al incremento capacidades inexistentes;
- propone comportamientos comprobables y defendibles.

## Andamiaje ante bloqueos

- **Quieren incluir todo:** «¿Qué es imprescindible para demostrar el primer aprendizaje?»
- **Quieren empezar con IA:** «¿Qué fundamentos Java podríais explicar y defender antes?»
- **Confunden compilar con correcto:** «¿Qué comportamiento concreto comprobaríais?»
- **No saben excluir una función:** «¿Es necesaria para cumplir el reto H1?»
- **Una persona domina el acuerdo:** pide primero el criterio individual del resto.
- **Alcance demasiado vago:** pide comportamientos observables.
- **Alcance demasiado grande:** separa núcleo H1 y futuro.

No resuelvas la clasificación por el equipo. Devuelve la decisión a los criterios acordados.

## Temporalización orientativa

| Tiempo | Acción |
|---|---|
| 0–6 min | Presentar H1 y formular individualmente alcance, exclusión, duda y criterio de comprobación. |
| 6–13 min | Explicar el alcance completo y las ideas de correcto, eficiente y mantenible. |
| 13–18 min | Analizar brevemente el ejemplo Java histórico. |
| 18–30 min | Comparar criterios y clasificar las propuestas en equipo. |
| 30–38 min | Acordar frase de alcance, requisitos comprobables y justificaciones. |
| 38–42 min | Registrar únicamente alcance, backlog, decisión o bloqueo real en Scrum. |
| 42–45 min | Comprobar respuestas finales y conectar con S207. |

## Cierre

Al terminar, cada persona y cada equipo deben poder responder:

```text
qué vamos a construir
qué no vamos a construir todavía
cómo sabremos si H1 cumple su objetivo
```

Cierra con la transición:

> Después de entender el reto, investigaremos cómo se pasa del código fuente a la compilación, la ejecución y la consola.

## Al terminar

Anota únicamente información útil para la continuidad docente: alumnado que necesite apoyo en la siguiente sesión, una confusión o error común que convenga retomar, un equipo con alcance inabarcable o un bloqueo real y cualquier ajuste temporal necesario para una futura aplicación.
