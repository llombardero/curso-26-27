# Guía docente completa — H6 sesión a sesión

## Agente persistente y trazable — MiniJarvis H6

## Programación + Entornos de Desarrollo — 1.º DAW — Curso 2026/2027

Versión: borrador 0.1

Documento autónomo para uso del profesorado.

Este documento permite impartir H6 completo sin abrir ningún otro material durante la clase.

---

## 1. Propósito de H6

H6 hace que MiniJarvis deje de depender solo de la memoria temporal.

Producto final:

```text
MiniJarvis H6: agente por consola con recuerdos persistentes en fichero, historial técnico simple, ejecución reproducible, pruebas de persistencia y decisiones básicas de seguridad documentadas.
```

H6 introduce:

```text
- problema de memoria que desaparece al cerrar el programa;
- lectura y escritura de ficheros de texto;
- creación segura de carpetas `data/` y `logs/`;
- clase `PersistentMemory`;
- clase `HistoryLog`;
- comando o herramienta para guardar/cargar recuerdos;
- pruebas de persistencia entre dos ejecuciones;
- README reproducible desde cero;
- documento de seguridad: sin secretos, sin `.env` real, sin datos personales reales;
- gestión de incidencias sencillas;
- comparación Java ↔ Python sobre ficheros;
- defensa H6.
```

Idea docente central:

```text
H6 no consiste solo en escribir un fichero. H6 consiste en demostrar que MiniJarvis puede cerrar, volver a abrirse y recuperar información de forma reproducible, trazable y segura.
```

---

## 2. Restricciones de H6

En H6 sí entra:

```text
[x] Guardar recuerdos en `data/recuerdos.txt` o equivalente.
[x] Cargar recuerdos al iniciar o al consultar.
[x] Crear carpetas con `Files.createDirectories(...)`.
[x] Registrar eventos técnicos simples en `logs/historial.log`.
[x] Probar persistencia en dos ejecuciones.
[x] Documentar cómo ejecutar desde cero.
[x] Documentar qué datos no se deben guardar.
[x] Revisar `.gitignore` para secretos y ficheros sensibles.
[x] Registrar una incidencia si algo falla.
[x] Comparar lectura/escritura Java ↔ Python.
[x] Defender persistencia, trazabilidad y seguridad.
```

En H6 todavía NO entra:

```text
[ ] Base de datos obligatoria.
[ ] API externa.
[ ] IA real obligatoria.
[ ] Credenciales reales.
[ ] `.env` real subido al repositorio.
[ ] Tokens, claves API o contraseñas.
[ ] Datos personales reales de alumnado, familias o profesorado.
[ ] Cifrado avanzado obligatorio.
[ ] Logging profesional con frameworks externos.
```

Frase docente:

```text
Si un recuerdo contiene una contraseña, un teléfono real o un dato personal, no es un buen ejemplo de H6. Persistir información también exige decidir qué NO se debe guardar.
```

---

## 3. Diseño mínimo de referencia

Partimos de H5:

```text
Main arranca.
Agent coordina.
Tool representa comandos/herramientas.
Memory recuerda durante la ejecución.
```

En H6 añadimos persistencia y trazabilidad:

| Clase/interfaz | Responsabilidad |
|---|---|
| `Main` | Crear y arrancar `Agent`. |
| `Agent` | Orquestar herramientas y compartir memoria/log. |
| `Tool` | Contrato común de herramientas. |
| `PersistentMemory` | Mantener recuerdos en memoria y guardarlos/cargarlos desde fichero. |
| `HistoryLog` | Registrar eventos técnicos simples. |
| `RememberTool` | Pedir un recuerdo y guardarlo. |
| `MemoryTool` | Mostrar recuerdos cargados. |
| `SaveTool` | Forzar guardado si se usa guardado manual. |
| `StatusTool` | Mostrar estado de recuerdos y rutas. |
| `HelpTool` | Mostrar comandos. |
| `ExitTool` | Registrar salida y terminar. |

Estructura esperada:

```text
h6-persistente-trazable/
├── README.md
├── .gitignore
├── src/
│   ├── Main.java
│   ├── Agent.java
│   ├── Tool.java
│   ├── PersistentMemory.java
│   ├── HistoryLog.java
│   ├── HelpTool.java
│   ├── RememberTool.java
│   ├── MemoryTool.java
│   ├── SaveTool.java
│   ├── StatusTool.java
│   └── ExitTool.java
├── data/
│   └── recuerdos.txt
├── logs/
│   └── historial.log
└── docs/
    ├── pruebas-persistencia-h6.md
    ├── seguridad-h6.md
    ├── logs-historial-h6.md
    ├── incidencia-h6.md
    ├── comparacion-java-python-h6.md
    ├── portfolio-h6.md
    ├── registro-ia.md
    └── defensa-h6.md
```

Código orientativo mínimo para explicar la meta:

```java
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;

public class PersistentMemory {
    private ArrayList<String> memories;
    private Path filePath;

    public PersistentMemory(String fileName) {
        this.memories = new ArrayList<>();
        this.filePath = Path.of(fileName);
        load();
    }

    public void add(String text) {
        if (text != null && !text.trim().isEmpty()) {
            memories.add(text.trim());
            save();
        }
    }

    public void load() {
        try {
            Files.createDirectories(filePath.getParent());
            if (Files.exists(filePath)) {
                memories.clear();
                memories.addAll(Files.readAllLines(filePath));
            }
        } catch (IOException e) {
            System.out.println("No se pudo cargar la memoria: " + e.getMessage());
        }
    }

    public void save() {
        try {
            Files.createDirectories(filePath.getParent());
            Files.write(filePath, memories);
        } catch (IOException e) {
            System.out.println("No se pudo guardar la memoria: " + e.getMessage());
        }
    }

    public int count() {
        return memories.size();
    }
}
```

```java
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.time.LocalDateTime;

public class HistoryLog {
    private Path logPath;

    public HistoryLog(String fileName) {
        this.logPath = Path.of(fileName);
    }

    public void record(String event) {
        try {
            Files.createDirectories(logPath.getParent());
            String line = LocalDateTime.now() + " - " + event + System.lineSeparator();
            Files.writeString(logPath, line, java.nio.file.StandardOpenOption.CREATE, java.nio.file.StandardOpenOption.APPEND);
        } catch (IOException e) {
            System.out.println("No se pudo escribir el historial: " + e.getMessage());
        }
    }
}
```

Nota didáctica:

```text
Los ejemplos usan ficheros de texto para que el alumnado pueda abrirlos, inspeccionarlos y entender qué ocurre. No hace falta introducir bases de datos para aprender persistencia básica.
```

---

## 4. Secuencia de sesiones H6

Preparación docente antes de iniciar H6:

