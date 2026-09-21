# Ejemplo de Site del Equipo Ada - H5

## Reto e incremento

Reto: Añadir herramientas con bajo impacto y refactorizar sin romper el programa.

Incremento: MiniJarvis extensible con refactorización y revisión Git.

## Decisión principal

Aplicamos un Command simplificado mediante la interfaz Tool.

## Pruebas realizadas

Ejecuté pruebas de regresión antes y después de la refactorización.

Resultado: Las herramientas comparten un contrato y el menú sigue funcionando.

## Evidencias seleccionadas

- Sheet Scrum: `URL_RESTRINGIDA_EJEMPLO`.
- Evidencia del incremento: `URL_RESTRINGIDA_EJEMPLO`.
- Versión evaluada: `h5-entrega`.

## Revisión

El equipo mostró el incremento, reprodujo la prueba principal y anotó la retroalimentación recibida.

## Retrospectiva y siguiente mejora

Detectamos este problema: Cada comando nuevo obligaba a modificar un bloque grande de condiciones.

Siguiente acción: Guardar memoria e historial entre ejecuciones.
