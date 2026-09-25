# Checklist de corrección — H2 Agente con decisiones y depuración

<!-- HEXA-CICLO-COMPLETO-POR-HITO:START -->

## Ciclo HEXA obligatorio del reto H2

**Reto del hito:** Transformar MiniJarvis en un programa interactivo con decisiones, repetición y depuración reproducible.

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
| 1 — Activar | S216 | Reto comprendido y criterios visibles. |
| 2 — Investigar | S217–S221 | Conocimientos necesarios contrastados. |
| 3 — Idear | S222 | Solución seleccionada y argumentada. |
| 4 — Planificar | S223 | Plan, responsabilidades y comprobaciones visibles. |
| 5 — Ejecutar | S224–S226 | Producto construido, probado y mejorado. |
| 6 — Comunicar | S227–S228 | Defensa, evaluación, reflexión y mejora. |

**Expediente HEXA mínimo del hito:** mapa de comandos, hipótesis de flujo, explicación de condiciones/bucle, menú funcional, pruebas, depuración y defensa.

Regla de avance: puede haber prototipos durante Investigar o Idear, pero Ejecutar no se considera completada si faltan evidencias de Activar, Investigar, Idear o Planificar. Comunicar exige presentar, evaluar y reflexionar. Si falta una fase, se recuperan esa fase y su evidencia; no se repite automáticamente todo el hito.

### Lista de comprobación del ciclo

| Fase | Sí | Parcial | No | Evidencia observada / recuperación |
|---|---|---|---|---|
| 1 — Activar: reto, propósito, límites y criterios comprendidos | | | | |
| 2 — Investigar: conocimientos necesarios buscados, contrastados o explicados | | | | |
| 3 — Idear: alternativas generadas y solución elegida con criterio | | | | |
| 4 — Planificar: tareas, tiempos, responsabilidades y comprobaciones visibles | | | | |
| 5 — Ejecutar: producto construido, probado y mejorado | | | | |
| 6 — Comunicar: producto presentado, proceso evaluado y aprendizaje reflexionado | | | | |

<!-- HEXA-CICLO-COMPLETO-POR-HITO:END -->

Documento para uso docente.

Relacionado con:

- `14-guia-docente-h2-decisiones-depuracion.md`
- `14B-ficha-alumnado-h2-decisiones-depuracion.md`
- `../../06-rubricas-hitos.md`

---

## 1. Datos de la entrega

Alumno/a o equipo:

```text

```

Repositorio o ubicación:

```text

```

---

## 2. Mínimos técnicos

| Ítem | Sí | Parcial | No | Observaciones |
|---|---|---|---|---|
| Existe `src/Main.java` | | | | |
| El programa se ejecuta | | | | |
| Hay menú o prompt de comandos | | | | |
| El programa se repite hasta `salir` | | | | |
| Implementa `ayuda` | | | | |
| Implementa `saluda` | | | | |
| Implementa `estado` | | | | |
| Implementa `salir` | | | | |
| Gestiona comando desconocido | | | | |

---

## 3. Control de flujo

| Ítem | Sí | Parcial | No | Observaciones |
|---|---|---|---|---|
| Usa bucle correctamente | | | | |
| Usa `if/else` o `switch` de forma comprensible | | | | |
| Compara texto correctamente (`equals` o equivalente) | | | | |
| La salida del programa está controlada | | | | |
| No introduce complejidad fuera de H2 | | | | |

---

## 4. Pruebas y depuración integradas

| Ítem | Sí | Parcial | No | Observaciones |
|---|---|---|---|---|
| Incluye `docs/pruebas-h2.md` | | | | |
| Prueba comandos principales | | | | |
| Incluye esperado/obtenido | | | | |
| Incluye `docs/depuracion-h2.md` | | | | |
| Usa breakpoint | | | | |
| Observa al menos una variable | | | | |
| Documenta incidencia si apareció | | | | |

---

## 5. Comparación Java ↔ Python

| Ítem | Sí | Parcial | No | Observaciones |
|---|---|---|---|---|
| Incluye comparación | | | | |
| Compara bucle | | | | |
| Compara decisiones | | | | |
| Compara entrada de usuario | | | | |
| Explica diferencias con comprensión | | | | |

---

## 6. Uso de IA

| Ítem | Sí | Parcial | No / N.A. | Observaciones |
|---|---|---|---|---|
| Declara uso de IA | | | | |
| Registra prompts relevantes | | | | |
| Verifica lo aceptado | | | | |
| Puede defender código asistido | | | | |
| No hay uso oculto evidente | | | | |

---

## 7. Preguntas de defensa

| Pregunta | Adecuada | Dudas | No responde | Observaciones |
|---|---|---|---|---|
| ¿Cómo se repite el menú? | | | | |
| ¿Qué hace `salir`? | | | | |
| ¿Qué ocurre con comando desconocido? | | | | |
| ¿Dónde pusiste el breakpoint? | | | | |
| ¿Qué variable observaste? | | | | |
| ¿Qué prueba detectó un fallo? | | | | |
| ¿Qué diferencia viste con Python? | | | | |

---

## 8. Decisión docente

```text
[ ] Evidencia válida.
[ ] Válida con mejoras menores.
[ ] Necesita recuperación parcial.
[ ] No válida todavía.
```

Mejoras solicitadas:

```text

```

## Cobertura curricular de Programación

Este hito queda alineado con el mapa `32-lista-conceptos-programacion-por-tema.md`.

```text
Hito: H2
Temas de referencia: Temas 1 y 3
Foco: decisiones, menú, repetición y depuración
```

Conceptos que deben trabajarse o, como mínimo, quedar conectados con evidencias del alumnado:

- if/else
- boolean
- comparaciones
- switch
- enhanced switch como ampliación
- while
- do-while como comparación
- for
- condición de salida
- bucle infinito
- pruebas manuales
- error de compilación
- error lógico
- eficiencia básica

Criterio docente de cierre:

- El alumnado no solo entrega el producto; debe poder señalar dónde aparece cada concepto en su código, README, pruebas o defensa.
- Si un concepto se marca como ampliación, no penaliza al alumnado que alcance el mínimo, pero sí orienta mejora, recuperación o enriquecimiento.
- La defensa debe incluir al menos una pregunta de comprensión sobre los conceptos nuevos del hito.