```text
1. Tener un H5 funcional o un caso mínimo con Agent, Tool y recuerdos.
2. Preparar una demostración de que la memoria temporal desaparece al cerrar el programa.
3. Preparar carpetas `data/` y `logs/` como idea, pero dejar que el alumnado entienda por qué se crean.
4. Tener decidido si el guardado será automático al añadir recuerdo o mediante comando `guardar`.
5. Priorizar guardado automático si el grupo necesita simplicidad.
6. Tener clara la política de seguridad: ejemplos ficticios, ningún secreto, ningún dato personal real.
7. Recordar que H6 no introduce IA real; eso queda para H7 de forma responsable o simulada.
```

Material mínimo de aula:

```text
- editor o IDE Java;
- terminal para compilar y ejecutar;
- posibilidad de borrar o renombrar temporalmente `data/` y `logs/`;
- pizarra para flujo guardar/cargar;
- ficha de pruebas de persistencia;
- registro de seguridad;
- registro de incidencia si algo falla.
```

Propuesta de 10 sesiones de 45 minutos.

| Sesión | Foco | Producto parcial |
|---|---|---|
| H6-S1 | Presentar el problema: memoria temporal desaparece | Diagnóstico de persistencia. |
| H6-S2 | Ficheros, rutas y carpetas seguras | Diseño `data/recuerdos.txt` y `logs/historial.log`. |
| H6-S3 | Crear `PersistentMemory` | Clase que carga y guarda recuerdos. |
| H6-S4 | Integrar persistencia con herramientas | `RememberTool`/`MemoryTool` usando memoria persistente. |
| H6-S5 | Crear `HistoryLog` | Historial técnico simple. |
| H6-S6 | Pruebas de persistencia en dos ejecuciones | Documento de pruebas. |
| H6-S7 | Seguridad: secretos, `.env`, datos personales y `.gitignore` | Documento de seguridad. |
| H6-S8 | README reproducible e incidencias | README + incidencia si procede. |
| H6-S9 | Comparación Java ↔ Python y documentación H6 | Comparación + portfolio/registro IA. |
| H6-S10 | Defensa H6 | Revisión, defensa y cierre. |

---

# H6-S1 — Presentar el problema: memoria temporal desaparece

## Duración

```text
45 minutos
```

## Objetivo

Que el alumnado entienda la diferencia entre memoria temporal y persistencia, y detecte por qué H6 es necesario.

## Resultado esperado

Diagnóstico breve:

```text
En H5 MiniJarvis recuerda mientras está abierto.
Al cerrar el programa, los recuerdos desaparecen.
En H6 necesitamos guardar en un fichero para recuperarlos después.
```

## Guion docente

```text
En H3 aprendimos memoria temporal. En H4 organizamos el código. En H5 hicimos el agente más extensible.

Pero todavía hay un problema importante: si cierro MiniJarvis, todo lo que recordaba se pierde.

H6 nace para resolver ese problema. Ahora el reto no es añadir muchos comandos, sino guardar y recuperar información de forma reproducible y segura.
```

## Pizarra

```text
Memoria temporal:
- vive mientras el programa está abierto;
- desaparece al cerrar.

Persistencia:
- se guarda fuera del programa;
- puede recuperarse en otra ejecución.

H6 = persistencia + trazabilidad + seguridad básica
```

## Qué explicas tú

```text
- Qué significa persistir información.
- Diferencia informal entre RAM y fichero.
- Por qué necesitamos una prueba en dos ejecuciones.
- Por qué guardar datos implica responsabilidad y seguridad.
```

## Actividad HEXA guiada

### H — Hecho

MiniJarvis H5 guarda recuerdos en memoria durante la ejecución.

### E — Explorar

Pregunta:

```text
¿Qué ocurre si guardo “Traer libreta”, cierro el programa y vuelvo a abrirlo?
```

Respuestas esperadas:

```text
- en H5 se pierde;
- en H6 debería recuperarse;
- necesitamos un fichero para comprobarlo.
```

### X — eXplicar

Conclusión:

```text
Persistencia significa que el dato sobrevive al cierre del programa.
```

### A — Aplicar

El alumnado escribe el flujo deseado:

```text
Ejecución 1:
recuerda -> Traer libreta -> salir

Ejecución 2:
memoria -> debe aparecer Traer libreta
```

## Actividad

```text
1. Ejecutar o imaginar H5.
2. Guardar un recuerdo ficticio.
3. Cerrar el programa.
4. Explicar por qué se pierde.
5. Diseñar la prueba que H6 deberá superar.
```

Ejemplos seguros de recuerdos:

```text
Traer libreta
Repasar ArrayList
Preparar defensa H6
```

Ejemplos no seguros:

```text
Mi contraseña es 1234
Teléfono real de una persona
Dirección real
Token de una API
```

## Errores frecuentes

| Error | Señal | Intervención docente |
|---|---|---|
| Confundir memoria temporal con persistencia | “Ya lo guardo en ArrayList” | Cerrar y abrir como prueba mental. |
| Pensar en base de datos inmediatamente | Proponen MySQL | Reencuadrar: fichero de texto primero. |
| Usar datos personales como ejemplos | Escriben datos reales | Sustituir por datos ficticios. |
| No definir prueba | “Creo que funciona” | Exigir dos ejecuciones. |

## Cierre

Ticket:

```text
1. ¿Qué diferencia hay entre memoria temporal y persistente?
2. ¿Qué fichero usaremos para recuerdos?
3. Escribe un ejemplo seguro de recuerdo ficticio.
```

## Criterio de éxito

```text
El alumnado entiende el problema de persistencia y puede describir una prueba en dos ejecuciones para comprobar H6.
```

---

# H6-S2 — Ficheros, rutas y carpetas seguras

## Duración

```text
45 minutos
```

## Objetivo

Diseñar las rutas de persistencia y comprender por qué el programa debe crear carpetas antes de leer o escribir.

## Resultado esperado

Diseño de rutas:

```text
data/recuerdos.txt
logs/historial.log
```

y explicación de qué contiene cada fichero.

## Guion docente

```text
Antes de escribir código, decidimos dónde vivirá la información.

Usaremos una carpeta data para recuerdos y una carpeta logs para historial técnico. Así se separan los datos de uso del código fuente.

Además, el programa debe funcionar desde cero. Si data o logs no existen, debe crearlas.
```

## Pizarra

```text
src/  = código
 data/ = recuerdos ficticios persistentes
logs/ = historial técnico simple
```

Regla:

```text
Antes de escribir:
Files.createDirectories(ruta.getParent())
```

## Qué explicas tú

```text
- Qué es una ruta relativa.
- Por qué `data/recuerdos.txt` es más claro que guardar en cualquier sitio.
- Por qué `logs/historial.log` no debe contener secretos.
- Qué problema ocurre si una carpeta no existe.
```

## Actividad HEXA guiada

### H — Hecho

Queremos escribir en `data/recuerdos.txt`.

### E — Explorar

Pregunta:

```text
¿Qué puede fallar si la carpeta data no existe?
```

