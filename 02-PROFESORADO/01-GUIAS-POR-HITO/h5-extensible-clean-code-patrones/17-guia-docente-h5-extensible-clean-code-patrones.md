# Guía docente — H5 Agente extensible, clean code y patrones iniciales

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

<!-- HEXA-CICLO-COMPLETO-POR-HITO:END -->

## Programación — 1.º DAW — Curso 2026/2027

Edición final para Moodle — septiembre de 2026

Documentos relacionados:

- `../../02-calendario-hitos-sprints-2026-2027.md`
- `../../04A-enunciados-y-entregables-alumnado.md`
- `../../06-rubricas-hitos.md`
- `README.md`
- `17B-ficha-alumnado-h5-extensible-clean-code-patrones.md`
- `17C-checklist-correccion-h5.md`

---

## 1. Propósito del hito

H5 convierte MiniJarvis en un agente más extensible y mantenible.

Producto esperado:

```text
MiniJarvis H5: agente con herramientas internas extensibles, refactorización documentada, revisión de código y decisión razonada sobre patrón de diseño.
```

El objetivo no es usar patrones por usarlos, sino detectar un problema real del código y mejorar la estructura.

---

## 2. Qué añade H5 respecto a H4

| H4 | H5 |
|---|---|
| Clases principales `Agent` y `Memory`. | Herramientas/comandos separables. |
| Diseño OO inicial. | Extensibilidad y bajo impacto al añadir comandos. |
| Diagramas de diseño. | Refactorización antes/después. |
| Defensa de responsabilidades. | Defensa de decisión de patrón o no patrón. |

---

## 3. Restricciones didácticas

En H5 sí debe aparecer:

- refactorización justificada;
- herramienta/comando interno nuevo;
- evidencia de Git o registro equivalente;
- revisión de código;
- decisión razonada sobre patrón;
- comparación Java ↔ Python.

En H5 NO debe forzarse:

- sistema real de plugins;
- arquitectura hexagonal;
- framework externo;
- persistencia;
- IA real;
- patrones múltiples sin necesidad.

---

## 4. Fechas y duración

Fechas orientativas:

```text
8 febrero - 19 marzo 2027
```

---

## 5. RA/CE y evidencias

### Programación

- PR RA7, no imprescindible pero evaluable.
- Refuerzo PR RA4 y PR RA6.

Evidencias:

- comandos/herramientas separables;
- nombres claros;
- responsabilidades mejoradas;
- capacidad de añadir una herramienta con bajo impacto.

### Prácticas técnicas del proyecto

- control de versiones, refactorización y automatización: refactorización, análisis de código y pruebas asociadas.
- control de versiones, refactorización y automatización: control de versiones, documentación y repositorios remotos.
- control de versiones, refactorización y automatización: integración continua si el nivel lo permite.
- diagramas de comportamiento si se usan diagramas de comportamiento/estado.

Evidencias:

- informe antes/después;
- evidencia de rama, commits, PR o revisión;
- revisión de código;
- registro de patrón si se usa.

---

## 6. Diseño mínimo recomendado

Solución didáctica recomendada:

```text
Separar cada herramienta/comando en una clase sencilla con una responsabilidad clara.
```

Clases posibles:

| Clase/interfaz | Responsabilidad |
|---|---|
| `Tool` | Contrato común para herramientas. |
| `HelpTool` | Mostrar comandos. |
| `GreetTool` | Saludar. |
| `RememberTool` | Guardar recuerdos. |
| `MemoryTool` | Mostrar memoria. |
| `StatusTool` | Mostrar estado. |
| `Agent` | Orquestar ejecución y delegar en herramientas. |
| `Memory` | Gestionar recuerdos. |

Patrón posible:

```text
Command simplificado: cada comando se representa como una herramienta con nombre y método execute.
```

Importante:

```text
Si el grupo no está preparado, se puede hablar de “herramientas/comandos separables” sin exigir terminología formal de patrón.
```

### Laboratorio técnico de cobertura Tema 6

