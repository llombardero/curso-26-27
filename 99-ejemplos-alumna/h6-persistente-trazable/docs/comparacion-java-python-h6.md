# Comparación Java ↔ Python — H6

## Java

```java
Files.write(filePath, memories, StandardOpenOption.CREATE, StandardOpenOption.TRUNCATE_EXISTING);
```

## Python

```python
with open("data/recuerdos.txt", "w", encoding="utf-8") as file:
    for memory in memories:
        file.write(memory + "
")
```

## Diferencias

```text
Java usa Path, Files y StandardOpenOption. Python usa open con un bloque with. En ambos casos hay que decidir ruta, formato y seguridad de los datos.
```
