# H6 — Agente persistente y trazable

<!-- HEXA-CICLO-COMPLETO-POR-HITO:START -->

## Ciclo HEXA obligatorio del reto H6

**Reto del hito:** Conservar memoria e historial entre ejecuciones con ficheros, trazabilidad y tratamiento seguro de errores y datos.

Debes conservar evidencias de las cuatro fases. Entregar solo el producto final no demuestra el ciclo completo.

| Fase | Pregunta que guía la fase | Acción del profesorado | Acción y evidencia del alumnado |
|---|---|---|---|
| **H — Hecho / reto** | ¿Qué problema real debemos resolver y con qué límites? | Presenta contexto, producto, restricciones, criterios y diagnóstico; no da todavía la solución completa. | Reformula el reto, identifica lo que sabe/no sabe y deja una ficha inicial con criterios de éxito. |
| **E — Exploración** | ¿Qué alternativas, hipótesis o pruebas iniciales ayudan a entenderlo? | Propone preguntas, ejemplos mínimos, casos y límites seguros. | Observa, compara, predice, prueba alternativas y registra decisiones o bloqueos. |
| **X — eXplicación** | ¿Qué conceptos permiten explicar lo observado y decidir con criterio? | Formaliza vocabulario, sintaxis, modelo mental, errores frecuentes, seguridad y criterios de calidad. | Explica con palabras propias, conecta teoría y exploración y corrige sus hipótesis. |
| **A — Aplicación** | ¿Cómo construimos, comprobamos, documentamos y defendemos la solución? | Desbloquea, exige pruebas y comprueba autoría y transferencia. | Implementa el producto, lo prueba, documenta evidencias, realiza review/defensa y propone mejora. |

### Temporalización mínima explícita

H6-S1–S10; 450 min mínimos en la guía autónoma. Los tiempos de fases se reservan dentro de las sesiones indicadas; los rangos pueden solaparse cuando una sesión cierra una fase y abre la siguiente.

| Fase | Reserva y momento recomendado | Puerta de salida |
|---|---|---|
| H | H6-S1; 45 min | Reto reformulado, límites y criterio de éxito visibles. |
| E | H6-S1–S2; 90 min integrados | Hipótesis, comparación, prueba inicial o decisiones justificadas. |
| X | H6-S2–S3; 135 min integrados | Explicación individual breve y conexión con el producto. |
| A | H6-S3–S10; 180 min integrados | Producto comprobado, documentación, defensa y mejora. |

**Expediente HEXA mínimo del hito:** problema reproducido, decisiones de ruta/formato, explicación de persistencia/excepciones/logs, código, prueba en dos ejecuciones, seguridad y defensa.

Regla de avance: puede haber prototipos durante E, pero no se considera completada A si faltan evidencias de H, E o X. Si una fase falta, se recupera esa fase y su evidencia; no se repite automáticamente todo el hito.

<!-- HEXA-CICLO-COMPLETO-POR-HITO:END -->


## Ficha para el alumnado

---

## 1. Reto

Vais a hacer que MiniJarvis pueda guardar y recuperar información entre ejecuciones.

También crearéis un historial simple y revisaréis seguridad: nada de secretos ni datos personales reales.

---

## 2. Qué debe tener H6

```text
[x] Guardar recuerdos en fichero.
[x] Recuperar recuerdos al iniciar o consultar.
[x] Crear logs o historial simple.
[x] README reproducible.
[x] Pruebas de persistencia.
[x] Registro de seguridad.
[x] Comparación Java ↔ Python.
```

---

## 3. Qué NO entra todavía

```text
[ ] API keys reales.
[ ] .env real en el repositorio.
[ ] Datos personales reales.
[ ] Base de datos compleja obligatoria.
[ ] IA real obligatoria.
```

---

## 4. Entregables

```text
h6-persistente-trazable/
├── README.md
├── src/
├── data/
│   └── recuerdos.txt
├── logs/
│   └── historial.log
└── docs/
    ├── pruebas-persistencia-h6.md
    ├── seguridad-h6.md
    ├── logs-historial-h6.md
    ├── incidencia-h6.md
    ├── comparacion-java-python-h6.md
    ├── portfolio-h6.md
    ├── registro-ia.md
    └── defensa-h6.md
```

---

## 5. Preguntas de defensa

```text
¿Dónde se guarda la información?
¿Qué ocurre si el fichero no existe?
¿Cómo puedo ejecutar tu proyecto desde cero?
¿Qué datos no deberías guardar?
¿Cómo sabes que persiste entre ejecuciones?
¿Qué diferencia hay entre ficheros en Java y Python?
```

<!-- AJUSTE-COBERTURA-CONCEPTOS-32 -->

## Ajuste curricular — cobertura de conceptos de Programación

Este hito queda alineado con el mapa `32-lista-conceptos-programacion-por-tema.md`.

```text
Hito: H6
Temas de referencia: Temas 5, 6 y puente hacia Tema 8
Foco: persistencia, logs, errores y trazabilidad
```

Conceptos que deben trabajarse o, como mínimo, quedar conectados con evidencias del alumnado:

- clases responsables
- excepciones checked y runtime
- throws
- validación
- invariantes
- repositorio como idea inicial
- ficheros
- logs
- seguridad
- Repository como patrón opcional
- pruebas de dos ejecuciones
- trazabilidad

Criterio docente de cierre:

- El alumnado no solo entrega el producto; debe poder señalar dónde aparece cada concepto en su código, README, pruebas o defensa.
- Si un concepto se marca como ampliación, no penaliza al alumnado que alcance el mínimo, pero sí orienta mejora, recuperación o enriquecimiento.
- La defensa debe incluir al menos una pregunta de comprensión sobre los conceptos nuevos del hito.

