# Mapa maestro del curso 2026/2027

<!-- HEXA-POLITICA-TODOS-HITOS:START -->

## Política obligatoria: un ciclo HEXA completo en cada hito

La fuente metodológica canónica es `../04-RECURSOS-NORMATIVOS-Y-TEMARIOS/Modelo_HEXA_COMPLETO.pdf`; su aplicación operativa se documenta en `../04-RECURSOS-NORMATIVOS-Y-TEMARIOS/Modelo_HEXA_APLICADO_A_MINIJARVIS.md`.

Cada hito de MiniJarvis debe recorrer y evidenciar las seis fases: Activar, Investigar, Idear, Planificar, Ejecutar y Comunicar. La Fase 0 Equipos es la base transversal. No se considera aplicado HEXA mediante cuatro letras, una única actividad aislada o solo el producto final.

| Fase | Función obligatoria en cada hito | Evidencia mínima |
|---|---|---|
| 1 — Activar | Entender reto, propósito, límites y criterios. | Reformulación y diagnóstico inicial. |
| 2 — Investigar | Aprender y contrastar lo necesario. | Fuentes, micropíldoras, práctica guiada o base conceptual. |
| 3 — Idear | Generar alternativas y elegir con criterio. | Opciones y decisión argumentada. |
| 4 — Planificar | Organizar tareas, tiempos y responsabilidades. | Backlog, tablero o plan verificable. |
| 5 — Ejecutar | Construir, probar y mejorar. | Producto, iteraciones y pruebas. |
| 6 — Comunicar | Presentar, evaluar y reflexionar. | Defensa, auto/coevaluación, reflexión y mejora. |

Los cierres C1/C2 regulan o recuperan fases; no sustituyen el ciclo del hito.

### Trazabilidad por retos

| Hito | Reto | Expediente HEXA mínimo |
|---|---|---|
| H0 | Organizar y completar una torre de papel mediante un sprint Scrum y transferir lo aprendido a MiniJarvis. | ficha inicial, autoevaluación privada, microprueba, equipos razonados, backlog, torre comprobada, review, retrospectiva, revisión del equipo y aportación individual |
| H1 | Construir el primer MiniJarvis Java por consola, pequeño, ejecutable y defendible. | ficha del reto, salida diseñada, explicación de Main/variables/Scanner, programa, README, evidencia y defensa |
| H2 | Transformar MiniJarvis en un programa interactivo con decisiones, repetición y depuración reproducible. | mapa de comandos, hipótesis de flujo, explicación de condiciones/bucle, menú funcional, pruebas, depuración y defensa |
| H3 | Añadir memoria temporal mediante una colección adecuada y demostrar su comportamiento y límites. | requisitos de memoria, comparación de alternativas, explicación de ArrayList/casos límite, código, pruebas y defensa |
| H4 | Reorganizar MiniJarvis con orientación a objetos y responsabilidades que coincidan con el código y los diagramas. | diagnóstico de Main, alternativas de reparto, explicación POO/encapsulación, clases, diagramas, relación diagrama-código y defensa |
| H5 | Resolver el crecimiento de comandos mediante refactorización segura, contratos simples y código extensible. | diagnóstico del problema, comparación de diseños, explicación de interfaz/Command, refactorización, herramienta nueva, revisión Git y defensa |
| H6 | Conservar memoria e historial entre ejecuciones con ficheros, trazabilidad y tratamiento seguro de errores y datos. | problema reproducido, decisiones de ruta/formato, explicación de persistencia/excepciones/logs, código, prueba en dos ejecuciones, seguridad y defensa |
| H7 | Integrar o simular una ayuda de IA con límites, seguridad, registro y validación humana. | caso de uso y riesgos, clasificación de prompts, explicación de seguridad/validación, simulación o integración segura, registros y defensa |
| HF | Demostrar el aprendizaje del itinerario, localizar carencias y aplicar una mejora o recuperación basada en evidencias. | mapa de evidencias, selección razonada, explicación del progreso, portfolio, demo, defensa, recuperación y plan de mejora |

Regla de evaluación: el producto final por sí solo no acredita el proceso. Si falta una fase, se identifica y recupera su evidencia específica.

<!-- HEXA-POLITICA-TODOS-HITOS:END -->

