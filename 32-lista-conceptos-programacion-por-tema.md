# Lista de conceptos de Programación trabajados por tema

## Curso 2026/2027 — 1.º DAW — Programación + MiniJarvis

Documento de análisis curricular de los temas existentes en la carpeta `documentacion/`.

Carpeta analizada:

```text
/mnt/compartido/Hlanz/Programacion/Curso 2026-2027/documentacion/
```

Documentos fuente de Programación analizados:

```text
Tema 1. Aspectos básicos de la programación.pdf
Tema 2.La programacion orientada a objetos.pdf
tema 3. La programación estructurada.pdf
Tema 4. Estructuras de Datos.pdf
Tema 5. Programacion Basica Clases.pdf
Tema 6. Programacion Avanzada Clases.pdf
Tema 7: Introduccion Programacion Funcional.pdf
Tema 8: Aplicaciones con interfaz gráfica de escritorio.pdf
```

Método de análisis:

- Extracción textual ad-hoc con `pdftotext -layout`.
- Revisión de encabezados internos detectados.
- Síntesis docente de conceptos de programación realmente trabajados en cada tema.
- Separación entre conceptos nucleares, conceptos de apoyo, casos prácticos probables y relación con MiniJarvis.

Nota importante:

Algunos PDF contienen texto extraído con ruido visual o caracteres sueltos. La estructura de apartados sí se pudo recuperar con suficiente claridad para construir este mapa de conceptos.

---

# 1. Resumen ejecutivo

Los temas de la carpeta `documentacion/` cubren una progresión clásica de Programación en Java:

```text
Tema 1  → fundamentos: variables, tipos, operadores, entrada/salida, if
Tema 2  → primera visión de POO: clases, objetos, métodos, constructores, excepciones, herencia inicial
Tema 3  → programación estructurada: secuencia, condiciones, switch, bucles, eficiencia
Tema 4  → estructuras de datos: colecciones, listas, arrays, sets, maps
Tema 5  → programación básica de clases: atributos, constructores, métodos, tests, TDD, interfaces, records, enum
Tema 6  → programación avanzada de clases: encapsulación, herencia, polimorfismo, abstractas, Object, Comparable, patrones
Tema 7  → programación funcional: lambdas, funciones de orden superior, streams, Optional
Tema 8  → GUI, eventos, JavaFX, MVC, arquitectura hexagonal y persistencia con base de datos
```

Para el curso MiniJarvis, la secuencia más natural no es seguir los temas de forma lineal exacta, sino reorganizar sus conceptos alrededor de los hitos del proyecto.

---

# 2. Tema 1 — Aspectos básicos de la programación

Archivo fuente:

```text
Tema 1. Aspectos básicos de la programación.pdf
```

## Apartados detectados

```text
1.- Introducción
2.- Objetivos de la programación
2.- Primeros aspectos léxicos
3.- Comentarios
4.- El almacenamiento de datos
4.1.- Variables
4.2.- Los tipos de datos
4.3.- Las variables en el lenguaje Java
4.2.- Los literales
4.3.- Mostrar variables por pantalla
4.4.- Pedir datos por teclado al usuario
5.- Operaciones con variables
5.1.- Asignación
5.2.- Operaciones numéricas
5.3.- Comparación
5.4.- Operaciones con variables booleanas
6.- Conversiones entre variables
6.1.- Conversión implícita
6.2.- Conversión explícita (casting)
6.3.- Conversiones entre String y tipos básicos
7.- La estructura condicional
8.1.- El bloque if-else
8.2.- La asignación condicional
```

## Conceptos de programación trabajados

### 2.1. Conceptos iniciales

- Qué es programar.
- Objetivo de un programa.
- Programa como secuencia de instrucciones.
- Código fuente frente a ejecución.
- Primeros programas sencillos.
- Sintaxis básica de Java.
- Errores iniciales de escritura.

### 2.2. Aspectos léxicos y estilo básico

- Palabras reservadas.
- Identificadores.
- Uso de mayúsculas y minúsculas.
- Separadores y signos básicos.
- Llaves, paréntesis, punto y coma.
- Comentarios de una línea y de bloque.
- Legibilidad mínima del código.

### 2.3. Datos, variables y tipos

- Variable como espacio de almacenamiento.
- Nombre de variable.
- Declaración de variables.
- Inicialización de variables.
- Asignación de valores.
- Tipos primitivos.
- Tipos numéricos enteros.
- Tipos numéricos decimales.
- Tipo `char`.
- Tipo `boolean`.
- Tipo `String` como texto.
- Literales numéricos, textuales y booleanos.

### 2.4. Entrada y salida

- Mostrar información por pantalla.
- Concatenación de texto y variables.
- Lectura de datos desde teclado.
- Uso inicial de `Scanner`.
- Diferencia entre pedir, almacenar y procesar datos.

### 2.5. Operadores

- Operador de asignación.
- Operadores aritméticos.
- Operadores de comparación.
- Operadores booleanos.
- Expresiones.
- Precedencia básica de operadores.

### 2.6. Conversiones

- Conversión implícita entre tipos compatibles.
- Conversión explícita o casting.
- Conversión entre `String` y tipos básicos.
- Riesgos de conversión incorrecta.
- Errores frecuentes al leer números desde teclado.

### 2.7. Primera toma de decisiones

