# H5 — Agente extensible, clean code y patrones iniciales

<!-- HEXA-CICLO-COMPLETO-POR-HITO:START -->

## Ciclo HEXA obligatorio del reto H5

**Reto del hito:** Resolver el crecimiento de comandos mediante refactorización segura, contratos simples y código extensible.

Debes conservar evidencias de las cuatro fases. Entregar solo el producto final no demuestra el ciclo completo.

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

<!-- HEXA-CICLO-COMPLETO-POR-HITO:END -->


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

