# Registro de patrón — H5

## Problema

```text
El método processCommand crecía cada vez que añadíamos un comando nuevo.
```

## Patrón usado o descartado

```text
Uso una versión sencilla del patrón Command: cada herramienta tiene un comando y un método execute.
```

## Alternativa simple

```text
Podíamos mantener if/else en Agent. Era más simple al principio, pero cada comando nuevo hacía crecer Agent.
```

## Decisión

```text
Usar Tool como Command simplificado tiene sentido porque queremos añadir herramientas internas con bajo impacto y cada herramienta es fácil de defender.
```

<!-- AJUSTE-COBERTURA-CONCEPTOS-32 -->

## Respuesta de Laura — cobertura de conceptos de Programación

Relación con `32-lista-conceptos-programacion-por-tema.md`:

```text
H5 trabaja principalmente: Temas 5 y 6.
Foco de aprendizaje: interfaces, extensibilidad, pruebas y primer patrón.
```

Conceptos que Laura debe saber defender en este hito:

- test unitario
- aserto
- TDD
- interfaz
- implementación
- método default como ampliación
- excepciones
- recursividad como comparación
- métodos estáticos
- records como ampliación
- enum
- polimorfismo por interfaz
- Command simplificado
- clean code
- refactorización segura

Respuesta modelo de Laura:

> En H5 defiendo que el patrón Command simplificado aparece porque resuelve un problema real: demasiados comandos mezclados dentro de Agent.

Evidencia que Laura debe señalar:

- una parte concreta del código o documento donde aparezca el concepto;
- una prueba, ejecución, captura o explicación que demuestre que no lo ha copiado sin entender;
- una mejora razonable que podría hacer si tuviera más tiempo.

