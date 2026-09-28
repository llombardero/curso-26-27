# Vocabulario H1 — completado (Ana García)

> No es un entregable independiente. Úsalo para preparar la defensa o recuperar conceptos.

Para cada término, escribo una definición propia, un ejemplo mínimo y un error frecuente.

---

## JDK, JVM e IDE

- **Definición propia:**
  - **JDK (Java Development Kit):** El kit de desarrollo de Java. Incluye el compilador (`javac`), la máquina virtual (JVM) y herramientas para escribir y ejecutar programas Java.
  - **JVM (Java Virtual Machine):** La máquina virtual que ejecuta el código bytecode de Java. Hace que un programa Java pueda correr en cualquier sistema operativo sin modificarlo.
  - **IDE (Entorno de Desarrollo Integrado):** Un programa que ayuda a escribir código Java: IntelliJ IDEA, VS Code con extensión Java, o Eclipse. Incluye editor, compilador, depurador y otras herramientas.
- **Ejemplo mínimo:**
  ```bash
  javac Main.java    # JDK: compila
  java Main          # JVM: ejecuta
  # IntelliJ IDEA    # IDE: escribe y ejecuta
  ```
- **Error frecuente:** Creer que JDK y JVM son lo mismo. El JDK incluye la JVM, pero también el compilador y otras herramientas. La JVM solo ejecuta; el JDK crea y ejecuta.

---

## Clase y `main`

- **Definición propia:**
  - **Clase:** Un bloque de código que define un "molde" para crear objetos. Todo programa Java debe tener al menos una clase. Se declara con `class`.
  - **`main`:** El método que Java ejecuta automáticamente al arrancar el programa. Es el punto de entrada.
- **Ejemplo mínimo:**
  ```java
  public class Main {          // Clase
      public static void main(String[] argumentos) {  // Método main
          System.out.println("Arranca aquí");
      }
  }
  ```
- **Error frecuente:** Olvidar `public static void` antes de `main`. Sin eso, Java no reconoce el método como punto de entrada y no ejecuta el programa.

---

## Instrucción, bloque y comentario

- **Definición propia:**
  - **Instrucción:** Una orden que el programa ejecuta. En Java, cada instrucción termina con punto y coma (`;`).
  - **Bloque:** Un conjunto de instrucciones agrupadas entre llaves `{ }`. Se usa en `main`, `if`, `else`, `for`, etc.
  - **Comentario:** Texto que el compilador ignora. Sirve para documentar el código. Puede ser de una línea (`//`) o de varias (`/* ... */`).
- **Ejemplo mínimo:**
  ```java
  int x = 5;      // Instrucción
  {                // Inicio de bloque
      int y = 10;  // Otra instrucción dentro del bloque
  }                // Fin de bloque
  // Esto es un comentario
  ```
- **Error frecuente:** Olvidar el punto y coma (`;`) al final de una instrucción. El compilador da error de sintaxis.

---

## Tipo primitivo y `String`

- **Definición propia:**
  - **Tipo primitivo:** Un tipo de dato básico integrado en Java: `int` (enteros), `double` (decimales), `boolean` (verdadero/falso), `char` (un carácter).
  - **`String`:** Un tipo de dato para cadenas de texto. No es primitivo; es una clase. Se escribe con comillas dobles: `"Hola"`.
- **Ejemplo mínimo:**
  ```java
  int edad = 25;           // Primitivo
  double precio = 9.99;    // Primitivo
  boolean activo = true;   // Primitivo
  String nombre = "Ana";   // Clase (no primitivo)
  ```
- **Error frecuente:** Usar `=` para comparar valores en lugar de `==`. `=` asigna; `==` compara. También confundir `String` con primitivo: `String` es una clase, no un tipo primitivo.

---

## Declaración, inicialización y asignación

- **Definición propia:**
  - **Declaración:** Decirle al compilador que existe una variable con un tipo y un nombre: `int edad;`
  - **Inicialización:** Darle un valor la primera vez: `int edad = 25;`
  - **Asignación:** Cambiar el valor de una variable ya declarada: `edad = 30;`
- **Ejemplo mínimo:**
  ```java
  int edad;        // Declaración
  edad = 25;       // Inicialización (y primera asignación)
  edad = 30;       // Asignación (cambio de valor)
  ```
- **Error frecuente:** Usar una variable antes de inicializarla. `int edad; System.out.println(edad);` → error de compilación: "variable might not have been initialized".

---

## Variable, constante y literal

