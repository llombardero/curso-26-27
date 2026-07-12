# Incidencia — H6

## Problema

```text
Si la carpeta data no existía, guardar recuerdos podía fallar.
```

## Causa

```text
El programa intentaba escribir en un fichero dentro de una carpeta que quizá no existía.
```

## Solución

```text
Añadí Files.createDirectories(filePath.getParent()) antes de crear, leer o escribir el fichero.
```
