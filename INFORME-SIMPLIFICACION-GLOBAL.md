# Informe de simplificación global de MiniJarvis

Fecha de cierre: 29 de septiembre de 2026
Rama: `reducida`

## 1. Resultado ejecutivo

Se ha sustituido el modelo de “una plantilla, captura o informe por sesión/hito” por un modelo canónico de producto y proceso:

- GitHub + README desde H1 para código, pruebas, ejecución, diseño y trazabilidad técnica.
- Diario individual solo cuando existe aprendizaje, decisión, bloqueo o uso significativo de IA.
- Scrum de equipo para backlog, acuerdos, decisiones/bloqueos, review y retrospectiva.
- Drive únicamente para enlaces, Scrum y evidencia no-código excepcional.
- Sites personal y de equipo solo en C1, C2 y HF.
- Moodle para distribuir progresivamente, recibir una entrega mínima por hito y centralizar calificación.
- Defensa para comprobar autoría; no genera un documento paralelo.

No se ha rebajado el nivel técnico: se mantienen programación, pruebas, depuración, Git, UML de clases, persistencia, seguridad, refactorización, patrones, comparaciones Java-Python e IA responsable. Se ha eliminado su duplicación documental.

## 2. Auditoría antes/después

| Área | Antes | Después | Variación |
|---|---:|---:|---:|
| `01-ALUMNADO` | 241 | 161 | -80 (-33,2 %) |
| `02-PROFESORADO` | 321 | 321 | 0 |
| `04-DRIVE-5-EQUIPOS` | 274 | 19 | -255 (-93,1 %) |
| `05-PAQUETE-MOODLE` | 261 | 174 | -87 (-33,3 %) |

La estabilidad del número docente no oculta duplicación: se conservan 106 guías y 106 presentaciones porque son materiales de uso real; se retiraron plantillas maestras redundantes y se añadió una guía operativa H1. Drive deja de ser una copia de Moodle/HTML.

## 3. Cambios curriculares y por fase

- H0: solo Scrum, review/retrospectiva y defensa oral; sin GitHub, tags ni páginas H0 en Sites.
- H1: guía docente específica; GitHub se introduce como repositorio canónico.
- H2: pruebas y depuración se integran en código/README; no hay informes separados.
- H3: cierre técnico y selección C1 de H1-H3; no existe portfolio H3 independiente.
- H4: diagrama de clases ligado al código; el diagrama de comportamiento queda como práctica opcional coordinada de Entornos (RA6), no entrega obligatoria de Programación.
- H5: Git/PR, refactorización y patrón usado o descartado quedan en el repositorio/README; selección C2 de H4-H5.
- H6: persistencia, logs, errores y seguridad se integran en código/README; sin portfolio H6.
- H7: alcance, integración/simulación, seguridad de prompts y validación humana; trazabilidad significativa en diario/Scrum.
- HF: release/tag final, Sites personal/equipo, demo y defensa; recuperación solo si procede.

El conjunto curricular detectado antes y después sigue siendo `RA1`–`RA9`. La documentación normativa y de coordinación no se eliminó.

## 4. Sesiones y presentaciones

- 106 fichas de alumnado conservadas.
- 106 guías docentes conservadas.
- 106 presentaciones regeneradas y validadas (`PASS`).
- 102 bloques residuales “Evidencia mínima antes de salir” retirados tras detectar que estaban separados del bloque “Registro breve”.
- 0 bloques automáticos “Registro breve” o “Evidencia mínima antes de salir” al cierre.
- 59 destinos `docs/...` sustituidos por README/repositorio, historial/PR, diario seleccionable o práctica opcional de Entornos.
- 106 enlaces del índice de sesiones corregidos añadiendo la extensión `.md` cuando el destino existía.

## 5. Plantillas y hojas de cálculo

Se eliminaron 65 plantillas específicas por hito y 15 plantillas globales redundantes. Cada hito queda con README, ficha principal y entrega digital; los modelos transversales viven en las guías del ecosistema.

Libros maestros finales:

- Diario: 2 pestañas, 7 columnas principales; sin una fila obligatoria por sesión.
- Scrum: 7 pestañas operativas (`EQUIPO_Y_ACUERDOS`, `BACKLOG_OPERATIVO`, `DECISIONES_Y_BLOQUEOS`, `REVIEW`, `RETROSPECTIVA`, `IA_EQUIPO`, `INSTRUCCIONES`).
- Se eliminan control docente, catálogo masivo de evidencias, enlace por sesión y exportación PDF/XLSX obligatoria.

## 6. Drive, Moodle y ejemplos

Drive contiene 19 archivos. Sus únicos duplicados exactos son copias operativas deliberadas: una hoja Scrum y dos LEEME por cada uno de los cinco equipos. No contiene HTML, presentaciones ni una segunda copia del material didáctico.

Moodle contiene 174 archivos, sin grupos de duplicados exactos internos y sin ejemplos privados. Incluye recursos HTML para publicación progresiva y una tarea mínima por H0-H7/HF. H0 no pide GitHub/tag/Sites; H1-H7 piden tag/release, URL del repositorio y una frase; HF añade Sites y defensa.

Los ejemplos completos de Laura permanecen únicamente en el área privada docente y en `Minijarvis-ejemplos-Laura-privados.zip`; no se incluyen en alumnado ni Moodle.

## 7. Artefactos regenerados

| ZIP | Archivos | Tamaño |
|---|---:|---:|
| `Minijarvis-alumnado-html.zip` | 163 | 296 853 B |
| `Minijarvis-alumnado.zip` | 161 | 225 464 B |
| `Minijarvis-drive-5-equipos.zip` | 19 | 63 457 B |
| `Minijarvis-ejemplos-Laura-privados.zip` | 166 | 299 395 B |
| `Minijarvis-paquete-moodle.zip` | 174 | 324 206 B |
| `Minijarvis-presentaciones-sesiones.zip` | 107 | 3 538 936 B |
| `Minijarvis-profesorado.zip` | 321 | 105 910 830 B |

Los siete ZIP pasan `ZipFile.testzip()` sin errores. Los dos ZIP grandes de profesorado/presentaciones se generan localmente pero siguen ignorados por Git conforme a `.gitignore`; los otros cinco están versionados.

Los PDF/temarios fuente permanecen intactos. No se generó un PDF curricular inexistente: la rama no contiene un generador de PDF propio. El paquete HTML evita distribuir de golpe los PDF pesados, coherente con la publicación progresiva.

## 8. Validación

Comandos principales:

```bash
/home/llombardero/.hermes/venvs/tools/bin/python -m pytest -q
python3 validar_simplificacion.py
python3 exportar_alumnado_html.py
/home/llombardero/.hermes/venvs/tools/bin/python generar_presentaciones_sesiones.py
/home/llombardero/.hermes/venvs/tools/bin/python generar_paquetes.py
python3 generar_manifiesto.py
git diff --check
```

Resultado final:

- 31 pruebas superadas.
- 0 enlaces Markdown rotos.
- 0 posibles secretos detectados.
- 0 directorios `plantillas/` por hito.
- 0 ejemplos privados en Moodle.
- 0 errores ZIP.
- paridad fuente HTML comprobada, salvo el índice adicional esperado `LEEME-ALUMNADO.html`.
- currículo `RA1`–`RA9` preservado.

## 9. Commits locales

- `a763d13` — Simplificar evidencias y flujo operativo del curso.
- `63f638c` — Regenerar materiales y paquetes simplificados.

La carpeta `.obsidian/` y los directorios `__pycache__/` ya no forman parte del alcance y no se han añadido a los commits.
