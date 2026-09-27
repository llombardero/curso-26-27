# Estado actual de MiniJarvis

> Este archivo es el punto de reentrada de Hermes.
> Debe contener solo el estado vigente del proyecto, no todo el historial.

## Última actualización

2026-09-25 23:54 CEST. Estado comprobado en el árbol de trabajo y Git.

## Rama y raíz

- Rama activa: `refactor/hitos-v3`.
- Raíz: `/mnt/compartido/Programación-26-27/Minijarvis`.
- `HEAD`: `fc5e9be` (`Revisión diapositvas realizadas`).
- `HEAD` coincide con `origin/refactor/hitos-v3`; no hay commits locales pendientes de publicación.
- El árbol contiene cambios locales de continuidad y las píldoras H1 aún no versionadas que se detallan más abajo.

## Objetivo actual

Completar y revisar las píldoras de consulta del alumnado para las sesiones S206-S214 de H1, manteniendo su publicación progresiva fuera del paquete Moodle hasta que corresponda.

## Decisiones vigentes

- MiniJarvis es un proyecto exclusivo del módulo de Programación de 1.º DAW.
- H1-Temp conserva la referencia de H1 v3; la tabla S206-S215 y los 24 periodos son la temporalización canónica actual.
- H1 introduce los fundamentos del Tema 1 y una decisión elemental mediante microprácticas; H2 aplica y encadena decisiones en menús, bucles, validaciones, pruebas y depuración.
- El producto principal de H1 permanece pequeño; no se premia la complejidad no solicitada.
- La evidencia de proceso se registra una sola vez: diario individual para el proceso personal, Scrum para el trabajo colectivo y Sites para seleccionar y explicar evidencias enlazadas. No existe un portfolio paralelo en H1.
- Los PDF temáticos permanecen en el área docente y se publican progresivamente. No se anticipan todos en el paquete HTML del alumnado.
- Las píldoras de H1 se organizan en un documento autónomo por sesión bajo `01-ALUMNADO/03-SESIONES/h1/pildoras/`; S215 no tiene documento porque su sesión no contiene píldoras.
- Los HTML de las píldoras se conservan como derivados sincronizados. El staging Moodle y los ZIP no se actualizan todavía para no anticipar materiales al alumnado.
- Toda trazabilidad curricular se limita a RA y criterios de Programación.
- Las fuentes se modifican antes que sus derivados; el HTML, las presentaciones y los ZIP se regeneran y verifican después.
- El commit publicado `fc5e9be` no se reescribirá para recuperar la partición por bloques que se había propuesto; esa separación se aplicará únicamente a cambios futuros.

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
- Los 216 cambios revisados quedaron consolidados en `fc5e9be`, que ya está publicado en `origin/refactor/hitos-v3`.
- Se crearon nueve documentos de píldoras para S206-S214 y sus nueve HTML derivados. Cubren las 31 píldoras presentes en las sesiones, con entre tres y cuatro ejemplos por píldora, errores frecuentes y preguntas de comprobación.

## Verificación vigente

- Última suite canónica completa documentada antes de estas píldoras: `30 passed in 2.35s`.
- Validación de las 106 presentaciones: todas en `PASS`; permanecen advertencias informativas de seguridad en algunas sesiones heredadas.
- Validación ad hoc de separación y coherencia H1: 10 presentaciones, 90 diapositivas, 781 líneas de notas sincronizadas y cero marcadores docentes visibles.
- Validación renderizada H1: 10 presentaciones, 90 diapositivas, sin desbordes geométricos, cobertura OCR mínima de 0,67 y media de 0,88.
- Validación renderizada de Sites: escritorio y móvil sin recortes detectados; contrastes WCAG comprobados.
- Última verificación del paquete anterior a estas píldoras: `PASS`, 261 archivos sincronizados.
- Prueba de integridad de los cuatro ZIP regenerados: correcta.
- `git diff --check`: correcto en la comprobación de cierre de las 23:54 CEST.
- Validación específica de píldoras: 9 documentos, 31 secciones canónicas y un mínimo de 3 ejemplos por píldora; sin errores de cobertura.
- Validación de HTML: 9 derivados con jerarquía de encabezados, UTF-8 y bloques de código coherentes con sus fuentes; sin errores estructurales.
- Suite completa actual: `30 passed in 2.01s`, ejecutada directamente con `/home/llombardero/.hermes/venvs/tools/bin/python`; el entorno contiene `pytest 9.1.1` y `python-pptx 1.0.2`.

## Estado actual del repositorio

- `HEAD` y el upstream coinciden en `fc5e9be` (`0` por delante y `0` por detrás).
- `git status` muestra 20 entradas locales: dos documentos de continuidad modificados y 18 archivos sin seguimiento.
- Los 18 archivos nuevos son las nueve fuentes Markdown de píldoras S206-S214 y sus nueve páginas HTML derivadas; no existe una píldora S215 porque esa sesión no contiene ninguna.
- No hay cambios preparados en el índice, commits locales pendientes de publicación ni `push` realizado por Hermes.
- No aparecen bloqueos temporales de LibreOffice ni otros archivos inesperados.

## Riesgos o pendientes

- El staging Moodle y los ZIP están deliberadamente pendientes: `generar_paquete_moodle.py --check` informa de nueve recursos ausentes hasta que se autorice su publicación progresiva.
- Los scripts y pruebas Python que necesiten dependencias externas deben ejecutarse con `/home/llombardero/.hermes/venvs/tools/bin/python`; no se debe modificar el Python del sistema.
- No se pudo completar una inspección visual directa mediante `computer_use`: ni Brave ni Okular expusieron una ventana capturable. La revisión realizada es estructural, no una validación visual de píxeles.
- La amplitud de `fc5e9be` reduce la granularidad histórica. No debe reescribirse porque ya está publicado; los cambios futuros sí deben separarse por bloques coherentes.

## Siguiente acción concreta

Revisar el contenido de las nueve píldoras con criterio docente y decidir en qué sesión se publica cada una; después, solo cuando corresponda, sincronizar Moodle y regenerar los ZIP.
