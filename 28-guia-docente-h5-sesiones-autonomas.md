# Guía docente completa — H5 sesión a sesión

## Agente extensible, clean code y patrones iniciales — MiniJarvis H5

## Programación + Entornos de Desarrollo — 1.º DAW — Curso 2026/2027

Versión: borrador 0.1

Documento autónomo para uso del profesorado.

Este documento permite impartir H5 completo sin abrir ningún otro material durante la clase.

---

## 1. Propósito de H5

H5 transforma MiniJarvis H4 en un agente más extensible y mantenible.

Producto final:

```text
MiniJarvis H5: agente por consola con herramientas/comandos internos separables, refactorización documentada, revisión de código, evidencia de Git o revisión equivalente y decisión razonada sobre patrón de diseño.
```

H5 introduce:

```text
- problema del if/else de comandos que crece demasiado;
- clean code aplicado a nombres, métodos y responsabilidades;
- refactorización antes/después;
- interfaz o contrato simple Tool;
- herramientas separadas: HelpTool, RememberTool, MemoryTool, StatusTool, CourseTool, ExitTool;
- añadir una herramienta nueva con bajo impacto;
- revisión de código entre iguales;
- evidencia Git o registro equivalente;
- patrón Command simplificado como opción razonada;
- comparación Java ↔ Python sobre interfaces y duck typing;
- defensa H5.
```

Idea docente central:

```text
H5 no consiste en usar patrones porque suenan profesionales. H5 consiste en detectar que añadir comandos empieza a ser incómodo y mejorar el diseño de forma defendible.
```

---

## 2. Restricciones de H5

En H5 sí entra:

```text
[x] Refactorización justificada.
[x] Herramientas o comandos internos separables.
[x] Una interfaz o contrato sencillo si el grupo está preparado.
[x] Nombres claros.
[x] Métodos cortos y responsabilidades visibles.
[x] Evidencia de Git, rama, commits, PR o revisión equivalente de aula.
[x] Revisión de código.
[x] Decisión razonada sobre patrón usado o descartado.
[x] Comparación Java ↔ Python.
[x] Defensa de extensibilidad y mantenibilidad.
```

En H5 todavía NO entra:

```text
[ ] Plugins reales cargados dinámicamente.
[ ] Frameworks externos.
[ ] Arquitectura hexagonal.
[ ] Persistencia en ficheros.
[ ] Base de datos.
[ ] API externa.
[ ] IA real.
[ ] Patrones múltiples por decoración.
```

Frase docente:

```text
Si para añadir un comando tengo que tocar muchas partes del programa y copiar bloques de if/else, el diseño empieza a pedir una refactorización. H5 trata de eso.
```

---

## 3. Diseño mínimo de referencia

Partimos de H4:

```text
Main arranca.
Agent coordina.
Memory recuerda.
```

En H5 añadimos herramientas separables:

| Clase/interfaz | Responsabilidad |
|---|---|
| `Tool` | Contrato común para comandos o herramientas. |
| `HelpTool` | Mostrar ayuda. |
| `GreetTool` | Saludar. |
| `RememberTool` | Guardar recuerdos usando `Memory`. |
| `MemoryTool` | Mostrar recuerdos. |
| `StatusTool` | Mostrar estado. |
| `CourseTool` | Mostrar información ficticia del curso/proyecto. |
| `ExitTool` | Solicitar salida del agente. |
| `Agent` | Orquestar ejecución y delegar en herramientas. |
| `Memory` | Gestionar recuerdos temporales. |
| `Main` | Crear y arrancar `Agent`. |

Estructura esperada:

```text
h5-extensible-clean-code-patrones/
├── README.md
├── src/
│   ├── Main.java
│   ├── Agent.java
│   ├── Memory.java
│   ├── Tool.java
│   ├── HelpTool.java
│   ├── GreetTool.java
│   ├── RememberTool.java
│   ├── MemoryTool.java
│   ├── StatusTool.java
│   ├── CourseTool.java
│   └── ExitTool.java
└── docs/
    ├── informe-refactorizacion-h5.md
    ├── evidencia-git-h5.md
    ├── revision-codigo-h5.md
    ├── registro-patron-h5.md
    ├── comparacion-java-python-h5.md
    ├── portfolio-h5.md
    ├── registro-ia.md
    └── defensa-h5.md
```

Código orientativo mínimo para explicar la meta:

```java
public interface Tool {
    String getName();
    String getDescription();
    boolean execute(Agent agent);
}
```

```java
public class Main {
    public static void main(String[] args) {
        Agent agent = new Agent("MiniJarvis", 2027);
        agent.start();
    }
}
```

```java
import java.util.ArrayList;

public class Agent {
    private String name;
    private int courseYear;
    private Memory memory;
    private ArrayList<Tool> tools;
    private boolean running;

    public Agent(String name, int courseYear) {
        this.name = name;
        this.courseYear = courseYear;
        this.memory = new Memory();
        this.tools = new ArrayList<>();
        this.running = true;
        registerTools();
    }

    private void registerTools() {
        tools.add(new HelpTool());
        tools.add(new GreetTool());
        tools.add(new RememberTool());
        tools.add(new MemoryTool());
        tools.add(new StatusTool());
        tools.add(new CourseTool());
        tools.add(new ExitTool());
    }

    public void start() {
        System.out.println("Hola, soy " + name + " H5.");
        System.out.println("Escribe ayuda para ver herramientas.");
    }
}
```

Nota didáctica:

```text
La interfaz Tool es una puerta didáctica hacia el patrón Command, pero no hace falta convertir H5 en una clase teórica de patrones. Primero se ve el problema; después se nombra la solución.
```

---

## 4. Secuencia de sesiones H5

Preparación docente antes de iniciar H5:

```text
1. Tener un H4 funcional con Main, Agent y Memory.
2. Preparar un ejemplo de Agent con muchos if/else para que el problema sea visible.
3. Tener clara la diferencia entre refactorizar y añadir funcionalidad.
4. Decidir si la evidencia Git será real con commits o registro equivalente de aula.
5. Evitar exigir GitHub si el grupo todavía no está preparado; lo importante es trazabilidad.
6. Mantener el vocabulario limpio: herramienta, comando, contrato, responsabilidad, refactorización.
7. Repetir que H5 no introduce persistencia. Guardar en ficheros será H6.
```

Material mínimo de aula:

```text
- editor o IDE Java;
- terminal para compilar y ejecutar;
- cuaderno o portfolio digital;
- pizarra para antes/después;
- plantilla de revisión de código en la propia sesión;
- registro Git o registro equivalente de cambios;
- registro de IA si se permite apoyo.
```

