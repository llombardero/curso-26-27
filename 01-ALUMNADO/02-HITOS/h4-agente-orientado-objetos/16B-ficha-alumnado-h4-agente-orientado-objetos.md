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
├── README
├── src/
│   ├── Main.java
│   ├── Agent.java
│   └── Memory.java
└── docs/
    ├── diagrama-clases-h4
    ├── diagrama-comportamiento-h4
    ├── relacion-diagrama-codigo-h4
    ├── comparacion-java-python-h4
    ├── portfolio-h4
    ├── registro-ia
    └── defensa-h4
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
