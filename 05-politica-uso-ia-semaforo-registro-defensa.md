# Política de uso de IA — Semáforo, registro y defensa

## Programación + Entornos de Desarrollo — 1.º DAW — Curso 2026/2027

Versión: borrador 0.1
Documentos relacionados:

- `00-mapa-maestro-curso-2026-2027.md`
- `01-matriz-integrada-ra-ce-evidencias-tareas.md`
- `02-calendario-hitos-sprints-2026-2027.md`
- `04-enunciados-entregables-y-modelo-laura.md`

---

## 1. Propósito

Esta política define cómo puede utilizar el alumnado herramientas de inteligencia artificial durante el curso.

La IA se entiende como una herramienta de apoyo al aprendizaje, no como sustituta del aprendizaje.

El objetivo es que el alumnado aprenda a usar IA de forma:

- responsable;
- ética;
- trazable;
- segura;
- crítica;
- defendible;
- útil para aprender y resolver problemas.

---

## 2. Herramientas previstas

Herramientas autorizadas inicialmente:

- Gemini, por acuerdo de la Junta de Andalucía con Google.
- Jarvis, modelo propio disponible para consulta.
- Otras herramientas autorizadas expresamente por el profesorado.

Condición:

- cada alumno/a tendrá cuenta nominal propia;
- no se compartirán contraseñas;
- no se introducirán datos personales, credenciales ni información sensible;
- cualquier uso en entregables evaluables debe registrarse.

---

## 3. Principio general

Se permite usar IA cuando ayuda a:

- comprender;
- practicar;
- contrastar;
- revisar;
- depurar;
- mejorar;
- documentar;
- comparar alternativas;
- preparar defensas.

No se permite usar IA para:

- sustituir el trabajo propio;
- ocultar falta de comprensión;
- entregar código no entendido;
- evitar pensar;
- copiar soluciones completas;
- introducir datos prohibidos;
- falsear autoría.

Regla básica:

> Puedes usar IA como copiloto, tutor o revisor. No puedes usarla como autor oculto de tu entrega.

---

## 4. Semáforo de uso de IA

### 4.1. Verde — Permitido y recomendado

Usos que normalmente están permitidos sin autorización especial, aunque deben registrarse si afectan a un entregable evaluable.

| Uso verde | Ejemplos |
|---|---|
| Pedir explicaciones | “Explícame qué es una variable en Java con un ejemplo sencillo”. |
| Pedir ejemplos pequeños | “Dame un ejemplo mínimo de Scanner”. |
| Comparar conceptos | “Diferencia entre variable y constante”. |
| Entender errores | “Qué significa este error de compilación”. |
| Mejorar documentación | “Ayúdame a redactar un README más claro”. |
| Preparar preguntas de estudio | “Hazme preguntas para repasar bucles”. |
| Revisar ortografía o claridad | “Revisa este portfolio para que se entienda mejor”. |
| Generar casos de prueba para revisar | “Propón casos de prueba para este menú”. |

Condición:

- El alumnado debe entender la respuesta.
- Si se incorpora algo a una entrega, se registra.

---

### 4.2. Amarillo — Permitido con registro, verificación y defensa

Usos permitidos, pero con más control.

| Uso amarillo | Condiciones |
|---|---|
| Generar fragmentos de código | Debe adaptarse, probarse y explicarse. |
| Refactorizar código | Debe compararse antes/después y justificarse. |
| Traducir Java a Python para la comparación de casa | Debe defenderse la equivalencia y diferencias. |
| Proponer diagramas UML | Deben revisarse contra el código real. |
| Proponer tests | Deben ejecutarse o comprobarse manualmente. |
| Ayudar a leer stack traces | El alumno debe explicar la causa y solución. |
| Sugerir patrones de diseño | Solo se acepta si resuelve un problema real. |
| Generar documentación técnica | Debe revisarse y ajustarse al proyecto real. |
| Ayudar con configuración Docker/CI | Debe entenderse y no incluir secretos. |

