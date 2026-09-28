# S212 — Entrada por teclado y conversiones

## Objetivo

Leer datos con una única instancia de `Scanner`, distinguir texto de número, convertir entradas válidas y documentar tanto una ejecución correcta como una entrada no convertible.

## 1. Pedir, leer, guardar y usar

`Scanner` permite leer lo que una persona escribe en la consola. `nextLine()` siempre devuelve un `String`.

Programa completo:

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] argumentos) {
        Scanner teclado = new Scanner(System.in);

        System.out.print("Nombre ficticio: ");
        String nombreUsuario = teclado.nextLine();

        System.out.print("Horas de estudio: ");
        String textoHoras = teclado.nextLine();
        int horasEstudio = Integer.parseInt(textoHoras);
        int minutosEstudio = horasEstudio * 60;

        System.out.println("Hola, " + nombreUsuario + ".");
        System.out.println("Minutos de estudio: " + minutosEstudio);

        teclado.close();
    }
}
```

La misma instancia `teclado` se reutiliza para todas las lecturas. Se cierra solo cuando el programa ya no necesita leer más, porque cerrar el `Scanner` también cierra `System.in`.

## 2. Entrada usada frente a entrada ignorada

Esto lee un texto, pero no lo guarda ni lo utiliza:

```java
teclado.nextLine();
```

Esto sí conserva el dato:

```java
String nombreUsuario = teclado.nextLine();
```

Para que la entrada tenga un efecto observable, el programa debe guardarla y después mostrarla, convertirla o usarla en una operación.

## 3. Texto y número no son lo mismo

- `"5"` es un `String`.
- `5` es un `int`.
- `7.5` puede representarse como `double`.

Aunque una persona escriba cifras, `nextLine()` devuelve texto. Para calcular hay que convertirlo.

```java
String textoHoras = "5";
int horas = Integer.parseInt(textoHoras);

String textoNota = "7.5";
double nota = Double.parseDouble(textoNota);
```

## 4. Parseo

El parseo interpreta un texto como un valor de otro tipo:

```java
int horas = Integer.parseInt("5");
double nota = Double.parseDouble("7.5");
boolean preparado = Boolean.parseBoolean("true");
```

`parseInt` y `parseDouble` pueden fallar si el texto no representa un número válido.

```java
int numero = Integer.parseInt("hola");
```

Este código compila, pero durante la ejecución produce `NumberFormatException`. En H1 debes reconocer, reproducir y explicar el error; todavía no necesitas resolverlo con `try/catch`.

## 5. Ampliación: conversión implícita y casting

Consulta la píldora S212 para estudiar estos dos mecanismos:

### Conversión implícita

Java puede ampliar automáticamente algunos valores:

```java
int horas = 5;
double horasDecimales = horas; // 5.0
```

### Casting

Un casting fuerza una conversión y puede perder información:

```java
double nota = 8.9;
int notaEntera = (int) nota; // 8
```

No redondea: descarta la parte decimal acercándose a cero.

Parsear, convertir implícitamente y hacer casting no son lo mismo:

- parseo: parte de un `String`;
- conversión implícita: Java amplía un valor automáticamente;
- casting: se indica el tipo de destino de forma explícita.

## 6. Actividad

1. Ejecuta el programa completo con dos nombres ficticios.
2. Prueba dos números válidos y predice los minutos.
3. Prueba una entrada no convertible, como `hola`.
4. Registra cuándo aparece el error y qué método lo provoca.
5. Comprueba que la entrada leída se utiliza realmente.
6. Como ampliación, ejecuta un ejemplo de conversión implícita y otro de casting.

## Evidencia verificable

No entregues una captura aislada. Registra:

| Caso | Entrada | Salida o error esperado | Resultado observado | Qué demuestra |
|---|---|---|---|---|
| Válido | `Laura`, `5` | `300` minutos | … | lectura, parseo y cálculo |
| No convertible | `Sam`, `hola` | `NumberFormatException` | … | el texto no representa un entero |

La evidencia debe permitir ver o enlazar el código, la entrada usada y la salida completa.

## Errores frecuentes

- Pensar que `nextLine()` devuelve un número.
- Crear un `Scanner` nuevo para cada dato.
- Cerrar `teclado` antes de terminar las lecturas.
- Leer una entrada y no guardarla ni usarla.
- Confundir parseo con casting.
- Afirmar que el casting redondea.
- Mostrar solo el mensaje de error sin indicar qué entrada lo produjo.

## Autoevaluación

Comprueba que puedes:

- explicar qué devuelve `nextLine()`;
- reutilizar una sola instancia de `Scanner`;
- describir el flujo pedir → leer → guardar → convertir → calcular → mostrar;
- distinguir `parseInt` y `parseDouble`;
- explicar cuándo aparece `NumberFormatException`;
- reconocer conversión implícita y casting.

## Seguridad y uso de IA

Usa datos ficticios y revisa las capturas antes de publicarlas. Nunca escribas contraseñas, claves ni tokens como entradas de prueba. Si una IA interpreta una excepción, reproduce el caso y verifica su explicación.
