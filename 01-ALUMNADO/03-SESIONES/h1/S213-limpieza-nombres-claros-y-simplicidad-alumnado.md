# S213 — Comparaciones, lógica y decisiones

| Dato | Valor |
|---|---|
| Hito | H1 — Primer MiniJarvis |
| Duración | 3 periodos; esta ficha organiza el checkpoint de 45 minutos |
| Fase HEXA | Ejecutar — crear |
| Registro de proceso | Una entrada en el diario individual al cerrar el checkpoint; no se crea un documento adicional |

> El producto principal H1 sigue siendo pequeño. Las microprácticas demuestran el Tema 1 y pueden permanecer separadas de `Main.java`.

**Objetivo:** Construir booleanos, combinarlos y usarlos en if/else; reconocer anidamiento y asignación condicional.

**D1** · 00:00–00:04 · EJECUTAR

## ¿Qué devuelve 5 > 3?

No devuelve 5 ni 3.<br>
Devuelve una respuesta lógica.

**Qué haces:** Predice.

**Qué debe quedar:** respondan true/false.

**D2** · 00:04–00:10 · PÍLDORA DOCENTE 1/6

## Comparar produce boolean

**Qué haces:** Predice 4 comparaciones.

**Qué debe quedar:** puedan escribir una comparación simple.

**D3** · 00:10–00:14 · MICROPRÁCTICA

## Guarda el resultado de comparar

int hours = 5;<br>
boolean enough = hours >= 4;<br>
System.out.println(enough);

**Qué haces:** Cambia hours y predice.

**Qué debe quedar:** ambos valores hayan aparecido.

**D4** · 00:14–00:20 · PÍLDORA DOCENTE 2/6

## AND, OR, NOT

**Qué haces:** Resuelve 3 casos.

**Qué debe quedar:** puedan verbalizar cada operador.

**D5** · 00:20–00:23 · MICROPRÁCTICA

## Combina condiciones

boolean canStart = hasName && hasGoal;<br>
boolean needsHelp = !canStart || hasError;

**Qué haces:** Traduce código↔lenguaje.

**Qué debe quedar:** puedan leer una expresión.

**D6** · 00:23–00:26 · PÍLDORA DOCENTE 3/6

## Del boolean a una decisión

Una condición es algo que produce true o false.<br>
<br>
if (...) usa ese resultado para decidir qué bloque ejecutar.

**Qué haces:** Propone una condición posible.

**Qué debe quedar:** entiendan que if necesita boolean.

**D7** · 00:26–00:32 · PÍLDORA DOCENTE 4/6

## if / else: dos caminos

if (hours >= 4) {<br>
System.out.println("Objetivo alcanzado");<br>
} else {<br>
System.out.println("Objetivo pendiente");<br>
}

**Qué haces:** Predice ambas rutas.

**Qué debe quedar:** puedan señalar qué rama se ejecuta.

**D8** · 00:32–00:35 · PRUEBA

## Una condición, dos casos

Caso A: hours = 5<br>
Caso B: hours = 2<br>
<br>
Escribe salida esperada antes de ejecutar.

**Qué haces:** Prueba ambas ramas.

**Qué debe quedar:** ambas ramas estén verificadas.

**D9** · 00:35–00:38 · PÍLDORA DOCENTE 5/6

## Anidamiento: reconocer la idea

**Qué haces:** Explica qué condición se mira primero.

**Qué debe quedar:** puedan leer el esquema.

**D10** · 00:38–00:40 · PÍLDORA DOCENTE 6/6

## Asignación condicional ?:

String message = hours >= 4<br>
? "Objetivo alcanzado"<br>
: "Objetivo pendiente";

**Qué haces:** Identifica condición, valor true y valor false.

**Qué debe quedar:** puedan señalar tres partes.

**D11** · 00:40–00:43 · ACTIVIDAD

## Micropráctica defendible

Dato → comparación → boolean → if/else → salida<br>
<br>
Prueba una entrada que haga true y otra que haga false.

**Qué haces:** Programa y prueba.

**Qué debe quedar:** dos casos funcionen.

**D12** · 00:43–00:45 · CIERRE

## Revisa una línea que ahora entiendes mejor

Elige una mejora de nombres, comentario o condición y regístrala.

**Qué haces:** Mejora y registra.

**Qué debe quedar:** quede una mejora concreta.

**Cierre:** registra evidencia y una breve explicación de lo aprendido. Usa datos ficticios y no publiques credenciales ni información personal.

## Evidencia única antes de salir

- conserva el código o la prueba en el lugar indicado por la sesión;
- añade una sola entrada al diario individual con prueba, bloqueo y siguiente paso;
- no copies la misma reflexión en otro documento; el Site personal seleccionará evidencias al cerrar H1.

## Seguridad y uso de IA

- Usa datos ficticios y no publiques credenciales ni información personal.
- Si utilizas IA de forma sustantiva, registra propósito, propuesta, cambios propios y validación en el registro de IA del hito.

## Cierre individual

**¿Qué puedes señalar, explicar y probar al terminar este checkpoint?**
