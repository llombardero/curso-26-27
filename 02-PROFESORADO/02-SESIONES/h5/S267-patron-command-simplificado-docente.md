# Sesión 267 — Guía operativa del profesorado

## Patrón Command simplificado

| Dato | Valor |
|---|---|
| Hito | H5 |
| Duración prevista | 45 minutos |
| Momento HEXA del hito | X |
| Resultado de hoy | Trabajar conceptos importantes de los temas 5 y 6 que no siempre aparecen en MiniJarvis mínimo. |
| Evidencia mínima | `docs/refuerzo-poo-avanzada-h5.md` con código, pruebas o salidas, decisión de qué se mantiene y qué se descarta, y justificación de composición/interfaz frente a herencia. Debe nombrar explícitamente los conceptos del Tema 6 trabajados y cuáles quedan como ampliación reconocida. |

> Esta es una guía de uso inmediato. Incluye únicamente lo necesario para preparar, impartir y cerrar esta sesión.

## Antes de entrar en clase

- [ ] Abrir o probar antes de clase el entorno y el proyecto que utilizará el alumnado; preparar una alternativa en pareja si falla un equipo.
- [ ] Comprobar que la evidencia mínima que se pedirá es: `docs/refuerzo-poo-avanzada-h5.md` con código, pruebas o salidas, decisión de qué se mantiene y qué se descarta, y justificación de composición/interfaz frente a herencia. Debe nombrar explícitamente los conceptos del Tema 6 trabajados y cuáles quedan como ampliación reconocida.
- [ ] Dejar visible el objetivo y reservar los últimos 8 minutos para comprobar y cerrar.

## Material imprescindible

- Un ordenador por estudiante o pareja, con JDK e IntelliJ disponibles y el proyecto del hito accesible.
- Pizarra o una hoja reutilizable para bosquejar antes de modificar el proyecto.

## Qué debes explicar

`enum`, `record`, `@Override`, `toString`, `equals`, `hashCode`, `instanceof`, ordenación con `Comparable` o `Comparator`, clase abstracta, herencia, `super`, `protected`, package-private, métodos `default`/privados en interfaces y reconocimiento de clases anónimas/finales/selladas como ampliación.

Guion breve sugerido:

> Hoy necesitamos comprender y practicar lo justo para producir una evidencia verificable. Primero observaremos un ejemplo, después trabajaréis y al final cada persona deberá poder explicar qué hizo y cómo sabe que funciona.

## Secuencia de aula

| Tiempo | Acción |
|---|---|
| 0–5 min | Presentar objetivo, producto y evidencia de hoy. |
| 5–13 min | Explicación breve: El patrón Command encapsula una acción como objeto. Aquí solo se nombra si el diseño lo justifica. |
| 13–18 min | Demostración o ejemplo: Cada `Tool` se parece a un comando ejecutable. |
| 18–35 min | Trabajo del alumnado: Crear `enum CommandType`, valorar un `record CommandResult`, añadir `@Override` en herramientas, implementar `toString` y una comparación `equals`/`hashCode` en una clase de dominio, ordenar herramientas por nombre y comparar `interface Tool` con una clase abstracta `BaseTool`. Analizar un microejemplo de `instanceof` y justificar por qué se prefiere polimorfismo cuando sea posible. |
| 35–40 min | Comprobar la evidencia con una explicación o prueba breve. |
| 40–45 min | Cierre: Pregunta: ¿por qué no siempre conviene usar herencia aunque sepamos programarla? |

## Ejemplo o demostración preparada

Cada `Tool` se parece a un comando ejecutable.

## Consigna que se entrega al alumnado

Decidir si se usa o se descarta el patrón.

Producto o evidencia que debe quedar: **`docs/refuerzo-poo-avanzada-h5.md` con código, pruebas o salidas, decisión de qué se mantiene y qué se descarta, y justificación de composición/interfaz frente a herencia. Debe nombrar explícitamente los conceptos del Tema 6 trabajados y cuáles quedan como ampliación reconocida.**

## Qué observar mientras trabajan

- [ ] Pueden explicar qué están intentando conseguir.
- [ ] Registran una decisión, prueba o bloqueo; no muestran solo el resultado final.
- [ ] Todas las personas pueden describir su aportación.
- [ ] Comprueban el producto con un criterio observable.
- [ ] No usan datos personales, credenciales ni respuestas de ejemplo antes del intento propio.

## Si aparece un bloqueo

No entregues la solución completa. Pide que localicen el error, predigan el resultado y hagan una prueba mínima. Solo después muestra una pista concreta.

## Comprobación final

Pregunta de control: **¿Qué problema real resuelve en tu proyecto? ### Refuerzo H5 — POO avanzada aplicada y descartes razonados**

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
