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
