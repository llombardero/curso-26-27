# Guía docente completa — H1 sesión a sesión

## Primer asistente básico — MiniJarvis H1

## Programación + Entornos de Desarrollo — 1.º DAW — Curso 2026/2027

Versión: cierre curricular 1.0 — julio 2026

Documento autónomo para uso del profesorado.

Este documento permite impartir H1 completo sin abrir ningún otro material.

---

## 1. Propósito de H1

H1 es el primer hito técnico del proyecto MiniJarvis.

Producto final:

```text
MiniJarvis H1: programa Java básico que pide el nombre de la persona usuaria y muestra varios mensajes iniciales.
```

H1 busca base sólida, no complejidad.

El alumnado debe comprender y defender:

```text
- clase Main;
- método main;
- salida por pantalla;
- variables;
- constantes;
- entrada con Scanner;
- ejecución en IntelliJ;
- README básico;
- evidencia de ejecución;
- defensa oral sencilla.
```

---

## 2. Restricciones de H1

En H1 todavía NO entra:

```text
[ ] Menú.
[ ] Bucles.
[ ] switch.
[ ] Listas o mapas.
[ ] Memoria.
[ ] Clases propias adicionales.
[ ] Ficheros.
[ ] Excepciones complejas.
[ ] Conexión con IA real.
[ ] Patrones de diseño.
```

Frase docente:

```text
Si H1 es pequeño, claro y defendible, H1 está bien.
```

---

## 3. Secuencia de sesiones H1

Propuesta de 7 sesiones de 45 minutos.

| Sesión | Foco | Producto parcial |
|---|---|---|
| H1-S1 | Presentar H1 y analizar salida esperada | Idea clara del producto mínimo. |
| H1-S2 | Crear proyecto en IntelliJ y clase Main | Proyecto ejecutable con primer mensaje. |
| H1-S3 | Variables, constantes y salida | Mensajes con datos fijos y variables. |
| H1-S4 | Entrada con Scanner | Nombre leído por teclado. |
| H1-S5 | Código completo, limpieza y ejecución | MiniJarvis H1 funcional. |
| H1-S6 | README y evidencias | Documentación mínima. |
| H1-S7 | Revisión, defensa y recuperación | Validación individual. |

---

# H1-S1 — Presentar H1 y analizar salida esperada

## Duración

```text
45 minutos
```

## Objetivo

Que el alumnado entienda qué va a construir en H1 y qué no debe intentar construir todavía.

## Resultado esperado

Cada alumno/a debe salir con:

```text
- una salida propuesta para su MiniJarvis H1;
- una lista clara de lo que entra y no entra;
- dudas iniciales identificadas.
```

## Guion docente

```text
En la sesión anterior vivimos cómo se trabaja por sprint con la torre de papel.

Ahora empezamos el primer hito técnico: H1.

H1 será una versión muy pequeña de MiniJarvis. No tendrá menú, memoria ni IA real. Será un primer programa Java por consola.
```

## Pizarra

```text
Hola, soy MiniJarvis.
¿Cómo te llamas? Laura
Encantada, Laura.
Este curso vamos a crear un pequeño agente IA.
Curso de inicio: 2026.
Primer objetivo: aprender la estructura básica de un programa Java.
```

## Preguntas guiadas

```text
¿Qué partes son texto fijo?
¿Qué parte cambia según la persona usuaria?
¿Qué debería poder explicar quien entregue este programa?
```

## Actividad HEXA guiada

Diseñar la salida de MiniJarvis H1.

| Parte | Texto propuesto |
|---|---|
| Saludo inicial | |
| Pregunta al usuario | |
| Respuesta usando el nombre | |
| Mensaje del curso | |
| Objetivo H1 | |

## Cierre

Ticket de salida:

```text
1. Una cosa que sí entra en H1.
2. Una cosa que no entra en H1.
3. Una duda antes de programar.
```

## Tú explicas

```text
- producto esperado;
- límites de H1;
- texto fijo frente a dato variable;
- evidencia defendible.
```

## El alumnado decide/investiga

```text
- mensajes del asistente;
- dudas iniciales;
- cómo comprobaría que la salida es correcta.
```

---

# H1-S2 — Crear proyecto en IntelliJ y clase Main

## Duración

```text
45 minutos
```

## Objetivo

Crear un proyecto Java mínimo y ejecutar el primer mensaje.

## Resultado esperado

```text
- proyecto Java abierto;
- clase Main creada;
- método main reconocido;
- primer println ejecutado.
```

