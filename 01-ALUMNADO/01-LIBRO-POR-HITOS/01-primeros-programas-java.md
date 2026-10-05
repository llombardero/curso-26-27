# Capítulo 01 — Primeros programas en Java

## Correspondencia

```text
Tema 1 — Aspectos básicos de la programación
RA1
H1 — Primer asistente por consola
```

Este capítulo prepara las primeras sesiones técnicas de H1: crear y ejecutar el proyecto, reconocer la estructura mínima de un programa Java y producir las primeras salidas por consola.

## 1. Qué vas a aprender

Al terminar este capítulo podrás:

- explicar qué significa programar mediante una secuencia de instrucciones;
- reconocer los elementos básicos de un programa Java sencillo;
- localizar la clase `Main` y el método `main`;
- identificar dónde comienza la ejecución;
- distinguir código fuente, compilación y ejecución;
- escribir y modificar mensajes sencillos por consola;
- reconocer algunos elementos básicos de la sintaxis de Java;
- interpretar errores iniciales de compilación y realizar una corrección pequeña;
- utilizar el entorno de trabajo para editar, ejecutar y comprobar un programa;
- explicar qué puede hacer MiniJarvis en H1 y qué capacidades todavía no forman parte de esta versión.

## 2. Dónde encaja

H0 ha servido para preparar la forma de trabajar.

Ahora empieza la construcción técnica de MiniJarvis.

En H1 no vamos a crear todavía un agente avanzado. El primer objetivo es mucho más pequeño:

```text
crear
  ↓
ejecutar
  ↓
observar
  ↓
modificar
  ↓
volver a ejecutar
  ↓
explicar
```

Antes de añadir decisiones, memoria, clases, herramientas o una IA real necesitamos dominar este recorrido.

Una versión pequeña que entiendes por completo es más útil para aprender que una versión compleja que no puedes explicar.

## 3. Conceptos fundamentales

### 3.1. ¿Qué es un programa?

En este nivel podemos pensar en un programa como un conjunto ordenado de instrucciones que el ordenador ejecutará.

Por ejemplo:

```java
System.out.println("Hola.");
System.out.println("Soy MiniJarvis.");
System.out.println("Este es mi primer paso.");
```

Las instrucciones se ejecutan en el orden en que aparecen.

Antes de ejecutar el ejemplo, intenta predecir:

```text
¿Qué línea aparecerá primero?
¿Qué línea aparecerá después?
¿Qué cambiaría si intercambiamos dos instrucciones?
```

Modificar el orden es una forma sencilla de comprobar que el programa sigue una secuencia.

### 3.2. El archivo fuente

El código que escribimos se guarda en un archivo con extensión `.java`.

En nuestro primer programa utilizaremos:

```text
Main.java
```

Si declaramos una clase pública llamada `Main`, el nombre del archivo debe corresponder con el de la clase.

### 3.3. La clase `Main`

Observa:

```java
public class Main {

}
```

En esta primera etapa no necesitas dominar todavía todos los conceptos de programación orientada a objetos que hay detrás de una clase.

Sí debes reconocer:

- dónde empieza la clase;
- dónde termina;
- su nombre;
- qué código queda dentro de sus llaves.

Las clases y los objetos se estudiarán con mayor profundidad cuando corresponda.

### 3.4. El método `main`

Nuestro programa necesita un punto por el que comenzar.

```java
public static void main(String[] args) {

}
```

Cuando ejecutes este programa, debes poder señalar en el código dónde comienza su ejecución.

Por ahora no necesitas memorizar por separado el significado completo de `public`, `static`, `void` y `String[] args`.

Sí necesitas reconocer correctamente la estructura y poder escribirla y utilizarla.

Más adelante entenderemos mejor los elementos que ahora aparecen juntos.

### 3.5. La estructura mínima

Juntando las dos piezas:

```java
public class Main {
    public static void main(String[] args) {

    }
}
```

Podemos verlo como cajas contenidas unas dentro de otras:

```text
clase Main
└── método main
    └── instrucciones
```

Las llaves `{` y `}` permiten reconocer esos bloques.

### 3.6. Una primera instrucción

Añadamos una salida por consola:

```java
public class Main {
    public static void main(String[] args) {
        System.out.println("Hola, soy MiniJarvis.");
    }
}
```

La instrucción:

```java
System.out.println("Hola, soy MiniJarvis.");
```

muestra un mensaje y después continúa con la siguiente instrucción.

No necesitas estudiar todavía todos los elementos de `System.out.println`. En este capítulo debes aprender a utilizarlo correctamente y reconocer qué texto se mostrará.

### 3.7. Algunos signos importan

Java tiene una sintaxis que debemos respetar.

