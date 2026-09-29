# Informe de corrección y auditoría Hermes — MiniJarvis

Fecha de cierre: 2026-09-29 13:37 +0200
Repositorio: `/mnt/compartido/Programación-26-27/Minijarvis`
Rama: `reducida`

## 1. Resultado ejecutivo

Se corrigieron las incoherencias heredadas de la simplificación global y se regeneraron los materiales desde sus fuentes. El resultado mantiene el modelo documental mínimo: GitHub/README como evidencia técnica desde H1, un diario individual evolutivo, un Scrum evolutivo por equipo, Drive operativo, Moodle como registro de entrega, Sites solo en C1/C2/HF y defensa individual para acreditar autoría.

La verificación final obtiene:

- 37 pruebas superadas;
- 106 parejas alumnado/docente con modalidad explícita y coincidente;
- 106 presentaciones legibles y con la modalidad canónica;
- 0 enlaces Markdown rotos;
- 0 incoherencias semánticas detectadas;
- 0 posibles secretos detectados;
- 0 ejemplos privados de Laura en Moodle;
- RA1-RA9 preservados;
- 7 ZIP íntegros.

## 2. Hallazgos corregidos

### 2.1. Ejemplos privados de Laura

El generador anterior reproducía cinco documentos por hito, creaba diarios y Scrum repetidos, Sites H0-H7, entregas Moodle sobredimensionadas y carpetas `docs/` paralelas. Además dependía de hojas XLSX que ya no pertenecían al modelo simplificado.

Se reescribió `generar_evidencias_laura.py` y se regeneró `03-EJEMPLOS-LAURA-PRIVADOS/`:

- 166 archivos anteriores reducidos a 72;
- un diario y un Scrum en `FUENTES-CURSO/`;
- 9 entregas Moodle mínimas en `ENTREGAS-MOODLE/`;
- 6 páginas de ejemplo en `PORTFOLIOS-PERIODICOS/`: personal/equipo para C1, C2 y HF;
- README técnicos por hito, con código, pruebas, decisiones y defensa integrados;
- 0 carpetas `docs/`;
- 0 carpetas `evidencias-digitales/`;
- H0 sin GitHub, tag ni Sites;
- ejemplos completos mantenidos fuera de Moodle.

### 2.2. Modalidad de las sesiones

Se auditó el contenido de S201-S306 y se añadió la modalidad a las 106 fichas de alumnado y sus 106 guías docentes. La distribución final es:

| Modalidad | Sesiones |
|---|---:|
| Individual | 23 |
| Equipo | 51 |
| Parejas | 2 |
| Individual → puesta en común en equipo | 18 |
| Equipo → comprobación individual | 12 |

Las sesiones con transición explicitan el orden del trabajo. Las defensas y demos separan el producto compartido de la comprobación individual. Los casos críticos S204, S215, S240, S257, S274, S291, S296, S304 y S306 tienen una modalidad coherente con su actividad evaluativa.

La tabla interna reproducible se encuentra en:

`02-PROFESORADO/00-PROGRAMACION-Y-COORDINACION/32-tabla-control-modalidades-sesiones.md`

### 2.3. Fuentes generales y guías por hito

Se corrigieron:

- la guía de Drive, para eliminar el espejo por hitos y reservarlo a enlaces, Scrum y evidencia no-code excepcional;
- las guías generales de proyecto e IA, retirando `docs/registro-ia`, portfolios por hito y capturas rutinarias;
- H1-H7 y HF en las guías por hito, sustituyendo tablas de plantillas por evidencias canónicas;
- checklists e instrucciones internas que todavía reintroducían documentos paralelos;
- HF, para utilizar repositorio, Sites, defensa y recuperación concreta, sin siete documentos finales nuevos;
- la separación entre Programación y la coordinación opcional con Entornos en los materiales dirigidos al alumnado.

Las cabeceras integradas que permanecen en `00-PROGRAMACION-Y-COORDINACION` corresponden a documentos internos de coordinación curricular, no a entregas mixtas del alumnado.

### 2.4. Presentaciones