Propuesta de 10 sesiones de 45 minutos.

| Sesión | Foco | Producto parcial |
|---|---|---|
| H5-S1 | Presentar problema: Agent crece con if/else | Diagnóstico antes/después. |
| H5-S2 | Clean code aplicado a comandos | Lista de olores de código y mejoras. |
| H5-S3 | Refactorización segura | Plan de refactorización pequeño y verificable. |
| H5-S4 | Interfaz/contrato `Tool` | `Tool.java` y primer comando separado. |
| H5-S5 | Separar herramientas principales | Help, Remember, Memory, Status. |
| H5-S6 | Añadir una herramienta nueva con bajo impacto | `CourseTool` u otra herramienta sencilla. |
| H5-S7 | Patrón Command simplificado o decisión de no patrón | Registro de patrón razonado. |
| H5-S8 | Git, revisión de código y evidencia | Registro de cambios y revisión entre iguales. |
| H5-S9 | Comparación Java ↔ Python y documentación H5 | Comparación + informe + portfolio. |
| H5-S10 | Defensa H5 | Revisión, defensa y cierre del hito. |

---

# H5-S1 — Presentar el problema: Agent crece con if/else

## Duración

```text
45 minutos
```

## Objetivo

Que el alumnado detecte que el método que procesa comandos en `Agent` puede crecer demasiado y dificultar añadir nuevas herramientas.

## Resultado esperado

Diagnóstico escrito:

```text
Problema detectado en H4:
- processCommand tiene demasiadas decisiones.
- Añadir un comando nuevo obliga a modificar Agent.
- Algunas responsabilidades están mezcladas.

Objetivo H5:
- separar comandos/herramientas;
- reducir impacto al añadir una nueva función;
- documentar la refactorización.
```

## Guion docente

```text
En H4 hicimos algo muy importante: separar Main, Agent y Memory.

Pero cuando MiniJarvis crece, aparece un nuevo problema. Agent empieza a tener un bloque de decisiones cada vez más largo: si el comando es ayuda, si es recuerda, si es memoria, si es estado, si es salir...

Esto todavía funciona, pero empieza a ser menos mantenible. H5 nace cuando algo funciona pero empieza a costar cambiarlo.
```

## Pizarra

```text
H4 resuelve:
Main demasiado grande.

H5 detecta:
Agent empieza a crecer demasiado.

Pregunta clave:
¿Qué tengo que tocar para añadir un comando nuevo?
```

## Qué explicas tú

```text
- Que refactorizar no significa cambiar lo que el programa hace desde fuera.
- Que un código que funciona puede necesitar mejora interna.
- Que el problema no es tener un if/else, sino que crezca sin control.
- Que el objetivo es reducir el impacto de añadir comandos.
```

## Actividad HEXA guiada

### H — Hecho

Muestras este fragmento:

```java
private void processCommand(String command) {
    if (command.equals("salir")) {
        running = false;
    } else if (command.equals("ayuda")) {
        showHelp();
    } else if (command.equals("recuerda")) {
        remember();
    } else if (command.equals("memoria")) {
        System.out.println(memory.formatMemories());
    } else if (command.equals("estado")) {
        System.out.println("Tengo " + memory.count() + " recuerdos.");
    } else {
        System.out.println("No entiendo ese comando.");
    }
}
```

### E — Explorar

Pregunta:

```text
Si mañana añadimos comandos curso, resumen, borrar, exportar y configurar, ¿qué pasará con este método?
```

Respuestas esperadas:

```text
- crecerá mucho;
- será más difícil de leer;
- habrá más riesgo de romper comandos existentes;
- Agent sabrá demasiados detalles.
```

### X — eXplicar

Conclusión:

```text
El bloque if/else es una señal de que quizá necesitamos separar comandos.
```

### A — Aplicar

El alumnado marca en su código qué comandos existen y qué tendría que cambiar para añadir uno nuevo.

## Actividad

```text
1. Abrir el H4 propio.
2. Localizar dónde se procesan comandos.
3. Contar cuántas ramas de decisión hay.
4. Escribir qué habría que modificar para añadir el comando `curso`.
5. No modificar todavía el código: solo diagnosticar.
```

## Errores frecuentes

| Error | Señal | Intervención docente |
|---|---|---|
| Querer cambiar todo inmediatamente | Empiezan a borrar Agent | Pedir diagnóstico antes de refactorizar. |
| Pensar que if/else siempre está mal | Rechazan cualquier condicional | Aclarar: el problema es crecimiento y mantenimiento. |
| Confundir refactorización con nueva función | Añaden persistencia o IA | Reencuadrar: H5 mejora estructura. |
| No ver el coste de cambio | “Solo añado otro else if” | Preguntar qué ocurrirá con diez comandos más. |

## Cierre

Ticket:

```text
1. ¿Qué problema aparece cuando processCommand crece demasiado?
2. ¿Qué significa refactorizar sin cambiar comportamiento externo?
3. ¿Qué comando nuevo usaremos como prueba en H5?
```

## Criterio de éxito

```text
El alumnado identifica el problema de extensibilidad y entiende que H5 mejora el diseño interno antes de añadir complejidad.
```

---

# H5-S2 — Clean code aplicado a comandos

## Duración

```text
45 minutos
```

## Objetivo

Aplicar principios básicos de clean code a MiniJarvis: nombres claros, métodos cortos, una responsabilidad y código defendible.

## Resultado esperado

Lista de olores de código y mejoras concretas:

```text
Olor detectado:
Por qué dificulta el cambio:
Mejora propuesta:
Cómo sabré que no he roto nada:
```

## Guion docente

```text
Clean code no significa escribir código elegante para impresionar.

En nuestro nivel significa que otra persona de clase pueda leer el código, entender qué hace y modificarlo sin miedo.

Vamos a buscar señales: nombres poco claros, métodos demasiado largos, código duplicado y responsabilidades mezcladas.
```

## Pizarra

```text
Clean code H5:
- nombres que expliquen intención;
- métodos pequeños;
- una responsabilidad principal;
- evitar duplicación;
- cambios pequeños y verificables;
- código que puedo defender.
```

## Qué explicas tú

```text
- La diferencia entre que el código compile y que sea mantenible.
- Qué es un olor de código de forma sencilla.
- Por qué un buen nombre reduce comentarios innecesarios.
- Por qué no se refactoriza todo a la vez.
- Que la mejora debe estar conectada con un problema visible.
```

## Actividad HEXA guiada

### H — Hecho

Presentas dos nombres:

```java
public void x() { }
public void rememberUserInput() { }
```

### E — Explorar

Pregunta:

```text
¿Cuál ayuda más a entender el programa y por qué?
```

### X — eXplicar

Respuesta esperada:

```text
El segundo expresa intención. El primero obliga a investigar o adivinar.
```

### A — Aplicar

Revisión de nombres y métodos del H4 propio.

## Actividad

Tabla de olores:

| Olor de código | Ejemplo en mi MiniJarvis | Mejora propuesta |
|---|---|---|
| Método largo | | |
| Nombre poco claro | | |
| Duplicación | | |
| Responsabilidad mezclada | | |
| Comentario que oculta mal nombre | | |

Consigna:

```text
No se modifica todo. Se eligen dos mejoras pequeñas y seguras.
```

## Errores frecuentes

| Error | Señal | Intervención docente |
|---|---|---|
| Cambiar nombres sin criterio | Renombran todo y rompen llamadas | Hacer cambios pequeños y compilar. |
| Confundir clean code con código avanzado | Añaden genéricos complejos | Volver a legibilidad y responsabilidad. |
| Usar comentarios para tapar nombres malos | Comentarios explican lo obvio | Mejorar nombre antes que comentar. |
| Refactorizar sin prueba manual | No saben si rompieron algo | Definir prueba mínima antes/después. |

## Cierre

Ticket:

```text
1. Escribe un olor de código que hayas visto.
2. Escribe una mejora concreta que no cambie comportamiento.
3. ¿Cómo comprobarás que no has roto MiniJarvis?
```

## Criterio de éxito

```text
El alumnado distingue entre funcionalidad y mantenibilidad, y propone mejoras pequeñas conectadas con problemas reales.
```

---

# H5-S3 — Refactorización segura

## Duración

```text
45 minutos
```

## Objetivo

Planificar y ejecutar una refactorización pequeña sin cambiar el comportamiento visible del programa.

## Resultado esperado

Documento inicial `docs/informe-refactorizacion-h5.md` con:

```text
- estado antes;
- problema detectado;
- cambio realizado;
- prueba antes/después;
- riesgo;
- resultado.
```

## Guion docente

```text
Refactorizar no es reescribir a lo loco.

Una refactorización segura tiene tres ideas: sé qué problema quiero mejorar, hago un cambio pequeño y compruebo que el comportamiento sigue funcionando.

Hoy no buscamos terminar H5. Buscamos aprender a cambiar con control.
```

## Pizarra

```text
Refactorización segura:
1. Observa.
2. Decide un cambio pequeño.
3. Cambia.
4. Compila.
5. Ejecuta caso mínimo.
6. Documenta.
```

## Qué explicas tú

```text
- Diferencia entre refactorización y nueva funcionalidad.
- Por qué conviene guardar evidencia antes/después.
- Por qué el cambio debe ser pequeño.
- Qué prueba manual mínima usaremos.
```

## Actividad HEXA guiada

### H — Hecho

Queremos separar un comando, pero el programa debe seguir respondiendo igual.

### E — Explorar

Pregunta:

```text
¿Qué salida esperamos antes y después para el comando ayuda?
```

### X — eXplicar

Respuesta esperada:

```text
La salida puede cambiar un poco en formato, pero debe seguir mostrando comandos disponibles y no romper el flujo.
```

### A — Aplicar

Escribir una prueba manual antes/después.

## Actividad

Prueba manual mínima:

```text
Entrada:
ayuda
estado
recuerda
Traer libreta
memoria
salir

Comprobaciones:
- ayuda muestra comandos;
- estado muestra número de recuerdos;
- recuerda guarda texto;
- memoria muestra el recuerdo;
- salir termina.
```

Plantilla de informe:

```markdown
# Informe de refactorización H5

## Estado antes

## Problema detectado

## Cambio realizado

## Prueba antes

## Prueba después

## Riesgo

## Resultado
```

## Errores frecuentes

| Error | Señal | Intervención docente |
|---|---|---|
| Refactorización demasiado grande | Muchas clases nuevas de golpe | Separar primero un comando. |
| No compilar entre pasos | Error acumulado difícil | Compilar tras cada cambio pequeño. |
| No documentar antes | Solo explican al final | Escribir estado antes antes de tocar. |
| Cambiar comportamiento sin darse cuenta | Comandos dejan de funcionar | Usar prueba manual fija. |

## Cierre

Ticket:

```text
1. ¿Qué cambio pequeño harás primero?
2. ¿Qué comando usarás para comprobar que no rompiste nada?
3. ¿Qué escribirás en el informe antes de modificar código?
```

## Criterio de éxito

```text
El alumnado planifica una refactorización limitada, verificable y documentada.
```

---

# H5-S4 — Interfaz o contrato Tool

## Duración

```text
45 minutos
```

## Objetivo

Crear un contrato común para herramientas/comandos mediante una interfaz `Tool` o una clase equivalente si el grupo necesita simplificación.

## Resultado esperado

Archivo `src/Tool.java` creado y primer comando separado, por ejemplo `HelpTool`.

## Guion docente

```text
Si queremos que Agent pueda trabajar con varias herramientas de forma parecida, necesitamos un acuerdo común.

En Java ese acuerdo puede representarse con una interfaz. Una interfaz dice qué métodos debe ofrecer una herramienta, pero cada herramienta decide cómo ejecutarlos.
```

## Pizarra

```text
Tool = contrato común

Toda Tool debe saber:
- cuál es su nombre;
- qué descripción tiene;
- cómo se ejecuta.
```

## Qué explicas tú

```text
- Qué es una interfaz de forma práctica.
- Que `Tool` no ejecuta nada por sí sola.
- Que `HelpTool`, `RememberTool` o `StatusTool` implementan ese contrato.
- Que esto facilita tratar comandos diferentes de forma uniforme.
```

## Actividad HEXA guiada

### H — Hecho

Tenemos comandos distintos pero todos comparten una idea: se invocan por nombre y hacen algo.

### E — Explorar

Pregunta:

```text
¿Qué información mínima debería tener cualquier herramienta?
```

Respuestas esperadas:

```text
- nombre del comando;
- descripción;
- acción al ejecutarse.
```

### X — eXplicar

Conclusión:

```text
Podemos crear un contrato Tool para que todas las herramientas tengan la misma forma externa.
```

### A — Aplicar

Crear `Tool.java` y una primera herramienta.

## Código base guiado

```java
public interface Tool {
    String getName();
    String getDescription();
    boolean execute(Agent agent);
}
```

Primer ejemplo:

```java
public class HelpTool implements Tool {
    public String getName() {
        return "ayuda";
    }

    public String getDescription() {
        return "Muestra los comandos disponibles.";
    }

    public boolean execute(Agent agent) {
        agent.showHelp();
        return true;
    }
}
```

