# H5 — Agente extensible, clean code y patrones iniciales

Paquete específico del hito H5.

Objetivo:

```text
Convertir MiniJarvis en un agente más extensible mediante herramientas/comandos internos, refactorización documentada, revisión de código y decisión razonada sobre patrones.
```

Documentos principales:

```text
17-guia-docente-h5-extensible-clean-code-patrones.md
17B-ficha-alumnado-h5-extensible-clean-code-patrones.md
17C-checklist-correccion-h5.md
```

Plantillas locales:

```text
plantillas/README-h5-template.md
plantillas/informe-refactorizacion-h5-template.md
plantillas/evidencia-git-h5-template.md
plantillas/revision-codigo-h5-template.md
plantillas/registro-patron-h5-template.md
plantillas/comparacion-java-python-h5-template.md
plantillas/portfolio-h5-template.md
plantillas/registro-ia-h5-template.md
plantillas/defensa-h5-template.md
```

Restricción didáctica clave:

```text
H5 introduce extensibilidad y refactorización. Un patrón solo se usa si resuelve un problema real y se puede defender. No se debe forzar arquitectura compleja, plugins reales, persistencia ni IA real.
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
- @Override
- toString
- Comparable o Comparator como ampliación guiada
- herencia, super, protected y clase abstracta como comparación técnica
- clean code
- refactorización segura

Refuerzo obligatorio de cobertura:

```text
H5 debe incluir un laboratorio de POO avanzada: enum, record opcional, @Override, toString y comparación entre interface Tool y una posible clase abstracta BaseTool.
No es obligatorio mantener herencia en el diseño final si la defensa justifica que interfaz/composición es más simple.
```

Criterio docente de cierre:

- El alumnado no solo entrega el producto; debe poder señalar dónde aparece cada concepto en su código, README, pruebas o defensa.
- Si un concepto se marca como ampliación, no penaliza al alumnado que alcance el mínimo, pero sí orienta mejora, recuperación o enriquecimiento.
- La defensa debe incluir al menos una pregunta de comprensión sobre los conceptos nuevos del hito.
