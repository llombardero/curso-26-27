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

<!-- AJUSTE-COBERTURA-CONCEPTOS-32 -->

## Respuesta de Laura — cobertura de conceptos de Programación

Relación con `32-lista-conceptos-programacion-por-tema.md`:

```text
H3 trabaja principalmente: Tema 4.
Foco de aprendizaje: memoria temporal con estructuras de datos.
```

Conceptos que Laura debe saber defender en este hito:

- colección
- genéricos
- List
- ArrayList
- índice
- recorrido
- for mejorado
- mutabilidad
- inmutabilidad
- clases envoltorio
- array
- tabla como ampliación
- Set para evitar repetidos
- Map para preferencias por clave

Respuesta modelo de Laura:

> En H3 defiendo por qué usé una lista para guardar recuerdos y qué cambiaría si necesitara evitar repetidos o buscar por clave.

Evidencia que Laura debe señalar:

- una parte concreta del código o documento donde aparezca el concepto;
- una prueba, ejecución, captura o explicación que demuestre que no lo ha copiado sin entender;
- una mejora razonable que podría hacer si tuviera más tiempo.

