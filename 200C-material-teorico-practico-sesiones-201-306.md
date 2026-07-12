# Material teórico-práctico para preparar las sesiones 201-306

## Programación orientada a objetos — MiniJarvis — Curso 2026/2027

Documentos de referencia:

- `200A-guia-docente-integral-plan-clases-scrum-hexa.md`
- `200B-plan-sesion-a-sesion-201-en-adelante.md`
- `05-politica-uso-ia-semaforo-registro-defensa.md`
- `06-rubricas-hitos.md`
- Carpeta `hitos/`

---

## 1. Cómo usar este material

Cada sesión incluye cuatro piezas:

| Pieza | Uso en clase |
|---|---|
| Explicación docente | Lo que debes explicar en lenguaje claro. |
| Demostración | Ejemplo, pizarra, código o dinámica que puedes mostrar. |
| Práctica | Tarea que debe hacer el alumnado. |
| Comprobación | Preguntas para verificar comprensión. |

Regla práctica:

```text
Explica poco, demuestra algo concreto, deja practicar y cierra con una pregunta defendible.
```

---

## 2. Mini-ejemplos reutilizables

### 2.1. Programa mínimo Java

```java
public class Main {
    public static void main(String[] args) {
        System.out.println("Hola, soy MiniJarvis.");
    }
}
```

Idea a explicar:

```text
Java necesita una clase. El programa empieza en main. Lo que pongamos dentro de main se ejecuta en orden.
```

### 2.2. Variables, constantes y entrada

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        final String ASSISTANT_NAME = "MiniJarvis";
        Scanner scanner = new Scanner(System.in);

        System.out.print("¿Cómo te llamas? ");
        String userName = scanner.nextLine();

        System.out.println("Hola, " + userName + ". Soy " + ASSISTANT_NAME + ".");
        scanner.close();
    }
}
```

### 2.3. Bucle y comandos

```java
boolean running = true;

while (running) {
    System.out.print("> ");
    String command = scanner.nextLine().trim().toLowerCase();

    if (command.equals("ayuda")) {
        System.out.println("Comandos: ayuda, estado, salir");
    } else if (command.equals("estado")) {
        System.out.println("Estoy funcionando.");
    } else if (command.equals("salir")) {
        running = false;
    } else {
        System.out.println("No entiendo ese comando.");
    }
}
```

### 2.4. Colección con memoria temporal

```java
import java.util.ArrayList;

ArrayList<String> memories = new ArrayList<>();
memories.add("Repasar bucles");

for (int i = 0; i < memories.size(); i++) {
    System.out.println((i + 1) + ". " + memories.get(i));
}
```

### 2.5. Clase `Memory`

```java
import java.util.ArrayList;
import java.util.List;

public class Memory {
    private final List<String> memories;

    public Memory() {
        this.memories = new ArrayList<>();
    }

    public void remember(String text) {
        if (text != null && !text.isBlank()) {
            memories.add(text);
        }
    }

    public List<String> getAll() {
        return new ArrayList<>(memories);
    }

    public int size() {
        return memories.size();
    }
}
```

### 2.6. Interfaz `Tool`

```java
public interface Tool {
    String name();
    String description();
    void execute();
}
```

### 2.7. Escritura y lectura simple de ficheros

```java
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.StandardOpenOption;
import java.util.List;

Path dataDir = Path.of("data");
Path file = dataDir.resolve("recuerdos.txt");

Files.createDirectories(dataDir);
Files.writeString(file, "Repasar ficheros\n", StandardOpenOption.CREATE, StandardOpenOption.APPEND);

