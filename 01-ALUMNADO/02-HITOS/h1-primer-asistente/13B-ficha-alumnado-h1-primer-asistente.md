# H1 — Primer asistente básico

<!-- HEXA-CICLO-COMPLETO-POR-HITO:START -->

## Ciclo HEXA obligatorio del reto H1

**Reto del hito:** Construir el primer MiniJarvis Java por consola, pequeño, ejecutable y defendible.

Debes conservar evidencias de las cuatro fases. Entregar solo el producto final no demuestra el ciclo completo.

| Fase | Pregunta que guía la fase | Acción del profesorado | Acción y evidencia del alumnado |
|---|---|---|---|
| **H — Hecho / reto** | ¿Qué problema real debemos resolver y con qué límites? | Presenta contexto, producto, restricciones, criterios y diagnóstico; no da todavía la solución completa. | Reformula el reto, identifica lo que sabe/no sabe y deja una ficha inicial con criterios de éxito. |
| **E — Exploración** | ¿Qué alternativas, hipótesis o pruebas iniciales ayudan a entenderlo? | Propone preguntas, ejemplos mínimos, casos y límites seguros. | Observa, compara, predice, prueba alternativas y registra decisiones o bloqueos. |
| **X — eXplicación** | ¿Qué conceptos permiten explicar lo observado y decidir con criterio? | Formaliza vocabulario, sintaxis, modelo mental, errores frecuentes, seguridad y criterios de calidad. | Explica con palabras propias, conecta teoría y exploración y corrige sus hipótesis. |
| **A — Aplicación** | ¿Cómo construimos, comprobamos, documentamos y defendemos la solución? | Desbloquea, exige pruebas y comprueba autoría y transferencia. | Implementa el producto, lo prueba, documenta evidencias, realiza review/defensa y propone mejora. |

### Temporalización mínima explícita

H1-S1–S7; 315 min mínimos en la guía autónoma. Los tiempos de fases se reservan dentro de las sesiones indicadas; los rangos pueden solaparse cuando una sesión cierra una fase y abre la siguiente.

| Fase | Reserva y momento recomendado | Puerta de salida |
|---|---|---|
| H | H1-S1; 45 min | Reto reformulado, límites y criterio de éxito visibles. |
| E | H1-S1–S2; 60 min integrados | Hipótesis, comparación, prueba inicial o decisiones justificadas. |
| X | H1-S2–S4; 75 min integrados | Explicación individual breve y conexión con el producto. |
| A | H1-S4–S7; 135 min integrados | Producto comprobado, documentación, defensa y mejora. |

**Expediente HEXA mínimo del hito:** ficha del reto, salida diseñada, explicación de Main/variables/Scanner, programa, README, evidencia y defensa.

Regla de avance: puede haber prototipos durante E, pero no se considera completada A si faltan evidencias de H, E o X. Si una fase falta, se recupera esa fase y su evidencia; no se repite automáticamente todo el hito.

<!-- HEXA-CICLO-COMPLETO-POR-HITO:END -->


## Ficha para el alumnado

Curso: 1.º DAW — Programación + Entornos de Desarrollo

Proyecto anual:

```text
MiniJarvis: construcción progresiva de un pequeño agente IA propio
```

---

## 1. Reto

Vas a crear la primera versión técnica de MiniJarvis.

Será un programa Java muy sencillo que se ejecuta por consola.

El programa debe:

- mostrar un saludo inicial;
- pedir tu nombre;
- guardar tu nombre en una variable;
- usar al menos una constante;
- mostrar varios mensajes relacionados con el proyecto;
- poder ejecutarse en IntelliJ;
- tener un README básico.

---

## 2. Muy importante: qué NO entra todavía

En H1 todavía NO debes incluir:

```text
[ ] Menú.
[ ] Bucles.
[ ] switch.
[ ] Memoria.
[ ] Listas o mapas.
[ ] Clases propias adicionales.
[ ] Ficheros.
[ ] Conexión con Gemini, Jarvis u otra IA real.
[ ] Patrones de diseño.
```

Esto se trabajará en hitos posteriores.

En H1 buscamos una versión pequeña, clara y defendible.

---

## 3. Producto esperado

Ejemplo de ejecución orientativo:

```text
Hola, soy MiniJarvis.
¿Cómo te llamas? Laura
Encantada, Laura.
Este curso vamos a crear un pequeño agente IA.
Curso de inicio: 2026.
Primer objetivo: aprender la estructura básica de un programa Java.
```

Tu salida puede tener otros mensajes, pero debe mantener el nivel básico del hito.

---

## 4. Pasos de trabajo

### Paso 1 — Crear proyecto

```text
[ ] Crear un proyecto Java en IntelliJ.
[ ] Crear la clase Main.
[ ] Comprobar que el proyecto ejecuta.
```

### Paso 2 — Primer mensaje

```text
[ ] Mostrar un saludo inicial con System.out.println.
```

### Paso 3 — Constantes y variables

```text
[ ] Crear una constante para el nombre del asistente.
[ ] Crear al menos otra constante sencilla si procede.
[ ] Usar nombres claros.
```

Ejemplos de nombres claros:

```text
ASSISTANT_NAME
COURSE_YEAR
userName
```

