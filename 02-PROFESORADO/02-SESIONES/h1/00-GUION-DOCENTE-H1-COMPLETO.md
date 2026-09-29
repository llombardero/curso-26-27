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
- enlaces a evidencias solo cuando ayuden a gestionar una tarea, decisión o bloqueo real;
- review y retrospectiva final.

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

- Moodle: una única entrega oficial de H1 en S215; S206-S213 no generan entregas Moodle individuales y S214 prepara el cierre.
- GitHub: código, README, historial y microprácticas si se guardan como archivos.
- Diario individual en Sheets: aprendizaje individual significativo, como un error relevante, un bloqueo, una decisión personal, una diferencia entre predicción y resultado, un uso relevante de IA o un siguiente paso especialmente significativo. No se completa una fila por sesión.
- Scrum de equipo en Sheets: backlog, tareas reales, estados, decisiones, cambios, bloqueos, review y retrospectiva. No se actualiza solo porque termine una sesión.
- Drive: solo evidencia no-code excepcional que no tenga una fuente más natural, siempre con enlaces profundos.
- Portfolio: el aprendizaje individual y el incremento de H1 podrán seleccionarse posteriormente durante C1. No se crea ahora una página Site H1 obligatoria.

Regla que debes repetir muchas veces:

> Una evidencia no es una captura suelta ni una carpeta general. Una evidencia debe permitir comprobar algo: qué entrada se usó, qué salida se obtuvo, dónde está el código o documento y qué demuestra.

## Rutina fija para cada sesión

Usa esta rutina aunque la sesión cambie de contenido.

1. Abre con el objetivo en lenguaje sencillo.
2. Recuerda la fase HEXA del día.
3. Haz una revisión Scrum de dos minutos.
4. Explica solo lo necesario para desbloquear la práctica.
5. Pide predicción antes de ejecutar código.
6. Haz trabajar individualmente cuando la comprensión deba ser personal.
7. Haz contrastar por parejas cuando convenga detectar errores.
8. Haz trabajar en equipo cuando haya decisión, backlog, README o reparto.
9. Pide evidencia concreta.
10. Cierra conservando solo la evidencia que corresponda: técnica en GitHub/README, aprendizaje individual significativo en el diario y trabajo real de equipo en Scrum.

Di en voz alta cuando haya código:

> Antes de ejecutar, escribe o di qué esperas que ocurra. Programar no es pulsar ejecutar hasta que algo salga. Programar es predecir, ejecutar, comparar y corregir.

Cuando utilices un ejemplo técnico, sigue esta secuencia breve:

1. Proyecta el ejemplo.
2. Pide una predicción antes de ejecutar.
3. Ejecuta o simula el resultado.
4. Pide explicar qué ha ocurrido.
5. Cambia un único elemento.
6. Vuelve a pedir predicción.

Puedes convertir cualquier ejemplo en una de estas tarjetas rápidas de aula: proyecta y predice, error para localizar, modifica una línea, microdefensa, contraste de alternativas o traza del valor paso a paso.

## S206 - Activar - Presentar H1 y delimitar alcance

**Modalidad:** **INDIVIDUAL → EQUIPO**

### Objetivo de la sesión

El alumnado debe entender qué es H1, qué entra, qué no entra y cómo se demostrará el avance.

### Antes de empezar

Ten abierta la presentación S206 y localizable el Sheet Scrum de los equipos.

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

Organización del trabajo:

- Qué: primeras tareas de backlog H1 y roles provisionales.
- Cuándo: durante los primeros 10 minutos.
- Dónde: Sheet Scrum del equipo.
- Cómo: filas concretas con tarea, responsable o pareja responsable, estado inicial y sesión S206.

### Explicación docente

Di en voz alta:

> H1 entra dentro del Tema 1. Vamos a tocar entorno, estructura básica de Java, salida por pantalla, variables, constantes, operaciones, entrada con Scanner, conversiones y una decisión sencilla. Pero no todo tiene que estar metido en el mismo `Main.java`. Algunas cosas serán microprácticas para aprender y defender.

Di en voz alta:

> En H1 sí entra: saludo, mensajes por consola, variables, constantes, entrada y salida, operaciones sencillas, comparación, una decisión básica y explicación. En H1 no entra: menús, bucles, memoria, ficheros, clases complejas, persistencia ni IA real. Eso llegará más adelante.

### Explicación guiada: alcance y calidad de H1

Úsala ahora, antes de que clasifiquen qué entra y qué queda fuera.

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

### Registro del trabajo de S206

Pide explícitamente:

> Antes de terminar, cada equipo debe dejar en Scrum tres cosas: frase de alcance H1, lista breve de lo que entra y lista breve de lo que queda fuera.

Dónde y cómo:

- Scrum de equipo: sección de decisiones o backlog.
- Formato: texto breve, fechado como S206.
- No aceptar: frases como `hacer que funcione` sin comprobar.

Modelo de uso del Scrum en S206:

```text
Backlog H1 - Equipo Ada

Tarea: Definir alcance H1
Responsable: equipo completo
Estado: hecho
Evidencia: decisión S206 en Scrum

Decisión S206:
En H1 entra saludo, entrada/salida, variables, constantes, una operación y una decisión sencilla.
Queda fuera menú, memoria, ficheros e IA real.
```

Modelo que no debes aceptar:

```text
Tarea: hacer Java
Responsable: todos
Estado: más o menos
```

El alcance y las decisiones del equipo ya quedan en Scrum. No pidas una entrada individual por haber terminado S206. El diario solo se utiliza si una persona necesita conservar un aprendizaje, una duda, un bloqueo o una decisión individual significativa.

### Cierre docente

Di en voz alta:

> Cerramos Activar. Para avanzar, cada equipo debe poder explicar qué va a construir y qué no va a construir. Mañana o en la siguiente sesión investigaremos cómo se pasa de escribir código a verlo ejecutarse en consola.

## S207 - Investigar - Entorno Java, IntelliJ, proyecto y ejecución

**Modalidad:** **INDIVIDUAL → PAREJAS**

### Objetivo de la sesión

El alumnado debe comprender el camino `código fuente -> compilación -> ejecución -> consola` y lograr una primera ejecución.

### Apertura docente

Di en voz alta:

> Hoy estamos en Investigar. Investigar no significa buscar cualquier cosa en Google. Significa aprender lo imprescindible para poder construir H1. Hoy necesitamos entender qué ocurre entre escribir `Main.java` y ver un mensaje en la consola.

### Scrum del día

Pide al alumnado:

> Equipos, abrid Scrum y añadid o actualizad estas tareas si forman parte de vuestro trabajo real: `crear o abrir proyecto Java`, `localizar Main.java` y `ejecutar primer mensaje`.

Organización del trabajo:

- Qué: tareas técnicas iniciales actualizadas.
- Cuándo: primeros 5 minutos.
- Dónde: Sheet Scrum del equipo.
- Cómo: estado claro de cada tarea.

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

### Explicación guiada: del código a la consola

Úsala antes de la primera ejecución y repítela cuando aparezca el primer error.

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

### Evidencia técnica de S207

Pide explícitamente:

> Dejad localizable en GitHub el código de la primera ejecución. Antes de darla por válida, ejecutadlo y explicad oralmente a vuestra pareja cómo sabéis que se ha ejecutado.

Dónde y cómo:

- GitHub: código del primer `Main.java`.
- Comprobación reproducible: ejecutar el código y contrastar la salida con la predicción.
- Scrum de equipo: marcar la tarea `primera ejecución` como hecha o bloqueada.

Modelo de uso de GitHub/evidencia en S207:

```text
Repositorio: minijarvis-h1
Archivo: src/Main.java
Commit útil: S207: primera ejecución por consola
Evidencia: código con System.out.println y salida visible en consola.
```

