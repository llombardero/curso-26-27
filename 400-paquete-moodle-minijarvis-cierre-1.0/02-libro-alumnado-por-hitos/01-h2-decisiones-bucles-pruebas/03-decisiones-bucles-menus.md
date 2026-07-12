# Capítulo 03 — Decisiones, bucles y menús

## Hitos relacionados

```text
H2
```

## Qué aprenderás

- condicionales if/else
- boolean
- bucles while
- menús por consola
- comandos
- casos límite

## 1. Punto de partida

MiniJarvis se construye por capas. Este capítulo trabaja una pieza concreta del proyecto y la conecta con evidencias reales: código, pruebas, documentación, defensa y uso responsable de IA si procede.

La regla de estudio es siempre la misma:

```text
Lee el concepto, ejecuta un ejemplo pequeño, aplícalo a MiniJarvis, documenta la evidencia y prepárate para defenderlo.
```

## 2. Conceptos básicos explicados

Un agente necesita tomar decisiones: si el usuario escribe `ayuda`, muestra ayuda; si escribe `salir`, termina. Para eso usamos condicionales.

Un menú necesita repetirse hasta que el usuario quiera salir. Para eso usamos un bucle `while`. Una variable booleana como `running` permite controlar si el programa sigue activo.

El objetivo no es crear un menú enorme, sino un bucle claro y defendible.

## 3. Ejemplo guiado en Java

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        boolean running = true;

        while (running) {
            System.out.print("> ");
            String command = scanner.nextLine().trim().toLowerCase();

            if (command.equals("ayuda")) {
                System.out.println("Comandos: ayuda, estado, salir");
            } else if (command.equals("estado")) {
                System.out.println("MiniJarvis está activo.");
            } else if (command.equals("salir")) {
                running = false;
            } else {
                System.out.println("No entiendo ese comando.");
            }
        }
    }
}
```

## 4. Caso práctico MiniJarvis

Construye el menú de MiniJarvis H2 con comandos `ayuda`, `estado` y `salir`. Añade un comando `saluda` que muestre un saludo.

Caso práctico de prueba: ejecuta `ayuda`, `estado`, un comando desconocido y `salir`. Documenta la salida.

## 5. Evidencia de Entornos de Desarrollo

Crea `docs/pruebas-menu.md` con tabla: comando, resultado esperado, resultado observado, estado. Esto conecta Programación con Entornos mediante pruebas manuales.

## 6. Errores frecuentes y cómo corregirlos

| Error | Síntoma | Corrección |
|---|---|---|
| Bucle infinito sin salida | No hay forma de terminar | Añadir comando salir y `running=false` |
| Comparar String con == | No entra en condiciones | Usar `.equals` |
| No normalizar entrada | AYUDA no funciona | Usar `trim().toLowerCase()` |

## 7. Preguntas de repaso

1. ¿Para qué sirve un boolean en el menú?
2. ¿Por qué usamos while?
3. ¿Qué hace trim?
4. ¿Qué comando demuestra el caso desconocido?

## 8. Para tu portfolio

Copia y completa este bloque en tu portfolio:

```text
Capítulo 03: Decisiones, bucles y menús
Qué he aprendido:
Código o documento que lo demuestra:
Prueba realizada:
Error que he corregido:
Qué puedo defender oralmente:
Uso de IA, si lo hubo, y cómo lo validé:
```

## 9. Estudio paso a paso

Un menú por consola debe ser predecible. Cada comando tiene una condición, una acción y una salida esperada. Si el menú crece demasiado, más adelante lo refactorizarás, pero ahora lo importante es entender el flujo. La variable `running` es el interruptor del programa: mientras sea `true`, el bucle continúa.

Caso de estudio: añade el comando `version`. Debe mostrar `MiniJarvis H2`. Después prueba mayúsculas, espacios antes/después y comando desconocido. Escribe una tabla de pruebas. No des por bueno el menú hasta comprobar al menos cuatro entradas distintas.
