# S208 — La estructura mínima de un programa Java

| Dato | Valor |
|---|---|
| Hito | H1 — Primer MiniJarvis |
| Duración | 2 periodos; esta ficha organiza el checkpoint de 45 minutos |
| Fase HEXA | Investigar — aprender lo necesario |
| Registro de proceso | Una entrada en el diario individual al cerrar el checkpoint; no se crea un documento adicional |

> El producto principal H1 sigue siendo pequeño. Las microprácticas demuestran el Tema 1 y pueden permanecer separadas de `Main.java`.

**Objetivo:** Leer, reconstruir y depurar la estructura mínima; reconocer aspectos léxicos y comentarios.

**D1** · 00:00–00:05 · INVESTIGAR

## ¿Qué líneas hacen algo visible?

public class Main {<br>
public static void main(String\[\] args) {<br>
System.out.println("Hola");<br>
System.out.println("MiniJarvis arranca");<br>
}<br>
}

**Qué haces:** Señala y justifica.

**Qué debe quedar:** identifiquen println como instrucción visible.

**D2** · 00:05–00:12 · PÍLDORA DOCENTE 1/4

## Clase, archivo y main

**Qué haces:** Localiza cada parte en su proyecto.

**Qué debe quedar:** puedan señalar ambas piezas.

**D3** · 00:12–00:18 · PÍLDORA DOCENTE 2/4

## Java es preciso con la escritura

**Qué haces:** Busca los símbolos en el código.

**Qué debe quedar:** puedan anticipar un error sencillo.

**D4** · 00:18–00:23 · DIAGNÓSTICO

## ¿Compilará? Caso 1

public class Main {<br>
public static void main(string\[\] args) {<br>
System.out.println("Hola");<br>
}<br>
}

**Qué haces:** Predice y corrige.

**Qué debe quedar:** expliquen por qué falla.

**D5** · 00:23–00:27 · DIAGNÓSTICO

## ¿Compilará? Caso 2

public class Main {<br>
public static void main(String\[\] args) {<br>
System.out.println("Hola")<br>
}<br>
}

**Qué haces:** Predice y corrige.

**Qué debe quedar:** formulen la regla.

**D6** · 00:27–00:32 · PÍLDORA DOCENTE 3/4

## Identificadores y palabras reservadas

**Qué haces:** Propone nombres válidos/invalidos.

**Qué debe quedar:** puedan justificar 3 casos.

**D7** · 00:32–00:35 · PÍLDORA DOCENTE 4/4

## Comentarios: explicar intención

// Comentario de una línea<br>
<br>
/\* Comentario<br>
de varias líneas \*/

**Qué haces:** Escribe un comentario útil.

**Qué debe quedar:** haya un comentario que aporte contexto.

**D8** · 00:35–00:42 · ACTIVIDAD

## Reconstruye el programa sin copiar

1\. Crea la estructura mínima.<br>
2. Añade 2–3 mensajes.<br>
3. Añade un comentario útil.<br>
4. Ejecuta.<br>
5. Corrige el primer error que aparezca.

**Qué haces:** Escribe y depura.

**Qué debe quedar:** cada persona logre ejecución.

**D9** · 00:42–00:45 · CIERRE

## Microdefensa de sintaxis

Señala:<br>
• dónde empieza la ejecución<br>
• una regla que rompería la compilación<br>
• un comentario útil

**Qué haces:** Defiende sobre su código.

**Qué debe quedar:** quede diagnosticada la comprensión.

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