Nota docente importante:

```text
Este ejemplo exige que Agent tenga un método público controlado para mostrar ayuda, o que HelpTool reciba la lista de herramientas de otra forma. Si el grupo se bloquea, primero se puede hacer HelpTool con un mensaje fijo.
```

Versión simplificada de `HelpTool`:

```java
public class HelpTool implements Tool {
    public String getName() {
        return "ayuda";
    }

    public String getDescription() {
        return "Muestra ayuda.";
    }

    public boolean execute(Agent agent) {
        System.out.println("Comandos: ayuda, saluda, recuerda, memoria, estado, curso, salir");
        return true;
    }
}
```

## Actividad

```text
1. Crear Tool.java.
2. Crear HelpTool.java.
3. Comprobar que HelpTool implementa los tres métodos.
4. Compilar.
5. Escribir en el informe qué problema empieza a resolver Tool.
```

Comando:

```bash
javac src/*.java
```

## Errores frecuentes

| Error | Señal | Intervención docente |
|---|---|---|
| No implementar todos los métodos | Error de compilación | Leer el contrato Tool y completar. |
| Confundir interfaz con clase normal | Intentan `new Tool()` | Explicar que se crean herramientas concretas. |
| Hacer Tool demasiado compleja | Añaden parámetros innecesarios | Mantener nombre, descripción y execute. |
| Bloqueo por dependencias con Agent | HelpTool necesita demasiados datos | Usar versión simplificada primero. |

## Cierre

Ticket:

```text
1. ¿Qué métodos exige Tool?
2. ¿Por qué HelpTool puede tratarse como Tool?
3. ¿Qué ventaja tiene que todas las herramientas tengan la misma forma?
```

## Criterio de éxito

```text
Existe un contrato Tool comprensible y al menos una herramienta separada que compila.
```

---

# H5-S5 — Separar herramientas principales

## Duración

```text
45 minutos
```

## Objetivo

Separar varios comandos de `Agent` en clases de herramienta, manteniendo `Agent` como orquestador.

## Resultado esperado

Herramientas mínimas creadas:

```text
HelpTool
RememberTool
MemoryTool
StatusTool
ExitTool
```

## Guion docente

```text
Ya tenemos el contrato Tool. Ahora vamos a usarlo para reducir el peso de Agent.

Agent no desaparece. Agent coordina, guarda la memoria compartida y busca qué herramienta ejecutar.

Las herramientas contienen comportamientos concretos.
```

## Pizarra

```text
Antes:
Agent tiene un if/else largo.

Después:
Agent tiene lista de Tool.
Cada Tool sabe ejecutar un comando.
```

## Qué explicas tú

```text
- Que las herramientas no deben duplicar la memoria.
- Que Agent puede compartir su Memory mediante métodos controlados.
- Que añadir una herramienta no debería obligar a tocar processCommand entero.
- Que todavía no estamos haciendo plugins reales.
```

## Actividad HEXA guiada

### H — Hecho

`RememberTool` necesita guardar en memoria.

### E — Explorar

Pregunta:

```text
¿Debe RememberTool crear su propia Memory o usar la Memory del Agent?
```

### X — eXplicar

Respuesta esperada:

```text
Debe usar la Memory del Agent; si crea otra, los recuerdos se separan y se pierden coherencia.
```

### A — Aplicar

Crear herramientas que usan métodos públicos controlados de Agent.

## Código orientativo

Métodos útiles en `Agent`:

```java
public Memory getMemory() {
    return memory;
}

public void requestStop() {
    running = false;
}

public String getName() {
    return name;
}

public int getCourseYear() {
    return courseYear;
}
```

Ejemplo `StatusTool`:

```java
public class StatusTool implements Tool {
    public String getName() {
        return "estado";
    }

    public String getDescription() {
        return "Muestra el estado de MiniJarvis.";
    }

    public boolean execute(Agent agent) {
        System.out.println("Soy " + agent.getName() + " H5.");
        System.out.println("Tengo " + agent.getMemory().count() + " recuerdos.");
        return true;
    }
}
```

Ejemplo `ExitTool`:

```java
public class ExitTool implements Tool {
    public String getName() {
        return "salir";
    }

    public String getDescription() {
        return "Termina el programa.";
    }

    public boolean execute(Agent agent) {
        agent.requestStop();
        System.out.println("Hasta pronto.");
        return true;
    }
}
```

## Actividad

```text
1. Crear dos herramientas sencillas primero: StatusTool y ExitTool.
2. Compilar.
3. Integrarlas en la lista de herramientas del Agent.
4. Ejecutar comandos estado y salir.
5. Crear después RememberTool y MemoryTool.
6. Documentar qué líneas se redujeron o movieron desde Agent.
```

Prueba mínima:

```text
estado
recuerda
Traer libreta
memoria
salir
```

## Errores frecuentes

| Error | Señal | Intervención docente |
|---|---|---|
| Cada herramienta crea su propia memoria | `memoria` no muestra lo recordado | Usar Memory compartida del Agent. |
| Agent deja de coordinar | Las herramientas controlan todo | Repartir: Agent orquesta, Tool ejecuta una acción. |
| Métodos públicos excesivos en Agent | Exponen todo por comodidad | Publicar solo lo necesario. |
| Separar todo de golpe | Muchos errores de compilación | Separar una herramienta cada vez. |

## Cierre

Ticket:

```text
1. ¿Por qué RememberTool no debe crear otra Memory?
2. ¿Qué responsabilidad conserva Agent?
3. ¿Qué herramienta has separado hoy?
```

## Criterio de éxito

```text
Varias herramientas funcionan como clases separadas y Agent empieza a delegar en ellas sin perder el estado compartido.
```

---

# H5-S6 — Añadir una herramienta nueva con bajo impacto

## Duración

```text
45 minutos
```

## Objetivo

Comprobar la extensibilidad añadiendo una herramienta nueva sin modificar muchas partes del programa.

## Resultado esperado

Nueva herramienta, por ejemplo `CourseTool`, añadida con evidencia:

```text
- archivo nuevo de herramienta;
- registro en Agent;
- prueba de ejecución;
- explicación de cuántos cambios fueron necesarios.
```

## Guion docente

```text
Hoy vamos a comprobar si la refactorización sirve para algo.

La prueba de extensibilidad es sencilla: añadimos un comando nuevo. Si para añadirlo tocamos medio programa, H5 no ha conseguido su objetivo. Si creamos una clase y la registramos, vamos en buena dirección.
```

## Pizarra

