# S207 — Entorno de trabajo: IntelliJ, proyecto y ejecución

## Objetivo

Comprender el recorrido desde el código fuente hasta la salida en consola, crear un proyecto Java ejecutable en IntelliJ y obtener una evidencia que permita repetir la ejecución.

## 1. Del código a la consola

El recorrido básico es:

```text
código fuente → compilación → bytecode → JVM → ejecución → consola
```

- El **código fuente** es el contenido de los archivos `.java`.
- El **JDK** incluye las herramientas necesarias para compilar y ejecutar Java.
- La **compilación** comprueba la sintaxis y transforma el código en bytecode.
- La **JVM** ejecuta ese bytecode.
- IntelliJ es el entorno de desarrollo: ayuda a crear, editar y ejecutar el proyecto, pero no sustituye al JDK.
- La **consola** muestra la salida y permite escribir entradas durante la ejecución.

## 2. Programa mínimo ejecutable

Crea un proyecto Java y guarda este contenido en `Main.java`:

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

Predice la salida antes de ejecutar. Después, compárala con la salida real.

## 3. Qué debes localizar en IntelliJ

Comprueba que puedes señalar:

1. la carpeta del proyecto;
2. la carpeta `src`;
3. el archivo `Main.java`;
4. el JDK asociado al proyecto;
5. el botón o configuración de ejecución;
6. la consola donde aparece la salida.

## 4. Si el programa no se ejecuta

### El JDK no está configurado

IntelliJ puede mostrar el código, pero no podrá compilarlo. Revisa el SDK del proyecto y selecciona un JDK instalado.

### No se encuentra `main`

Comprueba que existe exactamente un punto de entrada válido:

```java
public static void main(String[] argumentos)
```

### El nombre del archivo y la clase no coinciden

Si la clase es `public class Main`, el archivo debe llamarse `Main.java`.

### Hay un error de código

Lee el primer mensaje de error, localiza la línea y distingue si falta una comilla, un paréntesis, una llave o un punto y coma.

## 5. Práctica de predicción, error y corrección

1. Ejecuta el programa correcto.
2. Cambia el mensaje y predice la nueva salida.
3. Provoca un error controlado, por ejemplo eliminando `;`.
4. Copia el mensaje esencial del error.
5. Corrige el código y vuelve a ejecutar.

No conserves el proyecto roto como entrega final: registra el error y su corrección en la evidencia.

## 6. Evidencia verificable

Una evidencia útil debe mostrar:

- el archivo y fragmento de código relevante;
- la consola con la salida esperada;
- una frase que explique qué se comprobó;
- un commit con un mensaje concreto.

Ejemplo de commit útil:

```text
S207: crear proyecto Java y verificar primera ejecución
```

Ejemplo poco útil:

```text
cambios
```

## Errores frecuentes

- Pensar que IntelliJ incluye siempre un JDK listo para usar.
- Confundir escribir código con ejecutarlo.
- Fotografiar solo la consola sin mostrar qué programa produjo la salida.
- Corregir varios errores a la vez sin leer el primero.
- Usar una clase `Main` dentro de un archivo con otro nombre.

## Autoevaluación

Comprueba que puedes:

- explicar la diferencia entre JDK, compilación, JVM e IntelliJ;
- localizar `Main.java` y el punto de entrada;
- predecir y verificar una salida;
- provocar, explicar y corregir un error sencillo;
- crear una evidencia reproducible.

## Seguridad y uso de IA

No incluyas rutas personales, credenciales ni datos reales en capturas o repositorios. Si una IA te ayuda a interpretar un error, conserva el mensaje original y verifica la solución ejecutando el programa.