- Estructura condicional `if`.
- Estructura `if-else`.
- Condiciones booleanas.
- Asignación condicional.
- Control básico del flujo del programa.

## Casos prácticos sugeridos para alumnado

- MiniJarvis saluda al usuario por su nombre.
- MiniJarvis pregunta el módulo favorito y responde con un mensaje personalizado.
- MiniJarvis calcula una puntuación sencilla.
- MiniJarvis decide si una entrada está vacía o no.
- MiniJarvis muestra un pequeño diagnóstico usando una condición.

## Relación con MiniJarvis

Este tema alimenta principalmente:

```text
H1 — Primer asistente básico
H2 — Primeras decisiones y depuración
```

Conceptos clave que deben quedar dominados antes de avanzar:

- variable;
- tipo de dato;
- entrada/salida;
- expresión;
- condición;
- `if/else`;
- lectura de teclado;
- errores de sintaxis básicos.

---

# 3. Tema 2 — La programación orientada a objetos

Archivo fuente:

```text
Tema 2.La programacion orientada a objetos.pdf
```

## Apartados detectados

```text
1.- Introducción
2.- La programación orientada a objetos
2.1.- Perfiles del programador
3.- Clases y objetos
3.1.- Las clases
3.1.- Los objetos
3.3.- Utilización de una librería
4.- Métodos constructores
5.- Métodos de instancia
4.1.- Uso de métodos procedimiento
5.2.- Uso de métodos función
6.- Documentación de las clases
6.1.- Javadoc
6.2.- Diagrama de clases
7.- Excepciones
7.1.- Reconocimiento de métodos “peligrosos”
7.2.- El bloque try-catch
7.3.- Tipos de excepciones
8.- Herencia
8.1.- La clase Object
8.2.- La abstracción
10.- Métodos estáticos
11.- Constantes
12.- Tipos de dato referencia
13.1.- Representación en memoria de los tipos básicos
13.2.- Representación en memoria de los tipos referencia
```

## Conceptos de programación trabajados

### 3.1. Introducción a la orientación a objetos

- Programación orientada a objetos como forma de modelar entidades.
- Diferencia entre programa procedural y programa con objetos.
- Clase como plantilla.
- Objeto como instancia.
- Estado de un objeto.
- Comportamiento de un objeto.
- Responsabilidad de una clase.

### 3.2. Clases y objetos

- Definición de clase.
- Creación de objetos.
- Uso de `new`.
- Referencias a objetos.
- Diferencia entre variable primitiva y variable referencia.
- Uso de librerías existentes.
- Uso de clases predefinidas.

### 3.3. Constructores

- Constructor como método especial de creación.
- Parámetros del constructor.
- Inicialización de objetos.
- Constructor por defecto.
- Sobrecarga inicial de constructores.

### 3.4. Métodos de instancia

- Método procedimiento: realiza una acción.
- Método función: devuelve un valor.
- Parámetros de métodos.
- Valor de retorno.
- Llamada a métodos sobre objetos.
- Diferencia entre dato interno y resultado calculado.

### 3.5. Documentación y diagramas

- Documentar clases.
- Introducción a Javadoc.
- Diagrama de clases.
- Relación entre clase escrita en código y clase representada gráficamente.
- Lectura básica de un diagrama.

### 3.6. Excepciones

- Método peligroso.
- Concepto de excepción.
- Bloque `try-catch`.
- Tipos de excepciones.
- Manejo básico de errores en ejecución.

### 3.7. Herencia y abstracción inicial

- Herencia como relación entre clases.
- Clase base y clase derivada.
- Clase `Object`.
- Abstracción como simplificación de lo relevante.

### 3.8. Miembros estáticos y constantes

- Método estático.
- Diferencia entre método de instancia y método estático.
- Constantes.
- Valores compartidos por una clase.

### 3.9. Memoria y referencias

- Tipos básicos en memoria.
- Tipos referencia en memoria.
- Diferencia entre copiar un valor y copiar una referencia.
- Riesgo de confundir objeto con variable que lo referencia.

## Casos prácticos sugeridos para alumnado

- Clase `Agent` con nombre y método `greet()`.
- Clase `Memory` con responsabilidades iniciales.
- Clase `Message` o `AiResponse` simple.
- Diagrama de clases de una versión mínima de MiniJarvis.
- Ejercicio de explicar qué objeto recibe qué mensaje.

## Relación con MiniJarvis

Este tema alimenta principalmente:

```text
H4 — Agente orientado a objetos
```

También prepara parte de:

```text
H5 — Extensibilidad mediante herramientas
H6 — Persistencia separando responsabilidades
```

Conceptos clave que deben quedar dominados:

- clase;
- objeto;
- atributo;
- método;
- constructor;
- referencia;
- método de instancia;
- diagrama de clases;
- excepción básica.

---

# 4. Tema 3 — La programación estructurada

Archivo fuente:

```text
tema 3. La programación estructurada.pdf
```

## Apartados detectados

```text
1.- Introducción
2.- La estructura secuencial
3.- La estructura condicional
3.1.- El bloque switch-case
3.2.- El switch mejorado (enhanced switch)
4.- La estructura iterativa
4.1.- Las repeticiones en la vida real
4.2.- Las repeticiones en el lenguaje Java
5.- El bucle while
5.1.- El bucle do-while
6.- El bucle for
6.1.- Repeticiones mixtas
6.2.- Generación de números
7.- La estructura iterativa anidada
9.- Análisis de la eficiencia de un programa
```

