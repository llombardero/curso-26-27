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
