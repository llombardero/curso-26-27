# Guion docente completo H2 - Agente con decisiones y depuracion

## Para que sirve este guion

Este documento permite impartir H2 de forma secuencial aunque sea la primera vez que se trabaja por proyectos, Scrum o depuracion en aula.

Puedes leer literalmente los bloques marcados como `Di en voz alta`. Cuando aparezca `Pide al alumnado`, formula esa accion como orden concreta. Cuando aparezca `Entrega`, indica que debe quedar, cuando, donde y como.

H2 no introduce una IA real ni una arquitectura avanzada. H2 transforma MiniJarvis H1 en un agente de consola con menu, comandos, repeticion hasta `salir`, pruebas manuales, depuracion e incidencias documentadas.

## Producto final de H2

Al terminar H2, cada equipo debe tener un MiniJarvis por consola que se repite hasta que la persona usuaria escriba `salir`.

El producto debe incluir:

- `Main.java` ejecutable;
- menu o lista de comandos visibles;
- lectura de comandos con `Scanner`;
- bucle de repeticion;
- variable de control de salida;
- comandos minimos `ayuda`, `saluda`, `estado` y `salir`;
- respuesta controlada para comando desconocido;
- seleccion mediante `if/else` encadenado o `switch` simple;
- plan de pruebas manuales;
- evidencia de depuracion con breakpoint;
- una incidencia natural o didactica reproducida;
- comparacion Java-Python centrada en bucle, decision y entrada;
- README y defensa individual.

El producto no debe incluir todavia:

- memoria con listas o mapas;
- persistencia en ficheros;
- varias clases propias obligatorias;
- patrones de diseno;
- conexion con IA real;
- base de conocimiento;
- datos personales reales, claves, tokens o credenciales.

Di en voz alta al comienzo de H2:

> En H1 construimos un MiniJarvis pequeno y lineal. H2 no empieza desde cero: toma lo que ya sabemos, especialmente comparaciones, booleanos e `if/else`, y lo convierte en un programa interactivo que no termina hasta que el usuario escribe `salir`. El objetivo no es hacer muchas funciones; el objetivo es controlar el flujo, probarlo, depurarlo y poder defenderlo.

## Modelo HEXA en H2

H2 sigue el ciclo HEXA completo:

- S216 - Activar: entender el salto de H1 a H2.
- S217 - Investigar: disenar comandos antes de programar.
- S218 - Investigar: usar booleanos y variable de control.
- S219 - Investigar: construir el bucle `while`.
- S220 - Investigar: aplicar `if/else` encadenado.
- S221 - Investigar: comparar textos correctamente con `.equals()`.
- S222 - Idear: seleccionar y justificar la salida controlada.
- S223 - Planificar: elegir estructuras de control y ordenar pruebas.
- S224 - Ejecutar: probar manualmente el menu.
- S225 - Ejecutar: depurar con breakpoint.
- S226 - Ejecutar: documentar incidencia y correccion.
- S227 - Comunicar: comparar Java y Python.
- S228 - Comunicar: defender, evaluar y cerrar H2.

## Scrum minimo para H2

En H2 Scrum debe servir para controlar el incremento del producto. No abras documentos nuevos si la informacion ya tiene sitio.

Cada equipo debe mantener en su Sheet Scrum:

- backlog H2;
- tareas de comandos;
- tareas de pruebas;
- tarea de depuracion;
- incidencia seleccionada;
- responsable o pareja responsable;
- estado: pendiente, en curso, hecho, bloqueado;
- decisiones tecnicas;
- enlaces a evidencias;
- review y retrospectiva final.

Di en voz alta al inicio de cada sesion:

> Antes de tocar codigo, mirad el Scrum. En H2 es facil perderse porque el programa ya tiene varias rutas. Si no sabemos que comando estamos construyendo, que prueba lo comprueba y que bloqueo existe, no estamos trabajando como equipo.

## Ecosistema de entregas

