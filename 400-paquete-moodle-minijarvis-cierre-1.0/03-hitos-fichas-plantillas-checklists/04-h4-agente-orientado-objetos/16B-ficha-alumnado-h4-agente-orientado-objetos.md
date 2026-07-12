# H4 — Agente orientado a objetos

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