## Programación — 1.º DAW — Granada

Edición final para Moodle — septiembre de 2026
Fecha de creación: 2026-07-04
Fuente de trabajo: documentación en `/mnt/compartido/Hlanz/Programacion/Curso 2026-2027`

---

## 1. Propósito del documento

Este documento define el mapa maestro de Programación de 1.º DAW, con 8 periodos semanales de 45 minutos.

El objetivo es concretar un marco común para el módulo mediante un proyecto guía anual. Las herramientas y prácticas de desarrollo se incorporan solo cuando son necesarias para construir, probar, documentar y defender MiniJarvis; no constituyen un currículo ni una evaluación independientes.

Proyecto guía:

> Diseño y construcción progresiva de un pequeño agente IA propio.

Este proyecto actuará como hilo conductor del curso mediante retos, hitos, tareas técnicas, defensas y evidencias vinculadas exclusivamente a los Resultados de Aprendizaje y Criterios de Evaluación de Programación.

---

## 2. Decisiones confirmadas

### 2.1. Metodologías

Se usarán de forma integrada:

- ABP / aprendizaje basado en proyectos y retos.
- Scrum adaptado al aula.
- Modelo HEXA.
- DUA, por la heterogeneidad del alumnado.
- Evaluación competencial mediante productos, procesos, defensas y evidencias.
- Código limpio, inspirado en Robert C. Martin, trabajado de forma progresiva y adaptada al nivel inicial del alumnado.
- Patrones de diseño, inspirados en Erich Gamma y el catálogo GoF, introducidos gradualmente cuando el alumnado tenga base suficiente de POO.

Arquitectura metodológica confirmada:

| Capa | Función |
|---|---|
| HEXA | Ordena la secuencia didáctica de cada reto o hito. |
| ABP | Da sentido profesional al proyecto anual. |
| Scrum | Organiza el trabajo de los equipos durante el curso. |
| RA/CE | Justifican la evaluación y la trazabilidad curricular. |
| DUA | Asegura múltiples formas de acceso, acción, expresión y apoyo. |
| IA responsable | Acompaña el aprendizaje, pero exige trazabilidad, comprensión y defensa. |

### 2.2. Proyecto mínimo viable del agente IA

Se acepta como mínimo viable:

> Un agente conversacional educativo en Java, ejecutable inicialmente por consola, que recibe una petición del usuario, mantiene una memoria simple, usa comandos o herramientas internas, registra trazabilidad, permite consultar una pequeña base de conocimiento, puede integrar opcionalmente una llamada a Gemini/Jarvis, incluye pruebas, documentación, diagrama de clases, tablero Scrum, defensa oral y registro de uso de IA.

La interfaz gráfica o web será un hito avanzado opcional, no requisito mínimo.

### 2.3. Lenguajes y tecnologías

Lenguaje principal:

- Java.

Lenguajes secundarios para transferencia en hitos:

- Python.
- JavaScript.

Herramientas previstas:

- Linux como entorno recomendado.
- Windows como entorno habitual del alumnado, con transición guiada hacia Linux cuando sea viable.
- IntelliJ IDEA para Java.
- Git y GitHub.
- Moodle.
- Docker.
- Gemini, por acuerdo de la Junta de Andalucía con Google.
- Jarvis, modelo propio disponible para consulta.

Criterio para Docker:

- Obligatorio mínimo: uso guiado de contenedores ya preparados.
- Avanzado: creación de Dockerfile o docker-compose propio.

### 2.4. Organización de equipos

- Grupos de 3 o 4 alumnos/as.
- Excepcionalmente, trabajo individual si un alumno no puede trabajar en grupo.
- Roles Scrum adaptados al aula, no roles Scrum completos.

Roles iniciales sugeridos:

| Rol adaptado | Función |
|---|---|
| Facilitador/a | Cuida reuniones, acuerdos y bloqueos. |
| Responsable de backlog | Mantiene tareas, criterios de aceptación y tablero. |
| Responsable técnico/a | Coordina decisiones de código, pruebas y calidad. |
| Responsable de documentación y defensa | Mantiene portfolio, registro de IA y prepara demos. |

En equipos de 3, una persona puede asumir dos responsabilidades.

### 2.5. Primera semana