## Guion docente

```text
Hoy no vamos a escribir mucho código. Vamos a conseguir algo esencial: que el proyecto exista y se ejecute.
```

## Código docente mínimo

```java
public class Main {
    public static void main(String[] args) {
        System.out.println("Hola, soy MiniJarvis.");
    }
}
```

## Qué explicas tú

```text
public class Main: define una clase llamada Main.
main: punto de entrada del programa.
System.out.println: muestra texto por pantalla.
Las llaves agrupan el código.
El punto y coma cierra la instrucción.
```

## Práctica guiada

```text
1. Crear o abrir un proyecto Java.
2. Crear una clase Main.
3. Escribir el código mínimo.
4. Cambiar el mensaje por uno propio.
5. Ejecutar.
6. Copiar la salida en el cuaderno.
```

## Errores frecuentes

| Error | Intervención |
|---|---|
| Falta punto y coma | Revisar final de línea. |
| Llaves mal cerradas | Contar `{` y `}`. |
| Comillas mal cerradas | Revisar texto entre comillas. |
| No encuentra Main | Revisar nombre de clase y archivo. |

## Cierre

Pregunta rápida:

```text
¿Dónde empieza a ejecutarse el programa?
```

Respuesta esperada:

```text
en main
```

---

# H1-S3 — Variables, constantes y salida por pantalla

## Duración

```text
45 minutos
```

## Objetivo

Introducir variables y constantes de forma aplicada al asistente.

## Resultado esperado

El programa debe usar:

```text
- una constante para el nombre del asistente;
- una constante para el curso;
- varios mensajes por pantalla.
```

## Guion docente

```text
Si un dato no cambia, podemos guardarlo como constante. Si un dato puede cambiar, lo guardaremos como variable.
```

## Código de referencia

```java
public class Main {
    public static void main(String[] args) {
        final String ASSISTANT_NAME = "MiniJarvis";
        final int COURSE_YEAR = 2026;

        System.out.println("Hola, soy " + ASSISTANT_NAME + ".");
        System.out.println("Curso de inicio: " + COURSE_YEAR + ".");
    }
}
```

## Qué explicas tú

```text
String: texto.
int: número entero.
final: indica constante.
ASSISTANT_NAME: nombre claro de constante.
+: une textos y valores.
```

## Actividad

El alumnado añade:

```text
- constante ASSISTANT_NAME;
- constante COURSE_YEAR;
- tres mensajes propios;
- nombres claros.
```

## Investigación HEXA guiada

Pregunta:

```text
¿Qué nombre de constante es más claro y por qué?
```

Opciones:

```text
A. x
B. nombre
C. ASSISTANT_NAME
```

Producto:

```text
Una frase justificando el nombre elegido.
```

## Cierre

Ticket:

```text
1. ¿Qué diferencia hay entre variable y constante?
2. ¿Qué significa final?
```

---

# H1-S4 — Entrada con Scanner

## Duración

```text
45 minutos
```

## Objetivo

Leer el nombre del usuario por teclado y usarlo en un mensaje.

## Resultado esperado

El programa debe:

```text
- importar Scanner;
- crear un Scanner;
- preguntar el nombre;
- leer con nextLine;
- usar el nombre en una respuesta;
- cerrar el Scanner.
```

## Guion docente

```text
Hasta ahora el programa solo hablaba. Hoy vamos a hacer que escuche una respuesta del usuario.
```

