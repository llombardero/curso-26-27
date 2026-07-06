# Calendario de hitos y sprints 2026/2027

## Programación + Entornos de Desarrollo — 1.º DAW — Granada

Versión: borrador 0.1
Documento base: `00-mapa-maestro-curso-2026-2027.md`
Matriz: `01-matriz-integrada-ra-ce-evidencias-tareas.md`
Anexos: `01A-anexo-programacion-ra-ce.md`, `01B-anexo-entornos-ra-ce.md`

---

## 1. Propósito

Este documento secuencia el proyecto guía del curso por hitos, sprints, evaluaciones y periodos lectivos.

Proyecto guía:

> Construcción progresiva de un pequeño agente IA propio.

El calendario mantiene separados los módulos de Programación y Entornos de Desarrollo, aunque ambos se coordinan mediante el mismo proyecto.

---

## 2. Referencia principal de objetivos

La referencia principal para los objetivos por módulos es:

```text
documentacion/Propuesta Ciclos Superiores IESHLanz 2026-27.pdf
```

Objetivo final:

> Formar AI-Enhanced Developers capaces de resolver problemas.

El alumnado debe aprender progresivamente a:

1. Comprender qué construir:
   - problema;
   - requisitos;
   - arquitectura;
   - modelo de datos;
   - stack tecnológico.
2. Construir con apoyo crítico de IA:
   - prompting;
   - agentes;
   - documentación estructurada;
   - control del bucle del agente;
   - lectura de errores y stack traces.
3. Asegurar que funciona:
   - Git;
   - pruebas;
   - depuración;
   - código limpio;
   - revisión;
   - Docker/CI cuando proceda;
   - defensa de decisiones.

Los temas del curso 2025/2026 se usan como referencia de contenidos y progresión, pero no son el eje principal. El eje principal será el proyecto del agente IA, alineado con RA/CE.

---

## 3. Condiciones temporales confirmadas

### 3.1. Evaluaciones

| Evaluación | Periodo |
|---|---|
| 1.ª evaluación | 15 septiembre - 23 diciembre 2026 |
| 2.ª evaluación | 7 enero - 31 marzo 2027 |
| 3.ª evaluación | 1 abril - 23 junio 2027 |

### 3.2. Periodos no lectivos y FFEOE

| Periodo / día | Situación |
|---|---|
| 12 octubre 2026 | Festivo nacional |
| 2 noviembre 2026 | Traslado Todos los Santos |
| 7 diciembre 2026 | Traslado Constitución |
| 8 diciembre 2026 | Inmaculada |
| 23 diciembre 2026 - 6 enero 2027 | Navidad |
| 26 febrero 2027 | Día Comunidad Educativa |
| 1 marzo 2027 | Traslado Día de Andalucía |
| 22 - 28 marzo 2027 | Semana Santa |
| 1 mayo 2027 | Fiesta del Trabajo |
| 3 mayo 2027 | Fiesta local Granada |
| 27 mayo 2027 | Fiesta local Granada |
| 28 mayo 2027 | Día no lectivo provincial |

FFEOE:

```text
Inicio: viernes 30 de abril de 2027
Fin real de jornadas: miércoles 26 de mayo de 2027
27 mayo: fiesta local
28 mayo: no lectivo provincial
```

Durante la FFEOE:

- no hay clases en el centro;
- no se programan entregas;
- no se piden tareas nuevas;
- el proyecto debe quedar cerrado en versión base antes del inicio.

### 3.3. Horario de módulos

Programación:

- lunes: 2 periodos;
- martes: 3 periodos;
- jueves: 3 periodos.

Entornos de Desarrollo:

- lunes: 2 periodos;
- martes: 1 periodo.

Cada periodo lectivo dura 45 minutos.

---

## 4. Criterios de secuenciación