Usa siempre estos espacios:

- Moodle: entrega final de enlaces del hito.
- GitHub: codigo, README y documentos `docs/`.
- Diario individual: avance personal, prueba, bloqueo, uso de IA y siguiente paso.
- Scrum de equipo: backlog, decisiones, pruebas, incidencia, review y retrospectiva.
- Site personal: seleccion razonada de evidencias individuales.
- Site de equipo: comunicacion del incremento H2 y enlaces principales.
- Drive: capturas o evidencias no codigo, siempre enlazadas desde GitHub o los documentos.

Regla que debes repetir:

> Una prueba no es decir "funciona". Una prueba contiene entrada, salida esperada, salida obtenida y decision: pasa o no pasa.

## Rutina fija de aula

1. Abre con el objetivo en lenguaje sencillo.
2. Recuerda la fase HEXA.
3. Revisa Scrum durante dos minutos.
4. Explica solo lo necesario para desbloquear la practica.
5. Pide prediccion antes de ejecutar codigo.
6. Ejecuta o simula el resultado.
7. Haz que el alumnado pruebe con un caso favorable y uno desfavorable.
8. Pide evidencia concreta en su fuente correcta.
9. Cierra con diario, Scrum o documento `docs/` segun corresponda.

Di en voz alta cuando haya codigo:

> Antes de ejecutar, decid que creeis que va a pasar. En H2 hay varias rutas: ayuda, saluda, estado, salir y comando desconocido. Si no predigo la ruta, no estoy entendiendo el flujo.

## S216 - Activar - Presentar H2 desde H1

### Objetivo de la sesion

El alumnado debe entender que H2 convierte el programa lineal de H1 en un programa interactivo con menu, decisiones aplicadas y repeticion.

### Apertura docente

Di en voz alta:

> Hoy empieza H2. La pregunta central es: que tiene que cambiar para que MiniJarvis no termine despues del primer saludo. En H1 el programa avanzaba linea a linea y terminaba. En H2 necesitamos que escuche comandos hasta que el usuario decida salir.

Pide al alumnado:

> Escribid una tabla con dos columnas: `H1 hacia una vez` y `H2 debe repetir o decidir`. No programeis todavia.

### Scrum del dia

Pide al equipo:

> En el Scrum cread una tarea grande llamada `Construir MiniJarvis H2` y cinco subtareas: `disenar comandos`, `crear bucle`, `anadir decisiones`, `probar comandos`, `depurar e incidencia`.

Entrega de S216:

- Que: tabla H1 frente a H2 y backlog inicial H2.
- Cuando: durante la sesion.
- Donde: tabla en Scrum o README temporal; backlog en Sheet Scrum.
- Como: filas concretas con cambio observable.
- Moodle: no se entrega todavia.

### Explicacion docente

Proyecta este contraste:

```text
H1: saluda -> lee algun dato -> muestra salida -> termina
H2: muestra menu -> lee comando -> decide -> vuelve al menu -> termina solo con salir
```

Pregunta:

> Que palabra tecnica necesitamos para repetir algo mientras no se cumpla una condicion.

Respuesta esperada:

```text
Bucle.
```

### Cierre

Pide al alumnado:

> En el diario individual escribid una frase: `En H2 mi mayor cambio sera...` y una duda tecnica concreta.

## S217 - Investigar - Diseno de comandos antes de programar

### Objetivo de la sesion

El alumnado debe definir el comportamiento comprobable de cada comando antes de escribir codigo.

### Apertura docente

Di en voz alta:

> Un comando no esta disenado cuando suena bien. Esta disenado cuando podemos probar que entrada recibe y que salida produce.

### Actividad principal

Pide al alumnado:

> Completad una tabla con `comando`, `entrada`, `salida esperada`, `caso de prueba` y `quien lo implementa o revisa`.

Modelo minimo:

```text
Comando: ayuda
Entrada: ayuda
Salida esperada: Comandos: ayuda, saluda, estado, salir
Prueba: escribir ayuda y comprobar que aparecen los cuatro comandos
```

