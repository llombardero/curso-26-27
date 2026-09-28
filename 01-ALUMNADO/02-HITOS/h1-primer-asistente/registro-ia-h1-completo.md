# Uso de IA en H1 — registro completado (Ana García)

> No mantengas un archivo de IA paralelo. Registra el uso personal en el **Diario individual** y el uso colectivo en el **Sheet Scrum**.

## Campos mínimos que ya existen en esas hojas

- herramienta o `No`;
- objetivo o prompt resumido;
- salida relevante;
- cambio realizado;
- validación o prueba;
- decisión de aceptar, modificar o descartar.

## Registro detallado de uso de IA en H1

### S207 — Primera ejecución

- **Herramienta:** ChatGPT (IA generativa)
- **Objetivo:** Entender la estructura mínima de un programa Java que imprime por consola.
- **Prompt:** "¿Cuál es la estructura mínima de un programa Java que imprime 'Hola Mundo'?"
- **Salida relevante:** El modelo devolvió:
  ```java
  public class Main {
      public static void main(String[] argumentos) {
          System.out.println("Hola Mundo");
      }
  }
  ```
- **Cambio realizado:** Copié la estructura y la adapté a MiniJarvis, cambiando `"Hola Mundo"` por `"Hola, " + nombre`.
- **Validación o prueba:** Compilé y ejecuté. El programa funcionó correctamente.
- **Decisión:** Acepté la estructura tal cual porque coincide con lo explicado en clase (S208).

### S210 — Variables y tipos

- **Herramienta:** ChatGPT (IA generativa)
- **Objetivo:** Entender la diferencia entre `static final` y `final` sin `static`.
- **Prompt:** "¿Cuál es la diferencia entre static final y final en Java?"
- **Salida relevante:** El modelo explicó que `static` significa que la variable pertenece a la clase (no a una instancia), y `final` significa que no se puede reasignar. Combinados, crean constantes de clase.
- **Cambio realizado:** Añadí un comentario a mi código explicando la diferencia.
- **Validación o prueba:** Verifiqué con el temario del Tema 1 y la explicación del profesor. Coincide.
- **Decisión:** Acepté la explicación y la usé para justificar mi elección de `final String` (sin `static`) porque la constante solo se usa dentro de `main`.

### S212 — Scanner y conversión

- **Herramienta:** ChatGPT (IA generativa)
- **Objetivo:** Entender por qué `Integer.parseInt()` lanza excepción con entrada no numérica.
- **Prompt:** "¿Por qué Integer.parseInt('abc') lanza NumberFormatException?"
- **Salida relevante:** El modelo explicó que `parseInt()` intenta convertir la cadena a un número entero. Si la cadena no contiene dígitos válidos, no puede hacer la conversión y lanza `NumberFormatException`.
- **Cambio realizado:** Añadí una nota en el README explicando este comportamiento como limitación de H1.
- **Validación o prueba:** Probé con la entrada `"abc"` y confirmé que se lanza la excepción.
- **Decisión:** Acepté la explicación. No implementé `try/catch` porque queda fuera del alcance de H1.

### S213 — Comparaciones y if/else

- **Herramienta:** No (trabajo independiente)
- **Objetivo:** Implementar la lógica `if/else` para decidir la salida según si el número es positivo.
- **Resultado:** Escribí el código sin ayuda de IA, basándome en los ejemplos de clase y el temario.
- **Decisión:** No usé IA en esta sesión porque me sentía cómodo con los conceptos.

## Defensa

Debes poder indicar qué parte es tuya, qué cambió tras la ayuda y cómo comprobaste que la respuesta era correcta.

- **Parte propia:** Todo el código de `Main.java` es mío. Las decisiones de diseño (nombres de variables, estructura del flujo, lógica `if/else`) son mías.
- **Cambio tras ayuda de IA:** La estructura base del programa (S207) y la explicación de `static final` vs `final` (S210) vinieron de IA. Las validé con el temario y la clase.
- **Validación:** En cada caso, probé el código o verifiqué con el material de clase antes de aceptarlo.