1. H1 debe ser muy básico y coherente con el nivel inicial del alumnado.
2. H2 introduce menús, decisiones, bucles, errores y depuración.
3. H3 introduce memoria temporal y colecciones.
4. H4 introduce diseño orientado a objetos de forma fuerte.
5. H5 introduce extensibilidad, código limpio avanzado, refactorización, Git profesional y primeros patrones si procede.
6. H6 introduce persistencia, trazabilidad, ficheros, logs y ejecución reproducible.
7. H7 es opcional/adaptable y solo se profundiza si el grupo llega con base suficiente.
8. La comparación Java ↔ Python se hace en casa desde H2 hasta H7.
9. Código limpio se trabaja desde H1, pero con exigencia progresiva.
10. Patrones de diseño se introducen cuando haya una necesidad real, no como decoración.

---

## 5. Vista global de bloques

| Bloque | Fechas | Programación: periodos de 45 min | Entornos: periodos de 45 min | Producto principal |
|---|---|---:|---:|---|
| H0. Bootcamp Scrum | 15-18 septiembre | 6 | 1 | Torre de papel, tablero, roles y contrato de equipo. |
| H1. Primer asistente básico | 21 septiembre - 9 octubre | 24 | 9 | Programa Java muy básico + proyecto IntelliJ/GitHub. |
| H2. Decisiones y depuración | 13 octubre - 6 noviembre | 28 | 8 | Agente con menú, comandos, control de flujo y depuración. |
| H3. Memoria en colecciones | 9 noviembre - 4 diciembre | 32 | 12 | Agente con memoria temporal y pruebas de comportamiento. |
| C1. Cierre 1.ª evaluación | 9-22 diciembre | 16 | 6 | Demo parcial, portfolio, recuperación de mínimos y revisión. |
| H4. Agente orientado a objetos | 7 enero - 5 febrero | 35 | 12 | Modelo de clases del agente + diagramas UML. |
| H5. Herramientas, clean code y patrones iniciales | 8 febrero - 19 marzo | 46 | 16 | Agente extensible, refactorización, Git profesional y revisión. |
| C2. Cierre 2.ª evaluación | 29-31 marzo | 5 | 3 | Demo parcial, defensa y recuperación. |
| H6. Persistencia y trazabilidad | 1-23 abril | 27 | 9 | Ficheros, logs, base de conocimiento y documentación reproducible. |
| H7. IA responsable opcional | 26-29 abril | 8 | 3 | Integración Gemini/Jarvis o simulación robusta. |
| FFEOE | 30 abril - 28 mayo | 0 | 0 | Sin clases ni entregas. |
| HF. Presentación final y recuperación | 31 mayo - 22 junio | 29 | 12 | Defensa, portfolio final, recuperación y mejora. |

### 5.1. Vista global RA por bloque y módulo

Esta tabla se añade para que el calendario sea útil tanto para Programación como para Entornos de Desarrollo. Programación y Entornos mantienen documentación, RA/CE y evaluación separada, aunque compartan proyecto.

| Bloque | RA Programación | RA Entornos | Entregables especialmente útiles para Entornos |
|---|---|---|---|
| H0. Bootcamp Scrum | Diagnóstico inicial, sin calificación fuerte de RA técnicos | ED RA1.g | Tablero Scrum, contrato de equipo, retrospectiva de torre de papel. |
| H1. Primer asistente básico | PR RA1, PR RA2 inicial | ED RA1, ED RA2 | Proyecto IntelliJ, repositorio GitHub inicial, README de ejecución, evidencia de fuente/ejecutable. |
| H2. Decisiones y depuración | PR RA3, refuerzo PR RA1/RA2 | ED RA3 | Plan de pruebas manuales, informe de depuración, incidencias, capturas de breakpoints. |
| H3. Memoria en colecciones | PR RA6, refuerzo PR RA3 | ED RA3 | Pruebas de memoria, casos límite, documentación de incidencias, checklist de comportamiento. |
| C1. Cierre 1.ª evaluación | Consolidación PR RA1, RA2, RA3, RA6 | Consolidación ED RA1, RA2, RA3 inicial | Revisión de repositorio, portfolio técnico, defensa parcial, recuperación de evidencias. |
| H4. Agente orientado a objetos | PR RA4, refuerzo PR RA2 | ED RA5, ED RA6 | Diagrama de clases, diagrama de comportamiento, relación diagrama-código, defensa de diseño. |
| H5. Herramientas, clean code y patrones iniciales | PR RA7 no imprescindible, refuerzo PR RA4/RA6 | ED RA4, ED RA6 | Ramas/PRs, revisión de código, informe de refactorización, documentación de patrón si procede. |
| C2. Cierre 2.ª evaluación | Consolidación PR RA4 y ampliación PR RA7 | Consolidación ED RA4, RA5, RA6 | Demo parcial, revisión GitHub, defensa individual, plan de mejora. |
| H6. Persistencia y trazabilidad | PR RA5, PR RA8/RA9 como ampliación | ED RA3, ED RA4 | README reproducible, pruebas de persistencia, logs, Docker guiado si procede, documentación técnica. |
| H7. IA responsable opcional | Consolidación PR RA1-RA6; PR RA7/RA8/RA9 si procede | ED RA3, ED RA4 aplicados a seguridad, validación y trazabilidad | Documento de configuración segura, registro de prompts, validación humana, riesgos. |
| HF. Presentación final y recuperación | Recuperación/mejora de RA pendientes | Recuperación/mejora de RA pendientes | Portfolio final técnico, defensa individual, revisión de repositorio y evidencias. |

