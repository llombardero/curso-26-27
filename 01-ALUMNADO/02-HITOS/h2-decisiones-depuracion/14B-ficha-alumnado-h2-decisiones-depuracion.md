# H2 — Agente con decisiones y depuración

<!-- HEXA-CICLO-COMPLETO-POR-HITO:START -->

## Ciclo HEXA obligatorio del reto H2

**Reto del hito:** Transformar MiniJarvis en un programa interactivo con decisiones, repetición y depuración reproducible.

Debes conservar evidencias de las cuatro fases. Entregar solo el producto final no demuestra el ciclo completo.

| Fase | Pregunta que guía la fase | Acción del profesorado | Acción y evidencia del alumnado |
|---|---|---|---|
| **H — Hecho / reto** | ¿Qué problema real debemos resolver y con qué límites? | Presenta contexto, producto, restricciones, criterios y diagnóstico; no da todavía la solución completa. | Reformula el reto, identifica lo que sabe/no sabe y deja una ficha inicial con criterios de éxito. |
| **E — Exploración** | ¿Qué alternativas, hipótesis o pruebas iniciales ayudan a entenderlo? | Propone preguntas, ejemplos mínimos, casos y límites seguros. | Observa, compara, predice, prueba alternativas y registra decisiones o bloqueos. |
| **X — eXplicación** | ¿Qué conceptos permiten explicar lo observado y decidir con criterio? | Formaliza vocabulario, sintaxis, modelo mental, errores frecuentes, seguridad y criterios de calidad. | Explica con palabras propias, conecta teoría y exploración y corrige sus hipótesis. |
| **A — Aplicación** | ¿Cómo construimos, comprobamos, documentamos y defendemos la solución? | Desbloquea, exige pruebas y comprueba autoría y transferencia. | Implementa el producto, lo prueba, documenta evidencias, realiza review/defensa y propone mejora. |

### Temporalización mínima explícita

H2-S1–S9; 405 min mínimos en la guía autónoma. Los tiempos de fases se reservan dentro de las sesiones indicadas; los rangos pueden solaparse cuando una sesión cierra una fase y abre la siguiente.

| Fase | Reserva y momento recomendado | Puerta de salida |
|---|---|---|
| H | H2-S1; 45 min | Reto reformulado, límites y criterio de éxito visibles. |
| E | H2-S1–S2; 90 min integrados | Hipótesis, comparación, prueba inicial o decisiones justificadas. |
| X | H2-S2–S4; 90 min integrados | Explicación individual breve y conexión con el producto. |
| A | H2-S5–S9; 180 min integrados | Producto comprobado, documentación, defensa y mejora. |

**Expediente HEXA mínimo del hito:** mapa de comandos, hipótesis de flujo, explicación de condiciones/bucle, menú funcional, pruebas, depuración y defensa.

Regla de avance: puede haber prototipos durante E, pero no se considera completada A si faltan evidencias de H, E o X. Si una fase falta, se recupera esa fase y su evidencia; no se repite automáticamente todo el hito.

<!-- HEXA-CICLO-COMPLETO-POR-HITO:END -->


## Ficha para el alumnado

Curso: 1.º DAW — Programación + Entornos de Desarrollo

---

## 1. Reto

Vais a convertir MiniJarvis H1 en un agente con menú de comandos.

Ahora el programa no debe terminar después del primer saludo. Debe seguir funcionando hasta que la persona usuaria escriba:

```text
salir
```

---

## 2. Qué debe hacer MiniJarvis H2

Comandos mínimos:

| Comando | Qué debe hacer |
|---|---|
| `ayuda` | Mostrar comandos disponibles. |
| `saluda` | Saludar al usuario. |
| `estado` | Mostrar un estado simple del agente. |
| `salir` | Terminar el programa. |
| comando desconocido | Mostrar un mensaje de ayuda o error controlado. |

---

## 3. Qué entra en H2

