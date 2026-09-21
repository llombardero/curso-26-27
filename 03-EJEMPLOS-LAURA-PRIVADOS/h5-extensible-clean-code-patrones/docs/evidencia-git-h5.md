# Evidencia Git/revisión — H5

## Rama

```text
feature/h5-tools
```

## Commits o cambios

| Cambio | Motivo |
|---|---|
| Extraer interfaz Tool | Tener contrato común para herramientas. |
| Crear herramientas separadas | Reducir if/else en Agent. |
| Añadir CourseTool | Comprobar que añadir una herramienta tiene bajo impacto. |
| Actualizar README y defensa | Documentar diseño. |

## Revisión/PR

```text
Revisión simulada en clase: comprobar nombres, responsabilidades y que el patrón no sea decorativo.
```

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

