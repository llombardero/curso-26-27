# Libro del alumnado — Programación y Entornos con MiniJarvis

## 1.º DAW — Curso 2026/2027

Versión: cierre curricular 1.0 — julio 2026

Este libro reúne materiales de estudio con estructura de libro de texto para acompañar el proyecto anual MiniJarvis.

MiniJarvis crece así:

```text
programa básico → menú → memoria → clases → herramientas → persistencia → IA responsable → portfolio final
```

Cada capítulo incluye:

```text
- conceptos básicos explicados con lenguaje de alumnado;
- ejemplo guiado en Java;
- caso práctico MiniJarvis;
- evidencia de Entornos de Desarrollo;
- errores frecuentes;
- preguntas de repaso;
- bloque para portfolio.
```

## Política de entrega del libro

El libro no se entrega completo desde el primer día.

La política acordada para el curso es:

```text
Entrega por capítulo asociado a cada hito.
```

Esto permite que el alumnado estudie cada bloque cuando lo necesita para construir MiniJarvis, sin adelantar complejidad innecesaria.

Regla práctica:

```text
Primero se plantea el reto del hito, después se trabaja el capítulo correspondiente y finalmente se entrega la evidencia MiniJarvis.
```

## Uso de los ejemplos de Laura

Los ejemplos de Laura se muestran después de que el alumnado haya intentado su propia entrega o haya cerrado una primera versión defendible.

No se usan como plantilla para copiar al principio del hito.

Uso adecuado:

```text
- comparar nivel de detalle esperado;
- revisar cómo se justifica una decisión;
- preparar la defensa;
- detectar mejoras posibles;
- calibrar evidencias después del intento propio.
```

Uso no adecuado:

```text
- copiar la solución antes de pensar;
- sustituir la defensa individual;
- entregar la estructura de Laura como si fuera propia;
- evitar la fase de prueba, error y mejora.
```

## Índice por capítulos e hitos

| Capítulo | Título | Archivo | Hitos relacionados | Momento de entrega recomendado |
|---:|---|---|---|---|
| 00 | Cómo usar este libro | `00-como-usar-este-libro.md` | Todo el curso | Inicio de curso, antes de H0/H1. |
| 01 | Primeros programas en Java | `01-primeros-programas-java.md` | H1 | Antes o durante H1-S1/H1-S2. |
| 02 | Variables, constantes y entrada/salida | `02-variables-constantes-entrada-salida.md` | H1 | Durante H1, antes de pedir datos por teclado. |
| 03 | Decisiones, bucles y menús | `03-decisiones-bucles-menus.md` | H2 | Al comenzar H2, antes de construir el menú. |
| 04 | Pruebas, depuración y errores | `04-pruebas-depuracion-errores.md` | H2-H3 | Durante H2, antes de cerrar pruebas manuales y depuración. |
| 05 | Colecciones y memoria temporal | `05-colecciones-memoria-temporal.md` | H3 | Al comenzar H3, antes de implementar memoria con lista. |
| 06 | Programación orientada a objetos | `06-programacion-orientada-objetos.md` | H4 | Al comenzar H4, antes de separar `Agent` y `Memory`. |
| 07 | Encapsulación, responsabilidades y UML | `07-encapsulacion-responsabilidades-uml.md` | H4 | Durante H4, antes de cerrar diagrama y defensa. |
| 08 | Interfaces, extensibilidad y patrones iniciales | `08-interfaces-extensibilidad-patrones.md` | H5 | En H5, después de detectar que el menú crece demasiado. |
| 09 | Ficheros, persistencia y logs | `09-ficheros-persistencia-logs.md` | H6 | Al comenzar H6, antes de guardar memoria en fichero. |
| 10 | IA responsable en proyectos de programación | `10-ia-responsable.md` | H7 | Al comenzar H7, antes de simular o integrar respuestas IA. |
| 11 | Portfolio, defensa y proyecto final | `11-portfolio-defensa-proyecto-final.md` | HF | Al abrir HF, antes de seleccionar evidencias finales. |
| 12 | Revisión editorial del libro | `12-revision-editorial.md` | Profesorado / cierre | Uso docente: revisión final, publicación o adaptación a Moodle/PDF. |

## Cómo estudiar cada capítulo

1. Lee solo el capítulo correspondiente al hito actual.
2. Ejecuta el ejemplo mínimo.
3. Realiza el caso práctico MiniJarvis.
4. Guarda una evidencia en tu portfolio.
5. Prepara una defensa breve: qué hiciste, cómo lo probaste y qué aprendiste.
6. Después de tu primer intento, compara con el ejemplo de Laura si el profesorado lo habilita.

## Regla principal

```text
No basta con que el código funcione. Debe poder probarse, documentarse y defenderse.
```

## Uso de IA

Puedes usar IA para estudiar, pedir ejemplos pequeños o revisar explicaciones.

Debes cumplir siempre estas condiciones:

```text
- registrar el uso;
- validar la respuesta;
- no introducir secretos ni datos personales reales;
- adaptar el resultado a tu propio MiniJarvis;
- defender el código y las decisiones con tus palabras.
```

<!-- AJUSTE-COBERTURA-CONCEPTOS-32 -->

## Ajuste editorial — cobertura completa de conceptos de Programación

Este libro queda alineado con `32-lista-conceptos-programacion-por-tema.md`.

La cobertura completa se consigue así:

| Bloque del libro | Temas cubiertos |
|---|---|
| Capítulos 01-04 | Temas 1 y 3: fundamentos, variables, entrada/salida, condiciones, bucles, pruebas y depuración. |
| Capítulos 05-07 | Temas 2, 4 y 5: colecciones, POO, clases, objetos, constructores, encapsulación y diagramas. |
| Capítulos 08-09 | Temas 5 y 6: interfaces, TDD, excepciones, polimorfismo, patrones, persistencia y trazabilidad. |
| Capítulos 10-11 | Temas 6, 7 y 8 como cierre/ampliación: IA responsable, records/enums, Optional/streams, JavaFX, MVC, arquitectura hexagonal, repositorios, CRUD y transacciones. |

Los conceptos de Tema 7 y Tema 8 se tratan como ampliación o mejora final, salvo que el grupo avance lo suficiente para integrarlos en HF.

Criterio final de tono:

```text
El libro debe ayudar al alumnado a actuar: leer, probar, construir, documentar y defender. No sustituye las sesiones ni los retos; los acompaña hito a hito.
```