En los primeros programas presta atención especialmente a:

- mayúsculas y minúsculas;
- llaves `{ }`;
- paréntesis `( )`;
- comillas `" "`;
- punto y coma `;`.

No significan lo mismo:

```text
Main
main
```

ni tampoco:

```text
System
system
```

Cuando Java detecta que el código no respeta su sintaxis, la compilación puede fallar.

### 3.8. Comentarios útiles

Un comentario permite escribir información para quien lee el código sin convertirla en una instrucción del programa.

Por ejemplo:

```java
// Presentación inicial de MiniJarvis
System.out.println("Hola, soy MiniJarvis.");
```

Un comentario debe ayudar a comprender algo.

Evita comentarios que solo repitan exactamente lo que ya se ve:

```java
// Imprime Hola
System.out.println("Hola");
```

A medida que mejoremos los nombres y la estructura del código, muchas líneas necesitarán poca explicación adicional.

## 4. Java paso a paso

### Paso 1. Programa mínimo

```java
public class Main {
    public static void main(String[] args) {
        System.out.println("MiniJarvis empieza.");
    }
}
```

Antes de ejecutarlo, comprueba:

- archivo `Main.java`;
- clase `Main`;
- método `main`;
- una instrucción;
- llaves equilibradas;
- punto y coma.

Después ejecútalo.

### Paso 2. Añadir instrucciones

```java
public class Main {
    public static void main(String[] args) {
        System.out.println("Hola.");
        System.out.println("Soy MiniJarvis.");
        System.out.println("Todavía estoy aprendiendo.");
    }
}
```

Predice la salida antes de ejecutar.

Después cambia el orden de dos instrucciones y vuelve a comprobarlo.

### Paso 3. Modificar sin ampliar el nivel

Cambia únicamente los textos:

```java
public class Main {
    public static void main(String[] args) {
        System.out.println("Bienvenido a MiniJarvis.");
        System.out.println("Esta es mi primera versión.");
        System.out.println("Por ahora solo puedo mostrar mensajes.");
    }
}
```

El programa ha cambiado, pero todavía utiliza los mismos conceptos.

Eso es importante: mejorar un producto no siempre significa añadir una técnica nueva.

### Paso 4. Provocar un error controlado

Observa esta línea:

```java
System.out.println("Hola, soy MiniJarvis.")
```

Compárala con:

```java
System.out.println("Hola, soy MiniJarvis.");
```

Antes de utilizar la ayuda del entorno, intenta localizar la diferencia.

Después corrige el programa y vuelve a ejecutarlo.

El objetivo no es coleccionar errores, sino aprender a:

```text
observar → localizar → corregir → volver a comprobar
```

## 5. Compilar y ejecutar

Escribir código y ejecutarlo no son la misma acción.

El recorrido básico es:

```text
Main.java
   ↓
compilación
   ↓
programa preparado para ejecutarse
   ↓
ejecución
   ↓
salida observable
```

Durante el curso utilizarás el entorno de desarrollo para editar y ejecutar el proyecto.

También puedes reconocer el proceso mediante los comandos:

```bash
javac src/Main.java
java -cp src Main
```

Lo importante no es memorizar comandos sin comprenderlos, sino distinguir las dos acciones:

**Compilar** comprueba y prepara el código.

**Ejecutar** pone en marcha el programa que ha podido compilarse.

Si modificas el código fuente, el programa debe volver a pasar por ese proceso para que el cambio llegue a la ejecución correspondiente.

## 6. Llévalo a MiniJarvis

Construye una primera presentación por consola.

La versión debe mantenerse deliberadamente pequeña.

Por ejemplo, puede mostrar:

1. un saludo;
2. el nombre MiniJarvis;
3. una frase que explique que está comenzando;
4. una capacidad que tendrá más adelante, sin implementarla todavía.

Un posible resultado observable sería:

```text
Hola.
Soy MiniJarvis.
Esta es mi primera versión.
Más adelante aprenderé a interactuar contigo.
```

No necesitas todavía:

- menú;
- bucles;
- memoria;
- varias clases propias;
- conexión a servicios externos;
- una IA real.

Esas capacidades llegarán cuando hayamos aprendido los conceptos necesarios.

## 7. Comprueba que funciona

No basta con afirmar «funciona».

Realiza estas comprobaciones sobre tu programa:

1. ejecútalo;
2. comprueba que aparecen todos los mensajes;
3. comprueba que aparecen en el orden previsto;
4. modifica uno de ellos;
5. vuelve a ejecutar;
6. verifica que aparece el nuevo resultado;
7. introduce voluntariamente un error sencillo;
8. localízalo, corrígelo y vuelve a ejecutar.

