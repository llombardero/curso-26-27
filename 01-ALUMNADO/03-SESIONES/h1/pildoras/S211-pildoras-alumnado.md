# S211 — Píldoras: constantes, literales y operaciones

> Material de consulta de la sesión S211. Predice cada resultado antes de ejecutar los ejemplos.

## 1. Constantes con `final`

Una constante representa un dato que no debe cambiar durante la ejecución. En Java usamos `final` y, por convención, un nombre en mayúsculas con guiones bajos.

### Ejemplo 1 — Nombre del asistente

```java
final String NOMBRE_ASISTENTE = "MiniJarvis";
System.out.println(NOMBRE_ASISTENTE);
```

### Ejemplo 2 — Año de inicio

```java
final int ANIO_INICIO = 2026;
System.out.println("Inicio: " + ANIO_INICIO);
```

### Ejemplo 3 — Reasignación no permitida

```java
final int MAX_INTENTOS = 3;
MAX_INTENTOS = 4; // error: una constante no se reasigna
```

No todo dato que hoy coincide varias veces debe ser constante: lo es cuando su significado indica que no debe cambiar durante esa ejecución.

## 2. Literal = valor escrito directamente

### Ejemplo 1 — Literales de varios tipos

```java
int horas = 5;                 // 5 es literal entero
double nota = 7.5;            // 7.5 es literal decimal
char inicial = 'L';            // 'L' es literal de carácter
String mensaje = "Hola";       // "Hola" es literal de texto
boolean preparado = true;          // true es literal lógico
```

### Ejemplo 2 — Comillas simples y dobles

```java
char inicial = 'M';
String nombre = "MiniJarvis";
```

### Ejemplo 3 — Literal reutilizado mediante constante

```java
final String NOMBRE_ASISTENTE = "MiniJarvis";
System.out.println("Hola, soy " + NOMBRE_ASISTENTE);
System.out.println(NOMBRE_ASISTENTE + " está preparado");
```

El texto estable se define una sola vez.

## 3. Expresiones y operadores aritméticos

Una expresión combina literales, variables y operadores para producir un resultado. Ese resultado también tiene un tipo.

```java
int minutos = 3 * 60;                    // resultado int
boolean suficiente = minutos >= 120;     // resultado boolean
String resumen = "Minutos: " + minutos;  // resultado String
```

Una expresión calculada pero no guardada, mostrada ni utilizada no produce un efecto observable.

`+`, `-`, `*`, `/` y `%` producen un resultado. Debemos mostrarlo, guardarlo o usarlo si queremos conservarlo.

### Ejemplo 1 — Operaciones básicas

```java
int total = 6 + 2;       // 8
int pendiente = 6 - 2;     // 4
int minutos = 3 * 60;    // 180
```

### Ejemplo 2 — División entera y real

```java
int a = 5 / 2;        // 2
double b = 5 / 2.0;   // 2.5
```

Si ambos operandos son enteros, la parte decimal no aparece.

En `5 / 2.0`, uno de los operandos es decimal; por eso el resultado es `double`. En `5 / 2`, ambos son enteros y el resultado es `int`.

### Ejemplo 3 — Precedencia

```java
int resultadoA = 8 * 4 + 2;      // 34
int resultadoB = 8 * (4 + 2);    // 48
```

Los paréntesis permiten expresar con claridad qué se calcula primero.

## 4. El resto `%`

`%` no calcula un porcentaje: devuelve el resto de una división entera.

### Ejemplo 1 — Reparto

```java
int caramelos = 10;
int personas = 4;
int restantes = caramelos % personas; // 2
```

### Ejemplo 2 — Saber si un número es par

```java
int numero = 8;
int resto = numero % 2; // 0
```

Si el resto al dividir entre 2 es `0`, el número es par.

### Ejemplo 3 — Ciclos sencillos

```java
int minuto = 67;
int minutosTrasHora = minuto % 60; // 7
```

## 5. Actualizar sin reescribir todo

### Ejemplo 1 — Operadores compuestos

```java
int tareas = 3;
tareas += 2; // equivale a tareas = tareas + 2; ahora vale 5
tareas -= 1; // ahora vale 4
```

### Ejemplo 2 — Incremento y decremento

```java
int intentos = 1;
intentos++; // 2
intentos--; // 1
```

### Ejemplo 3 — Actualizar una cantidad mayor

```java
int minutos = 30;
minutos *= 2; // equivale a minutos = minutos * 2; ahora vale 60
```

## Errores frecuentes

- Intentar cambiar una variable declarada con `final`.
- Confundir `%` con porcentaje.
- Esperar `2.5` en una división `int / int`.
- Calcular un resultado sin guardarlo, mostrarlo ni usarlo.
- Leer `tareas++` como si declarase otra variable.

## Comprueba que lo entiendes

1. Clasifica cinco literales por tipo.
2. Predice `7 / 2`, `7 / 2.0` y `7 % 2`.
3. Explica la diferencia entre variable y constante.
4. Parte de `int tareas = 3;` y predice tres actualizaciones distintas.
