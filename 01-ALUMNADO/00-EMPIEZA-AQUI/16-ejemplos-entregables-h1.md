# Ejemplos de entregables H1

## Para qué sirve este documento

Este documento muestra ejemplos de cómo pueden quedar los entregables de H1.

No copies los ejemplos literalmente. Úsalos como modelo de claridad, profundidad y formato. Tus entregables deben hablar de tu equipo, tu código, tus pruebas y tus evidencias reales.

Regla principal:

> Una evidencia útil permite comprobar algo concreto: qué se probó, con qué entrada, qué salida se esperaba, qué salida apareció y dónde está el enlace exacto.

## 1. Ejemplo de diario individual

Dónde se hace:

- Sheet de diario individual.

Cuándo se usa en H1:

- Al final de una sesión con avance, prueba, bloqueo, decisión o uso de IA.

Ejemplo de fila:

```text
Fecha: 2026-10-02
Sesión: S212
Hito: H1
Objetivo: leer un nombre ficticio con Scanner y usarlo en la salida.
Acción realizada: añadí Scanner, pedí un nombre, guardé nextLine() en nombreUsuario y lo usé en un saludo.
Prueba y resultado: ejecuté con el nombre ficticio Laura y la consola mostró "Hola, Laura.".
Evidencia enlazada: enlace al commit o captura concreta donde se ve código y consola.
Bloqueo: al principio leía el nombre, pero seguía mostrando un saludo fijo.
Uso de IA: no.
Siguiente paso: leer horas como texto y convertirlas con parseInt.
```

Ejemplo demasiado pobre:

```text
Hoy hice Scanner. Funciona.
```

Por qué no sirve:

- No dice qué se probó.
- No indica entrada ni salida.
- No enlaza una evidencia concreta.
- No permite defender el aprendizaje.

## 2. Ejemplo de Scrum de equipo

Dónde se hace:

- Sheet Scrum del equipo.

Cuándo se usa en H1:

- Durante todo el hito: backlog, tareas, decisiones, bloqueos, review y retrospectiva.

Ejemplo de backlog y tareas:

```text
Equipo: Ada
Hito: H1 - Primer MiniJarvis

Tarea: Definir qué entra y qué queda fuera de H1
Responsable: equipo completo
Estado: hecho
Evidencia: decisión S206 en Scrum

Tarea: Implementar saludo inicial
Responsable: Nora
Estado: hecho
Evidencia: commit S209-salida-clara

Tarea: Leer nombre ficticio con Scanner
Responsable: Luis y Marta
Estado: hecho
Evidencia: README, apartado ejemplo de ejecución

Tarea: Probar dos ramas del if/else
Responsable: Amira
Estado: en curso
Bloqueo: solo está probado el caso true
Siguiente paso: ejecutar con horas = 2 y registrar salida

Decisión S209:
Usaremos mensajes breves y claros. No diremos que MiniJarvis recuerda conversaciones porque H1 no tiene memoria.

Review H1:
El programa ejecuta, saluda, pide nombre ficticio, calcula minutos y muestra si el objetivo se alcanza.

Retrospectiva H1:
Funcionó revisar por parejas antes de entregar. Debemos actualizar Scrum durante la sesión y no solo al final.
```

Ejemplo demasiado pobre:

```text
Tarea: hacer Java
Responsable: todos
Estado: bien
```

Por qué no sirve:

- No se puede comprobar.
- No tiene evidencia enlazada.
- No permite saber qué falta.

## 3. Ejemplo de repositorio GitHub

Dónde se entrega:

- En GitHub.
- En Moodle se pega el enlace al repositorio o al archivo concreto que se pida.

Estructura suficiente para H1:

```text
minijarvis-h1/
├── README.md
├── src/
│   └── Main.java
└── practicas-h1/
    ├── S208-estructura-minima.java
    ├── S211-operaciones.java
    └── S213-if-else.java
```

