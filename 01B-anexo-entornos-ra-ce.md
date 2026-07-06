# Anexo 01B — Entornos de Desarrollo: RA/CE → hitos → evidencias → tareas

## 1.º DAW — Curso 2026/2027

Versión: borrador 0.1
Documento integrado de referencia: `01-matriz-integrada-ra-ce-evidencias-tareas.md`
Mapa maestro: `00-mapa-maestro-curso-2026-2027.md`

---

## 1. Propósito del anexo

Este anexo desglosa el módulo de Entornos de Desarrollo en Resultados de Aprendizaje, Criterios de Evaluación, hitos del proyecto del agente IA, evidencias, entregables e instrumentos.

El módulo de Entornos se diseña como el soporte profesional del proyecto de Programación. No queda subordinado ni aislado: proporciona las prácticas, herramientas y hábitos que permiten desarrollar el agente IA de forma trazable, colaborativa, depurable, documentada y defendible.

---

## 2. Condiciones organizativas confirmadas

Distribución semanal:

- Lunes: 2 periodos lectivos de Entornos.
- Martes: 1 periodo lectivo de Entornos.
- Cada periodo lectivo dura 45 minutos.
- Las clases se imparten por la tarde.

Cómputo provisional:

| Periodo | Periodos lectivos de 45 min | Horas reloj aproximadas | Días con sesión de Entornos |
|---|---:|---:|---:|
| 1.ª evaluación | 36 | 27 h | 25 |
| 2.ª evaluación | 31 | 23,25 h | 21 |
| 3.ª evaluación antes de FFEOE | 12 | 9 h | 8 |
| FFEOE | 0 | 0 h | 0 |
| Recuperación/cierre tras FFEOE | 12 | 9 h | 8 |

Criterio didáctico:

- La sesión doble del lunes se usará para talleres, prácticas guiadas, revisión de herramientas, UML, GitHub, pruebas, refactorización o Docker.
- La sesión breve del martes se usará para seguimiento, resolución de incidencias, revisión de portfolio, checklist, preparación del sprint, cierre técnico o mini-defensas.

---

## 3. Relación general RA ↔ hitos

| RA Entornos | Hitos principales | Función dentro del proyecto |
|---|---|---|
| RA1 | H0-H1 | Comprender fases de desarrollo, herramientas, lenguajes y metodologías ágiles. |
| RA2 | H1 | Instalar, configurar y usar IntelliJ para crear, ejecutar y comparar proyectos. |
| RA3 | H2-H3-H6 | Diseñar casos de prueba, depurar, documentar incidencias y automatizar pruebas si procede. |
| RA4 | H5-H6 | Refactorizar, analizar código, usar Git/GitHub, repositorios remotos, documentación e integración continua si procede. |
| RA5 | H4 | Crear, interpretar y revisar diagramas de clases relacionados con el agente. |
| RA6 | H4-H5 | Crear e interpretar diagramas de comportamiento: casos de uso, actividad, interacción o estados. |

---

## 4. Entregables claros por hito desde Entornos

Cada entregable debe indicar explícitamente qué debe entregar el alumnado, en qué formato y cómo se verificará.

| Hito | Qué entrega el alumnado | Formato esperado | Verificación |
|---|---|---|---|
| H0 | Tablero Scrum inicial, contrato de equipo y retrospectiva de la torre de papel. | Foto o captura del tablero, Markdown/PDF breve, Moodle o GitHub. | Revisión de roles, backlog, acuerdos y retrospectiva. |
| H1 | Proyecto IntelliJ configurado, repositorio GitHub inicial y README de ejecución. | Repositorio GitHub + README.md + captura de ejecución. | Se clona/abre el proyecto, se ejecuta y se comprueba la estructura. |
| H2 | Plan de pruebas manuales, informe de depuración e incidencias del agente con menú. | `docs/pruebas-h2.md`, capturas de breakpoints, checklist. | Se reproducen casos de prueba y se pregunta por el proceso de depuración. |
| H3 | Pruebas de memoria temporal y documentación de casos límite. | Tests si procede, checklist, README actualizado. | Se comprueba que la memoria añade, lista, busca y gestiona errores. |
| H4 | Diagrama de clases y al menos un diagrama de comportamiento del agente. | PlantUML, Mermaid, draw.io exportado o imagen + fuente editable. | Se contrasta diagrama contra código y se defiende una relación/clase. |
| H5 | Evidencia de GitHub colaborativo, refactorización y revisión de código. | Ramas/commits/pull request o registro equivalente; informe breve. | Se revisa historial, cambios antes/después y justificación técnica. |
| H6 | Documentación de ejecución reproducible, persistencia y, si procede, Docker guiado. | README, checklist, capturas, configuración o guía paso a paso. | Se ejecuta el proyecto siguiendo la documentación. |
| H7 | Documento de configuración segura y trazabilidad de IA. | Registro de prompts, limitaciones, validación y riesgos. | Se verifica que no hay secretos y que la IA se valida humanamente. |
| HF | Portfolio final técnico y defensa del proceso. | Portfolio Markdown/GitHub o formato mixto si hay dificultades. | Entrevista individual, revisión de repositorio y evidencias. |

