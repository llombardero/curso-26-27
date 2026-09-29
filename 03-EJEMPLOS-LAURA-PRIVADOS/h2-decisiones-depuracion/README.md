# H2 — Decisiones y depuración

> Ejemplo privado de Laura. Mostrar solo después del intento propio del alumnado.

## Objetivo

Añadir menú, repetición, decisiones y salida controlada.

## Arquitectura de evidencias

Versión estable: `h2-entrega`. El repositorio y su README son la evidencia técnica canónica.

- Diario individual evolutivo: `../FUENTES-CURSO/01-Diario-individual-MiniJarvis.xlsx`.
- Scrum de equipo evolutivo: `../FUENTES-CURSO/02-Scrum-equipo-MiniJarvis.xlsx`.
- Entrega Moodle mínima: `../ENTREGAS-MOODLE/H2-entrega.md`.

## Pruebas y depuración [EQUIPO]

Casos: ayuda, saludo, estado, comando desconocido y salir. Un breakpoint después de leer el comando permitió observar `command`, `running` y `userName`; se corrigió la comparación con `equalsIgnoreCase`.

## Decisión y resultado

- Decisión: Se corrigió la comparación de textos y se documentó una depuración con breakpoint.
- Resultado probado: El menú responde a casos previstos y termina de forma controlada.

## Defensa de Laura [INDIVIDUAL]

Laura localiza su aportación, reproduce una prueba y explica una decisión sin apoyarse en una plantilla de defensa separada.
