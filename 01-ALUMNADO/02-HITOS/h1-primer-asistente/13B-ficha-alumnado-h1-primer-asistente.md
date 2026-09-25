# H1 — Primer MiniJarvis

## 1. Reto

Construirás la primera versión ejecutable de MiniJarvis en Java. Debe recibir datos, mostrar una salida clara y demostrar los conceptos del Tema 1 sin convertirse todavía en un menú completo.

El producto principal será pequeño. Algunas ideas —conversiones, comparaciones, booleanos y una decisión básica— se demostrarán mediante microprácticas separadas cuando añadirlas a `Main.java` complique el programa sin aportar valor.

## 2. Producto mínimo

`Main.java` debe:

1. iniciar en `public static void main(String[] args)`;
2. mostrar una presentación clara de MiniJarvis;
3. pedir al menos un dato mediante `Scanner`;
4. guardar datos en variables con tipos adecuados;
5. utilizar al menos una constante con `final`;
6. realizar una operación sencilla útil;
7. mostrar una respuesta que combine texto y datos;
8. compilar y ejecutarse de forma repetible.

H1 no necesita menú, bucle de interacción, `switch`, colecciones, persistencia, clases propias adicionales ni conexión con una IA real. Esas ampliaciones pertenecen a hitos posteriores.

## 3. Conceptos del Tema 1 que debes poder demostrar

| Bloque | Debes poder… | Evidencia admitida |
|---|---|---|
| Entorno Java | distinguir código fuente, JDK, compilación, JVM y ejecución | proyecto ejecutable y explicación |
| Estructura | localizar clase, método `main`, instrucciones, comentarios y errores básicos | `Main.java` y micropráctica |
| Datos | declarar, inicializar, asignar y actualizar variables de tipos básicos | producto o micropráctica |
| Constantes y literales | usar `final` y reconocer literales | producto o micropráctica |
| Operaciones | predecir y comprobar operaciones y precedencia elemental | micropráctica |
| Entrada y conversión | leer texto, convertirlo y explicar un error de conversión | micropráctica |
| Comparaciones y lógica | obtener y combinar valores `boolean` | micropráctica |
| Decisión básica | leer y probar un `if/else` con sus dos caminos | micropráctica |

En H2 aplicarás las decisiones a un menú, comandos, repetición, validación y depuración. En H1 solo necesitas comprender y probar la decisión básica.

## 4. Recorrido de 24 periodos

| Checkpoint | Periodos | Fase HEXA | Núcleo |
|---|---:|---|---|
| S206 | 2 | Activar | reto, alcance y salida esperada |
| S207 | 3 | Investigar | JDK, proyecto, compilación, JVM y errores |
| S208 | 2 | Investigar | lenguaje, clase, `main`, comentarios y sintaxis |
| S209 | 2 | Idear | alternativas de salida y concatenación |
| S210 | 2 | Planificar | variables, tipos y plan mínimo |
| S211 | 2 | Ejecutar | constantes, literales, operaciones y actualización |
| S212 | 3 | Ejecutar | `Scanner`, conversiones y errores de conversión |
| S213 | 3 | Ejecutar | comparaciones, lógica e `if/else` básico |
| S214 | 3 | Comunicar | README, prueba cruzada, diario y Sites |
| S215 | 2 | Comunicar | defensa, recuperación y cierre |
| **Total** | **24** |  |  |

Cada ficha S206-S215 organiza un checkpoint proyectable de 45 minutos. El resto de sus periodos se dedica a práctica, construcción, apoyo y recuperación.

<!-- HEXA-CICLO-COMPLETO-POR-HITO:START -->

### Ciclo HEXA canónico de H1

1. **1 — Activar** — entender el reto y delimitar el producto.
2. **2 — Investigar** — aprender lo necesario sobre entorno, estructura y salida.
3. **3 — Idear** — proponer mensajes y comportamiento mínimo.
4. **4 — Planificar** — organizar datos, operaciones, tareas y pruebas.
5. **5 — Ejecutar** — crear, convertir, comparar, decidir y comprobar.
6. **6 — Comunicar** — documentar, enlazar, defender y reflexionar.

