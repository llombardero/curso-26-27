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
Foco de aprendizaje: interfaces, extensibilidad, pruebas y primer patrón.
```

Conceptos que Laura debe saber defender en este hito:

- test unitario
- aserto
- TDD
- interfaz
- implementación
- método default como ampliación
- excepciones
- recursividad como comparación
- métodos estáticos
- records como ampliación
- enum
- polimorfismo por interfaz
- Command simplificado
- clean code
- refactorización segura

Respuesta modelo de Laura:

> En H5 defiendo que el patrón Command simplificado aparece porque resuelve un problema real: demasiados comandos mezclados dentro de Agent.

Evidencia que Laura debe señalar:

- una parte concreta del código o documento donde aparezca el concepto;
- una prueba, ejecución, captura o explicación que demuestre que no lo ha copiado sin entender;
- una mejora razonable que podría hacer si tuviera más tiempo.

