# Guion docente completo H1 - Primer MiniJarvis

## Para qué sirve este guion

Este documento está escrito para poder impartir H1 aunque sea la primera vez que das clase, trabajas por proyectos o usas Scrum.

Puedes leer muchas partes literalmente en voz alta. Cuando aparezca `Di en voz alta`, es una formulación preparada para el aula. Cuando aparezca `Pide al alumnado`, es una acción concreta que debes ordenar. Cuando aparezca `Entrega`, indica exactamente qué deben entregar, cuándo, dónde y cómo.

H1 no pretende que el alumnado haga una IA real. H1 pretende que construyan la primera versión ejecutable de MiniJarvis en Java: un programa pequeño de consola que saluda, usa datos, lee entrada, calcula o decide algo sencillo y puede explicarse.

## Producto final de H1

Al terminar H1, cada equipo debe tener un primer MiniJarvis ejecutable en Java y cada persona debe poder defender su comprensión individual.

El producto debe incluir, como máximo razonable de H1:

- proyecto Java ejecutable en IntelliJ;
- `Main.java` sencillo;
- salida clara por consola;
- variables con nombres significativos;
- al menos una constante;
- al menos una operación útil;
- entrada por teclado con `Scanner`;
- una conversión sencilla si se pide un número como texto;
- una comparación y una decisión `if/else` básica;
- README con alcance, límites, ejecución y ejemplo real;
- evidencia de pruebas y explicación.

El producto no debe incluir todavía:

- menú de comandos;
- bucle principal;
- `switch`;
- colecciones;
- ficheros;
- clases propias adicionales complejas;
- persistencia;
- IA real;
- datos personales reales;
- claves, contraseñas, tokens o credenciales.

## Modelo HEXA en H1

H1 sigue el ciclo HEXA completo:

- S206 - Activar: entender el reto y sus límites.
- S207 - Investigar: entender entorno, proyecto, compilación, ejecución y consola.
- S208 - Investigar: entender estructura mínima de Java, sintaxis y errores.
- S209 - Idear: proponer mensajes claros antes de programarlos.
- S210 - Planificar: organizar datos, tipos y nombres antes de escribir más código.
- S211 - Ejecutar: crear con constantes, literales y operaciones.
- S212 - Ejecutar: crear con entrada por teclado y conversiones.
- S213 - Ejecutar: crear con comparaciones, booleanos y una decisión.
- S214 - Comunicar: documentar, seleccionar evidencias y preparar entrega.
- S215 - Comunicar: defender, evaluar, reflexionar y cerrar.

Di en voz alta al comienzo de H1:

> Vamos a trabajar como si fuéramos un equipo de desarrollo. No vamos a estudiar Java como una lista de temas sueltos. Vamos a construir un producto pequeño, MiniJarvis H1, y cada concepto de Java aparecerá porque necesitamos resolver una parte del reto. Seguiremos HEXA: primero entendemos, luego investigamos, ideamos, planificamos, ejecutamos y finalmente comunicamos lo aprendido.

## Scrum mínimo para H1

No conviertas Scrum en una clase teórica larga. En H1 Scrum sirve para que el equipo se organice y deje rastro de decisiones, tareas y bloqueos.

Cada equipo debe usar su Sheet Scrum. En H1 deben aparecer como mínimo:

- backlog de H1;
- tareas de sesión o sprint corto;
- responsable o pareja responsable;
- estado: pendiente, en curso, hecho, bloqueado;
- decisiones del equipo;
- bloqueos;
- evidencias enlazadas;
- mini-review y retrospectiva final.

Roles recomendados para H1:

- facilitador: cuida tiempos y participación;
- responsable de backlog: actualiza tareas en Sheet Scrum;
- responsable técnico: comprueba que el código ejecuta;
- responsable de documentación: comprueba README, evidencias y enlaces.

Los roles no significan que solo una persona haga esa parte. Significan que esa persona vigila que se haga.

Di en voz alta al inicio de cada sesión:

> Antes de programar, cada equipo revisa su Scrum. No es burocracia: si no sabemos qué tarea estamos haciendo, qué decisión hemos tomado y qué bloqueo existe, no estamos trabajando como equipo. Tenéis dos minutos para mirar el tablero y decidir qué vais a mover hoy.

## Ecosistema de entregas

Usa siempre estos espacios. No crees entregables duplicados si la información ya está en su fuente correcta.

- Moodle: entrega final de enlaces y recepción de feedback.
- GitHub: código, README, historial y microprácticas si se guardan como archivos.
- Diario individual en Sheets: proceso personal, avance, prueba, bloqueo, uso de IA y siguiente paso.
- Scrum de equipo en Sheets: backlog, tareas, decisiones, bloqueos, review, retrospectiva y enlaces de evidencias de equipo.
- Site personal: selección razonada de evidencias individuales al cierre del hito.
- Site de equipo: comunicación del incremento del equipo al cierre del hito.
- Drive: evidencias no código y recursos de equipo, siempre con enlaces profundos.

Regla que debes repetir muchas veces:

> Una evidencia no es una captura suelta ni una carpeta general. Una evidencia debe permitir comprobar algo: qué entrada se usó, qué salida se obtuvo, dónde está el código o documento y qué demuestra.

## Entregables oficiales de H1

Estos son los entregables que debes pedir. No los pidas todos el primer día como si tuvieran que estar terminados; se van construyendo.

### Entregable 1 - Diario individual

Cuándo se pide:

- S206 al final: primera entrada de objetivo, alcance y siguiente paso.
- S207-S213 al final de cada sesión donde haya avance, prueba, bloqueo o decisión individual.
- S214 antes de preparar Sites: revisar que el diario contiene las entradas mínimas.
- S215 al cierre: retrospectiva individual final de H1.

Dónde se entrega:

- En el Sheet de diario individual de cada alumno o alumna.
- En Moodle no se sube el diario completo; en la entrega final se pega el enlace profundo o enlace solicitado según la tarea Moodle.

Cómo se entrega:

- Una fila por checkpoint significativo.
- Debe incluir fecha, sesión, objetivo, acción, prueba y resultado, evidencia enlazada, bloqueo si existe, uso de IA si existe y siguiente paso.

Qué debes decir:

> Ahora no quiero un informe largo. Quiero una fila útil en el diario. Si alguien la lee, debe entender qué intentabas hacer, qué hiciste, cómo lo comprobaste y cuál es tu siguiente paso.

### Entregable 2 - Scrum de equipo

Cuándo se pide:

- S206: crear o actualizar backlog H1 y límites del reto.
- S209: registrar decisión de mensajes de consola.
- S210: registrar plan de datos.
- S211-S213: registrar tareas de implementación, bloqueos y decisiones técnicas.
- S214: completar review de evidencias y enlaces.
- S215: completar retrospectiva del equipo.

Dónde se entrega:

- En el Sheet Scrum del equipo.
- En Moodle se entrega el enlace profundo al Sheet Scrum o a la sección indicada, no capturas sueltas salvo que Moodle las pida expresamente.

Cómo se entrega:

- Tareas concretas, no frases vagas.
- Cada tarea debe tener estado.
- Las decisiones deben estar fechadas o vinculadas a la sesión.
- Los bloqueos deben indicar quién puede desbloquearlos o cuál es el siguiente intento.

Qué debes decir:

> En Scrum no escribimos para decorar. Escribimos para que el equipo sepa qué hacer, qué está bloqueado y qué evidencia demuestra que algo está hecho.

### Entregable 3 - Repositorio GitHub H1

Cuándo se pide:

- S207: primera ejecución guardada.
- S208: estructura mínima funcionando.
- S209-S213: evolución del producto y microprácticas.
- S214: repositorio ordenado y README listo.
- S215: versión final defendible.

Dónde se entrega:

- En GitHub.
- En Moodle se entrega el enlace al repositorio y, si procede, enlace profundo a `Main.java`, README o commit concreto.

Cómo se entrega:

- Repositorio accesible al profesorado.
- README en la raíz.
- Código dentro de la estructura del proyecto.
- Microprácticas conservadas si no se integran en `Main.java`, por ejemplo en una carpeta de prácticas o archivos separados acordados.
- No subir credenciales ni datos personales reales.

Qué debes decir:

> GitHub es la fuente del código. Si algo es código, debe estar en el repositorio. Drive no es una segunda copia editable del proyecto.

### Entregable 4 - README H1

Cuándo se pide:

- S214 se pide formalmente.
- S215 debe estar terminado antes de defender.

Dónde se entrega:

- En la raíz del repositorio GitHub.
- En Moodle se entrega el enlace al README o al repositorio que lo contiene.

Cómo se entrega:

- Debe explicar qué hace H1.
- Debe explicar qué no hace todavía.
- Debe explicar cómo ejecutar.
- Debe incluir una transcripción o ejemplo real de entrada y salida.
- Debe indicar pruebas o evidencias usadas.
- Debe ser honesto: no promete H2.

Qué debes decir:

> El README es para una persona que no está sentada a vuestro lado. Si necesita que le expliquéis oralmente cómo ejecutar, el README todavía no está terminado.

### Entregable 5 - Site personal H1

Cuándo se pide:

- S214 se empieza o se completa.
- S215 se revisa antes de entrega final.

Dónde se entrega:

- En el Google Site personal de cada alumno o alumna.
- En Moodle se entrega el enlace profundo a la página H1 del Site personal.

Cómo se entrega:

- Página H1 con reto en sus palabras.
- Aportación individual.
- Una decisión justificada.
- Una dificultad o cambio.
- Una evidencia concreta enlazada.
- Qué demuestra esa evidencia.
- Uso de IA y validación, si procede.
- Mejora siguiente.

Qué debes decir:

> El Site personal no es copiar el diario. El diario cuenta el proceso completo. El Site selecciona una evidencia y explica por qué demuestra aprendizaje.

### Entregable 6 - Site de equipo H1

Cuándo se pide:

- S214 se empieza o se completa.
- S215 se revisa antes de entrega final.

Dónde se entrega:

- En el Google Site de equipo.
- En Moodle se entrega el enlace profundo a la página H1 del Site de equipo.

Cómo se entrega:

- Reto H1 explicado por el equipo.
- Incremento conseguido.
- Decisiones principales.
- Pruebas realizadas.
- Enlaces a repositorio, README y Scrum.
- Review breve.
- Retrospectiva breve.

Qué debes decir:

> El Site de equipo comunica el incremento del equipo. No es el diario de una persona ni una carpeta de enlaces sin explicar.

### Entregable 7 - Entrega final Moodle H1

Cuándo se pide:

- Se anuncia desde S206.
- Se prepara en S214.
- Se entrega al final de S215 o en el plazo Moodle que hayas definido.

Dónde se entrega:

- En la tarea Moodle de H1.

Cómo se entrega:

- Pegando enlaces profundos, no carpetas genéricas.
- Enlace al repositorio GitHub.
- Enlace al README o repositorio que lo contiene.
- Enlace al Site personal H1.
- Enlace al Site de equipo H1.
- Enlace al Sheet Scrum del equipo o sección H1.
- Enlace a evidencia o prueba concreta si la tarea Moodle lo pide.
- Confirmación de permisos comprobados.

Qué debes decir:

> Moodle es el cierre oficial. Si no está en Moodle, no está entregado oficialmente, aunque exista en Drive o GitHub. Moodle no necesita que copiéis todo: necesita enlaces profundos correctos y comprobables.

## Ejemplos modelo de uso de cada entregable

Estos ejemplos no son entregables adicionales. Sirven para enseñar al alumnado qué aspecto tiene una evidencia útil. Puedes proyectarlos, leerlos o pegarlos como modelo en Moodle si lo necesitas.

### Ejemplo 1 - Diario individual

Uso correcto:

```text
Fecha: 2026-10-02
Sesión: S212
Hito: H1
Objetivo: leer un nombre ficticio con Scanner y usarlo en la salida.
Acción realizada: añadí Scanner, pedí un nombre, guardé nextLine() en userName y lo concatené en el saludo.
Prueba y resultado: ejecuté con Laura y salió "Hola, Laura." como esperaba.
Evidencia enlazada: enlace profundo al commit o captura concreta de código + consola.
Bloqueo: al principio leía el nombre pero no usaba la variable.
Uso de IA: no.
Siguiente paso: convertir una entrada numérica con parseInt.
```

Uso incorrecto:

```text
Hoy hice Scanner. Funciona.
```

Qué debes explicar:

> El diario no es una redacción larga ni una frase vacía. Es una fila que permite reconstruir qué intentaste, qué hiciste, cómo lo comprobaste y qué toca después.

### Ejemplo 2 - Scrum de equipo

Uso correcto:

```text
Backlog H1 - Equipo Ada

Tarea: Definir alcance H1
Responsable: equipo completo
Estado: hecho
Evidencia: decisión S206 en Scrum

Tarea: Implementar saludo con nombre ficticio
Responsable: Laura y Samir
Estado: en curso
Evidencia: pendiente de commit

Tarea: Probar entrada no convertible en parseInt
Responsable: Irene
Estado: bloqueado
Bloqueo: no distingue error de compilación y ejecución
Siguiente intento: reproducir ejemplo S212 con el profesor o pareja

Decisión S209: usaremos mensajes breves, sin prometer IA ni memoria.
```

Uso incorrecto:

```text
Hacer Java. Responsable: todos. Estado: más o menos.
```

Qué debes explicar:

> Scrum debe permitir ver trabajo real. Una tarea buena se puede empezar, terminar, bloquear o comprobar. Si no se puede comprobar, está escrita demasiado vaga.

### Ejemplo 3 - Repositorio GitHub H1

Estructura suficiente para H1:

```text
minijarvis-h1/
├── README.md
├── src/
│   └── Main.java
└── practicas-h1/
    ├── S208-estructura.java
    ├── S211-operaciones.java
    └── S213-if-else.java
```

Ejemplo de commit útil:

```text
S212: leer nombre ficticio con Scanner
```

Ejemplo de commit poco útil:

```text
cambios
```

Qué debes explicar:

> GitHub debe permitir localizar el código que se defiende. Si una micropráctica no entra limpia en `Main.java`, puede conservarse separada, pero debe tener nombre y propósito.

### Ejemplo 4 - README H1

Modelo mínimo:

```markdown
# MiniJarvis H1

## Qué hace

MiniJarvis muestra un saludo, pide un nombre ficticio y responde por consola. También calcula minutos a partir de horas de estudio y muestra si el objetivo mínimo se ha alcanzado.

## Límites de H1

No incluye menú, bucle principal, memoria, ficheros, clases propias complejas ni IA real.

## Cómo ejecutar

1. Abrir el proyecto en IntelliJ.
2. Abrir `src/Main.java`.
3. Ejecutar el método `main`.
4. Introducir datos ficticios cuando la consola los pida.

## Ejemplo de ejecución

Entrada usada: Laura, 5
Salida esperada:

Hola, soy MiniJarvis.
Escribe un nombre ficticio: Laura
Encantado, Laura.
Horas de estudio: 5
Minutos equivalentes: 300
Objetivo alcanzado.

## Pruebas

Caso A: hours = 5 -> Objetivo alcanzado.
Caso B: hours = 2 -> Objetivo pendiente.
Entrada no convertible: "hola" en parseInt falla durante la ejecución.
```

Qué debes explicar:

> El README describe el producto real. Si pone que MiniJarvis recuerda conversaciones, pero H1 no tiene memoria, el README está mal aunque suene bonito.

### Ejemplo 5 - Site personal H1

Modelo de contenido:

```text
Reto H1 con mis palabras:
Construir una primera versión de MiniJarvis por consola, pequeña y defendible.

Mi aportación individual:
Implementé y probé la lectura del nombre ficticio con Scanner.

Decisión justificada:
Usé userName en lugar de x porque el nombre permite entender qué dato se guarda.

Dificultad o cambio:
Al principio pensaba que nextLine() devolvía un número si escribía cifras. Lo corregí usando parseInt.

Evidencia seleccionada:
Enlace profundo a prueba S212.

Qué demuestra:
Demuestra que entiendo el flujo pedir -> leer -> guardar -> usar y que sé explicar un error de conversión.

Uso de IA:
No usé IA / Usé IA para preguntar por el error, pero lo validé ejecutando una prueba propia.

Mejora siguiente:
En H2 necesito probar mejor las entradas no válidas.
```

Qué debes explicar:

> El Site personal no debe contener todo. Debe seleccionar una evidencia y explicar por qué demuestra aprendizaje individual.

### Ejemplo 6 - Site de equipo H1

Modelo de contenido:

```text
Reto H1:
Crear un MiniJarvis mínimo por consola con entrada, salida, datos y una decisión sencilla.

Incremento conseguido:
El programa saluda, pide un nombre ficticio, calcula minutos a partir de horas y muestra si se alcanza un objetivo.

Decisiones del equipo:
No incluimos menú ni memoria porque pertenecen a hitos posteriores.
Elegimos mensajes claros y cortos para no prometer funciones inexistentes.

Pruebas realizadas:
Prueba de saludo con Laura.
Prueba de hours = 5.
Prueba de hours = 2.
Prueba de entrada no convertible.

Enlaces:
Repositorio GitHub.
README H1.
Scrum H1.

Review:
El incremento cumple el alcance definido en S206.

Retrospectiva:
Funcionó revisar por parejas. Debemos actualizar Scrum antes y no después de programar.
```

Qué debes explicar:

> El Site de equipo cuenta el incremento colectivo. No sustituye a la defensa individual ni al diario personal.

### Ejemplo 7 - Entrega Moodle H1

Texto modelo para pegar en Moodle:

```text
Equipo: Ada
Integrantes: Laura, Samir, Irene

Repositorio GitHub:
https://...

README H1:
https://...

Site personal H1 de Laura:
https://...

Site personal H1 de Samir:
https://...

Site personal H1 de Irene:
https://...

Site equipo H1:
https://...

Scrum equipo H1:
https://...

Evidencia de ejecución:
https://...

Permisos comprobados: sí
Observaciones o bloqueo pendiente: ninguno / queda pendiente defender conversión de entrada no válida.
```

Uso incorrecto:

```text
Está todo en Drive.
```

Qué debes explicar:

> Moodle es el índice oficial de entrega. No quiero una carpeta general ni una frase. Quiero enlaces profundos que me lleven directamente a lo que debo revisar.

## Píldoras H1 integradas en el guion

Estas píldoras proceden de `01-ALUMNADO/03-SESIONES/h1/pildoras/`. No sustituyen a los archivos completos del alumnado; son una versión docente integrada para saber cuándo usarlas y qué idea leer en voz alta.

### Píldora S206 - Alcance y calidad de H1

Cuándo usarla:

- Durante S206, después de presentar el reto y antes de clasificar qué entra y qué queda fuera.

Di en voz alta:

> Un primer programa debe ser correcto, eficiente y mantenible. Correcto significa que hace lo pedido y podemos comprobarlo. Eficiente, en H1, no significa que vaya rapidísimo: significa que no añade complejidad innecesaria. Mantenible significa que se entiende y se puede modificar sin romperlo fácilmente.

Ejemplo para proyectar:

```java
final String ASSISTANT_NAME = "MiniJarvis";
String userName = "Laura";
System.out.println("Hola, soy " + ASSISTANT_NAME + ".");
System.out.println("Encantado, " + userName + ".");
```

Pregunta al alumnado:

> Qué requisito demuestra cada línea visible, qué parte quitarías si no pertenece a H1 y qué nombre ayuda a entender el código.

Error frecuente que debes cortar:

> Compilar no basta para decir que es correcto. Falta comprobar comportamiento.

### Píldora S207 - Del código a la consola

Cuándo usarla:

- Durante S207, antes de la primera ejecución y otra vez cuando aparezca el primer error.

Di en voz alta:

> El recorrido básico es código fuente, compilación, ejecución y consola. Escribir es modificar `Main.java`. Compilar es comprobar y traducir. Ejecutar es poner en marcha. La consola es donde observamos el resultado.

Ejemplo para proyectar:

```java
public class Main {
    public static void main(String[] args) {
        System.out.println("MiniJarvis arranca");
    }
}
```

Salida esperada:

```text
MiniJarvis arranca
```

Pregunta al alumnado:

> Señala dónde está el código fuente, qué ocurre antes de la consola y cómo sabes que se ha ejecutado.

Error frecuente que debes cortar:

> No reescribas todo si falla. Lee el primer error y decide si es código o configuración.

### Píldora S208 - Estructura y escritura de Java

Cuándo usarla:

- Durante S208, al explicar clase, archivo, `main`, delimitadores, identificadores y comentarios.

Di en voz alta:

> En estos primeros programas, el archivo se llama `Main.java`, la clase pública se llama `Main` y el método `main` es el punto de entrada. Java distingue mayúsculas y necesita delimitadores: punto y coma, llaves, paréntesis y comillas.

Ejemplo para proyectar:

```java
public class Main {
    public static void main(String[] args) {
        // Usamos un nombre ficticio para no publicar datos personales.
        String userName = "Laura";
        System.out.println("Hola, " + userName + ".");
    }
}
```

Pregunta al alumnado:

> Señala clase, punto de entrada, una instrucción visible, un identificador y un comentario útil.

Error frecuente que debes cortar:

> `String` no es `string`. `Main` no es `main`. Las mayúsculas importan.

### Píldora S209 - Mensajes claros y concatenación

Cuándo usarla:

- Durante S209, antes de abrir el IDE para obligar a idear la salida.

Di en voz alta:

> La consola también es una interfaz. Aunque sea texto, la persona usuaria debe entender qué ocurre, qué se le pide y qué resultado obtiene. Además, no debemos prometer funciones que H1 no tiene.

Ejemplo para comparar:

```text
MJ v1
ok
```

Frente a:

```text
Hola, soy MiniJarvis.
Escribe un nombre ficticio: Laura
Encantado, Laura.
Fin de la primera prueba.
```

Ejemplo de concatenación:

```java
String userName = "Laura";
System.out.println("Hola, " + userName + ".");
```

Pregunta al alumnado:

> Qué salida ayuda más, qué dato cambia y dónde hacen falta espacios o signos.

Error frecuente que debes cortar:

> No escribáis `Puedo recordar todo` si H1 no tiene memoria.

### Píldora S210 - Variables, tipos y nombres

Cuándo usarla:

- Durante S210, antes de la tabla de datos y antes de implementar variables.

Di en voz alta:

> Una variable es una zona de memoria identificada por un nombre. El tipo indica qué clase de dato puede guardar. El valor puede cambiar. La variable no es lo mismo que su valor actual.

Ejemplo para proyectar:

```java
int studyHours = 4;
String userName = "Laura";
boolean goalReached = true;

studyHours = 5;
```

Pregunta al alumnado:

> Identifica tipo, nombre y valor. Qué variable ha cambiado y por qué no se repite `int` al asignar de nuevo.

Error frecuente que debes cortar:

> `String` no sirve para todo. Elegimos el tipo según lo que necesitamos representar y hacer con el dato.

### Píldora S211 - Constantes, literales y operaciones

Cuándo usarla:

- Durante S211, antes de introducir `final`, división entera, `%` y actualización.

Di en voz alta:

> Una constante representa un dato que no debe cambiar durante la ejecución. Un literal es un valor escrito directamente. Una operación produce un resultado, pero ese resultado se pierde si no lo guardamos, mostramos o usamos.

Ejemplo para proyectar:

```java
final String ASSISTANT_NAME = "MiniJarvis";
int hours = 5;
int minutes = hours * 60;
int half = 5 / 2;
int remaining = 10 % 4;
```

Pregunta al alumnado:

> Predice `minutes`, `half` y `remaining`. Explica por qué `%` no significa porcentaje.

Error frecuente que debes cortar:

> `5 / 2` con enteros da `2`, no `2.5`.

### Píldora S212 - Scanner y conversiones

Cuándo usarla:

- Durante S212, al pasar de datos escritos en código a datos introducidos por consola.

Di en voz alta:

> `Scanner` permite leer lo que una persona escribe. `nextLine()` devuelve siempre un `String`. Si queremos calcular con un número escrito por teclado, necesitamos parsear ese texto.

Ejemplo para proyectar:

```java
import java.util.Scanner;

Scanner scanner = new Scanner(System.in);
System.out.print("Escribe un nombre ficticio: ");
String userName = scanner.nextLine();
System.out.println("Hola, " + userName + ".");
scanner.close();
```

Ejemplo de parseo:

```java
String text = "5";
int hours = Integer.parseInt(text);
int minutes = hours * 60;
```

Pregunta al alumnado:

> Qué devuelve `nextLine`, qué guarda `userName`, qué convierte `parseInt` y cuándo falla `Integer.parseInt("hola")`.

Error frecuente que debes cortar:

> Que el texto contenga cifras no lo convierte automáticamente en número.

