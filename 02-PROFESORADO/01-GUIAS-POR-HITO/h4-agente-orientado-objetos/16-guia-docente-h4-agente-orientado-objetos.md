# Guía docente — H4 Agente orientado a objetos

<!-- HEXA-CICLO-COMPLETO-POR-HITO:START -->

## Ciclo HEXA obligatorio del reto H4

**Reto del hito:** Reorganizar MiniJarvis con orientación a objetos y responsabilidades que coincidan con el código y los diagramas.

El profesorado debe hacer visible el avance de fase, proporcionar instrucción directa en X y no reducir HEXA a una etiqueta.

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


## Programación + Entornos de Desarrollo — 1.º DAW — Curso 2026/2027

Edición final para Moodle — septiembre de 2026

Documentos relacionados:

- `../../02-calendario-hitos-sprints-2026-2027.md`
- `../../04A-enunciados-y-entregables-alumnado.md`
- `../../06-rubricas-hitos.md`
- `README.md`
- `16B-ficha-alumnado-h4-agente-orientado-objetos.md`
- `16C-checklist-correccion-h4.md`

---

## 1. Propósito del hito

H4 rediseña MiniJarvis con programación orientada a objetos.

Producto esperado:

```text
MiniJarvis H4: agente con clases propias, responsabilidades claras, diagramas y defensa de diseño.
```

El alumnado debe dejar de concentrar todo el código en `Main` y empezar a repartir responsabilidades entre clases.

---

## 2. Qué añade H4 respecto a H3

| H3 | H4 |
|---|---|
| Código principalmente en `Main`. | Código organizado en clases. |
| Memoria como colección directa. | Memoria encapsulada en una clase. |
| Comandos en un bloque de control. | Agente con métodos y responsabilidades. |
| Pruebas de memoria. | Diagramas y relación diagrama-código. |

---

## 3. Restricciones didácticas

En H4 sí debe aparecer:

- clases propias;
- atributos;
- constructores;
- métodos;
- visibilidad `private`/`public`;
- relación entre clases;
- diagrama de clases;
- diagrama de comportamiento.

En H4 todavía NO debe forzarse:

- patrones de diseño;
- sistema de plugins;
- interfaces complejas;
- persistencia;
- arquitectura hexagonal;
- IA real.

---

## 4. Fechas y duración

Fechas orientativas:

```text
7 enero - 5 febrero 2027
```

---

## 5. RA/CE y evidencias

### Programación

- PR RA4: programas organizados en clases y principios de POO.
- Refuerzo PR RA2.

Evidencias:

- `Agent`, `Memory` u otras clases coherentes;
- atributos privados;
- métodos claros;
- constructor;
- defensa de responsabilidades.

### Entornos de Desarrollo

- ED RA5: diagramas de clases.
- ED RA6: diagramas de comportamiento.

Evidencias:

- diagrama de clases editable;
- diagrama de comportamiento;
- documento relación diagrama-código;
- defensa de una clase, relación o flujo.

---

## 6. Diseño mínimo recomendado

Clases mínimas:

| Clase | Responsabilidad |
|---|---|
| `Main` | Arrancar el programa y delegar en `Agent`. |
| `Agent` | Gestionar interacción, comandos y flujo principal. |
| `Memory` | Guardar y mostrar recuerdos temporales. |

Opcional si el grupo está preparado:

| Clase | Responsabilidad |
|---|---|
| `Message` | Representar un mensaje o recuerdo. |

Recomendación:

```text
Preferir pocas clases claras antes que muchas clases decorativas.
```

---

## 7. Entregables H4

| Entregable | Responsable | Formato | Plantilla local |
|---|---|---|---|
| Código Java OO | Equipo/individual | `src/*.java` | No aplica. |
| README H4 | Equipo/individual | `README.md` | `plantillas/README-h4-plantilla.md` |
| Diagrama de clases | Equipo | `docs/diagrama-clases-h4.md` | `plantillas/diagrama-clases-h4-plantilla.md` |
| Diagrama de comportamiento | Equipo | `docs/diagrama-comportamiento-h4.md` | `plantillas/diagrama-comportamiento-h4-plantilla.md` |
| Relación diagrama-código | Equipo | `docs/relacion-diagrama-codigo-h4.md` | `plantillas/relacion-diagrama-codigo-h4-plantilla.md` |
| Comparación Java ↔ Python | Individual | `docs/comparacion-java-python-h4.md` | `plantillas/comparacion-java-python-h4-plantilla.md` |
| Portfolio H4 | Individual | `docs/portfolio-h4.md` | `plantillas/portfolio-h4-plantilla.md` |
| Registro IA | Individual/equipo | `docs/registro-ia.md` | `plantillas/registro-ia-h4-plantilla.md` |
| Defensa H4 | Individual | `docs/defensa-h4.md` | `plantillas/defensa-h4-plantilla.md` |

---

## 8. Errores previsibles

| Error | Señal | Intervención docente |
|---|---|---|
| Todo sigue en `Main` | No hay POO real | Extraer `Agent` y `Memory`. |
| Clases sin responsabilidad | Clases decorativas | Preguntar qué sabe y qué hace cada clase. |
| Atributos públicos | Falta encapsulación | Reforzar `private` + métodos. |
| Diagrama no coincide | UML inventado | Pedir relación diagrama-código. |
| Patrones prematuros | Complejidad no defendible | Reencuadrar: H4 no necesita patrones. |

---

## 9. Uso de IA en H4

Permitido:

- pedir explicación de clase, objeto, atributo o constructor;
- revisar un diagrama contra el código;
- pedir preguntas de defensa;
- comparar clase Java con clase Python.

No permitido:

- generar un diseño completo no defendible;
- añadir patrones o arquitectura avanzada sin necesidad;
- entregar UML que no corresponde al código.

---

## 10. Preparación para H5

Antes de pasar a H5, comprobar:

- si cada clase tiene responsabilidad clara;
- si `Main` no concentra toda la lógica;
- si el diagrama coincide con el código;
- si el alumnado puede defender una clase y una relación.

H5 introducirá extensibilidad, refactorización, Git profesional y patrones iniciales si tienen sentido.

## Cobertura curricular de Programación

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

