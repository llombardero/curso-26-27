# Checklist de corrección — H7 Integración IA responsable o simulación robusta

Documento para uso docente.

---

## 1. Funcionalidad IA

| Ítem | Sí | Parcial | No | Observaciones |
|---|---|---|---|---|
| Caso de uso concreto | | | | |
| Integración o simulación funciona | | | | |
| Entrada controlada | | | | |
| Respuesta limitada | | | | |
| No rompe el proyecto | | | | |

---

## 2. Seguridad y validación

| Ítem | Sí | Parcial | No | Observaciones |
|---|---|---|---|---|
| No hay secretos | | | | |
| No hay `.env` real | | | | |
| No hay datos personales reales | | | | |
| Hay validación humana | | | | |
| Hay documento de riesgos | | | | |

---

## 3. Defensa

| Pregunta | Adecuada | Dudas | No responde | Observaciones |
|---|---|---|---|---|
| Qué datos recibe la IA | | | | |
| Qué no debe recibir | | | | |
| Cómo valida respuestas | | | | |
| Qué límites tiene | | | | |

---

## 4. Decisión docente

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
Hito: H7
Temas de referencia: Temas 5, 6 y 7
Foco: IA responsable, abstracción y mejora funcional opcional
```

Conceptos que deben trabajarse o, como mínimo, quedar conectados con evidencias del alumnado:

- record AiResponse
- enum para niveles de riesgo
- interfaz AiAssistant como ampliación
- polimorfismo
- Strategy como patrón opcional
- Optional para respuesta bloqueada o ausente
- lambdas como ampliación
- streams para analizar registros
- funciones puras en PromptSafety
- validación humana

Criterio docente de cierre:

- El alumnado no solo entrega el producto; debe poder señalar dónde aparece cada concepto en su código, README, pruebas o defensa.
- Si un concepto se marca como ampliación, no penaliza al alumnado que alcance el mínimo, pero sí orienta mejora, recuperación o enriquecimiento.
- La defensa debe incluir al menos una pregunta de comprensión sobre los conceptos nuevos del hito.

