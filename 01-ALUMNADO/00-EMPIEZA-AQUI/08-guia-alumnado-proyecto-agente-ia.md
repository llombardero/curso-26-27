# Guía del alumnado — Proyecto Agente IA

## Programación — 1.º DAW — Curso 2026/2027

---

## 1. Qué vamos a hacer durante el curso

Durante el curso vais a construir poco a poco un pequeño agente IA propio.

No empezaremos usando inteligencia artificial real desde el primer día. Primero aprenderemos las bases necesarias para poder construir, entender, probar y defender el proyecto.

La idea general es esta:

> Seremos equipos de desarrollo que construyen, documentan, prueban y defienden un asistente inteligente propio, usando Java, herramientas profesionales, Scrum e IA responsable.

El proyecto se llama de forma orientativa:

```text
MiniJarvis
```

Al final del curso, el proyecto podrá tener:

- un agente por consola en Java;
- comandos o herramientas internas;
- memoria temporal;
- clases y objetos bien organizados;
- pruebas y depuración;
- documentación clara;
- uso de Git/GitHub;
- diagramas;
- persistencia en ficheros o base de conocimiento simple;
- uso significativo de IA en diario o Scrum;
- defensa individual;
- integración real con Gemini/Jarvis o simulación robusta, si el grupo llega preparado.

Lo importante no es que la IA “haga” el proyecto.

Lo importante es que aprendáis a construir software, verificarlo, explicarlo y usar IA con criterio.

---

## 2. Cómo se trabaja por hitos

El curso se organiza por hitos. Cada hito añade una capacidad nueva al agente.

Un hito es una entrega parcial con un objetivo claro.

No se espera que el proyecto final aparezca de golpe. Se irá construyendo por versiones.

| Tramo | Qué construiremos o trabajaremos |
|---|---|
| H0. Bootcamp Scrum | Conoceremos el curso y Scrum, reconoceremos habilidades, prepararemos equipos provisionales de 3 o 4 y aplicaremos el sprint en la torre. |
| H1. Primer asistente básico | Programa Java básico por consola: saludo, nombre, variables, constantes y README. |
| H2. Decisiones y depuración | Agente con menú, comandos, bucles, gestión de errores, pruebas y depuración. |
| H3. Memoria en colecciones | Agente que recuerda información durante la ejecución usando colecciones. |
| C1. Cierre 1.ª evaluación | Demo parcial, selección de evidencias, revisión y recuperación si procede. |
| H4. Agente orientado a objetos | Rediseño con clases, objetos, responsabilidades y diagramas UML. |
| H5. Herramientas, código limpio y patrones iniciales | Agente extensible, refactorización y patrones cuando tengan sentido. |
| C2. Cierre 2.ª evaluación | Demo parcial, revisión del producto, defensa y recuperación si procede. |
| H6. Persistencia y trazabilidad | Persistencia, trazabilidad, reproducibilidad y seguridad según el alcance trabajado. |
| H7. IA responsable opcional | Integración responsable de IA o simulación robusta y defendible, según el progreso del curso. |
| FFEOE | Periodo sin clases ni entregas del módulo. |
| HF. Presentación final | Defensa final, selección final de evidencias, demo, recuperación y mejora. |

Esta tabla muestra la **secuencia del curso**, no un calendario cerrado. Las fechas concretas dependen de la temporalización vigente.

### H0 comienza antes de la torre

1. Presentación de curso, hitos, HEXA, evidencias, defensa e IA responsable.
2. Scrum mínimo: sprint, backlog, bloqueo, prueba, review y retrospectiva.
3. Diagnóstico sin nota: autoevaluación + microprueba + observación.
4. Equipos provisionales de tres o cuatro, con habilidades y apoyos variados.
5. Sesión siguiente: torre, review, retrospectiva y revisión de equipos.

El diagnóstico no es una prueba psicológica. No se publican puntuaciones, no fija roles y no se utiliza para decidir quién “vale”. Los roles rotan y todas las habilidades se desarrollan.

Cada hito tendrá:

1. una explicación del reto;
2. una lista de tareas;
3. entregables concretos;
4. relación con Programación;
5. normas de uso de IA;
6. defensa oral o revisión técnica.

Material de estudio:

```text
El libro del alumnado se entregará por capítulos asociados a cada hito.
No recibirás todo el libro como obligación inicial: trabajarás cada capítulo cuando lo necesites para construir MiniJarvis.
```

Ejemplos de Laura:

```text
Los ejemplos de Laura se mostrarán después de que hayas intentado tu propia solución o cerrado una primera versión defendible.
Sirven para comparar, mejorar y preparar la defensa, no para copiar antes de pensar.
```

---

## 3. Qué se entrega

No se crea un documento nuevo para cada actividad o evidencia. Cada resultado se conserva en su fuente canónica y se reutiliza cuando haya que demostrar el aprendizaje.

### 3.1. Evidencias de equipo

Según el hito, el equipo puede dejar:

- código y versión estable en GitHub;
- README con las instrucciones necesarias;
- pruebas realizadas y resultados relevantes;
- diagramas cuando correspondan;
- Scrum actualizado cuando haya tareas, decisiones, bloqueos o retrospectiva relevantes;
- demo o ejecución comprobable del producto;
- evidencia no-code excepcional en Drive cuando no tenga una ubicación mejor.

No se copia el código, el README ni las pruebas a otros lugares solo para volver a entregarlos.

### 3.2. Evidencias individuales

Cada persona demuestra su aprendizaje mediante las evidencias existentes y su capacidad para explicarlas.

Según corresponda:

- registra en el diario un aprendizaje, aportación, decisión, bloqueo o uso de IA significativo;
- selecciona evidencias para el Site personal en C1, C2 y HF;
- explica una parte del código o una decisión técnica;
- realiza la comparación Java ↔ Python y la integra en el diario o la selecciona posteriormente para el Site cuando aporte valor;
- participa en la defensa individual;
- realiza una recuperación específica cuando quede aprendizaje pendiente.

No hay un portfolio, registro de IA ni ficha de defensa independiente por cada hito.

### 3.3. Estructura del repositorio

El repositorio contiene principalmente el producto técnico y la información necesaria para comprenderlo y reproducirlo.

Una estructura orientativa incluye:

- README.md
- src/
- .gitignore

Se incorporan pruebas, diagramas u otros recursos técnicos cuando el hito los necesita.

No se crea una carpeta docs por defecto para duplicar diario, Scrum, defensa, incidencias o registros que ya tienen otra fuente canónica.

---

## 4. Qué se espera en cada entrega

Una entrega válida debe permitir comprobar tres cosas:

1. Que el producto funciona o puede revisarse.
2. Que existe trazabilidad suficiente del proceso.
3. Que cada alumno o alumna puede explicar su aportación y el producto trabajado.

No basta con subir código, pero tampoco es necesario duplicar evidencias en documentos separados.

Cada evidencia queda donde corresponde:

- código, versiones y pruebas técnicas: repositorio;
- instrucciones de ejecución y documentación técnica necesaria: README;
- trabajo, decisiones, bloqueos y retrospectiva del equipo: Scrum;
- aprendizaje y aportaciones individuales significativas: diario;
- selección de evidencias: Site personal en C1, C2 y HF;
- comprensión y autoría: defensa sobre el producto real;
- evidencia no-code excepcional: Drive, solo cuando no tenga mejor ubicación.

En Moodle se registra la versión evaluada y se confirma la actualización de las fuentes estables. No se vuelven a adjuntar rutinariamente README, capturas, registros de IA, PDF o XLSX.

Regla práctica:

Construye. Comprueba. Deja trazabilidad donde corresponde. Explica lo que has hecho. No dupliques evidencias.

---

## 5. Cómo se usa IA en este curso

La IA está permitida porque forma parte del trabajo profesional actual.

Pero se usará con reglas claras.

La IA puede ayudarte a:

- entender conceptos;
- pedir ejemplos pequeños;
- revisar errores;
- preparar pruebas;
- mejorar documentación;
- comparar Java con Python;
- proponer mejoras;
- preparar una defensa;
- revisar un README o portfolio.

La IA no puede sustituir tu aprendizaje.

Regla básica:

```text
Puedes usar IA como copiloto, tutor o revisor.
No puedes usarla como autor oculto de tu entrega.
```

### 5.1. Semáforo de IA