Entrega de S217:

- Que: tabla de comandos con respuesta esperada.
- Cuando: antes de programar los comandos.
- Donde: README en borrador o Scrum del equipo.
- Como: al menos `ayuda`, `saluda`, `estado`, `salir` y `otro`.
- Moodle: no todavia.

### Cierre

Pregunta de control:

> Si no sabemos que debe responder `estado`, que pasara cuando intentemos probarlo.

Respuesta esperada:

```text
No sabremos si funciona o solo si imprime algo.
```

## S218 - Investigar - Booleanos y variable de control

### Objetivo de la sesion

El alumnado debe usar una variable booleana para controlar si el programa sigue o termina.

### Explicacion docente

Di en voz alta:

> En H1 un booleano podia guardar el resultado de una comparacion. En H2 un booleano puede controlar la vida del programa. Mientras `running` sea `true`, MiniJarvis sigue escuchando.

Proyecta:

```java
boolean running = true;

System.out.println(running);
running = false;
System.out.println(running);
```

Pide prediccion antes de ejecutar:

```text
true
false
```

### Micropractica

Pide al alumnado:

> Cread una variable `running`. Escribid dos lineas que demuestren que puede cambiar de `true` a `false`. No hagais todavia el menu completo.

Entrega de S218:

- Que: codigo preparado para controlar repeticion.
- Cuando: durante la practica.
- Donde: `src/Main.java` o microarchivo guardado en GitHub.
- Como: variable `running` visible y explicable.
- Moodle: no todavia.

### Error frecuente

Di en voz alta:

> `running` no es decoracion. Si nunca cambia a `false`, el programa no sabra terminar.

## S219 - Investigar - Bucle `while`

### Objetivo de la sesion

El alumnado debe construir un bucle que repite el prompt `>` y lee comandos.

### Explicacion docente

Proyecta:

```java
Scanner scanner = new Scanner(System.in);
boolean running = true;

while (running) {
    System.out.print("> ");
    String command = scanner.nextLine();
    System.out.println("Has escrito: " + command);
}
```

Pregunta antes de ejecutar:

> Que problema tiene este programa si no cambiamos nunca `running`.

Respuesta esperada:

```text
No termina por si solo.
```

### Practica

Pide al alumnado:

> Haced que aparezca `>` mas de una vez. De momento puede repetir todo; en la siguiente sesion empezaremos a decidir que hacer con cada comando.

Entrega de S219:

- Que: programa que repite prompt `>`.
- Cuando: final de sesion.
- Donde: `src/Main.java`.
- Como: commit o captura enlazada con entrada y salida.
- Moodle: no todavia.

### Cierre

Pide diario individual:

> Escribe que condicion controla el bucle y que pasaria si esa condicion nunca cambia.

## S220 - Investigar - Aplicar y encadenar `if/else`

### Objetivo de la sesion

El alumnado debe aplicar `if`, `else if` y `else` a varios comandos y justificar el orden de evaluacion.

### Explicacion docente

Di en voz alta:

> H1 ya introdujo `if/else`. H2 no lo presenta como magia nueva: lo aplica a un menu. Cada comando es una pregunta: si el comando es ayuda, haz esto; si es estado, haz esto; si no es ninguno, responde con comando desconocido.

Proyecta:

```java
if (command.equals("ayuda")) {
    System.out.println("Comandos: ayuda, saluda, estado, salir");
} else if (command.equals("estado")) {
    System.out.println("Estoy funcionando en modo H2.");
} else {
    System.out.println("No entiendo ese comando. Escribe ayuda.");
}
```

Pide prediccion para estas entradas:

```text
ayuda
estado
inventa
```

Entrega de S220:

- Que: menu parcial funcional.
- Cuando: al cierre de la practica.
- Donde: `src/Main.java` y, si procede, prueba breve en `docs/pruebas-h2.md`.
- Como: evidenciar al menos `ayuda`, `estado` y comando desconocido.
- Moodle: no todavia.

