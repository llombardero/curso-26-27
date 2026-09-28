# S207 — Píldoras: del código a la consola

> Material de consulta de la sesión S207. El objetivo es distinguir qué escribes, qué comprueba Java y qué observas al ejecutar.

## 1. Código → compilación → ejecución → consola

El recorrido básico es:

1. **Código fuente:** escribes instrucciones en `Main.java`.
2. **Compilación:** Java comprueba y traduce el código.
3. **Ejecución:** el programa se pone en marcha.
4. **Consola:** ves los mensajes y escribes datos cuando el programa los pide.

El **proyecto** contiene `Main.java` y la configuración necesaria. El proyecto no es la consola ni una única línea de código.

### Ejemplo 1 — Recorrido correcto

Código fuente:

```java
public class Main {
    public static void main(String[] argumentos) {
        System.out.println("MiniJarvis arranca");
    }
}
```

Después de compilar y ejecutar, la consola muestra:

```text
MiniJarvis arranca
```

### Ejemplo 2 — El código cambia, la salida también

Si modificas solo el literal:

```java
System.out.println("MiniJarvis está preparado");
```

la nueva ejecución debe mostrar:

```text
MiniJarvis está preparado
```

Si la consola sigue mostrando el mensaje anterior, comprueba que has guardado y ejecutado el archivo correcto.

### Ejemplo 3 — Error de código

```java
System.out.println("Hola")
```

Falta `;`. La compilación falla antes de que el programa pueda ejecutarse. La consola no puede mostrar la salida prevista.

### Ejemplo 4 — Error de entorno

El código puede estar bien y, aun así, no ejecutarse porque el JDK no está configurado o se ha seleccionado otra clase de inicio. En ese caso no debes reescribir todo el programa: lee el mensaje y comprueba la configuración.

## 2. Escribir, compilar y ejecutar no significan lo mismo

- **Escribir:** crear o modificar el código fuente.
- **Compilar:** comprobar y traducir ese código.
- **Ejecutar:** poner en marcha el programa ya preparado.

### Ejemplo 1 — Escribir sin ejecutar

Cambias `"Hola"` por `"Buenos días"`, pero no pulsas ejecutar. Has escrito código, pero todavía no has comprobado su comportamiento.

### Ejemplo 2 — Compilar sin comportamiento correcto

```java
System.out.println("Adiós");
```

Puede compilar correctamente, pero sería incorrecto si el requisito era mostrar un saludo inicial. Compilar no demuestra que el programa resuelva el reto.

### Ejemplo 3 — Ejecutar y comprobar

Predicción: «La consola mostrará dos líneas».

```java
System.out.println("Hola");
System.out.println("Soy MiniJarvis");
```

Ejecución observada:

```text
Hola
Soy MiniJarvis
```

La comparación entre predicción y salida es una prueba sencilla.

## Errores frecuentes

- Llamar «programa» a la ventana de consola.
- Pulsar ejecutar muchas veces sin leer el primer error.
- Cambiar varias cosas a la vez y no saber qué corrección funcionó.
- Guardar una captura sin indicar qué código produjo esa salida.

## Comprueba que lo entiendes

1. Señala dónde está el código fuente en tu proyecto.
2. Explica qué ocurre antes de que aparezca un mensaje en la consola.
3. Da un ejemplo de error de código y otro de configuración.
4. Completa: «Sé que se ha ejecutado porque…».