```text
Prueba H5:
Añadir comando `curso`.

Cambios esperados:
1. Crear CourseTool.java.
2. Registrar CourseTool en Agent.
3. Probar comando curso.
```

## Qué explicas tú

```text
- Qué significa bajo impacto.
- Que añadir una clase nueva puede ser mejor que tocar un método enorme.
- Que no buscamos cero cambios, sino cambios localizados.
- Que la prueba debe documentarse en el informe.
```

## Actividad HEXA guiada

### H — Hecho

Queremos un comando `curso` que muestre información ficticia del proyecto.

### E — Explorar

Pregunta:

```text
¿Dónde debería vivir el código de ese comando si ya tenemos Tool?
```

### X — eXplicar

Respuesta esperada:

```text
En una clase CourseTool que implemente Tool.
```

### A — Aplicar

Crear y registrar `CourseTool`.

## Código orientativo

```java
public class CourseTool implements Tool {
    public String getName() {
        return "curso";
    }

    public String getDescription() {
        return "Muestra información del proyecto MiniJarvis.";
    }

    public boolean execute(Agent agent) {
        System.out.println("Proyecto MiniJarvis — 1.º DAW — Curso " + agent.getCourseYear());
        System.out.println("H5: extensibilidad, clean code y patrones iniciales.");
        return true;
    }
}
```

Registro en `Agent`:

```java
private void registerTools() {
    tools.add(new HelpTool());
    tools.add(new GreetTool());
    tools.add(new RememberTool());
    tools.add(new MemoryTool());
    tools.add(new StatusTool());
    tools.add(new CourseTool());
    tools.add(new ExitTool());
}
```

## Actividad

```text
1. Crear CourseTool.java.
2. Registrar la herramienta.
3. Ejecutar el programa.
4. Probar `ayuda` y comprobar si aparece curso.
5. Probar `curso`.
6. Escribir en el informe cuántos archivos se han modificado.
```

Pregunta de análisis:

```text
¿Ha sido más fácil que añadir otro else if? ¿Por qué?
```

## Errores frecuentes

| Error | Señal | Intervención docente |
|---|---|---|
| Crear la clase pero no registrarla | El comando no responde | Revisar `registerTools()`. |
| Registrar pero no compilar | Error de nombre de clase | Verificar archivo y clase con mismo nombre. |
| Modificar muchas clases sin necesidad | Cambios dispersos | Volver a la meta: clase nueva + registro. |
| Hacer CourseTool demasiado ambiciosa | Añade datos reales o persistencia | Mantener información ficticia y simple. |

## Cierre

Ticket:

```text
1. ¿Qué archivos tocaste para añadir curso?
2. ¿Qué demuestra esta prueba sobre extensibilidad?
3. ¿Qué riesgo sigue existiendo aunque usemos Tool?
```

## Criterio de éxito

```text
El alumnado añade una herramienta nueva con cambios localizados y puede explicar por qué el diseño es más extensible que el if/else largo.
```

---

# H5-S7 — Patrón Command simplificado o decisión de no patrón

## Duración

```text
45 minutos
```

## Objetivo

Comprender que un patrón de diseño debe responder a un problema real, y registrar si H5 usa un Command simplificado o una solución equivalente sin forzar terminología.

## Resultado esperado

Documento `docs/registro-patron-h5.md` con:

```text
- problema de diseño;
- alternativa simple;
- solución elegida;
- por qué se parece o no al patrón Command;
- riesgo de sobreingeniería;
- decisión final defendible.
```

## Guion docente

```text
Hoy aparece una palabra profesional: patrón de diseño.

Un patrón no es una medalla ni una obligación. Es una solución conocida para un problema que se repite.

Nuestro problema: representar comandos como objetos o herramientas separadas. Eso se parece a una versión sencilla del patrón Command.
```

## Pizarra

```text
Problema:
Cada comando es una acción que quiero separar.

Solución H5:
Tool + clases concretas.

Nombre profesional posible:
Command simplificado.

Peligro:
Usar patrones sin entender el problema.
```

## Qué explicas tú

```text
- Qué es un patrón de diseño en lenguaje de 1.º DAW.
- Que no hace falta implementar Command completo ni invocadores complejos.
- Que se puede decir “usamos una idea parecida a Command”.
- Que también es válido descartar un patrón si complica demasiado.
```

## Actividad HEXA guiada

### H — Hecho

Ahora cada comando vive en una clase que implementa `Tool`.

### E — Explorar

Pregunta:

```text
¿Qué problema real resuelve esta estructura?
```

Respuestas esperadas:

```text
- separar acciones;
- añadir comandos con menos cambios;
- reducir processCommand;
- hacer revisión más sencilla.
```

### X — eXplicar

Conclusión:

```text
La estructura se parece a Command porque encapsula acciones en objetos.
```

### A — Aplicar

Completar registro de patrón.

## Plantilla autónoma

```markdown
# Registro de patrón H5

## Problema

## Solución simple inicial

## Solución aplicada

## ¿Se parece al patrón Command?

## Qué ventaja aporta

## Qué riesgo de sobreingeniería existe

## Decisión final

## Cómo lo defenderé oralmente
```

Ejemplo de defensa aceptable:

```text
No he usado Command completo. He usado una versión simplificada: cada herramienta tiene nombre, descripción y execute. Esto me permite separar comandos y añadir `curso` con menos impacto.
```

## Errores frecuentes

| Error | Señal | Intervención docente |
|---|---|---|
| Patrón como palabra vacía | “Uso Command porque sí” | Pedir problema que resuelve. |
| Implementación demasiado avanzada | Invokers, receivers complejos, factories innecesarias | Volver a Tool simple. |
| Rechazar todo patrón | “Los patrones son malos” | Aclarar que el problema manda. |
| Copiar explicación de IA | Lenguaje no defendible | Pedir explicación con CourseTool delante. |

## Cierre

Ticket:

```text
1. ¿Qué problema resuelve nuestra idea de Tool?
2. ¿Por qué no debemos usar patrones porque sí?
3. Escribe una frase defendible sobre Command simplificado.
```

## Criterio de éxito

```text
El alumnado vincula patrón y problema real, y puede defender una decisión prudente sin sobreingeniería.
```

---

# H5-S8 — Git, revisión de código y evidencia

## Duración

```text
45 minutos
```

## Objetivo

Registrar la refactorización y realizar una revisión de código centrada en extensibilidad, claridad y riesgo.

## Resultado esperado

Dos evidencias:

```text
1. docs/evidencia-git-h5.md
2. docs/revision-codigo-h5.md
```

Si se usa Git real:

```text
- rama o registro de trabajo;
- commits con mensajes comprensibles;
- diff revisado;
- nota de revisión.
```

