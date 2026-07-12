# H1 — Primer asistente por consola

Equipo o alumno/a: Laura García Martín  
Curso: 1.º DAW  
Módulos: Programación + Entornos de Desarrollo  
Fecha: ejemplo docente

---

## 1. Qué hace este programa

Esta primera versión de MiniJarvis es un programa Java muy sencillo que se ejecuta por consola.

El programa:

- muestra un saludo inicial;
- pide el nombre de la persona usuaria;
- guarda ese nombre en una variable `String`;
- usa constantes para el nombre del asistente y el año del curso;
- muestra varios mensajes relacionados con el proyecto MiniJarvis.

Texto:

```text
MiniJarvis H1 sirve para comprobar que entiendo la estructura básica de un programa Java antes de añadir menú, bucles, memoria o IA real.
```

---

## 2. Qué NO incluye todavía

```text
[x] No tiene menú.
[x] No tiene bucles.
[x] No tiene switch.
[x] No tiene memoria.
[x] No tiene listas ni mapas.
[x] No tiene clases propias adicionales.
[x] No se conecta con una IA real.
```

Explicación:

```text
No incluye esas funciones porque H1 se centra en estructura básica, variables, constantes, entrada por teclado y salida por pantalla. El menú y los bucles se trabajarán en H2; la memoria en H3; las clases propias en H4; y la IA real o simulada más adelante.
```

---

## 3. Cómo ejecutar desde IntelliJ

1. Abrir el proyecto en IntelliJ.
2. Comprobar que el SDK de Java está configurado.
3. Abrir el archivo:

```text
src/Main.java
```

4. Pulsar Run.

Indicación específica:

```text
La clase principal se llama Main y está en src/Main.java.
```

---

## 4. Cómo ejecutar desde terminal, si procede

```bash
javac src/Main.java
java -cp src Main
```

---

## 5. Ejemplo de ejecución

```text
Hola, soy MiniJarvis.
¿Cómo te llamas? Laura
Encantada, Laura.
Este curso vamos a crear un pequeño agente IA.
Curso de inicio: 2026.
Primer objetivo: aprender la estructura básica de un programa Java.
```

---

## 6. Estructura del proyecto

```text
h1-primer-asistente/
├── README.md
├── src/
│   └── Main.java
└── docs/
    ├── evidencia-ejecucion-h1.md
    ├── portfolio-h1.md
    ├── registro-ia.md
    ├── defensa-h1.md
    ├── incidencia-h1.md
    └── vocabulario-h1.md
```

---

## 7. Conceptos usados

| Concepto | Dónde aparece en mi código |
|---|---|
| Clase `Main` | `public class Main` |
| Método `main` | `public static void main(String[] args)` |
| Variable para el nombre | `String userName = scanner.nextLine();` |
| Constante | `ASSISTANT_NAME` y `COURSE_YEAR` |
| `Scanner` | `Scanner scanner = new Scanner(System.in);` |
| `System.out.print` o `println` | En los mensajes de consola. |

---

## 8. Uso de IA

He usado IA:

```text
Sí
```

El registro está en:

```text
docs/registro-ia.md
```

Resumen breve:

```text
He usado IA para entender qué significa final en Java y cuándo conviene usar una constante. No he usado IA para generar el programa completo.
```

---

## 9. Qué sé defender

```text
[x] Dónde empieza el programa.
[x] Qué variable guarda el nombre.
[x] Qué constante he usado.
[x] Qué hace Scanner.
[x] Diferencia entre print y println.
[x] Cómo ejecuto el programa.
[x] Por qué todavía no hay menú.
```

Comentarios:

```text
Puedo explicar cada línea principal del programa y justificar por qué H1 debe mantenerse simple.
```

<!-- AJUSTE-COBERTURA-CONCEPTOS-32 -->

## Respuesta de Laura — cobertura de conceptos de Programación

Relación con `32-lista-conceptos-programacion-por-tema.md`:

```text
H1 trabaja principalmente: Tema 1.
Foco de aprendizaje: primer programa Java por consola y asistente mínimo.
```

Conceptos que Laura debe saber defender en este hito:

- programa
- instrucción
- sintaxis
- comentarios
- variable
- tipo de dato
- literal
- String
- Scanner
- entrada/salida
- operadores
- expresiones
- conversiones básicas

Respuesta modelo de Laura:

> En H1 defiendo que mi MiniJarvis todavía es sencillo, pero ya usa variables, tipos, salida por consola, entrada de usuario y nombres legibles.

Evidencia que Laura debe señalar:

- una parte concreta del código o documento donde aparezca el concepto;
- una prueba, ejecución, captura o explicación que demuestre que no lo ha copiado sin entender;
- una mejora razonable que podría hacer si tuviera más tiempo.

