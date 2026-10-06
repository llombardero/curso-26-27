# H1.3 — Estructura mínima de un programa Java

| Dato | Valor |
|---|---|
| Hito | H1 — Primer asistente ejecutable |
| Duración prevista | 45 minutos |
| Fase HEXA del hito | Investigar — aprender lo necesario |
| Modalidad de trabajo | **INDIVIDUAL → PAREJAS → comprobación INDIVIDUAL** |

> Basada en `00-GUION-DOCENTE-H1-COMPLETO.md`.

## Qué vas a aprender

Al terminar, cada persona debe poder reconstruir y explicar la estructura mínima de Java, reconocer el punto de entrada, predecir el orden de ejecución y depurar un error sintáctico sencillo mediante una hipótesis. También debe razonar sobre identificadores y distinguir un comentario útil de otro redundante.

## Antes de entrar en clase

- [ ] Abrir y ejecutar el proyecto que utilizará el alumnado.
- [ ] Preparar los fragmentos con errores sin corregirlos en la proyección.
- [ ] Comprobar que el entorno muestra diagnósticos de compilación con claridad.
- [ ] Reservar los últimos minutos para una comprobación individual real.

## Apertura docente

Di en voz alta:

> Seguimos en Investigar. Hoy vamos a entender la forma mínima que necesita Java para ejecutar un programa. No quiero que memoricéis símbolos sueltos: quiero que sepáis señalar qué parte hace qué y qué error aparece si rompemos una regla.

Pregunta inicial:

> En un archivo Java, ¿dónde empieza realmente la ejecución: en el nombre de la clase, en la primera llave o en el método `main`?

## Temporalización orientativa

| Tiempo | Acción |
|---|---|
| 0–5 min | Presentar la finalidad y distinguir archivo, clase, método, instrucción y salida. |
| 5–12 min | Proyectar el programa mínimo; relacionar `Main.java`, `Main` y `main`. |
| 12–17 min | Predecir el orden de ejecución y reconocer delimitadores básicos. |
| 17–27 min | Trabajo individual: reconstruir la estructura, clasificar nombres y provocar o localizar un error. |
| 27–34 min | Trabajo por parejas: formular una hipótesis, corregir, ejecutar y explicar el diagnóstico. |
| 34–40 min | Contraste guiado de identificadores y comentarios; no practicar todos los casos con igual profundidad. |
| 40–45 min | Comprobación individual y cierre. |

## Ideas y ejemplos

### Programa mínimo: archivo, clase, método, instrucción y salida

Proyecta este programa completo:

```java
public class Main {
    public static void main(String[] argumentos) {
        System.out.println("Hola");
    }
}
```

Recórrelo de fuera hacia dentro:

- **Archivo:** en estos primeros programas se guarda como `Main.java`.
- **Clase:** `public class Main` define la clase pública llamada `Main`.
- **Método:** `main` es el punto de entrada por el que comienza la ejecución.
- **Instrucción:** `System.out.println("Hola");` ordena una acción concreta.
- **Salida:** al ejecutar, aparece `Hola` en la consola.

Señala también los delimitadores:

- `{` y `}` delimitan bloques;
- `(` y `)` delimitan la información asociada a una llamada o a la cabecera del método;
- `"` delimita el texto;
- `;` cierra la instrucción.

Pregunta:

> Señala el archivo, la clase, el método, una instrucción y la salida observable. ¿Qué llave cierra `main` y cuál cierra la clase?

### `Main.java` y `public class Main`

En estos programas iniciales, el nombre del archivo y el de la clase pública deben coincidir:

```text
Archivo: Main.java
Clase pública: Main
```

Contrasta con este contraejemplo:

```java
// Archivo: Main.java
public class MiniJarvis {
    public static void main(String[] argumentos) {
        System.out.println("Hola");
    }
}
```

Pregunta antes de compilar:

> ¿Qué relación no se cumple? ¿Esperas un problema de escritura del mensaje o de correspondencia entre archivo y clase pública?

Respuesta esperada:

```text
Main.java no coincide con public class MiniJarvis.
```

### `Main` no es `main`

Aclara la diferencia con un segundo programa completo:

```java
public class Main {
    public static void main(String[] argumentos) {
        System.out.println("MiniJarvis");
    }
}
```

Di:

> `Main` puede ser el nombre de la clase. `main` es el método donde comienza la ejecución. Java distingue mayúsculas y minúsculas; no son nombres equivalentes.

Pregunta:

> Si señalas `Main`, ¿estás señalando la clase o el punto de entrada? ¿Qué palabra debes señalar para localizar el punto de entrada?

### Orden de ejecución

Antes de ejecutar, pide una predicción:

```java
public class Main {
    public static void main(String[] argumentos) {
        System.out.println("UNO");
        System.out.println("DOS");
    }
}
```

Pregunta:

> ¿Aparecerá primero `UNO` o `DOS`? Explica qué instrucción se ejecuta antes y qué salida esperas completa.

Después ejecuta y contrasta la predicción con la consola. No basta con acertar: deben relacionar el orden visible con el orden de las instrucciones dentro de `main`.

### Errores sintácticos: localizar antes de cambiar

No presentes los errores como una lista para memorizar. Para cada fragmento utiliza la secuencia:

```text
error -> hipótesis -> corrección -> ejecución
```

Pide primero que localicen el elemento sospechoso, nombren la regla que podría haberse roto y predigan si compilará. Solo después se corrige y se ejecuta.

#### `string` frente a `String`

```java
public static void main(string[] argumentos) {
    System.out.println("Hola");
}
```

Preguntas:

- ¿Qué palabra difiere de la cabecera que ya funcionaba?
- ¿Java trata `string` y `String` como el mismo identificador?
- ¿Qué hipótesis explica el diagnóstico?

Aclara después del intento: `String` es el tipo utilizado por Java en esta cabecera; `string` en minúscula no es equivalente y provoca un error de compilación.

#### Punto y coma ausente

```java
System.out.println("Hola")
System.out.println("MiniJarvis");
```

Pregunta:

> ¿Qué instrucción no queda cerrada? ¿En qué entorno del primer diagnóstico conviene mirar antes de modificar otras líneas?

#### Comilla sin cerrar

```java
System.out.println("Hola);
```

Pregunta:

> ¿Dónde empieza el texto y dónde debería terminar? ¿Qué parte posterior puede interpretar mal el compilador si falta la comilla?

#### Paréntesis sin cerrar

```java
System.out.println("Hola";
```

Pregunta:

> La cadena sí está cerrada. ¿Qué delimitador abierto sigue sin su pareja?

#### Llave de cierre ausente

```java
public class Main {
    public static void main(String[] argumentos) {
        System.out.println("Hola");
}
```

Pregunta:

> ¿Qué bloque cierra la llave visible? ¿Qué bloque permanece abierto?

Aclara que el primer diagnóstico ofrece una pista, no una orden para cambiar código al azar. En esta sesión basta con leer el mensaje, revisar la línea y su entorno, formular una hipótesis pequeña y comprobarla.

### Identificadores: validez y calidad no son lo mismo

Proyecta la clasificación:

```text
nombreUsuario       válido y claro
horasEstudio        válido y claro
nombreAsistente     válido y claro
x                   válido pero pobre
a                   válido pero pobre
dato                válido pero pobre
cosa                válido pero pobre
1nombre             no válido
nombre1             válido
horas estudio       no válido
horasEstudio        válido
class               no válido
public              no válido
nombreClase         válido
```

Desarrolla cuatro categorías:

- **Válido y claro:** cumple las reglas y permite anticipar qué representa.
- **Válido pero pobre:** Java lo admite, pero comunica poco a otra persona.
- **Inválido:** incumple una regla, por ejemplo empezar por una cifra o contener un espacio.
- **Palabra reservada:** `class` y `public` tienen una función propia en Java y no pueden usarse como identificadores.

No pidas solo marcar correcto o incorrecto. Pregunta:

> ¿Qué regla cumple o rompe? Si es válido, ¿qué esperas que almacene? ¿Otra persona comprendería su intención sin ver el valor?

### Comentarios: intención o contexto, no repetición

Contrasta un comentario redundante:

```java
// Muestra Hola
System.out.println("Hola");
```

con otro que aporta contexto:

```java
// Primer mensaje que identifica al asistente
System.out.println("Hola, soy MiniJarvis");
```

Pregunta:

> ¿Qué información añade cada comentario que no pueda leerse ya en la instrucción?

Amplía el contraste:

```java
// Declara horasEstudio
int horasEstudio = 4;

// Valor inicial usado en la demostración
int horasPractica = 4;
```

El primer comentario repite la declaración. El segundo aporta el contexto en el que se usa el valor.

Muestra también un comentario de bloque:

```java
/*
 * Primera versión de MiniJarvis.
 * De momento solo muestra mensajes por consola.
 */
```

Di:

> Un comentario útil explica intención o contexto. Un comentario pobre repite literalmente lo que ya se lee en el código.

## Secuencia de trabajo y modalidad

### Reconstruir, predecir y localizar — INDIVIDUAL

Antes de hablar con otra persona, cada estudiante debe:

1. reconstruir sin copiar la estructura mínima con clase, `main` y una salida;
2. señalar `Main` y `main` y explicar su diferencia;
3. predecir el orden de dos mensajes;
4. escoger uno de los errores preparados, localizarlo y formular una hipótesis sin corregir todavía;
5. clasificar al menos un identificador claro, uno pobre, uno inválido y una palabra reservada;
6. decidir cuál de dos comentarios aporta información nueva.

