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
└── src/
    ├── Main.java
    ├── Agent.java
    └── Memory.java
```

El diagrama de clases y su relación con el código se integran en el repositorio/README. El diagrama de comportamiento es práctica coordinada opcional de Entornos, no una entrega obligatoria de Programación. No hay portfolio ni registro IA separados por hito.

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
