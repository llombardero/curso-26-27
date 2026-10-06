# Auditoría de cierre GLOBAL + H1 previa a H2

## Veredicto

**APTO PARA INICIAR H2**

## 1. Rama y commit base

- Rama: `final-calidad-simplificada`.
- Commit base y `HEAD`: `c72af29fcb54ca6a6b153821e5c53adc8f0ac8fc`.
- No se hizo commit ni push.

## 2. Estado previo

El cierre partió del árbol sucio preservado por las fases 1–4: 46 archivos versionados modificados y tres rutas sin seguimiento (`.obsidian/`, `tests/__pycache__/` y `tests/test_contrato_global_h1_pre_h2.py`). La fase 4 había dejado 332 tests superados y un único fallo: solo existían cinco de los siete ZIP definidos.

## 3. Decisiones docentes

- Contrato H1 único: programa Java secuencial con entrada textual, conversión numérica, cálculo, comparación booleana observable y salida.
- La comparación no gobierna instrucciones. `if`, `if/else`, bifurcaciones, menús y bucles quedan para H2.
- Evidencia mínima: GitHub/README, versión estable en Moodle y defensa; diario, Scrum y Drive solo cuando proceda.
- RA7–RA9 permanece como `PENDIENTE DE DECISIÓN DOCENTE / VALIDACIÓN NORMATIVA`, sin aplicar silenciosamente una regla no aprobada.

## 4. Archivos modificados en este cierre

- Regenerado `MANIFIESTO-ARCHIVOS.md`.
- Reconstruidos los siete paquetes definidos por `generar_paquetes.py`: cinco ZIP versionados y dos ZIP locales ignorados por Git.
- Creado este informe en la ubicación raíz ya utilizada para informes de auditoría y calidad.
- No se modificaron fuentes docentes, HTML, presentaciones, generadores ni tests durante esta fase final.

## 5. Producto H1 final

`Main.java` usa `Scanner.nextLine()`, convierte la entrada numérica, calcula, produce y muestra un `boolean` y mantiene ejecución secuencial. Compila en salida aislada y, con `Laura` y `4`, muestra `5` y `true`. No deja `.class` en `src`.

## 6. Frontera H1/H2

H1 no exige control de flujo, ramas, menús ni bucles. Estos contenidos permanecen expresamente fuera del producto obligatorio y pasan a H2.

## 7. HEXA

La metodología activa conserva `Fase 0 — Equipos` como dimensión transversal y seis fases: Activar, Investigar, Idear, Planificar, Ejecutar y Comunicar.

## 8. Tests y validadores

- Suite completa: `333 passed`.
- `validar_simplificacion.py`: PASS; cero enlaces Markdown rotos, cero errores semánticos, cero secretos detectados, siete ZIP íntegros y cero ejemplos privados en Moodle.
- Compilación y ejecución H1: PASS.
- Integridad y paridad ZIP/árbol: PASS para los siete paquetes; cero entradas ausentes, sobrantes, corruptas, temporales o con hash distinto.
- `git diff --check`: código 0.
- No se repitieron generación, conversión PDF ni inspección visual de presentaciones: desde la validación exhaustiva de fase 4 no cambiaron sus fuentes, generador ni PPTX.

## 9. Presentaciones

Las cinco presentaciones H1 afectadas (S206, S211, S212, S214 y S215) corresponden a sus fuentes según la fase 4. Sus 115 diapositivas fueron reabiertas, convertidas e inspeccionadas; los PPTX actuales no cambiaron después de esa validación.

## 10. Moodle/HTML

La tarea Moodle es única y coherente entre fuente Markdown, HTML y copia privada de entrega. Los HTML GLOBAL/H1 afectados fueron regenerados en fase 4. El validador final confirma cero enlaces rotos y cero ejemplos privados en Moodle.

## 11. ZIP

La fuente vigente exige **siete paquetes**: `generar_paquetes.py` define siete mapeos y el README enumera los mismos siete. La aparente contradicción de cinco frente a siete se debía a que `Minijarvis-profesorado.zip` y `Minijarvis-presentaciones-sesiones.zip` están ignorados por Git y no existían localmente; no era un contrato de cinco paquetes ni una expectativa histórica aislada.

Se reconstruyeron únicamente esos siete ZIP. Cada archivo interno coincide por ruta y SHA-256 con su árbol actual. Por ello ficha H1, `Main.java`, guía GitHub vigente, guion H1, tarea Moodle, HTML y presentaciones proceden de las versiones actuales. No aparecen rutas retiradas ni temporales.

## 12. Manifiesto

Generado después de los ZIP, desde las tres raíces fuente definidas por `generar_manifiesto.py`.

- 556 entradas.
- 0 rutas inexistentes.
- 0 rutas vigentes ausentes.
- 0 hashes incorrectos.
- 0 duplicados.
- 0 rutas sustituidas/retiradas.
- 0 incoherencias con los ZIP fuente correspondientes.

## 13. Pendientes docentes

- `PENDIENTE DE DECISIÓN DOCENTE / VALIDACIÓN NORMATIVA`: clasificación, obligatoriedad, profundidad, peso, recuperación y efectos de superación de RA7–RA9.
- `PENDIENTE DE DECISIÓN DOCENTE`: correspondencia entre 33 periodos de calendario y las diez sesiones S206–S215.

Ninguno bloquea técnicamente el inicio de H2 bajo el contrato vigente.

## 14. Estado Git y puerta H2

Puertas A–J: PASS. Existe un contrato H1 único; la frontera H1/H2 está preservada; conversión y cálculo aparecen en producto e instrumentos; HEXA usa Fase 0 y seis fases; Moodle es coherente; Java compila y ejecuta; presentaciones y ZIP corresponden a fuentes; el manifiesto es correcto; el validador no detecta secretos.

El árbol continúa sucio de forma deliberada: conserva el trabajo acumulado de las fases 1–4, añade manifiesto y cinco ZIP versionados regenerados, mantiene dos ZIP generados ignorados y añade este informe sin seguimiento. No se alteraron `.obsidian/`, `tests/__pycache__/` ni el test sin seguimiento preexistente.
