# S206 - Activar - Presentar H1 y delimitar alcance

| Dato | Valor |
|---|---|
| Hito | H1 — Primer asistente ejecutable |
| Duración prevista | 45 minutos |
| Fase HEXA del hito | Activar — entender el reto |

> Basada en `00-GUION-DOCENTE-H1-COMPLETO.md`. Selecciona y desarrolla los conceptos, ejemplos, actividades y evidencias útiles para esta sesión.

## Qué vas a aprender

Al terminar, debes entender qué es H1, qué entra, qué no entra y cómo se demostrará el avance.

## Ideas y ejemplos

Úsala ahora, antes de que clasifiquen qué entra y qué queda fuera.

Un primer programa debe ser correcto, eficiente y mantenible. Correcto significa que hace lo pedido y podemos comprobarlo. Eficiente, en H1, no significa que vaya rapidísimo: significa que no añade complejidad innecesaria. Mantenible significa que se entiende y se puede modificar sin romperlo fácilmente.

Ejemplo para proyectar:

```java
final String NOMBRE_ASISTENTE = "MiniJarvis";
String nombreUsuario = "Laura";
System.out.println("Hola, soy " + NOMBRE_ASISTENTE + ".");
System.out.println("Encantado, " + nombreUsuario + ".");
```

Pregunta al alumnado:

Qué requisito demuestra cada línea visible, qué parte quitarías si no pertenece a H1 y qué nombre ayuda a entender el código.

Error frecuente que debes cortar:

Compilar no basta para decir que es correcto. Falta comprobar comportamiento.

## Actividad de la sesión

Clasificad estas ideas en tres columnas: entra en H1, más adelante, fuera del reto. Usad criterio, no gusto personal.

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

## Evidencia de la sesión

Conserva una decisión de alcance fechada como S206 que incluya:

- una frase que explique qué es H1;
- una lista breve de lo que entra;
- una lista breve de lo que queda fuera;
- una justificación de al menos una exclusión;
- una reflexión individual con el siguiente paso.

Modelo breve:

```text
H1 es una primera versión de MiniJarvis en consola que permite practicar fundamentos de Java.
Entra: saludo, entrada/salida, variables, constantes, una operación y una decisión sencilla.
Queda fuera: menú, memoria, ficheros e IA real.
Siguiente paso: crear y ejecutar Main.java.
```
## Comprueba lo aprendido

Cerramos Activar. Para avanzar, cada equipo debe poder explicar qué va a construir y qué no va a construir. Mañana o en la siguiente sesión investigaremos cómo se pasa de escribir código a verlo ejecutarse en consola.
