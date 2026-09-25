# S213 — Guía docente

## Comparaciones, lógica y decisiones

| Dato | Valor |
|---|---|
| Hito | H1 — Primer MiniJarvis |
| Duración | 3 periodos; checkpoint proyectable de 45 minutos y taller asociado |
| Fase HEXA | Ejecutar — crear |
| Agrupamiento | Individual con contraste por parejas o equipo cuando la práctica lo requiera |
| Resultado observable | Construir booleanos, combinarlos y usarlos en if/else; reconocer anidamiento y asignación condicional. |
| Evidencia mínima | Quede una mejora concreta. |

## Propósito

Construir booleanos, combinarlos y usarlos en if/else; reconocer anidamiento y asignación condicional.

El concepto se incorpora al Tema 1, pero solo pasa a `Main.java` cuando mejora el producto mínimo. Las demás prácticas se conservan como microejercicios defendibles.

## Material imprescindible

- presentación de S213;
- IntelliJ y JDK cuando haya práctica de código;
- proyecto o microarchivo de prueba;
- diario individual y tablero Scrum del equipo;
- datos ficticios.

## Secuencia de aula

| Tiempo / diap. | Tipo y actuación | Alumnado | Observa | Puerta de avance | Si hay retraso |
|---|---|---|---|---|---|
| 00:00–00:04 / D1 | EJECUTAR: Busca que aparezca true. | Predice. | Si entienden resultado booleano. | respondan true/false. | 3 minutos. |
| 00:04–00:10 / D2 | PÍLDORA DOCENTE 1/6: Explica comparadores y diferencia =/==. Recuerda que Tema 1 no usa == para comparar String. | Predice 4 comparaciones. | Asignación vs comparación. | puedan escribir una comparación simple. | prioriza == != > >=. |
| 00:10–00:14 / D3 | MICROPRÁCTICA: Modela el boolean como dato almacenado. | Cambia hours y predice. | Que vean boolean como variable real. | ambos valores hayan aparecido. | demo colectiva. |
| 00:14–00:20 / D4 | PÍLDORA DOCENTE 2/6: Usa situaciones verbales y muy pocas combinaciones. | Resuelve 3 casos. | Memorizar símbolos sin significado. | puedan verbalizar cada operador. | un ejemplo por operador. |
| 00:20–00:23 / D5 | MICROPRÁCTICA: Pregunta en lenguaje natural qué significa cada expresión. | Traduce código↔︎lenguaje. | Precedencia lógica compleja; no la compliques. | puedan leer una expresión. | solo primera línea. |
| 00:23–00:26 / D6 | PÍLDORA DOCENTE 3/6: Construye el puente conceptual. | Propone una condición posible. | Intentar if(int). | entiendan que if necesita boolean. | 2 minutos. |
| 00:26–00:32 / D7 | PÍLDORA DOCENTE 4/6: Explica llaves, condición y ramas. Ejecuta con dos valores. | Predice ambas rutas. | Que prueben true y false. | puedan señalar qué rama se ejecuta. | no suprimas; núcleo del Tema 1. |
| 00:32–00:35 / D8 | PRUEBA: Exige predicción y las dos pruebas. | Prueba ambas ramas. | Solo probar el caso favorable. | ambas ramas estén verificadas. | hazlo colectivo. |
| 00:35–00:38 / D9 | PÍLDORA DOCENTE 5/6: Solo enseña a leer la idea. No conviertas H1 en una sesión de condicionales complejos. | Explica qué condición se mira primero. | Sobrecarga cognitiva. | puedan leer el esquema. | menciona y sigue. |
| 00:38–00:40 / D10 | PÍLDORA DOCENTE 6/6: Muestra equivalencia con una elección de valor sencilla. No digas que sustituye a cualquier if. | Identifica condición, valor true y valor false. | Copiado sin lectura. | puedan señalar tres partes. | solo muestra y explica 90 segundos. |
| 00:40–00:43 / D11 | ACTIVIDAD: Circula; reduce condiciones complejas a preguntas sí/no. | Programa y prueba. | = vs ==, if no booleano, ramas sin probar. | dos casos funcionen. | una práctica guiada colectiva. |
| 00:43–00:45 / D12 | CIERRE: Conecta con mantenibilidad y preparación de documentación. | Mejora y registra. | Código que funciona pero no pueden explicar. | quede una mejora concreta. | solo selección oral. |

## Qué debes explicar

