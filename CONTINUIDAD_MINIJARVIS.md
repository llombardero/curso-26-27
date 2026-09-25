# Continuidad de MiniJarvis

Actualizado: 2026-09-25 02:02 CEST

## 1. Objetivo actual

Convertir la rama `refactor/hitos-v3` en un proyecto exclusivo del módulo de **Programación de 1.º DAW**, manteniendo únicamente los conocimientos técnicos necesarios para construir MiniJarvis.

Objetivos concretos del bloque en curso:

1. eliminar todas las referencias curriculares y organizativas explícitas a Entornos de Desarrollo;
2. no crear ni exigir entregables específicos de ese módulo;
3. adaptar la temporalización al horario de Programación: **8 periodos semanales de 45 minutos**, distribuidos en **3 el martes, 2 el jueves y 3 el viernes**;
4. aplicar las correcciones aceptadas para H0, H1 y H2;
5. mantener como fuentes de verdad: diario, Scrum, GitHub, portfolio/Site y Moodle;
6. regenerar los derivados solo después de validar las fuentes Markdown.

## 2. Decisiones tomadas

### Alcance curricular

- MiniJarvis deja de ser un proyecto compartido y pasa a pertenecer únicamente a Programación.
- Solo se conservan prácticas necesarias para el proyecto: IntelliJ, Git, pruebas, depuración, documentación, Scrum, UML cuando apoye el código, reproducibilidad y seguridad.
- Esas prácticas no deben presentarse como RA, CE, horas, evaluación ni entregables de otro módulo.
- Se elimina el anexo curricular específico `01B-anexo-entornos-ra-ce.md`.
- Se elimina el PDF normativo específico de ese módulo.

### H0

- Prueba de estabilidad única: aproximadamente **50 g durante 60 segundos**, con dos pruebas comparables.
- Backlog mínimo único: **seis tareas**.
- La microprueba se materializa con dos fases:
  - individual;
  - pareja o trío aleatorio.
- Cada fase deja un artefacto breve; la microprueba no se mezcla con el backlog posterior de la torre.

### H1

- S212 se limita al alcance real de H1: leer el nombre con `Scanner`, guardarlo y mostrarlo.
- No añade conversión numérica, cálculo, comparaciones ni validación de entradas; esos contenidos pertenecen a H2.
- H1 ocupa **24 periodos de Programación**.
- Las fichas S206–S215 son checkpoints dentro de esos 24 periodos, no diez periodos totales.
- La defensa H1 es **individual y obligatoria**.

### H2

- Cada equipo debe documentar una incidencia:
  - natural, si aparece una adecuada;
  - didáctica reproducida, si no aparece una natural.
- La incidencia y la depuración se integran en una sola ficha con reproducción, breakpoint, variables, causa, corrección y prueba de regresión.
- La IA usa una declaración universal `Sí/No`; el detalle solo se completa si se utilizó.
- El refuerzo de bucles se integra en `docs/pruebas-h2`; no genera un documento independiente.
- S223 pasa a tratar el refuerzo de bucles y la elección de estructura de control.
- La comparación Java–Python se prepara en casa después de S226 y antes de S227, durante 30–45 minutos; S227 se usa para revisar y validar, y S228 puede incluirla en la defensa.

### Evidencias

- Diario: proceso individual.
- Scrum: proceso de equipo.
- GitHub: código, historial y versión.
- Portfolio/Site: selección y reflexión.
- Moodle: entrega, fecha, rúbrica y feedback.
- Los derivados no deben convertirse en evidencias adicionales.

## 3. Trabajo completado

### Migración inicial ya ejecutada

Se ejecutó:

```bash
python3 /tmp/migrate_minijarvis_programacion.py
```

La migración:

- sustituyó numerosas menciones generales al antiguo marco compartido;
- retiró referencias `ED RA...` mediante formulaciones técnicas;
- eliminó:
  - `02-PROFESORADO/00-PROGRAMACION-Y-COORDINACION/01B-anexo-entornos-ra-ce.md`;
  - `02-PROFESORADO/04-RECURSOS-NORMATIVOS-Y-TEMARIOS/Programación Didactica Entornos de Desarrollo 1º GS DAW.pdf`;
- renombró y modificó la presentación inicial:
  - eliminado: `02-PROFESORADO/03-PRESENTACIONES/00-presentacion-inicial-programacion-entornos.pptx`;
  - creado sin seguimiento: `02-PROFESORADO/03-PRESENTACIONES/00-presentacion-inicial-programacion.pptx`.

### Cambios semánticos ya aplicados