---

## 6. Secuencia detallada por bloques

### H0. Bootcamp Scrum y acuerdos

Fechas:

```text
15-18 septiembre 2026
```

Objetivo:

- Comprender Scrum viviéndolo en una simulación breve.
- Crear equipos de 3-4.
- Definir roles adaptados.
- Crear primer tablero.
- Preparar el modo de trabajo del curso.

Actividad central:

```text
Construcción de torre de papel
```

Entregables:

| Entregable | Responsable | Formato |
|---|---|---|
| Foto o evidencia de la torre | Equipo | Imagen o documento breve. |
| Tablero inicial | Equipo | Moodle/GitHub/captura. |
| Contrato de equipo | Equipo | Markdown o PDF. |
| Retrospectiva inicial | Individual + equipo | Markdown breve. |

RA/CE principales:

Programación:

- Diagnóstico inicial, sin calificación fuerte de RA técnicos.

Entornos de Desarrollo:

- ED RA1.g: metodologías ágiles.
- ED RA1.b: fases de desarrollo de una aplicación informática.

Entregables clave para Entornos:

- Tablero Scrum inicial.
- Contrato de equipo.
- Retrospectiva de la torre de papel.
- Traducción de la dinámica Scrum al proyecto del agente IA.

HEXA:

- Fase 0: Equipos.
- Activar.
- Ejecutar.
- Comunicar.

---

### H1. Primer asistente básico

Fechas:

```text
21 septiembre - 9 octubre 2026
```

Objetivo:

- Crear una primera versión muy básica del asistente.
- No introducir aún menú, bucles ni `switch`.
- Centrar el aprendizaje en estructura de programa, variables, constantes, entrada/salida e IntelliJ.

Producto:

```text
MiniJarvis H1: programa Java básico que pide el nombre y muestra mensajes iniciales.
```

Entregables:

| Entregable | Responsable | Formato |
|---|---|---|
| Código Java básico | Equipo o individual según decidas | `src/Main.java` en GitHub. |
| README de ejecución | Equipo | `README.md`. |
| Captura o evidencia de ejecución | Equipo | Imagen o bloque de salida. |
| Portfolio H1 | Individual | Markdown. |
| Registro de IA si se usa | Individual | Markdown. |

RA/CE principales:

Programación:

- PR RA1.
- PR RA2 inicial.

Entornos de Desarrollo:

- ED RA1.a-f: relación programa-sistema, fases, fuente/ejecutable, JVM, clasificación de lenguajes y herramientas.
- ED RA2.a, ED RA2.g: instalación/configuración de IntelliJ y características del entorno.

Entregables clave para Entornos:

- Proyecto IntelliJ configurado.
- Repositorio GitHub inicial.
- README de ejecución.
- Evidencia de código fuente y ejecución.

Código limpio:

- nombres claros;
- simplicidad;
- cada línea debe poder explicarse;
- evitar funcionalidades prematuras.

