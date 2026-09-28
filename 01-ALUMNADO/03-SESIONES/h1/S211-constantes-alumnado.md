# S211 — Constantes, literales y expresiones

## Objetivo

Distinguir variables, constantes y literales; construir expresiones; predecir el tipo y el valor de sus resultados; y comprobar operaciones, precedencia y actualizaciones.

## 1. Constantes con `final`

Una constante representa un dato que no debe cambiar durante la ejecución.

```java
final String NOMBRE_ASISTENTE = "MiniJarvis";
final int ANIO_INICIO = 2026;
```

Por convención, sus nombres se escriben en mayúsculas con guiones bajos.

Esto produce un error de compilación:

```java
final int MAX_INTENTOS = 3;
MAX_INTENTOS = 4;
```

No todo valor repetido debe convertirse en constante. Debe tener un significado estable durante la ejecución.

## 2. Literales

Un literal es un valor escrito directamente en el código:

```java
int horas = 5;               // literal entero
long poblacion = 8000000000L; // literal long
float porcentaje = 82.5F;    // literal float
double nota = 7.5;           // literal double
char inicial = 'L';          // literal char
String mensaje = "Hola";     // literal String
boolean preparado = true;    // literal boolean
```

`'L'` es un carácter y usa comillas simples. `"L"` es un texto y usa comillas dobles.

## 3. Una expresión produce un valor y un tipo

Una expresión combina literales, variables y operadores:

```java
int minutos = 3 * 60;
boolean suficiente = minutos >= 120;
String resumen = "Minutos: " + minutos;
```

Resultados:

- `3 * 60` produce el valor `180` de tipo `int`;
- `minutos >= 120` produce `true` o `false` de tipo `boolean`;
- `"Minutos: " + minutos` produce un `String`.

Una expresión calculada pero no guardada, mostrada ni utilizada no produce un efecto observable.

## 4. Operadores aritméticos

| Operador | Operación |
|---|---|
| `+` | suma o concatenación |
| `-` | resta |
| `*` | multiplicación |
| `/` | división |
| `%` | resto |

División entera y real:

```java
int cocienteEntero = 5 / 2;       // 2
double cocienteReal = 5 / 2.0;    // 2.5
```

Si ambos operandos son enteros, el resultado también es entero y se descarta la parte decimal.

## 5. Precedencia y paréntesis

```java
int resultadoA = 2 + 3 * 4;       // 14
int resultadoB = (2 + 3) * 4;     // 20
```

La multiplicación se realiza antes que la suma. Los paréntesis cambian el orden y hacen explícita la intención.

Predice también:

```java
int resultadoC = 8 * (4 + 2) - 3;
```

## 6. El resto `%`

```java
int caramelos = 10;
int personas = 4;
int restantes = caramelos % personas; // 2
```

`%` no calcula porcentajes: devuelve el resto de la división entera.

Otro uso:

```java
int numero = 8;
int resto = numero % 2;
```

Si `resto` vale `0`, el número es par.

## 7. Actualizar una variable

```java
int tareas = 3;
tareas += 2; // 5
tareas -= 1; // 4
tareas++;    // 5
tareas--;    // 4
```

Traza cada línea de arriba abajo. Los operadores compuestos modifican el valor existente.

## 8. Actividad

Crea una micropráctica que incluya:

- una constante;
- una variable;
- una expresión aritmética;
- una actualización;
- una salida que permita comprobar el resultado.

Antes de ejecutar, anota el valor y el tipo esperados de cada expresión. Prueba además `5 / 2`, `5 / 2.0`, `10 % 4`, `2 + 3 * 4` y `(2 + 3) * 4`.

## Evidencia verificable

Registra para cada prueba:

| Expresión | Valor esperado | Tipo esperado | Resultado observado |
|---|---:|---|---:|
| `5 / 2` | 2 | `int` | … |

Conserva el código y la ejecución en el repositorio o en el lugar indicado para las microprácticas.

## Errores frecuentes

- Intentar reasignar una constante.
- Confundir `%` con porcentaje.
- Esperar `2.5` en una división `int / int`.
- Confundir `'L'` con `"L"`.
- Calcular un resultado sin usarlo.
- Ignorar la precedencia o añadir paréntesis sin justificar su efecto.

## Autoevaluación

Comprueba que puedes:

- distinguir constante, variable y literal;
- indicar el valor y el tipo de una expresión;
- explicar la división entera;
- predecir una expresión con precedencia;
- explicar el resto;
- trazar operadores compuestos e incrementos.

## Seguridad y uso de IA

No uses datos personales reales. Si una IA calcula una expresión, realiza primero tu propia predicción y verifica el resultado ejecutando el código.
