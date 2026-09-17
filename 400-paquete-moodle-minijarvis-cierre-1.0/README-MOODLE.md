# Paquete Moodle — MiniJarvis 1.º DAW 2026/2027

Versión: cierre curricular 1.0 — julio 2026

Este paquete está preparado para publicar el curso por secciones o temas en **Moodle Centros Andalucía**. No sustituye al repositorio completo: es una maqueta limpia para publicación docente.

Antes de configurar el aula, consulta:

`GUIA-MOODLE-CENTROS-ANDALUCIA.md`

La guía explica el acceso con IdEA, la creación del aula mediante Gestión de aulas, la sincronización con Séneca, la configuración de grupos y tareas, la publicación progresiva H0–HF, la protección de HADA y el procedimiento de copia de seguridad.

> El ZIP de este paquete no es una copia restaurable `.mbz`. La copia `.mbz` debe generarse desde Moodle Centros después de construir y comprobar el aula.

## Política de publicación

```text
El libro del alumnado se publica por capítulos asociados a cada hito.
Los ejemplos de Laura se publican después del intento propio del alumnado o tras una primera versión defendible.
```

## Estructura recomendada en Moodle

| Sección Moodle | Carpeta del paquete | Uso |
|---|---|---|
| 00. Presentación del curso | `01-documentos-base/` | Mapa, guía alumnado, política IA y rúbricas. |
| 01. Libro por hitos | `02-libro-alumnado-por-hitos/` | Publicar solo el bloque correspondiente al hito actual. |
| 02. Hitos y entregas | `03-hitos-fichas-plantillas-checklists/` | Fichas, checklists y plantillas de entrega. |
| 03. Guías docentes | `04-guias-docentes-autonomas/` | Uso del profesorado; no publicar íntegramente al alumnado salvo decisión expresa. |
| 04. Ejemplos modelo Laura | `05-ejemplos-laura-mostrar-despues/` | Ocultar inicialmente; mostrar después del intento propio. |
| 05. Plantillas globales | `06-plantillas-globales/` | Plantillas transversales de portfolio, defensa, IA, pruebas, etc. |

## Particularización para Moodle Centros Andalucía

Configuración recomendada:

```text
Acceso del profesorado: IdEA
Creación del aula: bloque Gestión de aulas
Origen de grupos oficiales: Séneca
Formato del curso: temas organizados por hitos H0–HF
Ejemplos de Laura: ocultos hasta el intento propio
Guías docentes: fuera de la vista del alumnado
Copia reutilizable: .mbz generada desde la plataforma
Soporte corporativo: CAUCE
```

Al comenzar 2026/2027 deben comprobarse en la instancia real la versión de Moodle, los complementos disponibles, los límites de subida y el comportamiento vigente de la sincronización.

## Orden sugerido de publicación del libro

| Momento | Carpeta |
|---|---|
| Inicio / H0-H1 | `02-libro-alumnado-por-hitos/00-inicio-h0-h1/` |
| H2 | `02-libro-alumnado-por-hitos/01-h2-decisiones-bucles-pruebas/` |
| H3 | `02-libro-alumnado-por-hitos/02-h3-colecciones-memoria/` |
| H4 | `02-libro-alumnado-por-hitos/03-h4-poo-uml/` |
| H5 | `02-libro-alumnado-por-hitos/04-h5-interfaces-patrones/` |
| H6 | `02-libro-alumnado-por-hitos/05-h6-persistencia-logs/` |
| H7 | `02-libro-alumnado-por-hitos/06-h7-ia-responsable/` |
| HF | `02-libro-alumnado-por-hitos/07-hf-portfolio-defensa/` |
| Solo profesorado | `02-libro-alumnado-por-hitos/99-docente-revision-editorial/` |

## Reglas de uso de Laura

```text
1. No publicar Laura como solución inicial.
2. Pedir primero intento propio, evidencia o versión defendible.
3. Usar Laura para comparar, revisar, mejorar y preparar defensa.
4. Mantener defensa individual obligatoria.
```

## Seguridad

```text
No se incluyen secretos ni credenciales reales.
No se debe pedir al alumnado subir .env real, tokens, API keys ni datos personales.
```
