# Matriz integrada RA/CE → evidencias → tareas

## Programación + Entornos de Desarrollo — 1.º DAW — Curso 2026/2027

Versión: borrador 0.1
Fecha: 2026-07-04
Documento base: `00-mapa-maestro-curso-2026-2027.md`

---

## 1. Propósito

Esta matriz conecta el proyecto guía del curso, la construcción progresiva de un pequeño agente IA propio, con los Resultados de Aprendizaje y Criterios de Evaluación de los módulos de Programación y Entornos de Desarrollo.

Se plantea como matriz integrada para coordinar ambos módulos, con anexos separados para facilitar la posterior redacción normativa de cada programación didáctica.

Documentos anexos:

- `01A-anexo-programacion-ra-ce.md`
- `01B-anexo-entornos-ra-ce.md`

---

## 2. Criterios de diseño

1. El proyecto guía articula la evaluación, pero no elimina la necesidad de evidencias individuales.
2. Programación aporta el núcleo de construcción del agente.
3. Entornos aporta la profesionalización del proceso: IDE, GitHub, pruebas, depuración, refactorización, UML, documentación y CI/Docker si procede.
4. Los RA imprescindibles de Programación son RA1, RA2, RA3, RA4, RA5 y RA6.
5. Los RA7, RA8 y RA9 de Programación son no imprescindibles, pero evaluables según avance del grupo.
6. En Entornos se intentan cubrir todos los RA de forma distribuida, porque el módulo tiene una carga menor pero muy conectada con el proyecto.
7. La IA puede usarse, pero toda evidencia asistida por IA exige registro, comprensión y defensa.
8. Cada hito debe producir evidencias técnicas, de proceso y de reflexión.

---

## 3. Hitos integrados

| Hito | Periodo orientativo | Producto guía | Scrum/HEXA | Resultado esperado |
|---|---|---|---|---|
| H0 | Semana 1 | Torre de papel + tablero inicial | Fase 0 completa + sprint simulado | Comprender Scrum y crear normas de equipo. |
| H1 | Sept-oct | Primer asistente por consola | Activar + Investigar + Ejecutar | Programa Java básico con entrada, salida y reglas simples. |
| H2 | Oct-nov | Agente con decisiones y depuración | Ejecutar + Comunicar | Comandos, menús, estructuras de control, pruebas manuales y depuración. |
| H3 | Nov-dic | Agente con memoria en colecciones | Ejecutar + Comunicar | Memoria temporal con arrays/listas/mapas y búsquedas. |
| H4 | Ene-feb | Agente orientado a objetos | Idear + Planificar + Ejecutar | Modelo de clases: Agent, Message, Memory, Tool, Command. |
| H5 | Feb-mar | Agente extensible con herramientas | Planificar + Ejecutar | Interfaces, composición/herencia, refactorización y GitHub colaborativo. |
| H6 | Abr-inicio mayo | Agente persistente y trazable | Ejecutar + Comunicar | Ficheros, logs, base de conocimiento, registro de IA, Docker guiado. |
| H7 | Antes de FFEOE si procede | Integración IA responsable | Ejecutar + Comunicar | Conexión opcional con Gemini/Jarvis o simulación robusta. |
| HF | Después FFEOE | Presentación/recuperación | Comunicar | Defensa, portfolio final, recuperación o mejora. |

---

## 4. Matriz integrada por hitos

### H0. Bootcamp Scrum y acuerdos de trabajo

| Elemento | Detalle |
|---|---|
| Producto | Torre de papel, tablero Scrum inicial, roles adaptados, contrato de equipo. |
| Programación | No evalúa aún RA técnicos de forma fuerte; sirve como activación y diagnóstico. |
| Entornos | ED RA1.g: metodologías ágiles y fases de desarrollo. |
| Evidencias | Foto/medición de torre, tablero, backlog, reflexión de retrospectiva, contrato de equipo. |
| Tareas | Crear equipo; definir roles; construir backlog; ejecutar sprint corto; hacer review; hacer retrospectiva; trasladar aprendizajes al proyecto del agente. |
| Defensa | Explicar qué es un sprint, qué salió mal, qué cambiarían y cómo se aplicará al agente IA. |
| IA | Sin IA o solo para contraste posterior sobre Scrum, registrada si se usa. |

### H1. Primer asistente por consola