La primera semana se dedicará a enseñar Scrum y preparar la dinámica de trabajo del curso.

Actividad principal confirmada:

- Construcción de una torre de papel.

Objetivo de la semana:

- Vivir un sprint corto.
- Entender backlog, tareas, roles, daily, revisión y retrospectiva.
- Traducir la experiencia a la organización del proyecto del agente IA.

---

## 3. Fuentes documentales ya revisadas

### 3.0. Propuesta de objetivos de Programación del IES

Documento principal para objetivos de Programación:

```text
documentacion/Propuesta Ciclos Superiores IESHLanz 2026-27.pdf
```

Este documento se considera la referencia prioritaria para orientar los objetivos de Programación.

Objetivo final del ciclo según la propuesta:

> Resolver problemas como AI-Enhanced Developers.

El alumnado debe avanzar hacia saber:

1. Qué construir: arquitectura, modelo de datos, stack y comprensión del problema.
2. Cómo construirlo rápido: prompting, agentes y automatización.
3. Cómo asegurar que funciona y escalarlo: CI/CD, Docker, Git y pruebas.

Objetivos específicos para Programación:

- Fundamentos y algoritmia.
- Paradigmas y arquitectura: POO, MVC e introducción práctica a arquitectura hexagonal.
- Buenas prácticas y código limpio.
- Flujo Git profesional: ramas, fusionado, resolución de conflictos, PRs y revisiones de código.
- Estrategia de pruebas: unitarias e integración, ajustadas al nivel.
- Desarrollo potenciado por IA: control del bucle del agente, lectura de stack traces, comprensión y validación de código generado.

Implicación para este diseño:

- Los temas del curso 2025/2026 se mantienen como referencia de contenidos.
- La propuesta IESHLanz 2026/2027 orienta el perfil profesional y la integración de esas prácticas en Programación.

### 3.1. Perfil de salida y diseño inverso

Documento:

```text
perfil-salida-diseno-inverso-dam-daw.md
```

Ideas clave aplicables:

- El diseño debe partir del perfil de salida.
- Las evidencias deben definirse antes que las actividades.
- El currículo puede organizarse mediante macrocompetencias.
- La IA responsable y los sistemas agénticos aparecen como competencia estratégica.

Competencia especialmente relevante:

> Usar IA y agentes como apoyo profesional, con trazabilidad, validación humana, control de datos y defensa de decisiones.

Macrocompetencias más conectadas con el proyecto:

| Macrocompetencia | Aplicación al proyecto agente IA |
|---|---|
| MC1. Análisis y especificación | Definir necesidades, historias de usuario, requisitos y criterios de aceptación. |
| MC2. Desarrollo de producto software | Construir el agente de forma incremental. |
| MC3. Calidad, pruebas y auditoría | Probar, depurar, revisar y defender código propio o asistido por IA. |
| MC5. Despliegue y operación básica | Git, GitHub, documentación, Docker y ejecución reproducible. |
| MC6. IA responsable y sistemas agénticos | Uso trazable, ético y defendible de Gemini/Jarvis/IA. |
| MC7. Colaboración profesional | Scrum, roles, demos, retrospectivas y defensa oral. |

### 3.2. Modelo HEXA

Documento:

```text
integracion_modelo_hexa_y_secuenciacion_didactica.md
```

Fases del modelo:

| Fase | Sentido didáctico en el curso |
|---|---|
| Fase 0. Equipos | Crear equipos, roles, normas, seguridad psicológica y acuerdos de trabajo. |
| 1. Activar | Presentar el reto, conectar con problemas reales y activar conocimientos previos. |
| 2. Investigar | Aprender lo necesario mediante mini-retos, talleres, ejemplos y exploración. |
| 3. Idear | Proponer soluciones, comparar alternativas y justificar decisiones. |
| 4. Planificar | Convertir la solución en backlog, tareas, criterios de aceptación y sprint plan. |
| 5. Ejecutar | Construir, probar, depurar, iterar y documentar. |
| 6. Comunicar | Demo, defensa, reflexión, coevaluación y portfolio. |

---

## 4. Resultados de Aprendizaje base

### 4.1. Programación

Fuente:

```text
Programacion Didactica Programacion1ºGS DAW.pdf
```

