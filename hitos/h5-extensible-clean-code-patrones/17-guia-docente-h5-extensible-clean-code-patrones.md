# Guía docente — H5 Agente extensible, clean code y patrones iniciales

## Programación + Entornos de Desarrollo — 1.º DAW — Curso 2026/2027

Versión: borrador 0.1

Documentos relacionados:

- `../../02-calendario-hitos-sprints-2026-2027.md`
- `../../04A-enunciados-y-entregables-alumnado.md`
- `../../06-rubricas-hitos.md`
- `README.md`
- `17B-ficha-alumnado-h5-extensible-clean-code-patrones.md`
- `17C-checklist-correccion-h5.md`

---

## 1. Propósito del hito

H5 convierte MiniJarvis en un agente más extensible y mantenible.

Producto esperado:

```text
MiniJarvis H5: agente con herramientas internas extensibles, refactorización documentada, revisión de código y decisión razonada sobre patrón de diseño.
```

El objetivo no es usar patrones por usarlos, sino detectar un problema real del código y mejorar la estructura.

---

## 2. Qué añade H5 respecto a H4

| H4 | H5 |
|---|---|
| Clases principales `Agent` y `Memory`. | Herramientas/comandos separables. |
| Diseño OO inicial. | Extensibilidad y bajo impacto al añadir comandos. |
| Diagramas de diseño. | Refactorización antes/después. |
| Defensa de responsabilidades. | Defensa de decisión de patrón o no patrón. |

---

## 3. Restricciones didácticas

En H5 sí debe aparecer:

- refactorización justificada;
- herramienta/comando interno nuevo;
- evidencia de Git o registro equivalente;
- revisión de código;
- decisión razonada sobre patrón;
- comparación Java ↔ Python.

En H5 NO debe forzarse:

- sistema real de plugins;
- arquitectura hexagonal;
- framework externo;
- persistencia;
- IA real;
- patrones múltiples sin necesidad.

---

## 4. Fechas y duración

Fechas orientativas:

```text
8 febrero - 19 marzo 2027
```

---

## 5. RA/CE y evidencias

### Programación

- PR RA7, no imprescindible pero evaluable.
- Refuerzo PR RA4 y PR RA6.

Evidencias:

- comandos/herramientas separables;
- nombres claros;
- responsabilidades mejoradas;
- capacidad de añadir una herramienta con bajo impacto.

### Entornos de Desarrollo

- ED RA4.a-e: refactorización, análisis de código y pruebas asociadas.
- ED RA4.f-h: control de versiones, documentación y repositorios remotos.
- ED RA4.i: integración continua si el nivel lo permite.
- ED RA6.g-h si se usan diagramas de comportamiento/estado.

Evidencias:

- informe antes/después;
- evidencia de rama, commits, PR o revisión;
- revisión de código;
- registro de patrón si se usa.

---

## 6. Diseño mínimo recomendado

Solución didáctica recomendada:

```text
Separar cada herramienta/comando en una clase sencilla con una responsabilidad clara.
```

Clases posibles:

| Clase/interfaz | Responsabilidad |
|---|---|
| `Tool` | Contrato común para herramientas. |
| `HelpTool` | Mostrar comandos. |
| `GreetTool` | Saludar. |
| `RememberTool` | Guardar recuerdos. |
| `MemoryTool` | Mostrar memoria. |
| `StatusTool` | Mostrar estado. |
| `Agent` | Orquestar ejecución y delegar en herramientas. |
| `Memory` | Gestionar recuerdos. |

Patrón posible:

```text
Command simplificado: cada comando se representa como una herramienta con nombre y método execute.
```

Importante:

```text
Si el grupo no está preparado, se puede hablar de “herramientas/comandos separables” sin exigir terminología formal de patrón.
```

---

## 7. Entregables H5

| Entregable | Responsable | Formato | Plantilla local |
|---|---|---|---|
| Código extensible | Equipo/individual | `src/*.java` | No aplica. |
| README H5 | Equipo/individual | `README.md` | `plantillas/README-h5-template.md` |
| Informe de refactorización | Equipo | `docs/informe-refactorizacion-h5.md` | `plantillas/informe-refactorizacion-h5-template.md` |
| Evidencia Git/revisión | Equipo | `docs/evidencia-git-h5.md` | `plantillas/evidencia-git-h5-template.md` |
| Revisión de código | Equipo | `docs/revision-codigo-h5.md` | `plantillas/revision-codigo-h5-template.md` |
| Registro de patrón | Equipo | `docs/registro-patron-h5.md` | `plantillas/registro-patron-h5-template.md` |
| Comparación Java ↔ Python | Individual | `docs/comparacion-java-python-h5.md` | `plantillas/comparacion-java-python-h5-template.md` |
| Portfolio H5 | Individual | `docs/portfolio-h5.md` | `plantillas/portfolio-h5-template.md` |
| Registro IA | Individual/equipo | `docs/registro-ia.md` | `plantillas/registro-ia-h5-template.md` |
| Defensa H5 | Individual | `docs/defensa-h5.md` | `plantillas/defensa-h5-template.md` |

---

## 8. Errores previsibles

| Error | Señal | Intervención docente |
|---|---|---|
| Patrón forzado | No sabe explicar problema | Pedir alternativa simple y motivo. |
| Refactorización cosmética | Solo cambia nombres | Exigir antes/después con impacto. |
| Git simulado sin trazabilidad | No hay commits/revisión | Aceptar registro equivalente si no hay GitHub, pero claro. |
| Herramientas acopladas | Añadir comando toca muchas clases | Preguntar “¿qué tendría que cambiar para añadir otra herramienta?”. |
| Código demasiado avanzado | No lo defiende | Reducir a interfaz/clase simple. |

---

## 9. Preparación para H6

Antes de pasar a H6, comprobar:

- si añadir una herramienta nueva es sencillo;
- si hay evidencia de refactorización real;
- si Git/revisión está documentado;
- si el patrón se usa o descarta con criterio;
- si el código sigue siendo entendible.

H6 introducirá persistencia, trazabilidad, reproducibilidad y seguridad básica.
