# H1 — Primer asistente por consola

> Ejemplo privado de Laura. Mostrar solo después del intento propio del alumnado.

## Objetivo

Construir y comprobar una primera versión pequeña de MiniJarvis utilizando únicamente los contenidos trabajados en H1.

Esta versión permite observar:

- la estructura básica de un programa Java;
- la clase `Main` y el método `main`;
- salida por consola;
- variables y constantes;
- tipos `String`, `int` y `boolean`;
- entrada mediante `Scanner`;
- conversión de texto a número;
- un cálculo sencillo;
- una comparación que produce un valor booleano.

No utiliza todavía menús, bucles, `switch`, colecciones, varias clases propias, ficheros, persistencia ni IA real.

---

## Arquitectura de evidencias

Versión estable:

```text
h1-entrega
```

El repositorio y este README son la evidencia técnica canónica.

- Diario individual evolutivo: `../FUENTES-CURSO/01-Diario-individual-MiniJarvis.xlsx`.
- Scrum de equipo evolutivo: `../FUENTES-CURSO/02-Scrum-equipo-MiniJarvis.xlsx`.
- Entrega Moodle mínima: `../ENTREGAS-MOODLE/H1-entrega.md`.

No se crean informes paralelos de ejecución, pruebas, defensa o uso de IA.

---

## Estructura

```text
h1-primer-asistente/
├── README.md
└── src/
    └── Main.java
```

---

## Compilación y ejecución

Desde la carpeta `h1-primer-asistente`:

```bash
javac -d out src/Main.java
java -cp out Main
```

---

## Ejecución comprobable [EQUIPO]

Ejemplo con datos ficticios:

```text
Hola, soy MiniJarvis.
¿Cómo te llamas? Laura
¿Cuántas horas has practicado Programación? 4
Hola, Laura.
Si la próxima semana practicas una hora más, serán 5 horas.
¿Has practicado al menos 3 horas? true
```

La salida puede cambiar según los datos introducidos.

Si en la entrada numérica se escribe un texto no convertible, `Integer.parseInt` produce un error de ejecución. En H1 se observa y se explica ese comportamiento; todavía no se incorpora tratamiento de excepciones.

---

## Qué ocurre en el programa

### Entrada de texto

```java
String userName = scanner.nextLine();
```

`nextLine()` devuelve texto y ese valor se guarda en una variable `String`.

### Entrada numérica

La entrada de consola sigue llegando inicialmente como texto:

```java
String hoursText = scanner.nextLine();
```

Después se convierte:

```java
int studyHours = Integer.parseInt(hoursText);
```

### Cálculo

```java
int nextWeekHours = studyHours + EXTRA_HOURS_NEXT_WEEK;
```

El programa suma una hora al valor introducido.

### Comparación

```java
boolean enoughPractice = studyHours >= REFERENCE_HOURS;
```

La comparación produce `true` o `false`.

No se utiliza todavía ese booleano para ejecutar caminos diferentes del programa.

---

## Decisiones del ejemplo

- Se mantiene todo el código propio dentro de `Main`.
- Se usa `Scanner` para leer por consola.
- La entrada numérica se recibe primero como `String`.
- La conversión se realiza mediante `Integer.parseInt`.
- El cálculo utiliza una constante con nombre.
- La comparación se guarda en una variable `boolean`.
- No se introducen contenidos de hitos posteriores.

---

## Comprobaciones realizadas

Caso utilizado en el ejemplo:

```text
Nombre: Laura
Horas: 4
```

Resultado esperado:

```text
Horas calculadas para la semana siguiente: 5
Comparación con 3 horas: true
```

También puede probarse, por ejemplo:

```text
Nombre: Laura
Horas: 2
```

En ese caso:

```text
Horas calculadas para la semana siguiente: 3
Comparación con 3 horas: false
```

---

## Defensa de Laura [INDIVIDUAL]

Laura debe poder localizar y explicar en el código:

- dónde comienza la ejecución;
- una variable;
- una constante;
- un literal;
- el objeto `Scanner`;
- qué devuelve `nextLine`;
- por qué es necesaria la conversión numérica;
- qué operación realiza el cálculo;
- por qué la comparación produce un `boolean`;
- cómo compilar y ejecutar el programa.

También debe poder modificar un dato sencillo, volver a ejecutar y explicar el cambio.

La defensa se realiza sobre el producto real. No necesita una plantilla escrita independiente.

---

## Idea clave

```text
No es un MiniJarvis avanzado.

Es una primera versión Java pequeña
que Laura puede ejecutar, comprobar,
modificar y explicar por completo.
```