Ejemplo de `Main.java` para H1:

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] argumentos) {
        final String NOMBRE_ASISTENTE = "MiniJarvis";
        final int HORAS_MINIMAS = 4;

        Scanner teclado = new Scanner(System.in);

        System.out.println("Hola, soy " + NOMBRE_ASISTENTE + ".");
        System.out.print("Escribe un nombre ficticio: ");
        String nombreUsuario = teclado.nextLine();

        System.out.print("Horas de estudio de hoy: ");
        String textoHoras = teclado.nextLine();
        int horasEstudio = Integer.parseInt(textoHoras);
        int minutosEstudio = horasEstudio * 60;

        System.out.println("Encantado, " + nombreUsuario + ".");
        System.out.println("Minutos de estudio: " + minutosEstudio);

        if (horasEstudio >= HORAS_MINIMAS) {
            System.out.println("Objetivo alcanzado.");
        } else {
            System.out.println("Objetivo pendiente.");
        }

        teclado.close();
    }
}
```

Ejemplo de commit útil:

```text
S212: leer nombre ficticio con Scanner
```

Ejemplo de commit poco útil:

```text
cambios
```

## 4. Ejemplo de README H1

Dónde se entrega:

- Archivo `README.md` en la raíz del repositorio.
- En Moodle se pega el enlace al repositorio o al README.

Ejemplo:

````markdown
# MiniJarvis H1

## Qué hace

MiniJarvis H1 es un programa Java de consola. Muestra un saludo, pide un nombre ficticio, pide horas de estudio, calcula minutos y muestra si se alcanza un objetivo mínimo.

## Límites de H1

Esta versión no tiene menú, bucle principal, memoria, ficheros, clases propias complejas ni conexión con una IA real.

## Cómo ejecutar

1. Abrir el proyecto en IntelliJ.
2. Abrir `src/Main.java`.
3. Ejecutar el método `main`.
4. Escribir datos ficticios cuando la consola los pida.

## Ejemplo de ejecución

Entrada usada:

```text
Laura
5
```

Salida esperada:

```text
Hola, soy MiniJarvis.
Escribe un nombre ficticio: Laura
Horas de estudio de hoy: 5
Encantado, Laura.
Minutos de estudio: 300
Objetivo alcanzado.
```

## Pruebas realizadas

Caso A:

- Entrada: Laura, 5
- Resultado esperado: Objetivo alcanzado.
- Resultado obtenido: Objetivo alcanzado.
- Qué demuestra: la rama true del if funciona.

Caso B:

- Entrada: Sam, 2
- Resultado esperado: Objetivo pendiente.
- Resultado obtenido: Objetivo pendiente.
- Qué demuestra: la rama false del if funciona.

Entrada no convertible:

- Entrada en horas: hola
- Resultado: el programa falla durante la ejecución al aplicar `Integer.parseInt`.
- Qué demuestra: `nextLine()` devuelve texto y no todo texto se puede convertir a entero.

## Evidencias

- Enlace al commit final.
- Enlace a captura o registro de ejecución.
- Enlace al Scrum del equipo.

## Uso de IA

No se ha usado IA.

## Qué sabemos defender

- Dónde empieza la ejecución.
- Qué variables y constantes se usan.
- Qué hace Scanner.
- Por qué usamos parseInt.
- Qué condición controla el if/else.
````

## 5. Ejemplo de Site personal H1

Dónde se entrega:

- Página H1 del Site personal.
- En Moodle se pega el enlace profundo a esa página.

Ejemplo de contenido:

```text
Título: H1 - Primer MiniJarvis

Reto con mis palabras:
En H1 hemos construido una primera versión pequeña de MiniJarvis por consola. El objetivo era entender la base de Java y poder demostrarla con código ejecutable.

Mi aportación individual:
Me encargué de probar la entrada por teclado con Scanner y de registrar una prueba con entrada válida y otra no convertible.

Decisión justificada:
Usé el nombre `nombreUsuario` en lugar de `x` porque permite entender que la variable guarda un nombre ficticio.

Dificultad o cambio:
Al principio pensaba que si escribía `5` en consola Java ya lo trataba como número. Después entendí que `nextLine()` devuelve texto y que necesitaba `Integer.parseInt`.