Modelo de commit poco útil:

```text
cambios
```

Qué no aceptar:

- Una imagen aislada de la consola sin código reproducible.
- Frase `funciona` sin explicación.

### Cierre docente

Di en voz alta:

> Hoy no hemos aprendido solo a pulsar ejecutar. Hemos aprendido el recorrido: escribir, compilar, ejecutar y observar. Si algo falla, primero leemos el error y formulamos una hipótesis.

## S208 - Investigar - Estructura mínima de un programa Java

**Modalidad:** **INDIVIDUAL → PAREJAS → comprobación INDIVIDUAL**

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

### Explicación guiada: clase, archivo, escritura precisa, nombres y comentarios

Usa esta explicación como una secuencia breve de ejemplos. No la conviertas en teoría larga: proyecta, pide predicción, corrige y haz que señalen el elemento exacto.

Di en voz alta:

> En estos primeros programas, el archivo se llama `Main.java`, la clase pública se llama `Main` y el método `main` es el punto de entrada. Java distingue mayúsculas y necesita delimitadores: punto y coma, llaves, paréntesis y comillas.

Ejemplo para proyectar:

```java
public class Main {
    public static void main(String[] args) {
        System.out.println("Hola");
    }
}
```

Pregunta al alumnado:

> Señala clase, punto de entrada, una instrucción visible, un identificador y un comentario útil.

Error frecuente que debes cortar:

> `String` no es `string`. `Main` no es `main`. Las mayúsculas importan.

Contrasta ahora la relación archivo-clase con este caso:

```java
// Archivo: Main.java
public class MiniJarvis {
    public static void main(String[] args) {
        System.out.println("Hola");
    }
}
```

Pregunta:

> Qué relación no se cumple aquí.

Respuesta esperada:

```text
Main.java no coincide con public class MiniJarvis.
```

Aclara la diferencia entre `Main` y `main`:

```java
public class Main {
    public static void main(String[] args) {
        System.out.println("MiniJarvis");
    }
}
```

Di:

> `Main` es el nombre de la clase. `main` es el método donde comienza la ejecución.

Haz una predicción de orden:

```java
public class Main {
    public static void main(String[] args) {
        System.out.println("UNO");
        System.out.println("DOS");
    }
}
```

Pregunta:

> Aparecerá primero UNO o DOS. Explica por qué.

Trabaja errores de escritura sin ejecutar primero:

```java
public static void main(string[] args) {
    System.out.println("Hola");
}
```

```java
System.out.println("Hola")
System.out.println("MiniJarvis");
```

```java
System.out.println("Hola);
```

```java
System.out.println("Hola";
```

```java
public class Main {
    public static void main(String[] args) {
        System.out.println("Hola");
}
```

Pide para cada caso:

> Localiza el error, di qué delimitador o escritura falla y predice si compila.

Después clasifica nombres. Proyecta solo los nombres, no el código completo:

```text
userName       válido y claro
studyHours     válido y claro
assistantName  válido y claro
x              válido pero pobre
a              válido pero pobre
dato           válido pero pobre
cosa           válido pero pobre
1name          no válido
name1          válido
study hours    no válido
studyHours     válido
class          no válido
public         no válido
className      válido
```

Pregunta:

> Sin ver el resto del programa, qué esperas que almacene cada nombre. Si nadie puede responder, probablemente el nombre sea mejorable.

Termina con comentarios útiles. Contrasta:

```java
// Muestra Hola
System.out.println("Hola");
```

```java
// Primer mensaje que identifica al asistente
System.out.println("Hola, soy MiniJarvis");
```

```java
// Declara studyHours
int studyHours = 4;

// Valor inicial usado en la demostración
int practiceHours = 4;
```

```java
/*
 * Primera versión de MiniJarvis.
 * De momento solo muestra mensajes por consola.
 */
```

Di:

> Un comentario útil explica intención o contexto. Un comentario pobre repite lo que ya se lee en la instrucción.

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

### Evidencia técnica y comprobación de S208

Pide explícitamente:

> Antes de terminar, cada persona debe poder mostrar la estructura mínima funcionando y explicar el error que ha provocado y corregido.

Dónde y cómo:

- GitHub: código actualizado o micropráctica de estructura.
- Diario individual: solo si el error ha producido un aprendizaje significativo que la persona necesite conservar.
- Scrum: si el error revela una decisión o un bloqueo real del equipo, registrarlo donde corresponda.

Qué debe contener la evidencia:

- Código con estructura mínima.
- Salida observada.
- Explicación de una regla sintáctica.

Modelo de uso de evidencia S208:

```text
Archivo: practicas-h1/S208-estructura-minima.java
Prueba: estructura mínima ejecutada con dos mensajes.
Error provocado: escribí string en lugar de String.
Hipótesis: Java distingue mayúsculas.
Corrección: cambié string por String.
Resultado: compila y muestra los mensajes esperados.
```

### Cierre docente

Di en voz alta:

> Para cerrar S208, cada persona debe poder señalar dónde empieza la ejecución, qué instrucción muestra texto y una regla cuya ruptura impide compilar.

## S209 - Idear - Salida por pantalla y mensajes del asistente

**Modalidad:** **PAREJAS → EQUIPO**

### Objetivo de la sesión

El alumnado debe idear mensajes claros antes de programarlos y usar literales y concatenación cuando sea necesario.

### Apertura docente

Di en voz alta:

> Hoy cambiamos de fase: Idear. Idear significa proponer soluciones antes de construir. La consola también es una interfaz. Si MiniJarvis escribe mensajes confusos, el programa puede compilar, pero la experiencia será mala.

### Scrum del día

Pide al alumnado:

> En Scrum, añadid una tarea de equipo: `decidir mensajes de H1`. Esa tarea no está hecha hasta que tengáis al menos dos alternativas y una razón para elegir una.

Organización del trabajo:

- Qué: decisión de mensajes de consola.
- Dónde: Sheet Scrum, sección decisiones o backlog.
- Cómo: alternativa elegida, alternativa descartada y motivo.

### Explicación docente

Di en voz alta:

> `System.out.println` no solo sirve para sacar texto. Sirve para comunicarse con la persona que ejecuta el programa. Un buen mensaje dice qué ocurre, qué se pide y qué resultado se obtiene. Además, si queremos mezclar texto fijo con datos, usamos concatenación.

### Explicación guiada: la consola como interfaz y concatenación

Úsala antes de abrir el IDE, para obligar a idear la salida.

Di en voz alta:

> La consola también es una interfaz. Aunque sea texto, la persona usuaria debe entender qué ocurre, qué se le pide y qué resultado obtiene. Además, no debemos prometer funciones que H1 no tiene.

Compara estos mensajes con el alumnado:

```text
ok
```

Frente a:

```text
MiniJarvis se ha iniciado correctamente.
```

```text
Dato:
```

Frente a:

```text
Escribe tu nombre:
```

```text
5
```

Frente a:

```text
Horas de estudio registradas: 5
```

```text
String userName initialized successfully.
```

Frente a:

```text
Hola, Laura.
```

```text
Analizando tus datos con inteligencia artificial...
```

Frente a:

```text
Hola, soy MiniJarvis. Esta es mi primera versión por consola.
```

Pregunta al alumnado:

> Qué salida ayuda más, qué dato cambia y dónde hacen falta espacios o signos.

Error frecuente que debes cortar:

> No escribáis `Puedo recordar todo` si H1 no tiene memoria.

Di también:

> El mensaje debe estar pensado para quien usa el programa, no para demostrarle que sabemos Java.

Trabaja ahora literal de texto y concatenación con predicción:

```java
System.out.println("Hola");
```

Pregunta:

> Qué parte ha escrito exactamente quien programa.

