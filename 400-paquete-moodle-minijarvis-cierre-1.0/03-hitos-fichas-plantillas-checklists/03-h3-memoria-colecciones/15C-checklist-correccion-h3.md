# Checklist de corrección — H3 Agente con memoria en colecciones

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

