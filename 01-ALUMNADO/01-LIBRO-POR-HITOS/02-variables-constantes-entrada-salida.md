# Capítulo 02 — Variables, constantes y entrada/salida

## Correspondencia

```text
Tema 1 — Aspectos básicos de la programación
RA principal: RA1
H1 — Primer asistente por consola
```

Este capítulo continúa H1. MiniJarvis deja de limitarse a mostrar mensajes fijos: empieza a almacenar datos, recibir información de la persona usuaria y realizar cálculos sencillos.

## 1. Qué vas a aprender

Al terminar este capítulo podrás:

- explicar para qué sirve una variable;
- declarar, inicializar y modificar variables;
- elegir entre varios tipos de datos básicos según la información que necesites guardar;
- distinguir entre variable, constante y literal;
- utilizar nombres de variables claros y coherentes;
- leer texto introducido por teclado mediante `Scanner`;
- mostrar información utilizando `print` y `println`;
- combinar texto y datos en una misma salida;
- utilizar operadores de asignación, aritméticos, de comparación y booleanos;
- predecir el resultado de expresiones sencillas teniendo en cuenta su precedencia;
- convertir texto a valores numéricos cuando sea necesario;
- reconocer que una conversión puede producir un error si el contenido no tiene el formato esperado;
- realizar pequeños cálculos y comprobar sus resultados sin introducir todavía menús ni estructuras de repetición.

## 2. Dónde encaja

En el capítulo anterior MiniJarvis podía ejecutar instrucciones y mostrar mensajes.

Ahora necesitamos que los datos puedan cambiar.

Por ejemplo:

```text
nombre de la persona
horas de estudio
nombre del asistente
curso
resultado de un cálculo
```

No todos estos datos tienen las mismas características.

Algunos cambian durante la ejecución. Otros deben permanecer constantes. Algunos son texto y otros son números.

Por eso necesitamos comprender:

```text
dato
 ↓
tipo
 ↓
variable o constante
 ↓
operación
 ↓
resultado
```

Todavía no vamos a construir un menú ni un programa que repita acciones. Eso llegará en H2.

## 3. Variables

Una variable permite guardar un valor con un nombre.

```java
String userName = "Laura";
```

Podemos leerlo así:

```text
tipo        nombre         valor inicial
String      userName       "Laura"
```

El valor puede cambiar:

```java
userName = "Álex";
```

La segunda instrucción no vuelve a declarar la variable. Le asigna un nuevo valor.

### 3.1. Declarar, inicializar y asignar

Estas acciones están relacionadas, pero no significan exactamente lo mismo.

Declarar:

```java
int studyHours;
```

Inicializar:

```java
studyHours = 4;
```

También podemos hacerlo a la vez:

```java
int studyHours = 4;
```

Y posteriormente cambiar el valor:

```java
studyHours = 5;
```

## 4. Elegir el tipo adecuado

El tipo indica qué clase de dato puede almacenar una variable y qué operaciones podremos realizar con ella.

En estos primeros programas utilizaremos especialmente:

| Tipo | Ejemplo de uso |
|---|---|
| `int` | número entero de intentos u horas |
| `double` | valor numérico con decimales |
| `boolean` | verdadero o falso |
| `char` | un único carácter |
| `String` | texto |

Ejemplos:

```java
int studyHours = 4;
double average = 7.5;
boolean active = true;
char option = 'A';
String userName = "Laura";
```

Observa que `String` comienza con mayúscula. No es un tipo primitivo como `int` o `boolean`, aunque en estos primeros programas lo utilizaremos continuamente para trabajar con texto.

## 5. Literales

Un literal es un valor escrito directamente en el código.

En:

```java
int studyHours = 4;
```

`4` es un literal entero.

En:

```java
String agentName = "MiniJarvis";
```

`"MiniJarvis"` es un literal de texto.

Otros ejemplos:

```text
7.5
true
'A'
```

Una variable tiene nombre. El literal es el valor escrito directamente.

## 6. Constantes

Cuando un valor no debe modificarse durante la ejecución podemos expresarlo mediante `final`.