### X — eXplicar

Respuesta esperada:

```text
El programa no podrá crear el fichero y lanzará un error de entrada/salida.
```

### A — Aplicar

Diseñar rutas y responsabilidades.

## Código explicativo

```java
Path memoryPath = Path.of("data/recuerdos.txt");
Files.createDirectories(memoryPath.getParent());
```

Explicación docente:

```text
`Path.of(...)` representa la ruta.
`getParent()` obtiene la carpeta `data`.
`createDirectories` crea la carpeta si no existe y no falla si ya existe.
```

## Actividad

```text
1. Dibujar la estructura de carpetas H6.
2. Escribir qué contiene `data/recuerdos.txt`.
3. Escribir qué contiene `logs/historial.log`.
4. Marcar qué datos no deben aparecer en ninguno de los dos.
```

Tabla:

| Fichero | Contenido permitido | Contenido prohibido |
|---|---|---|
| `data/recuerdos.txt` | recuerdos ficticios | contraseñas, teléfonos reales, datos personales |
| `logs/historial.log` | eventos técnicos simples | tokens, rutas sensibles, datos personales |

## Errores frecuentes

| Error | Señal | Intervención docente |
|---|---|---|
| Ruta absoluta del ordenador personal | `C:\Users\...` o `/home/...` | Usar ruta relativa para reproducibilidad. |
| No crear carpetas | Error al guardar | Añadir `Files.createDirectories`. |
| Mezclar código y datos | Guardan recuerdos en `src/` | Separar `src`, `data`, `logs`. |
| Logs con información sensible | Registran texto completo peligroso | Reducir logs a eventos técnicos. |

## Cierre

Ticket:

```text
1. ¿Para qué sirve la carpeta data?
2. ¿Para qué sirve la carpeta logs?
3. ¿Por qué conviene usar rutas relativas?
```

## Criterio de éxito

```text
El alumnado diseña rutas reproducibles y entiende que el programa debe crear carpetas antes de persistir información.
```

---

# H6-S3 — Crear PersistentMemory

## Duración

```text
45 minutos
```

## Objetivo

Crear una clase `PersistentMemory` que pueda cargar y guardar recuerdos en un fichero de texto.

## Resultado esperado

Archivo `src/PersistentMemory.java` con:

```text
- lista interna de recuerdos;
- ruta del fichero;
- constructor que carga recuerdos;
- método add;
- método save;
- método load;
- método count;
- método formatMemories.
```

## Guion docente

```text
Vamos a convertir la memoria de MiniJarvis en memoria persistente.

La clase PersistentMemory tendrá dos responsabilidades conectadas: mantener recuerdos durante la ejecución y sincronizarlos con un fichero.

No debe pedir datos por teclado. No debe decidir comandos. Solo gestiona recuerdos y fichero.
```

## Pizarra

```text
PersistentMemory sabe:
- qué recuerdos hay;
- dónde se guardan;
- cómo cargar;
- cómo guardar.

PersistentMemory NO sabe:
- qué comando escribió el usuario;
- cómo se muestra el menú;
- cuándo termina el agente.
```

## Qué explicas tú

```text
- Lectura de líneas con `Files.readAllLines`.
- Escritura de líneas con `Files.write`.
- Manejo básico de `IOException`.
- Por qué el constructor puede llamar a `load()`.
- Por qué conviene mantener mensajes de error comprensibles.
```

## Actividad HEXA guiada

### H — Hecho

Tenemos una lista de recuerdos y queremos que viva también en un fichero.

### E — Explorar

Pregunta:

```text
¿Qué métodos necesita una memoria persistente?
```

Respuestas esperadas:

```text
- cargar;
- guardar;
- añadir;
- contar;
- mostrar.
```

### X — eXplicar

Conclusión:

```text
PersistentMemory encapsula la lista y el fichero, igual que Memory encapsulaba la lista en H4.
```

### A — Aplicar

Crear clase con métodos mínimos.

## Código base guiado

```java
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;

public class PersistentMemory {
    private ArrayList<String> memories;
    private Path filePath;

    public PersistentMemory(String fileName) {
        this.memories = new ArrayList<>();
        this.filePath = Path.of(fileName);
        load();
    }

    public boolean add(String text) {
        if (text == null || text.trim().isEmpty()) {
            return false;
        }
        memories.add(text.trim());
        save();
        return true;
    }

    public void load() {
        try {
            Files.createDirectories(filePath.getParent());
            if (Files.exists(filePath)) {
                memories.clear();
                memories.addAll(Files.readAllLines(filePath));
            }
        } catch (IOException e) {
            System.out.println("No se pudo cargar la memoria.");
        }
    }

    public void save() {
        try {
            Files.createDirectories(filePath.getParent());
            Files.write(filePath, memories);
        } catch (IOException e) {
            System.out.println("No se pudo guardar la memoria.");
        }
    }

    public int count() {
        return memories.size();
    }

    public String formatMemories() {
        if (memories.isEmpty()) {
            return "No tengo recuerdos todavía.";
        }
        String result = "";
        for (int i = 0; i < memories.size(); i++) {
            result += (i + 1) + ". " + memories.get(i) + "\n";
        }
        return result;
    }
}
```

## Actividad

```text
1. Crear PersistentMemory.java.
2. Identificar atributo de lista y atributo de ruta.
3. Implementar constructor.
4. Implementar add, load, save, count y formatMemories.
5. Compilar.
```

Comando:

```bash
javac src/*.java
```

## Errores frecuentes

| Error | Señal | Intervención docente |
|---|---|---|
| Falta import de `Files` o `Path` | cannot find symbol | Revisar imports de `java.nio.file`. |
| No capturar `IOException` | Error de compilación | Añadir try/catch. |
| No crear carpeta | Falla al escribir | Usar `Files.createDirectories`. |
| Guardar sin cargar | Segunda ejecución no recupera | Constructor debe llamar a `load()`. |
| Duplicar recuerdos al cargar | Cada load añade encima | `memories.clear()` antes de `addAll`. |

## Cierre

Ticket:

```text
1. ¿Qué hace `load()`?
2. ¿Qué hace `save()`?
3. ¿Por qué `PersistentMemory` no debe leer teclado?
```

## Criterio de éxito

```text
Existe una clase PersistentMemory compilable que encapsula recuerdos y fichero de texto.
```

---

# H6-S4 — Integrar persistencia con herramientas

## Duración

```text
45 minutos
```

## Objetivo

Integrar `PersistentMemory` en `Agent` y en las herramientas de H5, manteniendo la estructura extensible.

## Resultado esperado

MiniJarvis puede ejecutar:

```text
recuerda
memoria
estado
salir
```

usando memoria persistente.

## Guion docente

```text
Crear PersistentMemory no basta. Ahora MiniJarvis debe usarla.

La idea es conservar lo bueno de H5: Agent coordina y las herramientas hacen acciones concretas. La diferencia es que ahora la memoria se carga y guarda en fichero.
```