| RA | Descripción | Peso en programación anterior |
|---|---|---:|
| RA1 | Reconoce la estructura de un programa informático, identificando y relacionando los elementos propios del lenguaje de programación utilizado. | 5% |
| RA2 | Escribe y prueba programas sencillos, reconociendo y aplicando los fundamentos de la programación orientada a objetos. | 15% |
| RA3 | Escribe y depura código, analizando y utilizando las estructuras de control del lenguaje. | 15% |
| RA4 | Desarrolla programas organizados en clases analizando y aplicando los principios de la programación orientada a objetos. | 15% |
| RA5 | Realiza operaciones de entrada y salida de información, utilizando procedimientos específicos del lenguaje y librerías de clases. | 15% |
| RA6 | Escribe programas que manipulen información seleccionando y utilizando tipos avanzados de datos. | 15% |
| RA7 | Desarrolla programas aplicando características avanzadas de los lenguajes orientados a objetos y del entorno de programación. | 10% |
| RA8 | Utiliza bases de datos orientadas a objetos, analizando sus características y aplicando técnicas para mantener la persistencia de la información. | 5% |
| RA9 | Gestiona información almacenada en bases de datos manteniendo la integridad y consistencia de los datos. | 5% |

Nota importante sobre la nueva programación:

La programación del curso 2026/2027 modificará el criterio de superación respecto a la programación anterior:

> Para superar el módulo será imprescindible superar cada Resultado de Aprendizaje imprescindible con calificación mayor o igual a 5.

Clasificación inicial de RA:

| Tipo | RA | Implicación |
|---|---|---|
| Imprescindibles | RA1, RA2, RA3, RA4, RA5, RA6 | Deben superarse con calificación mayor o igual a 5 para superar el módulo. |
| No imprescindibles, pero evaluables | RA7, RA8, RA9 | Deben tenerse en cuenta, pero su profundidad y alcance dependerán del avance real del grupo. |

Criterio didáctico:

- RA7, RA8 y RA9 se integrarán preferentemente como ampliación, consolidación o itinerario avanzado del proyecto del agente IA.
- Si el ritmo del grupo lo permite, se trabajarán mediante herramientas extensibles, persistencia y gestión de datos.
- Si el ritmo del grupo no lo permite, se recogerán evidencias mínimas o parciales sin comprometer la superación del módulo cuando los RA imprescindibles estén superados.

### 4.2. Prácticas técnicas instrumentales

MiniJarvis incorpora, dentro de Programación, las prácticas necesarias para desarrollar el producto con calidad y trazabilidad:

- IntelliJ para Java.
- Git/GitHub.
- Depuración.
- Testing.
- Refactorización.
- UML.
- Documentación.
- Repositorios remotos.
- Integración continua si el ritmo lo permite.
- Docker en uso guiado y, si procede, creación de contenedores.

Estas prácticas apoyan las tareas y evidencias de Programación. No tienen RA, CE, horas, calificación ni entregables propios.

---

## 5. Calendario base confirmado

Fuente:

```text
Resolución 27 mayo 2026 calendario escolar curso 2026-2027 Granada - con anexos.pdf
```

Fechas relevantes:

| Hito calendario | Fecha o periodo |
|---|---|
| Inicio régimen ordinario FP | 15 septiembre 2026 |
| Navidad | 23 diciembre 2026 - 6 enero 2027, ambos inclusive |
| Día Comunidad Educativa | 26 febrero 2027 |
| Día de Andalucía trasladado | 1 marzo 2027 |
| Semana Santa | 22 - 28 marzo 2027, ambos inclusive |
| Día del Trabajo | 1 mayo 2027 |
| Fiesta local de Granada | 3 mayo 2027 |
| Fiesta local de Granada | 27 mayo 2027 |
| Día no lectivo provincial | 28 mayo 2027 |
| Fin general de enseñanzas | 22 junio 2027 |

Fechas de evaluación dadas por el docente:

| Evaluación | Periodo aproximado de trabajo |
|---|---|
| 1.ª evaluación | 15 septiembre - 23 diciembre |
| 2.ª evaluación | 7 enero - 31 marzo |
| 3.ª evaluación | 1 abril - 23 junio |

Decisión sobre FFEOE:

- La FFEOE afecta a todo el alumnado.
- No asisten a clase durante la FFEOE.
- Son 18 jornadas lectivas seguidas, excluyendo fines de semana y festivos/no lectivos.
- No deben entregar tareas durante la FFEOE.
- El 27 de mayo de 2027 es fiesta local de Granada.
- El 28 de mayo de 2027 es día no lectivo provincial.
- Por tanto, la última jornada real debe ser el miércoles 26 de mayo.

Propuesta de periodo FFEOE:

```text
Inicio: viernes 30 de abril de 2027
Fin real de jornadas: miércoles 26 de mayo de 2027
Día 27 de mayo: fiesta local de Granada
Día 28 de mayo: no lectivo provincial
```

Fechas FFEOE lectivas contadas:

```text
2027-04-30,
2027-05-04, 2027-05-05, 2027-05-06, 2027-05-07,
2027-05-10, 2027-05-11, 2027-05-12, 2027-05-13, 2027-05-14,
2027-05-17, 2027-05-18, 2027-05-19, 2027-05-20, 2027-05-21,
2027-05-24, 2027-05-25, 2027-05-26
```

Carga semanal confirmada de Programación:

| Día | Periodos de 45 minutos |
|---|---:|
| Martes | 3 |
| Jueves | 2 |
| Viernes | 3 |
| **Total semanal** | **8** |

El cómputo detallado por hitos y evaluaciones se mantiene en `02-calendario-hitos-sprints-2026-2027.md`.

Pendiente:

- Confirmar si existen días no lectivos adicionales de centro/municipio.


---

## 6. Enfoque global del curso

### 6.1. Idea conductora

El curso se organiza como una evolución profesional del alumnado desde cero hasta la construcción y defensa de un agente IA propio.

Narrativa:

> Somos un pequeño equipo de desarrollo que debe construir, justificar, probar y defender un asistente inteligente propio, aprendiendo programación, herramientas profesionales, colaboración ágil y uso responsable de IA durante el proceso.

### 6.2. Principio de progresión

El agente no empieza usando IA real.

Progresión recomendada:

1. Programas básicos y toma de decisiones.
2. Objetos predefinidos y uso de librerías.
3. Estructuras de control y depuración.
4. Colecciones y estructuras de datos para memoria/contexto.
5. Clases propias para modelar agente, mensajes, comandos y memoria.
6. Herencia/interfaces/composición para herramientas del agente.
7. Entrada/salida, ficheros y persistencia simple.
8. Pruebas, depuración y refactorización sistemática.
9. Base de conocimiento y persistencia.
10. Integración opcional con Gemini/Jarvis.
11. Documentación, defensa y comparación Java ↔ Python fuera del horario lectivo.

---

## 7. Propuesta inicial de 7 hitos + presentación final

Esta propuesta debe revisarse después con la matriz RA/CE detallada.

| Hito | Periodo orientativo | Producto del alumnado | RA de Programación y prácticas integradas |
|---|---|---|---|
| 0. Bootcamp Scrum, diagnóstico y acuerdos | Semana 1 | Presentación, autoevaluación privada, microprueba, equipos provisionales 3–4, torre, tablero, review, retrospectiva y contrato | Diagnóstico no calificable; Scrum, tablero y revisión de equipos. |
| 1. Primer asistente por consola | Sept-oct | Programa Java que recibe una entrada simple y responde | RA1 y RA2 inicial; IDE, ciclo fuente-ejecutable, IntelliJ y Git. |
| 2. Agente con decisiones y depuración | Oct-nov | Agente con comandos, menús, control de flujo y manejo básico de errores | RA3; pruebas, breakpoints e incidencia documentada. |
| 3. Agente con memoria en colecciones | Nov-dic | Memoria temporal usando arrays/listas/mapas y búsqueda simple | RA6 inicial; casos límite y pruebas de comportamiento. |
| 4. Agente orientado a objetos | Ene-feb | Modelo de clases: Agent, Message, Memory, Tool, Command | RA4; diagramas vinculados al código. |
| 5. Agente extensible con herramientas | Feb-mar | Herramientas internas mediante interfaces, composición/herencia y plugins simples | RA7; refactorización, GitHub y revisión de código. |
| 6. Agente persistente y trazable | Abr-inicio mayo | Ficheros/base de conocimiento, logs, registro de IA, posible Docker guiado | RA5 y RA8/RA9 según alcance; ejecución reproducible y pruebas de persistencia. |
| 7. Integración IA responsable | Antes FFEOE, si el ritmo lo permite | Integración opcional con Gemini/Jarvis o simulación robusta de LLM | Consolidación de RA; validación, seguridad, documentación y pruebas. |
| Presentación final | Después FFEOE | Demo, defensa oral, portfolio final, recuperación/mejora | Recuperación o mejora de RA de Programación. |

