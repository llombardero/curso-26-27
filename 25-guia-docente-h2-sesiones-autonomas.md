# Guía docente completa — H2 sesión a sesión

## Agente con decisiones y depuración — MiniJarvis H2

## Programación + Entornos de Desarrollo — 1.º DAW — Curso 2026/2027

Versión: borrador 0.1

Documento autónomo para uso del profesorado.

Este documento permite impartir H2 completo sin abrir ningún otro material.

---

## 1. Propósito de H2

H2 transforma MiniJarvis H1 en un agente con menú de comandos.

Producto final:

```text
MiniJarvis H2: agente por consola con menú, comandos básicos, repetición hasta salir, gestión de comando desconocido, pruebas manuales y evidencia de depuración.
```

H2 introduce:

```text
- while;
- boolean;
- if/else o switch;
- equals para comparar String;
- trim y toLowerCase si se decide normalizar entrada;
- comando desconocido;
- pruebas manuales;
- depuración con breakpoint;
- comparación Java ↔ Python;
- defensa técnica corta.
```

---

## 2. Restricciones de H2

En H2 sí entra:

```text
[x] Menú.
[x] Bucle hasta escribir salir.
[x] if/else o switch.
[x] Comandos ayuda, saluda, estado y salir.
[x] Comando desconocido.
[x] Pruebas manuales.
[x] Depuración con breakpoint.
```

En H2 todavía NO entra:

```text
[ ] Memoria con listas o mapas.
[ ] Ficheros.
[ ] Varias clases propias obligatorias.
[ ] Interfaces.
[ ] Patrones de diseño.
[ ] Conexión con IA real.
[ ] Base de conocimiento.
```

Frase docente:

```text
H2 trata de controlar el flujo del programa. La memoria, las clases y la IA vendrán después.
```

---

## 3. Secuencia de sesiones H2

Propuesta de 9 sesiones de 45 minutos.

| Sesión | Foco | Producto parcial |
|---|---|---|
| H2-S1 | Presentar H2 y diseñar comandos | Tabla de comandos y respuestas. |
| H2-S2 | while y salida controlada | Programa que repite prompt. |
| H2-S3 | if/else y equals | Comandos básicos reconocidos. |
| H2-S4 | comando desconocido y normalización | Entrada robusta básica. |
| H2-S5 | integración del menú completo | MiniJarvis H2 funcional. |
| H2-S6 | pruebas manuales | `docs/pruebas-h2.md`. |
| H2-S7 | depuración con breakpoint | `docs/depuracion-h2.md`. |
| H2-S8 | comparación Java ↔ Python y documentación | Comparación + README/registro IA. |
| H2-S9 | defensa, revisión y recuperación | H2 validado. |

---

# H2-S1 — Presentar H2 y diseñar comandos

## Duración

```text
45 minutos
```

## Objetivo

Que el alumnado entienda qué añade H2 respecto a H1 y diseñe el menú antes de programar.

## Resultado esperado

Cada equipo/alumno debe tener una tabla de comandos:

```text
ayuda
saluda
estado
salir
comando desconocido
```

## Guion docente

```text
En H1 MiniJarvis empezaba, saludaba y terminaba.

En H2 MiniJarvis tendrá un menú. El programa seguirá funcionando hasta que el usuario escriba salir.

Antes de programar, vamos a decidir qué comandos existen y qué debe responder cada uno.
```

## Pizarra

```text
H1 = secuencia lineal
H2 = menú + repetición + decisiones + pruebas + depuración
```

## Actividad HEXA guiada

Completar la tabla:

| Comando | Qué debe hacer | Cómo lo pruebo |
|---|---|---|
| ayuda | | |
| saluda | | |
| estado | | |
| salir | | |
| otro | | |

## Qué explicas tú

```text
- diferencia entre programa lineal y programa interactivo;
- concepto de comando;
- salida controlada;
- necesidad de probar cada comando.
```

## Qué decide/investiga el alumnado

```text
- texto exacto de cada respuesta;
- cómo comprobar que cada comando funciona;
- qué debería pasar con un comando desconocido.
```

## Cierre

Pregunta:

```text
¿Por qué diseñamos comandos antes de programar?
```

Respuesta esperada:

```text
Porque si sabemos qué debe pasar, podremos programarlo y probarlo mejor.
```

---

# H2-S2 — while y salida controlada

## Duración

```text
45 minutos
```

## Objetivo

Introducir el bucle `while` y la variable booleana `running`.

## Resultado esperado

