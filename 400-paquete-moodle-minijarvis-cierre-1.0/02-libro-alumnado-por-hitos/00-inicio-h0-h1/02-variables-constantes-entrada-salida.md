# Capítulo 02 — Variables, constantes y entrada/salida

## Hitos relacionados

```text
H1
```

## Qué aprenderás

- variables
- tipos básicos
- constantes
- Scanner
- entrada por teclado
- salida por consola

## 1. Punto de partida

MiniJarvis se construye por capas. Este capítulo trabaja una pieza concreta del proyecto y la conecta con evidencias reales: código, pruebas, documentación, defensa y uso responsable de IA si procede.

La regla de estudio es siempre la misma:

```text
Lee el concepto, ejecuta un ejemplo pequeño, aplícalo a MiniJarvis, documenta la evidencia y prepárate para defenderlo.
```

## 2. Conceptos básicos explicados

Una variable guarda un dato que puede cambiar. Una constante guarda un dato que no debería cambiar durante la ejecución. Java exige indicar el tipo: `String` para texto, `int` para enteros, `boolean` para verdadero/falso.

La entrada permite que el usuario participe. Usaremos `Scanner` para leer texto desde teclado. La salida se realiza con `System.out.println` o `System.out.print`. Entrada y salida son la base de un asistente por consola.

## 3. Ejemplo guiado en Java

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        final String AGENT_NAME = "MiniJarvis";
        Scanner scanner = new Scanner(System.in);

        System.out.print("¿Cómo te llamas? ");
        String userName = scanner.nextLine();

        System.out.println("Hola, " + userName + ". Soy " + AGENT_NAME + ".");
    }
}
```

## 4. Caso práctico MiniJarvis

MiniJarvis debe pedir el nombre del usuario y responder con un saludo personalizado. Después añade una variable `courseYear` y muestra el curso ficticio.

Amplía el caso: si el usuario deja el nombre vacío, de momento solo observa qué ocurre. La validación llegará después.

## 5. Evidencia de Entornos de Desarrollo

Actualiza el README indicando que el programa requiere interacción por teclado. Añade una prueba manual: entrada usada y salida observada.

## 6. Errores frecuentes y cómo corregirlos

| Error | Síntoma | Corrección |
|---|---|---|
| No importar Scanner | cannot find symbol Scanner | Añadir `import java.util.Scanner;` |
| Confundir int y String | Error de tipos | Elegir tipo según dato |
| No probar entrada vacía | Caso límite no detectado | Registrar qué ocurre |

## 7. Preguntas de repaso

1. ¿Qué es una variable?
2. ¿Qué aporta una constante?
3. ¿Para qué sirve Scanner?
4. ¿Qué prueba manual puedes escribir para entrada/salida?

## 8. Para tu portfolio

Copia y completa este bloque en tu portfolio:

```text
Capítulo 02: Variables, constantes y entrada/salida
Qué he aprendido:
Código o documento que lo demuestra:
Prueba realizada:
Error que he corregido:
Qué puedo defender oralmente:
Uso de IA, si lo hubo, y cómo lo validé:
```

## 9. Estudio paso a paso

Cuando uses variables, pregúntate tres cosas: qué dato quiero guardar, qué tipo tiene y si cambiará durante la ejecución. El nombre de la variable debe explicar su intención. `n` dice poco; `userName` ayuda más. Una constante como `AGENT_NAME` evita escribir el mismo texto en varios lugares y comunica que ese valor no debe cambiar.

Caso de estudio: añade `String favoriteTopic` y pregunta al usuario qué parte de programación quiere practicar. MiniJarvis debe responder con una frase personalizada. Registra dos pruebas: una con texto normal y otra con entrada vacía. Todavía no tienes que resolver la entrada vacía, pero sí observarla.