## Conceptos de programación trabajados

### 4.1. Programación estructurada

- Secuencia.
- Selección.
- Iteración.
- Flujo de ejecución.
- Lectura del programa de arriba abajo.
- Bloques de código.

### 4.2. Estructura secuencial

- Instrucciones consecutivas.
- Orden de ejecución.
- Dependencia entre instrucciones.
- Estado de las variables tras cada paso.

### 4.3. Estructura condicional

- Condiciones simples.
- Condiciones compuestas.
- `if`.
- `if-else`.
- Condiciones encadenadas.
- Elección entre caminos alternativos.

### 4.4. `switch`

- `switch-case` clásico.
- `break`.
- Caso por defecto.
- `switch` mejorado.
- Selección por comando o por valor discreto.

### 4.5. Bucles

- Repetición controlada.
- Bucle `while`.
- Bucle `do-while`.
- Bucle `for`.
- Variable de control.
- Condición de salida.
- Riesgo de bucle infinito.
- Repeticiones mixtas.

### 4.6. Iteración anidada

- Bucle dentro de bucle.
- Recorridos por filas y columnas.
- Complejidad creciente de la lectura del código.

### 4.7. Generación de números

- Generación de valores.
- Uso probable de números aleatorios o secuencias.
- Casos de simulación.

### 4.8. Eficiencia

- Primer contacto con coste de un programa.
- Comparación entre soluciones.
- Impacto de bucles anidados.
- Idea inicial de rendimiento.

## Casos prácticos sugeridos para alumnado

- Menú principal de MiniJarvis con comandos.
- Bucle principal hasta escribir `salir`.
- Comando `ayuda`.
- Comando desconocido.
- Uso de `switch` para seleccionar acciones.
- Repetición de preguntas hasta obtener una entrada válida.

## Relación con MiniJarvis

Este tema alimenta principalmente:

```text
H1 — Asistente básico interactivo
H2 — Agente con decisiones y depuración
```

Y sirve de base para:

```text
H5 — Refactorizar menú con muchos comandos
```

Conceptos clave que deben quedar dominados:

- secuencia;
- condición;
- `switch`;
- bucle `while`;
- bucle `for`;
- menú;
- condición de salida;
- eficiencia básica.

---

# 5. Tema 4 — Estructuras de datos

Archivo fuente:

```text
Tema 4. Estructuras de Datos.pdf
```

## Apartados detectados

```text
1.- Introducción
2.- Estructuras de datos
3.- El Java Collection Framework
4.- La interfaz Collection<T>
5.- La interfaz List<T>
6.- Recorrido de una lista
7.- El for mejorado
8.- Listas mutables e inmutables
9.- Las clases envoltorio
10.- Arrays
11.- Tablas
12.- La interfaz Set<T>
13.- La interfaz Map<K,V>
```

## Conceptos de programación trabajados

### 5.1. Estructuras de datos

- Necesidad de organizar varios datos.
- Diferencia entre variable simple y colección.
- Agrupación de elementos.
- Recorrido de elementos.
- Selección de estructura según necesidad.

### 5.2. Java Collection Framework

- Marco de colecciones de Java.
- Interfaces y clases de colección.
- Tipos genéricos.
- `Collection<T>`.
- Operaciones comunes sobre colecciones.

### 5.3. Listas

- `List<T>`.
- Orden de inserción.
- Índices.
- Añadir elementos.
- Consultar elementos.
- Eliminar elementos.
- Tamaño de una lista.
- Recorrido completo de una lista.

### 5.4. Recorridos

- Bucle `for` tradicional.
- `for` mejorado.
- Recorrido seguro de una colección.
- Diferencia entre recorrer y modificar.

### 5.5. Mutabilidad

- Lista mutable.
- Lista inmutable.
- Riesgos de modificar estructuras compartidas.
- Decisión entre proteger o permitir cambios.

### 5.6. Clases envoltorio

- `Integer`, `Double`, `Boolean`, etc.
- Diferencia entre primitivo y objeto envoltorio.
- Relación con colecciones genéricas.

### 5.7. Arrays y tablas

- Array como estructura de tamaño fijo.
- Acceso por índice.
- Diferencias entre array y lista.
- Tablas o estructuras bidimensionales.

### 5.8. Sets y maps

- `Set<T>` como colección sin repetidos.
- `Map<K,V>` como asociación clave-valor.
- Diferencia entre lista, conjunto y mapa.
- Casos de uso de búsqueda por clave.

## Casos prácticos sugeridos para alumnado

- `Memory` guarda recuerdos en una `List<String>`.
- MiniJarvis muestra recuerdos numerados.
- MiniJarvis evita recuerdos vacíos.
- MiniJarvis detecta recuerdos repetidos usando un `Set`.
- MiniJarvis guarda preferencias por clave usando un `Map`.

## Relación con MiniJarvis

Este tema alimenta principalmente:

```text
H3 — Agente con memoria en colecciones
```

Y prepara:

```text
H6 — Persistencia de recuerdos en fichero
```

Conceptos clave que deben quedar dominados:

- colección;
- lista;
- índice;
- recorrido;
- `for` mejorado;
- mutable/inmutable;
- array;
- set;
- map;
- genéricos.

---

# 6. Tema 5 — Programación básica de clases

Archivo fuente:

```text
Tema 5. Programacion Basica Clases.pdf
```

## Apartados detectados

```text
1.- Introducción
2.- Estructura interna de una clase
3.- Programación de una clase
3.1.- Programación de las propiedades
3.2.- El constructor por defecto
3.3.- Acceso público a las propiedades (mala práctica!!)
4.- Programación de métodos constructores
4.1.- Protección de las propiedades
4.2.- Programación de varios constructores
4.3.- Constructor principal y constructores secundarios
5.- Test de las clases
5.1.- Test unitarios
5.2.- Asertos
6.- Test Driven Development (TDD)
7.- Programación de métodos de instancia
7.1.- Programación de métodos procedimiento
7.2.- Programación de métodos función
8.- Programación de métodos que lanzan excepciones
8.1.- Métodos que lanzan RuntimeExceptions
8.2.- Métodos que lanzan CheckedExceptions
8.3.- Programar un método sin usar try-catch en su interior
9.- Programación de métodos recursivos
10.- Programación de métodos estáticos
11.- Propiedades estáticas
12.- Interfaces
12.1.- Programación de una interfaz
12.2.- Implementación de una interfaz
12.3.- Métodos default
12.4.- Métodos privados en interfaces
13.- Records
13.1.- Inmutabilidad y records
14.- Enumeraciones
```

## Conceptos de programación trabajados

### 6.1. Diseño básico de clases

- Clase como unidad de código.
- Paquetes.
- Propiedades o atributos.
- Variables de instancia.
- Métodos.
- Constructores.
- Separación entre clase de modelo y clase de interacción.
- División de un programa en clases.

### 6.2. Propiedades y visibilidad

- Propiedades privadas.
- Acceso público a propiedades como mala práctica.
- Protección del estado interno.
- Relación entre atributos del diagrama y atributos del código.
- Modificadores de acceso.

### 6.3. Constructores

- Constructor por defecto.
- Constructor con parámetros.
- Validación dentro del constructor.
- Sobrecarga de constructores.
- Constructor principal.
- Constructores secundarios.
- Uso de `this`.
- Encadenamiento de constructores.

### 6.4. Tests

- Test de clases.
- Test unitario.
- Asertos.
- Comprobación de comportamiento esperado.
- Diferencia entre probar manualmente y automatizar una comprobación.

### 6.5. TDD

- Test Driven Development.
- Escribir una prueba antes o junto al código.
- Ciclo rojo-verde-refactor.
- Programar con criterios de éxito explícitos.

### 6.6. Métodos de instancia

- Métodos procedimiento.
- Métodos función.
- Parámetros.
- Retorno.
- Efectos secundarios.
- Lectura y modificación del estado del objeto.

### 6.7. Métodos con excepciones

- Métodos que lanzan `RuntimeException`.
- Métodos que lanzan checked exceptions.
- Firma de método con `throws`.
- Delegar el manejo de la excepción.
- Diferencia entre lanzar y capturar.

### 6.8. Recursividad

- Método recursivo.
- Caso base.
- Caso recursivo.
- Riesgo de recursión infinita.
- Comparación con solución iterativa.

### 6.9. Miembros estáticos

- Métodos estáticos.
- Propiedades estáticas.
- Diferencia entre lo que pertenece al objeto y lo que pertenece a la clase.
- Riesgos de usar estado global innecesario.

### 6.10. Interfaces

- Interfaz como contrato.
- Implementación de una interfaz.
- Métodos default.
- Métodos privados en interfaces.
- Uso de interfaces para desacoplar.

### 6.11. Records y enumeraciones

- `record` como clase de datos compacta.
- Inmutabilidad en records.
- `enum` para conjuntos cerrados de valores.
- Evitar cadenas mágicas cuando hay opciones fijas.

## Casos prácticos sugeridos para alumnado

- Clase `Memory` con constructor, métodos y validaciones.
- Clase `Agent` con métodos de instancia.
- Tests de `Memory`.
- Test de comando `remember`.
- Interfaz `Tool`.
- Implementaciones `HelpTool`, `RememberTool`, `StatusTool`.
- `enum CommandType` si procede.
- `record AiResponse` si procede en H7.

## Relación con MiniJarvis

Este tema alimenta principalmente:

```text
H4 — Agente orientado a objetos
H5 — Agente extensible, clean code y patrones iniciales
```

También prepara:

```text
H6 — Clases PersistentMemory y HistoryLog
H7 — AiResponse como posible record
```

Conceptos clave que deben quedar dominados:

- atributo privado;
- constructor;
- validación;
- test unitario;
- TDD básico;
- método de instancia;
- excepción;
- interfaz;
- implementación;
- record;
- enum.

---

# 7. Tema 6 — Programación avanzada de clases

Archivo fuente:

```text
Tema 6. Programacion Avanzada Clases.pdf
```

## Apartados detectados