Si no se usa Git real:

```text
- registro equivalente con fecha, cambio, archivo, motivo y verificación.
```

## Guion docente

```text
En desarrollo profesional no basta con decir “lo he cambiado”. Debe quedar rastro de qué se cambió, por qué y cómo se revisó.

Si usamos Git, lo veremos con commits o diff. Si el entorno no permite Git todavía, haremos un registro equivalente de aula.
```

## Pizarra

```text
Evidencia mínima:
Cambio -> Motivo -> Archivo -> Prueba -> Revisión
```

## Qué explicas tú

```text
- Qué es trazabilidad de cambios.
- Por qué una refactorización necesita revisión.
- Qué mirar en una revisión de código H5.
- Que la revisión no es buscar culpables, sino reducir riesgos.
```

## Actividad HEXA guiada

### H — Hecho

El código ha cambiado internamente.

### E — Explorar

Pregunta:

```text
¿Qué debería comprobar una compañera antes de aceptar la refactorización?
```

Respuestas esperadas:

```text
- compila;
- comandos básicos funcionan;
- herramientas tienen nombres claros;
- no hay duplicación innecesaria;
- Agent no vuelve a crecer demasiado;
- CourseTool se añadió con cambios localizados.
```

### X — eXplicar

Conclusión:

```text
La revisión ayuda a confirmar que la mejora no ha introducido errores ni complejidad innecesaria.
```

### A — Aplicar

Revisión por parejas.

## Plantilla de evidencia Git o equivalente

```markdown
# Evidencia Git o registro equivalente — H5

| Fecha | Cambio | Archivo(s) | Motivo | Verificación |
|---|---|---|---|---|
| | | | | |

## Si he usado Git

Rama:
Commits relevantes:
Diff revisado:

## Si no he usado Git real

Motivo:
Registro equivalente usado:
```

## Plantilla de revisión de código

```markdown
# Revisión de código H5

Revisor/a:
Autor/a:
Fecha:

## Checklist

| Elemento | Sí | Parcial | No | Observación |
|---|---|---|---|---|
| Compila | | | | |
| Comandos básicos funcionan | | | | |
| Agent coordina sin crecer demasiado | | | | |
| Tool es simple | | | | |
| Herramientas tienen responsabilidad clara | | | | |
| CourseTool se añade con bajo impacto | | | | |
| No hay persistencia adelantada | | | | |
| Nombres comprensibles | | | | |

## Cambio recomendado

## Riesgo detectado

## Decisión
```

## Errores frecuentes

| Error | Señal | Intervención docente |
|---|---|---|
| Evidencia Git decorativa | Mensajes “cambios” sin contenido | Pedir motivo y verificación. |
| Revisión superficial | Todo sí sin mirar código | Asignar una clase concreta a revisar. |
| Crítica personal | Comentarios sobre la persona | Reencuadrar a código y evidencias. |
| Git bloquea la sesión | Problemas técnicos con cuentas | Usar registro equivalente de aula. |

## Cierre

Ticket:

```text
1. ¿Qué cambio de H5 queda trazado?
2. ¿Qué ha detectado la revisión?
3. ¿Qué comprobarías antes de pasar a H6?
```

## Criterio de éxito

```text
Existe evidencia trazable de la refactorización y una revisión de código útil, aunque sea mediante registro equivalente si Git real no está disponible.
```

---

# H5-S9 — Comparación Java ↔ Python y documentación H5

## Duración

```text
45 minutos
```

## Objetivo

Comparar la solución H5 en Java con una idea equivalente en Python y cerrar la documentación técnica del hito.

## Resultado esperado

Documentos actualizados:

```text
- docs/comparacion-java-python-h5.md;
- docs/informe-refactorizacion-h5.md;
- docs/portfolio-h5.md;
- docs/registro-ia.md si procede.
```

## Guion docente

```text
Java nos obliga a declarar de forma explícita la interfaz Tool. Python puede resolver ideas parecidas con objetos que tengan el método esperado, aunque no declaren una interfaz igual.

Comparar lenguajes nos ayuda a entender el concepto, no a mezclar sintaxis dentro del proyecto.
```

## Pizarra

```text
Java:
interface Tool { execute(Agent agent); }
class StatusTool implements Tool { ... }

Python:
class StatusTool:
    def execute(self, agent):
        ...

Idea común:
objeto que representa una acción/comando.
```

## Qué explicas tú

```text
- Qué es una interfaz Java de forma práctica.
- Qué es duck typing explicado con cuidado: “si se comporta como herramienta, puede usarse como herramienta”.
- Que Python no exige la misma declaración formal en el nivel básico.
- Que la comparación debe quedarse en conceptos H5.
```

## Actividad HEXA guiada

### H — Hecho

En Java `StatusTool implements Tool`.

### E — Explorar

Pregunta:

```text
¿Qué tendría que tener una clase Python para poder actuar como herramienta?
```

### X — eXplicar

Respuesta esperada:

```text
Un nombre, una descripción si queremos mostrar ayuda, y un método execute o equivalente.
```

### A — Aplicar

Completar tabla comparativa.

## Plantilla de comparación

```markdown
# Comparación Java ↔ Python — H5

| Concepto | Java | Python | Qué debo recordar |
|---|---|---|---|
| Contrato | `interface Tool` | convención o clase base opcional | Java lo exige de forma explícita. |
| Implementación | `implements Tool` | método con el nombre esperado | Python es más flexible. |
| Comando como objeto | `new StatusTool()` | `StatusTool()` | La idea común es encapsular una acción. |
| Método de ejecución | `execute(Agent agent)` | `execute(agent)` | El comando recibe contexto. |
| Riesgo | demasiadas clases sin motivo | objetos sin contrato claro | El diseño debe ser defendible. |
```

## Documentación final H5

Portfolio mínimo:

```text
1. Qué problema tenía mi H4.
2. Qué refactorización hice.
3. Qué herramienta nueva añadí.
4. Qué evidencia tengo.
5. Qué patrón usé o descarté.
6. Qué aprendí sobre clean code.
7. Qué necesito mejorar para H6.
```

Registro IA mínimo si se usó:

```text
Fecha:
Herramienta:
Prompt:
Respuesta útil:
Qué acepté:
Qué rechacé:
Cómo verifiqué:
Qué entiendo ahora con mis palabras:
```

## Uso de IA permitido

```text
Se puede pedir a una IA que explique la diferencia entre interfaz Java y duck typing de Python para nivel principiante.
```

Condición:

```text
La respuesta debe reescribirse con palabras propias y conectarse con Tool, StatusTool o CourseTool del propio código.
```

