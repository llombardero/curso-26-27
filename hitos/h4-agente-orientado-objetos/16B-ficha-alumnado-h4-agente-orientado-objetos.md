# H4 — Agente orientado a objetos

<!-- HEXA-CICLO-COMPLETO-POR-HITO:START -->

## Ciclo HEXA obligatorio del reto H4

**Reto del hito:** Reorganizar MiniJarvis con orientación a objetos y responsabilidades que coincidan con el código y los diagramas.

Debes conservar evidencias de las cuatro fases. Entregar solo el producto final no demuestra el ciclo completo.

| Fase | Pregunta que guía la fase | Acción del profesorado | Acción y evidencia del alumnado |
|---|---|---|---|
| **H — Hecho / reto** | ¿Qué problema real debemos resolver y con qué límites? | Presenta contexto, producto, restricciones, criterios y diagnóstico; no da todavía la solución completa. | Reformula el reto, identifica lo que sabe/no sabe y deja una ficha inicial con criterios de éxito. |
| **E — Exploración** | ¿Qué alternativas, hipótesis o pruebas iniciales ayudan a entenderlo? | Propone preguntas, ejemplos mínimos, casos y límites seguros. | Observa, compara, predice, prueba alternativas y registra decisiones o bloqueos. |
| **X — eXplicación** | ¿Qué conceptos permiten explicar lo observado y decidir con criterio? | Formaliza vocabulario, sintaxis, modelo mental, errores frecuentes, seguridad y criterios de calidad. | Explica con palabras propias, conecta teoría y exploración y corrige sus hipótesis. |
| **A — Aplicación** | ¿Cómo construimos, comprobamos, documentamos y defendemos la solución? | Desbloquea, exige pruebas y comprueba autoría y transferencia. | Implementa el producto, lo prueba, documenta evidencias, realiza review/defensa y propone mejora. |

### Temporalización mínima explícita

H4-S1–S10; 450 min mínimos en la guía autónoma. Los tiempos de fases se reservan dentro de las sesiones indicadas; los rangos pueden solaparse cuando una sesión cierra una fase y abre la siguiente.

| Fase | Reserva y momento recomendado | Puerta de salida |
|---|---|---|
| H | H4-S1; 45 min | Reto reformulado, límites y criterio de éxito visibles. |
| E | H4-S1–S2; 90 min integrados | Hipótesis, comparación, prueba inicial o decisiones justificadas. |
| X | H4-S2–S6; 135 min integrados | Explicación individual breve y conexión con el producto. |
| A | H4-S3–S10; 180 min integrados | Producto comprobado, documentación, defensa y mejora. |

**Expediente HEXA mínimo del hito:** diagnóstico de Main, alternativas de reparto, explicación POO/encapsulación, clases, diagramas, relación diagrama-código y defensa.

Regla de avance: puede haber prototipos durante E, pero no se considera completada A si faltan evidencias de H, E o X. Si una fase falta, se recupera esa fase y su evidencia; no se repite automáticamente todo el hito.

<!-- HEXA-CICLO-COMPLETO-POR-HITO:END -->


## Ficha para el alumnado

---

## 1. Reto

Vais a rediseñar MiniJarvis usando programación orientada a objetos.

El objetivo es dejar de tener todo en `Main` y repartir responsabilidades entre clases.

---

## 2. Qué debe tener H4

```text
[x] Clases propias.
[x] Atributos.
[x] Constructores.
[x] Métodos.
[x] Visibilidad private/public.
[x] Diagrama de clases.
[x] Diagrama de comportamiento.
[x] Relación diagrama-código.
```

---

## 3. Clases sugeridas

| Clase | Responsabilidad |
|---|---|
| `Main` | Arrancar el programa. |
| `Agent` | Gestionar comandos y flujo. |
| `Memory` | Guardar recuerdos. |

---

## 4. Qué NO entra todavía

```text
[ ] Patrones obligatorios.
[ ] Plugins.
[ ] Persistencia en ficheros.
[ ] Base de datos.
[ ] IA real.
```

---

## 5. Entregables

```text
h4-agente-orientado-objetos/
├── README.md
├── src/
│   ├── Main.java
│   ├── Agent.java
│   └── Memory.java
└── docs/
    ├── diagrama-clases-h4.md
    ├── diagrama-comportamiento-h4.md
    ├── relacion-diagrama-codigo-h4.md
    ├── comparacion-java-python-h4.md
    ├── portfolio-h4.md
    ├── registro-ia.md
    └── defensa-h4.md
```

---

## 6. Preguntas de defensa

```text
¿Qué responsabilidad tiene cada clase?
¿Qué clase no debería saber demasiado?
¿Qué atributos son privados?
¿Qué método inicia el agente?
¿Qué relación del diagrama aparece en el código?
¿Qué diferencia hay entre constructor Java y __init__ en Python?
```

<!-- AJUSTE-COBERTURA-CONCEPTOS-32 -->

## Ajuste curricular — cobertura de conceptos de Programación

Este hito queda alineado con el mapa `32-lista-conceptos-programacion-por-tema.md`.

```text
Hito: H4
Temas de referencia: Temas 2 y 5
Foco: orientación a objetos y separación de responsabilidades
```

Conceptos que deben trabajarse o, como mínimo, quedar conectados con evidencias del alumnado:

- clase
- objeto
- atributo
- método
- constructor
- referencia
- estado
- comportamiento
- responsabilidad
- private/public
- this
- diagrama de clases
- diagrama de comportamiento
- Javadoc como ampliación
- excepción básica

Criterio docente de cierre:

- El alumnado no solo entrega el producto; debe poder señalar dónde aparece cada concepto en su código, README, pruebas o defensa.
- Si un concepto se marca como ampliación, no penaliza al alumnado que alcance el mínimo, pero sí orienta mejora, recuperación o enriquecimiento.
- La defensa debe incluir al menos una pregunta de comprensión sobre los conceptos nuevos del hito.

