# Checklist de corrección — H5 Agente extensible, clean code y patrones iniciales

<!-- HEXA-CICLO-COMPLETO-POR-HITO:START -->

## Ciclo HEXA obligatorio del reto H5

**Reto del hito:** Resolver el crecimiento de comandos mediante refactorización segura, contratos simples y código extensible.

La corrección debe comprobar las cuatro fases por separado. La ausencia de una fase genera una evidencia incompleta que debe recuperarse.

| Fase | Pregunta que guía la fase | Acción del profesorado | Acción y evidencia del alumnado |
|---|---|---|---|
| **H — Hecho / reto** | ¿Qué problema real debemos resolver y con qué límites? | Presenta contexto, producto, restricciones, criterios y diagnóstico; no da todavía la solución completa. | Reformula el reto, identifica lo que sabe/no sabe y deja una ficha inicial con criterios de éxito. |
| **E — Exploración** | ¿Qué alternativas, hipótesis o pruebas iniciales ayudan a entenderlo? | Propone preguntas, ejemplos mínimos, casos y límites seguros. | Observa, compara, predice, prueba alternativas y registra decisiones o bloqueos. |
| **X — eXplicación** | ¿Qué conceptos permiten explicar lo observado y decidir con criterio? | Formaliza vocabulario, sintaxis, modelo mental, errores frecuentes, seguridad y criterios de calidad. | Explica con palabras propias, conecta teoría y exploración y corrige sus hipótesis. |
| **A — Aplicación** | ¿Cómo construimos, comprobamos, documentamos y defendemos la solución? | Desbloquea, exige pruebas y comprueba autoría y transferencia. | Implementa el producto, lo prueba, documenta evidencias, realiza review/defensa y propone mejora. |

### Temporalización mínima explícita

H5-S1–S10; 450 min mínimos en la guía autónoma. Los tiempos de fases se reservan dentro de las sesiones indicadas; los rangos pueden solaparse cuando una sesión cierra una fase y abre la siguiente.

| Fase | Reserva y momento recomendado | Puerta de salida |
|---|---|---|
| H | H5-S1; 45 min | Reto reformulado, límites y criterio de éxito visibles. |
| E | H5-S1–S3; 90 min integrados | Hipótesis, comparación, prueba inicial o decisiones justificadas. |
| X | H5-S2–S4; 135 min integrados | Explicación individual breve y conexión con el producto. |
| A | H5-S3–S10; 180 min integrados | Producto comprobado, documentación, defensa y mejora. |

**Expediente HEXA mínimo del hito:** diagnóstico del problema, comparación de diseños, explicación de interfaz/Command, refactorización, herramienta nueva, revisión Git y defensa.

Regla de avance: puede haber prototipos durante E, pero no se considera completada A si faltan evidencias de H, E o X. Si una fase falta, se recupera esa fase y su evidencia; no se repite automáticamente todo el hito.

### Lista de comprobación del ciclo

| Fase | Sí | Parcial | No | Evidencia observada / recuperación |
|---|---|---|---|---|
| H — Está formulado el reto, producto, límites y criterio de éxito | | | | |
| E — Hay preguntas, hipótesis, comparación o pruebas iniciales | | | | |
| X — El alumnado explica conceptos y decisiones con vocabulario preciso | | | | |
| A — El producto se construye, prueba, documenta y defiende | | | | |

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

<!-- AJUSTE-COBERTURA-CONCEPTOS-32 -->

## Ajuste curricular — cobertura de conceptos de Programación

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

