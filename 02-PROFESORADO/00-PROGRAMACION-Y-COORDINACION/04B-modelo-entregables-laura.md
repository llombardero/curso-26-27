# Modelo privado de entregables — Laura

## Finalidad

Los ejemplos de Laura son referencias docentes privadas y se publican de forma diferida, después del intento propio. Ayudan a interpretar criterios, distinguir autoría y preparar la defensa; no son plantillas para copiar.

La fuente regenerable es `generar_evidencias_laura.py` y la salida vive en `03-EJEMPLOS-LAURA-PRIVADOS/`.

## Arquitectura canónica

```text
03-EJEMPLOS-LAURA-PRIVADOS/
├── README-PUBLICACION.md
├── FUENTES-CURSO/
│   ├── 01-Diario-individual-MiniJarvis.xlsx
│   └── 02-Scrum-equipo-MiniJarvis.xlsx
├── ENTREGA-MOODLE/
│   └── una entrega mínima por H0-H7 y HF
├── PORTFOLIOS-PERIODICOS/
│   └── Site personal y de equipo para C1, C2 y HF
└── h0...hf/
    ├── README.md
    ├── src/ cuando procede
    └── datos o logs ficticios cuando procede
```

No hay cinco documentos nuevos por hito ni carpetas `docs/` paralelas. El diario y el Scrum son fuentes estables durante todo el curso. Los Sites aparecen solo en C1, C2 y HF. La entrega Moodle de ejemplo replica el contrato real del hito.

## Qué muestra cada fuente

| Fuente | Autoría | Qué demuestra |
|---|---|---|
| Repositorio y README | Equipo desde H1 | Código, pruebas, decisiones, diagramas ligados al código, historial y versión evaluada. |
| Diario | Individual | Aprendizaje, decisión, bloqueo o IA significativa. |
| Scrum | Equipo | Backlog, decisiones, bloqueos, review, retrospectiva e IA colectiva. |
| Drive | Equipo, excepcional | Fotografía H0 u otra evidencia no-code sin fuente mejor. |
| Sites | Personal/equipo | Selección y comunicación en C1, C2 y HF. |
| Moodle | Equipo/individual según hito | Registro mínimo de la versión evaluada y de los enlaces exigidos. |
| Defensa | Individual | Comprensión y autoría; no genera un Markdown separado. |

## Contrato por hito

- H0: Scrum, ticket o texto breve y evidencia no-code opcional; sin GitHub, tag ni Sites.
- H1-H7: tag o commit estable, confirmación de diario/Scrum y evidencia no-code solo si existe.
- C1/C2: actualización de Sites y defensa o recuperación concreta.
- HF: release/tag final, Sites finales, defensa individual y recuperación únicamente si procede.

## Regla de publicación

1. El alumnado intenta y produce una primera versión defendible.
2. El profesorado selecciona solo el fragmento del ejemplo necesario.
3. El grupo compara criterios y decisiones, no copia artefactos.
4. Los ejemplos completos permanecen fuera de Moodle y de las carpetas compartidas del alumnado.
