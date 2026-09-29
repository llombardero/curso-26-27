# S210 - Planificar - Variables

| Dato | Valor |
|---|---|
| Hito | H1 — Primer asistente ejecutable |
| Duración prevista | 45 minutos |
| Fase HEXA del hito | Planificar — organizar el trabajo |

> Basada en `00-GUION-DOCENTE-H1-COMPLETO.md`. Selecciona y desarrolla los conceptos, ejemplos, actividades y evidencias útiles para esta sesión.

## Qué vas a aprender

Al terminar, debes planificar datos: qué se guarda, con qué tipo, con qué nombre y dónde se usa.

## Ideas y ejemplos

Úsala antes de la tabla de datos y antes de implementar variables.

Una variable es una zona de memoria identificada por un nombre. El tipo indica qué clase de dato puede guardar. El valor puede cambiar. La variable no es lo mismo que su valor actual.

Empieza con el cambio de valor:

```java
int horasEstudio = 4;
horasEstudio = 5;
```

Di:

La variable permanece; lo que cambia es el valor guardado. Primero `horasEstudio` vale 4 y después vale 5.

Contrasta variable y valor:

```java
String nombreUsuario = "Laura";
```

Pregunta:

Qué es `nombreUsuario` y qué es `"Laura"`.

Muestra dos variables con el mismo valor:

```java
int horasEstudio = 4;
int horasPractica = 4;
```

Pregunta:

Hay una variable o dos. Qué pasaría si después cambia solo `horasEstudio`.

Traza una variable que cambia:

```java
int tareas = 2;
System.out.println(tareas);
tareas = 3;
System.out.println(tareas);
```

Pregunta:

Predice la primera y la segunda salida.

Presenta cinco tipos de uso inmediato:

```java
String nombreUsuario = "Laura";
int horasEstudio = 4;
double notaMedia = 7.5;
boolean objetivoAlcanzado = true;
char inicial = 'L';
```

```text
Nombre -> String
Horas de estudio -> int
Nota media -> double
Objetivo alcanzado -> boolean
Inicial -> char
```

### Mapa mínimo de tipos de Java

Java ofrece más tipos de los que necesitamos usar ahora:

```text
Enteros   -> byte, short, int, long
Decimales -> float, double
Carácter  -> char
Lógico    -> boolean
```

En H1 utilizaremos principalmente `int`, `double`, `char` y `boolean`. No es necesario memorizar todavía sus rangos; sí reconocer qué familia representa cada dato y elegir un tipo compatible con las operaciones previstas.

### Tipos primitivos y tipo de referencia

```text
int, double, char, boolean -> tipos primitivos
String                     -> tipo de referencia; String es una clase
```

En H1 basta con esta distinción inicial. No necesitamos adelantar memoria, identidad de objetos ni constructores para usar correctamente texto, `String` y `Scanner`.

Pregunta de criterio:

Un número de teléfono contiene dígitos. Lo guardarías como número si no vas a hacer cálculos matemáticos con él.

Trabaja renombrado:

```java
int x = 4;
// mejor:
int horasEstudio = 4;

String s = "MiniJarvis";
// mejor:
String nombreAsistente = "MiniJarvis";

boolean b = true;
// mejor:
boolean objetivoAlcanzado = true;

double n = 7.5;
// mejor:
double notaMedia = 7.5;
```

Dinámica rápida:

Muestro solo el nombre de la variable. Decid qué dato esperáis encontrar. Si nadie puede responder, el nombre debe mejorar.

Por último, separa declarar, inicializar y asignar:

```java
int horasEstudio;
```

```java
int horasEstudio = 4;
```

```text
int horasEstudio = 4
tipo nombre valor inicial
```

```java
horasEstudio = 5;
```

```java
int horasEstudio;
horasEstudio = 4;
System.out.println(horasEstudio);
horasEstudio = 5;
System.out.println(horasEstudio);
```

Aclara:

No se vuelve a escribir el tipo si se modifica la variable existente.

Y corta esta confusión:

```java
int tareas = 2;
tareas = 5;
```

Di:

Esto no significa que 2 sea igual a 5. Significa: guarda ahora 5 en `tareas`.

Error frecuente que debes cortar:

`String` no sirve para todo. Elegimos el tipo según lo que necesitamos representar y hacer con el dato.

Vocabulario imprescindible:

- **Declaración:** introduce el tipo y el nombre, por ejemplo `int horasEstudio;`.
- **Inicialización:** declara y proporciona el primer valor, por ejemplo `int horasEstudio = 4;`.
- **Asignación posterior:** cambia el valor sin repetir el tipo, por ejemplo `horasEstudio = 5;`.
- **lowerCamelCase:** convención para nombres como `nombreUsuario` o `horasEstudio`.

## Actividad de la sesión

Antes del código, haced la tabla de datos. Después implementad al menos tres variables, mostradlas por consola, cambiad una y volved a mostrarla para comprobar que entendéis la asignación.

## Evidencia de la sesión

Hoy sí quiero una evidencia individual: cada persona debe poder señalar una variable propia y explicar tipo, nombre, valor inicial y una asignación posterior.

**Dónde y cómo conservar la evidencia:**

- GitHub: código con variables usadas.
- Diario individual: fila S210 con una variable explicada y prueba de salida.
- Moodle: no se entrega todavía.

Qué revisar:

- Que no usen `x`, `dato1` o nombres sin significado.
- Que no repitan valores fijos por todas partes.
- Que sepan distinguir variable y valor.

Modelo de uso del plan de datos:

```text
Dato: nombre ficticio
Tipo: String
Nombre: nombreUsuario
Cambia: sí, lo escribe la persona usuaria
Uso: personalizar el saludo

Dato: horas de estudio
Tipo: int
Nombre: horasEstudio
Cambia: sí
Uso: calcular minutos y decidir si alcanza el objetivo
```

## Comprueba lo aprendido

Cerramos Planificar con un plan de datos. La próxima sesión entraremos más fuerte en Ejecutar: constantes, literales y operaciones.