| Elemento | Detalle |
|---|---|
| Producto | Programa Java de consola que recibe una entrada simple y responde mediante reglas básicas. |
| Programación | PR RA1; PR RA2 inicial. |
| Entornos | ED RA1; ED RA2: IntelliJ, proyecto, fuente, ejecutable, configuración básica. |
| Evidencias | Repositorio inicial, código Java, capturas de ejecución, README básico, primer portfolio individual. |
| Tareas | Crear proyecto en IntelliJ; escribir programa básico; usar variables, constantes, operadores; leer entrada; generar respuesta; comentar código; subir a GitHub. |
| CE dominantes | PR RA1 a,b,c,d,e,f,g,h,i; PR RA2 b,i; ED RA1 a,b,c,e,f; ED RA2 a,g. |
| Defensa | Explicar estructura del programa, variables usadas, flujo de ejecución y cómo se ejecuta desde IntelliJ. |
| IA | Verde: pedir explicación de sintaxis. Amarillo: pedir ejemplos, registrarlos y adaptarlos. Rojo: entregar programa completo sin entender. |

### H2. Agente con decisiones y depuración

| Elemento | Detalle |
|---|---|
| Producto | Agente con menú, comandos, estructuras condicionales/repetitivas, control básico de errores y depuración. |
| Programación | PR RA3 imprescindible. Refuerzo de PR RA1/RA2. |
| Entornos | ED RA3: pruebas, depuración, puntos de ruptura e incidencias. |
| Evidencias | Código con estructuras de control; checklist de pruebas manuales; capturas de depuración; informe breve de incidencias. |
| Tareas | Diseñar comandos; implementar menú; usar if/switch/bucles; manejar errores; crear casos de prueba; depurar en IntelliJ; documentar incidencias. |
| CE dominantes | PR RA3 a,b,c,d,e,f,g,h,i; ED RA3 a,b,c,d,e,h. |
| Defensa | Modificar un comando en directo, explicar un breakpoint y justificar cómo se detectó un fallo. |
| IA | Permitida para sugerir casos de prueba o localizar errores, con registro y verificación. |

### H3. Agente con memoria en colecciones

| Elemento | Detalle |
|---|---|
| Producto | Agente con memoria temporal: historial de mensajes, preferencias simples, búsqueda de entradas y listado de interacciones. |
| Programación | PR RA6 imprescindible. Refuerzo de PR RA3. |
| Entornos | ED RA3: pruebas unitarias básicas si el nivel lo permite. |
| Evidencias | Uso de arrays/listas/mapas; pruebas de memoria; README con ejemplos; portfolio de decisiones. |
| Tareas | Modelar historial; elegir colección; añadir mensajes; listar memoria; buscar por patrón simple; probar casos límite; comparar implementación Java con Python/JS en mini-transferencia. |
| CE dominantes | PR RA6 a,b,c,d,e,g,j; ED RA3 f,g,h si se introducen pruebas unitarias. |
| Defensa | Explicar por qué se eligió una colección, cómo se recorre y cómo se prueba. |
| IA | Uso amarillo permitido para transferir el mismo comportamiento a Python/JavaScript, con defensa obligatoria. |

### H4. Agente orientado a objetos

| Elemento | Detalle |
|---|---|
| Producto | Diseño OO del agente: Agent, Message, Memory, Command, Tool, Conversation. |
| Programación | PR RA4 imprescindible. Refuerzo de PR RA2. |
| Entornos | ED RA5 y ED RA6: diagramas de clases, casos de uso, actividades/secuencia. |
| Evidencias | Código organizado en clases; diagrama de clases; diagrama de comportamiento sencillo; commits por funcionalidades. |
| Tareas | Identificar clases; definir responsabilidades; implementar constructores, atributos y métodos; aplicar visibilidad; crear objetos; generar/interpretar UML; defender diseño. |
| CE dominantes | PR RA4 a,b,c,d,e,f,h,i; ED RA5 a,b,c,d,f; ED RA6 a,b,c,d,e,f. |
| Defensa | Explicar responsabilidades de cada clase, relaciones y decisiones de diseño. |
| IA | Puede ayudar a revisar el diseño, pero el alumnado debe justificarlo y corregirlo. |

### H5. Agente extensible con herramientas

