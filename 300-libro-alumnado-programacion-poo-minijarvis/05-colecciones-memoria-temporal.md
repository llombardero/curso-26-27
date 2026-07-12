# Capítulo 05 — Colecciones y memoria temporal

## Hitos relacionados

```text
H3
```

## Qué aprenderás

- ArrayList
- memoria temporal
- add
- size
- isEmpty
- recorrido con for
- casos límite

## 1. Punto de partida

MiniJarvis se construye por capas. Este capítulo trabaja una pieza concreta del proyecto y la conecta con evidencias reales: código, pruebas, documentación, defensa y uso responsable de IA si procede.

La regla de estudio es siempre la misma:

```text
Lee el concepto, ejecuta un ejemplo pequeño, aplícalo a MiniJarvis, documenta la evidencia y prepárate para defenderlo.
```

## 2. Conceptos básicos explicados

Una colección permite guardar varios valores. En H3 usaremos `ArrayList<String>` para recuerdos. Es memoria temporal: vive mientras el programa está abierto. Si cierras, desaparece.

Los métodos básicos son `add` para añadir, `size` para contar, `isEmpty` para comprobar si está vacía y `get` para recuperar por posición.

## 3. Ejemplo guiado en Java

```java
import java.util.ArrayList;

public class MemoryExample {
    public static void main(String[] args) {
        ArrayList<String> memories = new ArrayList<>();
        memories.add("Traer libreta");
        memories.add("Repasar bucles");

        for (int i = 0; i < memories.size(); i++) {
            System.out.println((i + 1) + ". " + memories.get(i));
        }
    }
}
```

## 4. Caso práctico MiniJarvis

Añade a MiniJarvis los comandos `recuerda`, `memoria` y `estado`. `recuerda` pide texto y lo añade a la lista. `memoria` muestra recuerdos numerados. `estado` muestra cuántos recuerdos hay.

Prueba casos: memoria vacía, recuerdo normal y recuerdo vacío.

## 5. Evidencia de Entornos de Desarrollo

Crea `docs/pruebas-memoria.md` y `docs/justificacion-coleccion.md`. Explica por qué `ArrayList` es suficiente en este hito y por qué todavía no se guarda en fichero.

## 6. Errores frecuentes y cómo corregirlos

| Error | Síntoma | Corrección |
|---|---|---|
| No inicializar ArrayList | NullPointerException | Crear con `new ArrayList<>()` |
| No gestionar memoria vacía | Salida confusa | Usar `isEmpty()` |
| Guardar texto vacío | Recuerdos sin contenido | Validar `trim().isEmpty()` |

## 7. Preguntas de repaso

1. ¿Qué diferencia hay entre memoria temporal y persistente?
2. ¿Por qué ArrayList encaja en H3?
3. ¿Cómo recorres recuerdos?
4. ¿Qué caso límite debes probar?

## 8. Para tu portfolio

Copia y completa este bloque en tu portfolio:

```text
Capítulo 05: Colecciones y memoria temporal
Qué he aprendido:
Código o documento que lo demuestra:
Prueba realizada:
Error que he corregido:
Qué puedo defender oralmente:
Uso de IA, si lo hubo, y cómo lo validé:
```

## 9. Estudio paso a paso

Una colección no es solo una variable grande. Es una estructura que permite guardar varios elementos y operar con ellos. En H3 usamos `ArrayList` porque el orden de inserción nos sirve y porque queremos añadir recuerdos de forma sencilla. No necesitamos todavía búsquedas complejas ni claves.

Caso de estudio: guarda tres recuerdos ficticios y muéstralos numerados. Después prueba memoria vacía al iniciar el programa. Finalmente intenta guardar un recuerdo vacío. Si tu programa lo guarda, tienes una mejora pendiente: validar antes de añadir. Explica por qué guardar datos vacíos empeora la calidad del agente.