`generar_presentaciones_sesiones.py` se corrigió para leer `Modalidad` como metadato canónico y conservar `Agrupamiento` solo como compatibilidad. También se retiró del pie de las presentaciones la mezcla automática con Entornos.

Durante la verificación ad hoc se detectó primero que S241 y después S201 no trasladaban la modalidad canónica al PPTX. La causa era la prioridad del campo histórico `Agrupamiento`. Tras invertir esa prioridad, se regeneraron las 106 presentaciones y se añadió una prueba de regresión que compara cada PPTX con su ficha fuente.

## 3. Artefactos regenerados

Se ejecutaron los generadores del repositorio en orden de dependencia:

1. `generar_evidencias_laura.py`;
2. `exportar_alumnado_html.py`;
3. `generar_presentaciones_sesiones.py`;
4. `generar_paquetes.py`;
5. `generar_manifiesto.py`.

Inventario final:

| Ámbito | Archivos |
|---|---:|
| `01-ALUMNADO` | 161 |
| `01-ALUMNADO-HTML` | 163 |
| `02-PROFESORADO` | 322 |
| `03-EJEMPLOS-LAURA-PRIVADOS` | 72 |
| `04-DRIVE-5-EQUIPOS` | 19 |
| `05-PAQUETE-MOODLE` | 174 |
| Presentaciones por sesión | 106 |
| ZIP | 7 |

Los 23 PDF normativos o temáticos se conservaron como fuentes y no se regeneraron.

## 4. Verificación

### Suite del repositorio

```text
37 passed in 3.54s
```

La suite comprueba, entre otros aspectos:

- estructura reducida de hitos;
- 106 sesiones sin bloques administrativos automáticos;
- libros XLSX maestros;
- Drive operativo y Moodle sin ejemplos privados;
- paridad Markdown/HTML;
- 106 PPTX legibles y con modalidad canónica;
- 7 ZIP íntegros y sin cachés;
- modalidades, distribución y sesiones críticas;
- arquitectura mínima de Laura;
- contratos Moodle de Laura;
- ausencia de rutas documentales obsoletas;
- semántica de las guías GitHub/Drive.

### Auditoría reproducible

`validar_simplificacion.py` finalizó con código 0:

- `broken_markdown_links`: vacío;
- `curricular_tokens_preserved`: verdadero;
- `secret_hits`: vacío;
- `zip_errors`: vacío;
- `zip_count`: 7;
- `semantic_errors`: vacío;
- `private_example_files_in_moodle`: vacío.

### Verificación ad hoc

Se creó un verificador temporal bajo `/tmp` con prefijo `hermes-verify-`. El primer pase encontró el defecto real de modalidad en presentaciones. Tras corregir el parser y regenerar, el pase final devolvió:

```text
AD-HOC PASS: sintaxis; 106 modalidades emparejadas; 106 PPTX con modalidad canónica; Laura mínima; 7 ZIP; auditoría semántica
CLEANUP PASS: temporary verifier removed
```

Esta comprobación es ad hoc y complementa, no sustituye, la suite del repositorio.

También pasaron `git diff --check` para fuentes y derivados antes de cada commit.

## 5. Commits locales

- `b9cca1c` — `Corregir evidencias, modalidades y ejemplos privados`
- `24bc346` — `Regenerar materiales tras la auditoria de evidencias`

Este informe se confirma en un tercer commit local independiente.

## 6. Límites y contenido preservado

- No se realizó `push` ni merge.
- No se modificaron otras ramas.
- No se incluyeron credenciales ni valores sensibles.
- Los avisos de Pandoc sobre títulos HTML utilizan el nombre del documento como valor por defecto y no impiden la generación.
- Los duplicados de Drive son copias operativas esperadas del Scrum y de los LEEME por equipo; Moodle no contiene grupos de duplicados exactos.
- Se preservaron sin seguimiento `.obsidian/`, `__pycache__/` y `tests/__pycache__/`.
- También se preservaron, sin incluir en los commits, dos presentaciones raíz, sus dos guiones y el bloqueo de LibreOffice que aparecieron durante la ejecución; no pertenecen al pipeline auditado.