```java
String userName = "Laura";
System.out.println("Hola, " + userName);
```

Salida esperada:

```text
Hola, Laura
```

```java
String userName = "Laura";
String assistantName = "MiniJarvis";
System.out.println("Hola, " + userName + ". Soy " + assistantName + ".");
```

```java
int studyHours = 4;
System.out.println("Has estudiado " + studyHours + " horas.");
```

Predicción obligatoria:

```java
System.out.println(2 + 3);
System.out.println("Resultado: " + 2 + 3);
```

Pregunta:

> Predice ambas salidas antes de ejecutar y explica por qué el signo `+` no se comporta igual en las dos líneas.

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

### Conservación del trabajo de S209

Pide explícitamente:

> Registrad la decisión de diseño de mensajes y guardad la versión programada.

Dónde y cómo:

- Scrum de equipo: decisión de mensajes con motivo.
- GitHub: código con mensajes implementados.
- Diario individual: solo si cambiar o defender la decisión ha producido un aprendizaje individual significativo.

Qué debe aparecer:

- Mensaje elegido.
- Por qué se elige.
- Qué se cambió después de verlo ejecutado.

Modelo de uso de decisión de mensajes:

```text
Decisión S209:
Elegimos "Hola, soy MiniJarvis" y "Escribe un nombre ficticio" porque son claros y no piden datos personales reales.
Descartamos "MJ v1 ok" porque no explica qué ocurre.
Después de ejecutar añadimos un punto final y un espacio tras la coma para mejorar la lectura.
```

### Cierre docente

Di en voz alta:

> Hemos ideado antes de programar. Esa es la clave de hoy. La salida de consola no se improvisa al final: se diseña para que alguien entienda qué ocurre.

## S210 - Planificar - Variables

**Modalidad:** **INDIVIDUAL → EQUIPO → comprobación INDIVIDUAL**

### Objetivo de la sesión

El alumnado debe planificar datos: qué se guarda, con qué tipo, con qué nombre y dónde se usa.

### Apertura docente

Di en voz alta:

> Hoy estamos en Planificar. Planificar en programación significa decidir antes de escribir código qué datos necesitamos, qué tipo tienen y cómo se llaman. Si programamos sin plan de datos, acabamos con nombres vagos, valores repetidos y errores difíciles de explicar.

### Scrum del día

Pide al alumnado:

> Si `planificar datos de H1` es una tarea real del equipo, creadla o actualizadla en Scrum y no la marquéis como hecha hasta tener una tabla con dato, tipo, nombre, si cambia y dónde se usa.

Dónde queda el plan:

- En la propia planificación o junto al código, donde resulte técnicamente útil.
- En Scrum solo queda la tarea, decisión, cambio o bloqueo real; no se crea un documento paralelo por obligación.
- La tabla incluye dato, tipo, nombre, cambia sí/no y uso.

### Explicación docente

Di en voz alta:

> Una variable es una zona de memoria con nombre que guarda un dato. El tipo indica qué clase de dato puede guardar. El nombre debe ayudar a entender para qué sirve. En Java, declarar, inicializar y asignar no son exactamente lo mismo.

### Explicación guiada: variable, tipo, nombre y asignación

Úsala antes de la tabla de datos y antes de implementar variables.

Di en voz alta:

> Una variable es una zona de memoria identificada por un nombre. El tipo indica qué clase de dato puede guardar. El valor puede cambiar. La variable no es lo mismo que su valor actual.

Empieza con el cambio de valor:

```java
int studyHours = 4;
studyHours = 5;
```

Di:

> La variable permanece; lo que cambia es el valor guardado. Primero `studyHours` vale 4 y después vale 5.

Contrasta variable y valor:

```java
String userName = "Laura";
```

Pregunta:

> Qué es `userName` y qué es `"Laura"`.

Muestra dos variables con el mismo valor:

```java
int studyHours = 4;
int practiceHours = 4;
```

Pregunta:

> Hay una variable o dos. Qué pasaría si después cambia solo `studyHours`.

Traza una variable que cambia:

```java
int tasks = 2;
System.out.println(tasks);
tasks = 3;
System.out.println(tasks);
```

Pregunta:

> Predice la primera y la segunda salida.

Presenta cinco tipos de uso inmediato:

```java
String userName = "Laura";
int studyHours = 4;
double averageScore = 7.5;
boolean goalReached = true;
char initial = 'L';
```

Pide completar oralmente:

```text
Nombre -> String
Horas de estudio -> int
Nota media -> double
Objetivo alcanzado -> boolean
Inicial -> char
```

### Microexplicación: mapa mínimo de tipos de Java

No conviertas este momento en una tabla para memorizar. El objetivo es que el alumnado reconozca que Java ofrece varios tipos y que en H1 usaremos solo los más útiles para el reto.

Proyecta:

```text
TIPOS PRIMITIVOS

Enteros      -> byte, short, int, long
Decimales    -> float, double
Carácter     -> char
Lógico       -> boolean

En H1 usaremos principalmente:
int, double, char y boolean.
```

Di en voz alta:

> No tenéis que memorizar ahora rangos ni tamaños. Lo importante es reconocer que existen varios tipos y elegir uno coherente con el dato y con las operaciones que necesitaremos hacer.

Haz una comprobación rápida:

> Si quiero guardar una edad, una nota media, una inicial y si una tarea está terminada, qué tipo elegiríais para cada dato.

### Microexplicación: tipo primitivo y tipo referencia

Añade después:

```text
int, double, char, boolean -> tipos primitivos
String                     -> tipo referencia; String es una clase
```

Di en voz alta:

> En H1 nos basta con distinguir dos ideas. Los tipos como `int`, `double`, `char` o `boolean` son primitivos. `String`, en cambio, no es un tipo primitivo: es una clase que Java nos ofrece para trabajar con texto. En el tema siguiente entenderemos mejor qué significa trabajar con objetos y referencias.

No profundices todavía en memoria, identidad de objetos ni constructores. La finalidad de esta distinción es preparar el uso de `String`, `Scanner` y las comparaciones posteriores sin adelantar RA2.

Pregunta de criterio:

> Un número de teléfono contiene dígitos. Lo guardarías como número si no vas a hacer cálculos matemáticos con él.

Trabaja renombrado:

```java
int x = 4;
// mejor:
int studyHours = 4;

String s = "MiniJarvis";
// mejor:
String assistantName = "MiniJarvis";

boolean b = true;
// mejor:
boolean goalReached = true;

double n = 7.5;
// mejor:
double averageScore = 7.5;
```

Dinámica rápida:

> Muestro solo el nombre de la variable. Decid qué dato esperáis encontrar. Si nadie puede responder, el nombre debe mejorar.

Por último, separa declarar, inicializar y asignar:

```java
int studyHours;
```

```java
int studyHours = 4;
```

```text
int studyHours = 4
tipo nombre valor inicial
```

```java
studyHours = 5;
```

```java
int studyHours;
studyHours = 4;
System.out.println(studyHours);
studyHours = 5;
System.out.println(studyHours);
```

Aclara:

> No se vuelve a escribir el tipo si se modifica la variable existente.

Y corta esta confusión:

```java
int tasks = 2;
tasks = 5;
```

Di:

> Esto no significa que 2 sea igual a 5. Significa: guarda ahora 5 en `tasks`.

Error frecuente que debes cortar:

> `String` no sirve para todo. Elegimos el tipo según lo que necesitamos representar y hacer con el dato.

### Comprender, predecir y practicar — INDIVIDUAL

Pide al alumnado:

> Individualmente, clasificad estos datos: nombre de usuario, horas de estudio, nota media, objetivo alcanzado e inicial. Decid qué tipo usaríais y por qué.

Cada persona:

