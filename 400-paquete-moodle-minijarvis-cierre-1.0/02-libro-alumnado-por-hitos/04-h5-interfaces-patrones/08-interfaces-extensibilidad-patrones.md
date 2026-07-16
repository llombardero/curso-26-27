# Capítulo 08 — Interfaces, extensibilidad y patrones iniciales

## Hitos relacionados

```text
H5
```

## Qué aprenderás

- extensibilidad
- interfaz
- Tool
- refactorización
- clean code
- patrón Command simplificado
- cuándo introducir patrones
- enum y record como refuerzo
- @Override, toString y ordenación sencilla
- herencia y clase abstracta como comparación

## 1. Punto de partida

MiniJarvis se construye por capas. Este capítulo trabaja una pieza concreta del proyecto y la conecta con evidencias reales: código, pruebas, documentación, defensa y uso responsable de IA si procede.

La regla de estudio es siempre la misma:

```text
Lee el concepto, ejecuta un ejemplo pequeño, aplícalo a MiniJarvis, documenta la evidencia y prepárate para defenderlo.
```

## 2. Conceptos básicos explicados

La extensibilidad mide lo fácil que es añadir funcionalidades sin romper lo existente. En H5 el problema visible es que `Agent` puede llenarse de `if/else` para cada comando.

Una interfaz define un contrato. `Tool` puede exigir nombre, descripción y ejecución. Así cada comando se convierte en una herramienta separada.

Los patrones de diseño se introducen aquí porque ya existe base de POO: clases, objetos, responsabilidades, encapsulación e interfaces. Antes de H5 serían decoración. En H5 el patrón Command simplificado tiene sentido porque resuelve un problema real: encapsular acciones en objetos.

Aunque MiniJarvis se apoye principalmente en interfaces y composición, el Tema 6 también trabaja herencia, clases abstractas, `super`, `protected`, `@Override`, métodos de `Object` y comparación de objetos. En H5 se estudiarán como laboratorio técnico: solo se incorpora al proyecto principal lo que siga siendo simple y defendible.

## 3. Ejemplo guiado en Java

```java
public interface Tool {
    String getName();
    String getDescription();
    boolean execute(Agent agent);
}

public class StatusTool implements Tool {
    public String getName() { return "estado"; }
    public String getDescription() { return "Muestra el estado."; }
    public boolean execute(Agent agent) {
        System.out.println("MiniJarvis está activo.");
        return true;
    }
}
```

## 4. Caso práctico MiniJarvis

Refactoriza un comando de `Agent` a una clase `Tool`. Después añade `CourseTool` como herramienta nueva. Documenta cuántos archivos has tocado.

Defensa: explica si tu solución se parece al patrón Command y por qué no has añadido patrones más complejos.

Refuerzo de cobertura de los temas 5 y 6:

- Crea `enum CommandType` para comandos conocidos o explica por qué prefieres `String` en esta fase.
- Valora un `record CommandResult` o `record AiResponse` para transportar una respuesta simple.
- Añade `@Override` en las clases que implementan `Tool`.
- Implementa `toString` en una clase de dominio y explica cuándo ayuda.
- Ordena herramientas por nombre usando `Comparable` o `Comparator`, si el grupo está preparado.
- Compara `interface Tool` con una clase abstracta `BaseTool` que tenga `name` y `description`; decide cuál se mantiene.

## 5. Evidencia de Entornos de Desarrollo

Crea `docs/informe-refactorizacion.md`, `docs/revision-codigo.md` y `docs/registro-patron.md`. Incluye antes/después, prueba, revisión y decisión razonada sobre patrón.

## 6. Errores frecuentes y cómo corregirlos

| Error | Síntoma | Corrección |
|---|---|---|
| Usar patrón porque sí | No sabe explicar problema | Conectar patrón con if/else creciente |
| Demasiadas clases | Arquitectura no defendible | Mantener Tool simple |
| No probar tras refactorizar | Comandos rotos | Prueba mínima ayuda/estado/salir |
| Forzar herencia | Jerarquía artificial | Comparar con interfaz/composición y elegir lo más simple |
| No usar @Override | Errores pasan desapercibidos | Marcar métodos implementados o sobrescritos |

## 7. Preguntas de repaso

1. ¿Cuándo conviene introducir patrones de diseño?
2. ¿Qué problema resuelve Command simplificado?
3. ¿Qué es una interfaz?
4. ¿Qué prueba demuestra extensibilidad?
5. ¿Qué diferencia hay entre interfaz y clase abstracta?
6. ¿Qué aporta `@Override`?
7. ¿Cuándo usarías un `enum`?

## 8. Para tu portfolio

Copia y completa este bloque en tu portfolio:

```text
Capítulo 08: Interfaces, extensibilidad y patrones iniciales
Qué he aprendido:
Código o documento que lo demuestra:
Prueba realizada:
Error que he corregido:
Qué puedo defender oralmente:
Uso de IA, si lo hubo, y cómo lo validé:
```

## 9. Estudio paso a paso

Los patrones de diseño no aparecen al principio del curso porque antes serían una receta sin contexto. En H5 ya has visto el problema: cada comando nuevo puede hacer crecer `Agent`. Ahí tiene sentido hablar de una idea parecida a Command: convertir acciones en objetos con una forma común.

Caso de estudio: añade `CourseTool`. Si solo creas una clase y la registras en una lista, has reducido el impacto del cambio. Si tienes que modificar muchas condiciones en muchos sitios, tu diseño aún no es tan extensible. Defiende el patrón con una frase sencilla: “cada herramienta encapsula una acción ejecutable”.

Caso de estudio de refuerzo: crea `docs/refuerzo-poo-avanzada-h5.md`. Incluye una pequeña comparación entre `interface Tool` y `BaseTool abstracta`. Si descartas la clase abstracta, la evidencia sigue siendo válida si explicas técnicamente el motivo.