## Pizarra

```text
H5:
Agent -> Memory temporal

H6:
Agent -> PersistentMemory -> data/recuerdos.txt
```

## Qué explicas tú

```text
- Cómo sustituir Memory por PersistentMemory.
- Que las herramientas no deben crear su propio fichero cada una.
- Que Agent debe compartir la misma memoria persistente.
- Que guardar puede ser automático al añadir recuerdo.
```

## Actividad HEXA guiada

### H — Hecho

`RememberTool` necesita guardar un recuerdo.

### E — Explorar

Pregunta:

```text
¿Debe RememberTool crear una nueva PersistentMemory o usar la del Agent?
```

### X — eXplicar

Respuesta esperada:

```text
Debe usar la del Agent para que todas las herramientas compartan el mismo estado y el mismo fichero.
```

### A — Aplicar

Actualizar Agent y herramientas.

## Código orientativo

En `Agent`:

```java
private PersistentMemory memory;

public Agent(String name, int courseYear) {
    this.name = name;
    this.courseYear = courseYear;
    this.memory = new PersistentMemory("data/recuerdos.txt");
    registerTools();
}

public PersistentMemory getMemory() {
    return memory;
}
```

En `RememberTool`:

```java
public boolean execute(Agent agent) {
    String text = agent.readLine("¿Qué quieres que recuerde? ");
    if (agent.getMemory().add(text)) {
        System.out.println("Recuerdo guardado en fichero.");
    } else {
        System.out.println("No puedo guardar un recuerdo vacío.");
    }
    return true;
}
```

Si el grupo no tiene `readLine` en Agent, alternativa sencilla:

```java
// Agent puede tener un método public String ask(String prompt)
// que usa su Scanner interno y devuelve la respuesta.
```

## Actividad

```text
1. Cambiar el atributo de memoria en Agent.
2. Crear la memoria persistente con ruta relativa.
3. Ajustar RememberTool para usar agent.getMemory().add(text).
4. Ajustar MemoryTool para usar formatMemories().
5. Compilar.
6. Ejecutar una prueba corta.
```

Prueba corta:

```text
recuerda
Traer libreta
memoria
salir
```

## Errores frecuentes

| Error | Señal | Intervención docente |
|---|---|---|
| Cada tool crea su PersistentMemory | Datos incoherentes | Una sola memoria compartida en Agent. |
| Ruta diferente en cada clase | Se crean varios ficheros | Centralizar ruta en Agent o constante. |
| Guardar solo al salir | Si se cierra mal, se pierde | Para nivel básico, guardar al añadir es más seguro. |
| Romper herramientas H5 | ayuda/estado dejan de funcionar | Probar comandos básicos tras cada cambio. |

## Cierre

Ticket:

```text
1. ¿Quién crea PersistentMemory?
2. ¿Qué herramienta añade recuerdos?
3. ¿Dónde se guarda realmente el recuerdo?
```

## Criterio de éxito

```text
El agente usa memoria persistente compartida por sus herramientas y mantiene el diseño extensible de H5.
```

---

# H6-S5 — Crear HistoryLog

## Duración

```text
45 minutos
```

## Objetivo

Crear un historial técnico simple que registre eventos relevantes sin almacenar datos sensibles.

## Resultado esperado

Archivo `src/HistoryLog.java` y fichero `logs/historial.log` con eventos como:

```text
2027-04-10T10:15 - Agent started
2027-04-10T10:16 - Memory added
2027-04-10T10:18 - Agent stopped
```

## Guion docente

```text
Persistencia guarda datos que MiniJarvis necesita recuperar.

Trazabilidad registra eventos para saber qué ha ocurrido: arranque, guardado, errores, salida.

Pero un log no debe convertirse en un almacén de secretos ni datos personales.
```

## Pizarra

```text
Persistencia:
data/recuerdos.txt -> recuerdos ficticios

Trazabilidad:
logs/historial.log -> eventos técnicos
```

Regla de seguridad:

```text
El log debe decir qué ocurrió, no exponer información sensible.
```

## Qué explicas tú

```text
- Qué es un log o historial técnico.
- Diferencia entre dato persistente y evento registrado.
- Por qué no conviene escribir contraseñas ni datos personales en logs.
- Cómo añadir líneas a un fichero con APPEND.
```

## Actividad HEXA guiada

### H — Hecho

El programa guarda un recuerdo.

### E — Explorar

Pregunta:

```text
¿Qué debería registrar el log: el texto completo del recuerdo o solo que se añadió un recuerdo?
```

### X — eXplicar

Respuesta esperada:

```text
Para seguridad básica, basta registrar que se añadió un recuerdo, no necesariamente el contenido completo.
```

### A — Aplicar

Crear `HistoryLog` y registrar eventos.

## Código base guiado

```java
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.StandardOpenOption;
import java.time.LocalDateTime;

public class HistoryLog {
    private Path logPath;

    public HistoryLog(String fileName) {
        this.logPath = Path.of(fileName);
    }

    public void record(String event) {
        try {
            Files.createDirectories(logPath.getParent());
            String line = LocalDateTime.now() + " - " + event + System.lineSeparator();
            Files.writeString(logPath, line, StandardOpenOption.CREATE, StandardOpenOption.APPEND);
        } catch (IOException e) {
            System.out.println("No se pudo escribir el historial.");
        }
    }
}
```

Uso en `Agent`:

```java
private HistoryLog historyLog;

this.historyLog = new HistoryLog("logs/historial.log");
historyLog.record("Agent started");
```

Método de acceso:

```java
public HistoryLog getHistoryLog() {
    return historyLog;
}
```

Uso en una herramienta:

```java
agent.getHistoryLog().record("Memory added");
```

## Actividad

```text
1. Crear HistoryLog.java.
2. Crear HistoryLog en Agent.
3. Registrar arranque.
4. Registrar recuerdo añadido.
5. Registrar salida.
6. Ejecutar y abrir logs/historial.log para comprobarlo.
```

## Errores frecuentes

| Error | Señal | Intervención docente |
|---|---|---|
| Sobrescribir el log cada vez | Solo queda la última línea | Usar `StandardOpenOption.APPEND`. |
| Log con datos sensibles | Aparece texto personal completo | Registrar evento técnico. |
| No crear carpeta logs | Error al escribir | Usar `Files.createDirectories`. |
| Log demasiado detallado | Registra cada tecla | Limitar a eventos útiles. |

## Cierre

Ticket:

```text
1. ¿Qué diferencia hay entre recuerdo y evento de log?
2. ¿Por qué el log no debe guardar secretos?
3. ¿Qué evento registrarías al salir?
```

## Criterio de éxito

```text
Existe un historial técnico simple que registra eventos útiles sin exponer información sensible.
```

---

# H6-S6 — Pruebas de persistencia en dos ejecuciones