- elige tipos;
- propone nombres significativos;
- razona qué representa cada dato, qué valor inicial podría tener y si cambiará;
- realiza una micropráctica propia: declara e inicializa al menos una variable, predice qué ocurrirá al reasignarla, modifica su valor, ejecuta y compara el resultado con su predicción.

La micropráctica garantiza práctica individual antes de integrar en equipo. No es un nuevo entregable y no obliga a crear una entrada de diario.

### Contrastar y planificar — EQUIPO

El equipo compara las propuestas individuales, corrige nombres vagos y acuerda el plan de datos. Antes del código, completa la tabla con dato, tipo, nombre, valor inicial, si cambia y dónde se usa.

El plan queda en la propia planificación de trabajo o junto al código cuando resulte técnicamente útil. Solo se registra en Scrum si corresponde a una tarea, decisión, cambio o bloqueo real; no necesita un documento paralelo.

### Integrar en MiniJarvis — EQUIPO

Pide al alumnado:

> Después del plan de datos, implementad al menos tres variables en el incremento compartido, usadlas realmente, mostradlas por consola cuando proceda, cambiad una y volved a mostrarla para comprobar que entendéis la asignación.

El código y su evolución técnica quedan en GitHub.

### Comprobar comprensión — INDIVIDUAL

Pide explícitamente:

> Cada persona debe poder señalar una variable del incremento compartido y explicar tipo, nombre, valor inicial y una asignación posterior. Si se solicita, debe modificarla, predecir el efecto, ejecutar y comprobar el resultado.

Esta comprobación es individual, pero no genera una evidencia administrativa adicional. El diario solo se utiliza si la práctica ha producido un aprendizaje, error, bloqueo, decisión o siguiente paso significativo.

Qué revisar:

- Que no usen `x`, `dato1` o nombres sin significado.
- Que no repitan valores fijos por todas partes.
- Que sepan distinguir variable y valor.

Modelo de uso del plan de datos:

```text
Dato: nombre ficticio
Tipo: String
Nombre: userName
Cambia: sí, lo escribe la persona usuaria
Uso: personalizar el saludo

Dato: horas de estudio
Tipo: int
Nombre: studyHours
Cambia: sí
Uso: calcular minutos y decidir si alcanza el objetivo
```

### Cierre docente

Di en voz alta:

> Cerramos Planificar con un plan de datos. La próxima sesión entraremos más fuerte en Ejecutar: constantes, literales y operaciones.

## S211 - Ejecutar - Constantes, literales y operaciones

**Modalidad:** **INDIVIDUAL → PAREJAS**

### Objetivo de la sesión

El alumnado debe usar constantes, literales y operaciones aritméticas con predicción y prueba.

### Apertura docente

Di en voz alta:

> Hoy entramos en Ejecutar. Ejecutar no significa escribir mucho código sin pensar. Significa construir, probar y mejorar. Hoy cada operación debe ir acompañada de una predicción y una comprobación.

### Scrum del día

Pide al alumnado:

> En Scrum, cread o actualizad tareas como `añadir constante`, `añadir operación` o `probar resultado` solo cuando representen trabajo real del equipo. Un error o aprendizaje individual no se convierte automáticamente en tarea Scrum.

Dónde y cómo:

- Sheet Scrum.
- Estado por tarea.
- Bloqueo si no entienden división entera, `%` o precedencia.

### Explicación docente

Di en voz alta:

> Una constante es un dato que no debe cambiar durante la ejecución. En Java usamos `final`. Un literal es un valor escrito directamente en el código, como `5`, `3.5`, `"Hola"`, `'A'`, `true` o `false`. Una operación produce un resultado; si queremos usarlo, debemos mostrarlo o guardarlo.

### Explicación guiada: constantes, literales, operaciones, resto y actualización

Úsala antes de introducir `final`, división entera, `%` y actualización.

Di en voz alta:

> Una constante representa un dato que no debe cambiar durante la ejecución. Un literal es un valor escrito directamente. Una operación produce un resultado, pero ese resultado se pierde si no lo guardamos, mostramos o usamos.

Empieza con constantes y variables:

```java
final String ASSISTANT_NAME = "MiniJarvis";
final int START_YEAR = 2026;
```

Pregunta al alumnado:

> Esperamos que estos datos cambien durante la ejecución.

Contrasta constante y variable:

```java
final String ASSISTANT_NAME = "MiniJarvis";
int studyHours = 3;
studyHours = 4;
```

Aclara:

> Un dato puede empezar siempre igual y no ser constante si está pensado para cambiar.

```java
int tasks = 0;
```

Presenta literales:

```text
5
3.5
"Hola"
'A'
true
false
```

Clasifica con ejemplos:

```java
int hours = 5;
double score = 7.5;
String message = "Hola";
char initial = 'L';
boolean finished = false;
```

Pregunta:

> Qué diferencia hay entre `'L'` y `"L"`.

### Microexplicación: una expresión produce un resultado

Antes de seguir con las operaciones, fija explícitamente la palabra `expresión`.

Proyecta:

```java
3 + 2
hours * 60
hours >= 4
hasName && hasGoal
"Hola, " + userName
```

Di en voz alta:

> Una expresión combina valores, variables u operadores y produce un resultado. Ese resultado también tiene un tipo. Entender qué resultado produce una expresión será más importante que memorizar símbolos.

Relaciona cada expresión con su resultado:

```text
3 + 2                    -> int
5 / 2.0                  -> double
hours >= 4               -> boolean
"Hola, " + userName      -> String
```

Pregunta:

> Antes de ejecutar, qué valor y qué tipo esperas que produzca cada expresión.

Trabaja operaciones aritméticas:

```java
int totalHours = 3 + 2;
```

```java
int days = 5;
int hoursPerDay = 2;
int totalHours = days * hoursPerDay;
```

```java
int minutes = 4 * 60;
System.out.println(minutes);
```

Contrasta con resultado ignorado:

```java
4 * 60;
```

Pregunta:

> Dónde queda guardado el resultado para utilizarlo después.

Predice división entera y real:

```java
int a = 5 / 2;
double b = 5 / 2.0;
```

Pregunta:

> Qué vale `a` y qué vale `b`.

### Micropráctica: precedencia y paréntesis

No pidas memorizar una tabla completa de precedencia. Trabaja solo la idea de que Java no siempre evalúa de izquierda a derecha y que los paréntesis permiten hacer explícito el orden que queremos.

Proyecta y pide predicción antes de ejecutar:

```java
int a = 2 + 3 * 4;
int b = (2 + 3) * 4;
```

Pregunta:

> Cuánto vale `a`, cuánto vale `b` y qué han cambiado los paréntesis.

Después añade:

```java
double result = 10 + 6 / 2.0;
```

Pide que expliquen qué operación se realiza primero.

Di en voz alta:

> Cuando varias operaciones aparecen en una expresión, existe un orden de precedencia. No necesitamos memorizar hoy toda la tabla. Sí necesitamos predecir el resultado y usar paréntesis cuando queramos hacer explícito el orden y mejorar la lectura.

Regla práctica para H1:

> Si dudas del orden o quien lee el código puede dudar, usa paréntesis y comprueba el resultado con una predicción.

Explica `%` como resto, no como porcentaje:

```text
10 / 4 -> 2
10 % 4 -> 2

8 % 2 -> 0
9 % 2 -> 1

17 / 5 -> 3
17 % 5 -> 2
```

Di:

> Diez caramelos entre cuatro personas: dos para cada una y sobran dos. `%` expresa lo que sobra.

Termina con actualización:

```java
int tasks = 3;
tasks = tasks + 2;
tasks += 2;
tasks -= 1;
tasks++;
tasks--;
```

Traza paso a paso:

```java
int tasks = 2;
tasks += 3;
tasks--;
tasks++;
```