| Elemento | Detalle |
|---|---|
| Producto | Agente con herramientas internas: calculadora, buscador en memoria, ayuda, resumen, validador u otras. |
| Programación | PR RA7 no imprescindible, con alcance adaptable. Refuerzo de PR RA4 y RA6. |
| Entornos | ED RA4: refactorización, control de versiones, repositorios remotos, documentación, integración continua si procede. |
| Evidencias | Interfaces o clases abstractas; composición/herencia; pull requests o ramas; revisión de código; refactorización documentada. |
| Tareas | Definir interfaz Tool; implementar varias herramientas; refactorizar código repetido; usar ramas; revisar código; documentar clases; crear checklist de calidad. |
| CE dominantes | PR RA7 a,c,d,e,f,g,h,i,j; ED RA4 a,b,c,d,e,f,g,h,i. |
| Defensa | Justificar herencia frente a composición, explicar un refactor y revisar un commit. |
| IA | Permitida para proponer refactorizaciones, siempre con comparación antes/después y defensa. |

### H6. Agente persistente y trazable

| Elemento | Detalle |
|---|---|
| Producto | Agente que guarda/recupera información en ficheros, mantiene logs y consulta una pequeña base de conocimiento. Docker guiado si procede. |
| Programación | PR RA5 imprescindible. PR RA8/RA9 no imprescindibles si se introduce persistencia avanzada o BD. |
| Entornos | ED RA4: repositorio, documentación, CI/Docker guiado. ED RA3: pruebas de persistencia. |
| Evidencias | Lectura/escritura de ficheros; logs; base de conocimiento; prueba de recuperación; documentación de ejecución; registro IA. |
| Tareas | Guardar historial; cargar memoria; gestionar errores de fichero; crear formato de intercambio simple; preparar ejecución reproducible; usar contenedor preparado. |
| CE dominantes | PR RA5 a,b,c,d,e; PR RA8/RA9 si hay BD; ED RA3/RA4 según pruebas y herramientas. |
| Defensa | Explicar persistencia, formato de datos, errores posibles y cómo reproducir la ejecución. |
| IA | Se exige registro completo si se usa IA para diseñar formato, persistencia o Docker. |

### H7. Integración IA responsable

| Elemento | Detalle |
|---|---|
| Producto | Integración opcional con Gemini/Jarvis o simulación robusta de LLM si el grupo no está preparado para API real. |
| Programación | Consolidación de RA imprescindibles; RA7/RA8/RA9 según alcance. |
| Entornos | Seguridad, documentación, pruebas, configuración, trazabilidad. |
| Evidencias | Registro de prompts, validación humana, control de datos, pruebas de respuesta, limitaciones documentadas. |
| Tareas | Definir casos de uso; preparar prompts; evitar datos personales; gestionar respuestas; validar; registrar; comparar modo simulado vs modo real. |
| CE dominantes | Dependerá del alcance. Debe usarse como integración y no como sustituto de fundamentos. |
| Defensa | Explicar qué hace la IA, qué no hace, qué datos recibe, cómo se validó y qué errores puede cometer. |
| IA | Uso explícito, trazado, defendido y limitado. |

### HF. Presentación final, recuperación y mejora

| Elemento | Detalle |
|---|---|
| Producto | Demo final, portfolio, defensa individual, recuperación de RA pendientes y mejora opcional. |
| Programación | Recuperación o mejora de RA imprescindibles; ampliación de no imprescindibles si procede. |
| Entornos | Portfolio, documentación final, revisión de repositorio, defensa de proceso. |
| Evidencias | Demo, defensa, portfolio, repositorio, rúbricas, entrevista individual, recuperación específica. |
| Tareas | Preparar demo; cerrar README; revisar registro IA; completar portfolio; responder preguntas; recuperar evidencias pendientes. |
| Defensa | Individual y obligatoria, especialmente si hay uso intensivo de IA o desequilibrio de contribución en equipo. |
| IA | Permitida para preparar explicación, no para sustituir la defensa. |

---

## 5. Evidencias transversales por entrega

Cada hito, salvo H0 si se decide simplificar, debería producir:

| Evidencia | Individual/equipo | Uso |
|---|---|---|
| Código funcional | Equipo con trazabilidad individual | Producto técnico. |
| Commits GitHub | Individual/equipo | Autoría, progreso, colaboración. |
| README o documentación técnica | Equipo | Instalación, uso y decisiones. |
| Portfolio individual | Individual | Reflexión, aprendizaje y comprensión. |
| Registro de uso de IA | Individual/equipo según uso | Trazabilidad y ética. |
| Pruebas/checklist | Equipo | Calidad y validación. |
| Demo/review | Equipo | Comunicación técnica. |
| Defensa oral | Individual | Comprensión real y autoría. |
| Retrospectiva | Equipo + individual | Mejora continua. |