```java
final String AGENT_NAME = "MiniJarvis";
```

Así comunicamos dos ideas:

1. ese dato tiene un significado importante;
2. no esperamos que cambie durante la ejecución.

En estos primeros programas utilizaremos nombres en mayúsculas para las constantes:

```text
AGENT_NAME
COURSE_YEAR
```

No conviertas en constante cualquier dato. El nombre de la persona usuaria, por ejemplo, debe poder variar.

## 7. Nombres claros

Compara:

```java
String n;
int h;
```

con:

```java
String userName;
int studyHours;
```

El segundo código permite comprender mejor qué representa cada dato.

Un nombre debe ayudarnos a entender la intención del programa.

## 8. Entrada y salida

### 8.1. Mostrar información

Ya conocemos:

```java
System.out.println("Hola");
```

`println` muestra el contenido y después pasa a una nueva línea.

También podemos usar:

```java
System.out.print("¿Cómo te llamas? ");
```

`print` permite que la entrada de la persona usuaria aparezca en la misma línea.

### 8.2. Leer desde teclado

Para leer datos utilizaremos `Scanner`.

Primero importamos la clase:

```java
import java.util.Scanner;
```

Después creamos un objeto:

```java
Scanner scanner = new Scanner(System.in);
```

Y podemos leer una línea:

```java
String userName = scanner.nextLine();
```

Aunque todavía no hayamos estudiado en profundidad clases, objetos y constructores, ya podemos reconocer que estamos utilizando una clase proporcionada por Java.

Más adelante comprenderemos con mayor profundidad qué significa:

```java
new Scanner(System.in)
```

### 8.3. Un primer diálogo

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        final String AGENT_NAME = "MiniJarvis";

        Scanner scanner = new Scanner(System.in);

        System.out.print("¿Cómo te llamas? ");
        String userName = scanner.nextLine();

        System.out.println("Hola, " + userName + ".");
        System.out.println("Soy " + AGENT_NAME + ".");
    }
}
```

Ahora la salida depende de un dato introducido durante la ejecución.

MiniJarvis empieza a interactuar.

## 9. Concatenación

El operador `+` también puede utilizarse para construir mensajes.

```java
String userName = "Laura";

System.out.println("Hola, " + userName + ".");
```

Resultado:

```text
Hola, Laura.
```

Observa la diferencia entre:

```java
System.out.println(2 + 3);
```

y:

```java
System.out.println("Resultado: " + 2 + 3);
```

Antes de ejecutar, intenta predecir ambas salidas.

Cuando mezclamos texto y números debemos prestar atención al orden de evaluación.

Podemos hacer explícita nuestra intención utilizando paréntesis:

```java
System.out.println("Resultado: " + (2 + 3));
```

## 10. Operadores y expresiones

### 10.1. Asignación

```java
int studyHours = 3;
```

El `=` almacena el valor de la derecha en la variable de la izquierda.

No significa «es igual que» en el sentido matemático.

### 10.2. Operadores aritméticos

Podemos realizar cálculos sencillos:

```java
int total = 3 + 2;
int difference = 5 - 2;
int product = 4 * 3;
int quotient = 8 / 2;
int remainder = 7 % 2;
```

El operador `%` obtiene el resto de una división.

### 10.3. Precedencia

No todos los operadores se evalúan al mismo tiempo.

Compara:

```java
int result = 2 + 3 * 4;
```

con:

```java
int result = (2 + 3) * 4;
```

Predice ambos valores antes de ejecutar.

Los paréntesis permiten hacer explícito qué operación queremos realizar primero.

### 10.4. Comparaciones

Una comparación produce un valor booleano.

```java
boolean moreThanThree = studyHours > 3;
```

Algunos operadores de comparación son:

```text
>    mayor que
<    menor que
>=   mayor o igual
<=   menor o igual
==   igual
!=   distinto
```

Podemos comprobar el resultado sin tomar todavía ninguna decisión:

```java
int studyHours = 4;
boolean enoughPractice = studyHours >= 3;

