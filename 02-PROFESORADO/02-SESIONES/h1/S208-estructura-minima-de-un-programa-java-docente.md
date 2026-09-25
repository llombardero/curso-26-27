# S208 — Guía docente

## La estructura mínima de un programa Java

| Dato | Valor |
|---|---|
| Hito | H1 — Primer MiniJarvis |
| Duración | 2 periodos; checkpoint proyectable de 45 minutos y taller asociado |
| Fase HEXA | Investigar — aprender lo necesario |
| Agrupamiento | Individual con contraste por parejas o equipo cuando la práctica lo requiera |
| Resultado observable | Leer, reconstruir y depurar la estructura mínima; reconocer aspectos léxicos y comentarios. |
| Evidencia mínima | Quede diagnosticada la comprensión. |

## Propósito

Leer, reconstruir y depurar la estructura mínima; reconocer aspectos léxicos y comentarios.

El concepto se incorpora al Tema 1, pero solo pasa a `Main.java` cuando mejora el producto mínimo. Las demás prácticas se conservan como microejercicios defendibles.

## Material imprescindible

- presentación de S208;
- IntelliJ y JDK cuando haya práctica de código;
- proyecto o microarchivo de prueba;
- diario individual y tablero Scrum del equipo;
- datos ficticios.

## Secuencia de aula

| Tiempo / diap. | Tipo y actuación | Alumnado | Observa | Puerta de avance | Si hay retraso |
|---|---|---|---|---|---|
| 00:00–00:05 / D1 | INVESTIGAR: Pide predecir qué líneas producen salida. | Señala y justifica. | Si atribuyen salida a class o main. | identifiquen println como instrucción visible. | 3 minutos. |
| 00:05–00:12 / D2 | PÍLDORA DOCENTE 1/4: Explica que el nombre de la clase pública coincide con el archivo y que main es el punto de entrada en estos programas. | Localiza cada parte en su proyecto. | Confusión Main/main. | puedan señalar ambas piezas. | no suprimas; 5 minutos. |
| 00:12–00:18 / D3 | PÍLDORA DOCENTE 2/4: Relaciona cada regla con un error real. | Busca los símbolos en el código. | Errores de case y cierres. | puedan anticipar un error sencillo. | prioriza mayúsculas y ;. |
| 00:18–00:23 / D4 | DIAGNÓSTICO: No ejecutes aún. Pide voto y justificación. | Predice y corrige. | Que localicen string. | expliquen por qué falla. | hazlo oralmente. |
| 00:23–00:27 / D5 | DIAGNÓSTICO: Pide localizar el error antes de ejecutar. | Predice y corrige. | Punto y coma. | formulen la regla. | fusiona con la anterior. |
| 00:27–00:32 / D6 | PÍLDORA DOCENTE 3/4: Explica reglas mínimas y la importancia del nombre significativo. | Propone nombres válidos/invalidos. | Espacios, número inicial, reservadas. | puedan justificar 3 casos. | un ejemplo válido y tres inválidos. |
| 00:32–00:35 / D7 | PÍLDORA DOCENTE 4/4: Explica que no se ejecutan y que deben aportar intención, no repetir literalmente la instrucción. | Escribe un comentario útil. | Comentarios decorativos o redundantes. | haya un comentario que aporte contexto. | 2 minutos. |
| 00:35–00:42 / D8 | ACTIVIDAD: Circula y pide verbalizar la primera marca del IDE. | Escribe y depura. | Autonomía con llaves, comillas y ;. | cada persona logre ejecución. | permite partir de un esqueleto incompleto. |
| 00:42–00:45 / D9 | CIERRE: Pregunta a 2–3 personas y registra dificultades comunes. | Defiende sobre su código. | Memorización sin localizar en código. | quede diagnosticada la comprensión. | una sola microdefensa + ticket. |

## Qué debes explicar

