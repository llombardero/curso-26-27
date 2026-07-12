# Checklist de corrección — H5 Agente extensible, clean code y patrones iniciales

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

