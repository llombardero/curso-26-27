# Sesión 284 — Guía operativa del profesorado

## Errores de fichero

| Dato | Valor |
|---|---|
| Hito | H6 |
| Duración prevista | 45 minutos |
| Momento HEXA del hito | X |
| Resultado de hoy | Asegurar excepciones propias, `throws` e invariantes de estado. |
| Evidencia mínima | Código o decisión técnica en `docs/incidencia-h6.md`/`docs/seguridad-h6.md` con prueba de error controlado. |

> Esta es una guía de uso inmediato. Incluye únicamente lo necesario para preparar, impartir y cerrar esta sesión.

## Antes de entrar en clase

- [ ] Abrir o probar antes de clase el entorno y el proyecto que utilizará el alumnado; preparar una alternativa en pareja si falla un equipo.
- [ ] Comprobar que la evidencia mínima que se pedirá es: Código o decisión técnica en `docs/incidencia-h6.md`/`docs/seguridad-h6.md` con prueba de error controlado.
- [ ] Dejar visible el objetivo y reservar los últimos 8 minutos para comprobar y cerrar.

## Material imprescindible

- Un ordenador por estudiante o pareja, con JDK e IntelliJ disponibles y el proyecto del hito accesible.
- Datos ficticios de prueba. No se usarán contraseñas, tokens, claves API ni datos personales reales.

## Qué debes explicar

Diferencia entre lanzar y capturar; excepción propia `MemoryStorageException` o `PersistenceException`; checked/runtime según nivel; invariante de memoria válida.

Guion breve sugerido:

> Hoy necesitamos comprender y practicar lo justo para producir una evidencia verificable. Primero observaremos un ejemplo, después trabajaréis y al final cada persona deberá poder explicar qué hizo y cómo sabe que funciona.

## Secuencia de aula

| Tiempo | Acción |
|---|---|
| 0–5 min | Presentar objetivo, producto y evidencia de hoy. |
| 5–13 min | Explicación breve: Los ficheros pueden no existir, estar vacíos o fallar por permisos. |
| 13–18 min | Demostración o ejemplo: Ejecutar sin carpeta `data` y corregir con `createDirectories`. |
| 18–35 min | Trabajo del alumnado: Crear una excepción propia para errores de carga/guardado o documentar por qué se usa una excepción estándar; asegurar que `Memory` no guarda recuerdos nulos/vacíos ni expone su lista interna modificable. |
| 35–40 min | Comprobar la evidencia con una explicación o prueba breve. |
| 40–45 min | Cierre: Pregunta: ¿qué invariante debe mantener siempre `Memory`? |

## Ejemplo o demostración preparada

Ejecutar sin carpeta `data` y corregir con `createDirectories`.

## Consigna que se entrega al alumnado

Documentar y controlar un error.

Producto o evidencia que debe quedar: **Código o decisión técnica en `docs/incidencia-h6.md`/`docs/seguridad-h6.md` con prueba de error controlado.**

## Qué observar mientras trabajan

- [ ] Pueden explicar qué están intentando conseguir.
- [ ] Registran una decisión, prueba o bloqueo; no muestran solo el resultado final.
- [ ] Todas las personas pueden describir su aportación.
- [ ] Comprueban el producto con un criterio observable.
- [ ] No usan datos personales, credenciales ni respuestas de ejemplo antes del intento propio.

## Si aparece un bloqueo

No entregues la solución completa. Pide que localicen el error, predigan el resultado y hagan una prueba mínima. Solo después muestra una pista concreta.

## Comprobación final

Pregunta de control: **¿Qué mensaje recibe el usuario si falla? ### Refuerzo H6 — Excepción propia e invariantes**

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
