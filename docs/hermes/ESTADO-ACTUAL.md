# Estado actual de MiniJarvis

> Este archivo es el punto de reentrada de Hermes.
> Debe contener solo el estado vigente del proyecto, no todo el historial.

## Última actualización

2026-09-25 02:47 CEST. Estado comprobado en el árbol de trabajo y en Git.

## Rama activa

`refactor/hitos-v3`

## Raíz del proyecto

`/mnt/compartido/Programación-26-27/Minijarvis`

`pwd` y `git rev-parse --show-toplevel` coinciden con esta ruta.

## Objetivo actual

Preparar y validar la transición del modelo de hitos hacia la versión 3 tomando `H1-Temp` como referencia, manteniendo únicamente H0, H1 y H2 como foco de la rama de refactorización.

## Decisiones vigentes

- MiniJarvis es, en esta rama, un proyecto exclusivo del módulo de Programación de 1.º DAW.
- H1-Temp contiene la referencia de la versión 3 del modelo de hitos.
- Antes de adaptar H0 y H2 hay que deducir qué caracteriza realmente a H1 v3.
- Antes de modificar H0, H1 o H2 hay que comparar H1 actual con `H1-Temp` y presentar un plan si se proponen cambios estructurales.
- La auditoría de evidencias del alumnado en H0-H2 es prioritaria y debe favorecer la evidencia única sin perder aprendizaje, trazabilidad ni evaluación.
- Toda trazabilidad curricular debe limitarse a RA y criterios de Programación.
- No deben eliminarse ni fusionarse evidencias sin análisis y autorización.
- Debe preservarse el trabajo manual y modificarse la fuente o el generador antes que un artefacto generado.
- Git y GitHub deben utilizarse de forma conservadora, evitando operaciones destructivas.
- El contexto de Hermes debe gestionarse mediante sesiones acotadas, compresión preventiva y persistencia en archivos.

## Trabajo completado relevante

- La referencia de H1 v3 está conservada en `H1-Temp`; Git registra siete archivos en ese directorio.
- El commit actual es `95dd434` (`archivo: mantiene las referencias a H1 v3 antes de refactorizar`).
- `.hermes.md` y los cuatro documentos de `docs/hermes/` están presentes en el árbol de trabajo.
- Se comprobó el tamaño del prompt compacto mediante `minijarvis prompt-size`.
- Se verificaron la raíz, la rama, el estado del árbol de trabajo y los cinco commits más recientes.

## Estado actual del repositorio

- `HEAD` está en `95dd434`; también apuntan a ese commit `archive/pre-hitos-v3` y `origin/archive/pre-hitos-v3`.
- El índice está limpio: no hay cambios preparados para commit.
- El árbol de trabajo contiene 112 archivos modificados, 3 eliminados y 4 entradas sin seguimiento.
- Entre las entradas sin seguimiento están `.hermes.md`, `CONTINUIDAD_MINIJARVIS.md`, `docs/` y la nueva presentación inicial de Programación.
- Los cambios locales afectan a materiales de alumnado y profesorado, ejemplos privados, generadores, pruebas y artefactos binarios.
- `git diff --check` no detecta errores de espacios en los cambios rastreados actuales.

## Tareas pendientes

1. Analizar H1 actual frente a `H1-Temp` y determinar qué define el modelo v3.
2. Identificar las consecuencias sobre metodología, secuencia, productos, evidencias, evaluación, Scrum, HEXA, IA, sesiones, presentaciones y entregables.
3. Realizar la auditoría de evidencias de H0, H1 y H2.
4. Proponer una simplificación del sistema de evidencias sin eliminar ni fusionar elementos todavía.
5. Definir el plan de adaptación de H0 y H2 al modelo v3.
6. Clasificar los cambios locales existentes como trabajo manual, fuente, generado, sustitución, eliminación o temporal antes de consolidarlos.
7. Realizar cambios estructurales únicamente después de presentar el plan y recibir autorización.

## Riesgos o bloqueos

- El árbol de trabajo tiene muchos cambios previos sin preparar; no deben mezclarse, descartarse ni atribuirse sin revisar su origen y función.
- Hay tres eliminaciones, incluida documentación de Entornos y una presentación, que deben validarse como retiradas intencionadas antes de consolidarlas.
- Existen cambios fuera del foco H0-H2 y en scripts generadores; ampliar el refactor sin delimitar alcance aumentaría el riesgo de cambios colaterales.
- `docs/` y `.hermes.md` aún no están bajo seguimiento en esta rama.
- No hay un bloqueo técnico para el análisis de lectura, pero cualquier cambio estructural está bloqueado hasta disponer de diagnóstico, plan y autorización.

## Siguiente acción concreta

Realizar, sin modificar archivos, una comparación estructurada entre H1 actual y las fuentes de `H1-Temp`. El resultado debe identificar los rasgos de la versión 3, sus dependencias y los archivos de H0-H2 potencialmente afectados, y terminar con una propuesta de plan para aprobación.