## Duración

```text
45 minutos
```

## Objetivo

Demostrar con evidencias que los recuerdos persisten entre dos ejecuciones del programa.

## Resultado esperado

Documento `docs/pruebas-persistencia-h6.md` con prueba reproducible:

```text
Ejecución 1: guardar recuerdo.
Comprobación del fichero.
Ejecución 2: abrir programa y consultar memoria.
Resultado observado.
```

## Guion docente

```text
No basta con decir “guarda”. Tenemos que demostrar persistencia.

La prueba mínima de H6 exige dos ejecuciones separadas. En la primera guardamos; en la segunda comprobamos que el recuerdo sigue ahí.
```

## Pizarra

```text
Prueba H6:
1. Borrar o preparar data/recuerdos.txt.
2. Ejecutar programa.
3. Guardar recuerdo ficticio.
4. Salir.
5. Comprobar fichero.
6. Ejecutar de nuevo.
7. Consultar memoria.
8. Ver el recuerdo.
```

## Qué explicas tú

```text
- Qué significa prueba reproducible.
- Por qué mirar solo la consola no basta.
- Por qué hay que comprobar el fichero y la segunda ejecución.
- Cómo anotar resultado esperado y observado.
```

## Actividad HEXA guiada

### H — Hecho

El programa parece guardar un recuerdo.

### E — Explorar

Pregunta:

```text
¿Qué evidencia demuestra que no estaba solo en memoria temporal?
```

### X — eXplicar

Respuesta esperada:

```text
Que aparece en `data/recuerdos.txt` y vuelve a cargarse al ejecutar de nuevo.
```

### A — Aplicar

Ejecutar y documentar la prueba.

## Plantilla autónoma

```markdown
# Pruebas de persistencia H6

## Objetivo

## Preparación

## Ejecución 1

Comandos usados:

Resultado esperado:

Resultado observado:

## Comprobación del fichero

Ruta:
Contenido observado:

## Ejecución 2

Comandos usados:

Resultado esperado:

Resultado observado:

## Conclusión

## Incidencia si procede
```

## Actividad

Comandos de programa sugeridos:

```text
recuerda
Traer libreta
memoria
salir
```

Segunda ejecución:

```text
memoria
salir
```

Comprobaciones:

```text
- existe data/recuerdos.txt;
- contiene Traer libreta;
- al reiniciar aparece Traer libreta;
- logs/historial.log contiene eventos técnicos.
```

## Errores frecuentes

| Error | Señal | Intervención docente |
|---|---|---|
| Solo prueban una ejecución | No demuestran persistencia | Exigir cerrar y abrir. |
| No miran el fichero | Solo confían en consola | Abrir `data/recuerdos.txt`. |
| Prueba con datos inseguros | Texto sensible en ejemplo | Sustituir por datos ficticios. |
| No documentan fallo | Borran el error | Registrar incidencia. |

## Cierre

Ticket:

```text
1. ¿Por qué H6 necesita dos ejecuciones para probarse?
2. ¿Qué fichero debes comprobar?
3. ¿Qué harás si la prueba falla?
```

## Criterio de éxito

```text
El alumnado demuestra persistencia real con una prueba documentada en dos ejecuciones.
```

---

# H6-S7 — Seguridad: secretos, datos personales y .gitignore

## Duración

```text
45 minutos
```

## Objetivo

Identificar riesgos de seguridad básicos al guardar ficheros y documentar qué se permite y qué se prohíbe en H6.

## Resultado esperado

Documento `docs/seguridad-h6.md` y `.gitignore` revisado con entradas como:

```text
.env
*.key
*.token
```

## Guion docente

```text
Persistir información tiene una consecuencia: lo que antes desaparecía ahora puede quedar guardado y compartirse por error.

Por eso H6 incluye seguridad básica. No necesitamos ser expertos en ciberseguridad para aplicar una regla clara: no guardar secretos ni datos personales reales.
```

## Pizarra

```text
Permitido:
- recuerdos ficticios;
- eventos técnicos simples;
- datos de prueba inventados.

Prohibido:
- contraseñas;
- tokens;
- API keys;
- teléfonos reales;
- direcciones reales;
- datos personales reales;
- .env real.
```

## Qué explicas tú

```text
- Qué es un secreto: contraseña, token, clave API.
- Qué es un dato personal en contexto escolar.
- Por qué `.env.example` puede existir, pero `.env` real no debe subirse.
- Qué hace `.gitignore` y qué no hace: no borra secretos ya subidos.
```

## Actividad HEXA guiada

### H — Hecho

Un alumno escribe en `recuerdos.txt`: “Mi clave API es abc123”.

### E — Explorar

Pregunta:

```text
¿Qué riesgos aparecen aunque el programa funcione?
```

Respuestas esperadas:

```text
- el secreto queda guardado;
- puede subirse al repositorio;
- otra persona puede verlo;
- habría que eliminarlo y cambiar la clave real si existiera.
```

### X — eXplicar

Conclusión:

```text
Un programa puede ser técnicamente correcto y tener una mala práctica de seguridad.
```

### A — Aplicar

Completar registro de seguridad y revisar `.gitignore`.

## Plantilla autónoma de seguridad

```markdown
# Seguridad H6

## Datos permitidos

## Datos prohibidos

## Ficheros creados por el programa

## Qué contiene data/recuerdos.txt

## Qué contiene logs/historial.log

## Revisión de .gitignore

Entradas mínimas:
- `.env`
- `*.key`
- `*.token`

## Riesgo detectado

## Medida aplicada

## Frase de defensa
```

## Actividad

```text
1. Clasificar ejemplos como permitido/prohibido.
2. Revisar recuerdos usados en pruebas.
3. Revisar logs.
4. Crear o revisar .gitignore.
5. Completar documento de seguridad.
```

Tabla de clasificación:

| Ejemplo | Permitido/prohibido | Motivo |
|---|---|---|
| `Traer libreta` | Permitido | Ficticio y no sensible. |
| `Mi password es 1234` | Prohibido | Secreto. |
| `Teléfono de mi madre: ...` | Prohibido | Dato personal real. |
| `Repasar ficheros Java` | Permitido | Recuerdo académico ficticio. |

## Errores frecuentes

| Error | Señal | Intervención docente |
|---|---|---|
| Creer que `.gitignore` protege todo | Ya habían subido secreto | Explicar que evita futuros añadidos, no borra historia. |
| Guardar datos reales por realismo | Recuerdos con información personal | Usar datos ficticios. |
| Log demasiado explícito | Registra contenido sensible | Registrar solo evento. |
| Copiar `.env.example` como `.env` real | Aparece secreto | Eliminar y explicar riesgo. |

## Cierre

Ticket:

```text
1. Escribe un dato que nunca debes guardar en H6.
2. ¿Para qué sirve `.gitignore`?
3. ¿Por qué un log puede ser peligroso si guarda demasiado?
```

