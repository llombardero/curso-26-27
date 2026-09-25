# Estado actual de MiniJarvis

> Este archivo es el punto de reentrada de Hermes.
> Debe contener solo el estado vigente del proyecto, no todo el historial.

## Última actualización

2026-09-25 17:26 CEST. Estado comprobado en el árbol de trabajo y Git.

## Rama y raíz

- Rama activa: `refactor/hitos-v3`.
- Raíz: `/mnt/compartido/Programación-26-27/Minijarvis`.
- `HEAD`: `c738289` (`Actualizado estado actual y sincronizado github Itos-v3`).
- `HEAD` coincide con `origin/refactor/hitos-v3`; no hay commits locales pendientes de publicación.
- No hay cambios preparados en el índice.

## Objetivo actual

Organizar para su consolidación los cambios ya revisados de la migración H0-H2 al modelo de hitos v3, sin mezclar fuentes, documentación técnica y artefactos generados.

## Decisiones vigentes

- MiniJarvis es un proyecto exclusivo del módulo de Programación de 1.º DAW.
- H1-Temp conserva la referencia de H1 v3; la tabla S206-S215 y los 24 periodos son la temporalización canónica actual.
- H1 introduce los fundamentos del Tema 1 y una decisión elemental mediante microprácticas; H2 aplica y encadena decisiones en menús, bucles, validaciones, pruebas y depuración.
- El producto principal de H1 permanece pequeño; no se premia la complejidad no solicitada.
- La evidencia de proceso se registra una sola vez: diario individual para el proceso personal, Scrum para el trabajo colectivo y Sites para seleccionar y explicar evidencias enlazadas. No existe un portfolio paralelo en H1.
- Los PDF temáticos permanecen en el área docente y se publican progresivamente. No se anticipan todos en el paquete HTML del alumnado.
- Toda trazabilidad curricular se limita a RA y criterios de Programación.
- Las fuentes se modifican antes que sus derivados; el HTML, las presentaciones y los ZIP se regeneran y verifican después.

## Trabajo completado relevante

- Se auditó la conservación de las dos guías H1 condensadas frente a `HEAD`, `H1-Temp` y S206-S215. El núcleo se conserva; el desarrollo detallado está trasladado a las sesiones.
- Se recuperaron referencias operativas que habían quedado debilitadas: trazabilidad curricular, fuente integral del ejemplo, checklist, preguntas de defensa, apoyos, uso de IA, recuperación y ampliación.
- S212 usa `java.util.Scanner`, una instancia reutilizable y cierre explícito; se sincronizaron la ficha del alumnado, la guía docente, el HTML y la presentación.
- Se revisaron los dos modelos visuales de Google Sites en escritorio y móvil: cobertura OCR 0,89-0,95, sin texto en los bordes y con contrastes mínimos superiores a 5:1.
- Las diez presentaciones H1 separan ahora la proyección y las notas: la secuencia, los tiempos y las claves docentes quedan en las notas del título; las diapositivas visibles conservan objetivos, ejemplos, actividad, evidencia, seguridad y cierre para el alumnado.
- Las diez presentaciones H1 se regeneraron con 9 diapositivas cada una: 90 en total, cero elementos fuera del lienzo y cobertura OCR mínima de 0,67.
- Los siete HTML regenerados de H3, H5 y HF reproducen exactamente sus fuentes canónicas actuales; se mantienen como sincronización derivada, no como ampliación curricular.
- Se añadió `generar_paquete_moodle.py` con modo `--check`, ZIP determinista y sincronización de recursos del alumnado, tareas Moodle y copias de rúbricas.
- Se regeneraron `01-ALUMNADO-HTML/`, `05-PAQUETE-MOODLE/`, `Minijarvis-paquete-moodle.zip`, los ZIP del alumnado, el ZIP local de presentaciones y `MANIFIESTO-ARCHIVOS.md`.

## Verificación vigente

- Suite canónica: `30 passed in 2.35s`.
- Validación de las 106 presentaciones: todas en `PASS`; permanecen advertencias informativas de seguridad en algunas sesiones heredadas.
- Validación ad hoc de separación y coherencia H1: 10 presentaciones, 90 diapositivas, 781 líneas de notas sincronizadas y cero marcadores docentes visibles.
- Validación renderizada H1: 10 presentaciones, 90 diapositivas, sin desbordes geométricos, cobertura OCR mínima de 0,67 y media de 0,88.
- Validación renderizada de Sites: escritorio y móvil sin recortes detectados; contrastes WCAG comprobados.
- `generar_paquete_moodle.py --check`: `PASS`, 261 archivos sincronizados.
- Prueba de integridad de los cuatro ZIP regenerados: correcta.
- `git diff --check`: correcto.

## Estado actual del repositorio

- `git status --porcelain` muestra 216 entradas: 200 modificadas, 8 eliminadas y 8 entradas sin seguimiento.
- El diff rastreado comprende 208 archivos.
- No hay cambios preparados en el índice.
- Los bloqueos temporales de LibreOffice quedan excluidos de cualquier commit; no aparece ninguno en el estado actual.

## Partición propuesta, todavía sin commits

1. Fuentes pedagógicas H0-H2 y evidencia única: guías, fichas, sesiones, rúbricas, calendario y frontera H1-H2.
2. Modelos de Google Sites y documentación del ecosistema digital.
3. Generadores, dependencias, pruebas y documentación técnica.
4. HTML generado del alumnado y copias sincronizadas del staging Moodle.
5. Presentaciones H1 y manifiesto actualizado.
6. ZIP públicos y paquete Moodle reproducible.
7. Documentación de continuidad y seguimiento.

## Riesgos o pendientes

- El árbol es amplio y mezcla fuentes, binarios y derivados; debe revisarse y prepararse por bloques, nunca con un `git add .` global.
- Los cambios derivados de H3, H5 y HF son reproducibles desde fuentes limpias, pero conviene aislarlos en el bloque de artefactos generados.
- Falta convertir la partición propuesta en una secuencia de staging y commits; esta sesión no tiene autorización para crear commits.

## Siguiente acción concreta

Revisar la partición propuesta y, cuando exista autorización expresa, preparar cada bloque por separado, comprobar su diff y ejecutar las verificaciones focalizadas antes de crear el commit correspondiente.