## Código de referencia

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        final String ASSISTANT_NAME = "MiniJarvis";
        Scanner scanner = new Scanner(System.in);

        System.out.println("Hola, soy " + ASSISTANT_NAME + ".");
        System.out.print("¿Cómo te llamas? ");
        String userName = scanner.nextLine();
        System.out.println("Encantada, " + userName + ".");

        scanner.close();
    }
}
```

## Qué explicas tú

```text
import java.util.Scanner: permite usar Scanner.
new Scanner(System.in): prepara lectura desde teclado.
nextLine(): lee una línea de texto.
String userName: guarda el nombre.
print no salta de línea; println sí.
```

## Práctica guiada

```text
1. Añadir import.
2. Crear scanner.
3. Preguntar nombre con print.
4. Leer userName.
5. Mostrar mensaje usando userName.
6. Ejecutar dos veces con nombres distintos.
```

## Errores frecuentes

| Error | Intervención |
|---|---|
| No importa Scanner | Añadir import arriba. |
| Usa `println` para preguntar | No es grave; explicar diferencia con `print`. |
| Variable mal escrita | Revisar mayúsculas/minúsculas. |
| Cierra Scanner antes de leer | Mover `scanner.close()` al final. |

## Cierre

Pregunta:

```text
¿Qué línea guarda realmente el nombre escrito por el usuario?
```

Respuesta esperada:

```java
String userName = scanner.nextLine();
```

---

# H1-S5 — Código completo, limpieza y ejecución

## Duración

```text
45 minutos
```

## Objetivo

Completar MiniJarvis H1 y revisar claridad del código.

## Resultado esperado

Un `Main.java` funcional, simple y defendible.

## Checklist técnico

```text
[ ] Tiene import Scanner.
[ ] Tiene public class Main.
[ ] Tiene main.
[ ] Tiene ASSISTANT_NAME.
[ ] Tiene COURSE_YEAR.
[ ] Crea Scanner.
[ ] Pide el nombre.
[ ] Usa userName.
[ ] Muestra varios mensajes.
[ ] Cierra scanner.
[ ] No tiene menú, bucles ni memoria.
```

## Guion docente

```text
Hoy vamos a terminar la versión H1. No añadiremos cosas nuevas grandes. Vamos a hacer que lo básico esté claro, limpio y ejecutable.
```

## Código objetivo orientativo

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        final String ASSISTANT_NAME = "MiniJarvis";
        final int COURSE_YEAR = 2026;

        Scanner scanner = new Scanner(System.in);

        System.out.println("Hola, soy " + ASSISTANT_NAME + ".");
        System.out.print("¿Cómo te llamas? ");
        String userName = scanner.nextLine();

        System.out.println("Encantada, " + userName + ".");
        System.out.println("Este curso vamos a crear un pequeño agente IA.");
        System.out.println("Curso de inicio: " + COURSE_YEAR + ".");
        System.out.println("Primer objetivo: aprender la estructura básica de un programa Java.");

        scanner.close();
    }
}
```

## Actividad

El alumnado debe:

```text
1. Completar el código.
2. Ejecutarlo con su nombre.
3. Ejecutarlo con otro nombre.
4. Comprobar que no hay funciones adelantadas.
5. Prepararse para explicar 3 líneas.
```

## Microdefensa por parejas

Por parejas, una persona pregunta:

```text
¿Qué hace esta línea?
```

La otra explica una línea del código.

Cambian roles.

## Cierre

Cada alumno/a marca:

```text
[ ] Mi programa se ejecuta.
[ ] Puedo explicar main.
[ ] Puedo explicar Scanner.
[ ] Puedo explicar una constante.
[ ] Puedo explicar userName.
```

---

# H1-S6 — README y evidencia de ejecución

## Duración

```text
45 minutos
```

## Objetivo

Documentar H1 de forma mínima y recoger evidencia de ejecución.

## Resultado esperado

```text
- README.md básico;
- evidencia de ejecución;
- si procede, portfolio H1 iniciado;
- registro IA si se ha usado.
```

## Guion docente

```text
Un programa que funciona pero no se puede ejecutar siguiendo instrucciones está incompleto.

Hoy vamos a documentar cómo se usa MiniJarvis H1.
```

## README mínimo

El alumnado crea:

```markdown
# H1 — Primer asistente por consola

## Qué hace

Este programa muestra un saludo, pide el nombre del usuario y muestra mensajes iniciales del proyecto MiniJarvis.

## Cómo ejecutar

Desde IntelliJ:

1. Abrir el proyecto.
2. Abrir `src/Main.java`.
3. Pulsar Run.
4. Escribir un nombre cuando el programa lo pida.

## Ejemplo de ejecución

```text
Hola, soy MiniJarvis.
¿Cómo te llamas? Laura
Encantada, Laura.
```

## Qué no incluye todavía

No incluye menú, bucles, memoria ni IA real.
```

## Evidencia de ejecución

Puede ser:

```text
- captura de pantalla;
- bloque de salida copiado;
- explicación escrita de entrada y salida.
```

Plantilla:

```text
Entrada usada: Laura
Resultado obtenido:
...
¿Funciona como esperaba? Sí / No
```

## IA

Si se usó IA:

```text
- para qué se usó;
- qué se aceptó;
- qué se modificó;
- cómo se verificó.
```

Si no se usó:

```text
No he usado IA en H1.
```

## Cierre

Pregunta:

```text
¿Podría otra persona ejecutar tu programa siguiendo tu README?
```

