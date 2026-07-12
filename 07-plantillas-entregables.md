# Plantillas de entregables

## Programación + Entornos de Desarrollo — 1.º DAW — Curso 2026/2027

Versión: cierre curricular 1.0 — julio 2026
Documentos relacionados:

- `00-mapa-maestro-curso-2026-2027.md`
- `01-matriz-integrada-ra-ce-evidencias-tareas.md`
- `01A-anexo-programacion-ra-ce.md`
- `01B-anexo-entornos-ra-ce.md`
- `02-calendario-hitos-sprints-2026-2027.md`
- `04A-enunciados-y-entregables-alumnado.md`
- `04B-modelo-entregables-laura.md`
- `05-politica-uso-ia-semaforo-registro-defensa.md`
- `06-rubricas-hitos.md`

---

## 1. Propósito

Este documento recoge plantillas reutilizables para los entregables del proyecto anual:

> Construcción progresiva de un pequeño agente IA propio.

Las plantillas sirven para que el alumnado entregue evidencias homogéneas, revisables y defendibles, y para facilitar la coordinación entre Programación y Entornos de Desarrollo.

Uso recomendado:

- Copiar la plantilla necesaria en la carpeta `docs/` del hito correspondiente.
- Completar solo los apartados aplicables al hito.
- No borrar apartados importantes: si algo no aplica, escribir “No aplica en este hito” y justificar brevemente.

---

## 2. Estructura recomendada por hito

```text
hN-nombre-del-hito/
├── README.md
├── src/
│   └── ...
├── docs/
│   ├── portfolio.md
│   ├── registro-ia.md
│   ├── pruebas.md
│   ├── depuracion.md
│   ├── retrospectiva.md
│   ├── comparacion-java-python.md
│   └── decisiones-tecnicas.md
└── .gitignore
```

No todos los hitos necesitan todos los archivos.

| Hito | Plantillas mínimas recomendadas |
|---|---|
| H0 | retrospectiva, contrato de equipo, backlog inicial |
| H1 | README, portfolio, registro IA si procede |
| H2 | README, pruebas, depuración, incidencia, comparación Java ↔ Python, registro IA |
| H3 | README, pruebas, decisión de colección, comparación Java ↔ Python, portfolio |
| H4 | README, diagrama-código, comparación Java ↔ Python, portfolio |
| H5 | README, refactorización, revisión de código, patrón si procede, comparación Java ↔ Python |
| H6 | README, pruebas de persistencia, seguridad/datos, comparación Java ↔ Python |
| H7 | README, registro prompts, riesgos, configuración segura, defensa IA |
| HF | portfolio final, defensa final, registro IA final, recuperación si procede |

---

## 3. Plantilla README.md

```markdown
# HITO — Título del hito

Equipo:
Integrantes:
Curso:
Módulos: Programación + Entornos de Desarrollo
Fecha:

---

## 1. Descripción

Explica brevemente qué hace esta versión del agente.

---

## 2. Qué incluye esta entrega

- 
- 
- 

---

## 3. Cómo ejecutar

### Desde IntelliJ

1. 
2. 
3. 

### Desde terminal, si procede

```bash
# comandos necesarios
```

---

## 4. Estructura del proyecto

```text
src/
docs/
```

Explica brevemente qué hay en cada carpeta.

---

## 5. Funcionalidades implementadas

| Funcionalidad | Estado | Observaciones |
|---|---|---|
| | Hecho / Parcial / Pendiente | |

---

## 6. Relación con Programación

RA/CE trabajados:

- 

Evidencias:

- 

---

## 7. Relación con Entornos de Desarrollo

RA/CE trabajados:

- 

Evidencias:

- 

---

## 8. Pruebas realizadas

Resumen:

- 

Archivo de pruebas:

```text
docs/pruebas.md
```

---

## 9. Uso de IA

He usado IA: sí / no.

Si se ha usado, consultar:

```text
docs/registro-ia.md
```

---

## 10. Limitaciones conocidas

- 
- 

---

## 11. Qué sabemos defender

Cada integrante debe poder explicar:

- 
- 
- 
```

---

## 4. Plantilla portfolio individual