System.out.println(enoughPractice);
```

Resultado:

```text
true
```

En el siguiente hito aprenderemos a utilizar ese `true` o `false` para decidir qué instrucciones ejecutar.

### 10.5. Operadores booleanos

Podemos combinar condiciones:

```java
boolean enoughHours = studyHours >= 3;
boolean active = true;

boolean ready = enoughHours && active;
```

Los operadores booleanos básicos son:

```text
&&   y
||   o
!    no
```

No necesitamos construir todavía condiciones complejas. Lo importante es comprender que una expresión puede producir un valor `boolean`.

## 11. Convertir texto a número

### 11.1. El problema

`nextLine()` devuelve texto.

```java
String hoursText = scanner.nextLine();
```

Si la persona escribe:

```text
4
```

seguimos teniendo un texto que representa el número cuatro.

Para calcular necesitamos convertirlo.

### 11.2. Conversión a entero

```java
int studyHours = Integer.parseInt(hoursText);
```

Ejemplo completo:

```java
System.out.print("Horas de estudio: ");

String hoursText = scanner.nextLine();
int studyHours = Integer.parseInt(hoursText);

int nextWeekGoal = studyHours + 1;

System.out.println("Objetivo siguiente: " + nextWeekGoal);
```

### 11.3. Conversión a decimal

Cuando necesitamos decimales podemos trabajar con `double`.

```java
String scoreText = scanner.nextLine();
double score = Double.parseDouble(scoreText);
```

### 11.4. Una conversión puede fallar

¿Qué ocurrirá si intentamos convertir esto?

```text
cuatro
```

mediante:

```java
Integer.parseInt("cuatro");
```

La conversión no puede producir el entero esperado.

En este momento debes:

- reconocer el problema;
- observar el error;
- entender por qué se ha producido.

La forma de controlar estas excepciones se trabajará posteriormente.

No adelantes una solución que todavía no comprendes.

## 12. Conversión entre tipos numéricos

Algunas conversiones entre tipos compatibles pueden realizarse automáticamente.

Por ejemplo:

```java
int hours = 4;
double decimalHours = hours;
```

En otros casos una conversión puede requerir que indiquemos explícitamente nuestra intención.

```java
double value = 7.8;
int integerValue = (int) value;
```

No interpretes el `casting` como un método para «arreglar» errores de tipos.

Antes de convertir debes entender qué información puede cambiar o perderse.

## 13. Llévalo a MiniJarvis

Amplía H1 de forma controlada.

MiniJarvis debe:

1. mantener un nombre constante para el asistente;
2. preguntar el nombre de la persona;
3. guardar la respuesta en una variable;
4. mostrar un saludo personalizado;
5. preguntar cuántas horas ha dedicado a practicar Programación;
6. leer la respuesta como texto;
7. convertirla a `int`;
8. realizar un cálculo sencillo;
9. mostrar el resultado.

Por ejemplo:

```text
¿Cómo te llamas? Laura
Hola, Laura. Soy MiniJarvis.
¿Cuántas horas has practicado Programación? 4
Si la próxima semana practicas una hora más, serán 5 horas.
```

Todavía **no** necesitas:

- decidir si 4 horas son muchas o pocas;
- mostrar mensajes diferentes según la cantidad;
- repetir preguntas;
- construir un menú.

Eso pertenece al siguiente paso del proyecto.

## 14. Comprueba que funciona

### Prueba 1 — Texto normal

```text
Nombre: Laura
```

Comprueba que el nombre aparece correctamente en el saludo.

### Prueba 2 — Nombre diferente

Ejecuta de nuevo con otro nombre.

Comprueba que no has dejado el nombre anterior escrito directamente en la salida.

### Prueba 3 — Número válido

```text
Horas: 4
```

Comprueba el cálculo.

### Prueba 4 — Otro número válido

Utiliza un valor distinto y calcula previamente qué resultado esperas.

Después compáralo con la ejecución.

### Prueba 5 — Texto no numérico

Introduce:

```text
cuatro
```

Observa qué ocurre.

En este momento no es obligatorio controlar el error. Sí debes poder explicar por qué la conversión no puede realizarse.

No necesitas realizar capturas rutinarias de estas pruebas.

## 15. Errores frecuentes

| Problema | Qué observas | Qué revisar |
|---|---|---|
| No importar `Scanner` | Java no reconoce la clase | `import java.util.Scanner;` |
| Usar una variable antes de darle valor | Error de compilación | Declaración e inicialización |
| Confundir `String` e `int` | Operación o asignación incompatible | Tipo del dato |
| Olvidar comillas en un texto | Error de sintaxis | Literales `String` |
| Intentar modificar una constante | Error de compilación | Uso de `final` |
| Concatenar sin pensar en el orden | Resultado distinto al esperado | Precedencia y paréntesis |
| Convertir texto no numérico | Error durante la ejecución | Contenido recibido antes de `parseInt` |
| Elegir nombres poco claros | El código cuesta interpretar | Intención de la variable |
| Cambiar varias cosas a la vez | No sabes qué cambio causó el problema | Modificaciones pequeñas y comprobables |

## 16. Practica y razona

### Actividad A — Tipo adecuado

Elige un tipo para cada dato y explica por qué:

- nombre de usuario;
- número de intentos;
- nota media;
- programa activo o no;
- inicial del nombre.

### Actividad B — Predice el valor

```java
int a = 4;
int b = 2;
int result = a + b * 3;
```

Predice `result`.

Después prueba:

```java
int result = (a + b) * 3;
```

Explica por qué cambia.

### Actividad C — Variable o constante

Decide cuáles deberían ser constantes:

```text
nombre del asistente
nombre introducido por el usuario
año del curso
horas estudiadas esta semana
```

### Actividad D — Comparaciones

Con:

```java
int studyHours = 4;
```

predice el valor de:

```java
studyHours > 3
studyHours == 4
studyHours != 4
studyHours <= 2
```

### Actividad E — Conversión

Explica qué diferencia hay entre:

```java
String hoursText = "4";
```

y:

```java
int studyHours = 4;
```

¿Qué operación necesitas para pasar del primero al segundo?

## 17. Comprueba lo aprendido

Intenta responder sobre tu propio código:

1. ¿Qué diferencia hay entre declarar e inicializar?
2. ¿Por qué `userName` debe ser una variable?
3. ¿Por qué `AGENT_NAME` puede ser una constante?
4. ¿Qué diferencia hay entre variable y literal?
5. ¿Qué tipo utilizarías para un número entero?
6. ¿Qué tipo utilizarías para un valor verdadero/falso?
7. ¿Qué hace `scanner.nextLine()`?
8. ¿Por qué necesitamos convertir algunas entradas?
9. ¿Qué puede ocurrir si usamos `Integer.parseInt` con texto no numérico?
10. ¿Qué diferencia hay entre `=` y `==`?
11. ¿Qué produce una comparación como `studyHours >= 3`?
12. ¿Por qué los paréntesis pueden cambiar el resultado de una expresión?
13. Señala en tu programa una entrada, una variable, una constante, un cálculo y una salida.

## 18. Si vas más rápido

Sin adelantar H2 puedes:

- utilizar también una variable `double`;
- probar conversiones entre `int` y `double`;
- comparar resultados con y sin casting;
- crear varias expresiones booleanas y predecir su valor;
- combinar condiciones con `&&`, `||` y `!` sin utilizarlas todavía para controlar el flujo;
- mejorar nombres de variables;
- localizar literales repetidos y decidir razonadamente si alguno merece convertirse en constante.

No construyas todavía un menú ni añadas bucles solo por haber terminado antes.

## 19. Qué conservar

La evidencia principal sigue siendo el programa H1 funcionando y comprensible.

No necesitas crear:

- un portfolio de este capítulo;
- una tabla de pruebas independiente;
- capturas rutinarias;
- un informe de conversiones;
- una ficha específica de errores.

Cuando se cierre H1, el README conservará la información técnica necesaria para ejecutar la versión evaluada.

Si durante este capítulo aparece un aprendizaje individual especialmente significativo, puede anotarse brevemente en el diario.
