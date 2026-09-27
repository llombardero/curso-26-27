# S211 — Píldoras: constantes, literales y operaciones

> Material de consulta de la sesión S211. Predice cada resultado antes de ejecutar los ejemplos.

## 1. Constantes con `final`

Una constante representa un dato que no debe cambiar durante la ejecución. En Java usamos `final` y, por convención, un nombre en mayúsculas con guiones bajos.

### Ejemplo 1 — Nombre del asistente

```java
final String ASSISTANT_NAME = "MiniJarvis";
System.out.println(ASSISTANT_NAME);
```

### Ejemplo 2 — Año de inicio

```java
final int START_YEAR = 2026;
System.out.println("Inicio: " + START_YEAR);
```

### Ejemplo 3 — Reasignación no permitida

```java
final int MAX_ATTEMPTS = 3;
MAX_ATTEMPTS = 4; // error: una constante no se reasigna
```

No todo dato que hoy coincide varias veces debe ser constante: lo es cuando su significado indica que no debe cambiar durante esa ejecución.

## 2. Literal = valor escrito directamente

### Ejemplo 1 — Literales de varios tipos

```java
int hours = 5;                 // 5 es literal entero
double score = 7.5;            // 7.5 es literal decimal
char initial = 'L';            // 'L' es literal de carácter
String message = "Hola";       // "Hola" es literal de texto
boolean ready = true;          // true es literal lógico
```

### Ejemplo 2 — Comillas simples y dobles

```java
char initial = 'M';
String name = "MiniJarvis";
```

### Ejemplo 3 — Literal reutilizado mediante constante

```java
final String ASSISTANT_NAME = "MiniJarvis";
System.out.println("Hola, soy " + ASSISTANT_NAME);
System.out.println(ASSISTANT_NAME + " está preparado");
```

El texto estable se define una sola vez.

## 3. Operadores aritméticos

`+`, `-`, `*`, `/` y `%` producen un resultado. Debemos mostrarlo, guardarlo o usarlo si queremos conservarlo.

### Ejemplo 1 — Operaciones básicas

```java
int total = 6 + 2;       // 8
int pending = 6 - 2;     // 4
int minutes = 3 * 60;    // 180
```

### Ejemplo 2 — División entera y real

```java
int a = 5 / 2;        // 2
double b = 5 / 2.0;   // 2.5
```

Si ambos operandos son enteros, la parte decimal no aparece.

### Ejemplo 3 — Precedencia

```java
int resultA = 8 * 4 + 2;      // 34
int resultB = 8 * (4 + 2);    // 48
```

Los paréntesis permiten expresar con claridad qué se calcula primero.

## 4. El resto `%`

`%` no calcula un porcentaje: devuelve el resto de una división entera.

### Ejemplo 1 — Reparto

```java
int candies = 10;
int people = 4;
int remaining = candies % people; // 2
```

### Ejemplo 2 — Saber si un número es par

```java
int number = 8;
int remainder = number % 2; // 0
```

Si el resto al dividir entre 2 es `0`, el número es par.

### Ejemplo 3 — Ciclos sencillos

```java
int minute = 67;
int minutesAfterHour = minute % 60; // 7
```

## 5. Actualizar sin reescribir todo

### Ejemplo 1 — Operadores compuestos

```java
int tasks = 3;
tasks += 2; // equivale a tasks = tasks + 2; ahora vale 5
tasks -= 1; // ahora vale 4
```

### Ejemplo 2 — Incremento y decremento

```java
int attempts = 1;
attempts++; // 2
attempts--; // 1
```

### Ejemplo 3 — Actualizar una cantidad mayor

```java
int minutes = 30;
minutes *= 2; // equivale a minutes = minutes * 2; ahora vale 60
```

## Errores frecuentes

- Intentar cambiar una variable declarada con `final`.
- Confundir `%` con porcentaje.
- Esperar `2.5` en una división `int / int`.
- Calcular un resultado sin guardarlo, mostrarlo ni usarlo.
- Leer `tasks++` como si declarase otra variable.

## Comprueba que lo entiendes

1. Clasifica cinco literales por tipo.
2. Predice `7 / 2`, `7 / 2.0` y `7 % 2`.
3. Explica la diferencia entre variable y constante.
4. Parte de `int tasks = 3;` y predice tres actualizaciones distintas.
