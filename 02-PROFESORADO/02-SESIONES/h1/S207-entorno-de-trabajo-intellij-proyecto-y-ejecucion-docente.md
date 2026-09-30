# S207 — Del código fuente a la primera ejecución

| Dato | Valor |
|---|---|
| Hito | H1 — Primer asistente ejecutable |
| Duración prevista | 45 minutos |
| Fase HEXA del hito | Investigar — aprender lo necesario |
| Modalidad de trabajo | **INDIVIDUAL → PAREJAS** |

> Basada en `00-GUION-DOCENTE-H1-COMPLETO.md`.

## Finalidad de la sesión

El alumnado debe comprender qué ocurre entre escribir un programa y observar su salida:

```text
código fuente → compilación → ejecución → consola
```

La meta no es aprender a pulsar `Run`, sino localizar el código, anticipar el resultado, ejecutar, comprobar la consola y explicar por qué la salida demuestra que el programa se ha puesto en marcha.

## Antes de entrar en clase

- [ ] Comprobar que el JDK y el proyecto Java utilizado están configurados.
- [ ] Abrir y ejecutar el `Main.java` de referencia.
- [ ] Preparar una alternativa si algún puesto no puede abrir el proyecto.
- [ ] Verificar dónde muestra IntelliJ el primer diagnóstico y la consola.
- [ ] Evitar que la sesión se convierta en una explicación extensa de configuración.

## Apertura docente

Di en voz alta:

> Hoy estamos en Investigar. Necesitamos entender qué ocurre entre escribir `Main.java` y ver un mensaje. Escribir no es ejecutar, compilar no es ejecutar y la consola no es el código.

Pregunta:

> Si el texto está escrito dentro de `Main.java`, ¿podemos afirmar ya que el programa se ha ejecutado? ¿Qué tendríamos que observar para comprobarlo?

## Recorrido: del código a la consola

Presenta el recorrido completo como una relación entre cuatro etapas.

### 1. Código fuente

Es el programa escrito por una persona en un archivo como `Main.java`. Puede leerse y modificarse. En esta sesión el alumnado debe localizar el archivo dentro del proyecto, no limitarse a reconocer el texto mostrado en el editor.

Pregunta:

> ¿En qué archivo está el programa que vamos a ejecutar y dónde aparece ese archivo dentro del proyecto?

### 2. Compilación

Antes de ejecutar, las herramientas del JDK comprueban y traducen el código fuente a una forma que Java puede poner en marcha. Un error sencillo de escritura puede impedir que esta etapa termine.

En este nivel no es necesario desarrollar el funcionamiento interno de la JVM o de una toolchain. Basta con comprender que el código fuente no pasa directamente a la consola.

### 3. Ejecución

Si la compilación permite continuar y el proyecto está configurado, Java pone en marcha el programa. La ejecución comienza en `main` y realiza las instrucciones previstas.

La acción de pulsar `Run` solicita este proceso; no garantiza por sí sola que haya terminado correctamente.

### 4. Consola

La consola muestra la salida que el programa produce durante la ejecución y también puede mostrar diagnósticos. No contiene el código fuente: permite observar qué ocurrió al intentar ejecutarlo.

Pregunta de síntesis:

> ¿Qué etapa estamos observando cuando editamos `Main.java`, cuál ocurre antes de ejecutar y qué resultado visible esperamos encontrar en la consola?

## JDK, IDE y proyecto

### JDK

El JDK aporta las herramientas necesarias para compilar y ejecutar Java en el nivel trabajado. Si no está disponible o no está asociado correctamente, el proyecto puede no arrancar aunque el fragmento de código sea correcto.

### IntelliJ / IDE

IntelliJ organiza el trabajo: muestra archivos, ofrece el editor, utiliza el JDK configurado, permite solicitar la ejecución y presenta consola y diagnósticos. El IDE facilita el proceso, pero no sustituye al entorno Java.

### Proyecto

El proyecto reúne los archivos y la configuración con la que se compila y ejecuta. Para poder hacerlo, debe tener disponible y correctamente asociado el JDK necesario.

Introduce así dos familias de fallo:

- **problema de código:** una regla escrita en `Main.java` impide compilar o produce un resultado inesperado;
- **problema de configuración:** el proyecto no tiene disponible o correctamente asociado el JDK necesario.

El alumnado no debe resolver configuraciones complejas todavía. Sí debe evitar cambiar código al azar cuando el diagnóstico apunta al entorno.

## Programa mínimo y salida esperada

Proyecta el bloque histórico sin modificar sus identificadores:

```java
public class Main {
    public static void main(String[] argumentos) {
        System.out.println("MiniJarvis arranca");
    }
}
```

Salida esperada:

```text
MiniJarvis arranca
```

Antes de ejecutar, pide que cada persona señale:

- dónde está el código fuente;
- qué instrucción producirá salida;
- qué texto espera ver exactamente;
- dónde buscará ese texto.

No desarrolles aún toda la estructura de clase, delimitadores o identificadores. S208 profundiza en esas reglas.

## Actividad central

La actividad sigue esta secuencia, sin convertir cada paso en un documento:

```text
localizar → leer → modificar únicamente el mensaje → predecir → ejecutar → comprobar → explicar → provocar un error → diagnosticar → formular una hipótesis → corregir → volver a ejecutar → contrastar
```

### Primera ejecución — INDIVIDUAL

Cada persona:

1. localiza el proyecto;
2. encuentra `Main.java`;
3. lee el programa mínimo;
4. modifica únicamente el mensaje de `println` y utiliza un texto ficticio distinto al ejemplo;
5. expresa o anota qué espera ver en consola;
6. ejecuta;
7. compara predicción y resultado;
8. explica qué archivo se ejecutó y qué salida apareció.

