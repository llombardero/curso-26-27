# S207 — Guía docente

## Del código fuente a la consola

| Dato | Valor |
|---|---|
| Hito | H1 — Primer MiniJarvis |
| Duración | 3 periodos; checkpoint proyectable de 45 minutos y taller asociado |
| Fase HEXA | Investigar — aprender lo necesario |
| Agrupamiento | Individual con contraste por parejas o equipo cuando la práctica lo requiera |
| Resultado observable | Comprender el camino código fuente → compilación → ejecución → consola y conseguir una primera ejecución. |
| Evidencia mínima | Quede evidencia recuperable. |

## Propósito

Comprender el camino código fuente → compilación → ejecución → consola y conseguir una primera ejecución.

El concepto se incorpora al Tema 1, pero solo pasa a `Main.java` cuando mejora el producto mínimo. Las demás prácticas se conservan como microejercicios defendibles.

## Material imprescindible

- presentación de S207;
- IntelliJ y JDK cuando haya práctica de código;
- proyecto o microarchivo de prueba;
- diario individual y tablero Scrum del equipo;
- datos ficticios.

## Secuencia de aula

| Tiempo / diap. | Tipo y actuación | Alumnado | Observa | Puerta de avance | Si hay retraso |
|---|---|---|---|---|---|
| 00:00–00:04 / D1 | INVESTIGAR: Recupera S206 y plantea el objetivo técnico mínimo. | Anticipa pasos. | Confusión entre escribir y ejecutar. | haya hipótesis de pasos. | mantén 3 minutos. |
| 00:04–00:10 / D2 | PÍLDORA DOCENTE 1/2: Dibuja la cadena y define cada pieza funcionalmente. | Copia o reconstruye el mapa y hace una pregunta. | Si llaman “programa” a cualquier carpeta o consola. | distingan archivo, proyecto y salida. | explica solo las cuatro piezas y retoma al final. |
| 00:10–00:16 / D3 | DEMOSTRACIÓN: Crea/abre el proyecto y ejecuta lentamente. Señala editor y consola. | Observa primero; después reproduce. | Quién no localiza Main.java o la consola. | la mayoría tenga el proyecto listo. | usa un proyecto ya creado si la configuración consume tiempo. |
| 00:16–00:27 / D4 | ACTIVIDAD: Circula. Pregunta “¿qué esperabas ver?”. | Escribe, predice y ejecuta. | Copiado mecánico, errores de comillas y punto y coma. | cada persona haya logrado al menos una ejecución. | trabajo por parejas si hay problemas de entorno. |
| 00:27–00:33 / D5 | MICROINVESTIGACIÓN: Provoca un único error y modela la lectura del IDE. | Predice, ejecuta, localiza y corrige. | Si borran y reescriben sin leer el error. | puedan distinguir error de código de error de entorno. | haz solo un error colectivo. |
| 00:33–00:38 / D6 | PÍLDORA DOCENTE 2/2: Consolida usando la experiencia que acaban de vivir. | Explica los tres pasos a un compañero. | Uso correcto del vocabulario. | puedan describir el recorrido sin mirar. | reduce a una explicación oral de 2 minutos. |
| 00:38–00:45 / D7 | CIERRE: Pide evidencia concreta y una frase explicativa. | Guarda y registra. | Capturas sin consola o sin relación con el código. | quede evidencia recuperable. | la frase puede ser oral y registrada en el diario al inicio de S208. |

## Qué debes explicar

- **PÍLDORA DOCENTE 1/2:** Dibuja la cadena y define cada pieza funcionalmente.
- **PÍLDORA DOCENTE 2/2:** Consolida usando la experiencia que acaban de vivir.

## Ejemplo o demostración preparada

**D1 · Hoy investigamos el recorrido del programa —** ¿Qué ocurre entre escribir Main.java y ver un mensaje en la consola?

**D2 · Código → compilación → ejecución → consola —** ANTES: Código fuente<br>
Main.java<br>
<br>
Proyecto<br>
archivos + configuración \| AL EJECUTAR: JDK<br>
compila / prepara<br>
<br>
Consola<br>
muestra el resultado

**D3 · Primera ejecución: mira antes de copiar —** public class Main {<br>
public static void main(String\[\] args) {<br>
System.out.println("Hola, soy MiniJarvis.");<br>
}<br>
}

**D4 · Ahora ejecútalo tú —** 1. Escribe un mensaje distinto al del ejemplo.<br>
2. Predice la salida.<br>
3. Ejecuta.<br>
4. Comprueba si coincide.

**D5 · Rompe algo a propósito —** Quita un ; o una comilla.<br>
<br>
Antes de corregir:<br>
• ¿compila?<br>
• ¿dónde marca el IDE?<br>
• ¿qué hipótesis haces?

**D6 · Tres verbos que no significan lo mismo —** ESCRIBIR: Crear o modificar código fuente. \| COMPILAR: Comprobar/traducir el código para poder ejecutarlo. \| EJECUTAR: Poner el programa en marcha y observar su comportamiento.

**D7 · Guarda una primera evidencia —** Código + salida visible + frase:<br>
“Sé que se ha ejecutado porque…”

## Consigna que se entrega al alumnado

1. Predice antes de ejecutar cuando haya código.
2. Realiza la micropráctica o modificación prevista.
3. Prueba el caso normal y, cuando exista una decisión o conversión, también el caso alternativo o erróneo.
4. Conserva el código o resultado en el repositorio o espacio indicado.
5. Registra una sola entrada en el diario individual; no crees un informe paralelo.

## Qué observar mientras trabajan

- Confusión entre escribir y ejecutar.
- Si llaman “programa” a cualquier carpeta o consola.
- Quién no localiza Main.java o la consola.
- Copiado mecánico, errores de comillas y punto y coma.
- Si borran y reescriben sin leer el error.
- Uso correcto del vocabulario.
- Capturas sin consola o sin relación con el código.

## Criterios para considerar cerrada la sesión

- Haya hipótesis de pasos.
- Distingan archivo, proyecto y salida.
- La mayoría tenga el proyecto listo.
- Cada persona haya logrado al menos una ejecución.
- Puedan distinguir error de código de error de entorno.
- Puedan describir el recorrido sin mirar.
- Quede evidencia recuperable.
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