### Píldora S213 - Comparaciones, lógica y decisiones

Cuándo usarla:

- Durante S213, antes de `if/else` y antes de pedir las dos pruebas.

Di en voz alta:

> Una comparación produce un booleano: `true` o `false`. `=` asigna; `==` compara. `if` necesita una condición booleana. En H1 hacemos decisiones pequeñas; menús y decisiones encadenadas vendrán en H2.

Ejemplo para proyectar:

```java
int hours = 5;
boolean enough = hours >= 4;

if (enough) {
    System.out.println("Objetivo alcanzado");
} else {
    System.out.println("Objetivo pendiente");
}
```

Pregunta al alumnado:

> Qué pasa con `hours = 5`, qué pasa con `hours = 2`, qué rama se ejecuta y qué evidencia demuestra cada caso.

Error frecuente que debes cortar:

> Probar solo el caso `true` no demuestra el `else`.

### Píldora S214 - README y evidencias

Cuándo usarla:

- Durante S214, antes de documentar y antes de preparar Moodle.

Di en voz alta:

> Documentar no significa copiar la misma información en muchos sitios. Cada espacio responde a una pregunta: README explica cómo ejecutar; diario cuenta el proceso personal; Site personal selecciona aprendizaje; Site de equipo comunica el incremento; Moodle recoge enlaces oficiales.

Ejemplo de evidencia verificable:

```text
Prueba: saludo con nombre ficticio.
Entrada usada: Laura.
Salida esperada: Encantado, Laura.
Salida obtenida: Encantado, Laura.
Demuestra: la entrada leída se guarda y se usa en la salida.
Enlace: archivo o captura concreta, no carpeta general.
```

Pregunta al alumnado:

> Qué demuestra esta evidencia, dónde debería estar enlazada y por qué no basta con escribir `funciona`.

Error frecuente que debes cortar:

> No enlacéis carpetas generales. Enlazad la evidencia concreta.

## Rutina fija para cada sesión

Usa esta rutina aunque la sesión cambie de contenido.

1. Abre con el objetivo en lenguaje sencillo.
2. Recuerda la fase HEXA del día.
3. Haz una revisión Scrum de dos minutos.
4. Explica solo lo necesario para desbloquear la práctica.
5. Pide predicción antes de ejecutar código.
6. Haz trabajar individualmente cuando la comprensión deba ser personal.
7. Haz contrastar por parejas cuando convenga detectar errores.
8. Haz trabajar en equipo cuando haya decisión, backlog, README, Site o reparto.
9. Pide evidencia concreta.
10. Cierra con diario, Scrum o entrega según corresponda.

Di en voz alta cuando haya código:

> Antes de ejecutar, escribe o di qué esperas que ocurra. Programar no es pulsar ejecutar hasta que algo salga. Programar es predecir, ejecutar, comparar y corregir.

## S206 - Activar - Presentar H1 y delimitar alcance

### Objetivo de la sesión

El alumnado debe entender qué es H1, qué entra, qué no entra y cómo se demostrará el avance.

### Antes de empezar

Ten abierta la presentación S206. Ten localizable Moodle, el Sheet Scrum de equipos y el diario individual.

### Apertura docente

Di en voz alta:

> Hoy empieza H1, el primer MiniJarvis ejecutable. No vamos a construir una IA completa. Vamos a construir una primera versión pequeña, clara, ejecutable y defendible. El éxito de H1 no es hacer muchas cosas; el éxito es hacer pocas cosas bien, entenderlas y poder demostrarlas.

Di en voz alta:

> La fase HEXA de hoy es Activar. Activar significa entender el reto. Si hoy no dejamos claro el alcance, después programaremos cosas que no tocan o entregaremos evidencias que no demuestran nada.

### Scrum del día

Pide al alumnado:

> En equipos, abrid vuestro Sheet Scrum. Durante dos minutos escribid una primera tarea grande llamada `Entender alcance H1` y debajo tres tareas pequeñas: `definir qué entra`, `definir qué queda fuera`, `escribir requisitos comprobables`.

Trabajo en grupo:

- Cada equipo escribe tareas iniciales en Scrum.
- Cada equipo asigna roles H1, aunque sean provisionales.
- El responsable de backlog escribe las tareas.

Entrega en esta sesión:

- Qué: primeras tareas de backlog H1 y roles provisionales.
- Cuándo: durante los primeros 10 minutos.
- Dónde: Sheet Scrum del equipo.
- Cómo: filas concretas con tarea, responsable o pareja responsable, estado inicial y sesión S206.
- Moodle: no se entrega todavía en Moodle; se entregará enlace al Scrum al cierre de H1.

### Explicación docente

Di en voz alta:

> H1 entra dentro del Tema 1. Vamos a tocar entorno, estructura básica de Java, salida por pantalla, variables, constantes, operaciones, entrada con Scanner, conversiones y una decisión sencilla. Pero no todo tiene que estar metido en el mismo `Main.java`. Algunas cosas serán microprácticas para aprender y defender.

Di en voz alta:

> En H1 sí entra: saludo, mensajes por consola, variables, constantes, entrada y salida, operaciones sencillas, comparación, una decisión básica y explicación. En H1 no entra: menús, bucles, memoria, ficheros, clases complejas, persistencia ni IA real. Eso llegará más adelante.

### Investigación del alumnado

Pide al alumnado:

> Ahora investigad en la ficha de H1 y en la presentación qué tiene que poder demostrar una primera versión. No busquéis todavía soluciones en internet. Buscad primero los límites del reto y los criterios de evidencia.

Trabajo individual:

- Cada persona escribe en su cuaderno o borrador una frase: `H1 consiste en...`.
- Cada persona marca una duda sobre el alcance.

Trabajo en grupo:

- El equipo compara frases.
- El equipo decide una frase común de alcance.

### Actividad central

Pide al alumnado:

> Clasificad estas ideas en tres columnas: entra en H1, más adelante, fuera del reto. Usad criterio, no gusto personal.

Ideas para proyectar o dictar:

- saludar;
- pedir un nombre ficticio;
- guardar horas de estudio;
- calcular minutos;
- hacer un menú;
- recordar conversaciones;
- guardar en fichero;
- usar una API de IA;
- mostrar un mensaje final;
- decidir si se ha alcanzado un objetivo.

Trabajo en grupo:

- Cada equipo clasifica.
- Cada equipo justifica dos decisiones.

### Entrega de S206

Pide explícitamente:

> Antes de terminar, cada equipo debe dejar en Scrum tres cosas: frase de alcance H1, lista breve de lo que entra y lista breve de lo que queda fuera.

Dónde y cómo:

- Scrum de equipo: sección de decisiones o backlog.
- Formato: texto breve, fechado como S206.
- No aceptar: frases como `hacer que funcione` sin comprobar.

Pide también:

> Cada persona debe crear una entrada de diario individual de S206.

Dónde y cómo:

- Diario individual en Sheets.
- Una fila con objetivo, decisión de alcance, evidencia enlazada si existe, bloqueo si existe y siguiente paso.
- No se sube a Moodle hoy.

### Cierre docente

Di en voz alta:

> Cerramos Activar. Para avanzar, cada equipo debe poder explicar qué va a construir y qué no va a construir. Mañana o en la siguiente sesión investigaremos cómo se pasa de escribir código a verlo ejecutarse en consola.

## S207 - Investigar - Entorno Java, IntelliJ, proyecto y ejecución

### Objetivo de la sesión

El alumnado debe comprender el camino `código fuente -> compilación -> ejecución -> consola` y lograr una primera ejecución.

### Apertura docente

Di en voz alta:

> Hoy estamos en Investigar. Investigar no significa buscar cualquier cosa en Google. Significa aprender lo imprescindible para poder construir H1. Hoy necesitamos entender qué ocurre entre escribir `Main.java` y ver un mensaje en la consola.

### Scrum del día

Pide al alumnado:

> Equipos, abrid Scrum y añadid o actualizad estas tareas: `crear o abrir proyecto Java`, `localizar Main.java`, `ejecutar primer mensaje`, `guardar evidencia de ejecución`.

Entrega en esta sesión:

- Qué: tareas técnicas iniciales actualizadas.
- Cuándo: primeros 5 minutos.
- Dónde: Sheet Scrum del equipo.
- Cómo: estado claro de cada tarea.
- Moodle: todavía no.

### Explicación docente

Di en voz alta:

> Un archivo Java contiene código fuente. El proyecto reúne archivos y configuración. El JDK permite compilar y ejecutar. La consola muestra lo que el programa escribe cuando se ejecuta. Escribir no es ejecutar, compilar no es ejecutar y la consola no es el código.

Demuestra lentamente:

```java
public class Main {
    public static void main(String[] args) {
        System.out.println("Hola, soy MiniJarvis.");
    }
}
```

Mientras demuestras, di:

> Mirad primero, no copiéis todavía. Señalo el archivo, señalo el botón de ejecución y señalo la consola. Ahora vamos a comprobar qué parte es código y qué parte es resultado.

### Investigación del alumnado

Pide al alumnado:

> Individualmente, localiza en tu pantalla tres cosas: el archivo `Main.java`, el lugar donde escribes código y la consola donde aparece el resultado. Si no encuentras una, levanta la mano y tu pareja mira contigo antes de llamarme.

Trabajo individual:

- Localizar archivo, editor y consola.
- Escribir un mensaje propio.
- Predecir salida antes de ejecutar.

Trabajo por parejas:

- Comprobar que la predicción coincide con la salida.
- Ayudar a localizar errores de entorno.

### Actividad central

Pide al alumnado:

> Escribid un mensaje distinto al ejemplo. Antes de ejecutar, escribid qué esperáis ver. Luego ejecutad y comparad.

Después pide:

> Ahora romped algo a propósito: quitad un punto y coma o una comilla. Antes de corregir, leed el error. No borréis todo. Localizad el primer lugar donde el IDE os da información.

### Entrega de S207

Pide explícitamente:

> Guardad una evidencia de primera ejecución. Debe verse o quedar localizable el código y la salida. Añadid una frase: `Sé que se ha ejecutado porque...`.

Dónde y cómo:

- GitHub o espacio de trabajo acordado: código del primer `Main.java`.
- Drive si se usa captura puntual: captura con código y consola, no solo consola.
- Diario individual: enlace a la evidencia y frase explicativa.
- Scrum de equipo: marcar tarea `primera ejecución` como hecha o bloqueada.
- Moodle: no se entrega todavía; se enlazará al final de H1.

Qué no aceptar:

- Captura solo de consola sin código.
- Frase `funciona` sin explicación.

### Cierre docente

Di en voz alta:

> Hoy no hemos aprendido solo a pulsar ejecutar. Hemos aprendido el recorrido: escribir, compilar, ejecutar y observar. Si algo falla, primero leemos el error y formulamos una hipótesis.

## S208 - Investigar - Estructura mínima de un programa Java

### Objetivo de la sesión

El alumnado debe reconstruir y depurar la estructura mínima de Java: clase, `main`, llaves, paréntesis, comillas, punto y coma, identificadores y comentarios.

### Apertura docente

Di en voz alta:

> Seguimos en Investigar. Hoy vamos a entender la forma mínima que necesita Java para ejecutar nuestro programa. No quiero que memoricéis símbolos sueltos: quiero que sepáis señalar qué parte hace qué y qué error aparece si rompemos una regla.

### Scrum del día

Pide al alumnado:

> En Scrum, revisad si la tarea de primera ejecución está hecha. Añadid una tarea nueva: `reconstruir estructura mínima y depurar un error`.

Dónde y cómo:

- Sheet Scrum del equipo.
- Estado de la tarea y bloqueo si alguien no pudo ejecutar en S207.

### Explicación docente

Di en voz alta mientras proyectas código:

> `public class Main` define la clase pública. En estos programas iniciales, el archivo se llama `Main.java` y la clase pública se llama `Main`. `main` es el punto de entrada: por ahí empieza la ejecución. `System.out.println` es una instrucción que produce salida visible. Las llaves delimitan bloques. El punto y coma cierra instrucciones.

Código de referencia:

```java
public class Main {
    public static void main(String[] args) {
        // Presenta la version actual.
        System.out.println("Hola");
        System.out.println("MiniJarvis arranca");
    }
}
```

### Investigación del alumnado

Pide al alumnado:

> Sin ejecutar todavía, señalad qué líneas producirán salida y cuáles no. Después comparad con vuestra pareja.

Trabajo individual:

- Señalar partes del código.
- Predecir qué línea produce salida.

Trabajo por parejas:

- Comparar predicción.
- Localizar errores en dos fragmentos preparados.

### Actividad central

Pide al alumnado:

> Reconstruid la estructura mínima sin copiar directamente. Añadid dos mensajes y un comentario útil. Luego introducid un error pequeño, leed el diagnóstico, corregidlo y ejecutad.

Recuerda:

> Un comentario útil no repite lo obvio. No escribimos `// imprime hola` encima de `println("Hola")`. Escribimos contexto o intención.

### Entrega de S208

Pide explícitamente:

> Antes de terminar, cada persona debe conservar una evidencia de estructura mínima funcionando y una nota del error que ha provocado y corregido.

Dónde y cómo:

- GitHub: código actualizado o micropráctica de estructura.
- Diario individual: fila S208 con error provocado, hipótesis, corrección y resultado.
- Scrum: si el equipo detecta un error común, registrarlo como decisión o aprendizaje técnico.
- Moodle: no se entrega todavía.

Qué debe contener la evidencia:

- Código con estructura mínima.
- Salida observada.
- Explicación de una regla sintáctica.

### Cierre docente

Di en voz alta:

> Para cerrar S208, cada persona debe poder señalar dónde empieza la ejecución, qué instrucción muestra texto y una regla cuya ruptura impide compilar.

## S209 - Idear - Salida por pantalla y mensajes del asistente

### Objetivo de la sesión

El alumnado debe idear mensajes claros antes de programarlos y usar literales y concatenación cuando sea necesario.

### Apertura docente

Di en voz alta:

> Hoy cambiamos de fase: Idear. Idear significa proponer soluciones antes de construir. La consola también es una interfaz. Si MiniJarvis escribe mensajes confusos, el programa puede compilar, pero la experiencia será mala.

### Scrum del día

Pide al alumnado:

> En Scrum, añadid una tarea de equipo: `decidir mensajes de H1`. Esa tarea no está hecha hasta que tengáis al menos dos alternativas y una razón para elegir una.

Entrega en esta sesión:

- Qué: decisión de mensajes de consola.
- Dónde: Sheet Scrum, sección decisiones o backlog.
- Cómo: alternativa elegida, alternativa descartada y motivo.

### Explicación docente

Di en voz alta:

> `System.out.println` no solo sirve para sacar texto. Sirve para comunicarse con la persona que ejecuta el programa. Un buen mensaje dice qué ocurre, qué se pide y qué resultado se obtiene. Además, si queremos mezclar texto fijo con datos, usamos concatenación.

Ejemplo:

```java
String userName = "Laura";
System.out.println("Hola, " + userName + ".");
```

Di:

> Aquí `+` no está sumando números. Está uniendo texto con el valor de una variable.

### Investigación del alumnado

Pide al alumnado:

> Investigad en parejas qué hace comprensible una salida de consola. No busquéis diseño gráfico. Pensad en texto: orden, claridad, información y límites.

Trabajo por parejas:

- Comparar dos salidas.
- Formular dos criterios de claridad.

Trabajo en grupo:

- Proponer dos versiones de mensajes para H1.
- Elegir una.

### Actividad central

Pide al alumnado:

> Todavía no abráis el IDE. Primero escribid dos versiones de saludo, propósito y mensaje final. Después elegid una y justificadla. Solo entonces programadla.

Después:

> Programad la salida elegida. Ejecutadla. Pedid a otra persona que lea solo la consola y os diga si entiende qué hace MiniJarvis.

### Entrega de S209

Pide explícitamente:

> Registrad la decisión de diseño de mensajes y guardad la versión programada.

Dónde y cómo:

- Scrum de equipo: decisión de mensajes con motivo.
- GitHub: código con mensajes implementados.
- Diario individual: fila breve si la persona ha cambiado o defendido una decisión.
- Moodle: no se entrega todavía.

Qué debe aparecer:

- Mensaje elegido.
- Por qué se elige.
- Qué se cambió después de verlo ejecutado.

### Cierre docente

Di en voz alta:

> Hemos ideado antes de programar. Esa es la clave de hoy. La salida de consola no se improvisa al final: se diseña para que alguien entienda qué ocurre.

## S210 - Planificar - Variables

### Objetivo de la sesión