Ejemplo docente-alumna:

```text
99-ejemplos-alumna/h1-primer-asistente/
```

Estado del ejemplo:

```text
Dado por verificado definitivamente por decisión del docente.
```

---

### H2. Agente con decisiones y depuración

Fechas:

```text
13 octubre - 6 noviembre 2026
```

Objetivo:

- Convertir el asistente básico en un agente con menú.
- Introducir estructuras de selección, repetición, manejo de errores, pruebas manuales y depuración.

Producto:

```text
MiniJarvis H2: agente con comandos básicos, menú y salida controlada.
```

Entregables:

| Entregable | Responsable | Formato |
|---|---|---|
| Código Java con menú | Equipo | GitHub. |
| Plan de pruebas manuales | Equipo | `docs/pruebas-h2.md`. |
| Informe de depuración | Individual/equipo | Capturas o explicación de breakpoints. |
| Comparación Java ↔ Python | Individual, casa | Markdown + código Python si procede. |
| Registro de IA | Individual | Markdown. |
| Defensa corta | Individual | Oral. |

RA/CE principales:

Programación:

- PR RA3.
- Refuerzo PR RA1/RA2.

Entornos de Desarrollo:

- ED RA3.a-b: tipos de pruebas y definición de casos de prueba.
- ED RA3.c-e: herramientas de depuración, breakpoints y seguimiento en IntelliJ.
- ED RA3.h: documentación de incidencias.

Entregables clave para Entornos:

- `docs/pruebas-h2.md`.
- Informe de depuración.
- Registro de incidencia con síntoma, causa, solución y verificación.

HEXA:

- Investigar.
- Ejecutar.
- Comunicar.

Código limpio:

- evitar duplicación sencilla;
- nombres de comandos claros;
- mensajes comprensibles;
- comentarios solo si aclaran.

---

### H3. Agente con memoria en colecciones

Fechas:

```text
9 noviembre - 4 diciembre 2026
```

Objetivo:

- Añadir memoria temporal al agente.
- Trabajar estructuras de datos y casos límite.

Producto:

```text
MiniJarvis H3: agente que recuerda mensajes, preferencias o comandos usados.
```

Entregables:

| Entregable | Responsable | Formato |
|---|---|---|
| Código con memoria temporal | Equipo | GitHub. |
| README actualizado | Equipo | Markdown. |
| Pruebas de memoria | Equipo | Checklist o tests iniciales. |
| Comparación Java ↔ Python | Individual, casa | Listas/diccionarios frente a colecciones Java. |
| Portfolio H3 | Individual | Markdown. |
| Registro IA | Individual/equipo | Markdown. |

RA/CE principales:

Programación:

- PR RA6.
- Refuerzo PR RA3.

Entornos de Desarrollo:

- ED RA3.b: definición de casos de prueba para memoria temporal.
- ED RA3.f-g: pruebas unitarias/automáticas si el nivel lo permite.
- ED RA3.h: documentación de incidencias y casos límite.

Entregables clave para Entornos:

- Checklist de memoria temporal.
- Casos límite documentados.
- Primeras pruebas unitarias si el grupo está preparado.
- README actualizado con comportamiento esperado.

Código limpio:

- separar datos y lógica cuando sea posible;
- elegir colección con criterio;
- evitar nombres genéricos como `cosa`, `dato1`, `lista2`.

---

### C1. Cierre de 1.ª evaluación

Fechas:

```text
9-22 diciembre 2026
```

Objetivo:

- Consolidar H1-H3.
- Hacer demo parcial.
- Revisar portfolios.
- Recuperar mínimos de RA1, RA2, RA3 y RA6 si procede.

Entregables:

| Entregable | Responsable | Formato |
|---|---|---|
| Demo parcial del agente | Equipo | Oral + ejecución. |
| Portfolio 1.ª evaluación | Individual | Markdown/PDF. |
| Registro IA consolidado | Individual | Markdown. |
| Plan de mejora | Individual si procede | Markdown breve. |

---

### H4. Agente orientado a objetos

Fechas:

```text
7 enero - 5 febrero 2027
```

