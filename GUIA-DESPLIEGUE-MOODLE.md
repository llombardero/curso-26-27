# Guía de despliegue — Moodle Centros y ecosistema digital

Curso 2026/2027 — 1.º DAW.

## 1. Separación obligatoria

- Publicar progresivamente desde `01-ALUMNADO-HTML/` o desde `Minijarvis-alumnado-html.zip`.
- Usar `05-PAQUETE-MOODLE/` como estructura de montaje del aula, con recursos, tareas, grupos y comprobaciones.
- Conservar `01-ALUMNADO/` como fuente original editable en Markdown, no como formato principal para el alumnado.
- Mantener `02-PROFESORADO/` fuera de la vista del alumnado.
- Mantener `03-EJEMPLOS-LAURA-PRIVADOS/` oculto hasta después del intento propio.

## 2. Responsabilidad de cada plataforma

| Plataforma | Responsabilidad única                                 |
| ---------- | ----------------------------------------------------- |
| Moodle     | Reto, materiales, entrega, fecha, rúbrica y feedback. |
| Drive      | Evidencias de trabajo que no son código.              |
| Sheets     | Diario individual y seguimiento Scrum.                |
| Sites      | Selección razonada de evidencias.                     |
| GitHub     | Código, README, historial y versión evaluada.         |

## 3. Estructura del aula

1. Empieza aquí y ecosistema digital.
2. H0 — Equipo, HADA, Scrum y torre.
3. H1 — Primer MiniJarvis ejecutable.
4. H2 — Decisiones, bucles y depuración.
5. H3 — Memoria temporal y colecciones.
6. H4 — Orientación a objetos.
7. H5 — Extensibilidad, Clean Code y patrones.
8. H6 — Persistencia y trazabilidad.
9. H7 — IA responsable, si procede.
10. HF — Portfolio, demo, defensa y mejora.

## 4. Apertura de cada hito

Publicar únicamente:

1. ficha del reto;
2. capítulo necesario;
3. sesiones activas;
4. plantillas requeridas;
5. `ENTREGA-DIGITAL.html` del hito;
6. tarea Moodle correspondiente;
7. rúbrica o criterios visibles;
8. ejemplo de Laura solo después del intento propio.

Los PDF temáticos se conservan en el área docente y se publican individualmente cuando el avance del reto los haga necesarios. No se incluyen todos por adelantado en el paquete HTML del alumnado.

Cuando se publique un documento suelto, usar preferentemente su versión `.html`. El archivo `LEEME-ALUMNADO.html` sirve como entrada simple al paquete completo.

## 5. Entrega verificable

- Pedir enlaces profundos, no la carpeta general.
- Comprobar cada enlace con una cuenta no propietaria.
- Identificar el código con tag o commit desde H1.
- Adjuntar PDF/XLSX cuando la evidencia viva pueda cambiar.
- Conservar la fecha y el feedback en Moodle.
- Separar entregas individuales y de equipo.

## 6. Seguridad

- Acceso general restringido; nunca `cualquiera con el enlace`.
- Carpeta raíz del curso en lectura para el alumnado.
- Carpeta de cada equipo con acceso limitado y edición solo para sus integrantes.
- Desactivar que los editores cambien permisos o compartan.
- Mantener calificaciones, HADA, incidencias y observaciones privadas fuera de la carpeta del curso.
- No solicitar ni publicar contraseñas, tokens, claves API, credenciales IdEA/PASEN ni `.env` reales.

## 7. Verificación y copia

Antes de abrir un hito, probar permisos, agrupamientos, entrega individual/equipo y vista de estudiante. Los ZIP son transporte y no deben renombrarse como `.mbz`. Después de configurar y probar el aula, Moodle genera una copia `.mbz` sin usuarios ni datos de usuario; esa copia debe restaurarse primero en un curso de ensayo.
