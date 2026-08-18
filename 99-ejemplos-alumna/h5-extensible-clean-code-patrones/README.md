# H5 — Agente extensible, clean code y patrones iniciales

Alumna: Laura García Martín  
Equipo: Equipo Ada

---

## Qué mejora H5

```text
En H4 Agent tenía un bloque if/else para todos los comandos. En H5 cada herramienta tiene su propia clase y Agent solo busca la herramienta correspondiente y la ejecuta.
```

---

## Herramientas disponibles

| Herramienta | Clase | Responsabilidad |
|---|---|---|
| `ayuda` | `HelpTool` | Mostrar herramientas. |
| `saluda` | `GreetTool` | Saludar. |
| `recuerda` | `RememberTool` | Guardar recuerdos. |
| `memoria` | `MemoryTool` | Mostrar memoria. |
| `estado` | `StatusTool` | Mostrar estado. |
| `curso` | `CourseTool` | Mostrar curso de inicio. |
| `salir` | `ExitTool` | Terminar. |

---

## Cómo ejecutar

```bash
javac src/*.java
java -cp src Main
```

---

## Decisión de diseño

```text
Uso una interfaz Tool como Command simplificado. Cada herramienta conoce su comando, su descripción y cómo ejecutarse.
```

<!-- AJUSTE-COBERTURA-CONCEPTOS-32 -->

## Respuesta de Laura — cobertura de conceptos de Programación

Relación con `32-lista-conceptos-programacion-por-tema.md`:

```text
H5 trabaja principalmente: Temas 5 y 6.
Foco de aprendizaje: interfaces, extensibilidad, pruebas, primer patrón y laboratorio técnico de programación avanzada de clases.
```

Conceptos que Laura debe saber defender en este hito:

- test unitario, aserto y TDD como forma de comprobar cambios;
- interfaz `Tool` e implementación en clases concretas;
- polimorfismo por interfaz: `Agent` puede tratar varias herramientas como `Tool`;
- Command simplificado: cada herramienta encapsula una acción;
- clean code y refactorización segura;
- `enum` y `record` como ampliación razonada, no como adorno;
- métodos estáticos y recursividad como comparación/refuerzo;
- `@Override`, `toString`, `equals` y `hashCode` en ejemplos pequeños;
- `Comparable` / `compareTo` o `Comparator` para ordenar herramientas o comandos;
- `instanceof` como ejemplo que entiendo, pero que no debo abusar si puedo usar polimorfismo;
- clase abstracta, herencia, `super`, `protected` y package-private como comparación frente a interfaz/composición;
- métodos `default` y métodos privados en interfaces como lectura guiada o microejemplo;
- clases anónimas, clases finales y clases selladas como conceptos de reconocimiento/ampliación.

Respuesta modelo de Laura:

> En H5 defiendo que `Tool` funciona como un Command simplificado porque resuelve un problema real: antes `Agent` acumulaba demasiados `if/else` y ahora puede ejecutar herramientas diferentes mediante el mismo contrato. También puedo explicar que no todo lo avanzado del Tema 6 debe entrar en el producto final: he probado o estudiado `equals`, `hashCode`, `Comparable`, `instanceof`, clases abstractas y herencia para saber reconocerlos, pero mantengo en MiniJarvis la solución más simple y defendible.

Evidencia que Laura debe señalar:

- `Tool`, `HelpTool`, `RememberTool`, `StatusTool`, `CourseTool` o equivalente;
- `docs/registro-patron-h5.md`, explicando por qué Command sí tiene sentido y por qué otros patrones no;
- `docs/refuerzo-poo-avanzada-h5.md`, si existe, para demostrar el laboratorio de Tema 6;
- una prueba de que al añadir una herramienta nueva no se rompe el menú;
- una decisión explícita sobre interfaz/composición frente a herencia/clase abstracta.

Pregunta de defensa aconsejada:

> ¿Qué concepto avanzado del Tema 6 has decidido no meter en MiniJarvis y por qué esa renuncia mejora el diseño?

