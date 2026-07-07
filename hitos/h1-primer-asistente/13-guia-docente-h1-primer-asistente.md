# Guía docente — H1 Primer asistente básico

## Programación + Entornos de Desarrollo — 1.º DAW — Curso 2026/2027

Versión: borrador 0.1

Documento para uso del profesorado.

Documentos relacionados:

- `../../02-calendario-hitos-sprints-2026-2027.md`
- `../../04A-enunciados-y-entregables-alumnado.md`
- `../../06-rubricas-hitos.md`
- `../../07-plantillas-entregables.md`
- `13B-ficha-alumnado-h1-primer-asistente.md`
- `13C-checklist-correccion-h1.md`
- `../../99-ejemplos-alumna/h1-primer-asistente/`

---

## 1. Propósito del hito

H1 es el primer hito técnico del proyecto MiniJarvis.

El alumnado debe crear una primera versión muy sencilla de un asistente por consola en Java.

Este hito no busca complejidad. Busca base sólida.

Producto esperado:

```text
MiniJarvis H1: programa Java básico que pide el nombre de la persona usuaria y muestra varios mensajes iniciales.
```

El hito debe servir para comprobar que el alumnado empieza a comprender:

- estructura mínima de un programa Java;
- método `main`;
- variables;
- constantes;
- entrada por teclado;
- salida por pantalla;
- ejecución en IntelliJ;
- README básico;
- defensa oral sencilla.

---

## 2. Restricciones didácticas

Estas restricciones son importantes para mantener el hito en el nivel adecuado.

En H1 NO debe incluirse:

- menú;
- bucles;
- `switch`;
- listas o mapas;
- clases propias adicionales;
- herencia;
- interfaces;
- ficheros;
- excepciones complejas;
- conexión con Gemini, Jarvis u otra IA real;
- arquitectura avanzada;
- patrones de diseño.

Motivo:

```text
H1 debe demostrar comprensión de la estructura básica de un programa Java antes de añadir estructuras de control, memoria, orientación a objetos o integración IA.
```

Si un equipo trae algo más avanzado, no debe premiarse automáticamente. Debe comprobarse si:

- corresponde al hito;
- lo pueden explicar;
- no oculta falta de comprensión básica;
- no procede de IA sin adaptación ni defensa.

---

## 3. Fechas y duración

Fechas orientativas:

```text
21 septiembre - 9 octubre 2026
```

Carga estimada según calendario:

```text
Programación: 24 periodos de 45 min
Entornos: 9 periodos de 45 min
```

La distribución exacta puede ajustarse según horario real y nivel del grupo.

---

## 4. RA/CE y evidencias

### Programación

RA principales:

- PR RA1: estructura de un programa informático y elementos del lenguaje.
- PR RA2 inicial: programas sencillos y primeros fundamentos vinculados a objetos/librerías.

Evidencias H1:

- `src/Main.java`;
- uso correcto de `main`;
- variable `String` para nombre;
- constante con `final`;
- uso básico de `Scanner`;
- mensajes por pantalla;
- defensa individual.

### Entornos de Desarrollo

RA principales:

- ED RA1: relación programa, sistema, código fuente, ejecutable, JVM y herramientas.
- ED RA2: uso inicial de IntelliJ y configuración del entorno.

Evidencias H1:

- proyecto creado y abierto en IntelliJ;
- ejecución desde IntelliJ;
- opcionalmente ejecución desde terminal;
- README con instrucciones;
- estructura mínima del repositorio;
- evidencia de ejecución.

---

## 5. Producto mínimo esperado

El programa debe:

1. Tener una clase `Main`.
2. Tener método `public static void main(String[] args)`.
3. Mostrar un saludo inicial.
4. Pedir el nombre de la persona usuaria.
5. Guardar el nombre en una variable.
6. Usar al menos una constante.
7. Mostrar varios mensajes relacionados con el proyecto MiniJarvis.
8. Ejecutarse en IntelliJ.
9. Tener un README básico.

Ejemplo de comportamiento esperado:

```text
Hola, soy MiniJarvis.
¿Cómo te llamas? Laura
Encantada, Laura.
Este curso vamos a crear un pequeño agente IA.
Curso de inicio: 2026.
Primer objetivo: aprender la estructura básica de un programa Java.
```

---

## 6. Código mínimo de referencia docente

Este código es referencia para calibrar el nivel. No debe entregarse como solución directa si se quiere que el alumnado lo construya paso a paso.

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