## Errores frecuentes

| Error | Señal | Intervención docente |
|---|---|---|
| Comparación demasiado avanzada | Abstract classes, reflection, frameworks | Volver a Tool y execute. |
| Mezclar Python en el proyecto Java | Intentan ejecutar sintaxis Python | Aclarar que es comparación conceptual. |
| Documentación genérica | No cita su propio código | Pedir una clase concreta y un cambio real. |
| Registro IA incompleto | Solo pone “usé ChatGPT” | Exigir prompt, uso, verificación y palabras propias. |

## Cierre

Ticket:

```text
1. ¿Qué diferencia hay entre `interface Tool` en Java y una convención en Python?
2. ¿Qué herramienta de tu código demuestra H5?
3. ¿Qué documento te falta cerrar antes de defender?
```

## Criterio de éxito

```text
El alumnado documenta H5 con evidencias propias y compara Java/Python sin perder el foco en herramientas, contratos y extensibilidad.
```

---

# H5-S10 — Defensa H5

## Duración

```text
45 minutos
```

## Objetivo

Validar H5 mediante ejecución, revisión de extensibilidad, documentación y defensa individual de la refactorización.

## Resultado esperado

H5 entregado con:

```text
- código Java compilable y ejecutable;
- Tool o solución equivalente;
- varias herramientas separadas;
- una herramienta nueva añadida con bajo impacto;
- informe de refactorización;
- evidencia Git o registro equivalente;
- revisión de código;
- registro de patrón usado o descartado;
- comparación Java ↔ Python;
- portfolio y registro IA si procede;
- defensa individual.
```

## Guion docente

```text
Hoy no se defiende que MiniJarvis tenga más comandos. Se defiende que ahora es más fácil añadir comandos de forma controlada.

La pregunta clave de H5 es: ¿qué problema tenía el diseño anterior y cómo demuestra tu código que ahora es más extensible?
```

## Pizarra

```text
Defensa H5:
1. Ejecuta.
2. Enseña Tool o solución equivalente.
3. Enseña una herramienta concreta.
4. Explica qué cambió en Agent.
5. Demuestra comando nuevo.
6. Enseña evidencia de refactorización/revisión.
7. Defiende patrón usado o descartado.
```

## Qué explicas tú

```text
- Que se evalúa cambio razonado, no cantidad de clases.
- Que la defensa debe citar código real.
- Que Git o el registro equivalente son evidencia, no decoración.
- Que el patrón debe conectarse con el problema.
```

## Actividad HEXA guiada

### H — Hecho

Añadir un comando nuevo debería ser más sencillo que en H4.

### E — Explorar

Pregunta:

```text
¿Qué evidencias demuestran que H5 mejora extensibilidad?
```

Respuestas esperadas:

```text
- Tool o contrato común;
- herramientas separadas;
- CourseTool añadida con pocos cambios;
- Agent más corto o más claro;
- informe antes/después;
- revisión de código;
- defensa de patrón prudente.
```

### X — eXplicar

Conclusión:

```text
H5 está consolidado si el diseño facilita cambios futuros sin introducir complejidad que no se pueda defender.
```

### A — Aplicar

Defensa por turnos con checklist.

## Checklist docente de defensa

| Elemento | Sí | Parcial | No | Observación |
|---|---|---|---|---|
| Compila y ejecuta | | | | |
| Mantiene funciones básicas H4 | | | | |
| Existe Tool o contrato equivalente | | | | |
| Hay herramientas separadas | | | | |
| Agent delega en herramientas | | | | |
| Memory sigue siendo responsabilidad separada | | | | |
| Se añadió herramienta nueva | | | | |
| Cambios localizados | | | | |
| Informe de refactorización claro | | | | |
| Evidencia Git o equivalente | | | | |
| Revisión de código útil | | | | |
| Registro de patrón razonado | | | | |
| Comparación Java/Python comprensible | | | | |
| No introduce persistencia ni IA real | | | | |
| Defensa individual suficiente | | | | |

## Preguntas de defensa

```text
1. ¿Qué problema tenía tu Agent al final de H4?
2. ¿Qué significa extensibilidad en H5?
3. ¿Qué es Tool en tu diseño?
4. Señala una herramienta concreta y explica su responsabilidad.
5. ¿Qué hizo falta cambiar para añadir CourseTool?
6. ¿Qué parte de Agent se redujo o mejoró?
7. ¿Qué riesgo tenía tu refactorización?
8. ¿Cómo comprobaste que no rompiste recuerda/memoria/estado?
9. ¿Qué evidencia Git o equivalente puedes enseñar?
10. ¿Qué detectó la revisión de código?
11. ¿Tu solución usa una idea parecida a Command? ¿Por qué?
12. ¿Qué sería sobreingeniería en este hito?
13. ¿Qué diferencia hay entre interface Java y duck typing en Python?
14. ¿Qué uso de IA has hecho y cómo lo verificaste?
15. ¿Qué queda preparado para H6?
```

## Errores frecuentes

| Error | Señal | Intervención docente |
|---|---|---|
| Defender cantidad de clases | “Tengo muchas tools” | Preguntar qué problema resuelve cada una. |
| No demostrar comando nuevo | Habla de extensibilidad sin prueba | Pedir ejecutar `curso` o herramienta equivalente. |
| Agent sigue igual de largo | Solo añadieron clases decorativas | Revisar si realmente delega. |
| Patrón no defendible | Repite definición sin conectar código | Pedir señalar Tool y una implementación. |
| Evidencia Git vacía | No hay cambios trazables | Aceptar recuperación con registro equivalente claro. |
| Romper H4 | recuerda o memoria ya no funcionan | Priorizar recuperación funcional. |

Intervención oral si la defensa se atasca:

```text
No defiendas todo el proyecto. Defiende esta cadena:
Agent recibe un comando.
Agent busca una Tool.
La Tool ejecuta una acción.
Memory conserva los recuerdos.
CourseTool demuestra que puedo añadir una herramienta nueva.
```

Búsqueda guiada en el código:

```text
1. Busca `interface Tool`.
2. Busca `implements Tool`.
3. Busca `registerTools()`.
4. Busca `new CourseTool()`.
5. Busca `execute(Agent agent)`.
6. Busca `memory.add` o `getMemory().add`.
```

## Recuperación inmediata

Si no compila:

```text
Reducir a Tool + StatusTool + ExitTool + Agent compilable. Después recuperar RememberTool y MemoryTool.
```

Si no hay extensibilidad real:

```text
Crear una herramienta nueva mínima y registrar solo esa. Documentar cuántos cambios hizo falta tocar.
```