Evidencia seleccionada:
Enlace profundo a la prueba de S212.

Qué demuestra:
Demuestra que sé explicar el flujo pedir -> leer -> guardar -> convertir -> calcular -> mostrar.

Uso de IA:
No usé IA en esta parte.

Mejora para H2:
Necesito probar mejor entradas no válidas y aprender a mantener el programa en ejecución con un menú.
```

Ejemplo demasiado pobre:

```text
Hice MiniJarvis y aprendí Java.
```

Por qué no sirve:

- No selecciona una evidencia.
- No explica qué demuestra.
- No diferencia aportación individual y trabajo del equipo.

## 6. Ejemplo de Site de equipo H1

Dónde se entrega:

- Página H1 del Site de equipo.
- En Moodle se pega el enlace profundo a esa página.

Ejemplo de contenido:

```text
Título: Equipo Ada - H1 Primer MiniJarvis

Reto H1:
Crear una primera versión ejecutable de MiniJarvis en Java, pequeña, clara y defendible.

Incremento conseguido:
Nuestro MiniJarvis saluda, pide un nombre ficticio, pide horas de estudio, calcula minutos y muestra si el objetivo mínimo se alcanza.

Decisiones principales:
No incluimos menú ni memoria porque pertenecen a H2 o hitos posteriores.
Usamos mensajes sencillos para no prometer funciones inexistentes.
Guardamos microprácticas separadas cuando no formaban parte del Main final.

Pruebas realizadas:
Prueba de saludo con nombre ficticio.
Prueba de cálculo de minutos.
Prueba de horas = 5.
Prueba de horas = 2.
Prueba de entrada no convertible.

Enlaces:
Repositorio GitHub: https://...
README H1: https://...
Scrum H1: https://...

Review:
El incremento cumple el alcance que definimos en S206.

Retrospectiva:
Funcionó bien revisar por parejas antes de entregar.
Debemos mejorar la actualización diaria de Scrum.
En H2 queremos probar antes de añadir más comandos.
```

## 7. Ejemplo de entrega Moodle H1

Dónde se entrega:

- Tarea Moodle de H1.

Cuándo se entrega:

- Al cierre de H1, en S215 o en el plazo indicado por el profesor.

Ejemplo de texto para Moodle:

```text
Equipo: Ada
Integrantes: Nora, Luis, Marta, Amira

Repositorio GitHub:
https://github.com/...

README H1:
https://github.com/.../README.md

Site personal H1 - Nora:
https://sites.google.com/...

Site personal H1 - Luis:
https://sites.google.com/...

Site personal H1 - Marta:
https://sites.google.com/...

Site personal H1 - Amira:
https://sites.google.com/...

Site de equipo H1:
https://sites.google.com/...

Scrum de equipo H1:
https://docs.google.com/spreadsheets/...

Evidencia concreta de ejecución:
https://...

Permisos comprobados: sí

Observaciones:
La entrada no convertible está documentada como error de ejecución. Todavía no usamos try-catch porque no pertenece a H1.
```

Ejemplo que no sirve:

```text
Está todo en Drive.
```

Por qué no sirve:

- No hay enlaces profundos.
- No indica qué debe revisar el profesor.
- No confirma permisos.
- No funciona como entrega oficial completa.

## Lista final antes de entregar H1

Antes de entregar en Moodle, revisa:

- El repositorio abre correctamente.
- El README está en la raíz del repositorio.
- El código ejecuta con datos ficticios.
- Hay evidencia de entrada y salida.
- Hay prueba de las dos ramas del `if/else`.
- El diario individual tiene entradas útiles.
- El Scrum de equipo tiene tareas, decisiones, review y retrospectiva.
- El Site personal selecciona evidencia individual.
- El Site de equipo comunica el incremento.
- Moodle contiene enlaces profundos, no carpetas generales.
- Los permisos están comprobados.
- No hay datos personales reales, contraseñas, claves ni tokens.