---

## 5. RA1 — Elementos, herramientas y fases de desarrollo

Resultado de Aprendizaje:

> Reconoce los elementos y herramientas que intervienen en el desarrollo de un programa informático, analizando sus características y las fases en las que actúan hasta llegar a su puesta en funcionamiento.

Hitos principales:

- H0. Bootcamp Scrum y acuerdos.
- H1. Primer asistente por consola.

### 5.1. Criterios de evaluación y evidencias

| CE | Criterio | Evidencia propuesta | Instrumentos |
|---|---|---|---|
| a | Se ha reconocido la relación de los programas con componentes del sistema informático. | Explicación de cómo el agente usa memoria, procesador, entrada/salida y almacenamiento. | Portfolio, defensa. |
| b | Se han identificado las fases de desarrollo de una aplicación informática. | Mapa de fases aplicado al agente: idea, análisis, diseño, implementación, pruebas, despliegue, mantenimiento. | Actividad, portfolio. |
| c | Se han diferenciado código fuente, objeto y ejecutable. | Explicación sobre `.java`, `.class`, ejecución en JVM y salida del proyecto. | Defensa, README. |
| d | Se ha reconocido la generación de código intermedio para máquinas virtuales. | Relación entre Java, bytecode y JVM. | Preguntas orales, esquema. |
| e | Se han clasificado lenguajes de programación. | Comparativa Java/Python/JavaScript, especialmente desde H2 como tarea para casa. | Tabla comparativa. |
| f | Se ha evaluado la funcionalidad de herramientas de desarrollo. | Valoración inicial de IntelliJ, GitHub, Moodle y Jarvis/Gemini como herramientas de apoyo. | Portfolio, debate. |
| g | Se han identificado características y escenarios de uso de metodologías ágiles. | Sprint de torre de papel y traducción a Scrum del proyecto agente. | Tablero, retrospectiva. |

### 5.2. Entregable específico

Nombre sugerido:

```text
ED-H0H1-fases-herramientas-scrum.md
```

Debe incluir:

- Equipo y roles.
- Evidencia del sprint de torre de papel.
- Fases de desarrollo aplicadas al agente IA.
- Diferencia entre código fuente, bytecode y ejecución.
- Tabla de herramientas usadas y para qué sirven.
- Mini-reflexión individual: qué necesito aprender para trabajar bien en equipo.

---

## 6. RA2 — Entornos integrados de desarrollo

Resultado de Aprendizaje:

> Evalúa entornos integrados de desarrollo, analizando sus características para editar código fuente y generar ejecutables.

Hito principal:

- H1. Primer asistente por consola.

### 6.1. Criterios de evaluación y evidencias

| CE | Criterio | Evidencia propuesta | Instrumentos |
|---|---|---|---|
| a | Se han instalado entornos de desarrollo, propietarios y libres. | IntelliJ instalado/configurado; referencia a alternativas libres si procede. | Checklist, captura. |
| b | Se han añadido y eliminado módulos en el entorno. | Configuración básica del proyecto, SDK, módulos o estructura. | Captura, defensa. |
| c | Se ha personalizado y automatizado el entorno. | Formato de código, atajos, plantilla README o configuración mínima. | Checklist. |
| d | Se ha configurado el sistema de actualización del entorno. | Revisión de configuración de actualizaciones/plugins. | Captura breve. |
| e | Se han generado ejecutables a partir de código fuente de diferentes lenguajes en un mismo entorno. | Java como principal; Python como comparación en casa desde H2 si procede. | Evidencia técnica. |
| f | Se han generado ejecutables a partir de un mismo código fuente con varios entornos. | Opcional: ejecutar desde IntelliJ y terminal. | Captura/demo. |
| g | Se han identificado características comunes y específicas de diversos entornos. | Comparación IntelliJ / VS Code / terminal, si procede. | Tabla comparativa. |

### 6.2. Entregable específico

Nombre sugerido:

```text
ED-H1-intellij-github-readme.md
```

Debe entregar:

- Repositorio GitHub del equipo.
- Proyecto IntelliJ con SDK correcto.
- README con instrucciones para ejecutar el agente.
- Captura de ejecución.
- Captura o explicación de configuración básica del IDE.
- Tabla breve: IntelliJ frente a terminal/otro editor.

