# S210 — Variables: guardar datos con nombre y tipo

## Objetivo

Comprender la relación entre variable, tipo, nombre y valor; distinguir tipos primitivos de `String`; y planificar datos antes de incorporarlos al programa.

## 1. Variable, valor y tipo

Una variable es una zona de memoria identificada por un nombre. El tipo determina qué valores puede guardar y qué operaciones admite.

```java
int horasEstudio = 4;
System.out.println(horasEstudio);
horasEstudio = 5;
System.out.println(horasEstudio);
```

Traza:

| Momento | Valor de `horasEstudio` |
|---|---:|
| Después de inicializar | 4 |
| Después de asignar de nuevo | 5 |

La segunda asignación sustituye el valor anterior. El signo `=` en Java asigna; no expresa una igualdad matemática.

## 2. Mapa de tipos primitivos

Java tiene ocho tipos primitivos:

| Tipo | Uso habitual | Ejemplo |
|---|---|---|
| `byte` | enteros muy pequeños | `byte nivel = 3;` |
| `short` | enteros pequeños | `short dias = 180;` |
| `int` | enteros de uso general | `int horasEstudio = 4;` |
| `long` | enteros muy grandes | `long poblacion = 8000000000L;` |
| `float` | decimales con menor precisión | `float porcentaje = 82.5F;` |
| `double` | decimales de uso general | `double notaMedia = 7.5;` |
| `char` | un carácter | `char inicial = 'L';` |
| `boolean` | verdadero o falso | `boolean objetivoAlcanzado = true;` |

En H1 utilizarás sobre todo `int`, `double`, `boolean` y `char`. Debes reconocer los ocho, pero no memorizar sus rangos.

## 3. `String` no es un tipo primitivo

```java
String nombreUsuario = "Laura";
```

`String` es una clase de Java que representa texto. Por eso empieza con mayúscula. En H1 basta con distinguir:

- tipo primitivo: guarda un valor básico;
- tipo de referencia: permite trabajar con objetos, como los textos `String`.

No necesitas estudiar todavía programación orientada a objetos.

## 4. El tipo depende del dato, no de su apariencia

Un número de teléfono suele guardarse como `String`, no como `int`, porque no vamos a sumarlo y puede contener `+`, espacios o ceros iniciales.

```java
String telefonoFicticio = "+34 000 000 000";
```

Pregúntate siempre qué valores necesitas representar y qué operaciones realizarás.

## 5. Nombres significativos

Poco claros:

```java
String x = "Laura";
int n = 4;
```

Más claros:

```java
String nombreUsuario = "Laura";
int horasEstudio = 4;
```

Usa `lowerCamelCase` para variables: la primera palabra comienza en minúscula y las siguientes en mayúscula.

## 6. Declarar, inicializar y asignar

```java
int horasEstudio;      // declaración
horasEstudio = 4;      // primera asignación o inicialización
horasEstudio = 5;      // nueva asignación
```

También puedes declarar e inicializar en una sola línea:

```java
int horasEstudio = 4;
```

Una variable local debe recibir un valor antes de usarse.

## 7. Plan de datos

Antes de programar, completa una tabla:

| Dato | Tipo | Nombre | ¿Cambia? | ¿Dónde se usa? |
|---|---|---|---|---|
| nombre ficticio | `String` | `nombreUsuario` | sí | saludo |
| horas de estudio | `int` | `horasEstudio` | sí | cálculo |
| nombre del asistente | `String` | `NOMBRE_ASISTENTE` | no | presentación |

Añade al menos dos datos más y justifica el tipo elegido.

## 8. Actividad

1. Implementa entre tres y cinco variables de tu plan.
2. Muestra sus valores.
3. Cambia una variable y vuelve a mostrarla.
4. Explica la traza antes y después.
5. Renombra cualquier identificador vago.

## Evidencia verificable

Conserva la tabla de planificación, el código y una ejecución que muestre el valor antes y después de una asignación. En tu diario registra qué decisión de tipo o nombre has tenido que justificar.

## Errores frecuentes

- Confundir la variable con su valor actual.
- Usar `String` para todo sin pensar en las operaciones.
- Escribir otra vez el tipo al cambiar un valor.
- Usar una variable local antes de inicializarla.
- Elegir nombres válidos pero poco informativos.

## Autoevaluación

Comprueba que puedes:

- identificar tipo, nombre y valor;
- enumerar los ocho tipos primitivos;
- explicar por qué `String` no es primitivo;
- distinguir declaración, inicialización y asignación;
- justificar el tipo de un teléfono, una nota y una respuesta sí/no;
- explicar una traza de dos valores.

## Seguridad y uso de IA

Usa nombres, teléfonos y demás datos ficticios. Si una IA propone nombres o tipos, comprueba que expresen la intención y permitan las operaciones necesarias.
