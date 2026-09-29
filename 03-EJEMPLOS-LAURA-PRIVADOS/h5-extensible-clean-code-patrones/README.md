# H5 — Extensibilidad, código limpio y patrones

> Ejemplo privado de Laura. Mostrar solo después del intento propio del alumnado.

## Objetivo

Añadir herramientas con bajo impacto y refactorizar sin romper.

## Arquitectura de evidencias

Versión estable: `h5-entrega`. El repositorio y su README son la evidencia técnica canónica.

- Diario individual evolutivo: `../FUENTES-CURSO/01-Diario-individual-MiniJarvis.xlsx`.
- Scrum de equipo evolutivo: `../FUENTES-CURSO/02-Scrum-equipo-MiniJarvis.xlsx`.
- Entrega Moodle mínima: `../ENTREGAS-MOODLE/H5-entrega.md`.

## Refactorización y patrón [EQUIPO]

`Tool` define el contrato de las acciones. La semejanza con Command es encapsular cada acción ejecutable; no se añaden invocadores o fábricas sin necesidad. La revisión se acredita con historial y PR/revisión de código.

## Decisión y resultado

- Decisión: Se aplicó un Command simplificado mediante Tool sin introducir sobreingeniería.
- Resultado probado: Las herramientas comparten contrato y las pruebas de regresión pasan.

## Defensa de Laura [INDIVIDUAL]

Laura localiza su aportación, reproduce una prueba y explica una decisión sin apoyarse en una plantilla de defensa separada.
