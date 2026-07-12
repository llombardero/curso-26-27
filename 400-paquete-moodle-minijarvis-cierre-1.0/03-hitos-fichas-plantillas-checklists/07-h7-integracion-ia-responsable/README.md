# H7 — Integración IA responsable o simulación robusta

Paquete específico del hito H7.

Objetivo:

```text
Preparar una integración IA responsable real o simulada, con caso de uso limitado, validación humana, registro de prompts, riesgos y configuración segura.
```

Documentos principales:

```text
19-guia-docente-h7-integracion-ia-responsable.md
19B-ficha-alumnado-h7-integracion-ia-responsable.md
19C-checklist-correccion-h7.md
```

Plantillas locales:

```text
plantillas/README-h7-template.md
plantillas/registro-prompts-h7-template.md
plantillas/riesgos-ia-h7-template.md
plantillas/configuracion-segura-h7-template.md
plantillas/validacion-humana-h7-template.md
plantillas/comparacion-java-python-h7-template.md
plantillas/portfolio-h7-template.md
plantillas/defensa-h7-template.md
```

Restricción didáctica clave:

```text
H7 puede ser simulación robusta. No se deben usar secretos reales, datos personales reales ni llamadas externas no controladas. La IA no sustituye la defensa técnica.
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

