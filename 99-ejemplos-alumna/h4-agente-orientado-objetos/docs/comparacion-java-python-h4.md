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
