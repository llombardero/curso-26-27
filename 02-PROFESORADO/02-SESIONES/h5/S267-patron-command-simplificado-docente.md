# Sesión 267 — Guía operativa del profesorado

## Patrón Command simplificado o decisión de no patrón

| Dato | Valor |
|---|---|
| Hito | H5 |
| Duración prevista | 45 minutos |
| Fase HEXA del hito | Ejecutar — crear |
| Resultado de hoy | Relacionar un problema real del diseño de herramientas con la idea de Command y decidir si conviene usarla sin sobreingeniería. |
| Evidencia mínima | `docs/registro-patron-h5.md` con problema, alternativa simple, decisión, semejanza o diferencia respecto a Command y riesgo de sobreingeniería. |

> El patrón no es una meta ni una palabra que haya que introducir obligatoriamente. La decisión válida puede ser conservar `Tool` y sus clases concretas sin implementar un Command completo.

## Antes de entrar en clase

- [ ] Tener disponible una versión del proyecto con varias clases que implementen `Tool`.
- [ ] Preparar un ejemplo mínimo de acción encapsulada en un objeto.
- [ ] Comprobar que la plantilla `docs/registro-patron-h5.md` está disponible.
- [ ] Reservar los últimos 8 minutos para justificar la decisión y cerrar.

## Material imprescindible

- Un ordenador por estudiante o pareja, con JDK e IntelliJ disponibles y el proyecto H5 accesible.
- Pizarra o una hoja reutilizable para comparar problema, alternativa y decisión.
- Datos ficticios; no se usarán contraseñas, tokens, claves API ni datos personales reales.

## Qué debes explicar

- Un patrón de diseño describe una solución conocida para un problema que se repite.
- Command encapsula una acción como objeto.
- Cada implementación de `Tool` ya se parece a un comando ejecutable.
- No hacen falta invocadores, receptores o fábricas complejas si no resuelven un problema real.
- También es correcto descartar el patrón y documentar por qué la solución simple es suficiente.

## Secuencia de aula

| Tiempo | Acción |
|---|---|
| 0–5 min | Presentar el problema: añadir acciones sin hacer crecer un condicional central. |
| 5–12 min | Explicar patrón, problema recurrente y riesgo de utilizar nombres profesionales sin necesidad. |
| 12–18 min | Comparar `Tool` y una clase concreta con la idea mínima de Command. |
| 18–32 min | Analizar el proyecto y completar problema, alternativa simple, solución actual y coste de complicarla. |
| 32–37 min | Decidir si se adopta la expresión «Command simplificado» o si se descarta el patrón. |
| 37–42 min | Contrastar la decisión con otra pareja y mejorar una justificación. |
| 42–45 min | Responder la pregunta de control y guardar la evidencia. |

## Ejemplo o demostración preparada

```text
Problema: cada acción estaba dentro de un condicional grande.
Solución simple: Tool + clases concretas con execute().
Semejanza con Command: cada objeto encapsula una acción.
Límite: no añadimos infraestructura que el proyecto no necesita.
```

## Consigna que se entrega al alumnado

Completa `docs/registro-patron-h5.md` con:

1. el problema de diseño observado;
2. una alternativa simple;
3. la solución usada en el proyecto;
4. por qué se parece o no a Command;
5. una ventaja comprobable;
6. un riesgo de sobreingeniería;
7. la decisión final: mantener, simplificar o descartar.

Producto o evidencia que debe quedar: **una decisión defendible, no la implementación obligatoria de un patrón completo.**

## Qué observar mientras trabajan

- [ ] Nombran el problema antes que el patrón.
- [ ] Relacionan la decisión con código real del proyecto.
- [ ] Diferencian semejanza conceptual de implementación completa.
- [ ] Identifican al menos un coste o riesgo de complicar el diseño.
- [ ] Pueden explicar qué mantendrían y qué descartarían.

## Si aparece un bloqueo

Pide que respondan primero: «¿qué cambio sería difícil con el diseño actual?». Si no hay un problema concreto, no deben forzar el patrón.

## Comprobación final

Pregunta de control: **¿Qué problema real resuelve aquí la idea de Command y qué parte sería sobreingeniería?**

Criterio para cerrar la sesión:

- [ ] Existe `docs/registro-patron-h5.md`.
- [ ] La decisión está vinculada a un problema observable.
- [ ] Se distingue Command simplificado de una implementación completa.
- [ ] La persona puede defender por qué mantiene o descarta el patrón.

## Al terminar

Anota solo lo operativo:

- decisiones que se basan en el problema real;
- usos del nombre «Command» sin justificación;
- dudas que deban retomarse al revisar código;
- alumnado que necesita otro ejemplo concreto.
