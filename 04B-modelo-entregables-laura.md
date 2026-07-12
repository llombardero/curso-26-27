# Modelo de entregables de Laura

## Programación + Entornos de Desarrollo — 1.º DAW — Curso 2026/2027

Versión: cierre curricular 1.0 — julio 2026
Documento complementario: `04A-enunciados-y-entregables-alumnado.md`

---

## 1. Propósito

Este documento muestra qué entregaría Laura como ejemplo de alumna en cada hito.

No debe entregarse al alumnado como solución cerrada. Su función es ayudar al profesorado a calibrar:

- nivel esperado;
- estructura de carpetas;
- profundidad de documentación;
- evidencias mínimas;
- relación entre Programación y Entornos;
- uso responsable de IA;
- defensa individual.

---

## 2. Perfil ficticio de Laura

```text
Nombre: Laura García Martín
Equipo: Equipo Ada
Perfil: alumna de 1.º DAW con nivel inicial, responsable y progresiva
```

Criterio del modelo:

- Laura no entrega soluciones perfectas.
- Laura comete errores razonables y los documenta.
- Laura usa IA, pero la registra y explica qué acepta o modifica.
- Laura mejora su proyecto hito a hito.

---

## 3. H0 — Bootcamp Scrum: torre de papel

Laura entregaría, como parte del Equipo Ada:

```text
h0-torre-papel/
├── contrato-equipo.md
├── tablero-scrum-inicial.png
├── retrospectiva-equipo.md
├── glosario-scrum.md
└── backlog-inicial-agente.md
```

Ejemplo de contenido esperado en su retrospectiva individual:

```text
Hoy he aprendido que empezar a construir sin planificar nos hizo perder tiempo. En el siguiente sprint propondría dedicar dos minutos a decidir la estructura antes de cortar o doblar papel. Para el agente IA, esto significa que antes de programar necesitamos un backlog claro y criterios de aceptación.
```

Ejemplo de backlog inicial del agente:

```text
Pendiente:
- Elegir nombre del agente.
- Crear proyecto en IntelliJ.
- Mostrar mensaje de bienvenida.
- Pedir nombre de usuario.
- Preparar README.

Bloqueado:
- Todavía no sabemos usar GitHub bien.
```

---

## 4. H1 — Primer asistente básico

Laura ya tiene un ejemplo modelo en:

```text
99-ejemplos-alumna/h1-primer-asistente/
```

Estructura esperada:

```text
h1-primer-asistente/
├── README.md
├── src/
│   └── Main.java
├── docs/
│   ├── portfolio-h1.md
│   └── registro-ia.md
└── .gitignore
```

Resumen del código de Laura:

- saluda como MiniJarvis;
- pregunta el nombre;
- usa `String userName`;
- usa constantes como `ASSISTANT_NAME` y `COURSE_YEAR`;
- muestra mensajes básicos;
- no usa menú ni bucles.

Fragmento representativo:

```java
final String ASSISTANT_NAME = "MiniJarvis";
Scanner scanner = new Scanner(System.in);

System.out.println("Hola, soy " + ASSISTANT_NAME + ".");
System.out.print("¿Cómo te llamas? ");
String userName = scanner.nextLine();
```

Reflexión esperada de Laura:

```text
He dejado el programa más sencillo de lo que al principio quería. Iba a poner un menú, pero todavía no hemos trabajado bien bucles ni switch. Ahora puedo explicar cada línea.
```

---

## 5. H2 — Agente con decisiones y depuración

Laura entregaría:

```text
h2-menu-depuracion/
├── README.md
├── src/Main.java
├── docs/pruebas-h2.md
├── docs/depuracion-h2.md
├── docs/incidencia-h2.md
├── docs/comparacion-java-python-h2.md
└── docs/registro-ia.md
```

Ejemplo de caso de prueba de Laura:

| Caso | Entrada | Resultado esperado | Resultado obtenido |
|---|---|---|---|
| Comando ayuda | `ayuda` | Muestra comandos disponibles | Correcto |
| Comando desconocido | `pizza` | Muestra mensaje de error | Correcto |
| Salida | `salir` | Termina el programa | Correcto |

Ejemplo de incidencia:

```text
Síntoma:
Escribía "Salir" con mayúscula y el programa no terminaba.

Causa:
El programa comparaba exactamente con "salir".

Solución:
Convertí la entrada a minúsculas con toLowerCase().

Verificación:
Probé salir, Salir y SALIR.
```

Ejemplo de comparación Java ↔ Python:

```text
En Java uso while para repetir el menú y switch para decidir el comando.
En Python usaría while y match/case o if/elif.
La diferencia principal es que Python no exige declarar String ni boolean.
```

---

## 6. H3 — Agente con memoria en colecciones

Laura entregaría:

```text
h3-memoria-colecciones/
├── README.md
├── src/
├── docs/pruebas-memoria-h3.md
├── docs/decision-coleccion.md
├── docs/comparacion-java-python-h3.md
├── docs/portfolio-h3.md
└── docs/registro-ia.md
```

