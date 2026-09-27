# S210 — Píldoras: variables, tipos y nombres

> Material de consulta de la sesión S210. Una variable permite guardar un dato con un tipo y un nombre para utilizarlo después.

## 1. Variable = dato + nombre + memoria

Una variable es una zona de memoria identificada por un nombre. Su valor puede cambiar durante la ejecución si su tipo lo permite.

### Ejemplo 1 — Entero

```java
int studyHours = 4;
System.out.println(studyHours);
```

`studyHours` es la variable; `4` es el valor guardado en este momento.

### Ejemplo 2 — Texto

```java
String userName = "Laura";
System.out.println("Hola, " + userName);
```

La variable evita repetir el nombre directamente en todos los mensajes.

### Ejemplo 3 — El valor cambia

```java
int completedTasks = 1;
completedTasks = 2;
System.out.println(completedTasks);
```

La salida es `2`. La variable es la misma; ha cambiado su valor.

## 2. Mapa de tipos de Tema 1

El tipo indica qué clase de dato puede guardar una variable.

### Ejemplo 1 — Tipos de uso inmediato

```java
int studyHours = 4;          // entero
double averageScore = 7.5;   // decimal
boolean goalReached = true;  // verdadero o falso
char initial = 'L';          // un carácter
String userName = "Laura";   // texto
```

### Ejemplo 2 — `char` y `String`

```java
char initial = 'L';
String name = "Laura";
```

`char` usa comillas simples y guarda un carácter. `String` usa comillas dobles y puede guardar una cadena de caracteres.

### Ejemplo 3 — Entero y decimal

```java
int sessions = 3;
double duration = 1.5;
```

No elijas el tipo por el nombre de la variable, sino por los valores que necesitas representar.

## 3. Nombres válidos y significativos

Un buen nombre es válido para Java y explica qué dato guarda.

### Ejemplo 1 — Mejorar nombres vagos

```java
String x = "Laura";
int n = 4;
```

Mejor:

```java
String userName = "Laura";
int studyHours = 4;
```

### Ejemplo 2 — Nombres inválidos

```text
1name      empieza por número
my name    contiene un espacio
class      es palabra reservada
```

### Ejemplo 3 — Convención `lowerCamelCase`

```java
String assistantName = "MiniJarvis";
int completedTasks = 2;
double averageScore = 8.25;
```

La primera palabra comienza en minúscula y las siguientes, en mayúscula.

## 4. Declarar, inicializar y asignar

- **Declarar:** indicar tipo y nombre.
- **Inicializar:** dar el primer valor.
- **Asignar:** guardar un nuevo valor posteriormente.

### Ejemplo 1 — Declarar y luego inicializar

```java
int studyHours;  // declaración
studyHours = 4;  // primera asignación: inicialización
```

### Ejemplo 2 — Declarar e inicializar a la vez

```java
int studyHours = 4;
```

### Ejemplo 3 — Cambiar el valor

```java
int studyHours = 4;
studyHours = 5;
```

No se repite `int` en la segunda línea porque la variable ya estaba declarada.

### Ejemplo 4 — `=` no significa igualdad matemática

```java
int tasks = 2;
tasks = tasks + 1;
```

Java calcula primero `tasks + 1` y guarda el resultado, `3`, en `tasks`.

## Errores frecuentes

- Confundir la variable con su valor actual.
- Usar `String` para cualquier dato sin pensar qué operaciones necesitará.
- Escribir otra vez el tipo al cambiar un valor.
- Usar nombres válidos pero poco explicativos.

## Comprueba que lo entiendes

1. Identifica tipo, nombre y valor en tres ejemplos.
2. Elige tipos para un nombre, una edad, una nota, una inicial y una respuesta sí/no.
3. Renombra tres variables vagas.
4. Señala una declaración, una inicialización y una asignación posterior.
