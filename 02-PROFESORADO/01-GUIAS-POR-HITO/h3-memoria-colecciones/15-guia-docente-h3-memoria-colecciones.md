# Guía docente — H3 Agente con memoria en colecciones

<!-- HEXA-CICLO-COMPLETO-POR-HITO:START -->

## Ciclo HEXA obligatorio del reto H3

**Reto del hito:** Añadir memoria temporal mediante una colección adecuada y demostrar su comportamiento y límites.

**Base transversal — Fase 0 Equipos:** se mantienen roles, normas, colaboración y herramientas de organización durante todo el reto. El profesorado hace visible el avance de fase y sitúa la instrucción guiada principalmente en Investigar, sin reducir HEXA a una etiqueta.

| Fase | Pregunta que guía la fase | Acción del profesorado | Acción y evidencia del alumnado |
|---|---|---|---|
| **1 — Activar** | ¿Qué reto real debemos entender y con qué propósito, límites y criterios? | Presenta y contextualiza el reto sin anticipar la solución. | Reformula el reto y explicita objetivos, dudas y criterios. |
| **2 — Investigar** | ¿Qué necesitamos aprender para abordar el reto? | Facilita búsqueda guiada, micropíldoras y fuentes seguras. | Investiga, contrasta, practica y construye la base conceptual necesaria. |
| **3 — Idear** | ¿Qué soluciones posibles podemos proponer y cuál elegimos? | Abre alternativas y exige criterios de selección. | Genera, compara y argumenta una solución viable. |
| **4 — Planificar** | ¿Cómo convertimos la idea en tareas, tiempos y responsabilidades? | Ayuda a hacer visibles backlog, hitos, dependencias y criterios de seguimiento. | Organiza tareas, tiempos, responsabilidades y comprobaciones. |
| **5 — Ejecutar** | ¿Cómo construimos, probamos y mejoramos la solución? | Desbloquea sin sustituir la autoría y exige iteración y pruebas. | Crea el producto, lo prueba, corrige y conserva evidencias. |
| **6 — Comunicar** | ¿Cómo presentamos, evaluamos y reflexionamos sobre producto y proceso? | Facilita defensa, evaluación formativa, coevaluación y mejora. | Presenta, defiende, evalúa, reflexiona y formula el siguiente paso. |

### Temporalización explícita sobre las sesiones operativas

Las fases siguen el orden canónico y pueden solaparse cuando una sesión cierra una y abre la siguiente.

| Fase | Sesiones de referencia | Puerta de salida |
|---|---|---|
| 1 — Activar | S229 | Reto comprendido y criterios visibles. |
| 2 — Investigar | S230–S232 | Conocimientos necesarios contrastados. |
| 3 — Idear | S233 | Solución seleccionada y argumentada. |
| 4 — Planificar | S234 | Plan, responsabilidades y comprobaciones visibles. |
| 5 — Ejecutar | S235–S238 | Producto construido, probado y mejorado. |
| 6 — Comunicar | S239–S240 | Defensa, evaluación, reflexión y mejora. |

**Expediente HEXA mínimo del hito:** requisitos de memoria, comparación de alternativas, explicación de ArrayList/casos límite, código, pruebas y defensa.

Regla de avance: puede haber prototipos durante Investigar o Idear, pero Ejecutar no se considera completada si faltan evidencias de Activar, Investigar, Idear o Planificar. Comunicar exige presentar, evaluar y reflexionar. Si falta una fase, se recuperan esa fase y su evidencia; no se repite automáticamente todo el hito.

<!-- HEXA-CICLO-COMPLETO-POR-HITO:END -->

## Programación — 1.º DAW — Curso 2026/2027

Edición final para Moodle — septiembre de 2026

Documento para uso del profesorado.

Documentos relacionados:

- `../../02-calendario-hitos-sprints-2026-2027.md`
- `../../04A-enunciados-y-entregables-alumnado.md`
- `../../06-rubricas-hitos.md`
- `README.md`
- `15B-ficha-alumnado-h3-memoria-colecciones.md`
- `15C-checklist-correccion-h3.md`

