# Checklist de corrección — H6 Agente persistente y trazable

Documento para uso docente.

---

## 1. Persistencia

| Ítem | Sí | Parcial | No | Observaciones |
|---|---|---|---|---|
| Código compila y ejecuta | | | | |
| Guarda información en fichero | | | | |
| Recupera información | | | | |
| Crea carpetas si faltan | | | | |
| Gestiona errores básicos | | | | |
| Hay ficheros de ejemplo seguros | | | | |

---

## 2. Trazabilidad y reproducibilidad

| Ítem | Sí | Parcial | No | Observaciones |
|---|---|---|---|---|
| Hay logs/historial | | | | |
| README permite ejecutar desde cero | | | | |
| Pruebas de persistencia documentadas | | | | |
| Incidencias documentadas si proceden | | | | |

---

## 3. Seguridad

| Ítem | Sí | Parcial | No | Observaciones |
|---|---|---|---|---|
| No hay secretos | | | | |
| No hay `.env` real | | | | |
| No hay datos personales reales | | | | |
| Hay registro de decisiones de seguridad | | | | |

---

## 4. Decisión docente

```text
[ ] Evidencia válida.
[ ] Válida con mejoras menores.
[ ] Necesita recuperación parcial.
[ ] No válida todavía.
```

<!-- AJUSTE-COBERTURA-CONCEPTOS-32 -->

## Ajuste curricular — cobertura de conceptos de Programación

Este hito queda alineado con el mapa `32-lista-conceptos-programacion-por-tema.md`.

```text
Hito: H6
Temas de referencia: Temas 5, 6 y puente hacia Tema 8
Foco: persistencia, logs, errores y trazabilidad
```

Conceptos que deben trabajarse o, como mínimo, quedar conectados con evidencias del alumnado:

- clases responsables
- excepciones checked y runtime
- throws
- validación
- invariantes
- repositorio como idea inicial
- ficheros
- logs
- seguridad
- Repository como patrón opcional
- pruebas de dos ejecuciones
- trazabilidad

Criterio docente de cierre:

- El alumnado no solo entrega el producto; debe poder señalar dónde aparece cada concepto en su código, README, pruebas o defensa.
- Si un concepto se marca como ampliación, no penaliza al alumnado que alcance el mínimo, pero sí orienta mejora, recuperación o enriquecimiento.
- La defensa debe incluir al menos una pregunta de comprensión sobre los conceptos nuevos del hito.