## Criterio de éxito

```text
El alumnado identifica secretos y datos personales, documenta medidas básicas y evita que H6 persista información sensible.
```

---

# H6-S8 — README reproducible e incidencias

## Duración

```text
45 minutos
```

## Objetivo

Crear un README que permita ejecutar H6 desde cero y documentar incidencias de forma útil.

## Resultado esperado

Dos evidencias:

```text
README.md
Docs/incidencia-h6.md si ha ocurrido un fallo relevante
```

## Guion docente

```text
Un proyecto no está completo si solo funciona en mi ordenador y solo yo sé ejecutarlo.

El README debe permitir que otra persona compile, ejecute y compruebe H6 desde cero.

Además, si algo falla, no lo escondemos: lo convertimos en incidencia documentada.
```

## Pizarra

```text
README reproducible:
1. Requisitos.
2. Cómo compilar.
3. Cómo ejecutar.
4. Qué ficheros crea.
5. Cómo probar persistencia.
6. Qué datos no usar.
```

## Qué explicas tú

```text
- Qué significa reproducibilidad en un proyecto escolar.
- Por qué el README debe probarse siguiendo sus propios pasos.
- Qué es una incidencia: fallo, causa, solución o estado.
- Que documentar un error bien puede ser evidencia de aprendizaje.
```

## Actividad HEXA guiada

### H — Hecho

El programa funciona en el equipo de quien lo creó.

### E — Explorar

Pregunta:

```text
¿Qué necesita otra persona para ejecutarlo sin preguntarte?
```

### X — eXplicar

Respuesta esperada:

```text
Comandos exactos, estructura de carpetas, explicación de ficheros y prueba esperada.
```

### A — Aplicar

Escribir README y probarlo.

## Plantilla README autónoma

