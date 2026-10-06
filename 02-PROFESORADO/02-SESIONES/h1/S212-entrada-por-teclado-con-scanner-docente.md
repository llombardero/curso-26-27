# S212 — Scanner, lectura, conversiones y errores de ejecución

| Dato | Valor |
|---|---|
| Hito | H1 — Primer asistente ejecutable |
| Duración prevista | 45 minutos |
| Fase HEXA del hito | Ejecutar — crear |
| Modalidad de trabajo | **INDIVIDUAL → PAREJAS** |

> Basada en `00-GUION-DOCENTE-H1-COMPLETO.md`.

## Qué vas a aprender

Al terminar, cada persona debe poder pedir un dato, leerlo con una instancia reutilizable de `Scanner`, guardarlo, convertirlo, realizar un cálculo y producir y mostrar una comparación booleana sin bifurcar el flujo. También debe distinguir parseo, conversión implícita y casting, y explicar por qué una entrada no convertible puede provocar una `NumberFormatException` durante la ejecución.

## Antes de entrar en clase

- [ ] Abrir y ejecutar el proyecto que utilizará el alumnado.
- [ ] Preparar entradas ficticias para una lectura de texto, una conversión válida y otra no convertible.
- [ ] Comprobar que el entorno muestra con claridad los mensajes de compilación y de ejecución.
- [ ] Reservar el final para contrastar una predicción con el resultado observado.

## Apertura docente

Di en voz alta:

> Hasta ahora muchos datos los decidía quien programaba. Hoy MiniJarvis empezará a recibir datos de quien lo ejecuta. Para conseguirlo necesitamos pedir, leer, guardar, convertir cuando haga falta, utilizar el dato y mostrar un resultado.

Pregunta inicial:

> Si escribimos `5` en el teclado, ¿`nextLine()` entrega directamente un número o entrega texto?

## Temporalización orientativa

| Tiempo | Acción |
|---|---|
| 0–4 min | Presentar el flujo completo y predecir qué devuelve `nextLine()`. |
| 4–12 min | Explicar importación, instancia reutilizable, petición, lectura, almacenamiento y uso. |
| 12–22 min | Núcleo práctico individual: usar `Scanner`, leer con `nextLine()`, almacenar, parsear, calcular y mostrar una comparación booleana sin bifurcación. |
| 22–30 min | Núcleo práctico por parejas: comparar implementaciones, contrastar predicciones y analizar una entrada no convertible. |
| 30–36 min | Contraste guiado: distinguir conversión implícita y casting; usar `(int) 3.999` como predicción central sobre pérdida de información. |
| 36–40 min | Caso breve de análisis: reconocer `NumberFormatException` y distinguir error de compilación y de ejecución. |
| 40–45 min | Comprobar la prueba, explicar el recorrido del dato y cerrar. |

## Ideas y ejemplos

### Pedir, leer, guardar y utilizar

`Scanner` permite leer lo que una persona escribe. En H1 utilizaremos una sola instancia y la reutilizaremos. `nextLine()` devuelve siempre un `String`, incluso cuando el texto contiene cifras.

Proyecta el programa completo para que se vea también la importación:

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

Recorre el código en este orden:

1. `import java.util.Scanner` hace disponible la clase.
2. `new Scanner(System.in)` prepara la lectura desde la entrada estándar.
3. La variable `teclado` guarda la instancia para reutilizarla.
4. `nextLine()` espera una línea y devuelve un `String`.
5. `nombreUsuario` almacena el dato leído.
6. La última instrucción utiliza ese dato en la salida.

En H1 basta con esta explicación operativa. Clase, objeto y constructor se estudiarán con más profundidad más adelante.

Pregunta:

> ¿Qué parte prepara la lectura, qué variable guarda el `Scanner`, qué devuelve `teclado.nextLine()` y dónde queda almacenado el dato?

Dibuja el flujo:

```text
TECLADO -> nextLine() -> String -> variable -> programa -> salida
```

### Reutilizar la misma instancia

Una segunda lectura utiliza la misma variable `teclado`:

