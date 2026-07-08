# Comparación Java ↔ Python — H3

Alumno/a: Laura García Martín  
Fecha: ejemplo docente

---

## Colecciones comparadas

| Necesidad | Java | Python |
|---|---|---|
| Lista ordenada | `ArrayList<String>` | `list` |
| Añadir elemento | `memories.add(memory)` | `memories.append(memory)` |
| Tamaño | `memories.size()` | `len(memories)` |
| Acceso por índice | `memories.get(i)` | `memories[i]` |

---

## Fragmento Java

```java
ArrayList<String> memories = new ArrayList<>();
memories.add(memory);

for (int i = 0; i < memories.size(); i++) {
    System.out.println((i + 1) + ". " + memories.get(i));
}
```

---

## Fragmento Python

```python
memories = []
memories.append(memory)

for index, memory in enumerate(memories, start=1):
    print(f"{index}. {memory}")
```

---

## Qué he entendido

```text
ArrayList y list sirven para guardar varios elementos en orden. Java necesita indicar el tipo String y usar métodos como add(), size() y get(). Python usa una sintaxis más corta.
```