Programa que repite un prompt hasta poder controlar la salida.

## Guion docente

```text
Para que MiniJarvis no termine después del primer mensaje, necesitamos repetir una parte del programa.

En Java podemos hacerlo con while.
```

## Código base

```java
boolean running = true;

while (running) {
    System.out.print("> ");
    String command = scanner.nextLine();
    System.out.println("Has escrito: " + command);
}
```

## Qué explicas tú

```text
boolean: valor true o false.
running: variable que controla si el programa sigue.
while: repite mientras la condición sea true.
El peligro de un bucle infinito.
```

## Práctica guiada

```text
1. Recuperar código H1.
2. Añadir boolean running = true.
3. Añadir while.
4. Leer command dentro del while.
5. Mostrar temporalmente lo escrito.
```

## Advertencia importante

Este código todavía no sabe salir. Puedes usarlo unos minutos y luego parar desde el IDE si hace falta.

Explica:

```text
Un bucle sin salida es un problema. En la siguiente sesión añadiremos el comando salir.
```

## Cierre

Ticket:

```text
1. ¿Qué hace while?
2. ¿Qué variable controla el bucle?
3. ¿Por qué necesitamos una salida?
```

---

# H2-S3 — if/else, equals y comando salir

## Duración

```text
45 minutos
```

## Objetivo

Reconocer comandos básicos y permitir salir del programa.

## Resultado esperado

MiniJarvis reconoce al menos `ayuda` y `salir`.

## Guion docente

```text
Ya tenemos repetición. Ahora necesitamos decisiones.

Si el usuario escribe ayuda, hacemos una cosa.
Si escribe salir, terminamos.
Si escribe otra cosa, más adelante mostraremos comando desconocido.
```

## Código base

```java
if (command.equals("ayuda")) {
    System.out.println("Comandos: ayuda, saluda, estado, salir");
} else if (command.equals("salir")) {
    System.out.println("Hasta pronto.");
    running = false;
}
```

## Qué explicas tú

```text
if: si ocurre esto.
else if: si no, pero ocurre esto otro.
equals: forma correcta de comparar texto en Java.
== no debe usarse para comparar contenido de String.
running = false: provoca que el while termine.
```

## Práctica guiada

```text
1. Añadir if para ayuda.
2. Añadir else if para salir.
3. Probar ayuda.
4. Probar salir.
5. Ejecutar varias veces.
```

## Error frecuente

| Error | Intervención |
|---|---|
| Usa `==` | Explicar que para String usamos `.equals`. |
| `salir` no termina | Revisar `running = false`. |
| El if está fuera del while | Debe decidir en cada vuelta. |

## Cierre

Pregunta:

```text
¿Qué línea hace que el programa deje de repetirse?
```

Respuesta esperada:

```java
running = false;
```

---

# H2-S4 — comando desconocido y normalización

## Duración

```text
45 minutos
```

## Objetivo

Gestionar entradas no válidas y mejorar la lectura de comandos.

## Resultado esperado

MiniJarvis responde de forma controlada si el comando no existe.

## Guion docente

```text
Un programa no debe quedarse sin respuesta cuando el usuario escribe algo inesperado.

Hoy añadiremos una respuesta para comando desconocido y haremos que AYUDA y ayuda se traten igual.
```

## Código base

```java
String command = scanner.nextLine().trim().toLowerCase();

if (command.equals("ayuda")) {
    System.out.println("Comandos: ayuda, saluda, estado, salir");
} else if (command.equals("salir")) {
    running = false;
} else {
    System.out.println("No entiendo ese comando. Escribe ayuda.");
}
```

## Qué explicas tú

```text
trim: quita espacios al principio y al final.
toLowerCase: convierte a minúsculas.
else final: cubre cualquier comando no reconocido.
```

## Pruebas rápidas

El alumnado prueba:

```text
ayuda
AYUDA
 ayuda 
inventa
salir
```

## Investigación HEXA guiada

Pregunta:

```text
¿Qué entradas raras podría escribir una persona usuaria?
```

Producto:

```text
Lista de 3 entradas raras y qué debería pasar.
```

## Cierre

Ticket:

```text
1. ¿Para qué sirve trim?
2. ¿Para qué sirve toLowerCase?
3. ¿Qué hace el else final?
```

---

# H2-S5 — Integración del menú completo

## Duración

```text
45 minutos
```

## Objetivo

Completar los comandos mínimos de H2.

## Resultado esperado

MiniJarvis H2 funcional con:

```text
ayuda
saluda
estado
salir
comando desconocido
```

## Código objetivo orientativo

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        final String ASSISTANT_NAME = "MiniJarvis";
        Scanner scanner = new Scanner(System.in);

        System.out.println("Hola, soy " + ASSISTANT_NAME + ".");
        System.out.print("¿Cómo te llamas? ");
        String userName = scanner.nextLine();
        System.out.println("Escribe ayuda para ver los comandos disponibles.");

        boolean running = true;

        while (running) {
            System.out.print("> ");
            String command = scanner.nextLine().trim().toLowerCase();

            if (command.equals("ayuda")) {
                System.out.println("Comandos disponibles: ayuda, saluda, estado, salir");
            } else if (command.equals("saluda")) {
                System.out.println("Hola, " + userName + ". Soy " + ASSISTANT_NAME + ".");
            } else if (command.equals("estado")) {
                System.out.println("Estoy funcionando en modo H2, sin memoria todavía.");
            } else if (command.equals("salir")) {
                System.out.println("Hasta pronto, " + userName + ".");
                running = false;
            } else {
                System.out.println("No entiendo ese comando. Escribe ayuda.");
            }
        }

        scanner.close();
    }
}
```

## Actividad

El alumnado:

```text
1. Integra comandos.
2. Ejecuta una secuencia completa.
3. Comprueba que salir termina.
4. Comprueba comando desconocido.
5. Revisa que no ha añadido memoria ni ficheros.
```

## Microdefensa por parejas

Una persona pregunta:

```text
¿Qué pasa si command vale estado?
¿Qué pasa si command vale salir?
¿Qué pasa si command vale xyz?
```

La otra responde señalando el código.

## Cierre

Checklist:

```text
[ ] ayuda funciona.
[ ] saluda funciona.
[ ] estado funciona.
[ ] salir termina.
[ ] comando desconocido responde.
```

---

# H2-S6 — Pruebas manuales

## Duración

```text
45 minutos
```

## Objetivo

Documentar pruebas manuales con resultado esperado y obtenido.

## Resultado esperado

Documento `docs/pruebas-h2.md` o equivalente.

## Guion docente

```text
Probar no es ejecutar una vez y decir “funciona”.

Probar es definir casos, entrada, resultado esperado y resultado obtenido.
```

## Tabla mínima

| ID | Caso | Entrada | Resultado esperado | Resultado obtenido | Estado |
|---|---|---|---|---|---|
| P01 | Ayuda | ayuda | Lista comandos | | |
| P02 | Saludo | saluda | Saludo personalizado | | |
| P03 | Estado | estado | Estado H2 | | |
| P04 | Desconocido | inventa | Mensaje de error controlado | | |
| P05 | Salir | salir | Termina | | |

## Qué explicas tú

```text
Caso de prueba.
Entrada.
Resultado esperado.
Resultado obtenido.
Estado.
```

## Actividad

El alumnado ejecuta y completa la tabla.

Debe añadir al menos un caso límite:

```text
AYUDA
 ayuda 
