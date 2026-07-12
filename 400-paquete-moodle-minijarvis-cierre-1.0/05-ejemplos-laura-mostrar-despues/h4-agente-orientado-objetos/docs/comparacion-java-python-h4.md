# Comparación Java ↔ Python — H4

## Constructor

Java:
```java
public Memory() {
    this.memories = new ArrayList<>();
}
```

Python:
```python
class Memory:
    def __init__(self):
        self.memories = []
```

## Diferencias

```text
Java usa el constructor con el mismo nombre de la clase. Python usa __init__. Java declara tipos y visibilidad; Python es más breve y flexible.
```

<!-- AJUSTE-COBERTURA-CONCEPTOS-32 -->

## Respuesta de Laura — cobertura de conceptos de Programación

Relación con `32-lista-conceptos-programacion-por-tema.md`:

```text
H4 trabaja principalmente: Temas 2 y 5.
Foco de aprendizaje: orientación a objetos y separación de responsabilidades.
```

Conceptos que Laura debe saber defender en este hito:

- clase
- objeto
- atributo
- método
- constructor
- referencia
- estado
- comportamiento
- responsabilidad
- private/public
- this
- diagrama de clases
- diagrama de comportamiento
- Javadoc como ampliación
- excepción básica

Respuesta modelo de Laura:

> En H4 explico por qué Main era demasiado grande y cómo Agent y Memory reparten responsabilidades con atributos privados y métodos públicos.

Evidencia que Laura debe señalar:

- una parte concreta del código o documento donde aparezca el concepto;
- una prueba, ejecución, captura o explicación que demuestre que no lo ha copiado sin entender;
- una mejora razonable que podría hacer si tuviera más tiempo.