Resultado esperado:

```text
2 -> 5 -> 4 -> 5
```

Error frecuente que debes cortar:

> `5 / 2` con enteros da `2`, no `2.5`.

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

### Evidencia técnica y reflexión de S211

Pide explícitamente:

> Conservad en GitHub la micropráctica o el código integrado y explicad una predicción que haya sido confirmada o corregida.

Dónde y cómo:

- GitHub: código de micropráctica o `Main.java` actualizado.
- Diario individual: solo si la diferencia entre predicción y resultado ha producido un aprendizaje significativo.
- Scrum: actualizar únicamente tareas reales de constante, operación o prueba.

Qué debe contener:

- Uso de `final`.
- Una operación comprobable.
- Evidencia de resultado.

Modelo de uso de predicción S211:

```text
Predicción: si hours vale 5, minutes será 300.
Código probado: int minutes = hours * 60;
Resultado observado: la consola muestra 300.
Explicación: la operación multiplica horas por 60 y guarda el resultado.
```

### Cierre docente

Di en voz alta:

> Una operación no está demostrada porque el código compile. Está demostrada cuando puedo predecir el resultado, ejecutarlo y explicar si coincide.

## S212 - Ejecutar - Scanner y conversiones

**Modalidad:** **INDIVIDUAL → PAREJAS**

### Objetivo de la sesión

El alumnado debe leer entrada, guardarla, convertir texto a número cuando haga falta y reconocer errores de conversión.

### Apertura docente

Di en voz alta:

> Hasta ahora muchos datos los decidía quien programaba. Hoy MiniJarvis empezará a recibir datos de quien lo ejecuta. Eso cambia el programa: necesitamos pedir, leer, guardar, convertir si hace falta, calcular y mostrar.

### Scrum del día

Pide al alumnado:

> En Scrum, añadid tareas: `leer nombre ficticio`, `usar entrada en salida`, `leer número como texto`, `convertir y calcular`, `probar entrada no válida`.

Organización del trabajo:

- Qué: tareas de entrada y conversión.
- Dónde: Sheet Scrum.
- Cómo: cada tarea con estado y responsable.

### Explicación docente

Di en voz alta:

> `Scanner` nos permite leer desde teclado. Para H1 usaremos una sola instancia sencilla. `nextLine()` devuelve texto, es decir, `String`. Si ese texto representa un número y queremos calcular, debemos convertirlo.

### Explicación guiada: pedir, leer, guardar, parsear, convertir y hacer casting

Úsala al pasar de datos escritos en código a datos introducidos por consola.

Di en voz alta:

> `Scanner` permite leer lo que una persona escribe. `nextLine()` devuelve siempre un `String`. Si queremos calcular con un número escrito por teclado, necesitamos parsear ese texto.

Empieza por el flujo pedir, leer y guardar creando una única instancia de `Scanner` que después pueda reutilizarse.

Proyecta el programa completo para que se vea también el `import`:

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Escribe un nombre ficticio: ");
        String userName = scanner.nextLine();

        System.out.println("Hola, " + userName);
    }
}
```

Señala sin adelantar todavía la POO:

> `import java.util.Scanner` hace disponible la clase `Scanner`. Con `new Scanner(System.in)` usamos un objeto ya preparado de Java para leer desde teclado. Lo guardamos en la variable `scanner` y reutilizamos esa misma variable cada vez que necesitamos leer. En el tema siguiente entenderemos con más profundidad qué significan clase, objeto y constructor.

Pregunta:

> Qué parte prepara `Scanner`, qué variable lo guarda y qué devuelve `scanner.nextLine()`.

Muestra una segunda lectura reutilizando el mismo `Scanner`:

```java
System.out.print("Escribe las horas de estudio: ");
String text = scanner.nextLine();

int hours = Integer.parseInt(text);
```

Pregunta:

> Hemos creado otro `Scanner` o hemos reutilizado el mismo.

Como contraste, puedes mostrar esta forma compacta, pero aclara que no será el modelo de H1:

```java
String userName = new Scanner(System.in).nextLine();
```

Di:

> Esta forma puede leer una línea, pero oculta la idea que queremos practicar: crear una sola instancia y reutilizarla. En H1 escribiremos `Scanner scanner = new Scanner(System.in);` y leeremos con `scanner.nextLine()`.

Contrasta usar y no usar lo leído:

```java
String userName = scanner.nextLine();
System.out.println("Hola, " + userName);
```

```java
String userName = scanner.nextLine();
System.out.println("Hola");
```

Pregunta:

> En cuál de los dos programas la entrada afecta al comportamiento observable.

Dibuja el flujo en la pizarra:

```text
TECLADO -> nextLine() -> String -> variable -> programa -> salida
```

Después pasa a parsear texto:

```java
String text = "5";
int hours = Integer.parseInt(text);
```

```java
String text = new Scanner(System.in).nextLine();
int hours = Integer.parseInt(text);
int minutes = hours * 60;
System.out.println(minutes);
```

Pregunta:

> Para una entrada `2`, qué salida esperas.

Muestra otros parseos sin dedicarles el mismo tiempo:

```java
String text = "7.5";
double score = Double.parseDouble(text);
```

```java
boolean ok = Boolean.parseBoolean(text);
```

Di:

> En H1 priorizamos `parseInt` y `parseDouble`. El boolean aparece solo como otro ejemplo de conversión.

Explica conversión implícita:

```java
int whole = 7;
double wider = whole;
```

```text
7 -> 7.0
```

```java
int hours = 4;
double hoursDecimal = hours;
```

Pregunta:

> Se ha producido una conversión aunque no veamos casting escrito.

Contrasta con parseo:

```java
String text = "4";
int hours = Integer.parseInt(text);

int otherHours = 4;
double hoursDecimal = otherHours;
```

Pregunta:

> En cuál partíamos de texto.

Explica casting y pérdida de información:

```java
double price = 12.75;
int wholePrice = (int) price;
```

```text
wholePrice -> 12
```

```java
double score = 7.99;
int wholeScore = (int) score;
```

```text
wholeScore -> 7
```

Caso revelador:

```java
double value = 3.999;
int result = (int) value;
```

Pregunta:

> El resultado será 3 o 4. Por qué.

Termina distinguiendo tres mecanismos:

```text
Texto a número: Integer.parseInt("5")
Número compatible a tipo más amplio: double d = 5;
Conversión forzada: int n = (int) 5.8;
```

Pregunta al alumnado:

> Qué devuelve `nextLine`, qué guarda `userName`, qué convierte `parseInt` y cuándo falla `Integer.parseInt("hola")`.

Error frecuente que debes cortar:

> Que el texto contenga cifras no lo convierte automáticamente en número.

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

### Evidencia técnica de S212

Pide explícitamente:

> La prueba debe incluir una entrada válida, resultado esperado, resultado obtenido y explicación de qué ocurre con una entrada no convertible.

Dónde y cómo:

- GitHub: código con `Scanner` o micropráctica de conversión y pruebas reproducibles.
- README: puede documentarse antes si resulta útil, pero su consolidación formal ocurre en S214.
- Diario individual: solo si la conversión o el error han producido un aprendizaje o bloqueo significativo.
- Scrum: actualizar la tarea de entrada o conversión únicamente si su estado, planificación o bloqueo ha cambiado.

Qué no aceptar:

- Una prueba que no indique qué entrada se usó.
- Código que lee una variable pero no la usa.
- Decir `no funciona` sin distinguir compilación y ejecución.

Modelo de uso de evidencia S212:

```text
Prueba: conversión de horas.
Entrada válida: 5
Salida esperada: 300 minutos.
Salida obtenida: 300 minutos.
Demuestra: el texto leído se convierte a int y se usa en una operación.

