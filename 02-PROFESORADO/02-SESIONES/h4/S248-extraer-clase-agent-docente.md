# Sesión 248 — Guía operativa del profesorado

## Extraer clase `Agent`

| Dato | Valor |
|---|---|
| Hito | H4 |
| Duración prevista | 45 minutos |
| Fase HEXA del hito | Planificar — organizar el trabajo |
| Resultado de hoy | Sacar flujo principal de `Main`. |
| Evidencia mínima | `Main` queda reducido a crear y lanzar el agente. |

> Esta es una guía de uso inmediato. Incluye únicamente lo necesario para preparar, impartir y cerrar esta sesión.

## Antes de entrar en clase

- [ ] Abrir o probar antes de clase el entorno y el proyecto que utilizará el alumnado; preparar una alternativa en pareja si falla un equipo.
- [ ] Comprobar que la evidencia mínima que se pedirá es: `Main` queda reducido a crear y lanzar el agente.
- [ ] Dejar visible el objetivo y reservar los últimos 8 minutos para comprobar y cerrar.

## Material imprescindible

- Un ordenador por estudiante o pareja, con JDK e IntelliJ disponibles y el proyecto del hito accesible.

## Qué debes explicar

`Main` arranca; `Agent` coordina.

Guion breve sugerido:

> Hoy necesitamos comprender y practicar lo justo para producir una evidencia verificable. Primero observaremos un ejemplo, después trabajaréis y al final cada persona deberá poder explicar qué hizo y cómo sabe que funciona.

## Secuencia de aula

| Tiempo | Acción |
|---|---|
| 0–5 min | Presentar objetivo, producto y evidencia de hoy. |
| 5–13 min | Explicación breve: `Main` debe arrancar; `Agent` debe coordinar la conversación. |
| 13–18 min | Demostración o ejemplo: `new Agent().run();` en `Main`. |
| 18–35 min | Trabajo del alumnado: Crear `Agent` con método de ejecución. |
| 35–40 min | Comprobar la evidencia con una explicación o prueba breve. |
| 40–45 min | Cierre: Pregunta: ¿qué responsabilidad conserva `Main`? |

## Ejemplo o demostración preparada

`new Agent().run();` en `Main`.

## Consigna que se entrega al alumnado

Crear `Agent` con método `run`.

Producto o evidencia que debe quedar: **`Main` queda reducido a crear y lanzar el agente.**

## Qué observar mientras trabajan

- [ ] Pueden explicar qué están intentando conseguir.
- [ ] Registran una decisión, prueba o bloqueo; no muestran solo el resultado final.
- [ ] Todas las personas pueden describir su aportación.
- [ ] Comprueban el producto con un criterio observable.
- [ ] No usan datos personales, credenciales ni respuestas de ejemplo antes del intento propio.

## Si aparece un bloqueo

No entregues la solución completa. Pide que localicen el error, predigan el resultado y hagan una prueba mínima. Solo después muestra una pista concreta.

## Comprobación final

Pregunta de control: **¿Qué código debe quedarse en `Main`?**

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