No necesitas hacer una captura rutinaria de cada ejecución.

La propia ejecución reproducible permite comprobar el comportamiento.

## 8. Errores frecuentes y depuración inicial

| Problema | Qué puedes observar | Qué revisar |
|---|---|---|
| El archivo y la clase no tienen el mismo nombre | El proyecto no compila correctamente | `Main.java` y `public class Main` |
| Falta un `;` | Aparece un error de compilación | Final de la instrucción |
| Falta una comilla | Java interpreta mal el texto siguiente | Inicio y final del mensaje |
| Falta una llave | La estructura del programa queda incompleta | Apertura y cierre de los bloques |
| Se cambia una mayúscula | Java no reconoce el nombre esperado | Escritura exacta del identificador |
| La salida no corresponde al último cambio | Ves una versión anterior o distinta de la esperada | Guardar, compilar y ejecutar de nuevo |
| Se cambian muchas cosas a la vez | Es difícil descubrir qué provocó el problema | Hacer cambios pequeños y probar |

Cuando encuentres un error, intenta evitar el impulso de cambiar varias líneas a la vez.

Una estrategia inicial útil es:

```text
¿Qué esperaba?
      ↓
¿Qué ha ocurrido?
      ↓
¿Qué línea puede explicarlo?
      ↓
Cambio una cosa
      ↓
Vuelvo a ejecutar
```

## 9. Practica y razona

### Actividad A — Predice

Sin ejecutar todavía:

```java
public class Main {
    public static void main(String[] args) {
        System.out.println("Uno");
        System.out.println("Dos");
        System.out.println("Tres");
    }
}
```

Predice la salida.

Después ejecútalo y compárala con tu predicción.

### Actividad B — Reordena

Haz que aparezca:

```text
MiniJarvis
empieza
ahora
```

utilizando tres instrucciones.

Después cambia únicamente el orden para obtener:

```text
Ahora
empieza
MiniJarvis
```

Explica qué has cambiado y qué se ha mantenido igual.

### Actividad C — Encuentra el error

Localiza los problemas antes de ejecutar:

```java
public class main {
    public static void main(String[] args) {
        System.out.println("Hola)
        System.out.println("Soy MiniJarvis");
    }
}
```

No pruebes cambios al azar.

Señala primero qué elementos de la sintaxis revisarías.

### Actividad D — Explica el código

Sobre tu propia versión, señala:

- el archivo fuente;
- la clase;
- el método por el que comienza la ejecución;
- las instrucciones;
- los bloques delimitados por llaves;
- los mensajes que llegarán a la consola.

## 10. Comprueba lo aprendido

Intenta responder sin copiar definiciones:

1. ¿Dónde comienza la ejecución de este programa?
2. ¿Qué diferencia hay entre `Main` y `main` en nuestro ejemplo?
3. ¿Qué función cumplen las llaves?
4. ¿Por qué importa el punto y coma?
5. ¿Qué diferencia hay entre escribir código, compilarlo y ejecutarlo?
6. ¿Qué ocurrirá si intercambias dos instrucciones `println`?
7. ¿Por qué conviene cambiar una sola cosa cuando estás buscando un error?
8. Señala en tu programa una instrucción y explica qué resultado observable produce.
9. ¿Qué capacidades tiene ya MiniJarvis?
10. ¿Qué capacidades hemos decidido no añadir todavía?

Para la microdefensa debes poder abrir tu programa, localizar estas partes y modificar un mensaje sin depender de una respuesta memorizada.

## 11. Si vas más rápido

Estas actividades amplían la práctica sin adelantar contenidos que todavía no corresponden:

- añade más mensajes manteniendo el programa simple;
- reorganiza los mensajes y predice la salida antes de ejecutarlos;
- introduce y corrige distintos errores de sintaxis de uno en uno;
- mejora comentarios poco útiles;
- compara dos versiones y explica exactamente qué ha cambiado;
- intenta reconstruir de memoria la estructura mínima y después compárala con una versión que funcione.

No avances todavía hacia menús, bucles o estructuras complejas solo por terminar antes.

## 12. Qué conservar

La evidencia técnica principal es el propio programa ejecutable.

Cuando corresponda al cierre de H1, el README explicará cómo ejecutar la versión del proyecto.

No necesitas:

- una captura rutinaria de la consola;
- un informe independiente de esta práctica;
- una ficha de errores;
- un portfolio de este capítulo.

Si durante el trabajo has tenido un aprendizaje individual especialmente relevante, puedes reflejarlo brevemente en tu diario.

Lo importante al terminar es que puedas ejecutar el programa, comprobar su resultado y explicar su estructura.