### Paso 4 — Entrada por teclado

```text
[ ] Usar Scanner.
[ ] Pedir el nombre de la persona usuaria.
[ ] Guardar el nombre en una variable.
[ ] Usar esa variable en un mensaje.
```

### Paso 5 — Mensajes finales

```text
[ ] Mostrar varios mensajes sobre el proyecto MiniJarvis.
[ ] Comprobar que todo se entiende.
[ ] Evitar añadir funciones que no son de H1.
```

### Paso 6 — README

```text
[ ] Explicar qué hace el programa.
[ ] Explicar cómo se ejecuta.
[ ] Añadir ejemplo de ejecución.
[ ] Indicar qué no incluye todavía.
```

---

## 5. Estructura mínima de entrega

```text
h1-primer-asistente/
├── README.md
├── src/
│   └── Main.java
└── docs/
    ├── evidencia-ejecucion-h1.md
    ├── portfolio-h1.md
    ├── registro-ia.md      # solo si has usado IA
    ├── defensa-h1.md
    ├── incidencia-h1.md    # si aparece una incidencia importante
    └── vocabulario-h1.md   # si lo pide el profesor/a
```

Si todavía no se usa carpeta `docs/`, el profesor/a indicará el formato alternativo.

Plantillas específicas disponibles en este paquete H1:

```text
plantillas/README-h1-template.md
plantillas/evidencia-ejecucion-h1-template.md
plantillas/portfolio-h1-template.md
plantillas/registro-ia-h1-template.md
plantillas/defensa-h1-template.md
plantillas/incidencia-h1-template.md
plantillas/vocabulario-h1-template.md
```

---

## 6. README mínimo

Puedes usar esta estructura:

```markdown
# H1 — Primer asistente por consola

## Qué hace

Este programa muestra un saludo, pide el nombre del usuario y muestra mensajes iniciales del proyecto MiniJarvis.

## Cómo ejecutar

Desde IntelliJ:

1. Abrir el proyecto.
2. Abrir `src/Main.java`.
3. Pulsar Run.

## Ejemplo de ejecución

```text
Hola, soy MiniJarvis.
¿Cómo te llamas? Laura
Encantada, Laura.
```

## Qué no incluye todavía

No incluye menú, bucles, memoria ni IA real.
```

---

## 7. Uso de IA en H1

Puedes usar IA para:

- preguntar qué es una variable;
- preguntar qué es una constante;
- pedir explicación de `Scanner`;
- entender un error;
- revisar la claridad del README.

No puedes usar IA para:

- generar el programa completo y entregarlo sin entender;
- añadir cosas que no pertenecen a H1;
- ocultar que la has usado;
- entregar código que no puedes explicar.

Si usas IA para la entrega, regístralo en:

```text
docs/registro-ia.md
```

Debes poder explicar:

```text
Qué pediste.
Qué aceptaste.
Qué cambiaste tú.
Cómo comprobaste que funcionaba.
Qué aprendiste.
```

---

## 8. Preguntas de defensa

Prepárate para responder:

```text
¿Dónde empieza el programa?
¿Qué variable guarda el nombre?
¿Qué constante has usado?
¿Qué hace Scanner?
¿Qué diferencia hay entre print y println?
¿Cómo se ejecuta desde IntelliJ?
¿Por qué todavía no hay menú?
¿Has usado IA? ¿Para qué?
```

---

## 9. Checklist antes de entregar

```text
[ ] Existe src/Main.java.
[ ] El programa se ejecuta.
[ ] Hay una clase Main.
[ ] Hay método main.
[ ] El programa muestra un saludo.
[ ] El programa pide el nombre.
[ ] El nombre se guarda en una variable.
[ ] Hay al menos una constante.
[ ] Los nombres son claros.
[ ] No hay menú, bucles, switch ni IA real.
[ ] El README explica cómo ejecutar.
[ ] Hay evidencia de ejecución.
[ ] He registrado la IA si la he usado.
[ ] Puedo explicar cada línea importante.
```

---

## 10. Idea clave

En H1 no buscamos un agente avanzado.

Buscamos una primera versión pequeña que puedas entender completamente.

Frase clave:

```text
Si puedo ejecutarlo, explicarlo y defenderlo, voy por buen camino.
```

## Cobertura curricular de Programación

Este hito queda alineado con el mapa `32-lista-conceptos-programacion-por-tema.md`.

```text
Hito: H1
Temas de referencia: Tema 1
Foco: primer programa Java por consola y asistente mínimo
```

Conceptos que deben trabajarse o, como mínimo, quedar conectados con evidencias del alumnado:

- programa
- instrucción
- sintaxis
- comentarios
- variable
- tipo de dato
- literal
- String
- Scanner
- entrada/salida
- operadores
- expresiones
- conversiones básicas

Criterio docente de cierre:

- El alumnado no solo entrega el producto; debe poder señalar dónde aparece cada concepto en su código, README, pruebas o defensa.
- Si un concepto se marca como ampliación, no penaliza al alumnado que alcance el mínimo, pero sí orienta mejora, recuperación o enriquecimiento.
- La defensa debe incluir al menos una pregunta de comprensión sobre los conceptos nuevos del hito.