---

## 1. Propósito del hito

H3 añade memoria temporal a MiniJarvis.

Producto esperado:

```text
MiniJarvis H3: agente por consola que recuerda información durante la ejecución usando colecciones Java.
```

El hito introduce:

- elección de colección;
- memoria temporal;
- consulta de memoria;
- casos límite;
- pruebas de memoria;
- comparación Java ↔ Python;
- defensa de la estructura elegida.

---

## 2. Qué añade H3 respecto a H2

| H2 | H3 |
|---|---|
| Menú y comandos. | Menú con memoria temporal. |
| Control de flujo. | Almacenamiento durante la ejecución. |
| Pruebas de comandos. | Pruebas de memoria y casos límite. |
| Depuración básica. | Observación de cómo cambia una colección. |
| Comparación de bucles/decisiones con Python. | Comparación de colecciones Java con `list`/`dict`. |

---

## 3. Restricciones didácticas

En H3 sí debe aparecer:

- al menos una colección Java;
- comando para guardar información;
- comando para consultar memoria;
- caso de memoria vacía;
- pruebas de memoria;
- justificación de colección.

En H3 todavía NO debe aparecer:

- persistencia en ficheros;
- base de datos;
- arquitectura OO completa;
- interfaces/patrones;
- API externa;
- IA real.

Motivo:

```text
H3 debe consolidar estructuras de datos antes de introducir persistencia, diseño OO fuerte o integración IA.
```

---

## 4. Fechas y duración

Fechas orientativas:

```text
9 noviembre - 4 diciembre 2026
```

Carga estimada:

```text
Programación: 32 periodos de 45 min
```

---

## 5. RA/CE y evidencias

### Programación

RA principales:

- PR RA6: manipulación de información y tipos avanzados de datos.
- Refuerzo PR RA3: control de flujo y comandos.

Evidencias:

- uso de `ArrayList`, `HashMap` u otra colección;
- comandos de guardar/consultar;
- gestión de memoria vacía;
- explicación de elección de colección;
- defensa del recorrido o consulta.

### Prácticas técnicas del proyecto

RA principales:

- pruebas y depuración: definición de casos de prueba.
- pruebas y depuración: pruebas automáticas si el grupo está preparado.
- pruebas y depuración: documentación de incidencias y casos límite.

Evidencias:

- `docs/pruebas-memoria-h3.md`;
- `docs/incidencia-h3.md` si procede;
- README actualizado;
- comparación Java ↔ Python.

---

## 6. Producto mínimo esperado

Comandos orientativos:

| Comando | Comportamiento esperado |
|---|---|
| `ayuda` | Muestra comandos disponibles. |
| `saluda` | Saluda al usuario. |
| `recuerda` | Guarda un mensaje simple en memoria temporal. |
| `memoria` | Muestra mensajes guardados o avisa si está vacía. |
| `estado` | Indica cuántos elementos hay en memoria. |
| `salir` | Termina de forma controlada. |
| Otro texto | Mensaje de comando desconocido. |

Ejemplo:

```text
> memoria
No tengo recuerdos todavía.
> recuerda
¿Qué quieres que recuerde? Traer pendrive
He guardado: Traer pendrive
> memoria
1. Traer pendrive
> estado
Tengo 1 recuerdo en memoria temporal.
```

---

## 7. Secuencia didáctica sugerida

| Bloque | Foco | Producto parcial |
|---|---|---|
| 1 | Revisar H2 y presentar memoria temporal | Diferencia H2/H3 clara. |
| 2 | Elegir información a recordar | Decidir mensajes, comandos o preferencias. |
| 3 | Introducir `ArrayList`/`HashMap` | Colección inicial. |
| 4 | Crear comando `recuerda` | Guarda información. |
| 5 | Crear comando `memoria` | Consulta información. |
| 6 | Casos límite | Memoria vacía, entradas vacías, repetidos. |
| 7 | Pruebas de memoria | Tabla esperado/obtenido. |
| 8 | Comparación Java ↔ Python | `ArrayList`/`HashMap` frente a `list`/`dict`. |
| 9 | Defensa y cierre C1 | Validación individual. |