Objetivo:

- Rediseñar el agente usando clases propias.
- Introducir diseño OO y diagramas.

Producto:

```text
MiniJarvis H4: modelo OO con Agent, Message, Memory, Command u otras clases.
```

Entregables:

| Entregable | Responsable | Formato |
|---|---|---|
| Código Java organizado en clases | Equipo | GitHub. |
| Diagrama de clases | Equipo | Mermaid/PlantUML/draw.io. |
| Diagrama de comportamiento | Equipo | Actividad/secuencia/caso de uso. |
| Comparación Java ↔ Python | Individual, casa | Clases Java frente a clases Python. |
| Defensa de diseño | Individual | Oral. |

RA/CE principales:

Programación:

- PR RA4.
- Refuerzo PR RA2.

Entornos de Desarrollo:

- ED RA5.a-f: conceptos de POO, herramientas de diagramado, interpretación/generación de diagramas de clases e ingeniería inversa si procede.
- ED RA6.a-f: diagramas de comportamiento, casos de uso, interacción y actividad.

Entregables clave para Entornos:

- Diagrama de clases editable.
- Diagrama de comportamiento editable.
- Documento de relación diagrama-código.
- Defensa de una clase, relación o flujo.

Código limpio:

- clases con responsabilidad clara;
- nombres de clases significativos;
- evitar clases enormes;
- preparar el terreno para patrones, sin forzarlos aún.

---

### H5. Agente extensible, clean code y patrones iniciales

Fechas:

```text
8 febrero - 19 marzo 2027
```

Objetivo:

- Convertir el agente en extensible mediante herramientas o comandos.
- Introducir refactorización, revisión de código, Git profesional y patrones si tienen sentido.

Producto:

```text
MiniJarvis H5: agente con herramientas internas extensibles.
```

Entregables:

| Entregable | Responsable | Formato |
|---|---|---|
| Código con herramientas extensibles | Equipo | GitHub. |
| Evidencia de ramas/PR/revisión | Equipo | GitHub o registro equivalente. |
| Informe de refactorización | Equipo | Markdown. |
| Comparación Java ↔ Python | Individual, casa | Interfaces/composición frente a duck typing. |
| Registro de patrón si se usa | Equipo | Problema → patrón → alternativa → decisión. |
| Portfolio H5 | Individual | Markdown. |

RA/CE principales:

Programación:

- PR RA7, no imprescindible pero evaluable.
- Refuerzo PR RA4 y PR RA6.

Entornos de Desarrollo:

- ED RA4.a-e: patrones de refactorización, pruebas asociadas, analizador de código y refactorización con herramientas del entorno.
- ED RA4.f-h: control de versiones, documentación y repositorios remotos.
- ED RA4.i: integración continua si el nivel lo permite.
- ED RA6.g-h si se usan diagramas de estados para herramientas o flujo del agente.

Entregables clave para Entornos:

- Evidencia de ramas, commits, PR o revisión de código.
- Informe antes/después de refactorización.
- Captura o informe de inspecciones de IntelliJ.
- Registro de patrón de diseño si se usa.

Patrones de diseño:

- Introducción posible a Strategy, Command o Factory solo si resuelven un problema real.
- No se penaliza no usar patrón si una solución simple es más adecuada.
- Se penaliza usar un patrón sin entenderlo o sin necesidad.

Semana Santa:

```text
22-28 marzo 2027
```

No se programan entregas durante ese periodo.

---

### C2. Cierre de 2.ª evaluación

Fechas:

```text
29-31 marzo 2027
```

Objetivo:

- Cerrar H4-H5.
- Hacer defensa parcial.
- Revisar RA pendientes.
- Preparar la fase final antes de FFEOE.

Entregables:

| Entregable | Responsable | Formato |
|---|---|---|
| Demo parcial H4-H5 | Equipo | Oral + ejecución. |
| Revisión de repositorio | Equipo | GitHub. |
| Defensa individual | Individual | Oral. |
| Revisión de diagramas UML | Equipo | Fuente editable + exportación. |
| Plan de recuperación | Individual si procede | Markdown. |

