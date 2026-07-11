# Guía docente — H7 Integración IA responsable o simulación robusta

## Programación + Entornos de Desarrollo — 1.º DAW — Curso 2026/2027

Versión: borrador 0.1

Documentos relacionados:

- `../../02-calendario-hitos-sprints-2026-2027.md`
- `../../04A-enunciados-y-entregables-alumnado.md`
- `../../06-rubricas-hitos.md`
- `README.md`
- `19B-ficha-alumnado-h7-integracion-ia-responsable.md`
- `19C-checklist-correccion-h7.md`

---

## 1. Propósito del hito

H7 permite cerrar el proyecto con una integración IA responsable real o simulada.

Producto esperado:

```text
MiniJarvis H7: modo IA responsable, limitado, validado, seguro y defendible.
```

La simulación robusta es válida si el grupo no está preparado para API real o si no se quieren gestionar credenciales.

---

## 2. Qué añade H7 respecto a H6

| H6 | H7 |
|---|---|
| Persistencia y logs. | Modo IA real o simulado. |
| Seguridad de ficheros. | Seguridad de prompts/configuración. |
| Reproducibilidad. | Validación humana de respuestas. |
| Trazabilidad técnica. | Registro de prompts, riesgos y límites. |

---

## 3. Restricciones de seguridad

Permitido:

- simulador IA local;
- respuestas prefijadas o basadas en reglas;
- prompts controlados;
- configuración con `.env.example` sin secretos;
- validación humana documentada.

No permitido:

- subir API keys;
- introducir datos personales reales;
- enviar secretos a IA;
- aceptar respuestas sin revisar;
- ocultar uso de IA;
- romper el cierre del proyecto por una integración externa frágil.

---

## 4. Fechas y duración

Fechas orientativas:

```text
26-29 abril 2027
```

Hito breve y opcional para no comprometer el cierre antes de FFEOE.

---

## 5. RA/CE y evidencias

Programación:

- consolidación PR RA1-RA6;
- PR RA7/RA8/RA9 si procede.

Entornos:

- ED RA3: pruebas y validación;
- ED RA4: documentación, configuración, revisión y trazabilidad;
- seguridad transversal.

Evidencias:

- integración o simulación funcional;
- registro de prompts;
- documento de riesgos;
- configuración segura;
- validación humana;
- defensa individual.

---

## 6. Diseño mínimo recomendado

Clases posibles:

| Clase | Responsabilidad |
|---|---|
| `AiAssistant` | Contrato o clase que responde de forma controlada. |
| `SimulatedAiAssistant` | Simulación local sin API key. |
| `AiTool` | Herramienta del agente que pide y valida consulta IA. |
| `PromptSafety` | Reglas básicas para bloquear datos prohibidos. |

Caso de uso recomendado:

```text
Pedir a MiniJarvis una sugerencia breve de estudio o explicación conceptual, sin datos personales ni secretos.
```

---

## 7. Entregables H7

| Entregable | Responsable | Formato | Plantilla local |
|---|---|---|---|
| Integración/simulación IA | Equipo/individual | `src/*.java` | No aplica. |
| README H7 | Equipo | `README.md` | `plantillas/README-h7-template.md` |
| Registro de prompts | Individual/equipo | `docs/registro-prompts-h7.md` | `plantillas/registro-prompts-h7-template.md` |
| Riesgos IA | Equipo | `docs/riesgos-ia-h7.md` | `plantillas/riesgos-ia-h7-template.md` |
| Configuración segura | Equipo | `docs/configuracion-segura-h7.md` | `plantillas/configuracion-segura-h7-template.md` |
| Validación humana | Individual/equipo | `docs/validacion-humana-h7.md` | `plantillas/validacion-humana-h7-template.md` |
| Comparación Java ↔ Python | Individual | `docs/comparacion-java-python-h7.md` | `plantillas/comparacion-java-python-h7-template.md` |
| Portfolio H7 | Individual | `docs/portfolio-h7.md` | `plantillas/portfolio-h7-template.md` |
| Defensa H7 | Individual | `docs/defensa-h7.md` | `plantillas/defensa-h7-template.md` |

---

## 8. Preparación para HF

Antes de cerrar H7, comprobar:

- si el modo IA es limitado y defendible;
- si no hay secretos;
- si hay validación humana;
- si el alumnado sabe qué hace y qué no hace la IA;
- si el proyecto queda listo para demo/defensa final.
