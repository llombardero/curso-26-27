# MiniJarvis — edición final de trabajo y publicación

Curso 2026/2027 — 1.º DAW — Programación y Entornos de Desarrollo.

## Audiencias

- `01-ALUMNADO/`: materiales publicables progresivamente.
- `02-PROFESORADO/`: planificación, administración y guías privadas.
- `03-EJEMPLOS-LAURA-PRIVADOS/`: modelos ocultos hasta después del intento propio.

## Ecosistema de trabajo

- Moodle organiza, recibe entregas, conserva la fecha, aplica rúbricas y comunica feedback.
- La carpeta maestra docente de Drive ofrece recursos comunes y una carpeta de acceso limitado por equipo.
- Sheets registra el diario individual y el trabajo Scrum.
- Sites selecciona y explica evidencias.
- GitHub conserva el código y su historial desde H1.

La carpeta maestra de Drive simula la separación de una Unidad compartida, pero no su propiedad institucional: cada archivo puede pertenecer a quien lo crea. Por eso el profesorado crea los documentos estructurales y Moodle conserva evidencias cerradas.

## Despliegue y paquetes

- `GUIA-DESPLIEGUE-MOODLE.md`: publicación segura y progresiva.
- `MANIFIESTO-ARCHIVOS.md`: inventario SHA-256.
- `Minijarvis-alumnado.zip`: transporte de materiales publicables.
- `Minijarvis-alumnado-html.zip`: transporte de materiales publicables en HTML para alumnado.
- `Minijarvis-profesorado.zip`: transporte privado docente.
- `Minijarvis-ejemplos-Laura-privados.zip`: ejemplos de apertura diferida.
- `04-DRIVE-5-EQUIPOS/`: estructura preparada para recursos comunes y cinco equipos en Drive.
- `Minijarvis-drive-5-equipos.zip`: transporte de la estructura Drive.
- `05-PAQUETE-MOODLE/`: recursos, tareas y guías para montar el curso en Moodle.
- `Minijarvis-paquete-moodle.zip`: transporte del paquete de preparación Moodle.

La carpeta `01-ALUMNADO/` conserva los originales en Markdown. La carpeta `01-ALUMNADO-HTML/` y el ZIP HTML son la versión recomendada para entregar al alumnado, porque se abren directamente en el navegador y en Moodle sin exigir conocimientos de Markdown.

Para regenerar la versión HTML después de editar los originales:

```bash
python3 exportar_alumnado_html.py
```

Los ZIP no son copias restaurables `.mbz`. La copia `.mbz` se genera desde Moodle después de configurar y probar el aula, sin usuarios ni datos de usuario.