---

# H1-S7 — Revisión, defensa y recuperación

## Duración

```text
45 minutos
```

## Objetivo

Validar que la evidencia H1 es funcional y defendible.

## Resultado esperado

```text
- revisión del código;
- defensa individual breve;
- detección de recuperaciones;
- cierre de H1.
```

## Guion docente

```text
Hoy no se trata solo de entregar archivos. Se trata de comprobar que podéis explicar lo que habéis hecho.
```

## Checklist docente rápido

| Elemento | Sí | Parcial | No |
|---|---|---|---|
| Ejecuta | | | |
| Usa Main/main | | | |
| Usa constante | | | |
| Usa variable | | | |
| Usa Scanner | | | |
| README suficiente | | | |
| Evidencia de ejecución | | | |
| Puede defenderlo | | | |

## Preguntas de defensa

```text
1. ¿Dónde empieza el programa?
2. ¿Qué hace System.out.println?
3. ¿Qué diferencia hay entre print y println?
4. ¿Qué es ASSISTANT_NAME?
5. ¿Qué es userName?
6. ¿Qué hace scanner.nextLine()?
7. ¿Por qué H1 no tiene menú todavía?
8. ¿Cómo sabes que tu programa funciona?
```

## Recuperación inmediata

Si falla ejecución:

```text
Prioridad 1: que compile y ejecute.
```

Si falla defensa:

```text
Prioridad 2: explicar 5 líneas esenciales.
```

Si falla README:

```text
Prioridad 3: completar instrucciones y ejemplo.
```

## Cierre del hito

Mensaje:

```text
H1 nos da la primera versión técnica. Aún es muy sencilla, pero ya tenemos algo que se ejecuta, se documenta y se defiende.

En H2 añadiremos menú, decisiones, bucles, pruebas y depuración.
```

---

## 4. Evaluación formativa de H1

No uses H1 solo para poner nota.

Úsalo para detectar:

```text
- quién entiende estructura básica;
- quién copia sin comprender;
- quién necesita apoyo con IntelliJ;
- quién documenta bien;
- quién se adelanta demasiado;
- quién puede ayudar a otros.
```

---

## 5. Atención a la diversidad

### Si un alumno se bloquea con IntelliJ

Reduce objetivo:

```text
Conseguir que ejecute un println.
```

### Si un alumno avanza demasiado

Recuérdale:

```text
Tu reto no es añadir más cosas. Tu reto es explicar perfectamente lo básico.
```

### Si un alumno usa IA para todo

Pregunta:

```text
Explícame esta línea sin mirar la IA.
```

### Si un alumno tiene miedo a programar

Refuerza:

```text
H1 es pequeño a propósito. Solo necesitamos una primera versión.
```

---

## 6. Criterio de éxito de H1

H1 está consolidado si:

```text
[x] El programa ejecuta.
[x] Pide el nombre.
[x] Usa variable.
[x] Usa constante.
[x] Usa Scanner.
[x] Tiene README mínimo.
[x] Hay evidencia de ejecución.
[x] El alumno puede defender las líneas principales.
[x] No se han añadido funciones prematuras.
```

---

## 7. Conexión con H2

Al cerrar H1, deja preparada la siguiente idea:

```text
Ahora MiniJarvis habla una vez y termina.

En H2 aprenderemos a hacer que siga funcionando con un menú hasta que el usuario escriba salir.
```

Pregunta final:

```text
¿Qué tendría que cambiar en el código para que el programa no termine después del primer mensaje?
```

Respuesta esperada:

```text
Necesitaremos un bucle.
```

<!-- AJUSTE-COBERTURA-CONCEPTOS-32 -->

## Ajuste curricular — cobertura de conceptos de Programación

Este hito queda alineado con el mapa `32-lista-conceptos-programacion-por-tema.md`.

```text
Hito: H1
Temas de referencia: Tema 1
Foco: primer programa Java por consola y asistente mínimo
```

Conceptos que deben trabajarse o, como mínimo, quedar conectados con evidencias del alumnado:

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

Criterio docente de cierre:

- El alumnado no solo entrega el producto; debe poder señalar dónde aparece cada concepto en su código, README, pruebas o defensa.
- Si un concepto se marca como ampliación, no penaliza al alumnado que alcance el mínimo, pero sí orienta mejora, recuperación o enriquecimiento.
- La defensa debe incluir al menos una pregunta de comprensión sobre los conceptos nuevos del hito.

