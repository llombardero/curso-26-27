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