RA/CE principales:

Programación:

- Consolidación PR RA4.
- PR RA7 como ampliación/no imprescindible.

Entornos de Desarrollo:

- Consolidación ED RA4, ED RA5 y ED RA6.
- Revisión de evidencias: refactorización, GitHub, diagramas de clases y comportamiento.

---

### H6. Agente persistente y trazable

Fechas:

```text
1-23 abril 2027
```

Objetivo:

- Añadir persistencia simple, logs, base de conocimiento y trazabilidad.
- Preparar el proyecto para cerrarse antes de la FFEOE.

Producto:

```text
MiniJarvis H6: agente con memoria persistente en ficheros y documentación reproducible.
```

Entregables:

| Entregable | Responsable | Formato |
|---|---|---|
| Código con lectura/escritura de ficheros | Equipo | GitHub. |
| Logs o historial persistente | Equipo | Ficheros de ejemplo sin datos personales. |
| README reproducible | Equipo | Markdown. |
| Pruebas de persistencia | Equipo | Checklist o tests. |
| Comparación Java ↔ Python | Individual, casa | Ficheros/JSON/logs. |
| Registro IA | Individual/equipo | Markdown. |

RA/CE principales:

Programación:

- PR RA5.
- PR RA8/RA9 como ampliación si procede.

Entornos de Desarrollo:

- ED RA3.b, ED RA3.f-h: pruebas de persistencia, pruebas automáticas si procede e incidencias.
- ED RA4.f-i: control de versiones, documentación técnica, repositorios remotos e integración continua si el nivel lo permite.

Entregables clave para Entornos:

- README reproducible.
- Checklist o pruebas de persistencia.
- Documentación de logs/historial sin datos personales.
- Configuración Docker guiada si procede.
- Registro de decisiones de seguridad: `.env`, secretos y datos personales.

Seguridad:

- No usar credenciales reales.
- No subir `.env` con secretos.
- No introducir datos personales en pruebas.

---

### H7. Integración IA responsable opcional

Fechas:

```text
26-29 abril 2027
```

Objetivo:

- Integrar Gemini/Jarvis o simular de forma robusta una llamada IA.
- No comprometer el cierre del proyecto antes de FFEOE.

Producto:

```text
MiniJarvis H7: modo IA responsable real o simulado.
```

Entregables:

| Entregable | Responsable | Formato |
|---|---|---|
| Integración o simulación IA | Equipo | Código + README. |
| Registro de prompts | Individual/equipo | Markdown. |
| Documento de riesgos | Equipo | Markdown. |
| Comparación Java ↔ Python | Individual, casa | Integración/simulación equivalente. |
| Defensa de IA responsable | Individual | Oral. |

RA/CE principales:

Programación:

- Consolidación de RA imprescindibles.
- PR RA7/RA8/RA9 si procede.

Entornos de Desarrollo:

- ED RA3: pruebas y validación del comportamiento de la integración o simulación IA.
- ED RA4: documentación, control de versiones, configuración, revisión y trazabilidad.
- Aplicación transversal de seguridad: no secretos, no datos personales, validación humana.

Entregables clave para Entornos:

- Documento de configuración segura.
- Registro de prompts y validación.
- Documento de riesgos y limitaciones.
- Evidencia de revisión de código/configuración.

Condición:

- Si el grupo no está preparado, H7 será solo una simulación robusta y defendible.

---

### FFEOE

Fechas:

```text
30 abril - 28 mayo 2027
```

No hay clases ni entregas.

El proyecto base debe estar cerrado antes de este periodo.

---

### HF. Presentación final, recuperación y mejora

Fechas:

```text
31 mayo - 22 junio 2027
```

Objetivo:

- Presentación final si procede.
- Recuperación de RA pendientes.
- Mejora del portfolio.
- Defensa individual.

Entregables:

| Entregable | Responsable | Formato |
|---|---|---|
| Portfolio final | Individual | Markdown/GitHub o mixto. |
| Defensa final | Individual | Oral. |
| Demo final | Equipo | Ejecución + explicación. |
| Recuperación específica | Individual | Según RA pendiente. |
| Registro IA final | Individual | Markdown. |

