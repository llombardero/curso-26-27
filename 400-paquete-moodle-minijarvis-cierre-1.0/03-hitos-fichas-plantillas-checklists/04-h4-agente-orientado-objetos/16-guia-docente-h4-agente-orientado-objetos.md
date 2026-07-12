# Guía docente — H4 Agente orientado a objetos

## Programación + Entornos de Desarrollo — 1.º DAW — Curso 2026/2027

Versión: cierre curricular 1.0 — julio 2026

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
| README H4 | Equipo/individual | `README.md` | `plantillas/README-h4-template.md` |
| Diagrama de clases | Equipo | `docs/diagrama-clases-h4.md` | `plantillas/diagrama-clases-h4-template.md` |
| Diagrama de comportamiento | Equipo | `docs/diagrama-comportamiento-h4.md` | `plantillas/diagrama-comportamiento-h4-template.md` |
| Relación diagrama-código | Equipo | `docs/relacion-diagrama-codigo-h4.md` | `plantillas/relacion-diagrama-codigo-h4-template.md` |
| Comparación Java ↔ Python | Individual | `docs/comparacion-java-python-h4.md` | `plantillas/comparacion-java-python-h4-template.md` |
| Portfolio H4 | Individual | `docs/portfolio-h4.md` | `plantillas/portfolio-h4-template.md` |
| Registro IA | Individual/equipo | `docs/registro-ia.md` | `plantillas/registro-ia-h4-template.md` |
| Defensa H4 | Individual | `docs/defensa-h4.md` | `plantillas/defensa-h4-template.md` |

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