---

## 6. Transferencia a Python y JavaScript

La transferencia a otros lenguajes se aplicará al cerrar hitos relevantes.

Criterio:

- El alumnado podrá usar IA de forma amplia para generar la versión Python/JavaScript.
- La entrega no se valorará por memorizar sintaxis, sino por comprensión, comparación y defensa.
- Se harán preguntas para verificar que entienden lo generado.

Hitos recomendados para transferencia:

| Hito | Transferencia sugerida |
|---|---|
| H1 | Entrada/salida y reglas simples en Python/JavaScript. |
| H2 | Menús, condicionales y bucles. |
| H3 | Listas/diccionarios/arrays y memoria temporal. |
| H4 | Clases básicas y objetos. |
| H5 | Interfaces o equivalentes: duck typing, clases, módulos. |
| H6 | Lectura/escritura de ficheros o JSON. |

Preguntas de defensa:

- ¿Qué cambia entre Java y Python/JavaScript?
- ¿Dónde está el equivalente de una clase, método o colección?
- ¿Qué parte generó la IA?
- ¿Qué has modificado tú?
- ¿Cómo sabes que funciona?
- ¿Qué error tuviste que corregir?

---

## 7. Relación inicial entre hitos y RA

### 7.1. Programación

| RA Programación | Tipo | Hitos principales | Evidencias clave |
|---|---|---|---|
| RA1 | Imprescindible | H1 | Proyecto Java, estructura, variables, operadores, comentarios. |
| RA2 | Imprescindible | H1-H2 | Programas simples, objetos predefinidos, métodos, constructores/librerías básicas. |
| RA3 | Imprescindible | H2 | Control de flujo, excepciones, depuración, aserciones, documentación. |
| RA4 | Imprescindible | H4 | Clases propias, métodos, visibilidad, constructores, objetos. |
| RA5 | Imprescindible | H6 | Entrada/salida, ficheros, posible interfaz simple si procede. |
| RA6 | Imprescindible | H3 | Arrays, listas, mapas, iteradores, búsquedas, JSON si procede. |
| RA7 | No imprescindible | H5-H7 | Herencia, interfaces, composición, jerarquías, extensibilidad. |
| RA8 | No imprescindible | H6-H7 | Persistencia orientada a objetos si el nivel lo permite. |
| RA9 | No imprescindible | H6-H7 | Gestión de datos en BD si el nivel lo permite. |

### 7.2. Entornos

| RA Entornos | Hitos principales | Evidencias clave |
|---|---|---|
| RA1 | H0-H1 | Fases de desarrollo, metodologías ágiles, relación programa-sistema. |
| RA2 | H1 | Instalación/configuración IntelliJ, proyectos, ejecutables, comparación de entornos si procede. |
| RA3 | H2-H3-H6 | Casos de prueba, depuración, pruebas unitarias, incidencias. |
| RA4 | H5-H6 | Refactorización, analizador, Git/GitHub, repositorios remotos, documentación, CI opcional. |
| RA5 | H4 | Diagramas de clases, ingeniería inversa, generación/interpretación. |
| RA6 | H4-H5 | Diagramas de comportamiento: casos de uso, actividad, secuencia/estado sencillos. |

---

## 8. Evaluación y calificación: propuesta de uso de la matriz

La matriz no fija todavía porcentajes definitivos de instrumentos, pero propone esta lógica:

1. Cada RA se califica con evidencias asociadas a criterios concretos.
2. Cada hito puede aportar evidencias a varios RA.
3. Las defensas individuales pueden ajustar o validar la calificación de evidencias grupales.
4. El portfolio individual sirve para detectar aprendizaje real, evolución y uso responsable de IA.
5. Una prueba individual puntual puede usarse cuando haya dudas razonables sobre comprensión o autoría.
6. RA7, RA8 y RA9 de Programación deben estar visibles en el diseño, pero no bloquearán la superación si no son imprescindibles y el grupo no permite un desarrollo profundo.

---

## 9. Próximo paso

A partir de esta matriz integrada se deben completar los anexos específicos:

1. Anexo Programación: desglose RA/CE por hito, con criterios concretos.
2. Anexo Entornos: desglose RA/CE por hito, con criterios concretos.
3. Rúbricas de hitos.
4. Diseño de la primera semana Scrum.