```text
1.- Introducción
2.- Encapsulamiento
2.1.- El modificador de acceso por defecto
2.2.- El modificador de acceso por defecto en una clase
3.- Herencia
3.1.- El constructor de la clase hija
3.2.- El modificador de acceso protected
3.3.- Creación de excepciones propias
3.5.- El operador instanceof
3.6.- Herencia de interfaces
4.- Sobreescritura de métodos
4.1.- Ampliar la funcionalidad de un método heredado
5.- Métodos de la clase Object
5.1.- Sobreescritura de toString
5.2.- Sobreescritura de equals
5.3.- Sobreescritura de hashCode
6.- La interfaz Comparable<T>
7.- Clases abstractas
7.1.- Métodos abstractos
8.- Polimorfismo
8.1.- Polimorfismo mediante clases abstractas
8.2.- Polimorfismo mediante interfaces
9.- Clases anónimas
11.- Clases finales
11.1.- Clases selladas
12.- Patrones de diseño
```

## Conceptos de programación trabajados

### 7.1. Encapsulamiento avanzado

- Propiedades privadas.
- Métodos públicos controlados.
- Invariantes.
- Estado consistente.
- Modificador por defecto o package-private.
- Clase no pública.
- Control de visibilidad en paquetes.

### 7.2. Herencia

- Clase padre.
- Clase hija.
- `extends`.
- Constructor de la clase hija.
- Uso de `super`.
- Modificador `protected`.
- Herencia de interfaces.
- Riesgos de jerarquías mal diseñadas.

### 7.3. Excepciones propias

- Crear una excepción propia.
- Heredar de `Exception`.
- Mensajes de error significativos.
- Excepciones de dominio.

### 7.4. `instanceof`

- Comprobación de tipo real.
- Pattern matching con `instanceof`.
- Riesgo de abusar de comprobaciones de tipo.
- Relación con polimorfismo.

### 7.5. Sobreescritura

- `@Override`.
- Redefinir comportamiento heredado.
- Ampliar funcionalidad de un método heredado.
- Compatibilidad de tipos de retorno y excepciones.

### 7.6. Métodos de `Object`

- `toString`.
- `equals`.
- `hashCode`.
- Importancia de representar y comparar objetos correctamente.
- Relación entre `equals` y colecciones.

### 7.7. Ordenación y comparación

- `Comparable<T>`.
- Método `compareTo`.
- Orden natural.
- Ordenación de objetos.

### 7.8. Abstracción y polimorfismo

- Clase abstracta.
- Método abstracto.
- Polimorfismo mediante clases abstractas.
- Polimorfismo mediante interfaces.
- Usar un tipo general para objetos concretos.
- Sustitución de implementaciones.

### 7.9. Clases especiales

- Clases anónimas.
- Clases finales.
- Clases selladas.
- Restricción de herencia.

### 7.10. Patrones de diseño

- Introducción explícita a patrones de diseño.
- Patrones como solución a problemas recurrentes.
- No aplicar patrones sin necesidad.
- Posible relación con Strategy, Command, Factory o Builder según ejemplos concretos del tema.

## Casos prácticos sugeridos para alumnado

- `Tool` como interfaz polimórfica.
- Lista de herramientas tratadas como `List<Tool>`.
- `HelpTool`, `RememberTool`, `StatusTool` como implementaciones.
- `Command` simplificado para comandos del agente.
- `PromptSafety` como política separada.
- `AiAssistant` como abstracción si se quiere intercambiar simulación y proveedor real.

## Relación con MiniJarvis

Este tema alimenta principalmente:

```text
H5 — Extensibilidad, clean code y patrones iniciales
H7 — Integración IA responsable o simulación robusta
```

La introducción de patrones debe hacerse aquí o al final de H5, no antes.

Motivo:

```text
El alumnado ya habrá visto clases, objetos, métodos, interfaces y el problema real de un Agent con demasiados if/else.
```

Conceptos clave que deben quedar dominados:

- encapsulación;
- invariante;
- herencia;
- `super`;
- `protected`;
- excepción propia;
- `@Override`;
- `toString`;
- `equals`;
- `hashCode`;
- `Comparable`;
- clase abstracta;
- polimorfismo;
- patrón de diseño aplicado a un problema real.

---

# 8. Tema 7 — Introducción a la programación funcional

Archivo fuente:

```text
Tema 7: Introduccion Programacion Funcional.pdf
```

## Apartados detectados

```text
1.- Introducción
2.- Expresiones lambda
2.1.- Interfaces funcionales predefinidas
2.2.- Expresiones lambda
2.3.- Simplificación de las expresiones lambda
2.4.- Inmutabilidad y funciones puras
2.3.- Restricciones de las expresiones lambda
3.- Funciones de orden superior
3.1.- Borrar elementos de una lista
3.2.- Procesar todos los elementos de una lista
3.3.- Actualizar todos los elementos de una lista
3.4.- Ordenar una lista por distintos criterios
4.- Streams
4.1.- Optional
4.2.- Distintos orígenes de datos
5.- Referencias a métodos
```

## Conceptos de programación trabajados

### 8.1. Programación funcional en Java

- Programación funcional como estilo complementario.
- Funciones como valores.
- Comportamiento pasado como parámetro.
- Menos estado mutable.

### 8.2. Lambdas

- Expresión lambda.
- Sintaxis de lambda.
- Parámetros de una lambda.
- Cuerpo de una lambda.
- Simplificación de lambdas.
- Restricciones de uso.

### 8.3. Interfaces funcionales