List<String> lines = Files.readAllLines(file);
```

### 2.8. Simulación IA segura

```java
public class SimulatedAiAssistant {
    public String answer(String prompt) {
        if (prompt == null || prompt.isBlank()) {
            return "No puedo responder a una consulta vacía.";
        }

        if (prompt.toLowerCase().contains("contraseña")) {
            return "No puedo trabajar con contraseñas ni secretos.";
        }

        return "Sugerencia de estudio: divide el problema en pasos pequeños y prueba cada paso.";
    }
}
```

---

## 3. Material por sesión

## H0 — Scrum, equipos e IA responsable

### Sesión 201 — Presentación del curso y narrativa MiniJarvis

Explicación docente: Presenta el curso como construcción progresiva de un agente. Insiste en que al principio será un programa sencillo y que la IA real no es el punto de partida.

Demostración: Dibuja una línea de evolución: saludo → menú → memoria → clases → herramientas → persistencia → IA segura.

Práctica: Cada alumno responde qué cree que hará MiniJarvis y qué riesgo ve en usar IA.

Comprobación: ¿Qué diferencia hay entre hacer una IA completa y construir un agente educativo por hitos?

### Sesión 202 — Reglas de trabajo, IA responsable y evidencias

Explicación docente: Explica el semáforo IA. Verde ayuda a comprender, amarillo exige registro y defensa, rojo invalida o condiciona la evidencia.

Demostración: Muestra tres prompts: uno para entender variables, otro para generar código, otro para copiar una entrega completa. Clasificadlos.

Práctica: Rellenar un registro IA ficticio.

Comprobación: ¿Qué tienes que hacer si usas IA para generar una parte de código?

### Sesión 203 — Scrum vivido: preparación de la torre de papel

Explicación docente: Scrum no es una teoría de nombres; es una forma de trabajar con producto, tareas, roles, revisión y mejora.

Demostración: Crea en la pizarra un tablero `Pendiente | En curso | Hecho | Bloqueado`.

Práctica: Equipos, roles y backlog de la torre.

Comprobación: ¿Qué diferencia hay entre una tarea y un objetivo?

### Sesión 204 — Sprint de torre de papel, review y retrospectiva

Explicación docente: Review mira el producto; retrospectiva mira el proceso.

Demostración: Tras construir, pregunta primero si la torre cumple restricciones y después cómo trabajó el equipo.

Práctica: Construcción, medición, review y retro.

Comprobación: ¿Qué cambiaríais si repitierais el sprint?

### Sesión 205 — Transferencia de Scrum a MiniJarvis

Explicación docente: Lo vivido con la torre se aplicará a software: backlog, sprint, demo, pruebas y mejora.

Demostración: Convierte una tarea de torre en una tarea de MiniJarvis: “crear base” → “crear proyecto Java ejecutable”.

Práctica: Primer tablero del proyecto.

Comprobación: ¿Cómo sabremos que una tarea de programación está terminada?

---

## H1 — Java básico y primer asistente

### Sesión 206 — Presentar H1 y delimitar alcance

Explicación docente: H1 busca base sólida, no espectacularidad. No hay menú, bucles, memoria ni IA.

Demostración: Enseña una salida esperada de H1 en consola.

Práctica: Clasificar funcionalidades en “H1”, “más adelante” y “no adecuado”.

Comprobación: ¿Por qué un menú no pertenece todavía a H1?

### Sesión 207 — Entorno de trabajo: IntelliJ, proyecto y ejecución

Explicación docente: Diferencia entre código fuente, proyecto, JDK, compilación y ejecución.

Demostración: Crear proyecto y ejecutar `System.out.println("Hola")`.

Práctica: Cada alumno crea y ejecuta su primer proyecto.

Comprobación: ¿Dónde está el archivo fuente que acabas de ejecutar?

### Sesión 208 — Estructura mínima de un programa Java

Explicación docente: Java organiza el código en clases; `main` es el punto de entrada.

Demostración: Señala línea a línea `public class Main` y `public static void main`.

Práctica: Escribir un programa mínimo sin copiar y ejecutarlo.

Comprobación: ¿Qué línea indica dónde empieza el programa?

### Sesión 209 — Salida por pantalla y mensajes del asistente

Explicación docente: La consola es la primera interfaz. La salida debe ser clara para el usuario.

Demostración: Comparar mensajes confusos con mensajes claros.

Práctica: Diseñar los primeros mensajes de MiniJarvis.

Comprobación: ¿Qué verá exactamente la persona usuaria al ejecutar?

### Sesión 210 — Variables

Explicación docente: Una variable guarda un dato que puede usarse varias veces.

Demostración: Cambia el valor de `userName` y muestra cómo afecta a varios mensajes.

Práctica: Crear y usar `userName`.

Comprobación: ¿Qué partes tiene una declaración de variable?

### Sesión 211 — Constantes

Explicación docente: Una constante representa un dato que no debe cambiar durante la ejecución.

Demostración: `final String ASSISTANT_NAME = "MiniJarvis";`.

Práctica: Añadir nombre del asistente y año como constantes.

Comprobación: ¿Por qué `ASSISTANT_NAME` es mejor como constante que como texto repetido?

### Sesión 212 — Entrada por teclado con Scanner

Explicación docente: `Scanner` permite leer información introducida por usuario.

Demostración: Leer una línea y usarla en un saludo.

Práctica: Pedir nombre y responder con ese nombre.

Comprobación: ¿Qué devuelve `nextLine()`?

### Sesión 213 — Limpieza, nombres claros y simplicidad

Explicación docente: Código limpio en H1 significa que se entiende, no que sea avanzado.

Demostración: Renombra `x` a `userName` y compara legibilidad.

Práctica: Revisar nombres, orden y comentarios.

Comprobación: ¿Qué línea de tu código no sabes explicar?

### Sesión 214 — README y evidencia de ejecución

Explicación docente: Un README permite que otra persona entienda y ejecute el proyecto.

Demostración: Modelo mínimo: qué hace, cómo ejecutar, ejemplo de salida, limitaciones.

Práctica: Crear README H1.

Comprobación: ¿Podría otro compañero ejecutar tu proyecto leyendo solo el README?

### Sesión 215 — Defensa y cierre H1

Explicación docente: Defender no es recitar; es explicar código propio y modificar algo simple.

Demostración: Preguntas modelo: qué es `main`, qué es una variable, qué hace `Scanner`.

Práctica: Defensa por parejas antes de defensa docente.

Comprobación: ¿Puedes cambiar el mensaje inicial sin romper el programa?

---

## H2 — Menú, decisiones, bucles y depuración

### Sesión 216 — Presentar H2 desde H1

Explicación docente: H1 era lineal; H2 será interactivo. La diferencia clave es repetir y decidir.

Demostración: Ejecuta una salida H1 y pregunta por qué termina.

Práctica: Diseñar comportamiento esperado del menú.

Comprobación: ¿Qué dos estructuras nuevas necesitamos?

### Sesión 217 — Diseño de comandos antes de programar

Explicación docente: Antes de programar hay que saber qué debe ocurrir con cada comando.

Demostración: Tabla comando-respuesta.

Práctica: Completar comandos `ayuda`, `saluda`, `estado`, `salir`, `otro`.

Comprobación: ¿Cómo probarías el comando `estado`?

### Sesión 218 — Booleanos y variable de control

Explicación docente: Un booleano representa verdadero/falso; servirá para controlar el bucle.

Demostración: `boolean running = true;` y cambio a `false`.

Práctica: Añadir variable `running`.

Comprobación: ¿Qué valor debe tener `running` al empezar?

### Sesión 219 — Bucle `while`

Explicación docente: `while` repite mientras una condición sea verdadera.

Demostración: Dibuja el ciclo: comprobar condición → ejecutar → volver a comprobar.

Práctica: Crear prompt repetido `>`.

Comprobación: ¿Qué puede provocar un bucle infinito?

### Sesión 220 — Condicionales `if/else`

Explicación docente: Un condicional permite ejecutar una rama u otra según una condición.

Demostración: Rama para `ayuda`, `estado` y `else`.

Práctica: Implementar tres comandos.

Comprobación: ¿Para qué sirve el último `else`?

### Sesión 221 — Comparación de textos en Java

Explicación docente: En Java los textos se comparan con `.equals()`, no con `==`.

Demostración: Mostrar fallo típico de `==` y corrección con `.equals()`.

Práctica: Normalizar comando con `trim().toLowerCase()`.

Comprobación: ¿Qué problema resuelve `trim()`?

### Sesión 222 — Comando `salir` y cierre controlado

Explicación docente: Salir no es cortar el programa; es cambiar el estado para terminar bien.

Demostración: `running = false` dentro de la rama `salir`.

Práctica: Implementar salida con mensaje final.

Comprobación: ¿Dónde cambia el valor de `running`?

### Sesión 223 — `switch` como alternativa controlada

Explicación docente: `switch` puede ser más legible cuando hay muchas opciones exactas.

Demostración: Reescribir dos comandos con `switch`.

Práctica: Comparar `if/else` y `switch` y elegir.

Comprobación: ¿Qué versión puedes defender mejor?

### Sesión 224 — Pruebas manuales

Explicación docente: Probar es comparar resultado esperado con resultado obtenido.

Demostración: Caso: entrada `ayuda`, esperado: lista de comandos.

Práctica: Crear tabla de pruebas H2.

Comprobación: ¿Qué prueba demuestra que comando desconocido está controlado?

### Sesión 225 — Depuración con breakpoint

Explicación docente: Depurar permite ver valores internos mientras el programa se ejecuta.

Demostración: Breakpoint después de leer `command`.

Práctica: Observar `command`, `running` y `userName`.

Comprobación: ¿Qué valor tenía `command` antes del condicional?

### Sesión 226 — Incidencias y corrección de errores

Explicación docente: Una incidencia documenta problema, causa, solución y verificación.

Demostración: Incidencia típica: `salir` no termina porque no cambia `running`.

Práctica: Documentar un error real.

Comprobación: ¿Cómo sabes que la solución arregló el problema?

### Sesión 227 — Comparación Java-Python H2

Explicación docente: El objetivo es comparar ideas: bucle, decisión y entrada.

Demostración: Mostrar `while` en Java y Python.

Práctica: Señalar equivalencias entre ambas versiones.

Comprobación: ¿Dónde aparece el equivalente de `.equals()` en Python?

### Sesión 228 — Demo, defensa y cierre H2

Explicación docente: H2 se supera si el menú funciona, se prueba, se depura y se defiende.

Demostración: Defensa modelo modificando un comando en directo.

Práctica: Demo y defensa.

Comprobación: ¿Puedes añadir un comando simple sin ayuda?

---

## H3 — Colecciones y memoria temporal

### Sesión 229 — Presentar H3: MiniJarvis empieza a recordar

Explicación docente: H3 añade memoria temporal; se pierde al cerrar el programa.

Demostración: Ejecuta H2 y muestra que no recuerda nada.

Práctica: Listar qué debería recordar el agente.

Comprobación: ¿Qué significa “temporal” en este hito?

### Sesión 230 — Elegir qué información guardar

Explicación docente: La estructura de datos depende del tipo de información y de cómo se consultará.

Demostración: Recuerdos simples frente a preferencias con clave.

Práctica: Decidir datos de memoria del equipo.

Comprobación: ¿Necesitas orden, clave o búsqueda?

### Sesión 231 — Introducción a `ArrayList`

Explicación docente: `ArrayList` guarda varios elementos en orden y permite recorrerlos.

Demostración: Añadir tres cadenas y mostrarlas numeradas.

Práctica: Mini-lista de tareas.

Comprobación: ¿Qué índice tiene el primer elemento?

### Sesión 232 — Introducción a `HashMap`

Explicación docente: `HashMap` guarda pares clave-valor.

Demostración: `nombre -> Laura`, `lenguaje -> Java`.

Práctica: Crear mapa de preferencias.

Comprobación: ¿Cuándo usarías mapa en vez de lista?

### Sesión 233 — Crear comando `recuerda`

Explicación docente: El comando debe pedir texto, validarlo y guardarlo.

Demostración: Flujo: comando → pregunta → entrada → `add`.

Práctica: Implementar `recuerda`.

Comprobación: ¿Dónde se guarda realmente el recuerdo?

### Sesión 234 — Crear comando `memoria`

Explicación docente: Consultar memoria implica recorrer la colección y mostrar contenido.

Demostración: Bucle `for` numerado.

Práctica: Implementar `memoria`.

Comprobación: ¿Cómo evitas mostrar una lista vacía sin explicación?

### Sesión 235 — Caso límite: memoria vacía

Explicación docente: Los programas deben responder bien cuando no hay datos.

Demostración: `if (memories.isEmpty())`.

Práctica: Añadir mensaje de memoria vacía.

Comprobación: ¿Qué prueba ejecutas antes de guardar nada?

### Sesión 236 — Caso límite: entrada vacía y repetidos

Explicación docente: Validar entrada evita datos inútiles o confusos.

Demostración: `text.isBlank()`.

Práctica: Decidir y programar política de entradas vacías y repetidas.

Comprobación: ¿Qué hará tu agente si el usuario pulsa Enter sin escribir?

### Sesión 237 — Comando `estado` con memoria

Explicación docente: El estado puede calcularse a partir de datos internos.

Demostración: `memories.size()`.

Práctica: Actualizar `estado` para mostrar número de recuerdos.

Comprobación: ¿Qué valor muestra si hay cero recuerdos?

### Sesión 238 — Pruebas de memoria

Explicación docente: Hay que probar memoria vacía, guardar, listar y casos raros.

Demostración: Tabla de prueba para `recuerda` y `memoria`.

Práctica: Completar pruebas H3.

Comprobación: ¿Qué caso demuestra que no guardas entradas vacías?

### Sesión 239 — Comparación Java-Python H3

Explicación docente: `ArrayList` se parece a `list`; `HashMap` se parece a `dict`.

Demostración: Misma operación en Java y Python.

Práctica: Comparar añadir, recorrer y consultar.

Comprobación: ¿Qué estructura de Python usarías para tu memoria?

### Sesión 240 — Portfolio y defensa H3

Explicación docente: Defender H3 es justificar colección, recorrido y casos límite.

Demostración: Pregunta modelo: “¿por qué elegiste `ArrayList`?”.

Práctica: Preparar defensa por parejas.

Comprobación: ¿Puedes explicar cómo crece la memoria al guardar?

### Sesión 241 — Cierre C1: demo parcial y recuperación

Explicación docente: Antes de POO deben estar claros `main`, bucles, condicionales y colecciones.

Demostración: Mapa de requisitos mínimos H1-H3.

Práctica: Demo parcial y plan de recuperación.

Comprobación: ¿Qué RA o evidencia tienes pendiente?

---

## H4 — Programación orientada a objetos

### Sesión 242 — Presentar H4: por qué necesitamos POO

Explicación docente: La POO aparece porque el código en `Main` mezcla demasiadas responsabilidades.

Demostración: Señala en H3 partes de entrada, menú, memoria y salida mezcladas.

Práctica: Marcar responsabilidades con colores.

Comprobación: ¿Qué responsabilidad separarías primero?

### Sesión 243 — Clase y objeto

Explicación docente: Una clase define estructura y comportamiento; un objeto es una instancia concreta.

Demostración: Clase `Memory`; objeto `memory` creado con `new Memory()`.

Práctica: Escribir dos ejemplos de clase y objeto del proyecto.

Comprobación: ¿`Memory` es clase u objeto? ¿Y `memory`?

### Sesión 244 — Atributos y métodos

Explicación docente: Atributos son datos internos; métodos son acciones que puede realizar el objeto.

Demostración: En `Memory`, `memories` es atributo; `remember` es método.

Práctica: Tabla de atributos y métodos de `Agent` y `Memory`.

Comprobación: ¿Qué sabe `Agent`? ¿Qué hace `Agent`?

### Sesión 245 — Constructor y estado inicial

Explicación docente: El constructor deja el objeto preparado para usarse.

Demostración: `public Memory() { this.memories = new ArrayList<>(); }`.

Práctica: Crear constructor de `Memory`.

Comprobación: ¿Qué pasaría si la lista no se inicializa?

### Sesión 246 — Encapsulación

Explicación docente: Encapsular es proteger el estado interno y ofrecer operaciones controladas.

Demostración: Cambiar lista pública por `private final List<String> memories`.

Práctica: Hacer privados atributos y usar métodos públicos.

Comprobación: ¿Por qué no debe cualquiera modificar directamente la lista?

### Sesión 247 — Extraer clase `Memory`

Explicación docente: Extraer clase significa mover responsabilidad sin cambiar comportamiento externo.

Demostración: Pasar `memories.add(text)` a `memory.remember(text)`.

Práctica: Extraer operaciones de memoria.

Comprobación: ¿Qué prueba demuestra que no has roto H3?

### Sesión 248 — Extraer clase `Agent`

Explicación docente: `Main` debe arrancar; `Agent` debe coordinar la conversación.

Demostración: `new Agent().run();` en `Main`.

Práctica: Crear `Agent` con método `run`.

Comprobación: ¿Qué código debe quedarse en `Main`?

### Sesión 249 — Relaciones entre clases

Explicación docente: Los objetos colaboran. `Agent` usa `Memory`, pero no debe hacer su trabajo.

Demostración: Diagrama simple `Main -> Agent -> Memory`.

Práctica: Describir relaciones del proyecto.

Comprobación: ¿Quién decide el flujo? ¿Quién guarda recuerdos?

### Sesión 250 — Diagrama de clases I

Explicación docente: UML básico ayuda a comunicar diseño.

Demostración: Caja con nombre, atributos y métodos.

Práctica: Dibujar `Main`, `Agent`, `Memory`.

Comprobación: ¿Aparece en el diagrama algo que no exista en el código?

### Sesión 251 — Diagrama de clases II: relación código-diagrama

Explicación docente: Un diagrama inventado no sirve; debe corresponder al código.

Demostración: Señala un atributo del diagrama y localízalo en Java.

Práctica: Completar documento relación diagrama-código.

Comprobación: ¿Dónde está en código esta relación?

### Sesión 252 — Diagrama de comportamiento

Explicación docente: Además de estructura, hay que explicar flujo.

Demostración: Flujo del comando `recuerda`: usuario → Agent → Memory → respuesta.

Práctica: Dibujar flujo de un comando.

Comprobación: ¿Qué objeto actúa primero?

### Sesión 253 — Revisión de responsabilidades

Explicación docente: Una clase decorativa no aporta; una clase útil tiene responsabilidad clara.

Demostración: Preguntas: qué sabe, qué hace, qué no debe hacer.

Práctica: Revisar cada clase con esas preguntas.

Comprobación: ¿Qué método está en una clase incorrecta?

### Sesión 254 — Comparación Java-Python H4

Explicación docente: Java usa visibilidad formal; Python usa convenciones.

Demostración: Constructor Java frente a `__init__` en Python.

Práctica: Comparar `Memory` en ambos lenguajes.

Comprobación: ¿Cómo se indica en Python que algo no debería tocarse desde fuera?

### Sesión 255 — Pruebas de regresión H4

Explicación docente: Cambiar diseño no debe romper comportamiento ya logrado.

Demostración: Ejecutar pruebas de H3 sobre código H4.

Práctica: Checklist de regresión.

Comprobación: ¿Qué comando funcionaba antes y debe seguir funcionando?

### Sesión 256 — README, portfolio y registro IA H4

Explicación docente: En H4 hay que documentar diseño, no solo ejecución.

Demostración: Sección README: clases principales y responsabilidades.

Práctica: Actualizar documentación.

Comprobación: ¿Puede otra persona entender tu diseño leyendo el README?

### Sesión 257 — Defensa H4

Explicación docente: Defensa POO exige explicar clases, objetos, responsabilidades y relaciones.

Demostración: Defensa modelo sobre `Memory`.

Práctica: Defensa individual.

Comprobación: ¿Puedes explicar una clase sin leer literalmente el código?

---

## H5 — Extensibilidad, clean code, Git y patrones

### Sesión 258 — Presentar H5: añadir sin romper

Explicación docente: Un diseño extensible reduce cambios necesarios para añadir funcionalidad.

Demostración: Pregunta: para añadir `resumen`, ¿qué archivos tocaríamos?

Práctica: Diagnóstico de rigidez.

Comprobación: ¿Qué parte del diseño se repite demasiado?

### Sesión 259 — Clean code I: nombres y duplicación

Explicación docente: Código limpio es código que se entiende y se cambia con menos riesgo.

Demostración: Mal nombre `x` frente a `command`.

Práctica: Checklist de nombres, duplicación y tamaño.

Comprobación: ¿Qué nombre mejorarías hoy?

### Sesión 260 — Refactorización controlada

Explicación docente: Refactorizar mejora estructura sin cambiar comportamiento.

Demostración: Extraer método o renombrar variable y ejecutar pruebas.

Práctica: Refactor pequeño documentado.

Comprobación: ¿Qué prueba demuestra que el comportamiento no cambió?

### Sesión 261 — Herramientas internas

Explicación docente: Una herramienta encapsula una acción del agente.

Demostración: `HelpTool`, `RememberTool`, `MemoryTool`.

Práctica: Tabla de herramientas y responsabilidades.

Comprobación: ¿Qué responsabilidad tiene `HelpTool`?

### Sesión 262 — Interfaz `Tool`

Explicación docente: Una interfaz define un contrato común.

Demostración: `Tool` con `name`, `description`, `execute`.

Práctica: Crear primera implementación.

Comprobación: ¿Qué obliga a implementar una interfaz?

### Sesión 263 — Implementar `HelpTool`

Explicación docente: `Agent` delega en herramientas para no crecer indefinidamente.

Demostración: `HelpTool.execute()` muestra comandos.

Práctica: Extraer ayuda a clase propia.

Comprobación: ¿Qué código salió de `Agent`?

### Sesión 264 — Implementar `RememberTool`

Explicación docente: Las herramientas pueden necesitar colaborar con otros objetos.

Demostración: `RememberTool` usa `Memory`.

Práctica: Implementar guardar recuerdo como herramienta.

Comprobación: ¿Qué dependencia necesita `RememberTool`?

### Sesión 265 — Implementar `MemoryTool` y `StatusTool`

Explicación docente: Repetir la misma estructura permite crear una familia de herramientas.

Demostración: Dos herramientas con mismo contrato y distinta acción.

Práctica: Extraer memoria y estado.

Comprobación: ¿Qué tienen en común las herramientas?

### Sesión 266 — Registro de herramientas en `Agent`

Explicación docente: El agente puede buscar una herramienta por nombre en vez de tener un condicional enorme.

Demostración: Mapa `nombre -> Tool`.

Práctica: Registrar herramientas y ejecutar por comando.

Comprobación: ¿Qué cambia para añadir una herramienta nueva?

### Sesión 267 — Patrón Command simplificado

Explicación docente: El patrón Command encapsula una acción como objeto. Aquí solo se nombra si el diseño lo justifica.

Demostración: Cada `Tool` se parece a un comando ejecutable.

Práctica: Decidir si se usa o se descarta el patrón.

Comprobación: ¿Qué problema real resuelve en tu proyecto?

### Sesión 268 — Git profesional I: commits y ramas

Explicación docente: Git permite trazabilidad y recuperación. Un commit debe explicar un cambio coherente.

Demostración: Mensajes malos y buenos de commit.

Práctica: Revisar historial o crear registro equivalente.

Comprobación: ¿Qué cambio demuestra tu último commit?

### Sesión 269 — Git profesional II: revisión de código

Explicación docente: Revisar código mejora el producto y reparte conocimiento.

Demostración: Comentario útil frente a comentario vago.

Práctica: Revisión cruzada con checklist.

Comprobación: ¿Qué sugerencia aceptaste y por qué?

### Sesión 270 — Comparación Java-Python H5

Explicación docente: Java formaliza contratos; Python puede funcionar por convenciones o duck typing.

Demostración: Interfaz Java frente a clase Python con método esperado.

Práctica: Comparar herramienta Java/Python.

Comprobación: ¿Qué ventaja tiene la interfaz en Java?

### Sesión 271 — Pruebas tras refactorización

Explicación docente: Toda mejora estructural necesita pruebas de regresión.

Demostración: Ejecutar comandos antes y después de extraer herramientas.

Práctica: Checklist de pruebas H5.

Comprobación: ¿Qué funcionalidad podría haberse roto?

### Sesión 272 — README y documentación técnica H5

Explicación docente: Documentar H5 implica explicar cómo se añade una herramienta.

Demostración: Apartado “Cómo añadir una nueva Tool”.

Práctica: Actualizar README.

Comprobación: ¿Podría otro equipo añadir una herramienta leyendo tu README?

### Sesión 273 — Portfolio y registro IA H5

Explicación docente: Si IA ayudó a refactorizar o sugerir patrones, debe quedar registrado y verificado.

Demostración: Registro de prompt de refactorización.

Práctica: Completar portfolio y registro.

Comprobación: ¿Qué parte aceptaste y qué modificaste tú?

### Sesión 274 — Demo y defensa H5

Explicación docente: La defensa debe mostrar extensibilidad, refactorización y criterio sobre patrones.

Demostración: Añadir una herramienta mínima en directo o explicar cómo hacerlo.

Práctica: Demo y defensa.

Comprobación: ¿Puedes añadir una herramienta sin tocar muchas clases?

---

## C2 — Cierre segunda evaluación

### Sesión 275 — Revisión técnica H4-H5

Explicación docente: Antes de persistir datos hay que tener diseño entendible.

Demostración: Checklist de clases, herramientas, README, Git y pruebas.

Práctica: Revisión global.

Comprobación: ¿Qué evidencia falta para cerrar C2?

### Sesión 276 — Defensa individual C2

Explicación docente: La defensa individual valida lo que cada persona entiende del trabajo grupal.

Demostración: Preguntas sobre `Agent`, `Memory`, `Tool`, Git y pruebas.

Práctica: Defensa individual.

Comprobación: ¿Qué aportación concreta puedes demostrar?

### Sesión 277 — Recuperación específica C2

Explicación docente: Recuperar es demostrar el RA pendiente con una evidencia concreta.

Demostración: Si falla POO, extraer una clase pequeña; si falla Git, explicar commits.

Práctica: Tarea individual dirigida.

Comprobación: ¿Qué RA estás recuperando?

### Sesión 278 — Preparación para persistencia

Explicación docente: La persistencia permite que la memoria sobreviva entre ejecuciones.

Demostración: Cerrar el programa y perder recuerdos.

Práctica: Diseñar qué datos guardar.

Comprobación: ¿Qué riesgos aparecen al guardar datos?

---

## H6 — Persistencia, logs y seguridad

### Sesión 279 — Presentar H6: memoria persistente

Explicación docente: Persistencia significa guardar información fuera de la memoria RAM del programa.

Demostración: Guardar, cerrar, abrir y comprobar pérdida actual.

Práctica: Definir qué debe persistir.

Comprobación: ¿Qué debe sobrevivir entre ejecuciones?

### Sesión 280 — Formato de fichero

Explicación docente: Un formato simple facilita leer, probar y depurar.

Demostración: `data/recuerdos.txt`, una línea por recuerdo.

Práctica: Diseñar formato y ejemplos ficticios.

Comprobación: ¿Cómo sabrás leer ese formato después?

### Sesión 281 — Escritura de ficheros

Explicación docente: Escribir en fichero guarda datos fuera del programa.

Demostración: `Files.writeString` con `CREATE` y `APPEND`.

Práctica: Guardar recuerdos en `data/recuerdos.txt`.

Comprobación: ¿Dónde se crea el fichero?

### Sesión 282 — Lectura de ficheros

Explicación docente: Leer permite reconstruir memoria al iniciar.

Demostración: `Files.readAllLines`.

Práctica: Cargar recuerdos desde fichero.

Comprobación: ¿Qué ocurre si el fichero está vacío?

### Sesión 283 — Clase `PersistentMemory`

Explicación docente: La persistencia debe estar separada de la interacción del agente.

Demostración: `PersistentMemory` con `save` y `load`.

Práctica: Encapsular lectura y escritura.

Comprobación: ¿Por qué no debe hacerlo todo `Agent`?

### Sesión 284 — Errores de fichero

Explicación docente: Los ficheros pueden no existir, estar vacíos o fallar por permisos.

Demostración: Ejecutar sin carpeta `data` y corregir con `createDirectories`.

Práctica: Documentar y controlar un error.

Comprobación: ¿Qué mensaje recibe el usuario si falla?

### Sesión 285 — Logs e historial

Explicación docente: Un log registra eventos para trazabilidad, no debe guardar secretos.

Demostración: Línea de log: fecha simple, acción, resultado.

Práctica: Crear `logs/historial.log`.

Comprobación: ¿Qué información no debe aparecer en el log?

### Sesión 286 — Seguridad de datos

Explicación docente: Nunca subir claves, `.env` real, tokens ni datos personales.

Demostración: Diferencia entre `.env` y `.env.example`.

Práctica: Revisar repositorio con checklist.

Comprobación: ¿Qué harías si una clave se sube por error?

### Sesión 287 — README reproducible

Explicación docente: Reproducible significa que otra persona puede seguir pasos desde cero.

Demostración: Probar README de otro equipo.

Práctica: Actualizar instrucciones H6.

Comprobación: ¿Qué paso falta si otro equipo no puede ejecutar?

### Sesión 288 — Pruebas de persistencia

Explicación docente: La prueba clave es segunda ejecución: guardar, cerrar, abrir, consultar.

Demostración: Ejecutar prueba completa.

Práctica: Completar pruebas H6.

Comprobación: ¿Qué prueba demuestra persistencia real?

### Sesión 289 — Comparación Java-Python H6

Explicación docente: Ambos lenguajes pueden leer y escribir ficheros; cambia la API y la verbosidad.

Demostración: Java `Files.readAllLines` frente a Python `open`.

Práctica: Comparar lectura y escritura.

Comprobación: ¿Qué parte es más explícita en Java?

### Sesión 290 — Portfolio y registro IA H6

Explicación docente: Si IA ayuda con ficheros, revisar rutas, excepciones y seguridad.

Demostración: Prompt para pedir explicación de `Files.writeString` y registro asociado.

Práctica: Completar portfolio y registro.

Comprobación: ¿Qué verificaste antes de aceptar código de IA?

### Sesión 291 — Demo y defensa H6

Explicación docente: H6 se defiende demostrando guardar, cerrar, abrir y recuperar.

Demostración: Demo completa de persistencia.

Práctica: Defensa individual.

Comprobación: ¿Dónde se guardan los datos y cómo se cargan?

---

## H7 — IA responsable real o simulada

### Sesión 292 — Decidir alcance H7

Explicación docente: La simulación robusta es una opción válida y segura.

Demostración: Comparar riesgos de API real frente a simulador local.

Práctica: Elegir alcance del equipo.

Comprobación: ¿Qué opción es más defendible para tu equipo?

### Sesión 293 — Caso de uso IA y seguridad de prompts

Explicación docente: La IA debe tener un caso limitado y no recibir datos sensibles.

Demostración: Prompt seguro e inseguro.

Práctica: Diseñar caso de uso y riesgos.

Comprobación: ¿Qué datos no enviarás nunca?

### Sesión 294 — Implementar simulación o integración

Explicación docente: Lo importante es que el modo IA sea controlado, no espectacular.

Demostración: `SimulatedAiAssistant` con respuestas y bloqueo de secretos.

Práctica: Implementar simulación o integración segura.

Comprobación: ¿Qué hace tu agente si detecta una contraseña?

### Sesión 295 — Registro de prompts y validación humana

Explicación docente: Toda respuesta de IA debe validarse; no se acepta automáticamente.

Demostración: Registro: prompt, respuesta, aceptación, modificación, verificación.

Práctica: Completar registro y validación.

Comprobación: ¿Qué respuesta no aceptarías sin revisar?

### Sesión 296 — Demo y defensa H7

Explicación docente: Defender IA significa explicar qué hace, qué no hace, qué datos recibe y qué riesgos tiene.

Demostración: Preguntas de defensa IA.

Práctica: Demo y defensa.

Comprobación: ¿Dónde están los límites de tu modo IA?

---

## HF — Cierre, portfolio, recuperación y defensa

### Sesión 297 — Reentrada tras FFEOE y diagnóstico final

Explicación docente: Ya no se abre un proyecto nuevo; se cierra, recupera y mejora.

Demostración: Checklist final de evidencias.

Práctica: Diagnóstico por alumno y equipo.

Comprobación: ¿Qué evidencia falta para cerrar?

### Sesión 298 — Preparar demo final

Explicación docente: Una buena demo cuenta evolución y decisiones, no solo enseña una pantalla.

Demostración: Guion: problema, evolución, demo, pruebas, límites.

Práctica: Preparar guion de demo.

Comprobación: ¿Qué hito demuestra mejor vuestra evolución?

### Sesión 299 — Portfolio final

Explicación docente: El portfolio es relato técnico con evidencias, no acumulación de archivos.

Demostración: Afirmación sin evidencia frente a afirmación con enlace/captura/código.

Práctica: Completar portfolio.

Comprobación: ¿Cada aprendizaje importante tiene evidencia?

### Sesión 300 — README final y reproducibilidad

Explicación docente: El README final debe permitir ejecutar y entender el proyecto completo.

Demostración: Checklist de README final.

Práctica: Probar README desde cero.

Comprobación: ¿Qué necesita instalar o abrir una persona externa?

### Sesión 301 — Registro IA final y seguridad

Explicación docente: El registro IA final protege autoría, seguridad y aprendizaje.

Demostración: Revisar un registro incompleto y corregirlo.

Práctica: Completar registros faltantes.

Comprobación: ¿Qué uso de IA afectó más a tu proyecto?

### Sesión 302 — Recuperación específica I

Explicación docente: Recuperar Programación exige demostrar código y comprensión del RA pendiente.

Demostración: Ejemplos de recuperación: bucle, colección, clase o fichero.

Práctica: Tarea individual dirigida.

Comprobación: ¿Qué concepto estás demostrando?

### Sesión 303 — Recuperación específica II

Explicación docente: Recuperar Entornos exige evidencia de herramienta, proceso o documentación.

Demostración: Depuración, Git, UML, README o pruebas según caso.

Práctica: Completar evidencia pendiente.

Comprobación: ¿Cómo se verifica tu evidencia?

### Sesión 304 — Ensayo de defensa individual

Explicación docente: La defensa se prepara entendiendo, no memorizando.

Demostración: Simulación de pregunta inesperada sobre código.

Práctica: Defensa por parejas con preguntas cruzadas.

Comprobación: ¿Qué pregunta todavía te cuesta responder?

### Sesión 305 — Presentaciones finales

Explicación docente: La presentación debe equilibrar producto, proceso, pruebas, IA y aprendizaje.

Demostración: Rúbrica de presentación.

Práctica: Demo final por equipos.

Comprobación: ¿Qué decisión técnica defendió mejor el equipo?

### Sesión 306 — Defensa final, cierre y retrospectiva del curso

Explicación docente: El cierre valida producto funcional, proceso trazable y comprensión defendible.

Demostración: Pregunta final global: qué construyes, cómo lo pruebas, cómo lo documentas y cómo lo defiendes.

Práctica: Defensa individual y retrospectiva final.

Comprobación: ¿Qué sabes hacer ahora que no sabías al empezar?

---

## 4. Banco de preguntas rápidas por bloque

### H1

- ¿Dónde empieza el programa?
- ¿Qué diferencia hay entre variable y constante?
- ¿Qué hace `Scanner`?
- ¿Qué ocurre si cambio el valor de `userName`?

### H2

- ¿Qué condición mantiene vivo el bucle?
- ¿Por qué usamos `.equals()`?
- ¿Qué prueba demuestra que `salir` funciona?
- ¿Qué variable observaste con el depurador?

### H3

- ¿Por qué elegiste esa colección?
- ¿Cómo gestionas memoria vacía?
- ¿Cómo recorres los recuerdos?
- ¿Qué diferencia hay entre `ArrayList` y `HashMap`?

### H4

- ¿Qué responsabilidad tiene esta clase?
- ¿Qué atributo está encapsulado?
- ¿Qué hace el constructor?
- ¿Dónde se ve esta relación en el código?

### H5

- ¿Qué mejora aportó la refactorización?
- ¿Qué obliga a hacer `Tool`?
- ¿Qué problema resuelve el patrón Command simplificado?
- ¿Qué commit demuestra tu aportación?

### H6

- ¿Dónde se guardan los recuerdos?
- ¿Qué pasa si el fichero no existe?
- ¿Qué prueba demuestra persistencia?
- ¿Qué datos no deben aparecer en logs?

### H7

- ¿Qué datos recibe la IA o simulación?
- ¿Cómo validas una respuesta?
- ¿Qué riesgo has mitigado?
- ¿Qué hace y qué no hace el modo IA?

### HF

- ¿Qué evidencia demuestra tu aprendizaje principal?
- ¿Qué parte del proyecto puedes modificar en directo?
- ¿Qué uso de IA registraste?
- ¿Qué mejorarías si tuvieras otra iteración?
