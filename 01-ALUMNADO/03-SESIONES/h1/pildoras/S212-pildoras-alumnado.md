# S212 — Píldoras: `Scanner` y conversiones

> Material de consulta de la sesión S212. En todos los ejemplos usa datos ficticios y una sola instancia de `Scanner`.

## 1. `Scanner`: pedir → leer → guardar

`Scanner` permite leer lo que una persona escribe en la consola. `nextLine()` devuelve un `String`.

### Ejemplo 1 — Leer un nombre

```java
import java.util.Scanner;

Scanner teclado = new Scanner(System.in);
System.out.print("Escribe un nombre ficticio: ");
String nombreUsuario = teclado.nextLine();
System.out.println("Hola, " + nombreUsuario + ".");
teclado.close();
```

### Ejemplo 2 — Leer un texto diferente

```java
Scanner teclado = new Scanner(System.in);
System.out.print("Escribe un objetivo: ");
String objetivo = teclado.nextLine();
System.out.println("Objetivo registrado: " + objetivo);
teclado.close();
```

### Ejemplo 3 — Reutilizar la instancia

```java
Scanner teclado = new Scanner(System.in);
String nombreUsuario = teclado.nextLine();
String objetivo = teclado.nextLine();
teclado.close();
```

No hace falta crear un `Scanner` nuevo para cada línea.

## 2. Parsear texto a un tipo básico

Si `nextLine()` devuelve texto, necesitamos convertirlo para hacer operaciones numéricas.

### Ejemplo 1 — Texto a entero

```java
String texto = "5";
int horas = Integer.parseInt(texto);
int minutos = horas * 60;
```

### Ejemplo 2 — Texto a decimal

```java
String texto = "7.5";
double nota = Double.parseDouble(texto);
```

### Ejemplo 3 — Texto a booleano

```java
String texto = "true";
boolean preparado = Boolean.parseBoolean(texto);
```

### Ejemplo 4 — Entrada no convertible

```java
String texto = "cinco";
int horas = Integer.parseInt(texto);
```

Compila, pero falla al ejecutar porque `"cinco"` no representa un entero. En H1 observamos y explicamos el error; todavía no necesitamos resolverlo con `try-catch`.

## 3. Conversión implícita

Java puede convertir automáticamente algunos números a un tipo más amplio.

### Ejemplo 1 — `int` a `double`

```java
int entero = 7;
double valorAmpliado = entero; // 7.0
```

### Ejemplo 2 — `char` a `int`

```java
char letra = 'A';
int codigo = letra;
System.out.println(codigo); // 65
```

Basta con reconocer que Java puede ampliar el valor; no necesitas memorizar todos los códigos de caracteres.

### Ejemplo 3 — No es parseo

```java
int horas = 5;
double horasDecimales = horas;
```

Aquí convertimos entre tipos numéricos. No partimos de un `String`, por lo que no usamos `parseInt`.

## 4. Casting: forzar puede perder información

Un casting indica explícitamente el tipo de destino. Cuando pasamos de un decimal a un entero se descarta la parte decimal; no se redondea.

### Ejemplo 1 — Precio

```java
double precio = 12.75;
int precioEntero = (int) precio; // 12
```

### Ejemplo 2 — Nota

```java
double nota = 8.99;
int notaEntera = (int) nota; // 8
```

### Ejemplo 3 — Valor negativo

```java
double temperatura = -3.8;
int temperaturaEntera = (int) temperatura; // -3
```

Se elimina la parte decimal acercándose a cero; no se obtiene `-4`.

### Ejemplo 4 — Comparar antes y después

```java
double duracion = 2.75;
int horasCompletas = (int) duracion;
System.out.println(duracion);      // 2.75
System.out.println(horasCompletas); // 2
```

## Errores frecuentes

- Pensar que `nextLine()` devuelve un número porque el texto contiene cifras.
- Crear varios objetos `Scanner` sobre `System.in` sin necesidad.
- Confundir parseo de texto con conversión entre números.
- Creer que el casting redondea.
- No guardar el resultado de `parseInt` o del casting.

## Comprueba que lo entiendes

1. Explica qué devuelve `nextLine()`.
2. Convierte `"12"` a entero y calcula sus minutos.
3. Distingue un ejemplo de parseo, uno de conversión implícita y uno de casting.
4. Predice qué ocurre con `Integer.parseInt("hola")` y cuándo ocurre.
