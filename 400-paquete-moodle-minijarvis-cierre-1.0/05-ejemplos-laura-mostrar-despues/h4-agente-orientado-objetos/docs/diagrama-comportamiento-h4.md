# Diagrama de comportamiento — H4

```mermaid
sequenceDiagram
    actor Usuario
    Usuario->>Main: ejecuta programa
    Main->>Agent: new Agent("MiniJarvis", 2026)
    Main->>Agent: start()
    Agent->>Usuario: pide nombre y comando
    Usuario->>Agent: recuerda
    Agent->>Usuario: pide texto
    Usuario->>Agent: Traer pendrive
    Agent->>Memory: add("Traer pendrive")
    Memory-->>Agent: true
    Agent->>Usuario: confirma guardado
```

## Flujo explicado

```text
El usuario no trabaja directamente con Memory. Agent recibe comandos y delega en Memory cuando necesita guardar o mostrar recuerdos.
```