El alumnado debe planificar datos: qué se guarda, con qué tipo, con qué nombre y dónde se usa.

### Apertura docente

Di en voz alta:

> Hoy estamos en Planificar. Planificar en programación significa decidir antes de escribir código qué datos necesitamos, qué tipo tienen y cómo se llaman. Si programamos sin plan de datos, acabamos con nombres vagos, valores repetidos y errores difíciles de explicar.

### Scrum del día

Pide al alumnado:

> En Scrum, añadid una tarea: `planificar datos de H1`. No la marquéis como hecha hasta tener una tabla con dato, tipo, nombre, si cambia y dónde se usa.

Entrega en esta sesión:

- Qué: plan de datos H1.
- Dónde: Scrum de equipo o documento enlazado desde Scrum.
- Cómo: tabla breve con dato, tipo, nombre, cambia si/no y uso.

### Explicación docente

Di en voz alta:

> Una variable es una zona de memoria con nombre que guarda un dato. El tipo indica qué clase de dato puede guardar. El nombre debe ayudar a entender para qué sirve. En Java, declarar, inicializar y asignar no son exactamente lo mismo.

Ejemplo:

```java
int studyHours = 4; // declara e inicializa
studyHours = 5;     // asigna otro valor
```

Di:

> El tipo `int` se escribe al declarar. No se repite cada vez que cambia el valor.

### Investigación del alumnado

Pide al alumnado:

> Individualmente, clasificad estos datos: nombre de usuario, horas de estudio, nota media, objetivo alcanzado e inicial. Decid qué tipo usaríais y por qué.

Trabajo individual:

- Elegir tipos.
- Proponer nombres.

Trabajo en grupo:

- Unificar plan de datos.
- Corregir nombres vagos.

### Actividad central

Pide al alumnado:

> Antes del código, haced la tabla de datos. Después implementad al menos tres variables, mostradlas por consola, cambiad una y volved a mostrarla para comprobar que entendéis la asignación.

### Entrega de S210

Pide explícitamente:

> Hoy sí quiero una evidencia individual: cada persona debe poder señalar una variable propia y explicar tipo, nombre, valor inicial y una asignación posterior.

Dónde y cómo:

- Scrum o documento del equipo: plan de datos.
- GitHub: código con variables usadas.
- Diario individual: fila S210 con una variable explicada y prueba de salida.
- Moodle: no se entrega todavía.

Qué revisar:

- Que no usen `x`, `dato1` o nombres sin significado.
- Que no repitan valores fijos por todas partes.
- Que sepan distinguir variable y valor.

### Cierre docente

Di en voz alta:

> Cerramos Planificar con un plan de datos. La próxima sesión entraremos más fuerte en Ejecutar: constantes, literales y operaciones.

## S211 - Ejecutar - Constantes, literales y operaciones

### Objetivo de la sesión

El alumnado debe usar constantes, literales y operaciones aritméticas con predicción y prueba.

### Apertura docente

Di en voz alta:

> Hoy entramos en Ejecutar. Ejecutar no significa escribir mucho código sin pensar. Significa construir, probar y mejorar. Hoy cada operación debe ir acompañada de una predicción y una comprobación.

### Scrum del día

Pide al alumnado:

> En Scrum, añadid tareas concretas: `añadir constante`, `añadir operación`, `probar resultado`, `registrar error o aprendizaje`.

Dónde y cómo:

- Sheet Scrum.
- Estado por tarea.
- Bloqueo si no entienden división entera, `%` o precedencia.

### Explicación docente

Di en voz alta:

> Una constante es un dato que no debe cambiar durante la ejecución. En Java usamos `final`. Un literal es un valor escrito directamente en el código, como `5`, `3.5`, `"Hola"`, `'A'`, `true` o `false`. Una operación produce un resultado; si queremos usarlo, debemos mostrarlo o guardarlo.

Ejemplos:

```java
final String ASSISTANT_NAME = "MiniJarvis";
final int START_YEAR = 2026;

int minutes = studyHours * 60;
```

Di:

> Cuidado con `5 / 2`. Si ambos son enteros, el resultado entero es `2`. Para obtener `2.5`, necesitamos un decimal, por ejemplo `5 / 2.0`.

### Investigación del alumnado

Pide al alumnado:

> Investigad con ejemplos pequeños qué pasa con `5 / 2`, `5 / 2.0` y `10 % 4`. Primero predecid. Después ejecutad. Después explicad con palabras.

Trabajo individual:

- Resolver predicciones.
- Ejecutar micropráctica.

Trabajo por parejas:

- Comparar resultados.
- Explicar `%` sin decir porcentaje.

### Actividad central

Pide al alumnado:

> En vuestro MiniJarvis o en una micropráctica, usad una constante, una variable, una operación, una actualización y una salida que permita comprobar el resultado.

### Entrega de S211

Pide explícitamente:

> Conservad la micropráctica o el código integrado y registrad una predicción que haya sido confirmada o corregida.

Dónde y cómo:

- GitHub: código de micropráctica o `Main.java` actualizado.
- Diario individual: predicción, resultado observado y explicación breve.
- Scrum: marcar tareas de constante/operación/prueba.
- Moodle: no se entrega todavía.

Qué debe contener:

- Uso de `final`.
- Una operación comprobable.
- Evidencia de resultado.

### Cierre docente

Di en voz alta:

> Una operación no está demostrada porque el código compile. Está demostrada cuando puedo predecir el resultado, ejecutarlo y explicar si coincide.

## S212 - Ejecutar - Scanner y conversiones

### Objetivo de la sesión

El alumnado debe leer entrada, guardarla, convertir texto a número cuando haga falta y reconocer errores de conversión.

### Apertura docente

Di en voz alta:

> Hasta ahora muchos datos los decidía quien programaba. Hoy MiniJarvis empezará a recibir datos de quien lo ejecuta. Eso cambia el programa: necesitamos pedir, leer, guardar, convertir si hace falta, calcular y mostrar.

### Scrum del día

Pide al alumnado:

> En Scrum, añadid tareas: `leer nombre ficticio`, `usar entrada en salida`, `leer número como texto`, `convertir y calcular`, `probar entrada no válida`.

Entrega en esta sesión:

- Qué: tareas de entrada y conversión.
- Dónde: Sheet Scrum.
- Cómo: cada tarea con estado y responsable.

### Explicación docente

Di en voz alta:

> `Scanner` nos permite leer desde teclado. Para H1 usaremos una sola instancia sencilla. `nextLine()` devuelve texto, es decir, `String`. Si ese texto representa un número y queremos calcular, debemos convertirlo.

Ejemplo:

```java
import java.util.Scanner;

Scanner scanner = new Scanner(System.in);
System.out.print("Nombre ficticio: ");
String userName = scanner.nextLine();
System.out.println("Hola, " + userName + ".");
scanner.close();
```

Después:

```java
String text = "5";
int hours = Integer.parseInt(text);
int minutes = hours * 60;
System.out.println(minutes);
```

Di:

> `"5"` y `5` no son lo mismo para Java. El primero es texto; el segundo es un entero.

### Investigación del alumnado

Pide al alumnado:

> Investigad ejecutando dos veces con nombres ficticios distintos. ¿Qué cambia? ¿Qué no cambia? Después probad una conversión válida y una no válida.

Trabajo individual:

- Implementar entrada de nombre.
- Probar dos entradas ficticias.

Trabajo por parejas:

- Comparar flujo pedir-leer-guardar-mostrar.
- Probar `Integer.parseInt("hola")` como error útil si procede.

### Actividad central

Pide al alumnado:

> Construid una prueba con entrada válida: por ejemplo horas como texto, conversión a `int`, cálculo de minutos y salida. Después probad una entrada no convertible y explicad cuándo falla: al compilar o al ejecutar.

### Entrega de S212

Pide explícitamente:

> Hoy la evidencia debe incluir una entrada válida, resultado esperado, resultado obtenido y explicación de qué ocurre con una entrada no convertible.

Dónde y cómo:

- GitHub: código con `Scanner` o micropráctica de conversión.
- README puede ir recogiendo ejemplo, aunque se pedirá formalmente en S214.
- Diario individual: fila S212 con prueba válida y error de conversión explicado.
- Scrum: tarea de entrada/conversión actualizada.
- Moodle: no se entrega todavía.

Qué no aceptar:

- Captura sin decir qué entrada se usó.
- Código que lee una variable pero no la usa.
- Decir `no funciona` sin distinguir compilación y ejecución.