Notas:

- Los hitos 1 a 6 deben ser viables sin depender de una API externa de IA.
- El hito 7 puede tener dos rutas: integración real con Gemini/Jarvis o simulación defendible.
- En cada hito significativo se hará transferencia parcial a Python y JavaScript, con ayuda amplia de IA, pero con defensa obligatoria.

---

## 8. Uso ético y adecuado de IA

Se desarrollarán tres documentos derivados:

1. Semáforo de uso de IA.
2. Registro obligatorio de uso de IA por entrega.
3. Protocolo de defensa oral sobre código asistido por IA.

### 8.1. Definición inicial de uso adecuado

Uso adecuado de IA significa:

- usarla para comprender, contrastar, practicar, revisar y mejorar;
- declarar cuándo y cómo se ha usado;
- no introducir datos personales, credenciales ni información sensible;
- verificar el resultado antes de incorporarlo;
- poder explicar, modificar y defender cualquier parte entregada;
- distinguir entre ayuda al aprendizaje y sustitución del aprendizaje.

### 8.2. Semáforo inicial

| Nivel | Uso | Ejemplos |
|---|---|---|
| Verde | Permitido y recomendado | Pedir explicaciones, ejemplos alternativos, ayuda para depurar, preguntas de comprensión, mejora de documentación, generación de casos de prueba que luego se revisan. |
| Amarillo | Permitido con trazabilidad y defensa | Generar fragmentos de código, adaptar soluciones, traducir un hito a Python/JavaScript, proponer refactorizaciones, crear tests. Debe registrarse y defenderse. |
| Rojo | No permitido | Copiar soluciones completas sin entenderlas, ocultar uso de IA, usar IA en pruebas individuales si no está autorizado, introducir claves/datos personales, entregar código que no se puede explicar. |

### 8.3. Registro de uso de IA

Cada entrega importante incluirá:

- Herramienta usada: Gemini, Jarvis u otra autorizada.
- Fecha.
- Objetivo de uso.
- Prompt o resumen del prompt.
- Resultado aceptado.
- Cambios realizados por el alumno/equipo.
- Verificación aplicada.
- Qué se ha aprendido.
- Riesgos o errores detectados.

### 8.4. Defensa oral

La defensa podrá incluir:

- Explicar una función o clase concreta.
- Modificar código en directo o pseudodirecto.
- Detectar un bug introducido por el profesor.
- Justificar una decisión de diseño.
- Comparar la versión Java con Python/JavaScript.
- Identificar qué parte fue asistida por IA y cómo se validó.

---

## 9. DUA aplicado al curso

Dado que el grupo será heterogéneo, con alumnado de Bachillerato y Grado Medio y poco conocimiento inicial de programación, se aplicará DUA desde el diseño.

### 9.1. Múltiples formas de representación

- Explicaciones breves.
- Ejemplos de código guiados.
- Diagramas UML.
- Pseudocódigo.
- Demos en directo.
- Plantillas iniciales.
- Vídeos o capturas cuando proceda.
- Documentación paso a paso en Moodle.

### 9.2. Múltiples formas de acción y expresión

- Código individual.
- Código en equipo.
- Demos orales.
- Portfolios.
- Diagramas.
- Tests.
- Issues y commits.
- Reflexiones breves.
- Defensa técnica.

### 9.3. Múltiples formas de implicación

- Retos progresivos.
- Elección parcial de herramientas o temática del agente.
- Roles rotatorios.
- Hitos cortos.
- Feedback frecuente.
- Reconocimiento de mejoras, no solo de producto final.
- Itinerario mínimo, recomendado y avanzado.

---

