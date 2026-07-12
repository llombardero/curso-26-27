# H3 — Agente con memoria en colecciones

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

<!-- AJUSTE-COBERTURA-CONCEPTOS-32 -->

## Ajuste curricular — cobertura de conceptos de Programación

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

