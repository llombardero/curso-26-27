# Checklist de corrección — H3 Agente con memoria en colecciones

<!-- HEXA-CICLO-COMPLETO-POR-HITO:START -->

## Ciclo HEXA obligatorio del reto H3

**Reto del hito:** Añadir memoria temporal mediante una colección adecuada y demostrar su comportamiento y límites.

La corrección debe comprobar las cuatro fases por separado. La ausencia de una fase genera una evidencia incompleta que debe recuperarse.

| Fase | Pregunta que guía la fase | Acción del profesorado | Acción y evidencia del alumnado |
|---|---|---|---|
| **H — Hecho / reto** | ¿Qué problema real debemos resolver y con qué límites? | Presenta contexto, producto, restricciones, criterios y diagnóstico; no da todavía la solución completa. | Reformula el reto, identifica lo que sabe/no sabe y deja una ficha inicial con criterios de éxito. |
| **E — Exploración** | ¿Qué alternativas, hipótesis o pruebas iniciales ayudan a entenderlo? | Propone preguntas, ejemplos mínimos, casos y límites seguros. | Observa, compara, predice, prueba alternativas y registra decisiones o bloqueos. |
| **X — eXplicación** | ¿Qué conceptos permiten explicar lo observado y decidir con criterio? | Formaliza vocabulario, sintaxis, modelo mental, errores frecuentes, seguridad y criterios de calidad. | Explica con palabras propias, conecta teoría y exploración y corrige sus hipótesis. |
| **A — Aplicación** | ¿Cómo construimos, comprobamos, documentamos y defendemos la solución? | Desbloquea, exige pruebas y comprueba autoría y transferencia. | Implementa el producto, lo prueba, documenta evidencias, realiza review/defensa y propone mejora. |

### Temporalización mínima explícita

H3-S1–S10; 450 min mínimos en la guía autónoma. Los tiempos de fases se reservan dentro de las sesiones indicadas; los rangos pueden solaparse cuando una sesión cierra una fase y abre la siguiente.

| Fase | Reserva y momento recomendado | Puerta de salida |
|---|---|---|
| H | H3-S1; 45 min | Reto reformulado, límites y criterio de éxito visibles. |
| E | H3-S1–S2; 90 min integrados | Hipótesis, comparación, prueba inicial o decisiones justificadas. |
| X | H3-S3–S6; 135 min integrados | Explicación individual breve y conexión con el producto. |
| A | H3-S7–S10; 180 min integrados | Producto comprobado, documentación, defensa y mejora. |

**Expediente HEXA mínimo del hito:** requisitos de memoria, comparación de alternativas, explicación de ArrayList/casos límite, código, pruebas y defensa.

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

## 1. Mínimos técnicos

| Ítem | Sí | Parcial | No | Observaciones |
|---|---|---|---|---|
| Existe `src/Main.java` | | | | |
| El programa se ejecuta | | | | |
| Mantiene menú H2 | | | | |
| Usa colección Java | | | | |
| Guarda información en memoria temporal | | | | |
| Permite consultar memoria | | | | |
| Gestiona memoria vacía | | | | |
| No usa persistencia fuera de H3 | | | | |

---

## 2. Colección y casos límite

| Ítem | Sí | Parcial | No | Observaciones |
|---|---|---|---|---|
| Justifica colección elegida | | | | |
| Recorre o consulta la colección | | | | |
| Gestiona entrada vacía | | | | |
| Gestiona repetidos o los explica | | | | |
| Casos límite documentados | | | | |

---

## 3. Pruebas y documentación

| Ítem | Sí | Parcial | No | Observaciones |
|---|---|---|---|---|
| README actualizado | | | | |
| Pruebas de memoria | | | | |
| Evidencia de ejecución | | | | |
| Incidencia si procede | | | | |
| Comparación Java ↔ Python | | | | |
| Portfolio H3 | | | | |

---

## 4. Defensa

| Pregunta | Adecuada | Dudas | No responde | Observaciones |
|---|---|---|---|---|
| ¿Qué colección has usado? | | | | |
| ¿Por qué esa colección? | | | | |
| ¿Cómo guardas un dato? | | | | |
| ¿Cómo muestras la memoria? | | | | |
| ¿Qué pasa si está vacía? | | | | |
| ¿Qué cambia con Python? | | | | |

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

