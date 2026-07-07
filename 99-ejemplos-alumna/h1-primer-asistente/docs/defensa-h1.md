# Preparación de defensa — H1 Primer asistente básico

Alumno/a: Laura García Martín  
Equipo: Equipo Ada  
Fecha: ejemplo docente

---

## 1. Qué voy a defender

```text
Voy a defender el archivo src/Main.java y la documentación básica del hito H1.
```

---

## 2. Explicación general del programa

```text
MiniJarvis H1 es una primera versión muy sencilla de un asistente por consola. El programa empieza en el método main, muestra un saludo, pide el nombre del usuario con Scanner, guarda ese nombre en una variable y muestra varios mensajes. Usa constantes para el nombre del asistente y el año del curso. Todavía no tiene menú, bucles, memoria ni IA real porque eso se trabajará en hitos posteriores.
```

---

## 3. Línea o fragmento que sé explicar

```java
final String ASSISTANT_NAME = "MiniJarvis";
final int COURSE_YEAR = 2026;
```

Explicación con mis palabras:

```text
Estas dos líneas crean constantes. ASSISTANT_NAME guarda el nombre del asistente y COURSE_YEAR guarda el año del curso. Uso final porque esos valores no deberían cambiar mientras se ejecuta el programa.
```

---

## 4. Preguntas esenciales

### ¿Dónde empieza el programa?

```text
Empieza en public static void main(String[] args).
```

### ¿Qué hace `public static void main(String[] args)`?

```text
Es el método principal. Java empieza a ejecutar el programa desde ahí.
```

### ¿Qué variable guarda el nombre de la persona usuaria?

```text
La variable String userName.
```

### ¿Qué constante has usado?

```text
ASSISTANT_NAME y COURSE_YEAR.
```

### ¿Qué hace `Scanner`?

```text
Permite leer datos que escribe la persona usuaria por teclado.
```

### ¿Qué hace `nextLine()`?

```text
Lee una línea completa de texto introducida por teclado.
```

### ¿Qué diferencia hay entre `print` y `println`?

```text
print escribe sin saltar de línea. println escribe y después salta a la siguiente línea.
```

### ¿Cómo ejecutas el proyecto en IntelliJ?

```text
Abro el proyecto, abro src/Main.java y pulso Run.
```

### ¿Por qué todavía no hay menú?

```text
Porque el menú necesita decisiones y bucles, que pertenecen a H2. En H1 el objetivo es comprender la base.
```

---

## 5. Si he usado IA

¿Qué parte fue asistida por IA?

```text
La explicación de qué significa final en Java.
```

¿Qué modifiqué yo?

```text
Escribí mis propios mensajes y mantuve el programa en el nivel H1, sin menú ni funciones avanzadas.
```

¿Cómo comprobé que funcionaba?

```text
Ejecuté el programa y comprobé que la salida coincidía con lo esperado.
```

---

## 6. Si el profesor/a cambia algo

¿Qué crees que podrías modificar en directo?

```text
Podría cambiar el nombre del asistente, cambiar el año del curso, modificar el mensaje de bienvenida o explicar qué pasaría si quito Scanner.
```

---

## 7. Autoevaluación rápida

```text
[x] Puedo explicar qué hace el programa.
[x] Puedo explicar qué hace main.
[x] Puedo explicar variable y constante.
[x] Puedo explicar Scanner a nivel básico.
[x] Puedo ejecutar el proyecto.
[x] Puedo justificar por qué H1 es una versión simple.
```