Cada persona conserva su propio razonamiento antes del contraste. Esta actividad no es una prueba formal separada.

### Comparar, depurar y explicar — PAREJAS

Después, las parejas:

- comparan sus estructuras sin sustituir una por la otra de inmediato;
- contrastan las predicciones de salida;
- explican dónde están la clase y el punto de entrada;
- comparan sus hipótesis sobre el error;
- leen el primer diagnóstico y revisan la línea y su entorno;
- acuerdan una corrección mínima;
- ejecutan y contrastan el resultado;
- justifican la clasificación de identificadores;
- revisan si el comentario explica intención o solo repite el código.

No es necesario practicar con la misma profundidad los cinco errores. Cada pareja depura al menos uno mediante la secuencia completa y utiliza los demás como lectura o contraste guiado.

Secuencia obligatoria de depuración:

```text
error -> hipótesis -> corrección -> ejecución
```

### Comprobar comprensión — INDIVIDUAL

Al terminar, cualquier persona debe poder, sin apoyo de la pareja:

- señalar el punto de entrada;
- distinguir archivo, clase y método;
- explicar una instrucción visible y su salida;
- localizar una regla sintáctica en un fragmento;
- explicar el error provocado, la hipótesis y la corrección;
- justificar por qué un identificador es válido, inválido, claro o pobre;
- reconocer una palabra reservada;
- distinguir un comentario útil de otro redundante.

Si se le propone una modificación pequeña, debe predecir el efecto antes de ejecutar. El producto compartido no sustituye la comprensión individual.

## Evidencia que permanece

- **GitHub:** código de la estructura mínima y correcciones técnicas reproducibles.
- **Scrum:** solo si existe una tarea, decisión, cambio o bloqueo real.
- **Diario individual:** solo si un error o descubrimiento produjo aprendizaje individual significativo.
- **README / Moodle / Drive / Site:** sin actualización o entrega específica en H1.3.

No se crean capturas rutinarias, filas obligatorias ni documentos separados del error.

Modelo para razonar sobre una corrección:

```text
Prueba: estructura mínima ejecutada con dos mensajes.
Error provocado: escribí string en lugar de String.
Hipótesis: Java distingue mayúsculas.
Corrección: cambié string por String.
Resultado: compila y muestra los mensajes esperados.
```

## Observación docente

Durante la actividad y la comprobación individual, observa específicamente:

- que distingue archivo, clase y método;
- que identifica `main` como punto de entrada;
- que predice el orden de las instrucciones antes de ejecutar;
- que reconoce llaves, paréntesis, comillas y punto y coma como delimitadores con funciones distintas;
- que interpreta un diagnóstico sencillo revisando la línea y su entorno;
- que formula una hipótesis antes de modificar el código;
- que diferencia identificador válido de nombre significativo;
- que detecta palabras reservadas;
- que distingue comentario útil de redundante;
- que puede explicar individualmente una corrección realizada en pareja.

## Andamiaje ante bloqueos

No proporciones inmediatamente la solución completa. Utiliza la ayuda mínima correspondiente:

- **Confunde `Main` y `main`:** pide que señale primero la clase y después el método de entrada.
- **El nombre de clase no coincide:** coloca juntos `Main.java` y `public class ...` y pregunta qué nombres deberían coincidir.
- **Falta un delimitador:** pide que lea la línea y su entorno, y que empareje primero llaves, paréntesis o comillas.
- **Cambia elementos al azar:** vuelve al primer diagnóstico y exige una hipótesis sobre una única regla antes de modificar.
- **No comprende el orden:** pide numerar las instrucciones dentro de `main` y anticipar cada salida.
- **Identificador válido pero pobre:** pregunta qué entendería otra persona al leer el nombre sin conocer el valor.
- **Confunde palabra reservada e identificador:** pregunta si Java ya utiliza esa palabra para una función del lenguaje.
- **Comentario redundante:** pregunta qué información añade que no esté ya visible en el código.
- **Una persona resuelve todo:** pide a la otra una explicación o modificación breve sin apoyo.

## Comprueba lo aprendido

Pregunta principal:

> ¿Dónde empieza la ejecución, qué instrucción produce salida y qué delimitador o regla explica el error que has corregido?

Pregunta complementaria:

> ¿Por qué tu identificador comunica bien —o mal— su intención y qué información aporta tu comentario que no aparezca ya en el código?

Cierra en voz alta:

> Una estructura mínima no se aprende copiando símbolos. Se aprende señalando qué parte hace qué, prediciendo el orden y usando un diagnóstico para pasar de error a hipótesis, corrección y ejecución.

## Al terminar

Anota solo lo necesario para la continuidad docente: alumnado que necesita apoyo, regla sintáctica que conviene retomar, bloqueo pendiente con su siguiente paso y ajuste de tiempo necesario.