```text
[x] Menú.
[x] Bucle hasta escribir salir.
[x] if/else o switch.
[x] Comandos básicos.
[x] Comando desconocido.
[x] Pruebas manuales.
[x] Depuración con breakpoint.
[x] Comparación Java ↔ Python.
```

---

## 4. Qué NO entra todavía

```text
[ ] Memoria con listas o mapas.
[ ] Ficheros.
[ ] Varias clases avanzadas.
[ ] Patrones de diseño.
[ ] Conexión con IA real.
[ ] Base de conocimiento.
```

Eso se trabajará en hitos posteriores.

---

## 5. Entregables

```text
h2-decisiones-depuracion/
├── README.md
├── src/
│   └── Main.java
└── docs/
    ├── evidencia-ejecucion-h2.md
    ├── pruebas-h2.md
    ├── depuracion-h2.md
    ├── incidencia-h2.md
    ├── comparacion-java-python-h2.md
    ├── registro-ia.md
    └── defensa-h2.md
```

Plantillas disponibles:

```text
plantillas/README-h2-template.md
plantillas/evidencia-ejecucion-h2-template.md
plantillas/pruebas-h2-template.md
plantillas/depuracion-h2-template.md
plantillas/incidencia-h2-template.md
plantillas/comparacion-java-python-h2-template.md
plantillas/registro-ia-h2-template.md
plantillas/defensa-h2-template.md
```

---

## 6. Pasos recomendados

1. Recuperar el código de H1.
2. Diseñar la tabla de comandos.
3. Crear un bucle `while`.
4. Leer comandos con `Scanner`.
5. Comparar comandos con `.equals()` o usar `switch`.
6. Añadir `salir` como salida controlada.
7. Gestionar comandos desconocidos.
8. Probar cada comando.
9. Usar un breakpoint.
10. Documentar pruebas, depuración e incidencias.

---

## 7. Uso de IA

Puedes usar IA para entender errores, pedir ejemplos de pruebas o comparar con Python.

Debes registrar el uso si afecta a la entrega.

No puedes entregar un menú completo generado por IA si no puedes explicarlo.

---

## 8. Preguntas de defensa

Prepárate para responder:

```text
¿Cómo se repite el menú?
¿Qué ocurre si escribo un comando incorrecto?
¿Qué variable controla la salida?
¿Qué diferencia hay entre == y equals en Java?
¿Dónde pusiste el breakpoint?
¿Qué variable observaste?
¿Qué pruebas hiciste?
¿Qué diferencia viste entre Java y Python?
```

---

## 9. Checklist antes de entregar

```text
[ ] El programa se ejecuta.
[ ] El menú se repite.
[ ] Existe el comando ayuda.
[ ] Existe el comando saluda.
[ ] Existe el comando estado.
[ ] Existe el comando salir.
[ ] Hay respuesta para comando desconocido.
[ ] Hay plan de pruebas.
[ ] Hay evidencia de depuración.
[ ] Hay incidencia documentada si apareció.
[ ] Hay comparación Java ↔ Python.
[ ] He registrado IA si la he usado.
[ ] Puedo defender el flujo del programa.
```

## Cobertura curricular de Programación

Este hito queda alineado con el mapa `32-lista-conceptos-programacion-por-tema.md`.

```text
Hito: H2
Temas de referencia: Temas 1 y 3
Foco: decisiones, menú, repetición y depuración
```

Conceptos que deben trabajarse o, como mínimo, quedar conectados con evidencias del alumnado:

- if/else
- boolean
- comparaciones
- switch
- enhanced switch como ampliación
- while
- do-while como comparación
- for
- condición de salida
- bucle infinito
- pruebas manuales
- error de compilación
- error lógico
- eficiencia básica

Criterio docente de cierre:

- El alumnado no solo entrega el producto; debe poder señalar dónde aparece cada concepto en su código, README, pruebas o defensa.
- Si un concepto se marca como ampliación, no penaliza al alumnado que alcance el mínimo, pero sí orienta mejora, recuperación o enriquecimiento.
- La defensa debe incluir al menos una pregunta de comprensión sobre los conceptos nuevos del hito.