```markdown
# Portfolio individual — HITO

Alumno/a:
Equipo:
Fecha:

---

## 1. Qué he hecho yo

Describe tus aportaciones concretas.

- 
- 
- 

---

## 2. Qué he aprendido

Explica aprendizajes técnicos y de trabajo en equipo.

- 
- 
- 

---

## 3. Problemas encontrados

| Problema | Cómo lo detecté | Cómo lo resolví |
|---|---|---|
| | | |

---

## 4. Código o evidencia que sé defender

Indica fragmentos, clases, diagramas, pruebas o decisiones que puedes explicar.

- 
- 

---

## 5. Relación con Programación

RA/CE que creo haber trabajado:

- 

Explicación:

- 

---

## 6. Relación con Entornos de Desarrollo

RA/CE que creo haber trabajado:

- 

Explicación:

- 

---

## 7. Uso de IA

He usado IA: sí / no.

Resumen del uso:

- 

Registro completo:

```text
docs/registro-ia.md
```

---

## 8. Qué necesito mejorar

- 
- 

---

## 9. Preguntas que puedo responder en defensa

1. 
2. 
3. 
```

---

## 5. Plantilla registro de IA

```markdown
# Registro de uso de IA

Alumno/a:
Equipo:
Hito:
Fecha:
Herramienta usada: Gemini / Jarvis / otra autorizada

---

## Uso 1

### Objetivo

¿Qué querías conseguir?

### Prompt o resumen del prompt

```text
Escribe aquí el prompt o un resumen fiel.
```

### Resultado obtenido

¿Qué te devolvió la IA?

### Qué acepté

¿Qué parte usaste?

### Qué modifiqué yo

¿Qué cambiaste, corregiste o adaptaste?

### Cómo lo verifiqué

¿Cómo comprobaste que era correcto?

### Qué aprendí

¿Qué entiendes ahora que antes no entendías?

### Riesgos detectados

¿Había errores, inseguridad, código raro, datos sensibles o algo que no comprendías?

---

## Declaración final

Confirmo que:

- he revisado el resultado generado o sugerido por la IA;
- puedo explicar lo que he entregado;
- no he introducido datos personales ni secretos;
- no he copiado una solución completa sin entenderla.
```

---

## 6. Plantilla plan de pruebas

```markdown
# Plan de pruebas — HITO

Equipo:
Fecha:
Producto probado:

---

## 1. Objetivo de las pruebas

¿Qué queremos comprobar?

- 
- 

---

## 2. Casos de prueba

| ID | Caso | Entrada / acción | Resultado esperado | Resultado obtenido | Estado |
|---|---|---|---|---|---|
| P01 | | | | | Correcto / Error |
| P02 | | | | | Correcto / Error |

---

## 3. Casos límite

| Caso límite | Qué puede pasar | Cómo lo comprobamos |
|---|---|---|
| | | |

---

## 4. Incidencias detectadas

| Incidencia | Caso relacionado | Estado |
|---|---|---|
| | | Abierta / Resuelta |

---

## 5. Conclusión

¿El producto está listo para demo? ¿Qué falta?

- 
```

---

## 7. Plantilla informe de depuración

```markdown
# Informe de depuración — HITO

Alumno/a o equipo:
Fecha:

---

## 1. Problema detectado

Describe el error o comportamiento inesperado.

---

## 2. Cómo se reproduce

Pasos:

1. 
2. 
3. 

---

## 3. Herramienta usada

- IntelliJ Debugger
- Breakpoint en:
- Variables observadas:

---

## 4. Qué observé

¿Qué valor tenía cada variable? ¿Qué línea causaba el problema?

---

## 5. Causa probable

Explica la causa con tus palabras.

---

## 6. Solución aplicada

¿Qué cambiaste?

---

## 7. Verificación

¿Cómo comprobaste que ya funciona?

---

## 8. Qué aprendí

- 
```

---

## 8. Plantilla incidencia

```markdown
# Incidencia

ID:
Fecha:
Detectada por:
Estado: Abierta / En curso / Resuelta

---

## 1. Descripción

¿Qué ocurre?

---

## 2. Pasos para reproducir

1. 
2. 
3. 

---

## 3. Resultado esperado

¿Qué debería pasar?

---

## 4. Resultado obtenido

¿Qué pasa realmente?

---

## 5. Causa

¿Cuál era el problema?

---

## 6. Solución

¿Qué se ha cambiado?

---

## 7. Prueba de verificación

¿Cómo se ha comprobado?
```

---

## 9. Plantilla retrospectiva

```markdown
# Retrospectiva — HITO

Equipo:
Fecha:

---

## 1. Qué salió bien

- 
- 

---

## 2. Qué no salió bien

- 
- 

---

## 3. Bloqueos

| Bloqueo | Cómo apareció | Qué hicimos |
|---|---|---|
| | | |

---

## 4. Qué cambiaremos en el siguiente sprint

- 
- 

---

## 5. Acuerdos de mejora

| Acuerdo | Responsable | Fecha de revisión |
|---|---|---|
| | | |
```

