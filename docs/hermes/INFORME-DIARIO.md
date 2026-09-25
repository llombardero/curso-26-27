# Procedimiento de informe diario

Usa este documento al finalizar una jornada de trabajo.

## Ubicación

Guarda o actualiza:

`docs/seguimiento-hermes/YYYY-MM-DD.md`

Si ya existe el informe de la fecha actual, actualízalo en lugar de crear otro.

## Contenido

### Estado inicial
- rama de trabajo;
- estado Git al comenzar;
- commits pendientes;
- archivos sin seguimiento relevantes;
- objetivo principal.

### Trabajo realizado
Resume:
- análisis;
- archivos modificados, creados, eliminados o movidos;
- scripts modificados;
- artefactos regenerados;
- pruebas ejecutadas;
- documentación revisada.

Agrupa cambios triviales.

### Decisiones tomadas
Para cada decisión relevante indica:
- problema;
- decisión;
- motivo;
- consecuencias.

Presta atención a:
- estructura de hitos;
- HEXA;
- Scrum;
- evidencias;
- evaluación;
- documentación;
- arquitectura técnica;
- Git/GitHub.

### Auditoría pedagógica
Si se revisaron materiales del alumnado, registra:
- evidencias analizadas;
- redundancias;
- simplificaciones propuestas;
- decisiones aprobadas;
- cuestiones pendientes.

### Estado Git final
Incluye:
- rama;
- `git status`;
- commits creados;
- commits pendientes;
- estado respecto al remoto;
- último commit relevante;
- archivos sin seguimiento importantes.

### Verificaciones
Indica qué se ejecutó y el resultado:
- tests;
- validadores;
- `git diff --check`;
- generadores;
- enlaces;
- artefactos;
- otras comprobaciones.

No afirmes que algo está correcto si no fue comprobado.

### Pendiente
Distingue:
- siguiente acción;
- decisiones del usuario;
- problemas conocidos;
- verificaciones pendientes;
- cambios sin commit;
- cambios pendientes de push.

### Continuidad
Termina siempre con:
- dónde nos hemos quedado;
- rama activa;
- estado del repositorio;
- próxima tarea;
- precauciones importantes.

## Reglas

El informe debe:
- ser conciso;
- basarse en hechos comprobados;
- no inventar trabajo;
- no ocultar fallos;
- distinguir terminado de pendiente;
- evitar repetición;
- permitir retomar el proyecto días después.

Después de generar el informe, actualiza también `docs/hermes/ESTADO-ACTUAL.md` con el estado vigente.

No hagas un commit específico únicamente para el informe si aún existen cambios de trabajo que deban integrarse en un commit coherente.
