# Relación diagrama-código — H4

| Elemento del diagrama | Dónde aparece en código | Explicación |
|---|---|---|
| Main | `src/Main.java` | Crea el agente y llama a `start()`. |
| Agent | `src/Agent.java` | Contiene el flujo del programa y procesa comandos. |
| Memory | `src/Memory.java` | Encapsula la lista de recuerdos. |
| Main --> Agent | `Agent agent = new Agent(...)` | Main depende de Agent para iniciar MiniJarvis. |
| Agent --> Memory | `private final Memory memory` | Agent usa Memory para guardar y consultar recuerdos. |