## 10. Evaluación: enfoque inicial

El proyecto guiará la evaluación completa, aunque podrán existir pruebas individuales puntuales.

Principios:

- Cada RA debe tener evidencias suficientes.
- Cada RA debe poder superarse individualmente, aunque haya trabajo en equipo.
- El producto final no puede ocultar falta de comprensión individual.
- Las defensas orales y entrevistas técnicas son parte central de la evaluación.
- La IA se permite, pero aumenta la exigencia de explicación, trazabilidad y validación.

Instrumentos previstos:

| Instrumento | Función |
|---|---|
| Producto de hito | Evidencia técnica principal. |
| Portfolio individual | Evolución, reflexión, decisiones, registro de IA. |
| Repositorio GitHub | Historial, colaboración, issues, commits. |
| Defensa oral | Comprensión individual y autoría. |
| Prueba individual puntual | Verificar fundamentos cuando sea necesario. |
| Rúbrica | Transparencia de criterios. |
| Lista de cotejo | Control de mínimos por hito. |
| Observación sistemática | Trabajo diario, colaboración y autonomía. |
| Retrospectiva Scrum | Mejora continua y funcionamiento del equipo. |

---

## 11. Primera semana: curso, Scrum, diagnóstico y torre de papel

La torre no abre la semana sin preparación. Antes se presenta el curso, se explica Scrum y se recogen evidencias para formar equipos provisionales.

| Momento | Tiempo orientativo | Actividad | Evidencia |
|---|---:|---|---|
| H — Curso y reto | 35 min | MiniJarvis, hitos, HEXA, evidencias y criterios de H0. | Reformulación y preguntas. |
| Seguridad | 15 min | IA responsable, autoría y defensa. | Semáforo/ticket. |
| E/X — Scrum mínimo | 20 min | Sprint, backlog, bloqueo, prueba, review y retrospectiva. | Glosario y microcasos. |
| E — HADA individual | 25 min | Repartir 4–3–2–1 por fila; sumar Gestor, Colaborador, Desarrollador y Analista. | Cuatro valores, diagrama y reflexión privada. |
| Preparación docente | Entre sesiones | Combinar HADA, accesibilidad, asistencia y criterio profesional. | Propuesta privada de equipos. |
| Equipos provisionales | 45 min | Analizar composición, compensar ausencias y acordar funciones, participación y backlog. | Mapa sin puntuaciones, funciones justificadas y definición de terminado. |
| A — Torre | 90 min | Dos ciclos de backlog, construcción, prueba, review, retrospectiva y adaptación. | Torre, tablero, dos pruebas y revisión HADA-conducta. |
| Transferencia | 45 min | Decisión de equipo, contrato observable, rotación y backlog de MiniJarvis. | Acuerdos, criterios y mejora. |

Regla: los equipos no se forman únicamente por amistad ni por una puntuación. Se priorizan cuatro personas y se introducen equipos de tres según el resto al dividir la asistencia entre cuatro. Son provisionales hasta la retrospectiva. El diagnóstico no tiene nota, no publica puntuaciones y no fija roles.

Resultado esperado:

- El alumnado comprende el contenido y la forma de trabajo del curso.
- Puede explicar el ciclo Scrum mínimo.
- Reconoce aportaciones y habilidades que quiere desarrollar.
- El profesorado dispone de equipos equilibrados de tres o cuatro.
- La torre valida producto, proceso, roles y composición.
- Cada equipo inicia contrato, tablero y transferencia a MiniJarvis.

## 12. Riesgos detectados

| Riesgo | Mitigación inicial |
|---|---|
| Grupo heterogéneo y con poco nivel inicial | DUA, andamiaje, tareas mínimas/recomendadas/avanzadas. |
| Uso de IA como sustituto del aprendizaje | Semáforo, registro, defensas orales, preguntas individuales. |
| Dependencia de servicios externos de IA | El agente debe funcionar sin IA real hasta hito avanzado. |
| Descoordinación entre documentos | Mapa maestro común, matriz RA/CE/evidencias/tareas y revisiones de coherencia. |
| Exceso de ambición del agente | Mínimo viable por consola; interfaz como ampliación. |
| FFEOE corta la tercera evaluación | Cerrar el producto base antes del 4 de mayo; dejar presentación/recuperación después. |
| Alumnado en Windows si se quiere Linux | Transición guiada, Docker, documentación dual, Linux recomendado pero no bloqueo inicial. |
| Evaluación de trabajo en equipo injusta | Evidencias individuales, defensa oral, commits, portfolio y entrevistas. |

