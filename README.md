# MiniJarvis — edición final de trabajo y publicación

Curso 2026/2027 — 1.º DAW — Programación.

## Base metodológica

MiniJarvis adopta el Modelo HEXA de seis fases: Activar, Investigar, Idear, Planificar, Ejecutar y Comunicar, con Equipos como Fase 0 transversal.

- Fuente canónica: `02-PROFESORADO/04-RECURSOS-NORMATIVOS-Y-TEMARIOS/Modelo_HEXA_COMPLETO.pdf`.
- Aplicación al calendario y a las evidencias de MiniJarvis: `02-PROFESORADO/04-RECURSOS-NORMATIVOS-Y-TEMARIOS/Modelo_HEXA_APLICADO_A_MINIJARVIS.md`.

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
- `Minijarvis-presentaciones-sesiones.zip`: las 106 presentaciones de aula organizadas por hito.
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

Después de regenerar el HTML o modificar una tarea Moodle, sincroniza el staging y crea el ZIP reproducible:

```bash
python3 generar_paquete_moodle.py
python3 generar_paquete_moodle.py --check
```

Ambos exportadores requieren `pandoc` instalado en el sistema.

## Entorno Python de mantenimiento

Los generadores de presentaciones y sus pruebas requieren las dependencias declaradas en `requirements.txt` y `requirements-dev.txt`.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
pytest -q
```

Los ZIP no son copias restaurables `.mbz`. La copia `.mbz` se genera desde Moodle después de configurar y probar el aula, sin usuarios ni datos de usuario.
