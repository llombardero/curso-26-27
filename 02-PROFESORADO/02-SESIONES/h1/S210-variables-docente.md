# H1.5 — Variables

| Dato | Valor |
|---|---|
| Hito | H1 — Primer asistente ejecutable |
| Duración prevista | 45 minutos |
| Fase HEXA del hito | Planificar — organizar el trabajo |
| Modalidad de trabajo | **INDIVIDUAL → EQUIPO → comprobación INDIVIDUAL** |

## Temporalización orientativa

| Tiempo | Acción |
|---|---|
| 0–5 min | Presentar la finalidad: planificar datos antes de código. |
| 5–15 min | Explicar variable frente a valor, tipos de uso y renombrado. |
| 15–23 min | Declarar, inicializar y asignar; vocabulario imprescindible. |
| 23–31 min | Actividad individual: comprender, predecir y practicar variables. |
| 31–37 min | Contrastar y planificar en equipo: tabla de datos acordada. |
| 37–41 min | Integrar variables en MiniJarvis y ejecutar con reasignación. |
| 41–45 min | Comprobar comprensión individual y cerrar. |

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

### Comprender, predecir y practicar — INDIVIDUAL

Antes de integrar nada en el producto de equipo, cada persona propone qué datos necesita MiniJarvis y razona para cada uno:

- qué representa;
- qué tipo usaría;
- qué nombre significativo tendría;
- qué valor inicial podría tener.

Debe aplicar los conceptos trabajados previamente en la sesión: variable frente a valor, elección del tipo según el dato y su uso, nombres significativos, declaración, inicialización y asignación posterior.

Después realiza una micropráctica propia: declara e inicializa al menos una variable, predice qué ocurrirá al reasignarla, modifica su valor, ejecuta y comprueba el resultado frente a su predicción.

Esta micropráctica garantiza práctica individual antes de integrar en equipo. No es un nuevo entregable, no se sube a Moodle, Drive o Site y no obliga a crear una fila de diario.

### Contrastar y planificar — EQUIPO

El equipo compara las propuestas individuales y acuerda su plan de datos. Antes del código, hace la tabla de datos y decide:

- datos necesarios;
- tipos;
- nombres;
- valores iniciales;
- uso previsto.

### Integrar en MiniJarvis — EQUIPO

Sobre el incremento compartido, el equipo:

- incorpora al menos tres variables acordadas;
- las utiliza realmente;
- muestra sus valores por consola cuando procede;
- modifica posteriormente al menos una;
- predice el resultado antes de ejecutar y después lo comprueba.

Así se conserva la secuencia de la actividad: implementar al menos tres variables, mostrarlas por consola, cambiar una y volver a mostrarla para comprobar que se entiende la asignación.

### Comprobar comprensión — INDIVIDUAL

Cualquier integrante debe poder señalar una variable del incremento compartido y explicar:

- qué representa;
- cuál es su tipo;
- cuál es su nombre;
- cuál fue su valor inicial;
- dónde cambia;
- qué ocurre cuando cambia;
- por qué se eligió ese tipo y ese nombre.

Si se le pide, debe poder modificar esa variable, predecir el efecto y comprobarlo mediante la ejecución.

Estos momentos organizan el trabajo de la sesión. No se convierten en documentos ni formularios adicionales.

## Evidencia que permanece

- **Equipo — GitHub:** código del incremento con variables, tipos y nombres significativos, al menos una reasignación y ejecución comprobada.
- **Equipo — Scrum:** solo si aparece una decisión, un cambio de planificación o un bloqueo real.
- **Individual — Diario:** solo si existe un aprendizaje, error, bloqueo, decisión o uso relevante de IA que merezca conservarse.
- **README:** no requiere actualización específica en H1.5.
- **Moodle / Drive / Site:** no hay entrega o actualización específica en H1.5.

## Observación docente

Durante la actividad y la comprobación individual, revisa de forma observable:

- que el alumnado distingue la variable de su valor actual, incluso cuando dos variables contienen el mismo valor;
- que selecciona el tipo según el dato que representa y el uso u operaciones previstos;
- que emplea nombres significativos y puede justificar qué esperaría encontrar otra persona al leerlos;
- que distingue declaración, inicialización y asignación posterior;
- que comprende la reasignación como cambio del valor guardado, sin confundirla con una igualdad matemática;
- que predice las salidas antes de ejecutar;
- que ejecuta y comprueba el resultado frente a su predicción;
- que cualquier integrante puede explicar individualmente las decisiones tomadas por el equipo.

Comprueba además que no usen `x`, `dato1` o nombres sin significado y que no repitan valores fijos por todas partes.

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

## Andamiaje ante bloqueos

No reemplaces el razonamiento del alumnado por una solución completa. Utiliza la ayuda mínima que corresponda:

- **Confusión entre variable y valor:** vuelve al ejemplo de dos variables con el mismo valor y pregunta qué permanece y qué podría cambiar por separado.
- **Duda sobre el tipo:** pregunta qué representa el dato y qué operaciones se harán con él.
- **Nombres pobres:** pregunta qué esperaría encontrar otra persona al leer el nombre sin ver el valor.
- **Repetición del tipo al reasignar:** vuelve al contraste entre declaración y asignación posterior.
- **Ejecución sin razonamiento:** pide una predicción concreta antes de permitir la ejecución y contrástala después con el resultado.

## Comprueba lo aprendido

Cerramos Planificar con un plan de datos. La próxima sesión entraremos más fuerte en Ejecutar: constantes, literales y operaciones.