Condiciones obligatorias:

1. Registro de uso de IA.
2. Verificación humana.
3. Defensa oral si el profesorado lo solicita.
4. Capacidad de modificar o explicar el resultado.

---

### 4.3. Rojo — No permitido

Usos prohibidos.

| Uso rojo | Motivo |
|---|---|
| Entregar código completo generado por IA sin entenderlo | Sustituye el aprendizaje. |
| Ocultar que se ha usado IA | Falsea la autoría. |
| Usar IA en pruebas individuales si no está autorizado | Rompe las condiciones de evaluación. |
| Introducir contraseñas, tokens o claves API | Riesgo de seguridad. |
| Introducir datos personales propios o de terceros | Riesgo legal y ético. |
| Subir `.env` o credenciales a GitHub | Riesgo crítico de seguridad. |
| Pedir a la IA que haga la defensa oral | La defensa debe demostrar comprensión propia. |
| Copiar soluciones de otros equipos con ayuda de IA | Plagio. |
| Usar IA para saltarse restricciones del profesorado | Conducta no ética. |
| Mantener código que no se puede explicar | Evidencia no válida. |

Consecuencia posible:

- repetición parcial o total de la entrega;
- defensa reforzada;
- prueba individual;
- invalidación de la evidencia afectada;
- aplicación de las normas del centro si procede.

---

## 5. Registro obligatorio de uso de IA

Todo entregable evaluable que use IA debe incluir un registro.

Nombre recomendado:

```text
docs/registro-ia.md
```

### Plantilla

```markdown
# Registro de uso de IA

Alumno/a:
Equipo:
Hito:
Fecha:
Herramienta usada: Gemini / Jarvis / otra autorizada

---

## Uso 1

### Objetivo

¿Qué querías conseguir?

### Prompt o resumen del prompt

```text
Escribe aquí el prompt o un resumen fiel.
```

### Resultado obtenido

¿Qué te devolvió la IA?

### Qué acepté

¿Qué parte usaste?

### Qué modifiqué yo

¿Qué cambiaste, corregiste o adaptaste?

### Cómo lo verifiqué

¿Cómo comprobaste que era correcto?

### Qué aprendí

¿Qué entiendes ahora que antes no entendías?

### Riesgos detectados

¿Había errores, inseguridad, código raro, datos sensibles o algo que no comprendías?
```

---

## 6. Defensa oral sobre uso de IA

El profesorado podrá hacer preguntas individuales sobre cualquier entrega asistida por IA.

Preguntas tipo:

- ¿Qué parte generó o sugirió la IA?
- ¿Qué parte escribiste tú?
- ¿Qué modificaste?
- ¿Cómo verificaste que funcionaba?
- ¿Qué error detectaste?
- ¿Qué alternativa descartaste?
- ¿Qué pasaría si cambio esta línea?
- ¿Qué datos no debería recibir la IA?
- ¿Dónde podría haber una vulnerabilidad?
- ¿Qué harías si la IA entra en un bucle de errores?

La defensa puede incluir:

- explicar una función;
- modificar un fragmento;
- detectar un bug;
- comparar Java y Python;
- justificar un patrón;
- explicar un test;
- interpretar un stack trace.

---

## 7. Política específica para comparación Java ↔ Python

Desde H2 hasta H7 habrá comparación Java ↔ Python como tarea de casa.

Se permite usar IA de forma amplia para esta comparación, pero se exige:

- registro;
- comprensión;
- verificación;
- defensa.

La comparación debe responder al menos:

```text
¿Qué hace el programa en Java?
¿Cómo se expresa en Python?
¿Qué cambia en sintaxis?
¿Qué cambia en tipos/datos/estructura?
¿Qué parte generó la IA?
¿Qué he modificado yo?
¿Cómo he comprobado que funciona?
```

No se evaluará memorizar Python, sino comprender diferencias y transferir conceptos.

---

## 8. Política específica para código limpio y patrones

