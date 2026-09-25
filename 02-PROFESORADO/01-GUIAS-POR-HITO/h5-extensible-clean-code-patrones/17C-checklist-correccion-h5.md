# Checklist de corrección — H5 Agente extensible, clean code y patrones iniciales

<!-- HEXA-CICLO-COMPLETO-POR-HITO:START -->

## Ciclo HEXA obligatorio del reto H5

**Reto del hito:** Resolver el crecimiento de comandos mediante refactorización segura, contratos simples y código extensible.

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
| 1 — Activar | S258 | Reto comprendido y criterios visibles. |
| 2 — Investigar | S259–S260 | Conocimientos necesarios contrastados. |
| 3 — Idear | S261 | Solución seleccionada y argumentada. |
| 4 — Planificar | S262 | Plan, responsabilidades y comprobaciones visibles. |
| 5 — Ejecutar | S263–S271 | Producto construido, probado y mejorado. |
| 6 — Comunicar | S270 y S272–S274 | Defensa, evaluación, reflexión y mejora. |

**Expediente HEXA mínimo del hito:** diagnóstico del problema, comparación de diseños, explicación de interfaz/Command, refactorización, herramienta nueva, revisión Git y defensa.

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

---

## 1. Extensibilidad y código

| Ítem | Sí | Parcial | No | Observaciones |
|---|---|---|---|---|
| Código compila y ejecuta | | | | |
| Hay herramientas/comandos separados | | | | |
| Añadir un comando tiene bajo impacto | | | | |
| Nombres claros | | | | |
| Responsabilidades mejoradas | | | | |
| No hay complejidad gratuita | | | | |

---

## 2. Refactorización y Git

| Ítem | Sí | Parcial | No | Observaciones |
|---|---|---|---|---|
| Informe antes/después | | | | |
| Motivo de refactorización claro | | | | |
| Evidencia de rama/commits/PR o equivalente | | | | |
| Revisión de código documentada | | | | |
| Cambios verificables | | | | |

---

## 3. Patrón o decisión de diseño

| Ítem | Sí | Parcial | No | Observaciones |
|---|---|---|---|---|
| Identifica problema real | | | | |
| Usa o descarta patrón con criterio | | | | |
| Explica alternativa simple | | | | |
| Puede defender la decisión | | | | |

---

## 4. Defensa

| Pregunta | Adecuada | Dudas | No responde | Observaciones |
|---|---|---|---|---|
| Problema antes de refactorizar | | | | |
| Cambio realizado | | | | |
| Añadir nueva herramienta | | | | |
| Evidencia Git/revisión | | | | |
| Comparación con Python | | | | |

---

## 5. Decisión docente

```text
[ ] Evidencia válida.
[ ] Válida con mejoras menores.
[ ] Necesita recuperación parcial.
[ ] No válida todavía.
```

## Cobertura curricular de Programación

Este hito queda alineado con el mapa `32-lista-conceptos-programacion-por-tema.md`.

```text
Hito: H5
Temas de referencia: Temas 5 y 6
Foco: interfaces, extensibilidad, pruebas y primer patrón
```

Conceptos que deben trabajarse o, como mínimo, quedar conectados con evidencias del alumnado:

- test unitario
- aserto
- TDD
- interfaz
- implementación
- método default como ampliación
- métodos privados en interfaces como lectura guiada
- excepciones
- recursividad como comparación
- métodos estáticos
- records como ampliación
- enum
- `equals`, `hashCode`, `toString` y `@Override`
- `instanceof` como contraste frente a polimorfismo
- `Comparable` / `compareTo` o `Comparator` para ordenación sencilla
- herencia, clase abstracta, `super`, `protected` y package-private como laboratorio comparativo
- clases anónimas, clases finales y clases selladas como reconocimiento/ampliación
- polimorfismo por interfaz
- Command simplificado
- clean code
- refactorización segura

Criterio docente de cierre:

- El alumnado no solo entrega el producto; debe poder señalar dónde aparece cada concepto en su código, README, pruebas o defensa.
- Si un concepto se marca como ampliación, no penaliza al alumnado que alcance el mínimo, pero sí orienta mejora, recuperación o enriquecimiento.
- La defensa debe incluir al menos una pregunta de comprensión sobre los conceptos nuevos del hito.