| Color | Significado | Ejemplos |
|---|---|---|
| Verde | Permitido y recomendado | Pedir explicaciones, entender errores, revisar claridad, pedir ejemplos pequeños, generar preguntas de repaso. |
| Amarillo | Permitido con trazabilidad, verificación y defensa | Generar fragmentos de código, proponer tests, refactorizar, traducir Java a Python, sugerir diagramas o patrones. |
| Rojo | No permitido | Copiar una solución completa sin entenderla, ocultar uso de IA, usar IA en pruebas no autorizadas, introducir datos personales, subir secretos o claves. |

### 5.2. Trazabilidad del uso significativo de IA

No necesitas crear un registro de IA independiente.

Cuando la IA haya influido de forma significativa en una actividad o producto evaluable, deja una nota breve:

- en el diario individual, si el uso y el aprendizaje son personales;
- en Scrum, si el uso corresponde a una decisión o trabajo del equipo.

La nota debe permitir explicar:

- para qué se utilizó la IA;
- qué aportó;
- qué aceptaste, modificaste o descartaste;
- cómo comprobaste el resultado.

Si aporta valor para comprender el proceso, puedes conservar también el prompt o un resumen fiel.

No es necesario registrar consultas triviales que no hayan influido de forma significativa en el trabajo.

### 5.3. Seguridad

Nunca debes introducir en una IA ni subir a GitHub:

- contraseñas;
- tokens;
- claves API;
- archivos `.env` reales;
- datos personales;
- datos de compañeros/as;
- credenciales de GitHub, Moodle, Gemini o Jarvis.

Si hace falta simular datos, se usarán datos ficticios.

Ejemplo permitido:

```text
API_KEY_EJEMPLO
usuario_prueba
mensaje de ejemplo sin datos personales
```

---

## 6. Cómo se evalúa

La evaluación del módulo de Programación se apoya en sus Resultados de Aprendizaje y Criterios de Evaluación.

MiniJarvis organiza buena parte del trabajo del curso, pero el proyecto no sustituye la evaluación propia del módulo.

Las evidencias permiten comprobar tanto el funcionamiento del producto como el aprendizaje individual.

Por ejemplo:

- el código permite comprobar la aplicación de los contenidos trabajados;
- las pruebas permiten verificar el funcionamiento y detectar errores;
- el README permite comprobar que el producto puede comprenderse y ejecutarse;
- la trazabilidad permite reconstruir decisiones y cambios relevantes;
- la defensa permite comprobar comprensión y autoría individual.

### 6.1. Qué se valora

Se valorará especialmente:

- funcionamiento técnico;
- ajuste al hito;
- código limpio y comprensible;
- documentación;
- pruebas y verificación;
- uso de Git/GitHub y trazabilidad;
- uso responsable de IA;
- defensa oral;
- capacidad de corregir errores;
- mejora progresiva.

### 6.2. Rúbrica común

La escala general será:

| Nivel | Significado |
|---|---|
| 4 — Excelente | Cumple lo pedido con autonomía, claridad, calidad técnica y defensa sólida. |
| 3 — Adecuado | Cumple los requisitos principales con pequeños errores o aspectos mejorables. |
| 2 — Básico | Cumple parcialmente, pero necesita revisión o mejora. |
| 1 — Insuficiente | No cumple lo esencial, falta evidencia o no puede defenderse. |

Importante:

```text
Una entrega con buena apariencia técnica puede no ser válida si el alumno/a no puede explicarla, modificarla o defenderla.
```

---

## 7. Cómo conservar las evidencias sin formularios paralelos

No hay una plantilla nueva por sesión ni un documento independiente para cada tipo de evidencia.

El documento `07-plantillas-entregables` sirve para orientar dónde debe quedar cada resultado, no para obligarte a crear un archivo por cada actividad.

| Si ocurre esto… | Normalmente queda en… |
|---|---|
| Código, versión o prueba técnica | GitHub |
| Instrucciones para ejecutar o comprender el proyecto | README |
| Tarea, decisión, bloqueo o retrospectiva del equipo | Scrum |
| Aprendizaje o aportación individual significativa | Diario individual |
| Uso significativo de IA | Diario o Scrum, según autoría |
| Comparación Java ↔ Python | Diario o selección posterior para el Site cuando aporte valor |
| Evidencia para un cierre periódico | Site personal o de equipo en C1, C2 o HF |
| Defensa | Explicación oral o técnica sobre el producto; no requiere una plantilla escrita |
| Evidencia no-code sin mejor ubicación | Drive |
| Entrega oficial | Moodle, mediante la versión evaluada y las confirmaciones necesarias |

