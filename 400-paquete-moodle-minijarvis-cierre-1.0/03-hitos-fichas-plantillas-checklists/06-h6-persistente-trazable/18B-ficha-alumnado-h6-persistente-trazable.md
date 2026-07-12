# H6 — Agente persistente y trazable

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

