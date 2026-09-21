# Capítulo 01 — Primeros programas en Java

## Hitos relacionados

```text
H1
```

## Qué aprenderás

- estructura mínima de un programa Java
- clase Main
- método main
- compilación y ejecución
- primeros mensajes por consola

## 1. Punto de partida

MiniJarvis se construye por capas. Este capítulo trabaja una pieza concreta del proyecto y la conecta con evidencias reales: código, pruebas, documentación, defensa y uso responsable de IA si procede.

La regla de estudio es siempre la misma:

```text
Lee el concepto, ejecuta un ejemplo pequeño, aplícalo a MiniJarvis, documenta la evidencia y prepárate para defenderlo.
```

## 2. Conceptos básicos explicados

Un programa Java básico necesita una clase. Para empezar usaremos una clase llamada `Main`. Dentro aparece el método `main`, que es el punto de entrada: por ahí comienza la ejecución.

Compilar significa convertir el código fuente `.java` en bytecode `.class`. Ejecutar significa pedir a Java que arranque el programa. En este nivel debes entender el ciclo mínimo: escribir, compilar, ejecutar, observar, corregir.

La consola será nuestra primera interfaz. MiniJarvis todavía no será inteligente: primero debe hablar de forma simple y predecible.

## 3. Ejemplo guiado en Java

```java
public class Main {
    public static void main(String[] args) {
        System.out.println("Hola, soy MiniJarvis.");
        System.out.println("Estoy aprendiendo a funcionar por consola.");
    }
}
```

## 4. Caso práctico MiniJarvis

Crea `src/Main.java`. Haz que MiniJarvis muestre tres mensajes: saludo, nombre del proyecto y una frase sobre qué podrá hacer más adelante.

Después compila y ejecuta:

```bash
javac src/Main.java
java -cp src Main
```

Guarda en tu portfolio qué comando has usado y qué salida esperabas.

## 5. Evidencia de Entornos de Desarrollo

Documento mínimo: `README.md` con dos apartados: “Cómo compilar” y “Cómo ejecutar”. Añade una captura o copia de salida de consola. Si hay error, anota el mensaje exacto.

## 6. Errores frecuentes y cómo corregirlos

| Error | Síntoma | Corrección |
|---|---|---|
| Nombre de archivo incorrecto | Main.java no coincide con public class Main | Alinear nombre de archivo y clase |
| Falta punto y coma | Error de compilación | Revisar final de cada instrucción |
| Ejecutar desde carpeta equivocada | No encuentra la clase | Usar `java -cp src Main` |

## 7. Preguntas de repaso

1. ¿Qué hace el método main?
2. ¿Qué diferencia hay entre compilar y ejecutar?
3. ¿Por qué usamos consola al principio?
4. ¿Qué evidencia demuestra que tu programa funciona?

## 8. Para tu portfolio

Copia y completa este bloque en tu portfolio:

```text
Capítulo 01: Primeros programas en Java
Qué he aprendido:
Código o documento que lo demuestra:
Prueba realizada:
Error que he corregido:
Qué puedo defender oralmente:
Uso de IA, si lo hubo, y cómo lo validé:
```

## 9. Estudio paso a paso

Antes de avanzar, asegúrate de que puedes explicar el recorrido completo de un programa sencillo. Primero escribes el archivo `Main.java`. Después compilas con `javac`. Si hay errores, Java te indica una línea aproximada y un mensaje. No copies el mensaje sin leerlo: busca si falta una llave, un punto y coma o si el nombre de la clase no coincide. Cuando compila, ejecutas con `java -cp src Main`.

Caso de estudio: cambia el mensaje de bienvenida tres veces y recompila cada vez. Comprueba que la salida cambia solo cuando vuelves a compilar. Esto te ayuda a entender la diferencia entre código fuente y programa compilado.
