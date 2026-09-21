# Revisión de código — H5

| Elemento revisado | Hallazgo | Decisión |
|---|---|---|
| Nombres | Tool, Agent y Memory son claros. | Mantener. |
| Duplicación | Las herramientas comparten estructura. | Aceptable para nivel H5. |
| Responsabilidades | Agent orquesta; Tool ejecuta; Memory guarda. | Correcto. |
| Complejidad | Más clases que H4, pero cada una es simple. | Aceptable. |
| Nueva herramienta | CourseTool se añade sin tocar processCommand. | Evidencia de extensibilidad. |
