# S208 — Píldoras: estructura y escritura de Java

> Material de consulta de la sesión S208. Usa los ejemplos para localizar cada elemento y anticipar errores antes de ejecutar.

## 1. Clase, archivo y `main`

En estos primeros programas:

- el archivo se llama `Main.java`;
- la clase pública se llama `Main`;
- el método `main` es el punto de entrada de la ejecución.

### Ejemplo 1 — Estructura mínima

```java
public class Main {
    public static void main(String[] args) {
        System.out.println("Hola");
    }
}
```

Java empieza a ejecutar las instrucciones que están dentro de `main`.

### Ejemplo 2 — Otro nombre de clase

Si el archivo se llama `Assistant.java`, la clase pública debe coincidir:

```java
public class Assistant {
    public static void main(String[] args) {
        System.out.println("Asistente preparado");
    }
}
```

### Ejemplo 3 — Diferencia entre `Main` y `main`

`Main` es el nombre de la clase. `main` es el nombre del método de entrada. Las mayúsculas importan: no son la misma palabra.

## 2. Java es preciso con la escritura

Java distingue mayúsculas y minúsculas y necesita delimitadores como `;`, `{}`, `()` y comillas.

### Ejemplo 1 — Mayúsculas

Correcto:

```java
String message = "Hola";
```

Incorrecto:

```java
string message = "Hola";
```

`String` empieza por mayúscula.

### Ejemplo 2 — Punto y coma

Correcto:

```java
System.out.println("Hola");
```

Incorrecto:

```java
System.out.println("Hola")
```

La instrucción necesita terminar con `;`.

### Ejemplo 3 — Comillas y paréntesis

```java
System.out.println("Hola");
```

Las comillas delimitan el texto; los paréntesis contienen el dato que recibe `println`.

### Ejemplo 4 — Llaves equilibradas

Cada llave de apertura debe tener su cierre. Una pareja delimita la clase y otra el método `main`.

## 3. Identificadores y palabras reservadas

Un identificador es un nombre que damos a elementos del programa.

### Ejemplo 1 — Nombres válidos y útiles

```java
String userName = "Laura";
int studyHours = 4;
String assistantName = "MiniJarvis";
```

### Ejemplo 2 — Nombres inválidos

```text
1name      empieza por número
my name    contiene un espacio
class      es una palabra reservada
public     es una palabra reservada
```

### Ejemplo 3 — Válido pero poco claro

```java
String x = "Laura";
```

Compila, pero `userName` comunica mejor la intención.

## 4. Comentarios: explicar intención

Los comentarios no se ejecutan. Sirven para aportar contexto que el código por sí solo no expresa con claridad.

### Ejemplo 1 — Comentario útil

```java
// Usamos un nombre ficticio para no publicar datos personales.
String userName = "Laura";
```

### Ejemplo 2 — Comentario redundante

```java
// Muestra Hola
System.out.println("Hola");
```

Repite literalmente lo que ya se ve y no añade información.

### Ejemplo 3 — Comentario de varias líneas

```java
/* Esta micropráctica prueba la estructura mínima.
   No forma parte todavía del Main final de H1. */
```

## Errores frecuentes

- Guardar `public class Main` en un archivo con otro nombre.
- Escribir `string`, `system` o `main` con mayúsculas incorrectas.
- Corregir el síntoma sin leer la primera marca del IDE.
- Usar comentarios para ocultar código que no se entiende.

## Comprueba que lo entiendes

1. Señala la clase y el punto de entrada en un ejemplo.
2. Corrige un error de mayúsculas, uno de `;` y uno de comillas.
3. Propón tres identificadores válidos y significativos.
4. Escribe un comentario que explique una decisión, no una instrucción evidente.