```java
System.out.print("Escribe las horas de estudio: ");
String texto = teclado.nextLine();
int horas = Integer.parseInt(texto);
```

Pregunta:

> ¿Hemos creado otro `Scanner` o hemos reutilizado el mismo? ¿En qué variable queda la línea leída antes de convertirla?

Como contraste, muestra esta forma compacta:

```java
String nombreUsuario = new Scanner(System.in).nextLine();
```

Puede leer una línea, pero no será el modelo de H1 porque oculta la reutilización. El modelo será crear `Scanner teclado = new Scanner(System.in);` una vez y leer después mediante `teclado.nextLine()`.

### Leer no es lo mismo que utilizar

Contrasta estos dos fragmentos:

```java
String nombreUsuario = teclado.nextLine();
System.out.println("Hola, " + nombreUsuario);
```

```java
String nombreUsuario = teclado.nextLine();
System.out.println("Hola");
```

En ambos casos el dato se lee y se almacena. Solo en el primero afecta a la salida.

Pregunta:

> ¿Dónde queda almacenado el dato en cada fragmento? ¿En cuál de ellos se utiliza después? ¿Qué diferencia observable produce?

### Parsear texto para obtener un número

Leer cifras con `nextLine()` sigue produciendo un `String`. Para operar numéricamente hay que transformar ese texto en un valor numérico compatible.

```java
String texto = "5";
int horas = Integer.parseInt(texto);
```

La secuencia conceptual es:

```text
String -> parseo -> número
```

Aplícala a una lectura real:

```java
String texto = teclado.nextLine();
int horas = Integer.parseInt(texto);
int minutos = horas * 60;
boolean alcanzaReferencia = horas >= 4;
System.out.println(minutos);
System.out.println(alcanzaReferencia);
```

Antes de ejecutar, pregunta:

> Si la entrada es `2`, ¿qué guarda `texto`, qué guarda `horas`, qué cálculo se muestra y qué valor tiene `alcanzaReferencia`?

Después de ejecutar, contrasta la salida observada con la predicción.

Aclara el límite:

> `horas >= 4` produce un `boolean`. En H1 lo almacenamos y mostramos; no lo utilizamos con `if` ni para elegir caminos de ejecución.

### `parseDouble` y `parseBoolean`

Muestra el parseo de un decimal:

```java
String texto = "7.5";
double nota = Double.parseDouble(texto);
```

Pregunta:

> ¿Qué tipo tiene `texto` antes del parseo y qué tipo tiene `nota` después?

Como ejemplo secundario, muestra también:

```java
boolean correcto = Boolean.parseBoolean(texto);
```

En esta sesión se practican principalmente `Integer.parseInt(...)` y `Double.parseDouble(...)`. `Boolean.parseBoolean(...)` aparece solo para reconocer que también existe conversión desde texto a un valor booleano.

### Parseo, conversión implícita y casting no son lo mismo

#### Conversión implícita

Un `int` puede pasar a `double` sin escribir un casting explícito:

```java
int entero = 7;
double valorAmpliado = entero;
```

Resultado:

```text
7 -> 7.0
```

Otro ejemplo:

```java
int horas = 4;
double horasDecimales = horas;
```

Pregunta:

> ¿Ha ocurrido una conversión aunque no aparezca un casting escrito? ¿El valor de origen era texto o ya era un número?

#### Contraste con parseo

```java
String texto = "4";
int horas = Integer.parseInt(texto);

int otrasHoras = 4;
double horasDecimales = otrasHoras;
```

Pregunta:

> ¿En cuál de las dos conversiones partíamos de un `String`? ¿Cuál necesita `parseInt`?

Con este contraste, pasa del parseo y la conversión implícita al casting y a su posible pérdida de información.

### Casting y pérdida de información

Muestra:

```java
double precio = 12.75;
int precioEntero = (int) precio;
```

Resultado:

```text
precioEntero -> 12
```

Otro ejemplo:

```java
double nota = 7.99;
int notaEntera = (int) nota;
```