Puntos que debe poder defender el alumnado:

- qué hace `import java.util.Scanner`;
- dónde empieza el programa;
- qué es una constante;
- qué es una variable;
- qué hace `scanner.nextLine()`;
- para qué sirve `System.out.println`;
- por qué todavía no hay menú ni bucles.

---

## 7. Secuencia didáctica sugerida

### Vista global

| Sesión / bloque | Foco | Producto parcial |
|---|---|---|
| 1 | Presentar H1 y analizar ejemplo de salida | Idea clara del producto mínimo. |
| 2 | Crear proyecto en IntelliJ y clase `Main` | Proyecto ejecutable con primer mensaje. |
| 3 | Variables, constantes y salida por pantalla | Mensajes con datos fijos y variables. |
| 4 | Entrada con `Scanner` | Nombre leído por teclado. |
| 5 | Limpieza, nombres claros y ejecución | Código H1 completo y simple. |
| 6 | README y evidencia de ejecución | Documentación mínima. |
| 7 | Revisión, defensa y recuperación | Validación individual. |

No es necesario que cada bloque sea una sesión completa. Puede redistribuirse según ritmo real.

---

## 8. Desarrollo docente paso a paso

### Bloque 1 — Presentar H1

Objetivo:

- Aterrizar el primer hito técnico.
- Dejar claro qué entra y qué no entra.

Mensaje docente:

```text
En H1 vamos a construir la primera versión mínima de MiniJarvis. Será muy sencilla. No tendrá menú, memoria ni IA real. Queremos entender bien la estructura básica de un programa Java.
```

Actividad breve:

Pedir al alumnado que responda:

```text
¿Qué debería hacer una primera versión mínima de un asistente?
¿Qué sería demasiado avanzado para esta primera versión?
```

Cierre:

Clasificar ideas en pizarra:

```text
H1 | Hitos posteriores | No adecuado
```

---

### Bloque 2 — Crear proyecto y primera ejecución

Objetivo:

- Crear proyecto Java en IntelliJ.
- Ejecutar un primer `Hola, soy MiniJarvis`.

Pasos docentes:

1. Crear proyecto Java.
2. Localizar carpeta `src`.
3. Crear `Main.java`.
4. Escribir estructura mínima.
5. Ejecutar.

Código inicial:

```java
public class Main {
    public static void main(String[] args) {
        System.out.println("Hola, soy MiniJarvis.");
    }
}
```

Preguntas de defensa inmediata:

```text
¿Dónde empieza el programa?
¿Qué línea muestra texto por pantalla?
¿Qué ocurre si cambia el texto entre comillas?
```

---

### Bloque 3 — Variables y constantes

Objetivo:

- Introducir `String`, `int` y `final`.
- Usar nombres claros.

Código progresivo:

```java
final String ASSISTANT_NAME = "MiniJarvis";
final int COURSE_YEAR = 2026;

System.out.println("Hola, soy " + ASSISTANT_NAME + ".");
System.out.println("Curso de inicio: " + COURSE_YEAR + ".");
```

Ideas clave:

- una variable guarda un dato;
- una constante guarda un dato que no debe cambiar;
- los nombres deben ayudar a entender el código;
- concatenar significa unir texto y valores.

Error frecuente:

```java
System.out.println("Hola, soy ASSISTANT_NAME.");
```

Explicación:

- dentro de las comillas se imprime texto literal;
- fuera de las comillas se usa el valor de la variable o constante.

---

### Bloque 4 — Entrada por teclado con Scanner

Objetivo:

- Leer el nombre de la persona usuaria.

Código:

```java
import java.util.Scanner;

Scanner scanner = new Scanner(System.in);
System.out.print("¿Cómo te llamas? ");
String userName = scanner.nextLine();
System.out.println("Encantada, " + userName + ".");
scanner.close();
```

Puntos a explicar:

- `Scanner` es una clase de la biblioteca de Java;
- `System.in` representa la entrada por teclado;
- `nextLine()` lee una línea completa;
- `System.out.print` no salta de línea;
- `System.out.println` sí salta de línea;
- `scanner.close()` cierra el recurso.

No profundizar todavía en excepciones ni gestión avanzada de entrada.

---

### Bloque 5 — Código limpio inicial

Objetivo:

- Revisar que el código es simple y defendible.

Criterios H1:

- nombres claros;
- programa corto;
- sin funciones prematuras;
- sin menú;
- sin bucles;
- sin código copiado que no se entiende;
- mensajes comprensibles.

Actividad:

Dar dos nombres y preguntar cuál es mejor:

| Nombre débil | Nombre mejor |
|---|---|
| `x` | `userName` |
| `cosa` | `assistantName` |
| `numero` | `courseYear` |

Mensaje docente:

```text
Código limpio en H1 no significa código avanzado. Significa código sencillo, claro y explicable.
```

---

### Bloque 6 — README y evidencia de ejecución

Objetivo:

- Documentar cómo ejecutar el proyecto.

README mínimo:

```markdown
# H1 — Primer asistente por consola

## Qué hace

Este programa muestra un saludo, pide el nombre del usuario y muestra mensajes iniciales del proyecto MiniJarvis.

## Cómo ejecutar

Desde IntelliJ:

1. Abrir el proyecto.
2. Abrir `src/Main.java`.
3. Pulsar Run.

## Ejemplo de ejecución

```text
Hola, soy MiniJarvis.
¿Cómo te llamas? Laura
Encantada, Laura.
```

## Qué no incluye todavía

No incluye menú, bucles, memoria ni IA real.
```

Evidencia de ejecución:

- captura;
- o bloque de salida copiado en README;
- o explicación validada en clase.

---

### Bloque 7 — Revisión y defensa

Objetivo:

- Comprobar comprensión individual.

Formato posible:

- defensa oral breve de 2-3 minutos;
- preguntas rápidas durante revisión;
- entrevista técnica por muestreo;
- checklist individual.

Preguntas esenciales:

```text
¿Dónde empieza el programa?
¿Qué variable guarda el nombre?
¿Qué constante has usado?
¿Qué hace Scanner?
¿Qué diferencia hay entre print y println?
¿Cómo ejecutas el proyecto en IntelliJ?
¿Por qué no hay menú todavía?
¿Has usado IA? ¿Para qué? ¿Cómo lo comprobaste?
```

---

## 9. Entregables H1

| Entregable | Responsable | Formato | Plantilla local |
|---|---|---|---|
| Código Java básico | Individual o equipo, según decisión docente | `src/Main.java` | No aplica. |
| README de ejecución | Equipo o individual | `README.md` | `plantillas/README-h1-template.md` |
| Evidencia de ejecución | Equipo o individual | `docs/evidencia-ejecucion-h1.md` | `plantillas/evidencia-ejecucion-h1-template.md` |
| Portfolio H1 | Individual | `docs/portfolio-h1.md` | `plantillas/portfolio-h1-template.md` |
| Registro de IA, si se usa | Individual | `docs/registro-ia.md` | `plantillas/registro-ia-h1-template.md` |
| Defensa H1 | Individual | `docs/defensa-h1.md` | `plantillas/defensa-h1-template.md` |
| Incidencia, si aparece | Individual/equipo | `docs/incidencia-h1.md` | `plantillas/incidencia-h1-template.md` |
| Vocabulario H1, si se pide | Individual | `docs/vocabulario-h1.md` | `plantillas/vocabulario-h1-template.md` |

Recomendación:

Si el trabajo se hace en equipo, mantener defensa individual obligatoria para evitar que una evidencia grupal oculte falta de comprensión.

Carpeta de plantillas específicas del hito:

```text
plantillas/
```

---

## 10. Uso de IA en H1

### Permitido en verde

- Pedir explicación de `Scanner`.
- Preguntar qué es una variable.
- Preguntar qué es una constante.
- Pedir un ejemplo mínimo y adaptarlo.
- Revisar la claridad del README.

### Permitido en amarillo

- Pedir ayuda para corregir un error de compilación.
- Pedir que explique un mensaje de error.
- Pedir sugerencias de nombres más claros.

Debe registrarse si afecta a la entrega.

### No permitido

- Generar el programa completo y entregarlo sin entender.
- Añadir menú, memoria o IA real porque lo sugirió una herramienta.
- Ocultar el uso de IA.
- Entregar código que no se puede defender.

Frase para el alumnado:

```text
Si una IA te da código que no puedes explicar, todavía no tienes una solución: tienes una tarea pendiente.
```

---

## 11. Errores previsibles y respuesta docente

