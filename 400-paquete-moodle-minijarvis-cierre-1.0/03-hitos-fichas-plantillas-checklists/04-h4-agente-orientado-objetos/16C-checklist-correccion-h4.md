# Checklist de corrección — H4 Agente orientado a objetos

<!-- HEXA-CICLO-COMPLETO-POR-HITO:START -->

## Ciclo HEXA obligatorio del reto H4

**Reto del hito:** Reorganizar MiniJarvis con orientación a objetos y responsabilidades que coincidan con el código y los diagramas.

La corrección debe comprobar las cuatro fases por separado. La ausencia de una fase genera una evidencia incompleta que debe recuperarse.

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

## 1. Código OO

| Ítem | Sí | Parcial | No | Observaciones |
|---|---|---|---|---|
| Hay varias clases propias | | | | |
| `Main` delega lógica | | | | |
| Hay clase tipo `Agent` | | | | |
| Hay clase tipo `Memory` | | | | |
| Atributos privados | | | | |
| Constructores coherentes | | | | |
| Métodos con responsabilidad clara | | | | |

---

## 2. Diagramas

| Ítem | Sí | Parcial | No | Observaciones |
|---|---|---|---|---|
| Diagrama de clases | | | | |
| Diagrama de comportamiento | | | | |
| Diagramas coinciden con código | | | | |
| Relación diagrama-código documentada | | | | |

---

## 3. Defensa

| Pregunta | Adecuada | Dudas | No responde | Observaciones |
|---|---|---|---|---|
| Responsabilidad de `Agent` | | | | |
| Responsabilidad de `Memory` | | | | |
| Encapsulación | | | | |
| Relación del diagrama | | | | |
| Comparación con Python | | | | |

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