- **Definición propia:**
  - **Variable:** Un espacio en memoria con un nombre y un tipo cuyo valor puede cambiar: `int numero = 5; numero = 10;`
  - **Constante:** Una variable declarada con `final` cuyo valor no puede cambiar: `final int MAX = 100;`
  - **Literal:** Un valor escrito directamente en el código, sin nombre: `"Hola"`, `42`, `3.14`, `true`.
- **Ejemplo mínimo:**
  ```java
  int numero = 42;           // Variable: puede cambiar
  final int MAX = 100;       // Constante: no puede cambiar
  String saludo = "Hola";    // "Hola" es un literal
  ```
- **Error frecuente:** Intentar reasignar una constante: `MAX = 200;` → error de compilación: "cannot assign a value to final variable MAX".

---

## Operador aritmético, relacional y lógico

- **Definición propia:**
  - **Operador aritmético:** Realiza cálculos matemáticos: `+`, `-`, `*`, `/`, `%` (módulo/resto).
  - **Operador relacional:** Compara dos valores y devuelve `true` o `false`: `>`, `<`, `>=`, `<=`, `==`, `!=`.
  - **Operador lógico:** Combina expresiones booleanas: `&&` (y), `||` (o), `!` (no).
- **Ejemplo mínimo:**
  ```java
  int a = 10, b = 3;
  int suma = a + b;          // Aritmético: 13
  boolean mayor = a > b;     // Relacional: true
  boolean ambos = (a > 5) && (b < 5);  // Lógico: true && true = true
  ```
- **Error frecuente:** Usar `=` en lugar de `==` para comparar: `if (a = 10)` → error de compilación (intenta asignar, no comparar).

---

## Conversión y casting

- **Definición propia:**
  - **Conversión:** Cambiar un valor de un tipo a otro. Java hace conversiones automáticas cuando son seguras (ej: `int` a `double`).
  - **Casting:** Conversión explícita con paréntesis: `(double) 5` convierte el entero 5 al decimal 5.0.
  - **`Integer.parseInt()`:** Convierte una cadena a entero. Lanza excepción si la cadena no es un número.
- **Ejemplo mínimo:**
  ```java
  int entero = 5;
  double decimal = entero;           // Conversión automática: 5.0
  double explicito = (double) entero; // Casting explícito: 5.0
  int desdeString = Integer.parseInt("42"); // Conversión de String a int: 42
  ```
- **Error frecuente:** Casting inseguro: `int x = (int) 5.9;` → `x = 5` (se pierde la parte decimal). También: `Integer.parseInt("abc")` → `NumberFormatException`.

---

## Condición, `if/else` y `?:`

- **Definición propia:**
  - **Condición:** Una expresión que evalúa a `true` o `false`. Se usa en `if`, `while`, etc. Ejemplo: `numero > 0`.
  - **`if/else`:** Estructura que ejecuta un bloque si la condición es `true` y otro si es `false`.
  - **`?:` (operador ternario):** Versión corta de `if/else` en una línea: `condicion ? valorSiTrue : valorSiFalse`.
- **Ejemplo mínimo:**
  ```java
  int numero = 5;
  if (numero > 0) {
      System.out.println("Positivo");
  } else {
      System.out.println("No positivo");
  }
  // Equivalente con ?:
  String resultado = (numero > 0) ? "Positivo" : "No positivo";
  ```
- **Error frecuente:** Olvidar las llaves `{ }` en `if/else` cuando hay múltiples instrucciones. Solo la primera instrucción sin llaves pertenece al `if`; las demás se ejecutan siempre.

---

## Compilación, ejecución y error

- **Definición propia:**
  - **Compilación:** El proceso de convertir el código fuente (.java) en bytecode (.class). Lo hace `javac`. Si hay errores de sintaxis, la compilación falla.
  - **Ejecución:** El proceso de correr el bytecode. Lo hace `java`. Si hay errores lógicos o de datos, la ejecución falla (excepciones).
  - **Error de compilación:** Se detecta antes de ejecutar. Ejemplo: falta `;`, nombre de variable incorrecto.
  - **Error de ejecución:** Se detecta durante la ejecución. Ejemplo: división por cero, `NumberFormatException`, `NullPointerException`.
- **Ejemplo mínimo:**
  ```bash
  javac Main.java    # Compilación: si hay errores de sintaxis, falla aquí
  java Main          # Ejecución: si hay errores lógicos, falla aquí
  ```
- **Error frecuente:** Confundir errores de compilación con errores de ejecución. Los de compilación se arreglan antes de ejecutar; los de ejecución se detectan al correr el programa.
