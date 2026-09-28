# S212 - Ejecutar - Scanner y conversiones

| Dato | Valor |
|---|---|
| Hito | H1 — Primer asistente ejecutable |
| Duración prevista | 45 minutos |
| Fase HEXA del hito | Ejecutar — crear |

> Basada en `00-GUION-DOCENTE-H1-COMPLETO.md`. Selecciona y desarrolla los conceptos, ejemplos, actividades y evidencias útiles para esta sesión.

## Qué vas a aprender

Al terminar, debes leer entrada, guardarla, convertir texto a número cuando haga falta y reconocer errores de conversión.

## Ideas y ejemplos

Úsala al pasar de datos escritos en código a datos introducidos por consola.

`Scanner` permite leer lo que una persona escribe. `nextLine()` devuelve siempre un `String`. Si queremos calcular con un número escrito por teclado, necesitamos parsear ese texto.

Empieza por el flujo pedir, leer y guardar creando una sola instancia reutilizable de `Scanner`:

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] argumentos) {
        Scanner teclado = new Scanner(System.in);

        System.out.print("Escribe un nombre ficticio: ");
        String nombreUsuario = teclado.nextLine();

        System.out.println("Hola, " + nombreUsuario);
    }
}
```

Pregunta:

Qué parte prepara la lectura, qué variable guarda el `Scanner` y qué devuelve `teclado.nextLine()`.

Una segunda lectura reutiliza la misma instancia:

```java
System.out.print("Escribe las horas de estudio: ");
String texto = teclado.nextLine();
int horas = Integer.parseInt(texto);
```

La forma compacta siguiente puede leer una línea, pero no será el modelo de H1 porque oculta la reutilización del mismo `Scanner`:

```java
String nombreUsuario = new Scanner(System.in).nextLine();
```

Contrasta usar y no usar lo leído:

```java
String nombreUsuario = teclado.nextLine();
System.out.println("Hola, " + nombreUsuario);
```

```java
String nombreUsuario = teclado.nextLine();
System.out.println("Hola");
```

Pregunta:

En cuál de los dos programas la entrada afecta al comportamiento observable.

Dibuja el flujo en la pizarra:

```text
TECLADO -> nextLine() -> String -> variable -> programa -> salida
```

Después pasa a parsear texto:

```java
String texto = "5";
int horas = Integer.parseInt(texto);
```

```java
String texto = teclado.nextLine();
int horas = Integer.parseInt(texto);
int minutos = horas * 60;
System.out.println(minutos);
```

Pregunta:

Para una entrada `2`, qué salida esperas.

Muestra otros parseos sin dedicarles el mismo tiempo:

```java
String texto = "7.5";
double nota = Double.parseDouble(texto);
```

```java
boolean correcto = Boolean.parseBoolean(texto);
```

Di:

En H1 priorizamos `parseInt` y `parseDouble`. El boolean aparece solo como otro ejemplo de conversión.

Explica conversión implícita:

```java
int entero = 7;
double valorAmpliado = entero;
```

```text
7 -> 7.0
```

```java
int horas = 4;
double horasDecimales = horas;
```

Pregunta:

Se ha producido una conversión aunque no veamos casting escrito.

Contrasta con parseo:

```java
String texto = "4";
int horas = Integer.parseInt(texto);

int otrasHoras = 4;
double horasDecimales = otrasHoras;
```

Pregunta:

En cuál partíamos de texto.

Explica casting y pérdida de información:

```java
double precio = 12.75;
int precioEntero = (int) precio;
```

```text
precioEntero -> 12
```

```java
double nota = 7.99;
int notaEntera = (int) nota;
```

```text
notaEntera -> 7
```

Caso revelador:

```java
double valor = 3.999;
int resultado = (int) valor;
```

Pregunta:

El resultado será 3 o 4. Por qué.

Termina distinguiendo tres mecanismos:

```text
Texto a número: Integer.parseInt("5")
Número compatible a tipo más amplio: double valorDecimal = 5;
Conversión forzada: int valorEntero = (int) 5.8;
```

Pregunta al alumnado:

Qué devuelve `nextLine`, qué guarda `nombreUsuario`, qué convierte `parseInt` y cuándo falla `Integer.parseInt("hola")`.

Error frecuente que debes cortar:

Que el texto contenga cifras no lo convierte automáticamente en número.

Si `Integer.parseInt` o `Double.parseDouble` reciben un texto incompatible, el programa compila pero falla durante la ejecución con una **`NumberFormatException`**. En H1 basta con reconocer la causa, registrar la entrada que produjo el error y distinguirla de un error de compilación.

## Actividad de la sesión

Construid una prueba con entrada válida: por ejemplo horas como texto, conversión a `int`, cálculo de minutos y salida. Después probad una entrada no convertible y explicad cuándo falla: al compilar o al ejecutar.

## Evidencia de la sesión

Hoy la evidencia debe incluir una entrada válida, resultado esperado, resultado obtenido y explicación de qué ocurre con una entrada no convertible.

**Dónde y cómo conservar la evidencia:**

- GitHub: código con `Scanner` o ejercicio de conversión.
- README puede ir recogiendo ejemplo, aunque se pedirá formalmente en S214.
- Diario individual: fila S212 con prueba válida y error de conversión explicado.
- Moodle: no se entrega todavía.

Qué no aceptar:

- Captura sin decir qué entrada se usó.
- Código que lee una variable pero no la usa.
- Decir `no funciona` sin distinguir compilación y ejecución.

Modelo de uso de evidencia S212:

```text
Prueba: conversión de horas.
Entrada válida: 5
Salida esperada: 300 minutos.
Salida obtenida: 300 minutos.
Demuestra: el texto leído se convierte a int y se usa en una operación.

Entrada no convertible: hola
Resultado: error durante la ejecución al aplicar Integer.parseInt.
Demuestra: compilar no garantiza que cualquier entrada sea convertible.
```

## Comprueba lo aprendido

Hoy MiniJarvis ya no solo muestra datos escritos por quien programa. Ahora reacciona a una entrada. Pero si la entrada viene como texto, debemos decidir cuándo convertir y cómo comprobar el resultado.
