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