### Error frecuente

Di en voz alta:

> El ultimo `else` no sobra. Es lo que evita que el programa se quede mudo ante una entrada no prevista.

## S221 - Investigar - Comparacion de textos en Java

### Objetivo de la sesion

El alumnado debe evitar el error de comparar cadenas con `==` y usar `.equals()` de forma defendible.

### Explicacion docente

Di en voz alta:

> En Java, para comparar el contenido de un texto usamos `.equals()`. No evaluaremos explicaciones internas de memoria en profundidad, pero si exigiremos que el menu funcione y que sepais decir por que `==` no es la forma correcta para comandos.

Proyecta:

```java
String command = "ayuda";

System.out.println(command.equals("ayuda"));
System.out.println(command.equals("salir"));
```

Despues muestra normalizacion si el equipo decide soportarla:

```java
String command = scanner.nextLine().trim().toLowerCase();
```

Di en voz alta:

> `trim()` quita espacios al principio y al final. `toLowerCase()` convierte a minusculas. Si los usais, debereis probarlo; si no los usais, el README debe dejar claro que los comandos se escriben exactamente.

Entrega de S221:

- Que: comandos comparados con `.equals()` y decision sobre espacios/mayusculas.
- Cuando: durante la sesion.
- Donde: codigo y Scrum, seccion decisiones tecnicas.
- Como: decision escrita: `soportamos trim/toLowerCase` o `exigimos comandos exactos`.
- Moodle: no todavia.

## S222 - Idear - Comando `salir` y cierre controlado

### Objetivo de la sesion

El alumnado debe hacer que el programa termine solo cuando se escriba `salir`.

### Explicacion docente

Di en voz alta:

> `salir` no debe romper el programa. Debe cambiar el estado del programa para que el bucle deje de repetirse de forma controlada.

Proyecta:

```java
if (command.equals("salir")) {
    running = false;
    System.out.println("Hasta pronto.");
}
```

Pregunta:

> Que variable cambia y que ocurrira al volver al inicio del `while`.

Respuesta esperada:

```text
Cambia running a false; el while deja de repetirse.
```

Entrega de S222:

- Que: programa que termina solo con `salir`.
- Cuando: cierre de sesion.
- Donde: `src/Main.java` y prueba en `docs/pruebas-h2.md` si ya esta creado.
- Como: prueba con un comando normal antes de `salir` y prueba de salida.
- Moodle: no todavia.

## S223 - Planificar - Refuerzo de bucles y eleccion de estructura

### Objetivo de la sesion

El alumnado debe comparar `while`, `do-while`, `for` y `switch` con ejercicios acotados y elegir una estructura defendible para su menu.

### Explicacion docente

Di en voz alta:

> No todos los bucles sirven igual. `while` encaja cuando repetimos mientras se cumple una condicion. `do-while` garantiza una primera ejecucion. `for` encaja cuando sabemos cuantas repeticiones queremos. `switch` puede hacer mas legible un menu de opciones exactas.

Ejemplo con `switch` simple:

```java
switch (command) {
    case "ayuda":
        System.out.println("Comandos: ayuda, saluda, estado, salir");
        break;
    case "estado":
        System.out.println("Estoy funcionando en modo H2.");
        break;
    default:
        System.out.println("No entiendo ese comando.");
}
```

Pide al alumnado:

> No cambies a `switch` solo porque parece mas profesional. Elige la version que puedas explicar y probar.

Entrega de S223:

- Que: apartado `Refuerzo de bucles` dentro de `docs/pruebas-h2.md`.
- Cuando: durante la sesion.
- Donde: `docs/pruebas-h2.md`.
- Como: incluir codigo breve, explicacion y una pregunta de eficiencia o eleccion de estructura.
- Moodle: no todavia.

## S224 - Ejecutar - Pruebas manuales

