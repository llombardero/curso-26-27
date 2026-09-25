# S211 — Guía docente

## Constantes, literales y operaciones

| Dato | Valor |
|---|---|
| Hito | H1 — Primer MiniJarvis |
| Duración | 2 periodos; checkpoint proyectable de 45 minutos y taller asociado |
| Fase HEXA | Ejecutar — crear |
| Agrupamiento | Individual con contraste por parejas o equipo cuando la práctica lo requiera |
| Resultado observable | Aplicar constantes, literales y operaciones aritméticas con predicción y prueba. |
| Evidencia mínima | Quede diagnóstico. |

## Propósito

Aplicar constantes, literales y operaciones aritméticas con predicción y prueba.

El concepto se incorpora al Tema 1, pero solo pasa a `Main.java` cuando mejora el producto mínimo. Las demás prácticas se conservan como microejercicios defendibles.

## Material imprescindible

- presentación de S211;
- IntelliJ y JDK cuando haya práctica de código;
- proyecto o microarchivo de prueba;
- diario individual y tablero Scrum del equipo;
- datos ficticios.

## Secuencia de aula

| Tiempo / diap. | Tipo y actuación | Alumnado | Observa | Puerta de avance | Si hay retraso |
|---|---|---|---|---|---|
| 00:00–00:04 / D1 | EJECUTAR: Pide clasificar datos estables y cambiantes. | Decide y justifica. | Si confunden “dato fijo ahora” con constante semántica. | aparezca necesidad de final. | 3 minutos. |
| 00:04–00:09 / D2 | PÍLDORA DOCENTE 1/5: Explica que no deben cambiar durante la ejecución y por qué dan intención al código. | Convierte un dato estable en constante. | Intentos de reasignar final. | distingan variable/constante. | 4 minutos. |
| 00:09–00:14 / D3 | PÍLDORA DOCENTE 2/5: Introduce literales de forma práctica. | Identifica literales en su código. | Comillas simples/dobles. | reconozcan al menos cuatro tipos. | 3 minutos. |
| 00:14–00:21 / D4 | PÍLDORA DOCENTE 3/5: Explica que una operación produce un resultado que debemos usar/guardar si queremos trabajar con él. | Predice operaciones sencillas. | Resultado calculado pero ignorado. | puedan construir una expresión básica. | prioriza + - * / %. |
| 00:21–00:26 / D5 | EXPERIMENTO: Haz predicción antes de ejecutar. Explica cociente entero vs división real. | Predice y verifica. | Esperar 2.5 en int/int. | entiendan el papel de los tipos. | no suprimas; concepto nuclear. |
| 00:26–00:30 / D6 | PÍLDORA DOCENTE 4/5: Aclara que % no significa porcentaje. | Propone un uso. | Confusión con porcentaje. | puedan explicar qué sobra. | 2 minutos. |
| 00:30–00:34 / D7 | EXPERIMENTO: Haz resolver a mano. Conecta con precedencia matemática y paréntesis. | Calcula y verifica. | Orden de operaciones. | justifiquen el resultado. | un solo ejemplo. |
| 00:34–00:37 / D8 | PÍLDORA DOCENTE 5/5: Relaciona con asignación de S210. | Predice nuevos valores. | Creer que crea una variable nueva. | entiendan actualización. | muestra += y ++; menciona equivalentes. |
| 00:37–00:42 / D9 | ACTIVIDAD: Circula y pregunta qué entrada/datos usaron y qué esperaban. | Programa, predice, ejecuta. | División entera, % y precedencia. | haya resultado comprobado. | reduce a constante + división + salida. |
| 00:42–00:45 / D10 | CIERRE: Recoge respuestas y registra errores comunes. | Responde sin ejecutar primero. | Conceptos que necesitan reentrada en S212. | quede diagnóstico. | igual. |

## Qué debes explicar

- **PÍLDORA DOCENTE 1/5:** Explica que no deben cambiar durante la ejecución y por qué dan intención al código.
- **PÍLDORA DOCENTE 2/5:** Introduce literales de forma práctica.
- **PÍLDORA DOCENTE 3/5:** Explica que una operación produce un resultado que debemos usar/guardar si queremos trabajar con él.
- **PÍLDORA DOCENTE 4/5:** Aclara que % no significa porcentaje.
- **PÍLDORA DOCENTE 5/5:** Relaciona con asignación de S210.

## Ejemplo o demostración preparada

**D1 · ¿Qué datos deberían cambiar? —** Nombre del asistente · curso · horas de estudio · contador de tareas

**D2 · Constantes con final —** final String ASSISTANT_NAME = "MiniJarvis";<br>
final int START_YEAR = 2026;

**D3 · Literal = valor escrito directamente —** NÚMEROS: 5 / 3.5 \| TEXTO/CARÁCTER: "Hola" / 'A' \| LÓGICO: true / false

**D4 · Operadores aritméticos —** + suma<br>
- resta<br>
\* multiplicación<br>
/ división o cociente<br>
% resto

**D5 · ¿Qué devuelve 5 / 2? —** ENTEROS: int a = 5 / 2;<br>
→ 2 \| CON DECIMAL: double b = 5 / 2.0;<br>
→ 2.5

**D6 · El resto % —** 10 caramelos / 4 personas<br>
<br>
10 / 4 → 2 para cada una<br>
10 % 4 → 2 sobran

**D7 · Precedencia y paréntesis —** int result = 8 \* (4 + 2) - 3;<br>
<br>
// Predice antes de ejecutar

**D8 · Actualizar sin reescribir todo —** tasks += 2;<br>
tasks -= 1;<br>
tasks++;<br>
tasks--;

**D9 · Micropráctica: calcula y demuestra —** Usa una constante, una variable, una operación, una actualización y una salida que permita comprobar el resultado.

**D10 · Dos predicciones antes de salir —** 5 / 2 → ?<br>
5 / 2.0 → ?<br>
10 % 4 → ?

## Consigna que se entrega al alumnado

1. Predice antes de ejecutar cuando haya código.
2. Realiza la micropráctica o modificación prevista.
3. Prueba el caso normal y, cuando exista una decisión o conversión, también el caso alternativo o erróneo.
4. Conserva el código o resultado en el repositorio o espacio indicado.
5. Registra una sola entrada en el diario individual; no crees un informe paralelo.

## Qué observar mientras trabajan

- Si confunden “dato fijo ahora” con constante semántica.
- Intentos de reasignar final.
- Comillas simples/dobles.
- Resultado calculado pero ignorado.
- Esperar 2.5 en int/int.
- Confusión con porcentaje.
- Orden de operaciones.
- Creer que crea una variable nueva.
- División entera, % y precedencia.
- Conceptos que necesitan reentrada en S212.

## Criterios para considerar cerrada la sesión

- Aparezca necesidad de final.
- Distingan variable/constante.
- Reconozcan al menos cuatro tipos.
- Puedan construir una expresión básica.
- Entiendan el papel de los tipos.
- Puedan explicar qué sobra.
- Justifiquen el resultado.
- Entiendan actualización.
- Haya resultado comprobado.
- Quede diagnóstico.
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
