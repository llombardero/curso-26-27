# S214 — README y evidencia de ejecución

## Objetivo

Documentar H1 para que otra persona pueda comprenderlo, ejecutarlo y comprobar sus pruebas; organizar cada evidencia en su fuente de verdad y preparar enlaces profundos para la entrega.

## 1. El README explica el producto

El archivo `README.md` debe estar en la raíz del repositorio y contener, como mínimo:

1. propósito y alcance de H1;
2. requisitos para ejecutar;
3. instrucciones de ejecución;
4. ejemplo real de entrada y salida;
5. pruebas realizadas;
6. limitaciones conocidas;
7. enlace al Site de equipo si está publicado.

Modelo breve:

````markdown
# MiniJarvis H1

## Qué hace
Programa Java de consola que saluda, pide datos ficticios y muestra un cálculo.

## Qué no hace todavía
No tiene menú, memoria, ficheros ni conexión con una IA real.

## Cómo ejecutar
1. Abrir el proyecto con un JDK configurado.
2. Ejecutar `src/Main.java`.
3. Escribir los datos solicitados.

## Ejemplo de ejecución
```text
Nombre ficticio: Laura
Horas de estudio: 5
Hola, Laura.
Minutos de estudio: 300
```

## Pruebas
- entrada válida;
- entrada no convertible;
- rama verdadera del `if`;
- rama falsa del `if`.
````

## 2. Una evidencia debe demostrar algo

Una evidencia útil indica:

- qué se probó;
- con qué entrada;
- qué salida se esperaba;
- qué salida apareció;
- qué demuestra el resultado;
- dónde está el código correspondiente.

Ejemplo insuficiente:

```text
Funciona.
```

Ejemplo verificable:

```text
Prueba: rama falsa de la condición horas >= 4.
Entrada: nombre «Sam» y horas «2».
Salida esperada: «Objetivo pendiente».
Salida observada: «Objetivo pendiente».
Qué demuestra: el bloque else se ejecuta cuando la condición es falsa.
Código: enlace al commit y a las líneas relevantes.
```

Una captura sin entrada, contexto ni enlace al código no basta.

## 3. Qué corresponde a cada espacio

| Espacio | Función |
|---|---|
| Repositorio | código, historial, README y trazabilidad técnica |
| README | ejecución, pruebas, límites e instrucciones |
| Diario individual | aportación, aprendizaje, bloqueo y siguiente paso |
| Scrum de equipo | tareas, decisiones, bloqueos, review y retrospectiva |
| Site personal | selección y reflexión sobre evidencia individual |
| Site de equipo | comunicación sintética del incremento |
| Moodle | entrega oficial mediante enlaces profundos |

No copies el mismo contenido completo en varios lugares. Enlaza la fuente de verdad y sintetiza lo necesario.

## 4. Prueba cruzada

Pide a otra persona que, sin recibir instrucciones orales:

1. abra el repositorio;
2. localice el README;
3. ejecute el programa;
4. reproduzca una prueba;
5. siga un enlace de evidencia.

Registra qué paso resultó ambiguo y corrige el README.

## 5. Permisos y enlaces profundos

Un enlace profundo lleva directamente al recurso concreto: README, commit, página H1 o fila relevante. Evita enlaces a carpetas generales.

Comprueba los permisos en una ventana privada o con una cuenta distinta. Verifica:

- el repositorio abre;
- el README es visible;
- los Sites están publicados;
- las hojas permiten lectura;
- ningún enlace exige permisos que el profesorado no tiene.

## 6. Actualiza los Sites

### Site personal

Incluye una aportación concreta, una evidencia profunda, un aprendizaje, una dificultad y una mejora. No copies el diario completo.

### Site de equipo

Presenta el incremento, enlaza repositorio y README, resume una decisión, una prueba, una mejora detectada en la review y una acción de retrospectiva. No copies todo el Scrum.

## 7. Prepara el borrador de Moodle

Reúne enlaces profundos a:

- repositorio o código;
- README y pruebas;
- diario individual;
- Scrum de equipo;
- Site personal;
- Site de equipo.

Añade la identificación del equipo y una frase sobre tu aportación individual. La entrega oficial se completa en S215.

## Errores frecuentes

- Escribir solo «funciona».
- Mostrar una salida sin indicar la entrada.
- Enlazar una carpeta general en lugar del recurso concreto.
- Duplicar diario y Scrum en los Sites.
- Probar los enlaces con la misma cuenta propietaria.
- Ocultar una limitación conocida.

## Autoevaluación

Comprueba que puedes:

- explicar el contenido mínimo del README;
- convertir una captura aislada en evidencia verificable;
- distinguir la función de cada espacio;
- reproducir una prueba desde el README;
- comprobar enlaces y permisos;
- preparar un borrador completo de Moodle.

## Seguridad y uso de IA

Revisa código, capturas, historial y enlaces para eliminar datos personales, credenciales y tokens. Si una IA ayuda a redactar el README, verifica cada instrucción ejecutándola desde cero.