La IA puede sugerir mejoras de código limpio o patrones de diseño, pero se aplicarán estas reglas:

1. Primero se entiende el problema.
2. Después se intenta una solución simple.
3. Solo se introduce un patrón si resuelve un problema real.
4. Toda sugerencia de IA debe ser revisada por el alumnado.
5. El alumnado debe poder explicar por qué el cambio mejora o no mejora el código.

Preguntas de defensa:

- ¿Qué problema tenía el código antes?
- ¿Qué principio de código limpio aplicaste?
- ¿La IA propuso algo demasiado complejo?
- ¿Por qué aceptaste o rechazaste el patrón?
- ¿Qué alternativa simple había?

---

## 9. Seguridad, privacidad y secretos

Prohibido introducir en herramientas de IA:

- contraseñas;
- tokens;
- claves API;
- ficheros `.env`;
- datos personales;
- DNI, teléfonos o direcciones;
- información privada de compañeros/as;
- datos reales de empresas;
- credenciales de GitHub, Moodle, Gemini o Jarvis.

Regla para proyectos:

```text
Nunca se suben secretos al repositorio.
Nunca se pegan secretos en una IA.
Nunca se usan datos personales reales para probar.
```

Si se necesita simular:

- usar datos ficticios;
- usar claves falsas como `API_KEY_EJEMPLO`;
- usar `.env.example` sin valores reales;
- documentar cómo configurarlo sin revelar secretos.

---

## 10. Uso de IA por hitos

| Hito | Uso recomendado | Límite |
|---|---|---|
| H0 | Preguntar qué es Scrum o cómo hacer retrospectiva. | No sustituir la reflexión del equipo. |
| H1 | Explicar conceptos básicos: variable, constante, Scanner. | No generar un programa avanzado. |
| H2 | Ayudar a entender errores, bucles, switch, casos de prueba. | No entregar menú completo sin entender. |
| H3 | Comparar colecciones, sugerir pruebas de memoria. | No aceptar estructuras que no se puedan explicar. |
| H4 | Revisar diseño OO o diagramas. | No usar UML generado sin contrastarlo con código. |
| H5 | Sugerir refactorizaciones o patrones. | No aplicar patrones decorativos. |
| H6 | Ayudar con ficheros, logs, README, Docker guiado. | No usar secretos ni configuraciones opacas. |
| H7 | Diseñar prompts y validar IA real/simulada. | No delegar la responsabilidad del agente en la IA. |
| HF | Preparar defensa y portfolio. | No sustituir la defensa personal. |

---

## 11. Evaluación del uso de IA

El uso de IA se valora positivamente cuando:

- está declarado;
- mejora el aprendizaje;
- se verifica;
- se corrige;
- se explica;
- se usa con criterio;
- ayuda a comparar alternativas.

El uso de IA se valora negativamente cuando:

- está oculto;
- sustituye el trabajo;
- genera código no entendido;
- introduce errores no detectados;
- introduce riesgos de seguridad;
- impide la defensa individual.

---

## 12. Modelo de declaración breve en cada entrega

Cada entrega puede incluir al final:

```markdown
## Declaración de uso de IA

He usado IA: sí / no.

Herramienta usada:

Uso principal:

Confirmo que:

- he revisado el resultado;
- puedo explicar el código o documento entregado;
- no he incluido datos personales ni secretos;
- he registrado los usos relevantes en `docs/registro-ia.md`.
```

---

## 13. Mensaje para el alumnado

La IA puede ayudarte mucho, pero no puede aprender por ti.

En este curso se permite usar IA porque forma parte del trabajo profesional actual. Pero precisamente por eso debes aprender a usarla bien: con criterio, trazabilidad, seguridad y responsabilidad.

Si una IA te da una solución que no entiendes, todavía no tienes una solución: tienes una tarea pendiente.

---

## 14. Próximo paso

Crear las rúbricas de hitos:

```text
06-rubricas-hitos.md
```

Las rúbricas deberán incluir una dimensión específica de uso responsable de IA.