```markdown
# MiniJarvis H6 — Persistente y trazable

## Requisitos

- Java instalado.

## Compilar

```bash
javac src/*.java
```

## Ejecutar

```bash
java -cp src Main
```

## Ficheros que crea o usa

- `data/recuerdos.txt`
- `logs/historial.log`

## Prueba rápida

1. Ejecuta el programa.
2. Usa `recuerda` y escribe un recuerdo ficticio.
3. Usa `salir`.
4. Ejecuta de nuevo.
5. Usa `memoria`.
6. Comprueba que aparece el recuerdo.

## Seguridad

No usar contraseñas, tokens, claves API ni datos personales reales.
```

## Plantilla de incidencia

```markdown
# Incidencia H6

## Fecha

## Qué esperaba

## Qué ocurrió

## Mensaje de error

## Causa probable

## Cambio realizado

## Cómo lo verifiqué

## Estado
```

## Actividad

```text
1. Escribir README.
2. Intercambiar README con otra pareja.
3. La otra pareja intenta seguirlo.
4. Registrar duda o fallo.
5. Crear incidencia si procede.
```

## Errores frecuentes

| Error | Señal | Intervención docente |
|---|---|---|
| README demasiado general | “Ejecuta el programa” | Pedir comandos exactos. |
| README no menciona ficheros | No se sabe dónde mirar | Añadir data y logs. |
| Incidencia sin evidencia | “No funciona” | Pedir mensaje, paso y verificación. |
| Ocultar fallos | No documentan problemas | Valorar incidencia bien resuelta. |

## Cierre

Ticket:

```text
1. ¿Qué comando exacto compila tu proyecto?
2. ¿Qué paso del README demuestra persistencia?
3. ¿Cuándo debes abrir una incidencia?
```

## Criterio de éxito

```text
Otra persona puede ejecutar H6 siguiendo el README y las incidencias quedan documentadas de forma útil si aparecen.
```

---

# H6-S9 — Comparación Java ↔ Python y documentación H6

## Duración

```text
45 minutos
```

## Objetivo

Comparar lectura/escritura de ficheros en Java y Python y cerrar la documentación técnica del hito.

## Resultado esperado

Documentos actualizados:

```text
- docs/comparacion-java-python-h6.md;
- docs/pruebas-persistencia-h6.md;
- docs/seguridad-h6.md;
- docs/logs-historial-h6.md;
- docs/portfolio-h6.md;
- docs/registro-ia.md si procede.
```

## Guion docente

```text
Java y Python pueden leer y escribir ficheros, pero lo expresan de forma diferente.

Java suele ser más explícito con rutas, excepciones e imports. Python suele ser más breve. La idea común es la misma: abrir o localizar un fichero, leer o escribir, y controlar errores.
```

## Pizarra

```text
Java:
Path.of("data/recuerdos.txt")
Files.readAllLines(path)
Files.write(path, lines)
try/catch IOException

Python:
with open("data/recuerdos.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
```

## Qué explicas tú

```text
- Que Java obliga a gestionar IOException.
- Que Python usa habitualmente `with open(...)`.
- Que ambos lenguajes deben pensar en rutas, codificación y errores.
- Que la comparación debe ayudar a entender, no cambiar el proyecto Java.
```

## Actividad HEXA guiada

### H — Hecho

En Java usamos `Files.write`.

### E — Explorar

Pregunta:

```text
¿Qué sería parecido en Python?
```

### X — eXplicar

Respuesta esperada:

```text
Abrir un fichero en modo escritura y escribir líneas, por ejemplo con `with open(..., "w")`.
```

### A — Aplicar

Completar tabla comparativa.

## Plantilla comparación

```markdown
# Comparación Java ↔ Python — H6

| Concepto | Java | Python | Qué debo recordar |
|---|---|---|---|
| Ruta | `Path.of("data/recuerdos.txt")` | string o `Path("data/recuerdos.txt")` | Ambos necesitan ubicar el fichero. |
| Crear carpetas | `Files.createDirectories(...)` | `mkdir(parents=True, exist_ok=True)` | La carpeta debe existir antes de escribir. |
| Leer líneas | `Files.readAllLines(path)` | `f.readlines()` | Carga contenido del fichero. |
| Escribir líneas | `Files.write(path, lines)` | `f.write(...)` | Sobrescribe o escribe contenido. |
| Añadir log | `APPEND` | modo `"a"` | Añade al final. |
| Errores | `try/catch IOException` | `try/except OSError` | Hay que prever fallos de E/S. |
```

## Portfolio H6 mínimo

```text
1. Qué problema resolvía H6.
2. Qué fichero guarda recuerdos.
3. Qué fichero registra historial.
4. Cómo probé dos ejecuciones.
5. Qué riesgo de seguridad revisé.
6. Qué incidencia tuve o qué habría hecho si fallaba.
7. Qué aprendí sobre ficheros Java.
8. Qué preparo para H7.
```

## Uso de IA permitido

```text
Se puede pedir a una IA una explicación sencilla de `Files.readAllLines`, `Files.write` o comparación Java/Python.
```

Condición:

```text
La explicación debe verificarse con el código propio y no debe introducir rutas absolutas, secretos ni soluciones avanzadas no entendidas.
```

## Actividad

```text
1. Completar comparación Java/Python.
2. Revisar pruebas de persistencia.
3. Revisar seguridad.
4. Revisar logs.
5. Completar portfolio.
6. Preparar tres frases de defensa.
```

Tres frases de defensa:

```text
Mi memoria persiste porque...
Mi historial es trazable porque...
Mi solución es segura para H6 porque...
```

## Errores frecuentes

| Error | Señal | Intervención docente |
|---|---|---|
| Comparación demasiado avanzada | Streams complejos, serialización, bases de datos | Volver a ficheros de texto. |
| Copiar IA sin verificar | Explica métodos que no usa | Pedir señalar código real. |
| Documentación sin evidencias | Frases genéricas | Exigir ruta, comando y resultado. |
| Olvidar seguridad | Portfolio solo técnico | Añadir apartado de datos prohibidos. |

## Cierre

Ticket:

```text
1. ¿Qué se parece entre leer ficheros en Java y Python?
2. ¿Qué diferencia importante tiene Java con IOException?
3. ¿Qué documento te falta cerrar antes de defender?
```

## Criterio de éxito

```text
El alumnado documenta H6 con evidencias propias y compara Java/Python sin perder el foco en persistencia y seguridad básica.
```

---

# H6-S10 — Defensa H6

## Duración

```text
45 minutos
```

## Objetivo

Validar H6 mediante ejecución, prueba de persistencia, revisión de logs, seguridad y defensa individual.

## Resultado esperado

H6 entregado con:

```text
- código Java compilable y ejecutable;
- recuerdos persistentes en fichero;
- historial técnico simple;
- prueba de persistencia en dos ejecuciones;
- README reproducible;
- documento de seguridad;
- incidencia si procede;
- comparación Java ↔ Python;
- portfolio y registro IA si procede;
- defensa individual.
```

## Guion docente

```text
Hoy no basta con decir que MiniJarvis guarda. Hay que demostrarlo.

La defensa H6 debe enseñar dónde se guarda, cómo se recupera, qué registra el historial y qué medidas evitan guardar información sensible.
```

## Pizarra

```text
Defensa H6:
1. Compila.
2. Ejecuta.
3. Guarda recuerdo ficticio.
4. Cierra.
5. Enseña data/recuerdos.txt.
6. Ejecuta de nuevo.
7. Consulta memoria.
8. Enseña logs/historial.log.
9. Defiende seguridad.
```

## Qué explicas tú

```text
- Que la evidencia principal es la persistencia entre ejecuciones.
- Que un log útil no debe ser indiscreto.
- Que el README debe poder reproducir la prueba.
- Que seguridad básica forma parte del hito, no es un extra.
```

## Actividad HEXA guiada

### H — Hecho

Un programa puede escribir un fichero y aun así estar mal defendido.

### E — Explorar

Pregunta:

```text
¿Qué evidencias demuestran que H6 está completo?
```

Respuestas esperadas:

```text
- fichero de recuerdos;
- segunda ejecución recupera datos;
- historial técnico existe;
- README reproduce;
- seguridad documentada;
- no hay secretos ni datos personales reales.
```

### X — eXplicar

Conclusión:

```text
H6 se supera cuando persistencia, trazabilidad y seguridad se pueden comprobar, no solo prometer.
```

### A — Aplicar

Defensa por turnos con checklist.

## Checklist docente de defensa

| Elemento | Sí | Parcial | No | Observación |
|---|---|---|---|---|
| Compila y ejecuta | | | | |
| Crea `data/` si falta | | | | |
| Crea `logs/` si falta | | | | |
| Guarda recuerdos en fichero | | | | |
| Recupera en segunda ejecución | | | | |
| Usa recuerdos ficticios | | | | |
| No guarda secretos | | | | |
| Historial registra eventos | | | | |
| Log no expone datos sensibles | | | | |
| README permite reproducir | | | | |
| Pruebas de persistencia documentadas | | | | |
| Seguridad documentada | | | | |
| Incidencia documentada si procede | | | | |
| Comparación Java/Python comprensible | | | | |
| Defensa individual suficiente | | | | |

## Preguntas de defensa

```text
1. ¿Qué problema de H5 resuelve H6?
2. ¿Dónde se guardan los recuerdos?
3. ¿Qué ocurre si `data/` no existe?
4. ¿Dónde se registra el historial?
5. ¿Qué eventos registra tu log?
6. ¿Por qué el log no debe guardar secretos?
7. ¿Cómo demuestras persistencia en dos ejecuciones?
8. ¿Qué línea de código crea carpetas?
9. ¿Qué línea de código lee recuerdos?
10. ¿Qué línea de código escribe recuerdos?
11. ¿Qué dato no debes guardar nunca?
12. ¿Qué contiene tu `.gitignore`?
13. ¿Cómo ejecutaría tu proyecto otra persona desde cero?
14. ¿Qué diferencia hay entre leer ficheros en Java y Python?
15. ¿Qué prepararías para H7?
```

## Errores frecuentes

| Error | Señal | Intervención docente |
|---|---|---|
| Defender solo una ejecución | No cierra y reabre | Exigir prueba completa. |
| Mostrar fichero vacío | Guardado no funciona | Revisar `save()` y ruta. |
| No se crean carpetas | Funciona solo si ya existen | Revisar `Files.createDirectories`. |
| Log contiene texto sensible | Registra recuerdos completos peligrosos | Cambiar a eventos técnicos. |
| README no reproduce | Faltan comandos | Añadir `javac` y `java -cp src Main`. |
| Inventar evidencias | Dice que hay Git/log sin mostrarlo | Pedir fichero real o registro equivalente. |

Intervención oral si la defensa se atasca:

```text
No expliques todo el programa. Defiende esta cadena:
PersistentMemory conoce data/recuerdos.txt.
Al añadir un recuerdo, se guarda.
Al iniciar de nuevo, se carga.
HistoryLog registra eventos técnicos.
La seguridad evita secretos y datos personales reales.
```

Búsqueda guiada en el código:

```text
1. Busca `Path.of("data/recuerdos.txt")`.
2. Busca `Files.createDirectories`.
3. Busca `Files.readAllLines`.
4. Busca `Files.write`.
5. Busca `Path.of("logs/historial.log")`.
6. Busca `APPEND`.
```

## Recuperación inmediata

Si no compila:

```text
Reducir a PersistentMemory + Main de prueba. Después volver a Agent y Tools.
```

Si no persiste:

```text
Comprobar ruta, comprobar `save()`, comprobar que `load()` se llama en el constructor y hacer prueba en dos ejecuciones.
```

Si no hay logs:

```text
Crear HistoryLog mínimo y registrar solo Agent started y Agent stopped.
```

Si hay datos sensibles:

```text
Eliminar ejemplos inseguros, sustituir por datos ficticios y documentar la corrección en seguridad-h6.md.
```

Si el README falla:

```text
Probarlo desde cero y añadir comandos exactos.
```

## Cierre de H6

Guion:

```text
H6 cambia la madurez de MiniJarvis: ahora el agente no solo responde mientras está abierto, sino que conserva información y deja un rastro técnico básico.

También hemos aprendido una lección importante: guardar información exige responsabilidad. Persistencia sin seguridad puede crear problemas.

En H7 trabajaremos integración de IA responsable real o simulada. Gracias a H6 tendremos una base para hablar de datos, trazabilidad, seguridad y validación humana.
```

## Criterio de éxito

```text
El alumnado entrega un H6 funcional y puede demostrar persistencia real, trazabilidad básica y decisiones de seguridad defendibles.
```

---

## 5. Evaluación formativa de H6

H6 debe servir para detectar:

```text
- quién diferencia memoria temporal y persistente;
- quién entiende rutas relativas;
- quién sabe crear carpetas antes de escribir;
- quién maneja lectura/escritura básica con control de errores;
- quién demuestra con dos ejecuciones;
- quién documenta pruebas reproducibles;
- quién identifica secretos y datos personales;
- quién entiende que un log puede ser útil y peligroso;
- quién redacta un README ejecutable;
- quién registra incidencias en vez de ocultarlas;
- quién compara Java/Python a nivel de ficheros;
- quién usa IA como apoyo y no como sustituto de comprensión.
```

Evidencias mínimas:

| Evidencia | Qué mirar |
|---|---|
| Código | Compila, ejecuta y mantiene estructura H5. |
| `PersistentMemory.java` | Carga, guarda, crea carpetas y controla errores. |
| `HistoryLog.java` | Añade eventos técnicos sin secretos. |
| `data/recuerdos.txt` | Contiene recuerdos ficticios persistentes. |
| `logs/historial.log` | Contiene eventos técnicos útiles. |
| Pruebas de persistencia | Demuestran dos ejecuciones. |
| README | Permite reproducir desde cero. |
| Seguridad | Prohíbe secretos/datos personales y revisa `.gitignore`. |
| Incidencia | Documenta fallos si existen. |
| Comparación Java/Python | Explica ficheros, rutas y errores. |
| Defensa | La persona entiende cómo y por qué persiste. |

---

## 6. Atención a la diversidad

### Si el alumnado se bloquea con Files y Path

Reducir objetivo:

```text
Primero escribir una lista fija en `data/recuerdos.txt`.
Después leerla.
Después integrar con el agente.
```

Secuencia reducida:

```text
1. Crear ruta.
2. Crear carpeta.
3. Escribir una línea fija.
4. Leer y mostrar.
5. Conectar con recuerdos reales.
```

### Si el alumnado se bloquea con herramientas H5

Permitir una versión puente:

```text
Agent usa PersistentMemory directamente para recuerda y memoria.
Después se recuperan RememberTool y MemoryTool.
```

No sacrificar persistencia por mantener una arquitectura que el grupo no puede defender.

### Si el alumnado se bloquea con IOException

Explicación mínima:

```text
Leer o escribir ficheros puede fallar porque el fichero no existe, la ruta está mal o no hay permisos. Java nos obliga a reconocer ese riesgo con try/catch.
```

Plantilla de apoyo:

```java
try {
    // operación con fichero
} catch (IOException e) {
    System.out.println("Error de fichero.");
}
```

### Si el alumnado usa datos reales

Intervención inmediata:

```text
Detener la prueba, sustituir por datos ficticios y documentar el aprendizaje en seguridad-h6.md.
```

Si hubo secreto real:

```text
No copiarlo en la pizarra ni en documentos. Indicar que debe eliminarse y, si era una clave real, cambiarse fuera de la actividad.
```

### Si hay alumnado avanzado

Extensión permitida:

```text
Guardar con formato sencillo tipo CSV o añadir un campo fecha ficticia si puede defender lectura/escritura.
```

Extensiones no obligatorias:

```text
JSON complejo, base de datos, cifrado, logging profesional, serialización avanzada o sincronización en la nube.
```

---

## 7. Uso responsable de IA en H6

Usos permitidos:

```text
- pedir explicación sencilla de `Path`, `Files` o `IOException`;
- pedir una checklist de seguridad para no guardar secretos;
- pedir ayuda para redactar README reproducible;
- comparar lectura/escritura Java con Python;
- pedir preguntas de defensa sobre persistencia.
```

Usos no permitidos:

```text
- introducir datos personales reales en prompts;
- pegar tokens, claves API, contraseñas o `.env` reales;
- copiar código de persistencia que no se entiende;
- añadir base de datos o frameworks externos porque la IA lo sugiera;
- inventar pruebas o logs no ejecutados.
```

Registro mínimo de IA:

```text
Fecha:
Herramienta:
Prompt usado:
Respuesta útil:
Qué he aceptado:
Qué he rechazado:
Cómo lo he verificado:
Qué entiendo ahora con mis palabras:
```

Frase docente:

```text
La IA puede explicar ficheros, pero no puede demostrar por ti que tu programa guarda, se cierra, se abre y recupera recuerdos.
```

---

## 8. Criterios globales de éxito de H6

H6 está consolidado cuando:

```text
[x] El programa compila.
[x] El programa ejecuta comandos básicos.
[x] `data/` se crea si falta.
[x] `logs/` se crea si falta.
[x] Los recuerdos se guardan en `data/recuerdos.txt`.
[x] Los recuerdos se recuperan en una segunda ejecución.
[x] El historial registra eventos técnicos.
[x] El historial no expone secretos ni datos personales reales.
[x] El README permite ejecutar desde cero.
[x] Las pruebas de persistencia están documentadas.
[x] La seguridad está documentada.
[x] `.gitignore` contempla `.env`, `*.key` y `*.token`.
[x] Las incidencias se documentan si aparecen.
[x] La comparación Java ↔ Python es comprensible.
[x] El alumnado puede defender persistencia, trazabilidad y seguridad básica.
```

---

## 9. Puente hacia H7

Mensaje final al grupo:

```text
En H6 hemos aprendido que MiniJarvis puede conservar información y dejar evidencias técnicas.

También hemos aprendido que guardar datos exige límites: no todo lo que se puede guardar se debe guardar.

En H7 entraremos en IA responsable, probablemente con una simulación robusta o una integración controlada. Lo aprendido en H6 será clave: datos, logs, seguridad, trazabilidad y validación humana.
```

Preparación docente para la siguiente fase:

```text
Selecciona tres ejemplos H6:
- uno donde la prueba de persistencia esté muy clara;
- uno donde el log sea útil sin exponer datos sensibles;
- uno donde una incidencia haya sido bien documentada.

Servirán para iniciar H7 hablando de qué información puede recibir una IA, qué información debe bloquearse y cómo se valida una respuesta.
```