Si el patrón está forzado:

```text
Reescribir registro de patrón diciendo: usamos una idea sencilla de comandos separables; no implementamos Command completo porque sería excesivo.
```

Si no hay evidencia Git:

```text
Crear registro equivalente con fecha, cambio, archivo, motivo y prueba manual. No inventar commits.
```

Si la revisión de código es superficial:

```text
Revisar una clase concreta con tres preguntas: qué hace, qué depende de ella y qué riesgo tiene.
```

## Cierre de H5

Guion:

```text
H5 nos enseña una idea profesional: el código no solo debe funcionar hoy, debe poder cambiar mañana.

MiniJarvis ya tiene una estructura más extensible. Hemos visto clean code, refactorización, revisión, evidencia de cambios y una primera aproximación prudente a patrones.

En H6 cambiaremos de problema: hasta ahora la memoria desaparece al cerrar el programa. En H6 trabajaremos persistencia, trazabilidad y seguridad básica al guardar información.
```

## Criterio de éxito

```text
El alumnado entrega un H5 funcional y puede defender que su refactorización mejora la extensibilidad sin introducir complejidad innecesaria.
```

---

## 5. Evaluación formativa de H5

H5 debe servir para detectar:

```text
- quién entiende la diferencia entre funcionar y ser mantenible;
- quién puede refactorizar sin romper comportamiento;
- quién identifica olores de código sencillos;
- quién separa comandos con responsabilidad clara;
- quién usa interfaces o contratos sin convertirlos en magia;
- quién documenta cambios con trazabilidad;
- quién revisa código con criterio;
- quién distingue patrón útil de patrón decorativo;
- quién compara Java/Python a nivel conceptual;
- quién usa IA como apoyo y no como sustituto de comprensión.
```

Evidencias mínimas:

| Evidencia | Qué mirar |
|---|---|
| Código | Compila, ejecuta y conserva funciones H4. |
| `Tool.java` o equivalente | Contrato simple y comprensible. |
| Herramientas | Responsabilidades separadas y nombres claros. |
| `Agent.java` | Orquesta y delega, no concentra todos los comandos. |
| Nueva herramienta | Se añade con cambios localizados. |
| Informe de refactorización | Explica antes/después y riesgo. |
| Evidencia Git/equivalente | Muestra cambios, motivo y verificación. |
| Revisión de código | Detecta riesgos o confirma criterios. |
| Registro de patrón | Conecta problema y solución. |
| Comparación Java/Python | Explica interface vs convención/duck typing sin exceso. |
| Defensa | La persona entiende su propio cambio. |

---

## 6. Atención a la diversidad

### Si el alumnado se bloquea con interfaces

Reducir objetivo:

```text
Crear clases de comando con el mismo método `execute`, aunque todavía no usen interface.
Después introducir Tool como contrato común.
```

Secuencia reducida:

```text
1. StatusTool con método execute.
2. ExitTool con método execute.
3. Ver que ambas se parecen.
4. Extraer Tool como contrato.
```

### Si el alumnado se bloquea con demasiadas herramientas

Reducir objetivo:

```text
Mantener solo tres herramientas: HelpTool, StatusTool y ExitTool.
Demostrar después una cuarta: CourseTool.
```

No exigir todas las herramientas si se pierde comprensión.

### Si el alumnado copia una arquitectura avanzada

Reencuadre:

```text
Si no puedes explicar cada clase en una frase, hay demasiada arquitectura para H5.
```

Preguntas de control:

```text
¿Qué problema resuelve esta clase?
¿Qué pasaría si la quitamos?
¿Qué archivo debo tocar para añadir un comando nuevo?
```

### Si el alumnado no controla Git

Usar registro equivalente:

```text
Fecha, archivo, cambio, motivo, prueba y revisión.
```

No bloquear H5 por autenticación, GitHub o credenciales. La seguridad y la trazabilidad didáctica son prioritarias.

### Si hay alumnado avanzado

Extensión permitida:

```text
Usar `HashMap<String, Tool>` para buscar herramientas por nombre si puede defender por qué mejora la búsqueda.
```

Extensión no obligatoria:

```text
Factories, reflection, carga dinámica de plugins, anotaciones o frameworks.
```

---

## 7. Uso responsable de IA en H5

Usos permitidos:

```text
- pedir explicación sencilla de refactorización;
- pedir ejemplos mínimos de interfaz Java;
- pedir preguntas de revisión de código;
- comparar Command simplificado con una solución sin patrón;
- pedir explicación de interface Java frente a duck typing de Python.
```

Usos no permitidos:

```text
- generar una arquitectura completa no defendible;
- añadir patrones complejos sin necesidad;
- copiar una revisión de código sin mirar el código real;
- inventar commits, PR o evidencias Git;
- introducir claves, tokens, datos personales o repositorios privados en prompts sin permiso y protección.
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
La IA puede sugerir refactorizaciones, pero tú debes demostrar que el cambio compila, funciona y mejora un problema real de tu MiniJarvis.
```

---

## 8. Criterios globales de éxito de H5

H5 está consolidado cuando:

```text
[x] El programa compila.
[x] Los comandos básicos siguen funcionando.
[x] Agent no concentra todo el bloque de comandos.
[x] Existe Tool o contrato equivalente.
[x] Hay herramientas separadas con responsabilidad clara.
[x] Memory sigue encapsulando recuerdos.
[x] Se añade al menos una herramienta nueva con bajo impacto.
[x] La refactorización está documentada antes/después.
[x] Hay evidencia Git o registro equivalente veraz.
[x] Hay revisión de código útil.
[x] El patrón Command se usa o descarta con motivo.
[x] La comparación Java ↔ Python es comprensible.
[x] El alumnado puede defender extensibilidad, clean code y riesgo de sobreingeniería.
```

---

## 9. Puente hacia H6

Mensaje final al grupo:

```text
En H5 hemos aprendido a cambiar el diseño sin perder el control.

Ahora MiniJarvis puede crecer mejor: añadir herramientas es más ordenado, el código está más revisado y las decisiones quedan documentadas.

En H6 aparecerá un problema nuevo: la memoria temporal sigue desapareciendo al cerrar el programa. Trabajaremos persistencia en ficheros, trazabilidad de acciones y seguridad básica para no guardar información sensible.
```

Preparación docente para la siguiente fase:

```text
Selecciona tres evidencias H5:
- un ejemplo donde CourseTool se añadió con bajo impacto;
- un ejemplo donde se usó un patrón de forma prudente;
- un ejemplo donde la revisión detectó un problema real.

Servirán para iniciar H6 conectando extensibilidad con persistencia y trazabilidad.
```