| Error | Señal | Intervención docente |
|---|---|---|
| Falta `main` | El programa no ejecuta | Revisar estructura mínima de Java. |
| Clase con nombre distinto al archivo | Error de compilación | Explicar relación `Main.java` / `public class Main`. |
| Comillas mal cerradas | Error de compilación | Localizar línea y revisar literales. |
| Variable dentro de comillas | Imprime el nombre de la variable | Explicar texto literal vs valor de variable. |
| Olvida `import java.util.Scanner` | No reconoce Scanner | Explicar importación de biblioteca. |
| Usa `next()` y pierde apellidos | Solo lee primera palabra | Mostrar diferencia básica con `nextLine()`. |
| Añade menú o bucles | Hito se desborda | Reencuadrar: eso será H2. |
| Código demasiado avanzado | No puede explicarlo | Pedir versión mínima defendible. |
| README vacío | No se puede reproducir | Dar plantilla mínima. |

---

## 12. Checklist docente de corrección rápida

Usar junto con:

```text
13C-checklist-correccion-h1.md
```

Mínimos imprescindibles:

```text
[ ] Existe `src/Main.java`.
[ ] Compila o se ejecuta en IntelliJ.
[ ] Tiene clase `Main`.
[ ] Tiene método `main`.
[ ] Muestra mensajes por pantalla.
[ ] Pide el nombre al usuario.
[ ] Guarda el nombre en una variable.
[ ] Usa al menos una constante.
[ ] No introduce complejidad fuera de H1.
[ ] README explica cómo ejecutar.
[ ] El alumno/a puede defender lo básico.
```

---

## 13. Rúbrica H1 resumida

| Dimensión | Excelente | Adecuado | Básico | Insuficiente |
|---|---|---|---|---|
| Programa Java básico | Claro, ejecutable, con entrada/salida, variable y constante bien usadas. | Ejecutable con los elementos principales. | Incompleto o con errores menores. | No compila o no responde al hito. |
| Ajuste al nivel | Simple y sin complejidad prematura. | Alguna ampliación menor defendible. | Introduce código no trabajado con comprensión parcial. | Código avanzado no defendible. |
| IntelliJ y ejecución | Configura y ejecuta con autonomía. | Ejecuta con poca ayuda. | Necesita ayuda importante. | No puede ejecutarlo. |
| README | Explica qué hace y cómo ejecutar. | Suficiente. | Incompleto. | No útil o inexistente. |
| Defensa | Explica `main`, variable, constante, `Scanner` y ejecución. | Explica lo principal. | Dudas importantes. | No puede explicar el código. |

---

## 14. Atención a la diversidad

### Apoyos

- Plantilla inicial con huecos.
- Parejas de explicación.
- Ejemplo de salida antes del código.
- Lista de vocabulario: clase, método, variable, constante, entrada, salida.
- Ejecución guiada en IntelliJ.

### Ampliación sin romper H1

Si un alumno termina pronto, no añadir menú ni bucles.

Propuestas de ampliación permitidas:

- mejorar mensajes;
- añadir otra constante simple;
- mejorar README;
- preparar explicación de defensa;
- comparar `print` y `println`;
- explicar línea por línea el programa.

### Recuperación

Para alumnado con dificultades, pedir una versión mínima:

```text
Clase Main + main + saludo + variable nombre + una constante + ejecución.
```

La defensa puede hacerse con apoyo visual del propio código.

---

## 15. Criterio de éxito del hito

H1 habrá funcionado si la mayoría del alumnado puede decir y demostrar:

```text
Sé crear y ejecutar un programa Java básico.
Sé dónde empieza el programa.
Sé guardar un dato en una variable.
Sé usar una constante sencilla.
Sé pedir un dato por teclado.
Sé mostrar mensajes por pantalla.
Sé explicar por qué esta versión todavía no tiene menú ni IA real.
```

---

## 16. Preparación para H2

Antes de pasar a H2, comprobar:

- si el alumnado entiende `main`;
- si diferencia variable y constante;
- si puede ejecutar en IntelliJ;
- si sabe leer un error básico;
- si puede explicar `Scanner` a nivel inicial;
- si README y evidencia de ejecución están integrados.

H2 introducirá:

- menú;
- comandos;
- decisiones;
- bucles;
- entradas no válidas;
- depuración;
- pruebas manuales.

Mensaje de transición:

```text
H1 nos da una primera versión mínima. En H2 convertiremos esta primera versión en un agente con comandos y menú, pero solo cuando la base esté entendida.
```