Resultado:

```text
notaEntera -> 7
```

Antes de ejecutar el caso revelador, exige una predicción:

```java
double valor = 3.999;
int resultado = (int) valor;
```

Pregunta:

> ¿El resultado será 3 o 4? ¿Qué parte del valor se pierde?

Explica que este casting no redondea: descarta la parte decimal. La información perdida no puede recuperarse desde el `int` resultante.

Termina distinguiendo los tres mecanismos:

```text
Texto a número: Integer.parseInt("5")
Número compatible a tipo más amplio: double valorDecimal = 5;
Conversión forzada: int valorEntero = (int) 5.8;
```

### Error de ejecución: `NumberFormatException`

Pregunta antes de probar:

> ¿Qué ocurrirá si `Integer.parseInt(...)` recibe `"hola"`? ¿Fallará al compilar o al ejecutar?

Si `Integer.parseInt` o `Double.parseDouble` reciben un texto incompatible, el programa puede compilar y después fallar durante la ejecución con una `NumberFormatException`.

Distingue:

- **Error de compilación:** impide obtener o ejecutar el programa por un problema que el compilador detecta en el código.
- **Error de ejecución:** aparece cuando el programa ya se está ejecutando; en este caso, al intentar convertir un texto incompatible.

En H1 basta con reconocer la causa, identificar el texto que se intentó convertir y distinguir el momento del fallo. No introduzcas todavía tratamiento avanzado de excepciones.

### Errores frecuentes que debes cortar

- Creer que `nextLine()` devuelve un número porque se han escrito cifras.
- Crear un nuevo `Scanner` para cada lectura sin necesidad.
- Leer un dato, guardarlo y no utilizarlo.
- Intentar multiplicar o sumar un `String` como si ya fuera un número.
- Confundir `Integer.parseInt(texto)` con un casting numérico.
- Esperar que `(int) 3.999` redondee a 4.
- Decir que `NumberFormatException` es un error de compilación.
- Cambiar código al azar sin aislar lectura, conversión y uso.

## Secuencia de trabajo y modalidad

### Leer, convertir, predecir y probar — INDIVIDUAL

Antes de contrastar con otra persona, cada estudiante realiza un intento propio: utiliza una instancia reutilizable de `Scanner`, almacena la lectura, predice el tipo devuelto por `nextLine()` y distingue si un posible fallo aparece al compilar o al ejecutar.

Núcleo práctico sugerido:

> Pide unas horas como texto, conviértelas a `int`, calcula los minutos, compara las horas con una referencia y muestra tanto el cálculo como el resultado `boolean`. No utilices ese resultado para decidir instrucciones. Predice primero la salida para una entrada válida. Después prueba una entrada no convertible y explica qué instrucción falla y por qué.

### Comparar, probar y explicar — PAREJAS

Después del intento individual, las parejas:

- comparan sus implementaciones;
- explican dónde se almacena cada lectura;
- contrastan sus predicciones;
- prueban entradas válidas distintas;
- reproducen una entrada no convertible;
- localizan la instrucción y el dato que causan el error;
- distinguen lectura, parseo, conversión implícita y casting;
- explican qué información se pierde al convertir `double` a `int`.

No basta con que una persona escriba y la otra observe. Ambas deben poder recorrer verbalmente:

```text
petición -> lectura -> almacenamiento -> conversión -> cálculo -> comparación booleana -> salida
```

## Evidencia que permanece

- **GitHub:** código con `Scanner`, lectura almacenada, conversión, cálculo, comparación booleana visible sin bifurcación y pruebas reproducibles con una entrada válida y otra no convertible.
- **Scrum:** solo si cambia una tarea o aparece una decisión o bloqueo real.
- **Diario individual:** solo si el error o la diferencia entre predicción y resultado produjo aprendizaje significativo.
- **README:** puede recoger anticipadamente un ejemplo si resulta útil; su consolidación formal corresponde a S214.
- **Moodle / Drive / Site:** sin entrega o actualización específica en S212.

