# S212 — Scanner y conversiones

| Dato | Valor |
|---|---|
| Hito | H1 — Primer MiniJarvis |
| Duración | 3 periodos; esta ficha organiza el checkpoint de 45 minutos |
| Fase HEXA | Ejecutar — crear |
| Registro de proceso | Una entrada en el diario individual al cerrar el checkpoint; no se crea un documento adicional |

> El producto principal H1 sigue siendo pequeño. Las microprácticas demuestran el Tema 1 y pueden permanecer separadas de `Main.java`.

**Objetivo:** Leer entrada, convertir tipos y reconocer errores de conversión.

**D1** · 00:00–00:05 · MICROINVESTIGACIÓN

## Hasta ahora los datos los decide quien programa

¿Cómo hacemos para que los escriba la persona que ejecuta MiniJarvis?

**Qué haces:** Propone formas de entrada.

**Qué debe quedar:** aparezca “teclado/consola”.

**D2** · 00:05–00:11 · PÍLDORA DOCENTE 1/4

## Scanner: pedir → leer → guardar

import java.util.Scanner;<br>
<br>
Scanner scanner = new Scanner(System.in);<br>
String userName = scanner.nextLine();<br>
scanner.close();

**Qué haces:** Señala qué devuelve y dónde se guarda.

**Qué debe quedar:** puedan verbalizar el flujo.

**D3** · 00:11–00:17 · ACTIVIDAD

## Pide un nombre y úsalo

Ejecuta dos veces con nombres ficticios distintos.<br>
<br>
¿Qué cambia? ¿Qué no?

**Qué haces:** Programa y prueba.

**Qué debe quedar:** la entrada afecte a la salida.

**D4** · 00:17–00:20 · CONFLICTO

## Tengo "5". ¿Tengo el número 5?

"5" es texto si procede de nextLine().<br>
5 es un entero.

**Qué haces:** Distingue String/int.

**Qué debe quedar:** aparezca necesidad de convertir.

**D5** · 00:20–00:25 · PÍLDORA DOCENTE 2/4

## Parsear texto a un tipo básico

int hours = Integer.parseInt(text);<br>
double score = Double.parseDouble(text);<br>
boolean ok = Boolean.parseBoolean(text);

**Qué haces:** Predice tipos resultantes.

**Qué debe quedar:** puedan explicar para qué sirve parseInt.

**D6** · 00:25–00:29 · EXPERIMENTO

## Leer → convertir → calcular

Scanner scanner = new Scanner(System.in);<br>
String text = scanner.nextLine();<br>
int hours = Integer.parseInt(text);<br>
int minutes = hours \* 60;<br>
System.out.println(minutes);<br>
scanner.close();

**Qué haces:** Predice y prueba.

**Qué debe quedar:** comprendan la cadena completa.

**D7** · 00:29–00:33 · PÍLDORA DOCENTE 3/4

## Conversión implícita

int whole = 7;<br>
double wider = whole;<br>
<br>
// no hace falta casting

**Qué haces:** Identifica origen/destino.

**Qué debe quedar:** distingan conversión numérica de String→número.

**D8** · 00:33–00:37 · PÍLDORA DOCENTE 4/4

## Casting: forzar puede perder información

double price = 12.75;<br>
int wholePrice = (int) price;<br>
// wholePrice vale 12

**Qué haces:** Predice antes de ejecutar.

**Qué debe quedar:** puedan explicar la pérdida.

**D9** · 00:37–00:40 · ERROR ÚTIL

## ¿Compila? ¿Y al ejecutar?

String text = "hola";<br>
int number = Integer.parseInt(text);

**Qué haces:** Observa el error en ejecución.

**Qué debe quedar:** puedan nombrar cuándo falla.

**D10** · 00:40–00:43 · ACTIVIDAD

## Evidencia de conversión

Guarda:<br>
• una entrada válida<br>
• resultado esperado<br>
• resultado obtenido<br>
• qué ocurre con una entrada no convertible

**Qué haces:** Documenta prueba.

**Qué debe quedar:** quede trazabilidad.

**D11** · 00:43–00:45 · CIERRE

## Microdefensa de tipos

¿Qué devuelve nextLine()?<br>
¿Por qué necesitamos parseInt?<br>
¿Qué diferencia hay con un casting?

**Qué haces:** Responde sobre su código.

**Qué debe quedar:** quede diagnóstico.

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