- Interfaz funcional.
- Interfaces funcionales predefinidas.
- Relación entre lambda e interfaz funcional.
- Uso probable de `Predicate`, `Consumer`, `Function`, `Supplier` o comparadores.

### 8.4. Inmutabilidad y funciones puras

- Evitar modificar estado innecesariamente.
- Función pura.
- Entrada y salida predecible.
- Menor riesgo de efectos secundarios.

### 8.5. Funciones de orden superior

- Función que recibe otra función.
- Procesamiento de listas.
- Borrar elementos según criterio.
- Procesar todos los elementos.
- Actualizar elementos.
- Ordenar por distintos criterios.

### 8.6. Streams

- Stream como flujo de datos.
- Operaciones intermedias.
- Operaciones terminales.
- Filtrado.
- Transformación.
- Reducción o recogida de resultados.
- Orígenes de datos.

### 8.7. Optional y referencias a métodos

- `Optional` para representar posible ausencia de valor.
- Evitar algunos `null`.
- Referencias a métodos.
- Código más expresivo cuando procede.

## Casos prácticos sugeridos para alumnado

- Filtrar recuerdos de MiniJarvis por palabra clave.
- Ordenar recuerdos por longitud o fecha.
- Transformar una lista de comandos a texto de ayuda.
- Buscar una herramienta con `stream()`.
- Usar `Optional<Tool>` para comando no encontrado.

## Relación con MiniJarvis

Este tema es más avanzado y puede usarse como ampliación o mejora:

```text
H5 — búsqueda de herramientas
H6 — filtrado de historial
H7 — análisis de prompts registrados
HF — mejora opcional del proyecto
```

No es imprescindible para el núcleo mínimo de MiniJarvis, pero sí útil para alumnado avanzado.

Conceptos clave que deben quedar dominados si se introduce:

- lambda;
- interfaz funcional;
- función pura;
- inmutabilidad;
- función de orden superior;
- stream;
- filter/map/forEach;
- Optional;
- referencia a método.

---

# 9. Tema 8 — Aplicaciones con interfaz gráfica de escritorio

Archivo fuente:

```text
Tema 8: Aplicaciones con interfaz gráfica de escritorio.pdf
```

## Apartados detectados

```text
1.- Introducción
2.- La programación dirigida por eventos
3.- Aplicaciones de escritorio en Java
4.- JavaFX
4.1.- Inicio de un proyecto JavaFX
4.2.- Elementos básicos de una aplicación JavaFX
5.- Aplicaciones MVC
5.1.- Diseño de vistas con JavaFX
5.2.- Programación del controlador
5.3.- Integración de la vista y el controlador en la aplicación
6.- Elementos básicos de las interfaces de usuario
6.1.- Paneles
6.2.- Controles
7.- Realización de una aplicación con arquitectura hexagonal
7.1.- Arquitecturas de software
7.2.- La arquitectura hexagonal
7.3.- Definición del modelo
7.4.- Análisis de los casos de uso
7.5.- Definición de los repositorios
7.6.- Definición del origen de datos
7.7.- Programación de la lógica de negocio
7.8.- Test de la lógica de negocio
7.9.- Implementación del acceso a base de datos
7.9.1.- Conexión y desconexión de la base de datos
7.9.2.- Realización de consultas
7.9.3.- Realización de consultas con variables
7.9.4.- Inserción de datos
7.9.5.- Consulta del último ID generado
7.9.7.- Actualización de datos
7.9.8.- Borrado de datos
7.9.9.- Transacciones
7.10.- Contexto de la aplicación
7.10.- Diseño de las vistas
7.11.- Creación de la clase de la aplicación
7.12.- Programación de los controladores
7.12.1.- Gestión común de los mensajes de error
7.12.2.- Creación de un nuevo grado
7.12.3.- Mostrar el detalle del grado seleccionado en el ListView
7.12.4.- Borrar un grado
7.12.5.- Actualizar un grado
7.12.6.- Añadir un menú contextual a la tabla
7.12.7.- Abrir la ventana de asignaturas en forma modal
7.12.8.- Pasar un objeto de la ventana principal a la ventana modal
7.12.9.- Pasar un objeto de la ventana modal a la ventana principal
7.12.10.- Configurar las columnas de la tabla
7.12.11.- Configurar el inicio de la aplicación
7.12.12.- Borrar la asignatura de la tabla
```

## Conceptos de programación trabajados

### 9.1. Programación dirigida por eventos

- Evento.
- Manejador de evento.
- Flujo no lineal.
- Diferencia entre programa por consola y aplicación con interfaz.
- Responder a acciones del usuario.

### 9.2. Aplicaciones de escritorio

- Aplicación gráfica.
- Ventana.
- Ciclo de vida de una aplicación.
- Diferencia entre lógica y presentación.

### 9.3. JavaFX

- Proyecto JavaFX.
- Elementos básicos de una aplicación JavaFX.
- Escena, ventana y componentes.
- Integración entre código y vista.

### 9.4. MVC

- Modelo.
- Vista.
- Controlador.
- Separación de responsabilidades.
- Controlador como intermediario entre interfaz y lógica.
- Riesgo de mezclar lógica de negocio en la vista.

### 9.5. Interfaces de usuario

- Paneles.
- Controles.
- Listas visuales.
- Tablas.
- Menús contextuales.
- Ventanas modales.
- Paso de datos entre ventanas.
- Mensajes de error.