No se crean capturas rutinarias, filas obligatorias, documentos paralelos de pruebas ni microentregas.

Modelo para razonar sobre la prueba:

```text
Prueba: conversión de horas.
Entrada válida: 5
Salida esperada: 300 minutos.
Salida obtenida: 300 minutos.
Comparación: 5 >= 4
Resultado booleano esperado y obtenido: true.
Demuestra: el texto leído se convierte a int, se usa en una operación y produce un booleano visible sin bifurcación.

Entrada no convertible: hola
Resultado: error durante la ejecución al aplicar Integer.parseInt.
Demuestra: compilar no garantiza que cualquier entrada sea convertible.
```

## Observación docente

Durante el intento individual y el contraste por parejas, observa específicamente:

- que sabe que `nextLine()` devuelve un `String`;
- que identifica la variable que recibe el dato;
- que distingue leer, almacenar y utilizar;
- que crea una instancia razonablemente reutilizable de `Scanner`;
- que diferencia `String` de un tipo numérico;
- que reconoce cuándo necesita `Integer.parseInt` o `Double.parseDouble`;
- que realiza un cálculo y muestra su resultado;
- que produce y muestra una comparación booleana sin usarla para decidir el flujo;
- que explica la diferencia entre parseo, conversión implícita y casting;
- que predice la pérdida de información antes de ejecutar el casting;
- que distingue error de compilación y error de ejecución;
- que puede explicar la causa de `NumberFormatException` en el nivel trabajado;
- que prueba con datos ficticios y no introduce datos personales ni credenciales.

## Andamiaje ante bloqueos

No proporciones inmediatamente la solución completa. Utiliza la ayuda mínima necesaria:

- **No encuentra el dato leído:** pide que señale la variable situada a la izquierda de `teclado.nextLine()`.
- **Lee pero no utiliza:** pregunta en qué instrucción posterior vuelve a aparecer la variable.
- **Intenta operar con un `String`:** pregunta qué tipo necesita la operación y qué tipo devuelve `nextLine()`.
- **Confunde parseo y casting:** pregunta si el valor de origen es texto o ya es un número.
- **No entiende `(int) 3.999`:** exige una predicción y separa parte entera y parte decimal antes de ejecutar.
- **Aparece `NumberFormatException`:** pide copiar verbalmente el texto exacto que se intentó convertir y localizar la llamada de parseo.
- **Confunde compilación y ejecución:** pregunta si el programa llegó a iniciarse y en qué momento apareció el mensaje.
- **Cambia código al azar:** aísla lectura, almacenamiento, conversión y uso, y comprueba cada paso por separado.
- **Una persona resuelve todo:** pide a la otra que explique el recorrido y prediga una nueva entrada antes de ejecutarla.

## Límite de la sesión

Los valores de prueba sirven para comprobar lectura, conversión, cálculo y una comparación booleana observable. Los operadores lógicos complejos, `if`, `if/else` y cualquier bifurcación comienzan en H2; no forman parte de S212.

## Comprueba lo aprendido

Pregunta principal:

> ¿Qué devuelve `nextLine()`, dónde se almacena, cuándo necesitas parsear, qué cálculo y comparación se realizan, qué `boolean` se muestra y por qué `Integer.parseInt("hola")` puede provocar una `NumberFormatException` durante la ejecución aunque el programa compile?

Pregunta complementaria:

> ¿Dónde se reutiliza el `Scanner`, en qué se diferencian parseo, conversión implícita y casting, y qué información se pierde al convertir `(int) 3.999`?

Cierra en voz alta:

> Hoy MiniJarvis recibe texto con `nextLine()`, lo convierte, calcula y muestra una comparación booleana. El programa sigue siendo secuencial: utilizar ese resultado para decidir instrucciones corresponde a H2. También comprobamos qué ocurre con una entrada no convertible.

## Al terminar

Anota solo lo necesario para la continuidad docente: alumnado que necesita apoyo, confusión frecuente que conviene retomar, bloqueo técnico pendiente con su siguiente paso y ajuste de tiempo necesario.
