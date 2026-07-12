# Capítulo 07 — Encapsulación, responsabilidades y UML

## Hitos relacionados

```text
H4
```

## Qué aprenderás

- private/public
- encapsulación
- diagrama de clases
- diagrama de comportamiento
- relación diagrama-código

## 1. Punto de partida

MiniJarvis se construye por capas. Este capítulo trabaja una pieza concreta del proyecto y la conecta con evidencias reales: código, pruebas, documentación, defensa y uso responsable de IA si procede.

La regla de estudio es siempre la misma:

```text
Lee el concepto, ejecuta un ejemplo pequeño, aplícalo a MiniJarvis, documenta la evidencia y prepárate para defenderlo.
```

## 2. Conceptos básicos explicados

Encapsular significa proteger el estado interno de una clase. En Java, los atributos suelen ser `private` y se accede a ellos mediante métodos controlados. `public` debe reservarse para lo que otras clases necesitan usar.

UML ayuda a representar estructura y comportamiento. Un diagrama de clases muestra clases, atributos, métodos y relaciones. Un diagrama de comportamiento muestra pasos en el tiempo.

## 3. Ejemplo guiado en Java

```java
public class Memory {
    private ArrayList<String> memories;

    public Memory() {
        this.memories = new ArrayList<>();
    }

    public int count() {
        return memories.size();
    }
}
```

## 4. Caso práctico MiniJarvis

Haz un diagrama de clases de MiniJarvis H4 con `Main`, `Agent` y `Memory`. Después elige el flujo `recuerda` y escribe los pasos: usuario escribe comando, Agent pide texto, Memory guarda, Agent informa.

Relaciona al menos cinco elementos del diagrama con código real.

## 5. Evidencia de Entornos de Desarrollo

Crea `docs/diagrama-clases.md`, `docs/diagrama-comportamiento.md` y `docs/relacion-diagrama-codigo.md`. Entornos exige que el diagrama no sea inventado: debe coincidir con el código.

## 6. Errores frecuentes y cómo corregirlos

| Error | Síntoma | Corrección |
|---|---|---|
| Todo public | Cualquier clase puede tocar datos internos | Atributos private |
| Diagrama inventado | Aparecen clases inexistentes | Actualizar desde código real |
| Confundir estructura y comportamiento | Mezcla clases con pasos | Separar diagrama de clases y flujo |

## 7. Preguntas de repaso

1. ¿Por qué los atributos suelen ser private?
2. ¿Qué significa + y - en un diagrama?
3. ¿Qué relación hay entre Agent y Memory?
4. ¿Cómo demuestras que un diagrama coincide con código?

## 8. Para tu portfolio

Copia y completa este bloque en tu portfolio:

```text
Capítulo 07: Encapsulación, responsabilidades y UML
Qué he aprendido:
Código o documento que lo demuestra:
Prueba realizada:
Error que he corregido:
Qué puedo defender oralmente:
Uso de IA, si lo hubo, y cómo lo validé:
```

## 9. Estudio paso a paso

La encapsulación evita que cualquier parte del programa cambie datos internos sin control. Si `memories` fuera público, otra clase podría borrar la lista, meter valores vacíos o sustituirla por `null`. Al hacerla `private`, obligas a usar métodos que pueden validar.

Caso de estudio: intenta explicar una decisión de visibilidad. No digas “es private porque sí”. Di qué riesgo evita. Después revisa tu diagrama: por cada atributo o método importante, busca la línea de código correspondiente. Si no la encuentras, el diagrama está inventando información o el código está desactualizado.
