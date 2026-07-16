# H3 — Agente con memoria en colecciones

Paquete específico del hito H3.

Objetivo:

```text
Añadir memoria temporal a MiniJarvis usando colecciones Java y documentar pruebas, casos límite y justificación de la estructura elegida.
```

Documentos principales:

```text
15-guia-docente-h3-memoria-colecciones.md
15B-ficha-alumnado-h3-memoria-colecciones.md
15C-checklist-correccion-h3.md
```

Plantillas locales:

```text
plantillas/README-h3-template.md
plantillas/evidencia-ejecucion-h3-template.md
plantillas/pruebas-memoria-h3-template.md
plantillas/justificacion-coleccion-h3-template.md
plantillas/incidencia-h3-template.md
plantillas/comparacion-java-python-h3-template.md
plantillas/portfolio-h3-template.md
plantillas/registro-ia-h3-template.md
plantillas/defensa-h3-template.md
```

Restricción didáctica clave:

```text
H3 introduce memoria temporal con colecciones. Todavía no debe introducir persistencia en ficheros, bases de datos, arquitectura OO completa, patrones de diseño ni IA real.
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

Refuerzo obligatorio de cobertura:

```text
La defensa H3 debe incluir una comparación array vs ArrayList y una decisión explícita sobre Set para recuerdos repetidos.
Map puede trabajarse como preferencias por clave o como mini-reto separado.
```

Criterio docente de cierre:

- El alumnado no solo entrega el producto; debe poder señalar dónde aparece cada concepto en su código, README, pruebas o defensa.
- Si un concepto se marca como ampliación, no penaliza al alumnado que alcance el mínimo, pero sí orienta mejora, recuperación o enriquecimiento.
- La defensa debe incluir al menos una pregunta de comprensión sobre los conceptos nuevos del hito.