Entrada no convertible: hola
Resultado: error durante la ejecución al aplicar Integer.parseInt.
Demuestra: compilar no garantiza que cualquier entrada sea convertible.
```

### Cierre docente

Di en voz alta:

> Hoy MiniJarvis ya no solo muestra datos escritos por quien programa. Ahora reacciona a una entrada. Pero si la entrada viene como texto, debemos decidir cuándo convertir y cómo comprobar el resultado.

## S213 - Ejecutar - Comparaciones, lógica y decisiones

**Modalidad:** **INDIVIDUAL → PAREJAS → comprobación INDIVIDUAL**

### Objetivo de la sesión

El alumnado debe construir booleanos, combinar condiciones y usar una decisión `if/else` con dos ramas probadas.

### Apertura docente

Di en voz alta:

> Hoy MiniJarvis empieza a decidir algo muy pequeño. No haremos menús ni bucles. Eso será H2. Hoy queremos entender que una comparación produce `true` o `false`, y que `if/else` usa ese resultado para elegir una rama.

### Scrum del día

Pide al alumnado:

> En Scrum, cread o actualizad tareas como `crear comparación`, `guardar boolean`, `implementar if/else`, `probar caso true` o `probar caso false` únicamente cuando representen trabajo real del equipo. Registrad una mejora solo si existe una decisión o cambio concreto.

Dónde y cómo:

- Sheet Scrum para tareas, estados, decisiones o bloqueos reales.
- GitHub para el código y los casos de prueba reproducibles.

### Explicación docente

Di en voz alta:

> Comparar no devuelve uno de los operandos. Devuelve un booleano: `true` o `false`. `=` asigna. `==` compara. Para números podemos usar `==`, `!=`, `<`, `<=`, `>` y `>=`. En H1 no vamos a usar `==` para comparar textos.

### Explicación guiada: comparadores, lógica, decisiones y elección de valor

Úsala antes de `if/else` y antes de pedir las dos pruebas.

Di en voz alta:

> Una comparación produce un booleano: `true` o `false`. `=` asigna; `==` compara. `if` necesita una condición booleana. En H1 hacemos decisiones pequeñas; menús y decisiones encadenadas vendrán en H2.

Empieza con comparadores:

```text
5 > 3 -> true
2 < 1 -> false
5 == 5 -> true
5 == 4 -> false
5 != 4 -> true
```

Pregunta:

> `5 > 3` devuelve 5, devuelve 3 o devuelve una respuesta lógica.

Contrasta asignar y comparar:

```java
int hours = 4;  // asignación
hours == 4      // comparación: true o false
```

Trabaja límites:

```java
int hours = 4;
hours > 4
hours >= 4
```

Pregunta:

> Predice ambas expresiones.

Recuerda:

> En esta sesión no usamos `==` para comparar `String`.

Ahora introduce `&&`, `||` y `!` desde lenguaje natural:

```java
boolean canStart = hasName && hasGoal;
```

Di:

> MiniJarvis puede comenzar si tiene nombre y tiene objetivo.

```java
boolean needsHelp = missingConfig || hasError;
```

Di:

> Necesita ayuda si falta configuración o existe un error.

```java
boolean finished = false;
boolean pending = !finished;
```

Resultado esperado:

```text
pending -> true
```

Traduce en ambos sentidos:

```text
Puede continuar si tiene nombre y objetivo -> hasName && hasGoal
No hay error -> !hasError
```

Pasa del booleano a la decisión:

```java
int hours = 5;
boolean enough = hours >= 4;

if (enough) {
    System.out.println("Objetivo alcanzado");
}
```

Y después condición directa:

```java
if (hours >= 4) {
    System.out.println("Objetivo alcanzado");
}
```

Pregunta:

> Qué produce `hours >= 4`.

Contrasta con lo que no sirve:

```java
if (hours) {
    System.out.println("Objetivo alcanzado");
}
```

Pregunta:

> `hours` contiene un `int`. La condición de `if` responde true/false.

Ahora trabaja dos caminos:

```java
if (hours >= 4) {
    System.out.println("Objetivo alcanzado");
} else {
    System.out.println("Objetivo pendiente");
}
```

Casos obligatorios:

```text
Caso A: hours = 5
Caso B: hours = 2
```

Otro ejemplo cercano a MiniJarvis:

```java
if (hasName) {
    System.out.println("Nombre configurado");
} else {
    System.out.println("Falta configurar el nombre");
}
```

Dato sencillo para validar:

```java
if (studyHours >= 0) {
    System.out.println("Dato aceptado");
} else {
    System.out.println("Las horas no pueden ser negativas");
}
```

Predicción antes de ejecutar:

```java
int score = 5;
if (score >= 5) {
    System.out.println("Superado");
} else {
    System.out.println("Pendiente");
}
```

Pregunta:

> Qué bloque se ejecutará. Cambia `score` a 4 y vuelve a predecir.

Reconoce un `if` anidado sin profundizar:

```java
if (hasName) {
    if (hasGoal) {
        System.out.println("MiniJarvis está preparado");
    }
}
```

Pregunta:

> Qué condición se comprueba primero y cuándo se llega a comprobar `hasGoal`.

Otro anidado:

```java
if (hours >= 4) {
    if (tasks >= 2) {
        System.out.println("Objetivo completo");
    }
}
```

Explica oralmente:

```text
hours >= 4?
  si -> tasks >= 2?
          si -> mensaje
```

Di:

> Aquí basta con reconocer y leer la idea. No vamos a convertir H1 en una sesión de condicionales complejos.

Por último, muestra la asignación condicional `?:` como elección sencilla de valor:

```java
String message;
if (hours >= 4) {
    message = "Objetivo alcanzado";
} else {
    message = "Objetivo pendiente";
}
```

Misma elección con `?:`:

```java
String message = hours >= 4
        ? "Objetivo alcanzado"
        : "Objetivo pendiente";
```

Despieza:

```text
hours >= 4 -> condición
"Objetivo alcanzado" -> valor si true
"Objetivo pendiente" -> valor si false
```

Más ejemplos para leer, no para complicar:

```java
String status = tasks > 0
        ? "Hay tareas"
        : "No hay tareas";

String result = score >= 5
        ? "Superado"
        : "Pendiente";
```

Predicción:

```java
int hours = 2;
String message = hours >= 4
        ? "Objetivo alcanzado"
        : "Objetivo pendiente";
```

Pregunta:

> Qué valor termina almacenado en `message`.

Pregunta al alumnado:

> Qué pasa con `hours = 5`, qué pasa con `hours = 2`, qué rama se ejecuta y qué evidencia demuestra cada caso.

Error frecuente que debes cortar:

> Probar solo el caso `true` no demuestra el `else`.

No presentes `?:` como sustituto de cualquier `if`. En H1 solo interesa leer una elección sencilla de valor.

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

### Evidencia técnica y comprobación individual de S213

Pide explícitamente:

> La prueba debe demostrar dos ramas. No basta con probar el caso favorable. Cada persona debe poder explicar y comprobar ambos recorridos.

Dónde y cómo:

- GitHub: código con comparación e `if/else` y casos reproducibles.
- Diario individual: solo si la diferencia entre predicción y resultado, el error o la mejora han producido aprendizaje significativo.
- Scrum: actualizar pruebas o mejora únicamente cuando sean tareas, decisiones o cambios reales del equipo.

Qué debe poder defender cada persona:

- Qué comparación se evalúa.
- Qué significa `true`.
- Qué significa `false`.
- Qué rama se ejecuta en cada caso.
- Qué mejora concreta hizo en el código o nombres.

Modelo de uso de evidencia S213:

```text
Prueba de decisión if/else

Condición: studyHours >= 4