---

## 10. Plantilla comparación Java ↔ Python

```markdown
# Comparación Java ↔ Python — HITO

Alumno/a:
Hito:
Fecha:

---

## 1. Qué hace la versión Java

Explica con tus palabras qué hace el programa o fragmento en Java.

---

## 2. Versión o fragmento en Java

```java
// fragmento relevante
```

---

## 3. Versión o fragmento en Python

```python
# fragmento equivalente
```

---

## 4. Diferencias encontradas

| Aspecto | Java | Python |
|---|---|---|
| Tipos | | |
| Entrada/salida | | |
| Estructuras de control | | |
| Colecciones | | |
| Clases/objetos | | |
| Errores | | |

Completa solo las filas que correspondan al hito.

---

## 5. Uso de IA

¿He usado IA para esta comparación? sí / no

Si sí:

- herramienta:
- qué pedí:
- qué acepté:
- qué cambié:
- cómo lo verifiqué:

---

## 6. Qué he aprendido

- 
- 

---

## 7. Preguntas que puedo responder

1. 
2. 
3. 
```

---

## 11. Plantilla decisión técnica

```markdown
# Decisión técnica — HITO

Equipo:
Fecha:
Decisión:

---

## 1. Problema

¿Qué problema queríamos resolver?

---

## 2. Opciones consideradas

| Opción | Ventajas | Inconvenientes |
|---|---|---|
| | | |

---

## 3. Decisión tomada

¿Qué opción elegimos?

---

## 4. Justificación

¿Por qué?

---

## 5. Consecuencias

¿Qué mejora? ¿Qué limita? ¿Qué tendremos que revisar más adelante?

---

## 6. IA utilizada

¿Se usó IA para tomar o revisar esta decisión? sí / no

Si sí, enlazar `registro-ia.md`.
```

---

## 12. Plantilla registro de patrón de diseño

```markdown
# Registro de patrón de diseño — HITO

Equipo:
Fecha:
Patrón considerado:

---

## 1. Problema real detectado

¿Qué problema del código nos llevó a pensar en un patrón?

---

## 2. Solución simple considerada

Antes de aplicar un patrón, ¿qué solución más sencilla probamos o pensamos?

---

## 3. Patrón considerado

Nombre del patrón:

Qué propone:

---

## 4. Decisión

Aplicamos el patrón: sí / no

---

## 5. Justificación

¿Por qué tiene o no tiene sentido en este momento?

---

## 6. Evidencia en el código

Clases o métodos relacionados:

```text

```

---

## 7. Riesgos

¿El patrón añade complejidad? ¿Compensa?

---

## 8. Defensa

Preguntas que debemos poder responder:

- ¿Qué problema resuelve?
- ¿Qué alternativa había?
- ¿Qué pasa si mañana añadimos otra herramienta/comando?
```

---

## 13. Plantilla seguridad y datos

```markdown
# Seguridad y datos — HITO

Equipo:
Fecha:

---

## 1. Datos usados

¿Qué datos usa el proyecto?

| Dato | Real/ficticio | Dónde aparece |
|---|---|---|
| | | |

---

## 2. Secretos

¿El proyecto necesita claves, tokens o contraseñas? sí / no

Si sí:

- no se suben al repositorio;
- se documentan en `.env.example` sin valores reales;
- se explica cómo configurarlas.

---

## 3. Riesgos detectados

| Riesgo | Medida aplicada |
|---|---|
| | |

---

## 4. Revisión final

Confirmamos que:

- no hay contraseñas en el repositorio;
- no hay claves API reales;
- no hay datos personales reales;
- no hemos pegado secretos en herramientas de IA.
```

---

## 14. Plantilla defensa individual

```markdown
# Preparación de defensa individual — HITO

Alumno/a:
Hito:
Fecha:

---

## 1. Qué puedo explicar

- 
- 

---

## 2. Qué parte he hecho yo

- 
- 

---

## 3. Código o evidencia que puedo defender

Archivo / clase / documento:

Qué hace:

Por qué es importante:

---

## 4. Preguntas posibles

| Pregunta | Respuesta preparada |
|---|---|
| | |

---

## 5. Si el profesor cambia algo...

¿Qué parte sabría modificar?

- 

---

## 6. Uso de IA

¿Qué parte fue asistida por IA y cómo la verifiqué?
```

---

## 15. Próximo paso

Estas plantillas pueden copiarse después en archivos separados dentro de una carpeta:

```text
plantillas/
```

si se quiere entregar al alumnado como documentos independientes.
