# Sesión 232 — Guía operativa del profesorado

## Introducción a `HashMap`

| Dato | Valor |
|---|---|
| Hito | H3 |
| Duración prevista | 45 minutos |
| Momento HEXA del hito | E |
| Resultado de hoy | Asegurar cobertura completa del Tema 4. |
| Evidencia mínima | `docs/justificacion-coleccion-h3.md` ampliado con array vs lista, uso o descarte de `Set`, y decisión sobre mutabilidad. |

> Esta es una guía de uso inmediato. Incluye únicamente lo necesario para preparar, impartir y cerrar esta sesión.

## Antes de entrar en clase

- [ ] Abrir o probar antes de clase el entorno y el proyecto que utilizará el alumnado; preparar una alternativa en pareja si falla un equipo.
- [ ] Comprobar que la evidencia mínima que se pedirá es: `docs/justificacion-coleccion-h3.md` ampliado con array vs lista, uso o descarte de `Set`, y decisión sobre mutabilidad.
- [ ] Dejar visible el objetivo y reservar los últimos 8 minutos para comprobar y cerrar.

## Material imprescindible

- Un ordenador por estudiante o pareja, con JDK e IntelliJ disponibles y el proyecto del hito accesible.
- Pizarra o una hoja reutilizable para bosquejar antes de modificar el proyecto.

## Qué debes explicar

Diferencia entre array y `ArrayList`; genéricos; clases envoltorio como `Integer`; `Set` para evitar repetidos; lista mutable e inmutable.

Guion breve sugerido:

> Hoy necesitamos comprender y practicar lo justo para producir una evidencia verificable. Primero observaremos un ejemplo, después trabajaréis y al final cada persona deberá poder explicar qué hizo y cómo sabe que funciona.

## Secuencia de aula

| Tiempo | Acción |
|---|---|
| 0–5 min | Presentar objetivo, producto y evidencia de hoy. |
| 5–13 min | Explicación breve: `HashMap` guarda pares clave-valor. |
| 13–18 min | Demostración o ejemplo: `nombre -> Laura`, `lenguaje -> Java`. |
| 18–35 min | Trabajo del alumnado: Crear un array con tres comandos conocidos, comparar sus limitaciones con `ArrayList`, y usar `Set<String>` para detectar recuerdos repetidos o justificar por qué no se incorpora al diseño final. |
| 35–40 min | Comprobar la evidencia con una explicación o prueba breve. |
| 40–45 min | Cierre: Pregunta: ¿qué estructura usarías si no quieres repetidos? |

## Ejemplo o demostración preparada

`nombre -> Laura`, `lenguaje -> Java`.

## Consigna que se entrega al alumnado

Crear mapa de preferencias.

Producto o evidencia que debe quedar: **`docs/justificacion-coleccion-h3.md` ampliado con array vs lista, uso o descarte de `Set`, y decisión sobre mutabilidad.**

## Qué observar mientras trabajan

- [ ] Pueden explicar qué están intentando conseguir.
- [ ] Registran una decisión, prueba o bloqueo; no muestran solo el resultado final.
- [ ] Todas las personas pueden describir su aportación.
- [ ] Comprueban el producto con un criterio observable.
- [ ] No usan datos personales, credenciales ni respuestas de ejemplo antes del intento propio.

## Si aparece un bloqueo

No entregues la solución completa. Pide que localicen el error, predigan el resultado y hagan una prueba mínima. Solo después muestra una pista concreta.

## Comprobación final

Pregunta de control: **¿Cuándo usarías mapa en vez de lista? ### Refuerzo H3 — Array, Set, mutabilidad y envoltorios**

Criterio para cerrar la sesión:

- [ ] Existe la evidencia mínima.
- [ ] Al menos una persona puede demostrarla y otra puede explicarla.
- [ ] El bloqueo pendiente queda escrito con un siguiente paso concreto.

## Al terminar

Anota solo lo operativo:

- alumnado que necesita apoyo en la siguiente sesión;
- evidencia pendiente;
- error común que conviene retomar;
- ajuste de tiempo necesario.
