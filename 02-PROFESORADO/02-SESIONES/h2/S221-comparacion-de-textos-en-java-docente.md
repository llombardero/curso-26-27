# Sesión 221 — Guía operativa del profesorado

## Comparación de textos en Java

| Dato | Valor |
|---|---|
| Hito | H2 |
| Duración prevista | 45 minutos |
| Momento HEXA del hito | X |
| Resultado de hoy | Evitar el error de usar `==` con cadenas. |
| Evidencia mínima | Comandos funcionan con espacios o mayúsculas si se decide soportarlo. |

> Esta es una guía de uso inmediato. Incluye únicamente lo necesario para preparar, impartir y cerrar esta sesión.

## Antes de entrar en clase

- [ ] Abrir o probar antes de clase el entorno y el proyecto que utilizará el alumnado; preparar una alternativa en pareja si falla un equipo.
- [ ] Comprobar que la evidencia mínima que se pedirá es: Comandos funcionan con espacios o mayúsculas si se decide soportarlo.
- [ ] Dejar visible el objetivo y reservar los últimos 8 minutos para comprobar y cerrar.

## Material imprescindible

- Un ordenador por estudiante o pareja, con JDK e IntelliJ disponibles y el proyecto del hito accesible.
- Proyector solo si habrá demostración colectiva; la defensa puede realizarse directamente en el equipo.

## Qué debes explicar

`.equals()`, `trim()` y `toLowerCase()`.

Guion breve sugerido:

> Hoy necesitamos comprender y practicar lo justo para producir una evidencia verificable. Primero observaremos un ejemplo, después trabajaréis y al final cada persona deberá poder explicar qué hizo y cómo sabe que funciona.

## Secuencia de aula

| Tiempo | Acción |
|---|---|
| 0–5 min | Presentar objetivo, producto y evidencia de hoy. |
| 5–13 min | Explicación breve: En Java los textos se comparan con `.equals()`, no con `==`. |
| 13–18 min | Demostración o ejemplo: Mostrar fallo típico de `==` y corrección con `.equals()`. |
| 18–35 min | Trabajo del alumnado: Corregir comparación de comandos y normalizar entrada. |
| 35–40 min | Comprobar la evidencia con una explicación o prueba breve. |
| 40–45 min | Cierre: Microdefensa: explicar por qué no usamos `==`. |

## Ejemplo o demostración preparada

Mostrar fallo típico de `==` y corrección con `.equals()`.

## Consigna que se entrega al alumnado

Normalizar comando con `trim().toLowerCase()`.

Producto o evidencia que debe quedar: **Comandos funcionan con espacios o mayúsculas si se decide soportarlo.**

## Qué observar mientras trabajan

- [ ] Pueden explicar qué están intentando conseguir.
- [ ] Registran una decisión, prueba o bloqueo; no muestran solo el resultado final.
- [ ] Todas las personas pueden describir su aportación.
- [ ] Comprueban el producto con un criterio observable.
- [ ] No usan datos personales, credenciales ni respuestas de ejemplo antes del intento propio.

## Si aparece un bloqueo

Pide una explicación o modificación individual breve. El producto de equipo no sustituye la evidencia individual.

## Comprobación final

Pregunta de control: **¿Qué problema resuelve `trim()`?**

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