- H0: 60 segundos y seis tareas en la ficha principal y la guía antigua.
- S203 alumnado y docente: fases individual y pareja/trío materializadas.
- S212 alumnado y docente: reducido a lectura de nombre con `Scanner`.
- S223 alumnado y docente: título y evidencia de refuerzo de bucles corregidos.
- S226 alumnado y docente: incidencia natural o didáctica reproducida.
- S227 alumnado y docente: comparación preparada en casa y revisada en clase.
- S228 alumnado: declaración universal de IA.
- `04A-enunciados-y-entregables-alumnado.md`:
  - defensa H1 obligatoria;
  - incidencia y depuración H2 combinadas;
  - declaración de IA.
- `14B-ficha-alumnado-h2-decisiones-depuracion.md`:
  - estructura combinada de incidencia y depuración;
  - checklist de incidencia obligatoria;
  - declaración `Sí/No` de IA.
- `incidencia-h2-plantilla.md`: añadidos origen, breakpoint, variables y regresión.
- Calendario:
  - horario semanal corregido a martes 3, jueves 2, viernes 3;
  - H0 fijado en ocho periodos;
  - tabla global convertida a Programación;
  - H1 distribuido en 24 periodos y diez checkpoints;
  - defensa H1 declarada obligatoria;
  - H2 actualizado con incidencia/depuración combinadas.
- Guías H1:
  - `24-guia-docente-h1-sesiones-autonomas.md`;
  - `13-guia-docente-h1-primer-asistente.md`;
  ahora usan la temporalización de 24 periodos y S206–S215.

## 4. Estado actual

Repositorio:

```text
Ruta: /mnt/compartido/Programación-26-27/Minijarvis
Rama: refactor/hitos-v3
```

Último estado comprobado:

```text
110 archivos versionados modificados/eliminados
470 inserciones
997 eliminaciones
```

Elementos sin seguimiento visibles:

```text
.hermes.md
02-PROFESORADO/03-PRESENTACIONES/00-presentacion-inicial-programacion.pptx
docs/
CONTINUIDAD_MINIJARVIS.md   # creado en este punto
```

Precauciones:

- `.hermes.md` y `docs/hermes/` contienen instrucciones/contexto de Hermes; no deben borrarse ni incorporarse automáticamente a un commit.
- No se ha hecho commit ni push.
- No se han regenerado todavía HTML, presentaciones de sesiones, paquetes Moodle, copias Drive ni manifiesto final.
- No se han ejecutado todavía las pruebas tras el conjunto de cambios.
- El cambio es amplio y aún contiene sustituciones mecánicas que necesitan revisión editorial.

### Referencias explícitas aún pendientes

La última búsqueda encontró **27 archivos Markdown** con coincidencias de:

```regex
Entornos de Desarrollo|Programación y Entornos|Programación \+ Entornos|\bEntornos\b|\bED RA\d|\bED-H
```

Entre los archivos principales pendientes están:

- `02-PROFESORADO/00-PROGRAMACION-Y-COORDINACION/00-mapa-maestro-curso-2026-2027.md`;
- `01-matriz-integrada-ra-ce-evidencias-tareas.md`;
- `02-calendario-hitos-sprints-2026-2027.md`;
- `06-rubricas-hitos.md`;
- `200A-guia-docente-integral-plan-clases-scrum-hexa.md`;
- `200B-plan-sesion-a-sesion-201-en-adelante.md`;
- `31-guia-docente-hf-sesiones-autonomas.md`;
- varias guías de H0–H7 y HF;
- S303 alumnado/docente;
- libro del alumnado y ejemplos privados.

También queda una referencia en:

```text
generar_presentaciones_sesiones.py
```

El manifiesto conserva todavía la ruta antigua de la presentación y deberá regenerarse.

## 5. Archivos y rutas relevantes

### Fuentes prioritarias

```text
01-ALUMNADO/00-EMPIEZA-AQUI/04A-enunciados-y-entregables-alumnado.md
01-ALUMNADO/02-HITOS/h0-torre-papel-scrum/12-ficha-alumnado-torre-papel-scrum.md
01-ALUMNADO/03-SESIONES/h0/S203-microprueba-y-equipos-provisionales-de-3-o-4-alumnado.md
01-ALUMNADO/03-SESIONES/h1/S212-entrada-por-teclado-con-scanner-alumnado.md
01-ALUMNADO/02-HITOS/h2-decisiones-depuracion/14B-ficha-alumnado-h2-decisiones-depuracion.md
01-ALUMNADO/02-HITOS/h2-decisiones-depuracion/plantillas/incidencia-h2-plantilla.md
01-ALUMNADO/03-SESIONES/h2/S223-switch-como-alternativa-controlada-alumnado.md
01-ALUMNADO/03-SESIONES/h2/S226-incidencias-y-correccion-de-errores-alumnado.md
01-ALUMNADO/03-SESIONES/h2/S227-comparacion-java-python-h2-alumnado.md
01-ALUMNADO/03-SESIONES/h2/S228-demo-defensa-y-cierre-h2-alumnado.md
```