---

## 8. Entregables H3

| Entregable | Responsable | Formato | Plantilla local |
|---|---|---|---|
| Código con memoria temporal | Equipo/individual | `src/Main.java` | No aplica. |
| README H3 | Equipo/individual | `README.md` | `plantillas/README-h3-plantilla.md` |
| Evidencia de ejecución | Equipo/individual | `docs/evidencia-ejecucion-h3.md` | `plantillas/evidencia-ejecucion-h3-plantilla.md` |
| Pruebas de memoria | Equipo | `docs/pruebas-memoria-h3.md` | `plantillas/pruebas-memoria-h3-plantilla.md` |
| Justificación de colección | Individual/equipo | `docs/justificacion-coleccion-h3.md` | `plantillas/justificacion-coleccion-h3-plantilla.md` |
| Incidencia | Si procede | `docs/incidencia-h3.md` | `plantillas/incidencia-h3-plantilla.md` |
| Comparación Java ↔ Python | Individual | `docs/comparacion-java-python-h3.md` | `plantillas/comparacion-java-python-h3-plantilla.md` |
| Portfolio H3 | Individual | `docs/portfolio-h3.md` | `plantillas/portfolio-h3-plantilla.md` |
| Registro IA | Individual/equipo | `docs/registro-ia.md` | `plantillas/registro-ia-h3-plantilla.md` |
| Defensa H3 | Individual | `docs/defensa-h3.md` | `plantillas/defensa-h3-plantilla.md` |

---

## 9. Uso de IA en H3

Permitido:

- entender diferencias entre `ArrayList` y `HashMap`;
- pedir ejemplos pequeños de recorrido;
- pedir casos de prueba para memoria;
- comparar Java con Python;
- entender errores de índices o memoria vacía.

No permitido:

- generar una solución completa no defendible;
- añadir persistencia, bases de datos o IA real;
- usar estructuras que no se pueden explicar.

---

## 10. Errores previsibles

| Error | Señal | Intervención docente |
|---|---|---|
| Elige colección sin criterio | No sabe justificar | Preguntar qué necesita: orden, clave, búsqueda. |
| Memoria vacía no gestionada | Salida confusa | Añadir caso límite. |
| Entrada vacía guardada | Recuerdos vacíos | Validar texto antes de guardar. |
| Índices confusos | Muestra mal numeración | Separar índice interno de número visible. |
| Añade ficheros | Se adelanta a H6 | Reencuadrar: H3 es memoria temporal. |

---

## 11. Preparación para C1/H4

Antes de cerrar H3, comprobar:

- si el alumnado entiende qué colección usa;
- si puede guardar y consultar memoria;
- si gestiona memoria vacía;
- si puede probar casos límite;
- si puede explicar diferencias con Python.

H4 rediseñará el agente con clases propias.

## Cobertura curricular de Programación

Este hito queda alineado con el mapa `32-lista-conceptos-programacion-por-tema.md`.

```text
Hito: H3
Temas de referencia: Tema 4
Foco: memoria temporal con estructuras de datos
```

Conceptos que deben trabajarse o, como mínimo, quedar conectados con evidencias del alumnado:

- colección
- genéricos
- List
- ArrayList
- índice
- recorrido
- for mejorado
- mutabilidad
- inmutabilidad
- clases envoltorio
- array
- tabla como ampliación
- Set para evitar repetidos
- Map para preferencias por clave

Criterio docente de cierre:

- El alumnado no solo entrega el producto; debe poder señalar dónde aparece cada concepto en su código, README, pruebas o defensa.
- Si un concepto se marca como ampliación, no penaliza al alumnado que alcance el mínimo, pero sí orienta mejora, recuperación o enriquecimiento.
- La defensa debe incluir al menos una pregunta de comprensión sobre los conceptos nuevos del hito.