Caso A:
Valor usado: studyHours = 5
Salida esperada: Objetivo alcanzado.
Salida obtenida: Objetivo alcanzado.
Demuestra: se ejecuta la rama true.

Caso B:
Valor usado: studyHours = 2
Salida esperada: Objetivo pendiente.
Salida obtenida: Objetivo pendiente.
Demuestra: se ejecuta la rama false.
```

### Cierre docente

Di en voz alta:

> H1 ya tiene una decisión pequeña. Si hoy alguien solo puede decir `funciona`, todavía no basta. Debe poder señalar la condición, explicar las dos ramas y demostrar que ambas se han probado.

## S214 - Comunicar - README, evidencias y preparación del cierre

**Modalidad:** **INDIVIDUAL → EQUIPO → PAREJAS**

### Objetivo de la sesión

El alumnado debe consolidar el README de H1, localizar evidencias técnicas verificables y preparar enlaces y permisos para el cierre, sin duplicar diario ni Scrum.

### Apertura docente

Di en voz alta:

> Hoy pasamos a Comunicar. Comunicar no es decorar al final. Comunicar significa que otra persona puede entender qué hicisteis, ejecutarlo, comprobar evidencias y ver qué aprendisteis.

### Scrum del día

Pide al alumnado:

> En Scrum, cread o actualizad únicamente las tareas de cierre que sean trabajo real del equipo, como `terminar README`, `comprobar pruebas`, `comprobar enlaces` o `preparar entrega Moodle`. No añadáis tareas para completar el tablero si no existe trabajo, cambio o bloqueo real.

Registro durante la sesión:

- Las tareas reales conservan su estado y responsable en Scrum.
- Las decisiones, cambios y bloqueos se registran cuando ocurren.
- Scrum no constituye una evidencia independiente por el mero hecho de acabar S214.

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

### Explicación guiada: README, evidencias y enlaces

Úsala antes de documentar y antes de preparar Moodle.

Di en voz alta:

> Documentar no significa copiar la misma información en muchos sitios. Cada espacio responde a una pregunta: GitHub conserva el código y su evolución; README explica qué hace el incremento, sus límites, cómo ejecutarlo y cómo comprobarlo; el diario conserva solo aprendizaje personal significativo; Scrum conserva trabajo y decisiones reales del equipo; Moodle recogerá en S215 los enlaces oficiales. El aprendizaje y el incremento de H1 podrán seleccionarse posteriormente para el portfolio durante C1.

Ejemplo de evidencia verificable:

```text
Prueba: saludo con nombre ficticio.
Entrada usada: Laura.
Salida esperada: Encantado, Laura.
Salida obtenida: Encantado, Laura.
Demuestra: la entrada leída se guarda y se usa en la salida.
Enlace: archivo, prueba o sección concreta del repositorio, no carpeta general.
```

Pregunta al alumnado:

> Qué demuestra esta evidencia, dónde debería estar enlazada y por qué no basta con escribir `funciona`.

Error frecuente que debes cortar:

> No enlacéis carpetas generales. Enlazad la evidencia concreta.

### Investigación del alumnado

Pide al alumnado:

> Revisad vuestro propio material y localizad una evidencia fuerte y una evidencia débil. Investigad por qué una sirve para defender y la otra no.

Trabajo individual — **INDIVIDUAL**:

- Localizar una evidencia técnica fuerte y otra débil.
- Comprobar que puede explicar su aportación.
- Revisar si existe un aprendizaje personal significativo que deba conservarse en el diario; no completar el diario por obligación.

Trabajo en equipo — **EQUIPO**:

- Completar README.
- Localizar en GitHub el código y las pruebas reproducibles.
- Preparar los enlaces que se entregarán oficialmente en Moodle durante S215.
- Comprobar que las decisiones o bloqueos reales están en Scrum, sin forzar una actualización.

Trabajo por parejas — **PAREJAS**:

- Una persona intenta seguir el README de otra sin explicación oral.
- Revisar enlaces y permisos con otra persona.

### Preparación del cierre en S214

Pide explícitamente, en este orden:

1. Consolidar el README H1 en la raíz del repositorio GitHub.
2. Comprobar que el código y las pruebas son reproducibles y están localizables desde GitHub/README.
3. Preparar enlaces profundos para la entrega oficial.
4. Comprobar permisos.
5. Dejar S215 preparado para la defensa y la entrega oficial Moodle.

No se crea una evidencia separada de ejecución si el código, las pruebas y su explicación ya son localizables desde GitHub/README. Drive solo se utiliza ante una evidencia no-code excepcional sin una fuente más natural. S214 no realiza la entrega oficial de Moodle.

Di en voz alta:

> Hoy no vamos a copiar la misma información en varios soportes ni a entregar todavía. Vamos a consolidar el README, localizar el código y las pruebas, comprobar enlaces y permisos, y dejar preparado el cierre oficial de S215. El aprendizaje y el incremento de H1 podrán seleccionarse posteriormente para el portfolio durante C1.

Modelo de uso del README H1:

```markdown
# MiniJarvis H1

## Qué hace
MiniJarvis saluda, pide un nombre ficticio, calcula minutos a partir de horas y muestra si se alcanza un objetivo.

## Límites de H1
No incluye menú, memoria, ficheros ni IA real.

## Cómo ejecutar
1. Abrir el proyecto en IntelliJ.
2. Ejecutar `Main.java`.
3. Introducir datos ficticios.

## Pruebas
Caso A: hours = 5 -> Objetivo alcanzado.
Caso B: hours = 2 -> Objetivo pendiente.
Entrada no convertible: "hola" falla durante la ejecución con parseInt.
```

### Proyección posterior hacia C1 — no se produce ahora

No se crea una página de portfolio durante H1. Cuando llegue C1, cada persona podrá seleccionar aprendizajes como estos:

```text
Reto con mis palabras: construir una primera versión pequeña de MiniJarvis por consola.
Mi aportación: probé Scanner y documenté una entrada no convertible.
Evidencia seleccionable: enlace profundo a la prueba S212.
Qué demuestra: entiendo el flujo pedir -> leer -> guardar -> convertir -> mostrar.
Mejora siguiente: probar mejor entradas no válidas en H2.
```

El equipo también podrá seleccionar posteriormente una síntesis del incremento:

```text
Incremento conseguido: MiniJarvis saluda, pide nombre, calcula minutos y decide si se alcanza un objetivo.
Decisiones: no incluimos menú ni memoria porque no pertenecen a H1.
Pruebas: saludo, conversión, caso true, caso false y entrada no convertible.
Review: el incremento cumple el alcance de S206.
Retrospectiva: debemos actualizar Scrum cuando exista un cambio real, no reconstruirlo al final.
```

Estos textos preservan la reflexión y la selección razonada, pero no son entregables de S214 ni S215.

### Comprobación de permisos

Pide al alumnado:

> Antes de preparar la entrega oficial de S215, comprobad permisos. Un enlace que solo abre el propietario no será una entrega válida.

Cómo comprobar:

- Abrir enlace en ventana privada o con cuenta no propietaria si es posible.
- Pedir a una pareja que abra el enlace.
- Confirmar que lleva al archivo o página concreta, no a la carpeta raíz.

### Cierre docente

Di en voz alta:

> Mañana o en la siguiente sesión defenderéis. Defender no es recitar el README. Defender es señalar, ejecutar, predecir, modificar una parte pequeña y explicar qué demuestra vuestra evidencia.

## S215 - Comunicar - Defensa y cierre H1

**Modalidad combinada:** defensa **INDIVIDUAL**; ensayo y revisión por **PAREJAS**; review, retrospectiva y entrega en **EQUIPO**.

### Objetivo de la sesión

El alumnado debe defender individualmente, cerrar retrospectiva y realizar la entrega final en Moodle.

### Apertura docente

Di en voz alta:

> Hoy cerramos H1. La defensa no es un castigo ni una exposición larga. Es la comprobación de que entendéis vuestro propio producto. Vais a señalar código, explicar decisiones, ejecutar, predecir y, si hace falta, modificar algo pequeño.

### Scrum del día

Pide al alumnado:

> En Scrum, abrid la sección de review y retrospectiva. Durante la sesión vais a registrar qué incremento habéis conseguido, qué queda pendiente, qué bloqueo apareció y qué mejoraréis en H2.

Organización del trabajo:

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

Trabajo individual — **INDIVIDUAL**:

- Defensa individual.
- Reflexión personal; solo se conserva en el diario si contiene un aprendizaje, dificultad, decisión o siguiente paso significativo.

Trabajo por parejas — **PAREJAS**:

- Ensayo de defensa.
- Revisión cruzada de enlaces y permisos.

Trabajo en equipo — **EQUIPO**:

- Review y retrospectiva Scrum.
- Entrega oficial Moodle H1.

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
  - enlace al Sheet Scrum del equipo o sección H1 cuando forme parte del cierre;
  - confirmación de permisos revisados.

El código, las pruebas y la explicación técnica deben quedar localizables desde GitHub/README. No se crea para Moodle una captura, un documento ni una evidencia adicional si esa información ya está localizada.

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
Scrum equipo H1, si corresponde:

Permisos comprobados: sí/no
Observaciones o bloqueo pendiente:
```

