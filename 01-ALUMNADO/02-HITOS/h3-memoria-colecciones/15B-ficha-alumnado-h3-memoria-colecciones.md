# H3 — Agente con memoria en colecciones

<!-- HEXA-CICLO-COMPLETO-POR-HITO:START -->

## Ciclo HEXA obligatorio del reto H3

**Reto del hito:** Añadir memoria temporal mediante una colección adecuada y demostrar su comportamiento y límites.

Debes conservar evidencias de las cuatro fases. Entregar solo el producto final no demuestra el ciclo completo.

| Fase | Pregunta que guía la fase | Acción del profesorado | Acción y evidencia del alumnado |
|---|---|---|---|
| **H — Hecho / reto** | ¿Qué problema real debemos resolver y con qué límites? | Presenta contexto, producto, restricciones, criterios y diagnóstico; no da todavía la solución completa. | Reformula el reto, identifica lo que sabe/no sabe y deja una ficha inicial con criterios de éxito. |
| **E — Exploración** | ¿Qué alternativas, hipótesis o pruebas iniciales ayudan a entenderlo? | Propone preguntas, ejemplos mínimos, casos y límites seguros. | Observa, compara, predice, prueba alternativas y registra decisiones o bloqueos. |
| **X — eXplicación** | ¿Qué conceptos permiten explicar lo observado y decidir con criterio? | Formaliza vocabulario, sintaxis, modelo mental, errores frecuentes, seguridad y criterios de calidad. | Explica con palabras propias, conecta teoría y exploración y corrige sus hipótesis. |
| **A — Aplicación** | ¿Cómo construimos, comprobamos, documentamos y defendemos la solución? | Desbloquea, exige pruebas y comprueba autoría y transferencia. | Implementa el producto, lo prueba, documenta evidencias, realiza review/defensa y propone mejora. |

### Temporalización mínima explícita

H3-S1–S10; 450 min mínimos en la guía autónoma. Los tiempos de fases se reservan dentro de las sesiones indicadas; los rangos pueden solaparse cuando una sesión cierra una fase y abre la siguiente.

| Fase | Reserva y momento recomendado | Puerta de salida |
|---|---|---|
| H | H3-S1; 45 min | Reto reformulado, límites y criterio de éxito visibles. |
| E | H3-S1–S2; 90 min integrados | Hipótesis, comparación, prueba inicial o decisiones justificadas. |
| X | H3-S3–S6; 135 min integrados | Explicación individual breve y conexión con el producto. |
| A | H3-S7–S10; 180 min integrados | Producto comprobado, documentación, defensa y mejora. |

**Expediente HEXA mínimo del hito:** requisitos de memoria, comparación de alternativas, explicación de ArrayList/casos límite, código, pruebas y defensa.

Regla de avance: puede haber prototipos durante E, pero no se considera completada A si faltan evidencias de H, E o X. Si una fase falta, se recupera esa fase y su evidencia; no se repite automáticamente todo el hito.

<!-- HEXA-CICLO-COMPLETO-POR-HITO:END -->


## Ficha para el alumnado

Curso: 1.º DAW — Programación + Entornos de Desarrollo

---

## 1. Reto

Vais a añadir memoria temporal a MiniJarvis.

El agente deberá recordar información durante la ejecución, por ejemplo mensajes, comandos o preferencias simples.

---

## 2. Qué debe hacer MiniJarvis H3

```text
[x] Usar una colección Java.
[x] Guardar información durante la ejecución.
[x] Consultar la memoria.
[x] Gestionar memoria vacía.
[x] Probar casos límite.
[x] Justificar la colección elegida.
[x] Comparar Java ↔ Python.
```

---

## 3. Qué NO entra todavía

```text
[ ] Guardar en ficheros.
[ ] Usar base de datos.
[ ] Crear arquitectura OO completa.
[ ] Usar patrones de diseño.
[ ] Conectar con IA real.
```

---

## 4. Comandos sugeridos

| Comando | Qué debe hacer |
|---|---|
| `recuerda` | Guardar un mensaje. |
| `memoria` | Mostrar lo guardado. |
| `estado` | Indicar cuántos recuerdos hay. |
| `ayuda` | Mostrar comandos. |
| `salir` | Terminar. |

---

## 5. Entregables

```text
h3-memoria-colecciones/
├── README.md
├── src/
│   └── Main.java
└── docs/
    ├── evidencia-ejecucion-h3.md
    ├── pruebas-memoria-h3.md
    ├── justificacion-coleccion-h3.md
    ├── incidencia-h3.md
    ├── comparacion-java-python-h3.md
    ├── portfolio-h3.md
    ├── registro-ia.md
    └── defensa-h3.md
```

---

## 6. Preguntas de defensa

```text
¿Qué colección has usado y por qué?
¿Cómo guardas un recuerdo?
¿Cómo recorres la memoria?
¿Qué ocurre si la memoria está vacía?
¿Qué caso límite probaste?
¿Qué cambia entre ArrayList/HashMap y list/dict en Python?
```

---

## 7. Checklist antes de entregar

```text
[ ] El programa se ejecuta.
[ ] Hay memoria temporal.
[ ] Puedo guardar información.
[ ] Puedo consultar memoria.
[ ] La memoria vacía está gestionada.
[ ] Hay pruebas de memoria.
[ ] Hay justificación de colección.
[ ] Hay comparación Java ↔ Python.
[ ] He registrado IA si la he usado.
[ ] Puedo defender la colección elegida.
```

## Cobertura curricular de Programación

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

Criterio docente de cierre:

- El alumnado no solo entrega el producto; debe poder señalar dónde aparece cada concepto en su código, README, pruebas o defensa.
- Si un concepto se marca como ampliación, no penaliza al alumnado que alcance el mínimo, pero sí orienta mejora, recuperación o enriquecimiento.
- La defensa debe incluir al menos una pregunta de comprensión sobre los conceptos nuevos del hito.