### Objetivo de la sesion

El alumnado debe convertir el comportamiento esperado en casos de prueba con esperado, obtenido y resultado.

### Explicacion docente

Di en voz alta:

> Probar no es ejecutar una vez. Probar es elegir entradas representativas, anotar que esperas, ejecutar, comparar y decidir si pasa.

Modelo de caso:

```text
Caso: comando desconocido
Entrada: inventa
Esperado: No entiendo ese comando. Escribe ayuda.
Obtenido: No entiendo ese comando. Escribe ayuda.
Resultado: PASA
```

Casos minimos:

- `ayuda`;
- `saluda`;
- `estado`;
- comando desconocido;
- `salir`;
- mayusculas o espacios si el equipo decidio soportarlos.

Entrega de S224:

- Que: `docs/pruebas-h2.md`.
- Cuando: cierre de sesion.
- Donde: repositorio GitHub, carpeta `docs/`.
- Como: tabla o lista con entrada, esperado, obtenido y resultado.
- Moodle: no todavia; se enlazara en entrega final.

## S225 - Ejecutar - Depuracion con breakpoint

### Objetivo de la sesion

El alumnado debe observar el programa mientras se ejecuta y explicar valores de variables.

### Explicacion docente

Di en voz alta:

> Depurar no es mirar el codigo con mas atencion. Depurar es parar la ejecucion en un punto concreto y observar valores reales.

Breakpoint recomendado:

```text
Linea posterior a leer command = scanner.nextLine();
```

Variables a observar:

```text
command
running
userName
```

Preguntas de defensa:

```text
Que valor tiene command cuando escribes ayuda?
Que rama se ejecuta?
Cuando cambia running a false?
```

Entrega de S225:

- Que: `docs/depuracion-h2.md`.
- Cuando: durante la sesion.
- Donde: repositorio GitHub, carpeta `docs/`.
- Como: captura o descripcion textual del breakpoint, variable observada, valor y conclusion.
- Moodle: no todavia.

## S226 - Ejecutar - Incidencias y correccion de errores

### Objetivo de la sesion

El alumnado debe documentar una incidencia natural o didactica reproducida y su solucion.

### Explicacion docente

Di en voz alta:

> Una incidencia no es un fracaso. Una incidencia bien documentada demuestra que sabes reproducir un problema, localizar una causa, corregir y verificar.

Incidencia didactica si no aparece una natural:

```text
Sintoma: escribir salir no termina el programa.
Causa probable: la rama de salir imprime mensaje pero no cambia running a false.
Correccion: asignar running = false dentro de la rama salir.
Verificacion: ejecutar ayuda, luego salir, y comprobar que el programa termina.
```

Entrega de S226:

- Que: `docs/incidencia-h2.md`.
- Cuando: cierre de sesion.
- Donde: repositorio GitHub, carpeta `docs/`.
- Como: sintoma, reproduccion, esperado, obtenido, breakpoint o traza, causa, correccion y verificacion.
- Moodle: no todavia.

Tarea para casa antes de S227:

- Que: borrador de comparacion Java-Python H2.
- Tiempo: 30-45 minutos.
- Donde: `docs/comparacion-java-python-h2.md`.
- Como: comparar una idea concreta: bucle, decision o lectura de entrada.

## S227 - Comunicar - Comparacion Java-Python H2

### Objetivo de la sesion

El alumnado debe revisar y corregir una comparacion acotada entre Java y Python, centrada en comprension.

### Explicacion docente

Di en voz alta:

> La comparacion Java-Python no busca aprender Python de memoria. Busca comprobar que entendeis la idea: repetir, decidir, leer texto y terminar.

Proyecta:

```java
while (running) {
    String command = scanner.nextLine();
    if (command.equals("salir")) {
        running = false;
    }
}
```

Contrasta con Python:

```python
running = True
while running:
    command = input("> ")
    if command == "salir":
        running = False
```

Pide al alumnado:

> Senalad el equivalente del `while`, de la lectura de entrada, de la condicion y del cambio de la variable de control.

Entrega de S227:

- Que: `docs/comparacion-java-python-h2.md` corregido.
- Cuando: durante la sesion.
- Donde: repositorio GitHub, carpeta `docs/`.
- Como: comparacion breve, no traduccion enorme; debe incluir dos diferencias explicadas.
- Moodle: no todavia.

## S228 - Comunicar - Demo, defensa y cierre H2

### Objetivo de la sesion

El alumnado debe demostrar que el menu funciona, que se ha probado, que se ha depurado y que cada persona puede defender su comprension.

### Apertura docente

Di en voz alta:

> H2 se supera cuando el producto funciona y se puede explicar. La defensa no sustituye al codigo y el codigo no sustituye a la defensa. Hoy vamos a comprobar menu, pruebas, depuracion, incidencia y comprension individual.

### Secuencia de defensa

Pide por equipo:

1. Ejecutar MiniJarvis H2.
2. Probar `ayuda`.
3. Probar `saluda` o `estado`.
4. Probar un comando desconocido.
5. Probar `salir`.
6. Mostrar una prueba manual documentada.
7. Mostrar breakpoint o evidencia de depuracion.
8. Explicar una incidencia.

Pide individualmente una de estas microdefensas:

- senalar donde se repite el programa;
- explicar que cambia `running`;
- explicar por que se usa `.equals()`;
- anadir o modificar un comando simple;
- explicar un caso de prueba;
- explicar el breakpoint usado;
- comparar una linea Java con su equivalente Python.

Entrega final de S228:

- Que: enlaces finales H2.
- Cuando: cierre del hito.
- Donde: Moodle.
- Como: enlace al repositorio, README, pruebas, depuracion, incidencia, comparacion, defensa, Scrum, Site personal y Site de equipo si procede.

Checklist de cierre:

```text
[ ] El programa se ejecuta.
[ ] El menu se repite.
[ ] Existe ayuda.
[ ] Existe saluda.
[ ] Existe estado.
[ ] Existe salir.
[ ] Hay comando desconocido controlado.
[ ] Hay pruebas manuales.
[ ] Hay depuracion con breakpoint.
[ ] Hay incidencia documentada.
[ ] Hay comparacion Java-Python.
[ ] Hay README actualizado.
[ ] Hay registro IA si procede.
[ ] Cada persona puede defender su parte.
```

Di en voz alta para cerrar H2:

> H2 cierra el control de flujo basico de MiniJarvis: repetir, decidir, salir, probar y depurar. H3 podra anadir memoria, pero solo tiene sentido si este menu ya funciona y si entendeis por que toma cada ruta.

## Resumen de evidencias H2

| Sesion | Evidencia principal | Fuente correcta | Moodle |
|---|---|---|---|
| S216 | Tabla H1 frente a H2 y backlog inicial | Scrum o README borrador | No |
| S217 | Tabla de comandos | README o Scrum | No |
| S218 | Variable `running` explicable | Codigo o microarchivo | No |
| S219 | Prompt repetido con `while` | `src/Main.java` | No |
| S220 | Menu parcial funcional | `src/Main.java` y pruebas | No |
| S221 | Decision sobre `.equals()`, `trim()` y `toLowerCase()` | Codigo y Scrum | No |
| S222 | Salida controlada con `salir` | Codigo y prueba | No |
| S223 | Refuerzo de bucles | `docs/pruebas-h2.md` | No |
| S224 | Pruebas manuales | `docs/pruebas-h2.md` | No |
| S225 | Depuracion con breakpoint | `docs/depuracion-h2.md` | No |
| S226 | Incidencia corregida | `docs/incidencia-h2.md` | No |
| S227 | Comparacion Java-Python | `docs/comparacion-java-python-h2.md` | No |
| S228 | Entrega final y defensa | Moodle, GitHub, Sites y Sheets | Si |