entrada vacía
```

## Cierre

Pregunta:

```text
¿Qué prueba demostraría que salir funciona realmente?
```

---

# H2-S7 — Depuración con breakpoint

## Duración

```text
45 minutos
```

## Objetivo

Usar un breakpoint para observar variables durante la ejecución.

## Resultado esperado

Documento `docs/depuracion-h2.md` o evidencia equivalente.

## Guion docente

```text
Depurar no es adivinar. Depurar es parar el programa en un punto y observar qué valores tienen las variables.
```

## Breakpoint recomendado

Colocar breakpoint después de:

```java
String command = scanner.nextLine().trim().toLowerCase();
```

## Variables a observar

```text
command
running
userName
```

## Qué explicas tú

```text
breakpoint: punto donde se pausa el programa.
step over: avanzar una instrucción.
variable observada: dato que miro durante la ejecución.
```

## Actividad

El alumnado prueba:

```text
ayuda
salir
inventa
```

Y completa:

| Comando escrito | Valor de command | Rama ejecutada | Qué aprendí |
|---|---|---|---|
| ayuda | | | |
| salir | | | |
| inventa | | | |

## Cierre

Ticket:

```text
1. ¿Dónde pusiste el breakpoint?
2. ¿Qué variable observaste?
3. ¿Qué descubriste?
```

---

# H2-S8 — Comparación Java ↔ Python y documentación

## Duración

```text
45 minutos
```

## Objetivo

Comparar el menú en Java con una versión equivalente en Python y completar documentación.

## Resultado esperado

```text
- comparación Java ↔ Python;
- README H2 actualizado;
- registro IA si se usó;
- incidencia si apareció.
```

## Guion docente

```text
Comparar Java con Python no es copiar otro lenguaje. Es entender mejor la lógica común: entrada, bucle, decisión y salida.
```

## Comparación mínima

| Aspecto | Java | Python |
|---|---|---|
| Leer texto | `scanner.nextLine()` | `input()` |
| Bucle | `while (running)` | `while running:` |
| Decisión | `if / else if / else` | `if / elif / else` |
| Comparar texto | `.equals()` | `==` |
| Salir | `running = false` | `running = False` |

## Actividad

El alumnado completa una explicación:

```text
La lógica del menú es parecida porque...
La diferencia más importante es...
En Java debo recordar que para String uso...
```

## IA

Si se usa IA para comparar:

```text
- registrar prompt;
- verificar que no genera un programa demasiado avanzado;
- explicar qué se acepta y qué se descarta.
```

## Cierre

Pregunta:

```text
¿Qué parte de la lógica es igual aunque cambie el lenguaje?
```

---

# H2-S9 — Defensa, revisión y recuperación

## Duración

```text
45 minutos
```

## Objetivo

Validar H2 como evidencia técnica y defendible.

## Resultado esperado

```text
- código H2 revisado;
- pruebas documentadas;
- depuración documentada;
- defensa individual breve;
- recuperación si procede.
```

## Checklist docente

| Elemento | Sí | Parcial | No |
|---|---|---|---|
| Ejecuta | | | |
| Menú se repite | | | |
| ayuda | | | |
| saluda | | | |
| estado | | | |
| salir | | | |
| comando desconocido | | | |
| pruebas manuales | | | |
| depuración | | | |
| comparación Java/Python | | | |
| defensa | | | |

## Preguntas de defensa

```text
1. ¿Cómo se repite el menú?
2. ¿Qué variable controla la salida?
3. ¿Qué hace running?
4. ¿Por qué usamos equals?
5. ¿Qué hace trim?
6. ¿Qué hace toLowerCase?
7. ¿Qué pasa con un comando desconocido?
8. ¿Dónde pusiste el breakpoint?
9. ¿Qué variable observaste?
10. ¿Qué prueba demuestra que salir funciona?
```

## Recuperación inmediata

Si falla el menú:

```text
Revisar while + running.
```

Si falla la comparación de texto:

```text
Revisar equals.
```

Si falla depuración:

```text
Repetir breakpoint con command.
```

Si falla defensa:

```text
Explicar línea por línea el while y un if.
```

## Cierre del hito

Guion:

```text
H2 es importante porque MiniJarvis deja de ser una secuencia lineal y empieza a comportarse como un pequeño agente con comandos.

En H3 añadiremos memoria temporal con colecciones.
```

---

## 4. Evaluación formativa de H2

H2 debe servir para detectar:

```text
- quién entiende bucles;
- quién entiende decisiones;
- quién compara String correctamente;
- quién prueba de forma ordenada;
- quién depura sin adivinar;
- quién puede defender el flujo del programa.
```

---

## 5. Atención a la diversidad

### Si el alumnado se bloquea con while

Usar dibujo:

```text
inicio → leer comando → decidir → volver al inicio → salir
```

### Si se adelanta a memoria

Reencuadre:

```text
Eso será H3. Ahora solo queremos control de flujo.
```

### Si usa IA para crear todo el menú

Pedir defensa:

```text
Explícame qué ocurre cuando command vale salir.
```

### Si se frustra con depuración

Reducir objetivo:

```text
Solo observa command con ayuda y salir.
```

---

## 6. Criterio de éxito de H2

H2 está consolidado si:

```text
[x] El programa ejecuta.
[x] El menú se repite.
[x] salir termina.
[x] Hay ayuda, saluda y estado.
[x] Hay comando desconocido.
[x] Hay pruebas manuales.
[x] Hay breakpoint documentado.
[x] El alumno puede defender while, running, equals y una prueba.
[x] No hay memoria ni complejidad prematura.
```

---

## 7. Conexión con H3

Pregunta final:

```text
Ahora MiniJarvis responde a comandos, pero cuando cerramos el programa olvida todo. ¿Qué tendría que cambiar para que recuerde cosas mientras está abierto?
```

Respuesta esperada:

```text
Necesitará memoria temporal, probablemente una colección.
```