---

## 13. Decisiones tomadas y pendientes

### 13.1. Decisiones tomadas

1. Criterio de superación de Programación:
   - RA1, RA2, RA3, RA4, RA5 y RA6 son imprescindibles.
   - RA7, RA8 y RA9 no son imprescindibles, aunque deben tenerse en cuenta según avance del grupo.
2. El proyecto se desarrolla íntegramente dentro de Programación.
3. En este proceso de diseño, Hermes asumirá el papel de docente responsable del proyecto para proponer secuencias, evidencias y rúbricas coordinadas.
4. El alumnado usará IntelliJ IDEA como IDE principal para Java.
5. Gemini y Jarvis se usarán con cuentas nominales: cada alumno tendrá usuario propio.
6. El portfolio se diseñará preferentemente en Markdown sobre GitHub.
7. Si el alumnado tiene problemas con GitHub, se usará un formato mixto o alternativa documentada.
8. La matriz RA/CE → evidencias → tareas será diseñada por Hermes y validada posteriormente por el docente.
9. Las rúbricas serán definidas por Hermes a partir de los criterios de evaluación.
10. La primera semana Scrum será diseñada por Hermes con sesiones y tiempos.

### 13.2. Decisiones cerradas tras revisión

1. Distribución de Programación:
   - 3 periodos lectivos el martes, 2 el jueves y 3 el viernes.
   - Cada semana combina explicación, práctica guiada, taller, revisión, documentación y defensa dentro del mismo módulo.
2. Todas las clases se imparten por la tarde.
3. Cada periodo lectivo tiene una duración de 45 minutos.
4. No se contemplan más días festivos/no lectivos que los ya indicados en este mapa.

## 14. Próximos artefactos derivados

Orden recomendado:

1. Matriz RA/CE → evidencias → tareas.
2. Calendario de hitos y sprints 2026/2027.
3. Diseño detallado de la primera semana Scrum.
4. Política de uso ético de IA: semáforo, registro y defensa.
5. Backlog anual del proyecto agente IA.
6. Rúbricas de hitos.
7. Anexo curricular de Programación.

---

## 15. Veredicto del mapa actual

Estado: documento de referencia curricular.

Este mapa ya permite avanzar hacia la programación del proyecto, pero aún no debe considerarse documento final porque faltan:

- matriz completa RA/CE/evidencias;
- rúbricas;
- secuencia detallada por sesiones.

# 16. Ajuste aplicado a los hitos MiniJarvis

Este documento ya no queda solo como análisis: se ha usado para modificar los hitos, guías docentes autónomas, paquetes de hito, libro del alumnado, índice global y respuestas modelo de Laura.

Criterio aplicado:

```text
Todo concepto de Programación recopilado aquí debe aparecer al final del itinerario como núcleo, ampliación, recuperación o mejora defendible.
```

Distribución final:

| Bloque | Función curricular |
|---|---|
| H1-H2 | Fundamentos, variables, tipos, entrada/salida, condiciones, bucles, switch, depuración y eficiencia básica. |
| H3 | Colecciones, listas, recorridos, mutabilidad, arrays, Set y Map como ampliaciones. |
| H4 | Clases, objetos, métodos, constructores, referencias, diagramas y responsabilidades. |
| H5 | Tests, TDD, interfaces, polimorfismo, clean code y Command simplificado. |
| H6 | Excepciones, invariantes, persistencia, logs y repositorio como idea inicial. |
| H7 | Records/enums, abstracción, Strategy opcional, Optional, streams, funciones puras e IA responsable. |
| HF | Cierre y mejora: JavaFX, eventos, MVC, arquitectura hexagonal, repositorios, CRUD, transacciones y defensa global. |

Respuesta de Laura esperada al final:

> Puedo explicar dónde aparece cada concepto importante en mi proyecto MiniJarvis o, si es una ampliación, dónde lo he estudiado y cómo lo aplicaría de forma segura sin romper el diseño.