Ejemplo de reflexión de Laura:

```text
He usado una lista para guardar los comandos porque me interesa conservar el orden. Si necesitara buscar por clave, usaría un mapa. En Python la estructura más parecida para este caso sería una list.
```

Ejemplo de prueba de memoria:

| Caso | Acción | Resultado esperado |
|---|---|---|
| Memoria vacía | consultar memoria al inicio | mensaje “no hay datos todavía” |
| Añadir comando | escribir `saluda` | el comando aparece en historial |
| Listar memoria | usar `historial` | muestra comandos anteriores en orden |

---

## 7. H4 — Agente orientado a objetos

Laura entregaría:

```text
h4-poo-diagramas/
├── README.md
├── src/
│   ├── Main.java
│   ├── Agent.java
│   ├── Message.java
│   └── Memory.java
├── docs/diagrama-clases.md
├── docs/diagrama-comportamiento.md
├── docs/relacion-diagrama-codigo.md
├── docs/comparacion-java-python-h4.md
└── docs/registro-ia.md
```

Ejemplo de decisión de diseño:

```text
He creado una clase Agent porque Main estaba empezando a tener demasiada responsabilidad. Main solo inicia el programa. Agent se encarga de responder. Memory se encarga de guardar datos.
```

Ejemplo de relación diagrama-código:

```text
En el diagrama Agent tiene una relación con Memory.
En el código esto aparece como un atributo:

private Memory memory;
```

---

## 8. H5 — Agente extensible, código limpio y patrones iniciales

Laura entregaría:

```text
h5-herramientas-clean-code/
├── README.md
├── src/
├── docs/refactorizacion.md
├── docs/revision-codigo.md
├── docs/patron-command-o-decision.md
├── docs/comparacion-java-python-h5.md
└── docs/registro-ia.md
```

Ejemplo de decisión de Laura:

```text
He decidido no aplicar Factory todavía porque solo tengo dos herramientas. He usado una interfaz Tool porque todas las herramientas deben poder ejecutarse de forma parecida. Si el número de herramientas crece, revisaré si Factory tiene sentido.
```

Ejemplo de refactorización:

```text
Antes:
Todos los comandos estaban mezclados dentro de Agent.

Después:
He separado la herramienta HelpTool.

Motivo:
Agent queda más corto y es más fácil añadir nuevas herramientas.
```

---

## 9. H6 — Agente persistente y trazable

Laura entregaría:

```text
h6-persistencia-trazabilidad/
├── README.md
├── src/
├── data/ejemplo-memoria.txt
├── docs/pruebas-persistencia.md
├── docs/seguridad-datos.md
├── docs/comparacion-java-python-h6.md
└── docs/registro-ia.md
```

Ejemplo de decisión de seguridad:

```text
No he guardado nombres reales ni datos personales. El fichero de ejemplo usa datos ficticios. Si en el futuro usamos claves API, no se subirán a GitHub y se documentarán con .env.example.
```

Ejemplo de prueba de persistencia:

| Caso | Acción | Resultado esperado |
|---|---|---|
| Guardar memoria | escribir tres mensajes y salir | se crea fichero con historial |
| Cargar memoria | reiniciar programa | se recupera historial anterior |
| Fichero inexistente | borrar fichero y ejecutar | el programa crea memoria vacía sin fallar |

---

## 10. H7 — Integración IA responsable o simulación robusta

Laura entregaría:

```text
h7-ia-responsable/
├── README.md
├── src/
├── docs/registro-prompts.md
├── docs/riesgos-limitaciones.md
├── docs/configuracion-segura.md
├── docs/comparacion-java-python-h7.md
└── docs/defensa-ia.md
```

Ejemplo de riesgo documentado por Laura:

```text
Riesgo:
La IA puede inventar una respuesta o dar código que parece correcto pero no compila.

Control:
No uso la respuesta directamente. Primero la leo, la pruebo y la comparo con lo que esperaba.
```

Ejemplo de defensa IA:

```text
La IA no decide qué hace el agente. Solo propone una respuesta. Mi programa controla qué datos se envían y yo valido la salida antes de aceptarla.
```

---

## 11. HF — Presentación final, recuperación y mejora

Laura entregaría:

```text
hf-cierre-final/
├── portfolio-final-laura.md
├── registro-ia-final.md
├── defensa-final.md
└── recuperacion-si-procede.md
```

En su defensa debería poder explicar:

- evolución de H1 a H6/H7;
- qué partes entiende mejor;
- qué problemas tuvo;
- qué aprendió de la IA;
- qué evidencias demuestran cada RA pendiente.

Ejemplo de cierre de Laura:

```text
Al principio mi agente solo saludaba. Después aprendí a añadir comandos, memoria, clases y persistencia. Lo más difícil fue separar responsabilidades entre clases. La IA me ayudó a entender errores, pero tuve que probar y corregir el código porque no siempre daba soluciones adecuadas.
```
