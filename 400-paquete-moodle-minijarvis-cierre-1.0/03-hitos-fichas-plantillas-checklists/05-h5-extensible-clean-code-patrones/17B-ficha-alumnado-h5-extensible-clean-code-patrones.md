# H5 — Agente extensible, clean code y patrones iniciales

## Ficha para el alumnado

---

## 1. Reto

Vais a mejorar MiniJarvis para que sea más fácil añadir herramientas o comandos nuevos.

No se trata de hacer el código “más complicado”, sino más claro, mantenible y fácil de ampliar.

---

## 2. Qué debe tener H5

```text
[x] Herramientas o comandos internos separados.
[x] Refactorización explicada.
[x] Evidencia de Git, rama, commits, PR o revisión equivalente.
[x] Revisión de código.
[x] Decisión sobre patrón: usado o descartado con motivo.
[x] Comparación Java ↔ Python.
```

---

## 3. Qué NO entra todavía

```text
[ ] Plugins reales.
[ ] Frameworks externos.
[ ] Persistencia en ficheros.
[ ] Base de datos.
[ ] IA real.
[ ] Patrones usados porque sí.
```

---

## 4. Entregables

```text
h5-extensible-clean-code-patrones/
├── README.md
├── src/
│   ├── Main.java
│   ├── Agent.java
│   ├── Memory.java
│   ├── Tool.java
│   └── herramientas...
└── docs/
    ├── informe-refactorizacion-h5.md
    ├── evidencia-git-h5.md
    ├── revision-codigo-h5.md
    ├── registro-patron-h5.md
    ├── comparacion-java-python-h5.md
    ├── portfolio-h5.md
    ├── registro-ia.md
    └── defensa-h5.md
```

---

## 5. Preguntas de defensa

```text
¿Qué problema tenía el código antes?
¿Qué refactorización hiciste?
¿Qué herramienta nueva añadiste?
¿Por qué ahora es más fácil añadir comandos?
¿Qué patrón usaste o descartaste?
¿Qué evidencia hay en Git o en la revisión?
¿Qué diferencia hay entre interfaces Java y duck typing en Python?
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