<!-- HEXA-CICLO-COMPLETO-POR-HITO:END -->

## 5. Forma de trabajo

1. Predice antes de ejecutar.
2. Realiza la modificación o micropráctica.
3. Prueba y compara el resultado con la predicción.
4. Corrige el error con la pista mínima necesaria.
5. Conserva el código o enlaza la prueba.
6. Registra una única entrada breve en el diario individual al cerrar el checkpoint.
7. Actualiza Scrum solo cuando exista una tarea, decisión o bloqueo de equipo.

## 6. Evidencia única

| Necesidad | Fuente de verdad | No debes duplicar en… |
|---|---|---|
| Producto y trazabilidad técnica | repositorio, código, commits y README | documentos paralelos |
| Ejecución y pruebas | sección del README con transcripción o enlace profundo | ficha independiente de ejecución |
| Proceso individual | diario individual: una fila por checkpoint significativo | registro repetido por sesión y portfolio |
| Proceso de equipo | Sheet Scrum | actas y tableros paralelos |
| Uso personal de IA | columnas de IA del diario individual | un segundo registro salvo petición docente |
| Uso de IA del equipo | pestaña `REGISTRO_IA_EQUIPO` de Scrum | copias personales idénticas |
| Selección y reflexión | Site personal | copia completa del diario |
| Comunicación del incremento | Site de equipo | copia completa de Scrum |
| Entrega | Moodle con enlaces profundos | nueva subida de las mismas evidencias |
| Comprensión y autoría | defensa y modificación en directo | cuestionario escrito duplicado |

Las plantillas auxiliares son apoyos. Solo se entregan como archivos separados si el profesorado lo solicita expresamente.

## 7. Contenido mínimo del README

- propósito y alcance de H1;
- requisitos para ejecutar;
- instrucciones de ejecución;
- ejemplo o transcripción real de entrada y salida;
- pruebas realizadas, incluida una conversión o decisión cuando proceda;
- limitaciones conocidas;
- enlace al Site de equipo si está publicado.

## 8. Sites

### Site personal

Selecciona una aportación, una evidencia profunda, un aprendizaje, un bloqueo y una mejora. Resume: no copies el diario.

### Site de equipo

Presenta el incremento, enlaza el repositorio y el README, resume una decisión, una prueba, una mejora de review y una acción de retrospectiva. Resume: no copies Scrum.

Comprueba los permisos de lectura con una cuenta diferente antes de entregar.

## 9. Uso de IA

La IA puede ayudarte a comprender un concepto, interpretar un error, revisar claridad o preparar preguntas de defensa. No debe generar un producto completo que no puedas explicar.

Cuando el uso sea sustantivo registra:

- finalidad;
- prompt o resumen fiel;
- resultado utilizado;
- cambios propios;
- forma de validación.

Si no utilizas IA, marca “No” en el diario; no redactes una declaración adicional.

## 10. Entrega

Entrega en Moodle enlaces profundos a:

1. repositorio o carpeta de código;
2. README con ejecución y pruebas;
3. diario individual;
4. Sheet Scrum;
5. Site personal;
6. Site de equipo.

No entregues archivos vacíos “por si acaso”.

## 11. Defensa

Debes poder:

- ejecutar H1;
- localizar el punto de entrada;
- explicar variables, tipos, constantes, operaciones y `Scanner`;
- explicar una conversión y un posible error;
- predecir comparaciones y booleanos;
- probar las dos ramas de un `if/else` básico;
- distinguir lo que está en el producto de lo que se demostró como micropráctica;
- realizar una modificación pequeña;
- justificar y validar cualquier uso de IA.

## 12. Criterio de terminado

H1 está terminado cuando:

- el producto mínimo compila y se ejecuta;
- las microprácticas cubren los conceptos del Tema 1 que no están en `Main.java`;
- las pruebas son localizables mediante enlaces profundos;
- diario y Scrum están actualizados sin duplicidades;
- Sites sintetizan, no copian;
- los permisos han sido comprobados;
- cada persona puede defender y modificar su trabajo.
