# S210 — Guía docente

## Variables: guardar datos con nombre y tipo

| Dato | Valor |
|---|---|
| Hito | H1 — Primer MiniJarvis |
| Duración | 2 periodos; checkpoint proyectable de 45 minutos y taller asociado |
| Fase HEXA | Planificar — organizar el trabajo |
| Agrupamiento | Individual con contraste por parejas o equipo cuando la práctica lo requiera |
| Resultado observable | Planificar datos y comprender variable, tipo, nombre, declaración, inicialización y asignación. |
| Evidencia mínima | Quede evidencia individual. |

## Propósito

Planificar datos y comprender variable, tipo, nombre, declaración, inicialización y asignación.

El concepto se incorpora al Tema 1, pero solo pasa a `Main.java` cuando mejora el producto mínimo. Las demás prácticas se conservan como microejercicios defendibles.

## Material imprescindible

- presentación de S210;
- IntelliJ y JDK cuando haya práctica de código;
- proyecto o microarchivo de prueba;
- diario individual y tablero Scrum del equipo;
- datos ficticios.

## Secuencia de aula

| Tiempo / diap. | Tipo y actuación | Alumnado | Observa | Puerta de avance | Si hay retraso |
|---|---|---|---|---|---|
| 00:00–00:05 / D1 | PLANIFICAR: Provoca la necesidad de almacenar datos. | Detecta repetición. | Si proponen copiar/pegar en vez de guardar. | aparezca la idea de un único dato reutilizable. | 3 minutos. |
| 00:05–00:11 / D2 | PÍLDORA DOCENTE 1/4: Usa la metáfora de casilla etiquetada y conecta con RAM de Tema 1 sin profundizar en binario. | Explica una variable con sus palabras. | Si dicen que variable y valor son exactamente lo mismo. | puedan distinguir variable/valor. | 5 minutos. |
| 00:11–00:18 / D3 | PÍLDORA DOCENTE 2/4: Presenta el mapa completo; para uso inmediato céntrate en int, double, boolean, char y String. | Asocia datos a tipos. | String vs char; entero vs decimal. | clasifiquen ejemplos básicos. | muestra mapa y trabaja solo 5 tipos de uso inmediato. |
| 00:18–00:23 / D4 | MICROPRÁCTICA: Pide respuesta y razón, no solo el nombre del tipo. | Clasifica. | Razonamiento sobre naturaleza del dato. | justifiquen al menos 4 casos. | 3 casos. |
| 00:23–00:28 / D5 | PÍLDORA DOCENTE 3/4: Conecta con identificadores de S208 y legibilidad. | Renombra ejemplos pobres. | Nombres vagos. | produzcan nombres válidos y semánticos. | un ejemplo y una corrección. |
| 00:28–00:33 / D6 | PÍLDORA DOCENTE 4/4: Explica que el tipo se escribe al declarar, no cada vez que cambia el valor. Diferencia = de igualdad matemática. | Predice valor antes/después. | Repetición del tipo en la asignación. | puedan señalar declaración/inicialización/asignación. | 4 minutos. |
| 00:33–00:36 / D7 | PLANIFICACIÓN: Modela una fila y detente. | Planifica 3–5 datos. | Código sin plan. | cada dato tenga tipo/nombre/uso. | 3 datos. |
| 00:36–00:42 / D8 | ACTIVIDAD: Circula y pregunta qué línea prueba el cambio. | Programa y prueba. | Variables no usadas y tipos incompatibles. | haya salida antes/después de una asignación. | haz 2 variables y una asignación. |
| 00:42–00:45 / D9 | CIERRE: Pregunta sobre su propio código. | Explica. | Comprensión real de las partes. | quede evidencia individual. | una pregunta rápida a varias personas. |

## Qué debes explicar

- **PÍLDORA DOCENTE 1/4:** Usa la metáfora de casilla etiquetada y conecta con RAM de Tema 1 sin profundizar en binario.
- **PÍLDORA DOCENTE 2/4:** Presenta el mapa completo; para uso inmediato céntrate en int, double, boolean, char y String.
- **PÍLDORA DOCENTE 3/4:** Conecta con identificadores de S208 y legibilidad.
- **PÍLDORA DOCENTE 4/4:** Explica que el tipo se escribe al declarar, no cada vez que cambia el valor. Diferencia = de igualdad matemática.

## Ejemplo o demostración preparada

**D1 · Un dato repetido, un problema —** Si el curso aparece en tres mensajes y después cambia el año, ¿cuántos sitios tendrías que modificar?

**D2 · Variable = dato + nombre + memoria —** IDEA: Una variable es una zona de memoria con un nombre que guarda un dato. \| EJEMPLO: int studyHours = 4;<br>
<br>
String userName = "Laura";

**D3 · Mapa de tipos que aparecen en Tema 1 —** ENTEROS: byte / short / int / long \| DECIMALES: float / double \| OTROS: char / boolean / String

**D4 · Elige el tipo adecuado —** Nombre de usuario → ?<br>
Horas de estudio → ?<br>
Nota media → ?<br>
Objetivo alcanzado → ?<br>
Inicial → ?

**D5 · Nombres válidos y significativos —** MEJOR: userName<br>
studyHours<br>
averageScore \| EVITA: x<br>
data1<br>
1name<br>
my name<br>
class

**D6 · Declarar, inicializar y asignar —** int studyHours = 4; // declara + inicializa<br>
<br>
studyHours = 5; // asigna otro valor

**D7 · Antes del código: plan de datos —** Dato \| Tipo \| Nombre \| ¿Cambia? \| ¿Dónde se usa?

**D8 · Implementa el plan y comprueba —** Crea variables, muéstralas, cambia una y vuelve a ejecutar.

**D9 · Microdefensa de una variable —** Señala tipo, nombre, valor inicial y una asignación posterior.

## Consigna que se entrega al alumnado

1. Predice antes de ejecutar cuando haya código.
2. Realiza la micropráctica o modificación prevista.
3. Prueba el caso normal y, cuando exista una decisión o conversión, también el caso alternativo o erróneo.
4. Conserva el código o resultado en el repositorio o espacio indicado.
5. Registra una sola entrada en el diario individual; no crees un informe paralelo.

## Qué observar mientras trabajan

- Si proponen copiar/pegar en vez de guardar.
- Si dicen que variable y valor son exactamente lo mismo.
- String vs char; entero vs decimal.
- Razonamiento sobre naturaleza del dato.
- Nombres vagos.
- Repetición del tipo en la asignación.
- Código sin plan.
- Variables no usadas y tipos incompatibles.
- Comprensión real de las partes.

## Criterios para considerar cerrada la sesión

- Aparezca la idea de un único dato reutilizable.
- Puedan distinguir variable/valor.
- Clasifiquen ejemplos básicos.
- Justifiquen al menos 4 casos.
- Produzcan nombres válidos y semánticos.
- Puedan señalar declaración/inicialización/asignación.
- Cada dato tenga tipo/nombre/uso.
- Haya salida antes/después de una asignación.
- Quede evidencia individual.
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