### Coordinación y temporalización

```text
02-PROFESORADO/00-PROGRAMACION-Y-COORDINACION/00-mapa-maestro-curso-2026-2027.md
02-PROFESORADO/00-PROGRAMACION-Y-COORDINACION/01-matriz-integrada-ra-ce-evidencias-tareas.md
02-PROFESORADO/00-PROGRAMACION-Y-COORDINACION/01A-anexo-programacion-ra-ce.md
02-PROFESORADO/00-PROGRAMACION-Y-COORDINACION/02-calendario-hitos-sprints-2026-2027.md
02-PROFESORADO/00-PROGRAMACION-Y-COORDINACION/24-guia-docente-h1-sesiones-autonomas.md
02-PROFESORADO/00-PROGRAMACION-Y-COORDINACION/25-guia-docente-h2-sesiones-autonomas.md
```

### Guías docentes paralelas

```text
02-PROFESORADO/01-GUIAS-POR-HITO/h0-torre-papel-scrum/03-primera-semana-scrum-torre-papel.md
02-PROFESORADO/01-GUIAS-POR-HITO/h1-primer-asistente/13-guia-docente-h1-primer-asistente.md
02-PROFESORADO/01-GUIAS-POR-HITO/h2-decisiones-depuracion/14-guia-docente-h2-decisiones-depuracion.md
02-PROFESORADO/02-SESIONES/h0/S203-microprueba-y-equipos-provisionales-de-3-o-4-docente.md
02-PROFESORADO/02-SESIONES/h1/S212-entrada-por-teclado-con-scanner-docente.md
02-PROFESORADO/02-SESIONES/h2/S223-switch-como-alternativa-controlada-docente.md
02-PROFESORADO/02-SESIONES/h2/S226-incidencias-y-correccion-de-errores-docente.md
02-PROFESORADO/02-SESIONES/h2/S227-comparacion-java-python-h2-docente.md
```

### Generadores y validación

```text
exportar_alumnado_html.py
generar_presentaciones_sesiones.py
generar_manifiesto.py
generar_paquetes.py
limpiar_material_alumnado.py
generar_evidencias_laura.py
tests/test_generar_presentaciones_sesiones.py
tests/test_modelo_hexa.py
```

### Scripts temporales de esta migración

```text
/tmp/migrate_minijarvis_programacion.py       # ya ejecutado
/tmp/finalize_programacion_only.py            # escrito, NO ejecutado
```

No ejecutar `finalize_programacion_only.py` a ciegas. Hace sustituciones globales de `Entornos` por `prácticas técnicas`, elimina la plantilla separada de depuración H2 y puede producir redacción deficiente o duplicados. Debe revisarse antes o sustituirse por parches controlados.

## 6. Comandos importantes

Como la ruta contiene `ó`, el backend puede bloquearla como `workdir`. Usar `/mnt/compartido` y descubrir el repositorio:

```bash
repo=$(printf '%s\n' */Minijarvis | head -n1)
cd "$repo"
pwd
git rev-parse --show-toplevel
git branch --show-current
git status --short
git diff --stat
git diff --check
```

Buscar referencias explícitas en fuentes de texto:

```bash
python3 - <<'PY'
from pathlib import Path
import re
r = next(Path('/mnt/compartido').glob('*/Minijarvis'))
rx = re.compile(r'Entornos de Desarrollo|Programación y Entornos|Programación \\+ Entornos|\\bEntornos\\b|\\bED RA\\d|\\bED-H', re.I)
for p in r.rglob('*'):
    if not p.is_file() or p.suffix.lower() not in {'.md', '.py', '.txt', '.json', '.csv'}:
        continue
    for n, line in enumerate(p.read_text(encoding='utf-8', errors='ignore').splitlines(), 1):
        if rx.search(line):
            print(f'{p.relative_to(r)}:{n}:{line.strip()}')
PY
```

Búsquedas funcionales que deben quedar sin contradicciones:

```bash
rg -n "10 segundos|al menos cinco|mínimo de cinco" .
rg -n "conversión numérica|dato válido|dato inválido|cálculo" 01-ALUMNADO/03-SESIONES/h1 02-PROFESORADO/02-SESIONES/h1
rg -n "incidencia.*si apareció|registro IA si procede|refuerzo-bucles-h2" .
rg -n "lunes: 2|jueves: 3|Entornos: [0-9]+ periodos" .
```

Usar `search_files` en vez de `rg` cuando se trabaje mediante herramientas Hermes.

## 7. Problemas encontrados y soluciones

### Ruta con caracteres acentuados

Problema:

```text
Blocked: workdir contains disallowed character 'ó'.
```

Solución:

- usar `/mnt/compartido` como `workdir`;
- localizar la carpeta con `*/Minijarvis`;
- entrar después con `cd "$repo"`.

### Falta de `python-pptx`

El primer intento de migración falló porque `pptx` no estaba instalado.

Solución aplicada:

- se modificó `/tmp/migrate_minijarvis_programacion.py` para editar el PPTX como ZIP/XML con la biblioteca estándar;
- el segundo intento terminó con `migration complete`.

### Sustitución global demasiado amplia

La migración inicial corrigió muchas referencias, pero dejó redacciones mecánicas o incoherentes, por ejemplo:

- encabezados duplicados `Programación:`;
- formulaciones como `Programación mantienen`;
- tablas que todavía conservan columnas o etiquetas del antiguo módulo;
- referencias técnicas transformadas sin revisión editorial.

Solución pendiente:

- revisar cada uno de los 27 archivos restantes;
- mantener el conocimiento técnico útil, pero eliminar su clasificación curricular externa;
- no ejecutar otra sustitución global sin inspeccionar el diff.

### Derivados desactualizados

La presentación inicial nueva existe, pero:

- el manifiesto aún menciona el nombre anterior;
- HTML, Moodle y Drive todavía no se han regenerado;
- las presentaciones de sesiones no reflejan todavía todos los cambios.

Solución pendiente:

- validar primero Markdown y scripts;
- ejecutar generadores;
- regenerar manifiesto al final.

## 8. Tareas pendientes

1. Revisar el diff completo de los 110 archivos y corregir redacciones mecánicas.
2. Eliminar las referencias explícitas restantes de los 27 Markdown y de `generar_presentaciones_sesiones.py`.
3. Reescribir, no solo sustituir, las secciones específicas del antiguo módulo en:
   - mapa maestro;
   - matriz integrada;
   - rúbricas;
   - guía integral;
   - plan sesión a sesión;
   - recuperación final.
4. Decidir si `01-matriz-integrada-ra-ce-evidencias-tareas.md` conserva el nombre histórico o se renombra a una matriz exclusiva de Programación; si se renombra, actualizar todos los enlaces.
5. Consolidar H2:
   - eliminar de forma controlada la plantilla separada `depuracion-h2-plantilla.md` y el ejemplo correspondiente, o convertirlos en redirección;
   - revisar todos los enlaces a `docs/depuracion-h2`;
   - evitar entradas duplicadas tras apuntar a `docs/incidencia-h2`.
6. Completar la declaración universal de IA H2 en ficha, plantillas, Moodle, rúbrica y guía docente.
7. Revisar todas las copias de H0 para confirmar 50 g, 60 segundos, dos pruebas y seis tareas.
8. Revisar S212 en alumnado, docente, presentaciones, guía H1 y tareas Moodle.
9. Revisar H1 para que 24 periodos, diez checkpoints y defensa obligatoria sean coherentes en todos los documentos.
10. Explicar también en H2 la diferencia entre 28 periodos oficiales y 13 fichas ancla; los restantes son talleres sin evidencia nueva.
11. Revisar el calendario completo y eliminar columnas, totales y reparto del antiguo módulo.
12. Regenerar:
    - presentaciones de sesiones;
    - `01-ALUMNADO-HTML`;
    - paquetes Moodle;
    - copias Drive si existe un flujo reproducible;
    - `MANIFIESTO-ARCHIVOS.md`.
13. Buscar referencias dentro de PPTX, XLSX, HTML, ZIP y PDF, no solo Markdown.
14. Ejecutar pruebas, `git diff --check`, revisión de enlaces y `git status`.
15. Actualizar `docs/hermes/ESTADO-ACTUAL.md` e informe diario únicamente cuando el bloque esté validado.

## 9. Siguiente paso exacto

No regenerar todavía.

Primero ejecutar una revisión controlada de las referencias restantes:

1. abrir `/tmp/finalize_programacion_only.py` solo como lista de transformaciones propuestas;
2. **no ejecutarlo tal como está**;
3. corregir mediante parches los documentos troncales, en este orden:
   - `00-mapa-maestro-curso-2026-2027.md`;
   - `01-matriz-integrada-ra-ce-evidencias-tareas.md`;
   - `02-calendario-hitos-sprints-2026-2027.md`;
   - `06-rubricas-hitos.md`;
   - `200A-guia-docente-integral-plan-clases-scrum-hexa.md`;
   - `200B-plan-sesion-a-sesion-201-en-adelante.md`;
4. repetir la búsqueda global;
5. corregir después las guías y sesiones restantes;
6. solo cuando las fuentes queden limpias y coherentes, ejecutar los generadores y las pruebas.
