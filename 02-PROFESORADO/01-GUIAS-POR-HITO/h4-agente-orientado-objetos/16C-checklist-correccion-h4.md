# Checklist de corrección — H4 Agente orientado a objetos

<!-- HEXA-CICLO-COMPLETO-POR-HITO:START -->

## Ciclo HEXA obligatorio del reto H4

**Reto del hito:** Reorganizar MiniJarvis con orientación a objetos y responsabilidades que coincidan con el código y los diagramas.

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
| 1 — Activar | S242 | Reto comprendido y criterios visibles. |
| 2 — Investigar | S243–S246 | Conocimientos necesarios contrastados. |
| 3 — Idear | S247 | Solución seleccionada y argumentada. |
| 4 — Planificar | S248 | Plan, responsabilidades y comprobaciones visibles. |
| 5 — Ejecutar | S249–S253 | Producto construido, probado y mejorado. |
| 6 — Comunicar | S254–S257 | Defensa, evaluación, reflexión y mejora. |

**Expediente HEXA mínimo del hito:** diagnóstico de Main, alternativas de reparto, explicación POO/encapsulación, clases, diagramas, relación diagrama-código y defensa.

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

## 1. Código OO

| Ítem | Sí | Parcial | No | Observaciones |
|---|---|---|---|---|
| Hay varias clases propias | | | | |
| `Main` delega lógica | | | | |
| Hay clase tipo `Agent` | | | | |
| Hay clase tipo `Memory` | | | | |
| Atributos privados | | | | |
| Constructores coherentes | | | | |
| Métodos con responsabilidad clara | | | | |

---

## 2. Diagramas

| Ítem | Sí | Parcial | No | Observaciones |
|---|---|---|---|---|
| Diagrama de clases | | | | |
| Diagrama de comportamiento | | | | |
| Diagramas coinciden con código | | | | |
| Relación diagrama-código documentada | | | | |

---

## 3. Defensa

| Pregunta | Adecuada | Dudas | No responde | Observaciones |
|---|---|---|---|---|
| Responsabilidad de `Agent` | | | | |
| Responsabilidad de `Memory` | | | | |
| Encapsulación | | | | |
| Relación del diagrama | | | | |
| Comparación con Python | | | | |

---

## 4. Decisión docente

```text
[ ] Evidencia válida.
[ ] Válida con mejoras menores.
[ ] Necesita recuperación parcial.
[ ] No válida todavía.
```

## Cobertura curricular de Programación

Este hito queda alineado con el mapa `32-lista-conceptos-programacion-por-tema.md`.

```text
Hito: H4
Temas de referencia: Temas 2 y 5
Foco: orientación a objetos y separación de responsabilidades
```

Conceptos que deben trabajarse o, como mínimo, quedar conectados con evidencias del alumnado:

- clase
- objeto
- atributo
- método
- constructor
- referencia
- estado
- comportamiento
- responsabilidad
- private/public
- this
- diagrama de clases
- diagrama de comportamiento
- Javadoc como ampliación
- excepción básica

Criterio docente de cierre:

- El alumnado no solo entrega el producto; debe poder señalar dónde aparece cada concepto en su código, README, pruebas o defensa.
- Si un concepto se marca como ampliación, no penaliza al alumnado que alcance el mínimo, pero sí orienta mejora, recuperación o enriquecimiento.
- La defensa debe incluir al menos una pregunta de comprensión sobre los conceptos nuevos del hito.