La predicción es una actividad pedagógica, no una fila de diario ni un entregable.

No aceptes como explicación suficiente:

> Funciona.

Pide completar:

- qué se ejecutó;
- qué salida se esperaba;
- qué salida apareció;
- por qué la coincidencia demuestra que se produjo la ejecución.

### Error deliberado y diagnóstico — INDIVIDUAL

Sobre el mismo programa, cada persona elimina temporalmente un punto y coma o una comilla. No añadas varios errores a la vez.

Debe seguir:

```text
provocar → leer diagnóstico → formular hipótesis → corregir → volver a ejecutar
```

Consigna:

> Antes de corregir, lee el primer diagnóstico y localiza la zona señalada. Explica qué crees que impide continuar. Corrige solo ese cambio y vuelve a ejecutar para comprobar la hipótesis.

La finalidad no es clasificar todos los errores, sino descubrir que el diagnóstico aporta información y que una corrección se valida mediante una nueva ejecución.

### Contraste — PAREJAS

Después de la primera ejecución individual, las parejas:

- comparan sus predicciones y salidas;
- explican el recorrido código fuente → compilación → ejecución → consola;
- muestran el primer diagnóstico leído;
- contrastan si parece un problema de código o de configuración;
- ayudan a localizar la zona relevante sin escribir la solución de la otra persona;
- comprueban que la corrección funciona al volver a ejecutar.

El trabajo por parejas no sustituye la primera ejecución individual.

## Commit descriptivo, solo cuando proceda

Si el flujo técnico del proyecto incluye un commit real tras la primera ejecución, contrasta:

```text
S207: primera ejecución por consola
```

con:

```text
cambios
```

El primer mensaje identifica el cambio realizado; el segundo no permite saber qué ocurrió. No conviertas S207 en una sesión de Git ni crees un commit artificial solo para evidenciarla.

## Evidencia que permanece

- **GitHub:** código ejecutable y evolución técnica real cuando corresponda al flujo del proyecto.
- **Scrum:** únicamente una tarea o bloqueo técnico real.
- **Diario individual:** solo si el error o descubrimiento produjo aprendizaje significativo.
- **README / Moodle / Drive / Site:** sin actualización o entrega específica en S207.

No se crea captura, copia de consola, frase obligatoria, documento de ejecución ni microentrega. La primera ejecución se comprueba ejecutando el código y relacionando predicción, salida y explicación.

## Observación docente

Durante la actividad, comprueba específicamente:

- que cada persona encuentra `Main.java`;
- que distingue el código del resultado mostrado;
- que predice antes de ejecutar;
- que explica código fuente → compilación → ejecución → consola;
- que reconoce el papel básico del JDK;
- que distingue el JDK del IDE;
- que relaciona el proyecto con archivos y configuración;
- que valora si un fallo parece de código o configuración;
- que lee el primer diagnóstico antes de cambiar código;
- que formula una hipótesis concreta;
- que valida la corrección mediante una nueva ejecución.

## Andamiaje ante bloqueos

No resuelvas automáticamente el problema. Utiliza una ayuda específica:

- **No encuentra el archivo:** pide localizar primero la estructura del proyecto y después `Main.java`.
- **Pulsa `Run` sin leer:** detén la ejecución y pide la predicción exacta.
- **Confunde IDE con Java:** pregunta qué aporta las herramientas de compilación y ejecución y qué organiza el proyecto.
- **Cambia código al azar:** pide leer en voz alta el primer diagnóstico y señalar la zona asociada.
- **No sabe si ejecutó realmente:** relaciona salida esperada, salida obtenida e instrucción que la produce.
- **Sospecha de configuración:** reduce la prueba al programa mínimo antes de modificar muchas cosas.
- **La pareja resuelve por otra persona:** pide que dé una pista y que la persona afectada formule la hipótesis y ejecute la corrección.

## Temporalización orientativa

| Tiempo | Acción |
|---|---|
| 0–5 min | Localizar proyecto, `Main.java`, editor y consola. |
| 5–12 min | Explicar código fuente → compilación → ejecución → consola y el papel de JDK, IDE y proyecto. |
| 12–18 min | Leer el programa mínimo, modificar solo el mensaje y formular la predicción individual. |
| 18–25 min | Realizar y comprobar la primera ejecución individual. |
| 25–33 min | Provocar un error simple, leer el diagnóstico, formular una hipótesis y corregir. |
| 33–40 min | Contrastar por parejas predicciones, recorrido y diagnósticos. |
| 40–45 min | Volver a ejecutar, explicar la evidencia y cerrar. |

## Comprobación y cierre

Pregunta:

> ¿Dónde está el código fuente, qué ocurrió antes de ver la consola, qué ejecutaste, qué salida esperabas y qué salida apareció?

Cierra en voz alta:

> Hoy no hemos aprendido solo a pulsar ejecutar. Hemos comprendido el recorrido entre escribir, compilar, ejecutar y observar. Cuando algo falla, primero leemos el diagnóstico, decidimos si apunta al código o a la configuración y formulamos una hipótesis.

## Límite respecto a S208

S207 introduce el programa mínimo, el recorrido hasta la consola y un primer error sencillo. S208 profundiza en clase, `main`, delimitadores, errores sintácticos, identificadores, comentarios y depuración inicial.

## Al terminar

Anota únicamente lo necesario para continuar: alumnado que no pudo ejecutar, problema de configuración pendiente, error común o ajuste temporal para la siguiente sesión.
