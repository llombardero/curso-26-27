# S213 — Píldoras: comparaciones, lógica y decisiones

> Material de consulta de la sesión S213. Predice siempre `true`, `false` o la salida antes de ejecutar. H1 introduce decisiones pequeñas; los menús y decisiones encadenadas se trabajarán en H2.

## 1. Comparar produce un `boolean`

Una comparación no devuelve uno de los valores comparados: devuelve `true` o `false`.

### Ejemplo 1 — Igual y distinto

```java
int hours = 4;
System.out.println(hours == 4); // true
System.out.println(hours != 4); // false
```

`=` asigna un valor; `==` compara valores.

### Ejemplo 2 — Orden

```java
int hours = 5;
System.out.println(hours > 3);  // true
System.out.println(hours <= 4); // false
```

### Ejemplo 3 — Guardar el resultado

```java
int hours = 5;
boolean enough = hours >= 4;
System.out.println(enough); // true
```

### Ejemplo 4 — Texto

En Tema 1 no usamos `==` para comparar el contenido de dos `String`. Basta con recordar que el texto necesita otra forma de comparación, que se retomará cuando sea necesaria.

## 2. AND, OR, NOT

- `&&` — AND: las dos condiciones deben ser verdaderas.
- `||` — OR: basta con que una sea verdadera.
- `!` — NOT: invierte `true` y `false`.

### Ejemplo 1 — AND

```java
boolean hasName = true;
boolean hasGoal = true;
boolean canStart = hasName && hasGoal; // true
```

Si `hasGoal` fuese `false`, `canStart` sería `false`.

### Ejemplo 2 — OR

```java
boolean hasQuestion = false;
boolean hasError = true;
boolean needsHelp = hasQuestion || hasError; // true
```

### Ejemplo 3 — NOT

```java
boolean finished = false;
boolean pending = !finished; // true
```

### Ejemplo 4 — Expresión combinada y legible

```java
boolean canStart = hasName && hasGoal;
boolean needsHelp = !canStart || hasError;
```

Primero explica cada parte con palabras: «Necesita ayuda si no puede empezar o si tiene un error».

## 3. Del `boolean` a una decisión

`if` necesita una condición que produzca `true` o `false`.

### Ejemplo 1 — Variable booleana

```java
boolean ready = true;
if (ready) {
    System.out.println("Empezamos");
}
```

### Ejemplo 2 — Comparación directa

```java
int hours = 5;
if (hours >= 4) {
    System.out.println("Objetivo alcanzado");
}
```

### Ejemplo 3 — Lo que no sirve como condición

```java
int hours = 5;
// if (hours) { ... }  // incorrecto: hours es int, no boolean
```

## 4. `if / else`: dos caminos

Si la condición es `true`, se ejecuta el bloque `if`; si es `false`, el bloque `else`.

### Ejemplo 1 — Horas de estudio

```java
if (hours >= 4) {
    System.out.println("Objetivo alcanzado");
} else {
    System.out.println("Objetivo pendiente");
}
```

Prueba `hours = 5` y `hours = 2`.

### Ejemplo 2 — Preparación

```java
if (ready) {
    System.out.println("MiniJarvis está preparado");
} else {
    System.out.println("Falta completar la preparación");
}
```

### Ejemplo 3 — Dos casos necesarios

Un único caso favorable no demuestra el `else`. Guarda la entrada o valor usado y la salida esperada de cada rama.

## 5. Anidamiento: reconocer la idea

Un `if` puede contener otra decisión. En H1 solo necesitas leer la estructura, no construir decisiones complejas.

### Ejemplo 1 — Primera condición y condición interior

```java
if (hasName) {
    if (hasGoal) {
        System.out.println("Datos completos");
    }
}
```

Primero se comprueba `hasName`. Solo si es `true` se comprueba `hasGoal`.

### Ejemplo 2 — Rama exterior

```java
if (ready) {
    if (hasError) {
        System.out.println("Revisa el error");
    } else {
        System.out.println("Puedes continuar");
    }
} else {
    System.out.println("Completa la preparación");
}
```

### Ejemplo 3 — Evitar sobrecarga

Si necesitas dibujar muchas ramas para explicar una condición de H1, probablemente estás adelantando el trabajo de H2. Reduce la práctica a una pregunta sí/no defendible.

## 6. Asignación condicional `?:`

El operador ternario elige un valor a partir de una condición sencilla.

```text
condición ? valor_si_true : valor_si_false
```

### Ejemplo 1 — Mensaje

```java
String message = hours >= 4
        ? "Objetivo alcanzado"
        : "Objetivo pendiente";
```

### Ejemplo 2 — Estado

```java
String status = ready ? "Preparado" : "Pendiente";
```

### Ejemplo 3 — Valor numérico

```java
int points = goalReached ? 1 : 0;
```

### Ejemplo 4 — Cuándo preferir `if / else`

Si cada camino necesita varias instrucciones, `if / else` suele ser más claro. El ternario no sustituye a cualquier decisión.

## Errores frecuentes

- Usar `=` cuando se quería comparar con `==`.
- Escribir `if (hours)` cuando `hours` es `int`.
- Memorizar `&&`, `||` y `!` sin traducir la expresión a palabras.
- Probar solo la rama que produce `true`.
- Comparar el contenido de `String` con `==`.
- Encadenar decisiones complejas que pertenecen a H2.

## Comprueba que lo entiendes

1. Predice cuatro comparaciones con resultados `true` y `false`.
2. Traduce a palabras una expresión con `&&`, otra con `||` y otra con `!`.
3. Prueba las dos ramas de un `if / else` y anota los valores usados.
4. Señala condición, valor verdadero y valor falso en un ternario.