### Cierre docente

Di en voz alta:

> Hoy MiniJarvis ya no solo muestra datos escritos por quien programa. Ahora reacciona a una entrada. Pero si la entrada viene como texto, debemos decidir cuándo convertir y cómo comprobar el resultado.

## S213 - Ejecutar - Comparaciones, lógica y decisiones

### Objetivo de la sesión

El alumnado debe construir booleanos, combinar condiciones y usar una decisión `if/else` con dos ramas probadas.

### Apertura docente

Di en voz alta:

> Hoy MiniJarvis empieza a decidir algo muy pequeño. No haremos menús ni bucles. Eso será H2. Hoy queremos entender que una comparación produce `true` o `false`, y que `if/else` usa ese resultado para elegir una rama.

### Scrum del día

Pide al alumnado:

> En Scrum, añadid tareas: `crear comparación`, `guardar boolean`, `implementar if/else`, `probar caso true`, `probar caso false`, `registrar mejora`.

Dónde y cómo:

- Sheet Scrum.
- Cada prueba debe enlazar o describir la evidencia.

### Explicación docente

Di en voz alta:

> Comparar no devuelve uno de los operandos. Devuelve un booleano: `true` o `false`. `=` asigna. `==` compara. Para números podemos usar `==`, `!=`, `<`, `<=`, `>` y `>=`. En H1 no vamos a usar `==` para comparar textos.

Ejemplo:

```java
int hours = 5;
boolean enough = hours >= 4;
System.out.println(hours == 5); // true
System.out.println(hours != 5); // false
System.out.println(enough);     // true
```

Después:

```java
if (hours >= 4) {
    System.out.println("Objetivo alcanzado");
} else {
    System.out.println("Objetivo pendiente");
}
```

Di:

> Un `if` necesita una expresión booleana. `if (hours)` no vale, porque `hours` es un `int`, no una condición.

### Investigación del alumnado

Pide al alumnado:

> Investigad tres operadores lógicos con ejemplos verbales: `&&`, `||` y `!`. No memoricéis símbolos: traducidle el significado a una persona que no programa.

Trabajo individual:

- Predecir comparaciones.
- Cambiar un valor para obtener `true` y `false`.

Trabajo por parejas:

- Traducir condiciones a lenguaje natural.
- Comprobar si se han probado ambas ramas.

### Actividad central

Pide al alumnado:

> Construid una práctica defendible: dato, comparación, boolean, `if/else` y salida. Debéis probar dos casos: uno que entre por `if` y otro que entre por `else`.

### Entrega de S213

Pide explícitamente:

> La evidencia de hoy debe demostrar dos ramas. No basta con probar el caso favorable.

Dónde y cómo:

- GitHub: código con comparación e `if/else`.
- Diario individual: caso A, salida esperada, salida obtenida; caso B, salida esperada, salida obtenida.
- Scrum: marcar pruebas true/false y registrar mejora concreta.
- Moodle: no se entrega todavía.

Qué debe poder defender cada persona:

- Qué comparación se evalúa.
- Qué significa `true`.
- Qué significa `false`.
- Qué rama se ejecuta en cada caso.
- Qué mejora concreta hizo en el código o nombres.

### Cierre docente

Di en voz alta:

> H1 ya tiene una decisión pequeña. Si hoy alguien solo puede decir `funciona`, todavía no basta. Debe poder señalar la condición, explicar las dos ramas y demostrar que ambas se han probado.

## S214 - Comunicar - README, evidencia y Site

### Objetivo de la sesión

El alumnado debe documentar H1, seleccionar evidencias verificables, preparar Sites y comprobar enlaces sin duplicar diario ni Scrum.

### Apertura docente

Di en voz alta:

> Hoy pasamos a Comunicar. Comunicar no es decorar al final. Comunicar significa que otra persona puede entender qué hicisteis, ejecutarlo, comprobar evidencias y ver qué aprendisteis.

### Scrum del día

Pide al alumnado:

> En Scrum, añadid tareas de cierre: `terminar README`, `seleccionar evidencia personal`, `actualizar Site personal`, `actualizar Site equipo`, `comprobar enlaces`, `preparar entrega Moodle`.

Entrega en esta sesión:

- Qué: tablero Scrum de cierre actualizado.
- Dónde: Sheet Scrum.

### Explicación docente

Di en voz alta:

> El README mínimo de H1 debe responder a cuatro preguntas: qué hace, qué límites tiene, cómo se ejecuta y qué ejemplo real demuestra que funciona. No debe prometer menú, memoria ni IA real si todavía no existen.

Estructura mínima:

```markdown
## Qué hace
MiniJarvis saluda y pide un nombre ficticio.

## Límites de H1
No incluye menú, memoria, ficheros ni IA real.

## Cómo ejecutar
1. Abre el proyecto.
2. Ejecuta Main.
3. Introduce datos ficticios.

## Ejemplo de ejecución
Entrada: Laura
Salida: Hola, Laura.
```

Di:

> Una evidencia debe demostrar algo. No vale un enlace a una carpeta general. Quiero entrada usada, salida observada, enlace profundo y explicación de qué demuestra.

### Investigación del alumnado

Pide al alumnado:

> Revisad vuestro propio material y localizad una evidencia fuerte y una evidencia débil. Investigad por qué una sirve para defender y la otra no.

Trabajo individual:

- Elegir evidencia para Site personal.
- Revisar diario.
- Comprobar que puede explicar su aportación.

Trabajo en equipo:

- Completar README.
- Actualizar Site de equipo.
- Preparar enlaces Moodle.

Trabajo por parejas:

- Una persona intenta seguir el README de otra sin explicación oral.

### Entrega de S214

Pide explícitamente, en este orden:

1. README H1.
2. Evidencia de ejecución.
3. Diario individual revisado.
4. Scrum de equipo actualizado.
5. Site personal H1 iniciado o terminado.
6. Site de equipo H1 iniciado o terminado.
7. Borrador de entrega Moodle con enlaces.

Dónde y cómo:

- README: raíz del repositorio GitHub.
- Evidencia de ejecución: README, repositorio o Drive con enlace profundo; debe indicar entrada, salida esperada, salida obtenida y qué demuestra.
- Diario individual: Sheet personal, no documento aparte.
- Scrum: Sheet de equipo.
- Site personal: página H1 del Site personal.
- Site de equipo: página H1 del Site de equipo.
- Moodle: todavía puede quedar como borrador si S215 es el cierre oficial, salvo que hayas configurado plazo de entrega en S214.

Di en voz alta:

> Hoy no quiero que copiéis el diario en el Site. Quiero que seleccionéis. El diario contiene proceso. El Site personal contiene evidencia seleccionada y explicación. El Site de equipo comunica el incremento. Moodle cerrará la entrega oficial.

### Comprobación de permisos

Pide al alumnado:

> Antes de decir que está entregado, comprobad permisos. Un enlace que solo abre el propietario no es una entrega válida.

Cómo comprobar:

- Abrir enlace en ventana privada o con cuenta no propietaria si es posible.
- Pedir a una pareja que abra el enlace.
- Confirmar que lleva al archivo o página concreta, no a la carpeta raíz.

### Cierre docente

Di en voz alta:

> Mañana o en la siguiente sesión defenderéis. Defender no es recitar el README. Defender es señalar, ejecutar, predecir, modificar una parte pequeña y explicar qué demuestra vuestra evidencia.

## S215 - Comunicar - Defensa y cierre H1

### Objetivo de la sesión

El alumnado debe defender individualmente, cerrar retrospectiva y realizar la entrega final en Moodle.

### Apertura docente

Di en voz alta:

> Hoy cerramos H1. La defensa no es un castigo ni una exposición larga. Es la comprobación de que entendéis vuestro propio producto. Vais a señalar código, explicar decisiones, ejecutar, predecir y, si hace falta, modificar algo pequeño.

### Scrum del día

Pide al alumnado:

> En Scrum, abrid la sección de review y retrospectiva. Durante la sesión vais a registrar qué incremento habéis conseguido, qué queda pendiente, qué bloqueo apareció y qué mejoraréis en H2.

Entrega en esta sesión:

- Qué: review y retrospectiva H1 de equipo.
- Dónde: Sheet Scrum de equipo.
- Cómo: texto breve y concreto, con evidencias enlazadas.

### Modelo de defensa

Di en voz alta:

> Una respuesta defendible tiene cuatro partes: señalo, explico, ejecuto y compruebo. Por ejemplo: `Esta línea lee el nombre`, `esta variable guarda el dato`, `si escribo Laura espero este saludo`, `lo ejecuto y compruebo que coincide`.

Preguntas de defensa que puedes usar:

- Señala dónde empieza la ejecución.
- Señala una variable y explica tipo, nombre y valor.
- Señala una constante y explica por qué es constante.
- Ejecuta con una entrada ficticia y predice la salida.
- Explica una conversión.
- Provoca o explica un error de conversión.
- Señala una comparación.
- Ejecuta un caso `true` y un caso `false`.
- Explica qué queda fuera de H1 y por qué.
- Cambia un mensaje o valor pequeño y predice el efecto.

### Organización de aula

Mientras haces defensas con algunas personas, el resto no espera sin tarea.

Pide al resto:

> Mientras hago defensas, los demás hacéis tres cosas: comprobáis enlaces, termináis retrospectiva y ensayáis por parejas una pregunta de defensa. Nadie está parado.

Trabajo individual:

- Defensa individual.
- Retrospectiva personal en diario.
- Comprobación de Site personal.

Trabajo por parejas:

- Ensayo de defensa.
- Revisión cruzada de enlaces.

Trabajo en equipo:

- Review y retrospectiva Scrum.
- Site de equipo.
- Entrega Moodle.

### Entrega final de S215

Pide explícitamente:

> Ahora sí, preparad y realizad la entrega oficial de H1 en Moodle. Recordad: si no está en Moodle, no está entregado oficialmente.

Dónde se entrega:

- Tarea Moodle de H1.

Cómo se entrega:

- Pegando enlaces profundos, no carpetas genéricas.
- Incluyendo al menos:
  - enlace al repositorio GitHub;
  - enlace al README H1 o repositorio con README visible;
  - enlace a la página H1 del Site personal;
  - enlace a la página H1 del Site de equipo;
  - enlace al Sheet Scrum del equipo o sección H1;
  - enlace a evidencia concreta de ejecución si Moodle lo solicita;
  - confirmación de permisos revisados.

Pide al alumnado que escriba en Moodle una mini declaración:

```text
Confirmo que los enlaces llevan a evidencias concretas de H1 y que he comprobado los permisos de acceso.
```

Si Moodle permite texto de entrega, pide este formato:

```text
Equipo:
Integrantes:

Repositorio GitHub:
README H1:
Site personal H1:
Site equipo H1:
Scrum equipo H1:
Evidencia de ejecución:

Permisos comprobados: sí/no
Observaciones o bloqueo pendiente:
```

### Diario individual final

Pide explícitamente:

> Cada persona escribe ahora la última entrada de diario de H1. Debe incluir: una cosa que ya puede hacer sola, una cosa que todavía necesita apoyo, una evidencia que lo demuestra y un siguiente paso para H2.

Dónde y cómo:

- Diario individual en Sheets.
- Una fila final S215.
- No hacer documento separado.

### Retrospectiva de equipo

Pide explícitamente:

> En equipo, cerrad retrospectiva H1 con cuatro frases: qué funcionó, qué no funcionó, qué mantendremos en H2 y qué cambiaremos en H2.

Dónde y cómo:

- Sheet Scrum de equipo, sección retrospectiva.
- Enlace desde Moodle si la tarea lo pide.

### Si alguien no puede defender

Di en voz alta:

> Si aparece una laguna, no se repite todo H1. Se recupera la evidencia concreta: investiga, corrige, prueba y vuelve a explicar. Lo importante es localizar qué falta.

Registra tú:

- persona;
- evidencia pendiente;
- concepto no defendido;
- recuperación concreta;
- fecha o momento de revisión.

### Cierre final de H1

Di en voz alta:

> H1 queda cerrado cuando existe producto, pruebas, documentación, reflexión y entrega oficial. Hemos pasado por todo HEXA: activamos el reto, investigamos Java básico, ideamos la salida, planificamos datos, ejecutamos código y comunicamos evidencias. En H2 evolucionaremos esto hacia decisiones más completas, comandos, repetición, pruebas y depuración.

## Lista rápida de comprobación docente H1

Antes de cerrar H1, comprueba:

- Cada equipo tiene repositorio accesible.
- Cada equipo tiene README H1.
- Cada equipo tiene Scrum con backlog, decisiones, review y retrospectiva.
- Cada persona tiene diario con entradas relevantes.
- Cada persona puede defender al menos una parte técnica.
- Existe Site personal H1 o página H1 actualizada.
- Existe Site de equipo H1 o página H1 actualizada.
- Moodle contiene enlaces profundos.
- Los permisos funcionan.
- No hay datos personales reales ni credenciales.
- No se ha convertido H1 en H2 con menús, bucles o funciones fuera de alcance.

## Frases útiles para gestionar aula

Cuando copian sin entender:

> Para un momento. No quiero que borres y pegues otra cosa. Quiero que señales qué línea entiendes, cuál no y qué predices que hará.

Cuando dicen `funciona`:

> `Funciona` no es una evidencia. Dime qué entrada usaste, qué salida esperabas, qué salió y dónde puedo comprobarlo.

Cuando quieren hacer más de la cuenta:

> Esa idea puede ser buena, pero no pertenece a H1. La registramos como más adelante y protegemos el alcance actual.

Cuando no saben qué escribir en diario:

> Escribe una frase para cada punto: objetivo, acción, prueba, resultado y siguiente paso. Si hubo bloqueo, escríbelo. Si usaste IA, escribe qué preguntaste y cómo validaste.

Cuando el equipo no actualiza Scrum:

> Si la tarea solo está en vuestra cabeza, el equipo no la puede gestionar. Escribidla en Scrum con estado y responsable.

Cuando entregan enlaces generales:

> Este enlace abre una carpeta, no una evidencia. Necesito el enlace profundo al archivo, página, README o prueba concreta.

Cuando una defensa es vaga:

> Vuelve al código. Señala una línea, explica qué dato maneja, ejecútala y comprueba el resultado.

## Qué no debes hacer en H1

- No des una solución completa para copiar.
- No aceptes evidencias sin explicación.
- No conviertas el Site en copia del diario.
- No conviertas Moodle en almacén duplicado de todo.
- No pidas informes extra si el diario, Scrum, GitHub, Sites y Moodle ya cubren la evidencia.
- No metas contenidos fuertes de H2 por adelantar.
- No evalúes solo que compile.
- No permitas código que la persona no pueda explicar.

## Resumen de entregas por sesión

| Sesión | Qué se pide | Dónde se entrega | Cómo se entrega | Moodle |
|---|---|---|---|---|
| S206 | Alcance H1, límites, backlog inicial, diario inicial | Scrum y diario | Texto breve con tareas, decisiones y siguiente paso | No todavía |
| S207 | Primera ejecución | GitHub/Drive, diario, Scrum | Código + salida + frase explicativa | No todavía |
| S208 | Estructura mínima y error corregido | GitHub, diario, Scrum | Código + regla sintáctica + corrección | No todavía |
| S209 | Decisión de mensajes | Scrum, GitHub, diario si procede | Alternativas, decisión, código ejecutado | No todavía |
| S210 | Plan de datos y variables | Scrum/documento enlazado, GitHub, diario | Tabla de datos + código + microdefensa | No todavía |
| S211 | Constante, operación y predicción | GitHub, diario, Scrum | Código + predicción + resultado | No todavía |
| S212 | Entrada y conversión | GitHub, diario, Scrum | Entrada válida, resultado y error de conversión | No todavía |
| S213 | Comparación e if/else con dos ramas | GitHub, diario, Scrum | Caso true, caso false y mejora | No todavía |
| S214 | README, evidencias, Sites, enlaces | GitHub, diario, Scrum, Sites | README + evidencias profundas + permisos | Borrador o entrega si se decide |
| S215 | Defensa, retrospectiva y entrega final | Moodle, diario, Scrum, Sites, GitHub | Enlaces profundos, defensa y cierre | Sí, entrega oficial |

## Cierre para el profesor

Si en algún momento dudas, vuelve a estas tres preguntas:

- Qué debe aprender hoy el alumnado.
- Qué evidencia concreta lo demuestra.
- Dónde queda esa evidencia sin duplicarla.

Si puedes responder a esas tres preguntas, la sesión está bien orientada.