### 9.6. Arquitectura hexagonal

- Arquitectura de software.
- Modelo de dominio.
- Casos de uso.
- Repositorios.
- Orígenes de datos.
- Lógica de negocio independiente de la interfaz.
- Test de lógica de negocio.
- Adaptadores.

### 9.7. Persistencia en base de datos

- Conexión y desconexión.
- Consultas.
- Consultas con variables.
- Inserción de datos.
- Identificador generado.
- Actualización.
- Borrado.
- Transacciones.
- Riesgos de errores en acceso a datos.

## Casos prácticos sugeridos para alumnado

- Versión gráfica opcional de MiniJarvis.
- Vista con campo de entrada y área de respuesta.
- Controlador que llama a `Agent`.
- Modelo independiente de JavaFX.
- Repositorio de recuerdos.
- Sustitución de fichero por base de datos como ampliación.
- Test de lógica sin abrir interfaz gráfica.

## Relación con MiniJarvis

Este tema es de ampliación avanzada para cierre o mejora:

```text
HF — mejora opcional del proyecto final
```

También puede conectar con:

```text
H6 — persistencia
H7 — integración IA responsable
```

Pero no debería introducirse antes de consolidar clases, colecciones, persistencia y separación de responsabilidades.

Conceptos clave si se trabaja:

- evento;
- JavaFX;
- vista;
- controlador;
- modelo;
- MVC;
- arquitectura hexagonal;
- caso de uso;
- repositorio;
- base de datos;
- CRUD;
- transacción.

---

# 10. Mapa global de conceptos por familias

## 10.1. Fundamentos de programación

Trabajados principalmente en:

```text
Tema 1
Tema 3
```

Conceptos:

- programa;
- instrucción;
- sintaxis;
- comentario;
- variable;
- tipo de dato;
- literal;
- operador;
- expresión;
- entrada/salida;
- condición;
- secuencia;
- flujo de ejecución;
- conversión de tipos.

## 10.2. Control de flujo

Trabajado principalmente en:

```text
Tema 1
Tema 3
```

Conceptos:

- `if`;
- `if-else`;
- asignación condicional;
- `switch-case`;
- enhanced switch;
- `while`;
- `do-while`;
- `for`;
- bucle anidado;
- condición de salida;
- eficiencia básica.

## 10.3. Estructuras de datos

Trabajadas principalmente en:

```text
Tema 4
Tema 7
```

Conceptos:

- estructura de datos;
- colección;
- genéricos;
- `Collection<T>`;
- `List<T>`;
- recorrido;
- `for` mejorado;
- mutabilidad;
- inmutabilidad;
- wrapper classes;
- array;
- tabla;
- `Set<T>`;
- `Map<K,V>`;
- streams sobre colecciones.

## 10.4. Programación orientada a objetos

Trabajada principalmente en:

```text
Tema 2
Tema 5
Tema 6
```

Conceptos:

- clase;
- objeto;
- atributo;
- método;
- constructor;
- referencia;
- estado;
- comportamiento;
- responsabilidad;
- encapsulación;
- invariante;
- modificadores de acceso;
- método estático;
- propiedad estática;
- herencia;
- `super`;
- `protected`;
- abstracción;
- clase abstracta;
- interfaz;
- polimorfismo;
- sobreescritura;
- `Object`;
- `toString`;
- `equals`;
- `hashCode`;
- `Comparable`;
- clase anónima;
- clase final;
- clase sellada.

## 10.5. Calidad, pruebas y depuración

Trabajadas principalmente en:

```text
Tema 5
Tema 6
```

Y aplicadas transversalmente en MiniJarvis.

Conceptos:

- test de clase;
- test unitario;
- aserto;
- TDD;
- validación;
- excepción;
- excepción propia;
- error de compilación;
- error de ejecución;
- error lógico;
- comportamiento esperado;
- refactorización segura.

## 10.6. Patrones, diseño y arquitectura

Trabajados principalmente en:

```text
Tema 6
Tema 8
```

Con introducción práctica en:

```text
H5 / capítulo 08 del libro de alumnado
```

Conceptos:

- patrón de diseño;
- patrón como solución a problema recurrente;
- Command simplificado;
- Strategy posible;
- Builder posible;
- separación de responsabilidades;
- MVC;
- arquitectura hexagonal;
- caso de uso;
- repositorio;
- adaptador;
- lógica de negocio independiente.

## 10.7. Programación funcional

Trabajada principalmente en:

```text
Tema 7
```

Conceptos:

- lambda;
- interfaz funcional;
- función pura;
- inmutabilidad;
- función de orden superior;
- stream;
- Optional;
- referencia a método;
- procesamiento declarativo de colecciones.

## 10.8. Interfaces gráficas y persistencia avanzada

Trabajadas principalmente en:

```text
Tema 8
```

Conceptos:

- evento;
- JavaFX;
- panel;
- control;
- controlador;
- vista;
- ventana modal;
- tabla;
- CRUD;
- conexión a base de datos;
- consulta parametrizada;
- transacción;
- gestión de errores en UI.

---

# 11. Relación recomendada con los hitos MiniJarvis