- **PÍLDORA DOCENTE 1/6:** Explica comparadores y diferencia =/==. Recuerda que Tema 1 no usa == para comparar String.
- **PÍLDORA DOCENTE 2/6:** Usa situaciones verbales y muy pocas combinaciones.
- **PÍLDORA DOCENTE 3/6:** Construye el puente conceptual.
- **PÍLDORA DOCENTE 4/6:** Explica llaves, condición y ramas. Ejecuta con dos valores.
- **PÍLDORA DOCENTE 5/6:** Solo enseña a leer la idea. No conviertas H1 en una sesión de condicionales complejos.
- **PÍLDORA DOCENTE 6/6:** Muestra equivalencia con una elección de valor sencilla. No digas que sustituye a cualquier if.

## Ejemplo o demostración preparada

**D1 · ¿Qué devuelve 5 \> 3? —** No devuelve 5 ni 3.<br>
Devuelve una respuesta lógica.

**D2 · Comparar produce boolean —** IGUAL / DISTINTO: == / != \| ORDEN: \< \<= / \> \>= \| RESULTADO: true / false

**D3 · Guarda el resultado de comparar —** int hours = 5;<br>
boolean enough = hours \>= 4;<br>
System.out.println(enough);

**D4 · AND, OR, NOT —** &&: true si se cumplen las dos condiciones \| \|\|: true si se cumple al menos una \| !: invierte true ↔ false

**D5 · Combina condiciones —** boolean canStart = hasName && hasGoal;<br>
boolean needsHelp = !canStart \|\| hasError;

**D6 · Del boolean a una decisión —** Una condición es algo que produce true o false.<br>
<br>
if (...) usa ese resultado para decidir qué bloque ejecutar.

**D7 · if / else: dos caminos —** if (hours \>= 4) {<br>
System.out.println("Objetivo alcanzado");<br>
} else {<br>
System.out.println("Objetivo pendiente");<br>
}

**D8 · Una condición, dos casos —** Caso A: hours = 5<br>
Caso B: hours = 2<br>
<br>
Escribe salida esperada antes de ejecutar.

**D9 · Anidamiento: reconocer la idea —** DECISIÓN EXTERIOR: if (condA) {<br>
...<br>
} \| DENTRO PUEDE HABER OTRA: if (condA) {<br>
if (condB) { ... }<br>
}

**D10 · Asignación condicional ?: —** String message = hours \>= 4<br>
? "Objetivo alcanzado"<br>
: "Objetivo pendiente";

**D11 · Micropráctica defendible —** Dato → comparación → boolean → if/else → salida<br>
<br>
Prueba una entrada que haga true y otra que haga false.

**D12 · Revisa una línea que ahora entiendes mejor —** Elige una mejora de nombres, comentario o condición y regístrala.

## Consigna que se entrega al alumnado

1. Predice antes de ejecutar cuando haya código.
2. Realiza la micropráctica o modificación prevista.
3. Prueba el caso normal y, cuando exista una decisión o conversión, también el caso alternativo o erróneo.
4. Conserva el código o resultado en el repositorio o espacio indicado.
5. Registra una sola entrada en el diario individual; no crees un informe paralelo.

## Qué observar mientras trabajan

- Si entienden resultado booleano.
- Asignación vs comparación.
- Que vean boolean como variable real.
- Memorizar símbolos sin significado.
- Precedencia lógica compleja; no la compliques.
- Intentar if(int).
- Que prueben true y false.
- Solo probar el caso favorable.
- Sobrecarga cognitiva.
- Copiado sin lectura.
- = vs ==, if no booleano, ramas sin probar.
- Código que funciona pero no pueden explicar.

## Criterios para considerar cerrada la sesión

- Respondan true/false.
- Puedan escribir una comparación simple.
- Ambos valores hayan aparecido.
- Puedan verbalizar cada operador.
- Puedan leer una expresión.
- Entiendan que if necesita boolean.
- Puedan señalar qué rama se ejecuta.
- Ambas ramas estén verificadas.
- Puedan leer el esquema.
- Puedan señalar tres partes.
- Dos casos funcionen.
- Quede una mejora concreta.
- La persona puede señalar la evidencia y explicar qué demuestra.

## Seguridad y uso de IA

- Trabajar con datos ficticios.
- No publicar credenciales, tokens, claves ni información personal.
- Si la IA interviene de forma sustantiva, registrar propuesta, cambios propios y validación; no aceptar código que no pueda defenderse.

## Comprobación final

**¿Qué puedes señalar, explicar, predecir o modificar para demostrar el aprendizaje de esta sesión?**

## Anotación docente al terminar

- alumnado que necesita reentrada;
- evidencia pendiente;
- error común;
- ajuste temporal necesario sin eliminar el núcleo conceptual.