### 7.1. Regla de mínima burocracia

Antes de crear un archivo nuevo, comprueba si la evidencia ya existe en el código, README, Scrum, diario o producto.

Si ya existe y puede revisarse, enlazarse o explicarse desde allí, no la copies a otro documento.

### 7.2. Cuándo crear documentación adicional

Solo crea documentación adicional cuando aporte información que no pueda conservarse adecuadamente en las fuentes anteriores o cuando la actividad lo indique expresamente.

---

## 8. Qué se espera en las defensas

Habrá defensas orales, revisiones técnicas o preguntas individuales durante el curso.

La defensa sirve para comprobar comprensión, no para pillar a nadie.

Pero si una entrega ha usado IA o es grupal, la defensa es especialmente importante.

En una defensa se puede pedir:

- explicar una función;
- explicar una clase;
- justificar una colección;
- explicar un diagrama;
- ejecutar el proyecto;
- modificar una línea;
- detectar un error;
- explicar una prueba;
- justificar un uso de IA;
- comparar Java y Python;
- explicar qué parte hizo cada persona.

Preguntas típicas:

```text
¿Qué hace esta parte del código?
¿Por qué elegisteis esta solución?
¿Qué error encontrasteis y cómo lo corregisteis?
¿Qué parte generó o sugirió la IA?
¿Qué modificaste tú?
¿Cómo comprobaste que funcionaba?
¿Qué pasaría si cambio este valor?
¿Qué datos no debe recibir nunca una IA?
```

Cada integrante debe saber defender su aportación y una parte razonable del producto común.

---

## 9. Qué hacer si el equipo se bloquea

Bloquearse forma parte del aprendizaje.

Cuando aparezca un problema:

1. anotad qué ocurre;
2. intentad reproducirlo;
3. revisad el mensaje de error;
4. buscad una hipótesis;
5. usad depuración o pruebas;
6. pedid ayuda si el bloqueo continúa;
7. registradlo en Scrum o diario únicamente si deja una decisión, bloqueo o aprendizaje significativo.

No se penaliza tener errores.

Sí puede afectar negativamente:

- ocultarlos;
- no probar nada;
- no documentar;
- entregar código que nadie entiende;
- decir “lo hizo la IA” sin poder explicarlo.

---

## 10. Checklist rápido antes de entregar

Antes de entregar un hito, revisad:

- el proyecto se puede abrir, revisar o ejecutar;
- el README contiene la información necesaria para comprenderlo y ejecutarlo;
- el código corresponde al nivel del hito;
- las pruebas solicitadas se han realizado y pueden reproducirse;
- Scrum está actualizado si hubo tareas, decisiones, bloqueos o retrospectiva relevantes;
- el diario recoge únicamente aprendizajes o aportaciones individuales significativas;
- el uso significativo de IA está registrado en diario o Scrum, según autoría;
- el Site está actualizado solo cuando corresponde a C1, C2 o HF;
- no hay datos personales, contraseñas, tokens ni otros secretos;
- cada integrante puede localizar, ejecutar y explicar su aportación;
- Moodle contiene únicamente la versión evaluada, las confirmaciones necesarias y cualquier evidencia no-code excepcional.

Esta lista sirve para revisar el trabajo. No hay que rellenarla, copiarla ni entregarla como documento independiente.

---

## 11. Idea final

Este curso no consiste solo en “hacer un programa”.

Consiste en aprender a trabajar como desarrolladores/as en formación:

- entender un problema;
- construir una solución paso a paso;
- usar herramientas profesionales;
- colaborar;
- probar;
- depurar;
- documentar;
- usar IA con responsabilidad;
- defender técnicamente lo aprendido.

La meta no es tener un agente perfecto.

La meta es que puedas decir:

```text
Sé qué he construido, sé cómo funciona, sé cómo lo he comprobado y puedo mejorarlo.
```