---

## 7. RA3 — Verificación, pruebas y depuración

Resultado de Aprendizaje:

> Verifica el funcionamiento de programas diseñando y realizando pruebas.

Hitos principales:

- H2. Agente con decisiones y depuración.
- H3. Agente con memoria en colecciones.
- H6. Agente persistente y trazable.

### 7.1. Criterios de evaluación y evidencias

| CE | Criterio | Evidencia propuesta | Instrumentos |
|---|---|---|---|
| a | Se han identificado los diferentes tipos de pruebas. | Tabla de pruebas manuales, unitarias y de regresión aplicadas al agente. | Portfolio, checklist. |
| b | Se han definido casos de prueba. | Casos de prueba para comandos, entradas inválidas, memoria y persistencia. | `docs/pruebas.md`. |
| c | Se han identificado herramientas de depuración y prueba del IDE. | Breakpoints, step over, watch variables en IntelliJ. | Capturas, defensa. |
| d | Se han utilizado herramientas de depuración para puntos de ruptura y seguimiento. | Evidencia de sesión de depuración. | Capturas, observación. |
| e | Se ha examinado/modificado el comportamiento en tiempo de ejecución. | Seguimiento de variables y corrección de bug. | Informe de incidencia. |
| f | Se han efectuado pruebas unitarias de clases y funciones. | JUnit básico si el ritmo lo permite. | Tests, informe. |
| g | Se han implementado pruebas automáticas. | Actividad de ampliación o consolidación. | Tests automatizados. |
| h | Se han documentado incidencias detectadas. | Registro de bugs, pasos para reproducir, solución. | GitHub issues o Markdown. |
| i | Se han utilizado dobles de prueba para aislar componentes. | Ampliación si hay arquitectura suficiente. | Actividad avanzada. |

### 7.2. Entregable específico

Nombre sugerido:

```text
ED-H2H3-pruebas-depuracion-incidencias.md
```

Debe entregar:

- Tabla de casos de prueba.
- Al menos una incidencia documentada con: síntoma, pasos, causa, solución y verificación.
- Captura o descripción de depuración con breakpoint.
- Checklist de comportamiento esperado.
- Si procede, primeros tests unitarios.

---

## 8. RA4 — Optimización, refactorización, GitHub e integración

Resultado de Aprendizaje:

> Optimiza código empleando las herramientas disponibles en el entorno de desarrollo.

Hitos principales:

- H5. Agente extensible con herramientas.
- H6. Agente persistente y trazable.

### 8.1. Criterios de evaluación y evidencias

| CE | Criterio | Evidencia propuesta | Instrumentos |
|---|---|---|---|
| a | Se han identificado patrones de refactorización usuales. | Tabla: extraer método, renombrar, extraer clase, eliminar duplicación. | Portfolio. |
| b | Se han elaborado pruebas asociadas a refactorización. | Pruebas antes/después de refactorizar. | Tests/checklist. |
| c | Se ha revisado código con analizador. | Uso de inspecciones IntelliJ o herramienta equivalente. | Captura, informe. |
| d | Se han identificado posibilidades de configuración de analizador. | Configuración básica de inspecciones/formato. | Captura. |
| e | Se han aplicado patrones de refactorización con herramientas del entorno. | Refactorización real en IntelliJ. | Diff, commits. |
| f | Se ha realizado control de versiones integrado en el entorno. | Git desde IntelliJ o terminal. | Commits, defensa. |
| g | Se han utilizado herramientas para documentar clases. | JavaDoc o documentación equivalente. | Código, README. |
| h | Se han utilizado repositorios remotos para desarrollo colaborativo. | GitHub con ramas, issues o PR. | Repositorio. |
| i | Se han utilizado herramientas para integración continua. | GitHub Actions básico si procede. | Workflow, badge, captura. |

### 8.2. Entregable específico

Nombre sugerido:

```text
ED-H5H6-refactorizacion-github-calidad.md
```

Debe entregar:

- Evidencia de uso de GitHub: commits, ramas o issues.
- Informe antes/después de una refactorización.
- Justificación de qué problema resolvía la refactorización.
- Captura o informe de inspección de IntelliJ.
- README actualizado.
- Si procede, workflow de GitHub Actions o explicación de por qué no se aplicó.

---

## 9. RA5 — Diagramas de clases

Resultado de Aprendizaje:

> Genera diagramas de clases, valorando su importancia en el desarrollo de aplicaciones y empleando las herramientas disponibles específicas.

Hito principal:

- H4. Agente orientado a objetos.

### 9.1. Criterios de evaluación y evidencias

