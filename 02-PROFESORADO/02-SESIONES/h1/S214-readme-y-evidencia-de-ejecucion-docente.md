# S214 - Comunicar - README, evidencia y Site

| Dato | Valor |
|---|---|
| Hito | H1 — Primer asistente ejecutable |
| Duración prevista | 45 minutos |
| Fase HEXA del hito | Comunicar — evaluar y reflexionar |

> Basada en `00-GUION-DOCENTE-H1-COMPLETO.md`. Selecciona y desarrolla los conceptos, ejemplos, actividades y evidencias útiles para esta sesión.

## Qué vas a aprender

Al terminar, debes documentar H1 con un README reproducible, seleccionar evidencias verificables y comprobar permisos y enlaces profundos antes de preparar la entrega.

## Ideas y ejemplos

Úsala antes de documentar y antes de preparar Moodle.

Documentar no significa copiar la misma información en muchos sitios. Cada espacio responde a una pregunta: README explica cómo ejecutar; diario cuenta el proceso personal; Site personal selecciona aprendizaje; Site de equipo comunica el incremento; Moodle recoge enlaces oficiales.

Ejemplo de evidencia verificable:

```text
Prueba: saludo con nombre ficticio.
Entrada usada: Laura.
Salida esperada: Encantado, Laura.
Salida obtenida: Encantado, Laura.
Demuestra: la entrada leída se guarda y se usa en la salida.
Enlace: archivo o captura concreta, no carpeta general.
```

Pregunta al alumnado:

Qué demuestra esta evidencia, dónde debería estar enlazada y por qué no basta con escribir `funciona`.

Error frecuente que debes cortar:

No enlacéis carpetas generales. Enlazad la evidencia concreta.

## Actividad de la sesión

Revisad el README, preparad una evidencia de ejecución con entrada, salida esperada y salida obtenida, y comprobad desde una cuenta no propietaria que los enlaces profundos abren el recurso correcto.

## Evidencia de la sesión

1. README H1.
2. Evidencia de ejecución.
3. Diario individual revisado.
5. Site personal H1 iniciado o terminado.
6. Site de equipo H1 iniciado o terminado.
7. Borrador de entrega Moodle con enlaces.

**Dónde y cómo conservar la evidencia:**

- README: raíz del repositorio GitHub.
- Evidencia de ejecución: README, repositorio o Drive con enlace profundo; debe indicar entrada, salida esperada, salida obtenida y qué demuestra.
- Diario individual: Sheet personal, no documento aparte.
- Site personal: página H1 del Site personal.
- Site de equipo: página H1 del Site de equipo.
- Moodle: todavía puede quedar como borrador si S215 es el cierre oficial, salvo que hayas configurado plazo de entrega en S214.

Hoy no quiero que copiéis el diario en el Site. Quiero que seleccionéis. El diario contiene proceso. El Site personal contiene evidencia seleccionada y explicación. El Site de equipo comunica el incremento. Moodle cerrará la entrega oficial.

Modelo de uso del README H1:

```markdown
# MiniJarvis H1

## Qué hace
MiniJarvis saluda, pide un nombre ficticio, calcula minutos a partir de horas y muestra si se alcanza un objetivo.

## Límites de H1
No incluye menú, memoria, ficheros ni IA real.

## Cómo ejecutar
1. Abrir el proyecto en IntelliJ.
2. Ejecutar `Main.java`.
3. Introducir datos ficticios.

## Pruebas
Caso A: horas = 5 -> Objetivo alcanzado.
Caso B: horas = 2 -> Objetivo pendiente.
Entrada no convertible: "hola" falla durante la ejecución con parseInt.
```

Modelo de uso del Site personal H1:

```text
Reto con mis palabras: construir una primera versión pequeña de MiniJarvis por consola.
Mi aportación: probé Scanner y documenté una entrada no convertible.
Evidencia seleccionada: enlace profundo a la prueba S212.
Qué demuestra: entiendo el flujo pedir -> leer -> guardar -> convertir -> mostrar.
Mejora siguiente: probar mejor entradas no válidas en H2.
```

Modelo de uso del Site de equipo H1:

```text
Incremento conseguido: MiniJarvis saluda, pide nombre, calcula minutos y decide si se alcanza un objetivo.
Decisiones: no incluimos menú ni memoria porque no pertenecen a H1.
Pruebas: saludo, conversión, caso true, caso false y entrada no convertible.
Review: el incremento cumple el alcance de S206.
```

## Permisos y privacidad

Antes de decir que está entregado, comprobad permisos. Un enlace que solo abre el propietario no es una entrega válida.

Cómo comprobar:

- Abrir enlace en ventana privada o con cuenta no propietaria si es posible.
- Pedir a una pareja que abra el enlace.
- Confirmar que lleva al archivo o página concreta, no a la carpeta raíz.

## Comprueba lo aprendido

Mañana o en la siguiente sesión defenderéis. Defender no es recitar el README. Defender es señalar, ejecutar, predecir, modificar una parte pequeña y explicar qué demuestra vuestra evidencia.
