# Comparación Java ↔ Python — H5

## Java: interfaz/composición

```java
public interface Tool {
    String getCommand();
    String getDescription();
    void execute(Agent agent);
}
```

## Python: duck typing

```python
class CourseTool:
    def get_command(self):
        return "curso"

    def execute(self, agent):
        print(f"Proyecto iniciado en {agent.course_year}")
```

## Qué he entendido

```text
En Java la interfaz obliga a que todas las herramientas tengan los mismos métodos. En Python no hace falta declarar una interfaz obligatoria: si el objeto tiene los métodos esperados, puede funcionar.
```
