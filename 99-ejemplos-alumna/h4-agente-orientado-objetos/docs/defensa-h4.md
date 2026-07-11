# Defensa — H4

## ¿Qué responsabilidad tiene cada clase?

```text
Main arranca, Agent gestiona el flujo y Memory guarda recuerdos.
```

## ¿Qué atributos son privados?

```text
En Agent son privados name, courseYear, memory, scanner, userName y running. En Memory es privado memories.
```

## ¿Qué relación aparece en el diagrama y en el código?

```text
Agent usa Memory. En el código aparece como private final Memory memory.
```