| Hito MiniJarvis | Conceptos de temas que más encajan |
|---|---|
| H1 — Primer asistente básico | Tema 1: variables, tipos, entrada/salida, expresiones. Tema 3: secuencia básica. |
| H2 — Decisiones y depuración | Tema 1: `if/else`, booleanos. Tema 3: flujo, `switch`, bucles. Tema 5: primeras pruebas. |
| H3 — Memoria en colecciones | Tema 4: `List`, recorridos, mutabilidad, arrays, sets/maps como ampliación. |
| H4 — Agente orientado a objetos | Tema 2: clase, objeto, método, constructor, diagrama. Tema 5: clase programada, atributos, constructores. |
| H5 — Extensible, clean code y patrones | Tema 5: interfaces, tests, excepciones. Tema 6: polimorfismo y patrones. |
| H6 — Persistente y trazable | Tema 5: excepciones y clases responsables. Tema 8: repositorios/persistencia como ampliación posterior. |
| H7 — IA responsable o simulación robusta | Tema 5: records/enums/interfaces. Tema 6: abstracción/polimorfismo. Tema 7: Optional/streams como mejora. |
| HF — Presentación, recuperación y mejora | Repaso integrado de todos los temas; Tema 8 como mejora opcional gráfica o persistencia avanzada. |

---

# 12. Cuándo introducir patrones de diseño

Recomendación:

```text
No introducir patrones de diseño antes de H5.
```

Motivo:

- Antes de H5 el alumnado todavía está construyendo las bases: variables, condiciones, bucles, colecciones, clases y objetos.
- Un patrón antes de que exista un problema visible se convierte en teoría decorativa.
- En H5 ya aparece un problema real: un `Agent` que crece con muchos comandos y demasiados `if/else` o `switch`.

Momento recomendado:

```text
H5 — cuando el alumnado vea que añadir comandos modifica demasiadas partes del código.
```

Patrón inicial recomendado:

```text
Command simplificado
```

Formulación didáctica:

```text
Cada comando se convierte en una herramienta con una forma común de ejecutarse.
```

Conceptos previos necesarios:

- clase;
- objeto;
- método;
- interfaz;
- implementación;
- lista de objetos;
- responsabilidad única;
- refactorización segura.

Patrones que podrían aparecer después, solo si el proyecto lo pide:

| Patrón | Momento razonable | Problema que resolvería |
|---|---|---|
| Command simplificado | H5 | Muchos comandos en `Agent`. |
| Strategy | H7/HF | Cambiar entre IA simulada, IA real o respuesta fija. |
| Repository | H6/HF | Cambiar entre memoria en fichero y memoria en base de datos. |
| Factory simple | HF ampliación | Crear herramientas o asistentes según configuración. |
| Builder | Tema 6 o HF | Construcción de objetos con muchos datos opcionales. |

---

# 13. Observaciones editoriales

1. El Tema 2 introduce muchos conceptos de POO de forma panorámica. Para MiniJarvis conviene no cargarlo todo de golpe; clase/objeto/método/constructor debe consolidarse antes de herencia.
2. El Tema 5 y el Tema 6 se solapan parcialmente con POO, pero el Tema 5 es más operativo y el Tema 6 más avanzado.
3. El Tema 8 contiene conceptos muy potentes —MVC, arquitectura hexagonal, repositorios y base de datos— que pueden ser excesivos para el núcleo mínimo del proyecto anual, pero son excelentes para ampliaciones de alumnado avanzado o mejora HF.
4. La programación funcional del Tema 7 debería tratarse como mejora expresiva sobre colecciones, no como sustitución temprana de bucles.
5. Los patrones deben aparecer cuando el alumnado haya sufrido un problema de diseño real y pueda defender por qué el patrón mejora el código.

---

# 14. Lista breve para consulta rápida

| Tema | Conceptos principales |
|---|---|
| Tema 1 | Variables, tipos, literales, operadores, entrada/salida, conversiones, `if/else`. |
| Tema 2 | POO inicial, clases, objetos, constructores, métodos, Javadoc, diagramas, excepciones, herencia inicial, referencias. |
| Tema 3 | Secuencia, condicionales, `switch`, bucles, bucles anidados, eficiencia. |
| Tema 4 | Colecciones, `Collection`, `List`, recorridos, `for` mejorado, mutabilidad, arrays, tablas, `Set`, `Map`. |
| Tema 5 | Clases, atributos, constructores, tests, TDD, métodos, excepciones, recursividad, estáticos, interfaces, records, enums. |
| Tema 6 | Encapsulación, herencia, excepciones propias, `instanceof`, sobreescritura, `Object`, `Comparable`, abstractas, polimorfismo, patrones. |
| Tema 7 | Lambdas, interfaces funcionales, inmutabilidad, funciones puras, funciones de orden superior, streams, Optional, referencias a métodos. |
| Tema 8 | Eventos, JavaFX, MVC, UI, arquitectura hexagonal, modelo, casos de uso, repositorios, base de datos, CRUD, transacciones. |

---

# 15. Uso recomendado de este documento

Este documento puede usarse para:

- comprobar si el libro del alumnado cubre los conceptos básicos;
- ajustar la secuencia MiniJarvis a los temas oficiales existentes;
- preparar actividades de recuperación por tema;
- localizar qué conceptos necesita reforzar un alumno;
- decidir qué conceptos avanzados dejar como ampliación;
- justificar por qué los patrones de diseño aparecen en H5 y no al principio.
