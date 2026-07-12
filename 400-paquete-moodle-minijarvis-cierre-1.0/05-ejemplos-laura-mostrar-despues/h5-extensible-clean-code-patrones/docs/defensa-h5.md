# Defensa — H5

## ¿Qué problema tenía el código antes?

```text
Agent tenía demasiadas decisiones sobre comandos. Cada comando nuevo hacía crecer processCommand.
```

## ¿Qué refactorización hiciste?

```text
Creé una interfaz Tool y moví cada comando a una clase propia.
```

## ¿Por qué usaste o descartaste un patrón?

```text
Usé Command simplificado porque cada herramienta representa una acción ejecutable. No añadí Factory ni plugins porque sería demasiado para H5.
```

## ¿Qué evidencia hay?

```text
CourseTool demuestra que se puede añadir una herramienta nueva registrándola en registerDefaultTools().
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

