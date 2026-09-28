# S208 — Estructura mínima de un programa Java

## Objetivo

Reconocer la clase, el método `main`, las instrucciones y los delimitadores básicos de Java; identificar errores sencillos y utilizar nombres y comentarios que mejoren la lectura.

## 1. Clase, archivo y punto de entrada

```java
public class Main {
    public static void main(String[] argumentos) {
        System.out.println("Hola desde MiniJarvis");
    }
}
```

- `Main.java` es el nombre del archivo.
- `Main` es la clase pública; debe coincidir con el nombre del archivo.
- `main` es el método donde comienza la ejecución.
- `String[] argumentos` permite recibir argumentos de línea de comandos, aunque H1 no los utiliza.
- `System.out.println(...)` es una instrucción que muestra texto.

`Main` y `main` no son lo mismo: Java distingue mayúsculas y minúsculas.

## 2. Orden de ejecución

Las instrucciones de `main` se ejecutan de arriba abajo:

```java
System.out.println("Primero");
System.out.println("Después");
System.out.println("Al final");
```

Predice la salida y cambia el orden de dos instrucciones para comprobar el efecto.

## 3. Delimitadores que debes revisar

- `{ }` delimitan bloques.
- `( )` delimitan parámetros y expresiones.
- `" "` delimitan textos.
- `;` termina la mayoría de instrucciones.

Compara:

```java
System.out.println("Correcto");
```

```java
System.out.println("Falta el punto y coma")
```

```java
System.out.println("Falta cerrar el paréntesis";
```

```java
System.out.println("Falta cerrar la comilla);
```

Los tres últimos fragmentos son incorrectos. Lee el primer error del compilador y señala el delimitador que falta.

## 4. Identificadores

Un identificador es el nombre de una clase, variable o método. Puede contener letras, números, `_` y `$`, pero no puede empezar por un número ni ser una palabra reservada.

Ejemplos válidos y claros:

```java
String nombreUsuario = "Laura";
int horasEstudio = 4;
String nombreAsistente = "MiniJarvis";
```

Ejemplos inválidos:

```text
1nombre         empieza por número
horas estudio   contiene un espacio
class           es una palabra reservada
public          es una palabra reservada
```

Ejemplo válido pero poco claro:

```java
String x = "Laura";
```

`nombreUsuario` comunica mejor la intención que `x`.

## 5. Comentarios útiles

Los comentarios no se ejecutan. Deben explicar una intención o decisión que el código no muestra por sí solo.

```java
// Usamos un nombre ficticio para no publicar datos personales.
String nombreUsuario = "Laura";
```

Comentario redundante:

```java
// Muestra Hola.
System.out.println("Hola");
```

No comentes cada línea. Prefiere código legible y comentarios breves cuando aporten contexto.

## 6. Actividad

1. Escribe el programa mínimo correcto.
2. Predice y comprueba su salida.
3. Provoca por separado un error de comillas, uno de paréntesis y uno de punto y coma.
4. Para cada error, registra:
   - cambio realizado;
   - mensaje esencial del compilador;
   - causa;
   - corrección.
5. Renombra dos identificadores vagos.
6. Añade un comentario útil y elimina uno redundante.

## Evidencia verificable

Conserva el código correcto y una tabla breve:

| Error provocado | Mensaje esencial | Causa | Corrección |
|---|---|---|---|
| Falta `;` | … | La instrucción no termina | Añadir `;` |

La evidencia debe permitir localizar el código y comprobar que el programa vuelve a ejecutarse después de la corrección.

## Errores frecuentes

- Confundir `Main` con `main`.
- Escribir `string` en lugar de `String`.
- Corregir una línea distinta de la que señala el primer error.
- Usar una palabra reservada como nombre.
- Añadir comentarios que solo repiten la instrucción.

## Autoevaluación

Comprueba que puedes:

- localizar clase, `main` e instrucciones;
- explicar por qué `Main.java` y `Main` deben coincidir;
- predecir el orden de salida;
- diagnosticar errores de delimitadores;
- distinguir identificadores válidos, inválidos y poco claros;
- justificar un comentario útil.

## Seguridad y uso de IA

Usa datos ficticios en ejemplos y capturas. Si una IA propone una corrección, identifica primero el error por tu cuenta y verifica la solución compilando y ejecutando.