Modelo de uso de entrega Moodle ya rellenada:

```text
Equipo: Ada
Integrantes: Nora, Luis, Marta, Amira

Repositorio GitHub: https://...
README H1: https://...
Scrum equipo H1: https://...

Permisos comprobados: sí
Observaciones: la entrada no convertible está documentada y es reproducible desde el README; no usamos try-catch porque no pertenece a H1.
```

Modelo que no debes aceptar en Moodle:

```text
Está todo en Drive.
```

### Reflexión individual final

Pide al alumnado que piense:

> Identifica una cosa que ya puedes hacer sin ayuda, una cosa para la que todavía necesitas apoyo, una evidencia que lo demuestra y un siguiente paso para H2.

La reflexión forma parte del cierre individual. Solo se conserva en el diario cuando contiene aprendizaje significativo; no se obliga a crear una entrada S215 ni un documento separado.

Modelo de una reflexión significativa que sí podría conservarse en el diario:

```text
Fecha: cierre H1
Sesión: S215
Objetivo: cerrar H1 y preparar H2.
Acción realizada: defendí mi código, revisé enlaces y entregué en Moodle.
Prueba y resultado: expliqué Scanner, parseInt y las dos ramas del if/else.
Evidencia enlazada: enlace a README y prueba S213.
Bloqueo: necesito practicar errores de entrada.
Siguiente paso: en H2 probar comandos y depuración.
```

### Retrospectiva de equipo

Pide explícitamente:

> En equipo, cerrad retrospectiva H1 con cuatro frases: qué funcionó, qué no funcionó, qué mantendremos en H2 y qué cambiaremos en H2.

Dónde y cómo:

- Sheet Scrum de equipo, sección retrospectiva.
- Enlace desde Moodle si la tarea lo pide.

Modelo de uso de retrospectiva de equipo:

```text
Qué funcionó: revisar por parejas antes de entregar.
Qué no funcionó: actualizamos Scrum demasiado tarde.
Qué mantendremos en H2: predicción antes de ejecutar.
Qué cambiaremos en H2: registrar bloqueos en cuanto aparezcan.
```

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
- Cada equipo tiene Scrum con backlog, decisiones, review y retrospectiva reales.
- El diario de cada persona contiene solo las entradas relevantes que hayan sido necesarias.
- Cada persona puede defender al menos una parte técnica.
- Moodle contiene los enlaces profundos de la entrega oficial H1.
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

Cuando dudan si algo merece conservarse en el diario:

> No escribas por completar una fila. Si hubo un aprendizaje, una diferencia relevante entre predicción y resultado, un error, un bloqueo, una decisión personal, un uso relevante de IA o un siguiente paso significativo, explica qué ocurrió y qué aprendiste. Si no ocurrió nada relevante, no hay nada que registrar.

Cuando el equipo no actualiza Scrum:

> Si la tarea solo está en vuestra cabeza, el equipo no la puede gestionar. Escribidla en Scrum con estado y responsable.

Cuando entregan enlaces generales:

> Este enlace abre una carpeta, no una evidencia. Necesito el enlace profundo al archivo, página, README o prueba concreta.

Cuando una defensa es vaga:

> Vuelve al código. Señala una línea, explica qué dato maneja, ejecútala y comprueba el resultado.

## Qué no debes hacer en H1

- No des una solución completa para copiar.
- No aceptes evidencias sin explicación.
- No crees durante H1 una página de portfolio obligatoria; la selección se hará posteriormente en C1.
- No conviertas Moodle en almacén duplicado de todo.
- No pidas informes extra si el diario, Scrum, GitHub/README y Moodle ya cubren la evidencia.
- No metas contenidos fuertes de H2 por adelantar.
- No evalúes solo que compile.
- No permitas código que la persona no pueda explicar.

## Resumen de actividad, evidencia y modalidad por sesión

| Sesión | Actividad pedagógica principal | Evidencia que persiste y fuente canónica | Modalidad |
|---|---|---|---|
| S206 | Delimitar alcance, clasificar requisitos y crear backlog inicial | Alcance, tareas y decisiones reales en Scrum | INDIVIDUAL → EQUIPO |
| S207 | Comprender código, compilación, ejecución y consola | Código de la primera ejecución en GitHub; estado o bloqueo real en Scrum | INDIVIDUAL → PAREJAS |
| S208 | Reconstruir estructura mínima, provocar y corregir un error | Código o micropráctica en GitHub; diario solo ante aprendizaje significativo | INDIVIDUAL → PAREJAS → comprobación INDIVIDUAL |
| S209 | Diseñar, contrastar e implementar mensajes | Decisión real en Scrum y código en GitHub | PAREJAS → EQUIPO |
| S210 | Practicar variables, planificar datos e integrarlos en MiniJarvis | Código en GitHub; planificación junto al trabajo; diario/Scrum solo cuando corresponda | INDIVIDUAL → EQUIPO → comprobación INDIVIDUAL |
| S211 | Predecir y comprobar constantes, literales y operaciones | Código o micropráctica en GitHub; reflexión solo si produjo aprendizaje significativo | INDIVIDUAL → PAREJAS |
| S212 | Leer, convertir y probar entradas válidas y no convertibles | Código y pruebas reproducibles en GitHub; README opcional hasta su consolidación en S214 | INDIVIDUAL → PAREJAS |
| S213 | Construir y probar las dos ramas de una decisión | Código y casos reproducibles en GitHub; comprobación individual de comprensión | INDIVIDUAL → PAREJAS → comprobación INDIVIDUAL |
| S214 | Consolidar README, localizar pruebas, preparar enlaces y comprobar permisos | README y pruebas en GitHub; no hay entrega oficial Moodle | INDIVIDUAL → EQUIPO → PAREJAS |
| S215 | Defender, revisar, hacer retrospectiva y cerrar H1 | Defensa individual; review/retrospectiva en Scrum; entrega oficial en Moodle con enlaces a GitHub/README | INDIVIDUAL + PAREJAS + EQUIPO |

## Cierre para el profesor

Si en algún momento dudas, vuelve a estas tres preguntas:

- Qué debe aprender hoy el alumnado.
- Qué evidencia concreta lo demuestra.
- Dónde queda esa evidencia sin duplicarla.

Si puedes responder a esas tres preguntas, la sesión está bien orientada.