Para que el Tema 6 no quede reducido solo a interfaces y Command, H5 incluye un laboratorio breve, evaluable por evidencia pero no necesariamente incorporado completo al producto final. Debe trabajar:

- comparación entre interfaz, clase abstracta, herencia y composición;
- `@Override`, `toString`, `equals` y `hashCode` en ejemplos pequeños;
- `Comparable`/`compareTo` o `Comparator` para ordenar herramientas o comandos;
- `instanceof` como contraste frente a una solución polimórfica;
- `protected`, `super` y package-private dentro de un ejemplo controlado;
- métodos `default` y métodos privados en interfaces como lectura o microejemplo;
- clases anónimas, clases finales y clases selladas solo como reconocimiento/ampliación si no aportan al diseño.

La decisión docente clave es esta: se trabajan los conceptos para poder reconocerlos y defenderlos, pero solo se integran en MiniJarvis si simplifican el diseño.

---

## 7. Entregables H5

| Entregable | Responsable | Formato | Plantilla local |
|---|---|---|---|
| Código extensible | Equipo/individual | `src/*.java` | No aplica. |
| README H5 | Equipo/individual | `README.md` | `plantillas/README-h5-plantilla.md` |
| Informe de refactorización | Equipo | `docs/informe-refactorizacion-h5.md` | `plantillas/informe-refactorizacion-h5-plantilla.md` |
| Evidencia Git/revisión | Equipo | `docs/evidencia-git-h5.md` | `plantillas/evidencia-git-h5-plantilla.md` |
| Revisión de código | Equipo | `docs/revision-codigo-h5.md` | `plantillas/revision-codigo-h5-plantilla.md` |
| Registro de patrón | Equipo | `docs/registro-patron-h5.md` | `plantillas/registro-patron-h5-plantilla.md` |
| Comparación Java ↔ Python | Individual | `docs/comparacion-java-python-h5.md` | `plantillas/comparacion-java-python-h5-plantilla.md` |
| Portfolio H5 | Individual | `docs/portfolio-h5.md` | `plantillas/portfolio-h5-plantilla.md` |
| Registro IA | Individual/equipo | `docs/registro-ia.md` | `plantillas/registro-ia-h5-plantilla.md` |
| Defensa H5 | Individual | `docs/defensa-h5.md` | `plantillas/defensa-h5-plantilla.md` |

---

## 8. Errores previsibles

| Error | Señal | Intervención docente |
|---|---|---|
| Patrón forzado | No sabe explicar problema | Pedir alternativa simple y motivo. |
| Refactorización cosmética | Solo cambia nombres | Exigir antes/después con impacto. |
| Git simulado sin trazabilidad | No hay commits/revisión | Aceptar registro equivalente si no hay GitHub, pero claro. |
| Herramientas acopladas | Añadir comando toca muchas clases | Preguntar “¿qué tendría que cambiar para añadir otra herramienta?”. |
| Código demasiado avanzado | No lo defiende | Reducir a interfaz/clase simple. |

---

## 9. Preparación para H6

Antes de pasar a H6, comprobar:

- si añadir una herramienta nueva es sencillo;
- si hay evidencia de refactorización real;
- si Git/revisión está documentado;
- si el patrón se usa o descarta con criterio;
- si el código sigue siendo entendible.

H6 introducirá persistencia, trazabilidad, reproducibilidad y seguridad básica.

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
- excepciones
- recursividad como comparación
- métodos estáticos
- records como ampliación
- enum
- polimorfismo por interfaz
- Command simplificado
- clean code
- refactorización segura

Criterio docente de cierre:

- El alumnado no solo entrega el producto; debe poder señalar dónde aparece cada concepto en su código, README, pruebas o defensa.
- Si un concepto se marca como ampliación, no penaliza al alumnado que alcance el mínimo, pero sí orienta mejora, recuperación o enriquecimiento.
- La defensa debe incluir al menos una pregunta de comprensión sobre los conceptos nuevos del hito.