| CE | Criterio | Evidencia propuesta | Instrumentos |
|---|---|---|---|
| a | Se han identificado conceptos básicos de POO. | Relación clase/objeto/atributo/método en el agente. | Defensa. |
| b | Se han utilizado herramientas para diagramas de clases. | Mermaid, PlantUML, draw.io, IntelliJ u otra. | Archivo fuente + imagen. |
| c | Se ha interpretado el significado de diagramas de clases. | Explicación oral de relaciones. | Defensa. |
| d | Se han trazado diagramas de clases a partir de especificaciones. | Diagrama inicial del agente. | Diagrama. |
| e | Se ha generado código a partir de un diagrama. | Actividad guiada si procede. | Código/actividad. |
| f | Se ha generado diagrama mediante ingeniería inversa. | Diagrama desde código si herramienta lo permite, o reconstrucción razonada. | Evidencia técnica. |

### 9.2. Entregable específico

Nombre sugerido:

```text
ED-H4-diagrama-clases-agente.md
```

Debe entregar:

- Diagrama de clases del agente.
- Archivo editable del diagrama.
- Relación entre clases del diagrama y clases del código.
- Explicación de al menos tres decisiones de diseño.
- Una revisión posterior: qué cambió del diagrama inicial al código real.

---

## 10. RA6 — Diagramas de comportamiento

Resultado de Aprendizaje:

> Genera diagramas de comportamiento, valorando su importancia en el desarrollo de aplicaciones y empleando las herramientas específicas.

Hitos principales:

- H4. Agente orientado a objetos.
- H5. Agente extensible con herramientas.

### 10.1. Criterios de evaluación y evidencias

| CE | Criterio | Evidencia propuesta | Instrumentos |
|---|---|---|---|
| a | Se han identificado distintos tipos de diagramas de comportamiento. | Tabla breve: casos de uso, actividad, secuencia, estados. | Portfolio. |
| b | Se ha reconocido significado de casos de uso. | Caso de uso: usuario consulta al agente. | Diagrama, defensa. |
| c | Se han interpretado diagramas de interacción. | Lectura de secuencia usuario-agente-herramienta. | Preguntas orales. |
| d | Se han elaborado diagramas de interacción sencillos. | Diagrama de secuencia de un comando. | Diagrama. |
| e | Se ha interpretado significado de diagramas de actividades. | Flujo de decisión del agente. | Defensa. |
| f | Se han elaborado diagramas de actividades sencillos. | Actividad: procesar comando. | Diagrama. |
| g | Se han interpretado diagramas de estados. | Estados opcionales del agente: esperando, procesando, error, finalizado. | Actividad. |
| h | Se han planteado diagramas de estados sencillos. | Ampliación si procede. | Diagrama. |

### 10.2. Entregable específico

Nombre sugerido:

```text
ED-H4H5-diagramas-comportamiento-agente.md
```

Debe entregar:

- Al menos un diagrama de comportamiento obligatorio:
  - actividad o secuencia.
- Opcionalmente, caso de uso o estados.
- Archivo editable del diagrama.
- Explicación de cómo el diagrama ayuda a entender o mejorar el agente.
- Comparación entre el diagrama previsto y el comportamiento real del programa.

---

## 11. Ejemplo real de entregable como alumna

A partir de ahora se generarán ejemplos reales de entregables como si los elaborara una alumna del ciclo.

Ejemplo inicial creado para orientar el nivel esperado:

```text
99-ejemplos-alumna/h1-primer-asistente/
```

Este ejemplo no debe entregarse al alumnado como solución cerrada sin adaptación. Su función es servir al docente para calibrar:

- nivel de detalle esperado;
- estructura de repositorio;
- README;
- portfolio;
- registro de IA;
- defensa mínima;
- calidad realista de una primera entrega.

---

## 12. Recuperación y mejora en Entornos

| RA pendiente | Actividad de recuperación propuesta |
|---|---|
| RA1 | Documento individual sobre fases, herramientas y Scrum aplicado al agente. |
| RA2 | Configurar proyecto IntelliJ, ejecutarlo y defender SDK/proyecto/README. |
| RA3 | Crear casos de prueba, depurar un bug y documentar incidencia. |
| RA4 | Refactorizar un fragmento, justificarlo y mostrar commits. |
| RA5 | Crear/revisar diagrama de clases y relacionarlo con código. |
| RA6 | Crear diagrama de actividad/secuencia y defender el comportamiento. |

---

## 13. Próximo paso recomendado

Después de este anexo, el siguiente artefacto debería ser:

```text
02-calendario-hitos-sprints-2026-2027.md
```

Ese documento secuenciará por trimestres:

- hitos;
- sprints;
- RA/CE principales;
- entregables;
- semanas sin clase;
- FFEOE;
- recuperación posterior.
