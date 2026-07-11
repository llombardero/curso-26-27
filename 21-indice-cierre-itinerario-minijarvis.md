# Índice de cierre — Itinerario MiniJarvis

## Programación + Entornos de Desarrollo — 1.º DAW — Curso 2026/2027

Versión: borrador 0.1

Documento de cierre del itinerario completo.

---

## 1. Finalidad de este documento

Este índice sirve para localizar rápidamente todos los materiales creados para el proyecto anual MiniJarvis.

El itinerario queda organizado en dos líneas complementarias:

```text
hitos/
```

Material docente, fichas de alumnado, checklists de corrección y plantillas.

```text
99-ejemplos-alumna/
```

Ejemplos completos de Laura, usados como modelo calibrado de entrega.

---

## 2. Documentos base del curso

| Documento | Función |
|---|---|
| `00-mapa-maestro-curso-2026-2027.md` | Visión global del curso y estructura curricular. |
| `02-calendario-hitos-sprints-2026-2027.md` | Calendario de hitos, sprints y evaluaciones. |
| `04A-enunciados-y-entregables-alumnado.md` | Enunciados y entregables por hito. |
| `05-politica-uso-ia-semaforo-registro-defensa.md` | Política de uso de IA, semáforo, registro y defensa. |
| `06-rubricas-hitos.md` | Rúbricas por hito. |
| `07-plantillas-entregables.md` | Plantillas generales. |
| `08-guia-alumnado-proyecto-agente-ia.md` | Guía completa del alumnado. |
| `09-presentacion-alumnado-proyecto-agente-ia.md` | Presentación breve para alumnado. |

---

## 3. Estructura docente por hitos

| Hito | Carpeta | Foco |
|---|---|---|
| H0 | `hitos/h0-torre-papel-scrum/` | Scrum inicial, torre de papel, roles, backlog, review y retrospectiva. |
| H1 | `hitos/h1-primer-asistente/` | Primer asistente básico por consola. |
| H2 | `hitos/h2-decisiones-depuracion/` | Menú, decisiones, bucles, pruebas y depuración. |
| H3 | `hitos/h3-memoria-colecciones/` | Memoria temporal con colecciones. |
| H4 | `hitos/h4-agente-orientado-objetos/` | Orientación a objetos, clases y diagramas. |
| H5 | `hitos/h5-extensible-clean-code-patrones/` | Extensibilidad, refactorización, revisión, Git y patrones iniciales. |
| H6 | `hitos/h6-persistente-trazable/` | Persistencia, logs, reproducibilidad y seguridad básica. |
| H7 | `hitos/h7-integracion-ia-responsable/` | Integración IA responsable o simulación robusta. |
| HF | `hitos/hf-presentacion-final-recuperacion-mejora/` | Portfolio final, demo, defensa, recuperación y registro IA final. |

---

## 4. Ejemplos completos de Laura

| Fase | Carpeta de ejemplo |
|---|---|
| H0 | `99-ejemplos-alumna/h0-torre-papel/` |
| H1 | `99-ejemplos-alumna/h1-primer-asistente/` |
| H2 | `99-ejemplos-alumna/h2-decisiones-depuracion/` |
| H3 | `99-ejemplos-alumna/h3-memoria-colecciones/` |
| H4 | `99-ejemplos-alumna/h4-agente-orientado-objetos/` |
| H5 | `99-ejemplos-alumna/h5-extensible-clean-code-patrones/` |
| H6 | `99-ejemplos-alumna/h6-persistente-trazable/` |
| H7 | `99-ejemplos-alumna/h7-integracion-ia-responsable/` |
| HF | `99-ejemplos-alumna/hf-presentacion-final-recuperacion-mejora/` |

---

## 5. Lectura recomendada para el profesorado

Orden recomendado:

1. `00-mapa-maestro-curso-2026-2027.md`
2. `02-calendario-hitos-sprints-2026-2027.md`
3. `05-politica-uso-ia-semaforo-registro-defensa.md`
4. `06-rubricas-hitos.md`
5. `hitos/README.md`
6. Carpetas de `hitos/` según fase.
7. Ejemplos de Laura en `99-ejemplos-alumna/`.

---

## 6. Lectura recomendada para el alumnado

Orden recomendado:

1. `09-presentacion-alumnado-proyecto-agente-ia.md`
2. `08-guia-alumnado-proyecto-agente-ia.md`
3. Ficha del hito correspondiente dentro de `hitos/`.
4. Plantillas del hito correspondiente.
5. Ejemplo de Laura solo cuando el profesorado decida mostrarlo como modelo.

---

## 7. Criterio de uso de los ejemplos de Laura

Los ejemplos de Laura no deben usarse como solución para copiar.

Uso recomendado:

```text
- mostrar nivel de detalle esperado;
- calibrar documentación;
- enseñar cómo justificar decisiones;
- preparar defensas;
- comparar una entrega incompleta con una entrega modelo.
```

Uso no recomendado:

```text
- entregar el ejemplo como trabajo propio;
- copiar código sin entenderlo;
- sustituir la defensa individual;
- eliminar el proceso de prueba, error y mejora.
```

---

## 8. Seguridad e IA

Reglas transversales:

```text
- No subir secretos.
- No subir .env real.
- No usar datos personales reales en ejemplos.
- Registrar uso de IA.
- Validar respuestas generadas por IA.
- Defender individualmente el trabajo entregado.
```

Regla docente central:

```text
Sin comprensión defendible, no hay evidencia completa de aprendizaje.
```

---

## 9. Estado de cierre del itinerario

El itinerario queda cerrado en esta estructura:

```text
H0 → H1 → H2 → H3 → H4 → H5 → H6 → H7 → HF
```

Cada fase cuenta con:

```text
[x] paquete docente;
[x] ficha o guía para alumnado;
[x] checklist de corrección;
[x] plantillas locales;
[x] ejemplo completo de Laura, salvo H0 con estructura propia de actividad inicial;
[x] verificación ad-hoc durante la construcción.
```

---

## 10. Próximas acciones posibles

Antes de publicar o versionar:

```text
[ ] Revisar tono final de documentos de alumnado.
[ ] Decidir qué ejemplos de Laura se mostrarán y cuándo.
[ ] Limpiar archivos temporales/swap si procede.
[ ] Revisar enlaces internos si se va a publicar en Moodle/GitHub.
[ ] Crear commit o snapshot del estado final.
```
