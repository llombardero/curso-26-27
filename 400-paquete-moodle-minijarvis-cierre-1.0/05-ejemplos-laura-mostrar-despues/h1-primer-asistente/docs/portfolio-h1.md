# Portfolio individual — H1 Primer asistente básico

Alumno/a: Laura García Martín  
Equipo: Equipo Ada  
Fecha: ejemplo docente

---

## 1. Qué he hecho yo

Mi aportación:

```text
He creado una primera versión sencilla de MiniJarvis por consola. He escrito la clase Main, he usado Scanner para pedir el nombre, he creado constantes para el nombre del asistente y el año del curso, he probado la ejecución y he preparado la documentación básica del hito.
```

---

## 2. Qué hace nuestro programa

```text
El programa saluda como MiniJarvis, pregunta el nombre de la persona usuaria, guarda ese nombre en una variable y después muestra varios mensajes relacionados con el proyecto del curso.
```

---

## 3. Qué he aprendido

| Concepto | Qué he entendido |
|---|---|
| `main` | Es el punto donde empieza a ejecutarse el programa Java. |
| Variable | Guarda un valor que puedo usar después, como el nombre del usuario. |
| Constante | Guarda un valor que no debería cambiar, usando `final`. |
| `Scanner` | Permite leer texto introducido por teclado. |
| `System.out.println` | Muestra un mensaje por pantalla y salta de línea. |
| Ejecutar en IntelliJ | Abrir `src/Main.java` y pulsar Run con el SDK configurado. |

---

## 4. Problemas encontrados

| Problema | Cómo lo detecté | Cómo lo resolví |
|---|---|---|
| Quería añadir un menú | Vi que necesitaba bucles y decisiones que aún no tocaban | Lo dejé para H2 y mantuve H1 simple. |
| Al principio no distinguía texto literal y variable | Imprimía el nombre de la constante dentro de comillas | Saqué la constante fuera de las comillas y usé concatenación. |

---

## 5. Código que sé defender

### Fragmento 1

```java
final String ASSISTANT_NAME = "MiniJarvis";
final int COURSE_YEAR = 2026;
```

Explicación:

```text
Son constantes. Uso final porque el nombre del asistente y el año del curso no deberían cambiar durante la ejecución.
```

### Fragmento 2

```java
System.out.print("¿Cómo te llamas? ");
String userName = scanner.nextLine();
```

Explicación:

```text
Primero muestro una pregunta sin saltar de línea. Después leo la respuesta de la persona usuaria y la guardo en la variable userName.
```

---

## 6. Qué NO hemos añadido todavía

```text
[x] Menú.
[x] Bucles.
[x] switch.
[x] Memoria.
[x] IA real.
```

¿Por qué no pertenece todavía a H1?

```text
Porque H1 es solo la primera versión básica. El menú y los bucles pertenecen a H2; la memoria a H3; y la IA real o simulada se trabajará más adelante cuando sepamos validar y documentar mejor.
```

---

## 7. Uso de IA

He usado IA:

```text
Sí
```

Resumen:

```text
La he usado para entender qué significa final en Java. Acepté la idea de usar constantes para valores que no cambian, pero escribí mis propios mensajes y mantuve el código al nivel de H1.
```

Registro completo:

```text
docs/registro-ia.md
```

---

## 8. Qué necesito mejorar

```text
Necesito mejorar la lectura de errores de compilación y practicar más la diferencia entre texto literal, variables y concatenación.
```

---

## 9. Preguntas que puedo responder en defensa

### ¿Dónde empieza el programa?

```text
En el método public static void main(String[] args).
```

### ¿Qué variable guarda el nombre?

```text
La variable String userName.
```

### ¿Qué constante has usado?

```text
ASSISTANT_NAME para el nombre del asistente y COURSE_YEAR para el año del curso.
```

### ¿Qué hace Scanner?

```text
Scanner permite leer datos que introduce la persona usuaria por teclado.
```

### ¿Cómo ejecutas el proyecto?

```text
Desde IntelliJ abro src/Main.java y pulso Run. También puedo compilar con javac src/Main.java y ejecutar con java -cp src Main.
```

<!-- AJUSTE-COBERTURA-CONCEPTOS-32 -->

## Respuesta de Laura — cobertura de conceptos de Programación

Relación con `32-lista-conceptos-programacion-por-tema.md`:

```text
H1 trabaja principalmente: Tema 1.
Foco de aprendizaje: primer programa Java por consola y asistente mínimo.
```

Conceptos que Laura debe saber defender en este hito:

- programa
- instrucción
- sintaxis
- comentarios
- variable
- tipo de dato
- literal
- String
- Scanner
- entrada/salida
- operadores
- expresiones
- conversiones básicas

Respuesta modelo de Laura:

> En H1 defiendo que mi MiniJarvis todavía es sencillo, pero ya usa variables, tipos, salida por consola, entrada de usuario y nombres legibles.

Evidencia que Laura debe señalar:

- una parte concreta del código o documento donde aparezca el concepto;
- una prueba, ejecución, captura o explicación que demuestre que no lo ha copiado sin entender;
- una mejora razonable que podría hacer si tuviera más tiempo.

