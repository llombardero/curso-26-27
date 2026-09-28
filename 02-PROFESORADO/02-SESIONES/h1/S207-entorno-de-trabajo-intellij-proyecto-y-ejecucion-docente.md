# S207 - Investigar - Entorno Java, IntelliJ, proyecto y ejecución

| Dato | Valor |
|---|---|
| Hito | H1 — Primer asistente ejecutable |
| Duración prevista | 45 minutos |
| Fase HEXA del hito | Investigar — aprender lo necesario |

> Basada en `00-GUION-DOCENTE-H1-COMPLETO.md`. Selecciona y desarrolla los conceptos, ejemplos, actividades y evidencias útiles para esta sesión.

## Qué vas a aprender

Al terminar, debes comprender el camino `código fuente -> compilación -> ejecución -> consola` y lograr una primera ejecución.

## Ideas y ejemplos

Úsala antes de la primera ejecución y repítela cuando aparezca el primer error.

El recorrido básico es código fuente, compilación, ejecución y consola. Escribir es modificar `Main.java`. Compilar es comprobar y traducir. Ejecutar es poner en marcha. La consola es donde observamos el resultado.

Ejemplo para proyectar:

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

Pregunta al alumnado:

Señala dónde está el código fuente, qué ocurre antes de la consola y cómo sabes que se ha ejecutado.

Error frecuente que debes cortar:

No reescribas todo si falla. Lee el primer error y decide si es código o configuración.

El **JDK** aporta las herramientas necesarias para compilar y ejecutar Java. IntelliJ es el entorno de trabajo: organiza el proyecto, usa el JDK configurado y permite lanzar el programa. Si el JDK no está asociado al proyecto, el código puede ser correcto y aun así no ejecutarse.

## Actividad de la sesión

Escribid un mensaje distinto al ejemplo. Antes de ejecutar, escribid qué esperáis ver. Luego ejecutad y comparad.

Después pide:

Ahora romped algo a propósito: quitad un punto y coma o una comilla. Antes de corregir, leed el error. No borréis todo. Localizad el primer lugar donde el IDE os da información.

## Evidencia de la sesión

Guardad una evidencia de primera ejecución. Debe verse o quedar localizable el código y la salida. Añadid una frase: `Sé que se ha ejecutado porque...`.

**Dónde y cómo conservar la evidencia:**

- GitHub o espacio de trabajo acordado: código del primer `Main.java`.
- Drive si se usa captura puntual: captura con código y consola, no solo consola.
- Diario individual: enlace a la evidencia y frase explicativa.
- Moodle: no se entrega todavía; se enlazará al final de H1.

Modelo de uso de GitHub/evidencia en S207:

```text
Repositorio: minijarvis-h1
Archivo: src/Main.java
Commit útil: S207: primera ejecución por consola
Evidencia: código con System.out.println y salida visible en consola.
Frase de diario: Sé que se ha ejecutado porque la consola muestra el mensaje que predije.
```

Modelo de commit poco útil:

```text
cambios
```

Qué no aceptar:

- Captura solo de consola sin código.
- Frase `funciona` sin explicación.

## Comprueba lo aprendido

Hoy no hemos aprendido solo a pulsar ejecutar. Hemos aprendido el recorrido: escribir, compilar, ejecutar y observar. Si algo falla, primero leemos el error y formulamos una hipótesis.