- **PÍLDORA DOCENTE 1/4:** Explica que el nombre de la clase pública coincide con el archivo y que main es el punto de entrada en estos programas.
- **PÍLDORA DOCENTE 2/4:** Relaciona cada regla con un error real.
- **PÍLDORA DOCENTE 3/4:** Explica reglas mínimas y la importancia del nombre significativo.
- **PÍLDORA DOCENTE 4/4:** Explica que no se ejecutan y que deben aportar intención, no repetir literalmente la instrucción.

## Ejemplo o demostración preparada

**D1 · ¿Qué líneas hacen algo visible? —** public class Main {<br>
public static void main(String\[\] args) {<br>
System.out.println("Hola");<br>
System.out.println("MiniJarvis arranca");<br>
}<br>
}

**D2 · Clase, archivo y main —** ARCHIVO Y CLASE: Main.java<br>
↕<br>
public class Main \| PUNTO DE ENTRADA: public static void main(String\[\] args)<br>
<br>
Aquí comienza la ejecución.

**D3 · Java es preciso con la escritura —** MAYÚSCULAS: Main ≠ main / String ≠ string \| DELIMITADORES: ; { } ( ) \| TEXTO: "comillas dobles" para String

**D4 · ¿Compilará? Caso 1 —** public class Main {<br>
public static void main(string\[\] args) {<br>
System.out.println("Hola");<br>
}<br>
}

**D5 · ¿Compilará? Caso 2 —** public class Main {<br>
public static void main(String\[\] args) {<br>
System.out.println("Hola")<br>
}<br>
}

**D6 · Identificadores y palabras reservadas —** IDENTIFICADOR ÚTIL: userName<br>
studyHours<br>
assistantName<br>
<br>
Describe qué guarda. \| NO VALE COMO NOMBRE: 1name<br>
my name<br>
class<br>
public

**D7 · Comentarios: explicar intención —** // Comentario de una línea<br>
<br>
/\* Comentario<br>
de varias líneas \*/

**D8 · Reconstruye el programa sin copiar —** 1. Crea la estructura mínima.<br>
2. Añade 2–3 mensajes.<br>
3. Añade un comentario útil.<br>
4. Ejecuta.<br>
5. Corrige el primer error que aparezca.

**D9 · Microdefensa de sintaxis —** Señala:<br>
• dónde empieza la ejecución<br>
• una regla que rompería la compilación<br>
• un comentario útil

## Consigna que se entrega al alumnado

1. Predice antes de ejecutar cuando haya código.
2. Realiza la micropráctica o modificación prevista.
3. Prueba el caso normal y, cuando exista una decisión o conversión, también el caso alternativo o erróneo.
4. Conserva el código o resultado en el repositorio o espacio indicado.
5. Registra una sola entrada en el diario individual; no crees un informe paralelo.

## Qué observar mientras trabajan

- Si atribuyen salida a class o main.
- Confusión Main/main.
- Errores de case y cierres.
- Que localicen string.
- Punto y coma.
- Espacios, número inicial, reservadas.
- Comentarios decorativos o redundantes.
- Autonomía con llaves, comillas y ;.
- Memorización sin localizar en código.

## Criterios para considerar cerrada la sesión

- Identifiquen println como instrucción visible.
- Puedan señalar ambas piezas.
- Puedan anticipar un error sencillo.
- Expliquen por qué falla.
- Formulen la regla.
- Puedan justificar 3 casos.
- Haya un comentario que aporte contexto.
- Cada persona logre ejecución.
- Quede diagnosticada la comprensión.
- La persona puede señalar la evidencia y explicar qué demuestra.

## Seguridad y uso de IA

- Trabajar con datos ficticios.
- No publicar credenciales, tokens, claves ni información personal.
- Si la IA interviene de forma sustantiva, registrar propuesta, cambios propios y validación; no aceptar código que no pueda defenderse.

## Comprobación final

**¿Qué puedes señalar, explicar, predecir o modificar para demostrar el aprendizaje de esta sesión?**

## Anotación docente al terminar

- alumnado que necesita reentrada;
- evidencia pendiente;
- error común;
- ajuste temporal necesario sin eliminar el núcleo conceptual.