---

## 7. Resumen RA por evaluación

### 1.ª evaluación

Programación:

| RA | Papel en la evaluación | Evidencias principales |
|---|---|---|
| PR RA1 | Principal | H1: estructura básica Java, variables, constantes, entrada/salida. |
| PR RA2 inicial | Inicial/refuerzo | H1-H2: programas simples y primeros objetos/librerías. |
| PR RA3 | Principal | H2: menú, decisiones, bucles, errores y depuración. |
| PR RA6 | Principal | H3: memoria temporal y colecciones. |

Entornos de Desarrollo:

| RA | Papel en la evaluación | Evidencias principales |
|---|---|---|
| ED RA1 | Principal | H0-H1: fases, metodologías ágiles, fuente/ejecutable, herramientas. |
| ED RA2 | Principal | H1: IntelliJ, proyecto, configuración, ejecución y comparación básica de entornos. |
| ED RA3 inicial | Inicial/principal parcial | H2-H3: casos de prueba, depuración, incidencias y pruebas iniciales. |

### 2.ª evaluación

Programación:

| RA | Papel en la evaluación | Evidencias principales |
|---|---|---|
| PR RA4 | Principal | H4: clases, objetos, constructores, visibilidad y diseño OO. |
| PR RA7 | No imprescindible/evaluable | H5: extensibilidad, interfaces/herencia/composición si procede. |
| PR RA2, RA3, RA6 | Refuerzo | Evolución del agente y defensa técnica. |

Entornos de Desarrollo:

| RA | Papel en la evaluación | Evidencias principales |
|---|---|---|
| ED RA4 | Principal | H5: refactorización, GitHub, revisión de código, documentación e integración si procede. |
| ED RA5 | Principal | H4: diagrama de clases, interpretación y relación con código. |
| ED RA6 | Principal | H4-H5: diagramas de comportamiento, actividad/secuencia/estados si procede. |

### 3.ª evaluación antes de FFEOE

Programación:

| RA | Papel en la evaluación | Evidencias principales |
|---|---|---|
| PR RA5 | Principal | H6: entrada/salida, ficheros, logs, persistencia simple. |
| PR RA8 | No imprescindible/evaluable | H6-H7: persistencia orientada a objetos si el ritmo lo permite. |
| PR RA9 | No imprescindible/evaluable | H6-H7: gestión de datos/BD si el ritmo lo permite. |
| PR RA1-RA6 | Consolidación | Cierre del proyecto base antes de FFEOE. |

Entornos de Desarrollo:

| RA | Papel en la evaluación | Evidencias principales |
|---|---|---|
| ED RA3 | Aplicación avanzada | H6-H7: pruebas de persistencia, validación de integración/simulación IA, incidencias. |
| ED RA4 | Aplicación avanzada | H6-H7: documentación reproducible, GitHub, CI/Docker si procede, seguridad y trazabilidad. |
| ED RA1-RA6 | Consolidación | Revisión final del flujo profesional y evidencias pendientes. |

### Tras FFEOE

Programación:

- Recuperación de RA imprescindibles pendientes.
- Mejora de evidencias.
- Defensa individual.

Entornos de Desarrollo:

- Recuperación de RA pendientes.
- Revisión de repositorio, documentación, diagramas, pruebas y portfolio.
- Defensa individual del proceso técnico seguido.

---

## 8. Próximos documentos derivados

1. Diseño detallado de la primera semana Scrum.
2. Política de IA: semáforo, registro y defensa.
3. Rúbricas por hito.
4. Plantillas de entregables.
5. Ejemplos reales progresivos como alumna para H2, H3, H4...

---

## 9. Estado de verificación del ejemplo H1

El ejemplo:

```text
99-ejemplos-alumna/h1-primer-asistente/
```

queda marcado como:

```text
Verificado definitivamente por decisión del docente.
```

Nota de trazabilidad:

- La verificación automática ad-hoc no pudo ejecutarse por bloqueo del sistema de permisos.
- El docente ha decidido dar por verificado el ejemplo para no bloquear el diseño didáctico.
