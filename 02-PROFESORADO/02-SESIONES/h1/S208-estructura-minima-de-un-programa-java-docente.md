# S208 - Investigar - Estructura mínima de un programa Java

| Dato | Valor |
|---|---|
| Hito | H1 — Primer asistente ejecutable |
| Duración prevista | 45 minutos |
| Fase HEXA del hito | Investigar — aprender lo necesario |

> Basada en `00-GUION-DOCENTE-H1-COMPLETO.md`. Selecciona y desarrolla los conceptos, ejemplos, actividades y evidencias útiles para esta sesión.

## Qué vas a aprender

Al terminar, debes reconstruir y depurar la estructura mínima de Java: clase, `main`, llaves, paréntesis, comillas, punto y coma, identificadores y comentarios.

## Ideas y ejemplos

Usa esta explicación como una secuencia breve de ejemplos. No la conviertas en teoría larga: proyecta, pide predicción, corrige y haz que señalen el elemento exacto.

En estos primeros programas, el archivo se llama `Main.java`, la clase pública se llama `Main` y el método `main` es el punto de entrada. Java distingue mayúsculas y necesita delimitadores: punto y coma, llaves, paréntesis y comillas.

Ejemplo para proyectar:

```java
public class Main {
    public static void main(String[] argumentos) {
        System.out.println("Hola");
    }
}
```

Pregunta al alumnado:

Señala clase, punto de entrada, una instrucción visible, un identificador y un comentario útil.

Error frecuente que debes cortar:

`String` no es `string`. `Main` no es `main`. Las mayúsculas importan.

Contrasta ahora la relación archivo-clase con este caso:

```java
// Archivo: Main.java
public class MiniJarvis {
    public static void main(String[] argumentos) {
        System.out.println("Hola");
    }
}
```

Pregunta:

Qué relación no se cumple aquí.

Respuesta esperada:

```text
Main.java no coincide con public class MiniJarvis.
```

Aclara la diferencia entre `Main` y `main`:

```java
public class Main {
    public static void main(String[] argumentos) {
        System.out.println("MiniJarvis");
    }
}
```

Di:

`Main` es el nombre de la clase. `main` es el método donde comienza la ejecución.

Haz una predicción de orden:

```java
public class Main {
    public static void main(String[] argumentos) {
        System.out.println("UNO");
        System.out.println("DOS");
    }
}
```

Pregunta:

Aparecerá primero UNO o DOS. Explica por qué.

Trabaja errores de escritura sin ejecutar primero:

```java
public static void main(string[] argumentos) {
    System.out.println("Hola");
}
```

```java
System.out.println("Hola")
System.out.println("MiniJarvis");
```

```java
System.out.println("Hola);
```

```java
System.out.println("Hola";
```

```java
public class Main {
    public static void main(String[] argumentos) {
        System.out.println("Hola");
}
```

Localiza el error, di qué delimitador o escritura falla y predice si compila.

Después clasifica nombres. Proyecta solo los nombres, no el código completo:

```text
nombreUsuario       válido y claro
horasEstudio     válido y claro
nombreAsistente  válido y claro
x              válido pero pobre
a              válido pero pobre
dato           válido pero pobre
cosa           válido pero pobre
1nombre        no válido
nombre1        válido
horas estudio  no válido
horasEstudio     válido
class          no válido
public         no válido
nombreClase      válido
```

Pregunta:

Sin ver el resto del programa, qué esperas que almacene cada nombre. Si nadie puede responder, probablemente el nombre sea mejorable.

Termina con comentarios útiles. Contrasta:

```java
// Muestra Hola
System.out.println("Hola");
```

```java
// Primer mensaje que identifica al asistente
System.out.println("Hola, soy MiniJarvis");
```

```java
// Declara horasEstudio
int horasEstudio = 4;

// Valor inicial usado en la demostración
int horasPractica = 4;
```

```java
/*
 * Primera versión de MiniJarvis.
 * De momento solo muestra mensajes por consola.
 */
```

Di:

Un comentario útil explica intención o contexto. Un comentario pobre repite lo que ya se lee en la instrucción.

## Actividad de la sesión

Reconstruid la estructura mínima sin copiar directamente. Añadid dos mensajes y un comentario útil. Luego introducid un error pequeño, leed el diagnóstico, corregidlo y ejecutad.

**Recuerda:**

Un comentario útil no repite lo obvio. No escribimos `// imprime hola` encima de `println("Hola")`. Escribimos contexto o intención.

## Evidencia de la sesión

Antes de terminar, cada persona debe conservar una evidencia de estructura mínima funcionando y una nota del error que ha provocado y corregido.

**Dónde y cómo conservar la evidencia:**

- GitHub: código actualizado o ejercicio de estructura.
- Diario individual: fila S208 con error provocado, hipótesis, corrección y resultado.
- Moodle: no se entrega todavía.

**Qué debe contener la evidencia:**

- Código con estructura mínima.
- Salida observada.
- Explicación de una regla sintáctica.

Modelo de uso de evidencia S208:

```text
Archivo: practicas-h1/S208-estructura-minima.java
Prueba: estructura mínima ejecutada con dos mensajes.
Error provocado: escribí string en lugar de String.
Hipótesis: Java distingue mayúsculas.
Corrección: cambié string por String.
Resultado: compila y muestra los mensajes esperados.
```

## Comprueba lo aprendido

Para cerrar S208, cada persona debe poder señalar dónde empieza la ejecución, qué instrucción muestra texto y una regla cuya ruptura impide compilar.
