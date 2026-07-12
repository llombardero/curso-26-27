# Informe de refactorización — H5

## Problema antes

```text
En H4 Agent tenía un método processCommand con muchas ramas if/else. Si añadíamos un comando nuevo, había que modificar Agent.
```

## Cambio realizado

```text
Creé la interfaz Tool y una clase para cada herramienta: HelpTool, GreetTool, RememberTool, MemoryTool, StatusTool, CourseTool y ExitTool.
```

## Después

```text
Agent mantiene una lista de herramientas. Para añadir una herramienta nueva, creo una clase nueva que implementa Tool y la registro en registerDefaultTools().
```

## Verificación

```text
Compilé el proyecto y probé ayuda, curso, recuerda, estado, memoria y salir.
```
