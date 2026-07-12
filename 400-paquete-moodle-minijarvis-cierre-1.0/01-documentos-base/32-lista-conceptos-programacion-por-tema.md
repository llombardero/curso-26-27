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

<!-- AJUSTE-COBERTURA-CONCEPTOS-32 -->

# 16. Ajuste aplicado a los hitos MiniJarvis

Este documento ya no queda solo como análisis: se ha usado para modificar los hitos, guías docentes autónomas, paquetes de hito, libro del alumnado, índice global y respuestas modelo de Laura.

Criterio aplicado:

```text
Todo concepto de Programación recopilado aquí debe aparecer al final del itinerario como núcleo, ampliación, recuperación o mejora defendible.
```

Distribución final:

| Bloque | Función curricular |
|---|---|
| H1-H2 | Fundamentos, variables, tipos, entrada/salida, condiciones, bucles, switch, depuración y eficiencia básica. |
| H3 | Colecciones, listas, recorridos, mutabilidad, arrays, Set y Map como ampliaciones. |
| H4 | Clases, objetos, métodos, constructores, referencias, diagramas y responsabilidades. |
| H5 | Tests, TDD, interfaces, polimorfismo, clean code y Command simplificado. |
| H6 | Excepciones, invariantes, persistencia, logs y repositorio como idea inicial. |
| H7 | Records/enums, abstracción, Strategy opcional, Optional, streams, funciones puras e IA responsable. |
| HF | Cierre y mejora: JavaFX, eventos, MVC, arquitectura hexagonal, repositorios, CRUD, transacciones y defensa global. |

Respuesta de Laura esperada al final:

> Puedo explicar dónde aparece cada concepto importante en mi proyecto MiniJarvis o, si es una ampliación, dónde lo he estudiado y cómo lo aplicaría de forma segura sin romper el diseño.

<!-- MAPA-CONCEPTOS-HITOS-DEFINICIONES-EJEMPLOS -->

# 17. Mapa operativo de conceptos: hito, definición, uso y ejemplo

Este apartado convierte la lista de conceptos anterior en una herramienta práctica para programar, evaluar y recuperar.

Criterio de lectura:

```text
- Hito principal: momento en el que el concepto se trabaja de forma más explícita.
- Otros hitos: momentos donde se reutiliza, amplía o defiende.
- Ejemplo: caso MiniJarvis, no teoría aislada.
```

## 17.1. Fundamentos de programación

| Concepto | Hito principal | Otros hitos | Definición operativa | Cuándo se usa | Ejemplo MiniJarvis |
|---|---|---|---|---|---|
| Programa | H1 | H2-HF | Conjunto de instrucciones que se compilan y ejecutan para producir un comportamiento. | Cuando se crea una primera versión ejecutable. | `Main` muestra un saludo de MiniJarvis por consola. |
| Código fuente | H1 | H2-HF | Texto escrito por el programador en Java antes de compilarse. | Al editar clases, métodos y pruebas. | `Main.java` contiene las instrucciones iniciales del asistente. |
| Ejecución | H1 | H2-HF | Puesta en marcha del programa para comprobar su comportamiento real. | Cada vez que se valida una entrega. | Ejecutar MiniJarvis y guardar captura o salida en evidencias. |
| Sintaxis | H1 | H2-HF | Reglas de escritura del lenguaje Java. | Al corregir errores de compilación. | Añadir `;`, cerrar llaves y escribir correctamente `System.out.println`. |
| Instrucción | H1 | H2-HF | Orden individual que el programa puede ejecutar. | Para construir el flujo paso a paso. | `System.out.println("Hola, soy MiniJarvis");`. |
| Secuencia | H1 | H2 | Ejecución ordenada de instrucciones una detrás de otra. | Cuando no hay todavía decisiones ni bucles complejos. | Pedir nombre, guardarlo y saludar en ese orden. |
| Comentario | H1 | H2-HF | Texto no ejecutable que aclara intención o decisiones del código. | Para explicar partes no evidentes sin ensuciar el programa. | `// Pedimos el nombre para personalizar el saludo`. |
| Identificador | H1 | H2-HF | Nombre de una variable, clase, método o constante. | Al nombrar elementos de forma legible. | `userName`, `memory`, `rememberCommand`. |
| Palabra reservada | H1 | H2-HF | Término del lenguaje Java con significado fijo. | Para reconocer estructura del código. | `class`, `public`, `static`, `void`, `if`. |
| Llaves, paréntesis y punto y coma | H1 | H2-HF | Signos que delimitan bloques, llamadas e instrucciones. | Al escribir cualquier programa Java. | Cerrar el bloque de `main` y cada llamada a `println`. |
| Variable | H1 | H2-HF | Espacio con nombre para guardar un dato que puede cambiar. | Cuando el programa necesita recordar un valor temporal. | `String userName = scanner.nextLine();`. |
| Constante | H1 | H4-HF | Valor con nombre que no debe cambiar durante la ejecución. | Para evitar números o textos mágicos repetidos. | `static final String APP_NAME = "MiniJarvis";`. |
| Tipo de dato | H1 | H2-HF | Categoría que indica qué valores puede almacenar una variable. | Al declarar datos correctamente. | `String` para texto, `int` para contadores, `boolean` para validaciones. |
| Tipo primitivo | H1 | H2-HF | Tipo básico de Java que guarda valores simples. | Para números, caracteres o booleanos. | `int attempts = 0; boolean valid = true;`. |
| String | H1 | H2-HF | Tipo de referencia usado para texto. | En entradas, comandos, mensajes y recuerdos. | `String command = scanner.nextLine();`. |
| Literal | H1 | H2-HF | Valor escrito directamente en el código. | Para textos o números simples, con cuidado de no abusar. | `"salir"`, `0`, `true`. |
| Entrada por teclado | H1 | H2 | Lectura de datos introducidos por la persona usuaria. | En programas de consola interactivos. | MiniJarvis pregunta el nombre o un comando. |
| Salida por pantalla | H1 | H2-HF | Información que el programa muestra a la persona usuaria. | Para saludar, explicar errores o mostrar resultados. | `System.out.println("Comandos: ayuda, salir");`. |
| Scanner | H1 | H2 | Clase usada para leer datos desde consola. | En las primeras versiones interactivas. | `Scanner scanner = new Scanner(System.in);`. |
| Concatenación | H1 | H2-HF | Unión de textos y valores para construir un mensaje. | Para personalizar salidas. | `"Hola, " + userName + "."`. |
| Operador de asignación | H1 | H2-HF | Operador que guarda un valor en una variable. | Al inicializar o actualizar datos. | `command = scanner.nextLine();`. |
| Operadores aritméticos | H1 | H2 | Símbolos para calcular valores numéricos. | En contadores, puntuaciones o simulaciones. | `attempts = attempts + 1;`. |
| Operadores de comparación | H1 | H2-HF | Operadores que comparan valores y producen booleanos. | En condiciones y validaciones. | `memory.size() > 0`. |
| Operadores booleanos | H1 | H2-HF | Operadores para combinar condiciones. | Cuando una regla depende de varios criterios. | `!text.isBlank() && text.length() < 100`. |
| Expresión | H1 | H2-HF | Combinación de valores, variables y operadores que produce un resultado. | En asignaciones, condiciones y retornos. | `command.trim().toLowerCase()`. |
| Conversión implícita | H1 | H2 | Conversión automática entre tipos compatibles. | En operaciones numéricas simples. | Usar un `int` dentro de una operación con `double`. |
| Conversión explícita o casting | H1 | H2 | Conversión indicada por el programador. | Cuando Java no puede convertir de forma segura. | Convertir un cálculo decimal a entero si se justifica. |
| Conversión String-tipo básico | H1 | H2 | Transformar texto leído en número o booleano. | Al leer opciones numéricas desde consola. | `Integer.parseInt(optionText)`. |
| Error de sintaxis | H1 | H2-HF | Fallo de escritura que impide compilar. | Al aprender estructura básica de Java. | Olvidar un `;` o cerrar mal una llave. |

## 17.2. Control de flujo, menús y depuración

| Concepto | Hito principal | Otros hitos | Definición operativa | Cuándo se usa | Ejemplo MiniJarvis |
|---|---|---|---|---|---|
| Condición | H1 | H2-HF | Expresión booleana que decide si se ejecuta un bloque. | Para validar entradas o elegir respuestas. | `if (name.isBlank())`. |
| if | H1 | H2-HF | Estructura que ejecuta código solo si se cumple una condición. | En la primera toma de decisiones. | Si el nombre está vacío, mostrar aviso. |
| if-else | H1 | H2-HF | Estructura que elige entre dos caminos. | Cuando hay respuesta alternativa. | Si hay recuerdos, mostrarlos; si no, decir que no hay memoria. |
| Condiciones encadenadas | H2 | H3-HF | Varios `if/else if/else` para elegir entre múltiples casos. | En menús pequeños antes de refactorizar. | `ayuda`, `salir`, `recordar`, comando desconocido. |
| Asignación condicional | H2 | H7 | Forma de elegir un valor según condición. | Para simplificar asignaciones sencillas. | Mensaje distinto si el usuario tiene recuerdos o no. |
| switch-case | H2 | H5 | Selección entre valores discretos. | Para menús de comandos antes de introducir Command. | `switch (command)` con `ayuda`, `recordar`, `salir`. |
| switch mejorado | H2 | H5-H7 | Variante moderna de `switch` más expresiva. | Cuando mejora legibilidad sin adelantar complejidad. | `case "ayuda" -> showHelp();`. |
| break | H2 | H5 | Instrucción que evita que un `switch` clásico continúe al siguiente caso. | En `switch-case` tradicional. | Terminar el caso `ayuda` tras mostrar comandos. |
| default | H2 | H5 | Rama para valores no contemplados. | Para comandos desconocidos. | MiniJarvis responde: “No conozco ese comando”. |
| while | H2 | H3-HF | Bucle que repite mientras una condición sea verdadera. | Para mantener vivo el menú. | Repetir hasta que `command.equals("salir")`. |
| do-while | H2 | H3 | Bucle que ejecuta al menos una vez y luego comprueba condición. | Cuando se debe mostrar el menú al menos una vez. | Pedir comando y repetir mientras no sea `salir`. |
| for | H2 | H3-HF | Bucle con contador o recorrido controlado. | Para repetir un número conocido de veces o recorrer índices. | Mostrar recuerdos numerados con índice. |
| for mejorado | H3 | H4-HF | Bucle simplificado para recorrer colecciones. | Cuando no se necesita el índice. | `for (String memory : memories)`. |
| Bucle anidado | H2 | H3 | Bucle dentro de otro bucle. | En tablas o recorridos bidimensionales, con prudencia. | Revisar una tabla de comandos por categorías. |
| Condición de salida | H2 | H3-HF | Regla que permite terminar un bucle. | Para evitar bucles infinitos. | Salir cuando el comando sea `salir`. |
| Bucle infinito | H2 | H6 | Error donde un bucle nunca termina. | Se estudia para depurar menús. | No actualizar `command` dentro del `while`. |
| Flujo de ejecución | H2 | H4-HF | Orden real en que se ejecutan instrucciones, decisiones y llamadas. | Para depurar y explicar el programa. | Seguir el camino desde `main` hasta `Agent.respond`. |
| Menú | H2 | H5 | Interfaz textual con opciones o comandos. | Para organizar funciones del asistente. | Comandos: `ayuda`, `recordar`, `memoria`, `salir`. |
| Comando desconocido | H2 | H5-H7 | Entrada no reconocida por el programa. | Para diseñar respuestas seguras y amables. | “No entiendo ese comando. Escribe ayuda.” |
| Validación de entrada | H2 | H4-HF | Comprobación de que un dato cumple reglas mínimas. | Antes de guardar o procesar datos. | No guardar recuerdos vacíos. |
| Error de compilación | H1 | H2-HF | Error detectado antes de ejecutar. | Al corregir sintaxis o tipos. | Llamar a un método que no existe. |
| Error de ejecución | H2 | H6-HF | Fallo que ocurre mientras el programa se ejecuta. | Al leer ficheros, convertir datos o acceder a índices. | `NumberFormatException` al convertir texto no numérico. |
| Error lógico | H2 | H5-HF | El programa compila pero produce resultado incorrecto. | En depuración y pruebas. | Guardar el comando completo en vez del recuerdo. |
| Depuración | H2 | H5-HF | Proceso de localizar, entender y corregir errores. | Cuando la salida no coincide con lo esperado. | Revisar variable `command` paso a paso. |
| Eficiencia básica | H2 | H3-HF | Primer análisis del coste o claridad de una solución. | Cuando hay bucles innecesarios o código repetido. | Evitar recorrer toda la memoria si solo se busca un primer resultado. |

## 17.3. Colecciones y estructuras de datos

| Concepto | Hito principal | Otros hitos | Definición operativa | Cuándo se usa | Ejemplo MiniJarvis |
|---|---|---|---|---|---|
| Estructura de datos | H3 | H6-HF | Forma organizada de almacenar varios datos. | Cuando una variable simple ya no basta. | Guardar varios recuerdos del usuario. |
| Colección | H3 | H5-HF | Objeto que agrupa varios elementos. | Para manejar listas, conjuntos o mapas. | `List<String> memories`. |
| Java Collection Framework | H3 | H5-HF | Conjunto de interfaces y clases de Java para colecciones. | Al elegir entre `List`, `Set` o `Map`. | Usar `ArrayList` para memoria ordenada. |
| Genéricos | H3 | H5-HF | Parámetros de tipo que indican qué contiene una colección. | Para evitar mezclas de tipos y casts innecesarios. | `List<Tool>` o `Map<String, String>`. |
| Collection<T> | H3 | H5 | Interfaz general para grupos de elementos. | Cuando solo importan operaciones comunes. | Recibir una colección de recuerdos sin depender de `ArrayList`. |
| List<T> | H3 | H5-HF | Colección ordenada que permite repetidos e índices. | Para memoria cronológica o historial. | Recuerdos en el orden en que se añadieron. |
| ArrayList<T> | H3 | H6 | Implementación habitual de lista mutable. | En memoria temporal sencilla. | `new ArrayList<>()` para recuerdos. |
| Índice | H3 | H5-HF | Posición numérica de un elemento en una lista o array. | Al mostrar o recuperar elementos por posición. | Recuerdo 1, recuerdo 2, recuerdo 3. |
| Recorrido | H3 | H5-HF | Visita de todos o parte de los elementos. | Para mostrar, buscar o validar datos. | Recorrer recuerdos para imprimirlos. |
| Mutabilidad | H3 | H6-H7 | Capacidad de modificar una estructura después de crearla. | Cuando se añaden o borran recuerdos. | `memories.add(newMemory)`. |
| Inmutabilidad | H3 | H7-HF | Diseño donde los datos no se modifican tras crearse. | Para reducir efectos secundarios y errores. | Devolver copia no modificable de la memoria. |
| Clases envoltorio | H3 | H5 | Clases objeto para valores primitivos. | Al usar primitivos en colecciones genéricas. | `List<Integer>` para puntuaciones. |
| Array | H3 | H4-HF | Estructura de tamaño fijo con acceso por índice. | Para comparar con listas o manejar datos fijos. | Array de comandos básicos si no se necesita modificar. |
| Tabla | H3 | HF | Estructura bidimensional o visual de datos. | En ampliaciones o interfaces con listados. | Tabla de historial en una versión JavaFX. |
| Set<T> | H3 | H5-HF | Colección sin elementos repetidos. | Para evitar duplicados o comprobar pertenencia. | Detectar comandos o recuerdos repetidos. |
| Map<K,V> | H3 | H6-HF | Asociación clave-valor. | Para buscar datos por identificador. | Preferencias: `idioma -> español`, `tema -> claro`. |
| Búsqueda por clave | H3 | H6-HF | Localización directa de un valor a partir de una clave. | Cuando no conviene recorrer toda una lista. | Recuperar una preferencia del usuario. |

## 17.4. Programación orientada a objetos

| Concepto | Hito principal | Otros hitos | Definición operativa | Cuándo se usa | Ejemplo MiniJarvis |
|---|---|---|---|---|---|
| POO | H4 | H5-HF | Forma de programar organizando responsabilidades en clases y objetos. | Cuando el programa deja de caber bien en `Main`. | Separar `Agent`, `Memory` y `ConsoleApp`. |
| Clase | H4 | H5-HF | Plantilla que define estado y comportamiento. | Para modelar partes del sistema. | `class Agent`. |
| Objeto | H4 | H5-HF | Instancia concreta de una clase. | Para usar una clase en ejecución. | `Agent agent = new Agent(memory);`. |
| Instancia | H4 | H5-HF | Objeto creado a partir de una clase. | Al diferenciar plantilla de elemento real. | Un `Memory` concreto usado por MiniJarvis. |
| new | H4 | H5-HF | Operador que crea objetos. | Al construir dependencias. | `new ArrayList<>()`, `new Agent()`. |
| Atributo | H4 | H5-HF | Dato interno de un objeto. | Para guardar estado propio. | `private final List<String> memories;`. |
| Estado | H4 | H6-HF | Valores internos de un objeto en un momento dado. | Para razonar sobre cambios y persistencia. | Recuerdos actuales almacenados en memoria. |
| Comportamiento | H4 | H5-HF | Acciones que un objeto puede realizar mediante métodos. | Para repartir responsabilidades. | `memory.remember(text)`. |
| Método | H4 | H5-HF | Bloque de código con nombre que realiza una operación. | Para evitar repetición y expresar acciones. | `respondTo(command)`. |
| Método procedimiento | H4 | H5-HF | Método que realiza una acción sin devolver valor relevante. | Para mostrar, guardar o modificar estado. | `showHelp()`. |
| Método función | H4 | H5-HF | Método que calcula y devuelve un valor. | Para obtener respuestas o resultados. | `String buildResponse(String command)`. |
| Parámetro | H4 | H5-HF | Dato que se entrega a un método o constructor. | Para reutilizar código con distintos valores. | `remember(String text)`. |
| Retorno | H4 | H5-HF | Valor devuelto por un método. | Para separar cálculo y salida. | `return "He guardado el recuerdo";`. |
| Constructor | H4 | H5-HF | Método especial que inicializa un objeto. | Para crear objetos válidos desde el inicio. | `Memory(List<String> initialMemories)`. |
| Constructor por defecto | H4 | H5 | Constructor sin parámetros. | En modelos muy simples o primeras pruebas. | `new Memory()`. |
| Constructor con parámetros | H4 | H5-HF | Constructor que recibe datos obligatorios. | Para inyectar dependencias o estado inicial. | `new Agent(memory, tools)`. |
| Sobrecarga de constructores | H4 | H5 | Varios constructores con distintas firmas. | Cuando hay formas controladas de crear objetos. | `Memory()` y `Memory(List<String>)`. |
| this | H4 | H5-HF | Referencia al objeto actual. | Para distinguir atributo y parámetro. | `this.memories = memories;`. |
| Referencia | H4 | H5-HF | Variable que apunta a un objeto, no contiene el objeto completo. | Para entender alias, mutabilidad y paso de objetos. | Dos variables pueden apuntar a la misma `Memory`. |
| Tipo referencia | H4 | H5-HF | Tipo cuyo valor es una referencia a un objeto. | Con `String`, listas y clases propias. | `Agent`, `Memory`, `List<String>`. |
| Responsabilidad | H4 | H5-HF | Motivo claro por el que una clase o método existe. | Para evitar clases gigantes. | `Memory` guarda recuerdos; `Agent` decide respuestas. |
| Encapsulación | H4 | H5-HF | Protección del estado interno mediante atributos privados y métodos controlados. | Para impedir cambios inseguros. | No exponer directamente la lista interna de recuerdos. |
| private | H4 | H5-HF | Modificador que limita acceso a la propia clase. | Para proteger atributos y detalles internos. | `private final List<String> memories;`. |
| public | H4 | H5-HF | Modificador que permite acceso desde otras clases. | Para la API visible de una clase. | `public void remember(String text)`. |
| Modificador por defecto | H6 | HF | Acceso de paquete cuando no se escribe modificador. | En organización avanzada de paquetes. | Clases auxiliares internas del paquete `domain`. |
| protected | H6 | HF | Acceso para clase, paquete y subclases. | En herencia, con prudencia. | Ampliación avanzada de una herramienta base. |
| Invariante | H6 | H5-HF | Regla que siempre debe cumplirse en un objeto válido. | Al validar constructores y métodos. | Un recuerdo no puede ser `null` ni estar en blanco. |
| Paquete | H4 | H5-HF | Agrupación lógica de clases Java. | Para ordenar el proyecto. | `domain`, `app`, `persistence`. |
| Javadoc | H4 | H5-HF | Documentación técnica vinculada a clases y métodos. | Para explicar contratos públicos. | Documentar qué hace `remember`. |
| Diagrama de clases | H4 | H5-HF | Representación visual de clases, atributos, métodos y relaciones. | Para diseñar y defender POO. | Diagrama `Agent` → `Memory`. |
| Relación diagrama-código | H4 | H5-HF | Correspondencia entre diseño visual y clases reales. | Para comprobar que el diagrama no es decorativo. | El atributo `memory` del diagrama existe en `Agent.java`. |
| Librería | H4 | H5-HF | Código ya existente que se usa desde el proyecto. | Para aprovechar clases de Java o herramientas externas permitidas. | `java.util.List`, `java.nio.file.Files`. |
| Clase predefinida | H4 | H5-HF | Clase disponible en Java o en una librería. | Para no reinventar funcionalidad básica. | `Scanner`, `ArrayList`, `Path`. |
| Método estático | H4 | H5-HF | Método asociado a la clase, no a un objeto concreto. | En utilidades o punto de entrada. | `public static void main(String[] args)`. |
| Propiedad estática | H5 | HF | Dato compartido por la clase. | Con constantes, evitando estado global mutable. | `static final int MAX_MEMORY_LENGTH = 120;`. |
| Estado global | H5 | HF | Estado compartido de forma amplia y difícil de controlar. | Se evita para reducir errores. | No guardar recuerdos en una variable global modificable. |

## 17.5. Calidad, pruebas, excepciones y TDD

| Concepto | Hito principal | Otros hitos | Definición operativa | Cuándo se usa | Ejemplo MiniJarvis |
|---|---|---|---|---|---|
| Test manual | H2 | H1-HF | Comprobación ejecutando el programa y observando la salida. | En primeras versiones y evidencias sencillas. | Probar `ayuda`, `salir` y comando desconocido. |
| Test de clase | H5 | H4-HF | Prueba centrada en una clase concreta. | Cuando una responsabilidad ya está separada. | Probar `Memory.remember`. |
| Test unitario | H5 | H6-HF | Prueba automatizada de una unidad pequeña. | Para validar comportamiento repetible. | Test que comprueba que no se guarda recuerdo vacío. |
| Aserto | H5 | H6-HF | Comprobación que debe cumplirse en una prueba. | Para expresar resultado esperado. | `assertEquals(1, memory.size())`. |
| TDD | H5 | H6-HF | Desarrollo guiado por pruebas: rojo, verde, refactor. | Para diseñar comportamiento antes de complicar código. | Escribir primero el test de `remember`. |
| Rojo-verde-refactor | H5 | H6-HF | Ciclo TDD: prueba falla, código mínimo pasa, mejora diseño. | Para enseñar evolución segura. | Fallar por no validar vacío, pasar validando, refactorizar nombres. |
| Comportamiento esperado | H2 | H5-HF | Resultado que debe producir el programa ante una entrada. | En pruebas, checklists y defensa. | Entrada `ayuda` debe mostrar comandos disponibles. |
| Validación | H2 | H5-HF | Comprobación de reglas antes de aceptar datos. | Para proteger objetos y persistencia. | Rechazar recuerdo en blanco. |
| Excepción | H4 | H6-HF | Señal de situación anómala durante la ejecución. | Para errores que no deben ignorarse. | Fallo al leer archivo de memoria. |
| try-catch | H4 | H6-HF | Bloque para capturar y manejar excepciones. | En entrada/salida, conversiones y ficheros. | Capturar error al cargar recuerdos. |
| Método peligroso | H4 | H6 | Método que puede fallar y requiere tratamiento. | Al leer archivos o convertir datos. | `Files.readAllLines(path)`. |
| RuntimeException | H5 | H6-HF | Excepción no comprobada por el compilador. | Para errores de uso o invariantes incumplidas. | Lanzar si se intenta guardar `null`. |
| CheckedException | H5 | H6-HF | Excepción que Java obliga a declarar o capturar. | En operaciones de E/S. | `IOException` al guardar historial. |
| throws | H5 | H6-HF | Declaración de que un método puede lanzar excepción. | Al delegar manejo a otra capa. | `save() throws IOException`. |
| Excepción propia | H6 | HF | Clase de excepción creada para el dominio. | En ampliaciones con reglas de negocio claras. | `InvalidMemoryException`. |
| Mensaje de error significativo | H2 | H6-HF | Explicación útil del problema sin exponer datos sensibles. | Al informar al usuario o registrar logs. | “No se pudo guardar la memoria. Revisa permisos.” |
| Refactorización | H5 | H6-HF | Mejora interna del código sin cambiar comportamiento observable. | Cuando el código funciona pero está desordenado. | Extraer `handleCommand` de un `main` demasiado largo. |
| Refactorización segura | H5 | H6-HF | Refactor apoyado por pruebas o checklist. | Para evitar romper funciones existentes. | Pasar tests antes y después de extraer `Tool`. |
| Clean code | H5 | H6-HF | Código claro, simple, nombrado y defendible. | En revisión y rúbricas. | Métodos pequeños con nombres como `showMemories`. |
| Nombre significativo | H1 | H5-HF | Identificador que expresa intención. | Siempre que se declara algo. | `memoryText` mejor que `x`. |

## 17.6. Herencia, abstracción, interfaces y polimorfismo

| Concepto | Hito principal | Otros hitos | Definición operativa | Cuándo se usa | Ejemplo MiniJarvis |
|---|---|---|---|---|---|
| Interfaz | H5 | H6-HF | Contrato que define operaciones sin fijar implementación concreta. | Para desacoplar herramientas o repositorios. | `interface Tool { String execute(String input); }`. |
| Implementación | H5 | H6-HF | Clase que cumple el contrato de una interfaz. | Para crear comportamientos intercambiables. | `HelpTool implements Tool`. |
| Método default | H5 | HF | Método con implementación dentro de una interfaz. | En ampliaciones, si aporta comportamiento común sencillo. | `Tool.description()` con valor por defecto. |
| Método privado en interfaz | H5 | HF | Método auxiliar interno de una interfaz. | En Java avanzado, con prudencia didáctica. | Formatear ayuda común dentro de una interfaz avanzada. |
| Herencia | H6 | HF | Relación donde una clase hija reutiliza o especializa una clase padre. | Solo si hay una relación clara “es un tipo de”. | Una ampliación `LoggingTool` especializa una herramienta base, si procede. |
| Clase padre | H6 | HF | Clase general de la que hereda otra. | En jerarquías justificadas. | `AbstractTool`. |
| Clase hija | H6 | HF | Clase que hereda de otra. | Para especializar comportamiento. | `RememberTool` como especialización si se usa herencia. |
| extends | H6 | HF | Palabra clave para heredar de una clase. | En herencia de clases. | `class RememberTool extends AbstractTool`. |
| super | H6 | HF | Referencia a la clase padre. | Para llamar constructor o comportamiento heredado. | `super("recordar")`. |
| Herencia de interfaces | H6 | HF | Interfaz que amplía otra interfaz. | En diseños avanzados. | `SecureTool extends Tool`. |
| Sobreescritura | H6 | HF | Redefinir en una clase hija o implementación un método heredado. | Para adaptar comportamiento. | `@Override execute`. |
| @Override | H6 | HF | Anotación que confirma que un método sobrescribe otro. | Para evitar errores de firma. | `@Override public String execute(...)`. |
| Object | H6 | HF | Clase raíz de las clases Java. | Al entender métodos comunes. | Todos los objetos de MiniJarvis heredan de `Object`. |
| toString | H6 | HF | Método que devuelve representación textual de un objeto. | Para depuración o logs. | Mostrar `MemoryEntry{text='...', date=...}` sin datos sensibles. |
| equals | H6 | HF | Método que define igualdad lógica entre objetos. | Para comparar entidades. | Dos comandos son iguales si tienen el mismo nombre normalizado. |
| hashCode | H6 | HF | Código usado junto a `equals` en colecciones hash. | Cuando se usan `Set` o `Map` con objetos propios. | Evitar duplicados de `Command`. |
| Comparable | H6 | H7-HF | Interfaz para definir orden natural. | Para ordenar objetos. | Ordenar recuerdos por fecha o prioridad. |
| compareTo | H6 | H7-HF | Método que compara un objeto con otro. | En ordenación natural. | Comparar dos `MemoryEntry`. |
| Clase abstracta | H6 | HF | Clase incompleta que sirve de base común. | Cuando hay código común y no se debe instanciar directamente. | `AbstractTool` en ampliación avanzada. |
| Método abstracto | H6 | HF | Método declarado sin implementación en clase abstracta. | Para obligar a concretar comportamiento. | `execute` en una herramienta base. |
| Abstracción | H6 | H7-HF | Separar lo importante de los detalles concretos. | Para cambiar implementaciones sin romper el sistema. | `AiAssistant` oculta si la respuesta es simulada o real. |
| Polimorfismo | H5 | H6-HF | Usar un tipo general para objetos concretos distintos. | Para listas de herramientas o asistentes intercambiables. | `List<Tool>` con `HelpTool`, `RememberTool`, `StatusTool`. |
| instanceof | H6 | HF | Operador para comprobar tipo real. | Solo cuando no basta el polimorfismo. | Evitar abusarlo en herramientas; preferir `Tool.execute`. |
| Clase anónima | H6 | H7-HF | Clase sin nombre declarada en el punto de uso. | En ejemplos avanzados o callbacks. | Herramienta temporal para una prueba. |
| Clase final | H6 | HF | Clase que no puede heredarse. | Para proteger diseños cerrados. | `final class PromptSafety`. |
| Clase sellada | H6 | HF | Clase que limita qué clases pueden heredar. | En Java avanzado, si el grupo lo permite. | Jerarquía cerrada de tipos de respuesta. |
| Record | H7 | HF | Clase compacta e inmutable para datos. | Cuando se transportan datos sin mucha lógica. | `record AiResponse(String text, boolean safe)`. |
| Enum | H7 | H5-HF | Tipo con conjunto cerrado de valores. | Para evitar cadenas mágicas. | `enum CommandType { HELP, REMEMBER, EXIT }`. |

## 17.7. Patrones, diseño y arquitectura

| Concepto | Hito principal | Otros hitos | Definición operativa | Cuándo se usa | Ejemplo MiniJarvis |
|---|---|---|---|---|---|
| Patrón de diseño | H5 | H6-HF | Solución reutilizable a un problema de diseño recurrente. | Solo cuando existe un problema visible. | Sustituir muchos `if/else` por herramientas ejecutables. |
| Command simplificado | H5 | H6-HF | Organización donde cada comando se encapsula como objeto o herramienta ejecutable. | Cuando el menú crece y modificarlo es costoso. | `HelpTool`, `RememberTool`, `ExitTool`. |
| Strategy | H7 | HF | Patrón para intercambiar algoritmos o políticas. | Cuando se quiere cambiar la forma de responder sin tocar el cliente. | `SimulatedAiAssistant` frente a `FixedResponseAssistant`. |
| Repository | H6 | HF | Patrón/idea para aislar el acceso a datos. | Cuando se quiere cambiar fichero por base de datos. | `MemoryRepository` con implementación en fichero. |
| Factory simple | HF | H7 | Objeto o método que centraliza creación de instancias. | En ampliaciones con configuración. | Crear herramientas según comandos activados. |
| Builder | HF | H6 | Construcción paso a paso de objetos con muchos datos opcionales. | Si un constructor se vuelve demasiado largo. | Crear una configuración de MiniJarvis avanzada. |
| Separación de responsabilidades | H4 | H5-HF | Cada clase/método tiene una razón clara para cambiar. | En diseño, refactorización y defensa. | `PromptSafety` valida prompts; `Agent` coordina respuestas. |
| Caso de uso | HF | H6-HF | Acción significativa del sistema desde el punto de vista del usuario. | En arquitectura más avanzada. | “Guardar recuerdo”, “listar historial”, “validar prompt”. |
| Adaptador | HF | H7-HF | Pieza que conecta el dominio con una tecnología externa. | En arquitectura hexagonal o integración. | Adaptador de fichero o base de datos para memoria. |
| Lógica de negocio | H4 | HF | Reglas propias del problema, independientes de interfaz. | Para poder probar sin consola o GUI. | No aceptar prompts con secretos. |
| Modelo de dominio | H4 | HF | Clases que representan reglas y conceptos principales. | En diseño orientado a objetos y arquitectura. | `Agent`, `Memory`, `Tool`, `PromptSafety`. |
| MVC | HF | H7 | Separación entre modelo, vista y controlador. | Si se crea interfaz gráfica. | Vista JavaFX llama a controlador, controlador usa `Agent`. |
| Arquitectura hexagonal | HF | H6-HF | Arquitectura que protege el dominio de detalles externos mediante puertos y adaptadores. | Como mejora final avanzada. | Dominio MiniJarvis independiente de JavaFX y base de datos. |
| Puerto | HF | H6-HF | Interfaz que expresa una necesidad del dominio. | Para desacoplar persistencia o IA. | `MemoryRepository`. |
| Adaptador de salida | HF | H6-HF | Implementación que conecta un puerto con tecnología concreta. | Para ficheros, BD o proveedor IA simulado. | `FileMemoryRepository`. |

## 17.8. Persistencia, ficheros, logs y seguridad

| Concepto | Hito principal | Otros hitos | Definición operativa | Cuándo se usa | Ejemplo MiniJarvis |
|---|---|---|---|---|---|
| Persistencia | H6 | HF | Conservación de datos más allá de una ejecución. | Cuando la memoria no debe perderse al cerrar. | Guardar recuerdos en un fichero. |
| Fichero | H6 | HF | Archivo del sistema usado para leer o guardar datos. | Para memoria, historial o configuración simulada. | `memories.txt`. |
| Ruta | H6 | HF | Localización de un fichero o carpeta. | Para leer y escribir de forma controlada. | `Path.of("data", "memories.txt")`. |
| Lectura de fichero | H6 | HF | Cargar contenido persistido. | Al iniciar MiniJarvis. | Leer recuerdos previos. |
| Escritura de fichero | H6 | HF | Guardar información en disco. | Al añadir recuerdos o logs. | Escribir historial de comandos. |
| Log | H6 | H7-HF | Registro de eventos relevantes del sistema. | Para trazabilidad y depuración. | Guardar fecha, comando y resultado sin secretos. |
| Trazabilidad | H6 | H7-HF | Capacidad de reconstruir qué pasó y por qué. | En evidencias, depuración y seguridad. | Historial de pruebas y decisiones. |
| Reproducibilidad | H6 | HF | Posibilidad de repetir una prueba o ejecución con resultado comparable. | Para defender entregas. | Instrucciones exactas para ejecutar MiniJarvis. |
| Configuración | H6 | H7-HF | Datos que ajustan el comportamiento sin cambiar código. | En ampliaciones seguras. | Usar `.env.example` sin valores reales. |
| Secreto | H6 | H7-HF | Dato sensible que no debe subirse ni exponerse. | En seguridad e IA responsable. | API key, token, contraseña. |
| Placeholder | H6 | H7-HF | Valor ficticio que muestra formato sin revelar secreto. | En plantillas y ejemplos. | `API_KEY=pon-aqui-tu-clave-no-real`. |
| .env real | H6 | H7-HF | Archivo local con secretos reales que no debe compartirse. | En proyectos con integraciones externas. | No entregar `.env` en el portfolio. |
| .env.example | H6 | H7-HF | Plantilla sin secretos reales. | Para documentar configuración segura. | `AI_PROVIDER=simulated`. |
| Datos personales reales | H6 | H7-HF | Información identificable de personas. | Deben evitarse en prompts, logs y ejemplos. | No guardar DNI, teléfono ni dirección. |
| Base de datos | HF | H6 | Sistema estructurado para persistir y consultar datos. | Como mejora avanzada frente a fichero. | Tabla de recuerdos de MiniJarvis. |
| Conexión a base de datos | HF | H6 | Apertura de comunicación con la BD. | En ampliación avanzada. | Conectar con SQLite. |
| Consulta | HF | H6 | Petición de lectura a una BD. | Para recuperar recuerdos. | `SELECT text FROM memories`. |
| Consulta parametrizada | HF | H6 | Consulta que separa datos de código SQL. | Para evitar inyección SQL. | Buscar recuerdos por palabra clave segura. |
| Inserción | HF | H6 | Operación que añade datos a una BD. | Para guardar nuevos recuerdos. | Insertar un recuerdo validado. |
| Actualización | HF | H6 | Operación que modifica datos existentes. | Para corregir una preferencia. | Cambiar alias del usuario. |
| Borrado | HF | H6 | Operación que elimina datos. | Para limpiar memoria o cumplir privacidad. | Borrar un recuerdo seleccionado. |
| CRUD | HF | H6 | Crear, leer, actualizar y borrar datos. | En mejora avanzada con repositorio. | CRUD de recuerdos. |
| Transacción | HF | H6 | Grupo de operaciones que se confirman o revierten juntas. | Cuando hay cambios relacionados. | Guardar recuerdo y log de auditoría de forma consistente. |

## 17.9. Programación funcional y mejoras expresivas

| Concepto | Hito principal | Otros hitos | Definición operativa | Cuándo se usa | Ejemplo MiniJarvis |
|---|---|---|---|---|---|
| Programación funcional | H7 | HF | Estilo que favorece funciones, transformaciones e inmutabilidad. | Como mejora expresiva sobre colecciones. | Filtrar recuerdos sin modificar la lista original. |
| Lambda | H7 | HF | Función anónima escrita de forma compacta. | Para filtros, transformaciones o comparadores. | `memory -> memory.contains("java")`. |
| Interfaz funcional | H7 | HF | Interfaz con un único método abstracto compatible con lambdas. | Al usar `Predicate`, `Function` o `Consumer`. | `Predicate<String> isSafe`. |
| Predicate | H7 | HF | Interfaz funcional que devuelve booleano. | Para filtros y validaciones. | `text -> !text.isBlank()`. |
| Consumer | H7 | HF | Interfaz funcional que consume un valor sin devolver resultado. | Para procesar o imprimir elementos. | `memories.forEach(System.out::println)`. |
| Function | H7 | HF | Interfaz funcional que transforma un valor en otro. | Para mapear datos. | Convertir recuerdos a texto de resumen. |
| Supplier | H7 | HF | Interfaz funcional que produce un valor sin entrada. | Para generación diferida o configuración. | Proveedor de respuesta simulada. |
| Función pura | H7 | HF | Función cuyo resultado depende solo de sus entradas y no causa efectos secundarios. | En validaciones y transformaciones fáciles de probar. | `isPromptSafe(text)`. |
| Efecto secundario | H5 | H7-HF | Cambio externo producido por una operación. | Se controla en persistencia, logs y estado. | Guardar en fichero es un efecto secundario. |
| Función de orden superior | H7 | HF | Función que recibe o devuelve otra función. | En procesamiento avanzado de listas. | Filtrar recuerdos con un criterio recibido. |
| Stream | H7 | HF | Flujo de datos para procesar colecciones de forma declarativa. | Para filtrar, transformar y recoger resultados. | `memories.stream().filter(...)`. |
| Operación intermedia | H7 | HF | Operación de stream que transforma el flujo y devuelve otro stream. | En cadenas declarativas. | `filter`, `map`, `sorted`. |
| Operación terminal | H7 | HF | Operación que produce resultado final o ejecuta procesamiento. | Al cerrar un stream. | `toList()`, `count()`, `forEach()`. |
| filter | H7 | HF | Operación que conserva elementos que cumplen una condición. | Para buscar recuerdos relevantes. | Filtrar recuerdos que contienen “Java”. |
| map | H7 | HF | Operación que transforma cada elemento. | Para generar resúmenes o vistas. | Convertir recuerdos a mayúsculas para mostrar. |
| forEach | H7 | HF | Operación que aplica una acción a cada elemento. | Para mostrar o registrar, con prudencia. | Imprimir cada comando disponible. |
| Optional | H7 | HF | Contenedor que representa presencia o ausencia de valor. | Para evitar algunos `null`. | `Optional<Tool> findTool(command)`. |
| Referencia a método | H7 | HF | Forma abreviada de usar un método existente como función. | Para código más legible cuando procede. | `System.out::println`. |

## 17.10. IA responsable, interfaz gráfica y cierre HF

| Concepto | Hito principal | Otros hitos | Definición operativa | Cuándo se usa | Ejemplo MiniJarvis |
|---|---|---|---|---|---|
| IA responsable | H7 | H1-HF | Uso de IA con registro, validación, seguridad y defensa humana. | En cualquier ayuda de IA y especialmente en H7. | Registrar prompt, respuesta, validación y cambios aplicados. |
| Prompt | H7 | H1-HF | Instrucción o pregunta enviada a una IA. | Para pedir explicación, ejemplo o revisión. | “Explícame por qué mi bucle no termina”. |
| Registro de prompts | H7 | HF | Evidencia del uso de IA y de la validación realizada. | Para transparencia y evaluación. | Tabla con prompt, respuesta útil, cambios y comprobación. |
| Validación humana | H7 | HF | Revisión crítica de una respuesta de IA por parte del alumno. | Antes de aceptar código o explicación. | Ejecutar, probar y explicar el código sugerido. |
| Simulación de IA | H7 | H5-HF | Componente local que imita respuestas sin proveedor real. | Para practicar integración sin secretos ni Internet. | `SimulatedAiAssistant`. |
| Proveedor real de IA | HF | H7 | Servicio externo que respondería prompts reales. | Solo como ampliación controlada, nunca con credenciales reales en clase. | Sustituir simulación por adaptador, si el entorno lo permite. |
| PromptSafety | H7 | H6-HF | Componente que bloquea entradas inseguras. | Para evitar secretos o datos personales. | Rechazar texto que contiene `password` o `api key`. |
| Política de seguridad | H7 | H6-HF | Conjunto de reglas sobre qué se permite y qué se prohíbe. | En IA, logs, ficheros y entregas. | No subir tokens, `.env` real ni datos personales. |
| Evento | HF | H7 | Acción que desencadena código en una interfaz gráfica. | En JavaFX o GUI. | Pulsar botón “Enviar” llama al controlador. |
| JavaFX | HF | H7 | Tecnología Java para interfaces gráficas de escritorio. | Como mejora final opcional. | Ventana con campo de texto y área de respuesta. |
| Vista | HF | H7 | Parte visual de la aplicación. | En MVC o JavaFX. | Pantalla de conversación de MiniJarvis. |
| Controlador | HF | H7 | Clase que recibe eventos de la vista y coordina acciones. | Para no meter lógica en la interfaz. | `ChatController` llama a `Agent.respond`. |
| Panel | HF | H7 | Contenedor visual de controles. | Al organizar una interfaz JavaFX. | Panel con entrada, botón y lista de recuerdos. |
| Control | HF | H7 | Elemento interactivo de interfaz. | En formularios y pantallas. | Botón, campo de texto, tabla. |
| Ventana modal | HF | H7 | Ventana que requiere atención antes de volver a la principal. | Para diálogos concretos. | Confirmar borrado de recuerdo. |
| Tabla visual | HF | H7 | Control que muestra datos en filas y columnas. | Para historial o memoria avanzada. | Tabla de comandos ejecutados. |
| Mensaje de error en UI | HF | H7 | Aviso visible ante un fallo o entrada inválida. | Para orientar sin exponer detalles sensibles. | “No se puede guardar un recuerdo vacío”. |
| Portfolio | HF | H1-HF | Recopilación defendible de evidencias de aprendizaje. | Durante todo el curso y en cierre. | Capturas, código, pruebas, reflexiones y registro IA. |
| Demo | HF | H1-HF | Presentación ejecutable del producto. | Para mostrar funcionamiento real. | Ejecutar MiniJarvis y enseñar H1-H7. |
| Defensa | HF | H1-HF | Explicación individual de decisiones, código, pruebas y aprendizaje. | Para comprobar comprensión. | Laura explica por qué `Tool` evita muchos `if/else`. |
| Recuperación específica | HF | H1-HF | Actividad enfocada en conceptos no consolidados. | Cuando falta evidencia de un tema o hito. | Recuperar Tema 4 implementando memoria con `List`. |
| Mejora opcional | HF | H6-HF | Extensión no obligatoria que amplía el proyecto sin romper el núcleo. | Para alumnado avanzado. | JavaFX, repositorio SQLite o Strategy de IA. |

## 17.11. Uso docente de este mapa operativo

Para programar sesiones:

```text
1. Elegir el hito.
2. Localizar sus conceptos principales.
3. Preparar una actividad MiniJarvis donde aparezcan en código o documentación.
4. Pedir evidencia ejecutable, prueba o defensa breve.
```

Para evaluar:

```text
Un concepto no se considera cubierto solo porque aparezca escrito.
Debe aparecer en una evidencia: código, prueba, diagrama, README, portfolio o defensa individual.
```

Para recuperar:

```text
Si un alumno no domina un concepto, se le asigna una tarea corta del hito donde ese concepto se trabaja de forma principal.
Ejemplo: si falla `List<T>`, recuperar con una memoria H3 mínima; si falla interfaz/polimorfismo, recuperar con una herramienta H5 mínima.
```

<!-- ABP-HEXA-EXPLICACION-INVESTIGACION-MOMENTO-HITO -->

# 18. Reparto ABP/HEXA: qué explica el profesor, qué investiga el alumnado y cuándo hacerlo

Este apartado traduce el mapa operativo anterior a una secuencia docente ABP con modelo HEXA.

Criterio general:

```text
- El profesor explica lo que desbloquea, lo que requiere precisión técnica o lo que afecta a seguridad/evaluación.
- El alumnado investiga lo que puede observar, comparar, justificar, aplicar o defender en MiniJarvis.
- Lo mixto se trabaja con una breve explicación docente, exploración guiada y aplicación inmediata.
```

Uso recomendado dentro de HEXA:

| Fase HEXA | Papel del profesor | Papel del alumnado |
|---|---|---|
| H — Hecho / reto | Presenta el problema MiniJarvis y las restricciones. | Comprende el producto parcial esperado. |
| E — Exploración | Da ejemplos mínimos, preguntas guía y límites. | Observa, compara, prueba y formula hipótesis. |
| X — eXplicación | Formaliza conceptos, vocabulario, errores frecuentes y criterios. | Conecta lo investigado con teoría útil. |
| A — Aplicación | Acompaña, desbloquea y exige evidencias. | Programa, prueba, documenta y defiende. |

Regla práctica:

```text
En cada hito, la explicación docente fuerte debería aparecer justo antes de que el concepto bloquee la construcción de MiniJarvis, no semanas antes como teoría aislada.
```

## 18.1. H1 — Primer asistente básico

| Concepto o familia | Tratamiento ABP/HEXA | Momento aconsejado del hito | Qué explica el profesor | Qué investiga o decide el alumnado | Evidencia MiniJarvis |
|---|---|---|---|---|---|
| Programa, código fuente, ejecución, clase `Main` y método `main` | Explicación docente | H1-S1 / H1-S2, antes de crear el proyecto | Qué es un programa Java mínimo, qué archivo se ejecuta y qué significa compilar/ejecutar. | Qué espera que haga su primer MiniJarvis y cómo comprobar que se ejecuta. | Proyecto que arranca y muestra un mensaje. |
| Sintaxis básica: llaves, paréntesis, punto y coma, mayúsculas/minúsculas | Explicación docente | H1-S2, durante el primer código | Reglas mínimas para que Java compile y cómo leer errores simples. | Localizar errores de sintaxis en ejemplos preparados. | Código H1 sin errores de compilación. |
| Instrucción, secuencia y salida por pantalla | Mixto | H1-S2, al construir los primeros mensajes | Cómo se ejecutan instrucciones en orden y cómo usar `System.out.println`. | Diseñar qué mensajes iniciales dirá MiniJarvis y en qué orden. | Saludo inicial claro y ordenado. |
| Variable, identificador, tipo de dato, `String` y literal | Explicación docente con práctica guiada | H1-S3, antes de personalizar mensajes | Qué es guardar un dato, cómo nombrarlo y por qué el tipo importa. | Comparar nombres buenos/malos y elegir nombres defendibles. | Variable `userName` o equivalente usada correctamente. |
| Constante | Mixto | H1-S3, cuando aparezcan textos repetidos | Diferencia entre variable y constante; evitar valores mágicos. | Detectar qué textos o límites podrían ser constantes. | Constante sencilla para nombre de app o mensaje fijo. |
| Entrada por teclado y `Scanner` | Explicación docente | H1-S4, justo antes de pedir datos | Receta mínima segura para leer texto por consola. | Decidir qué dato debe pedir MiniJarvis y cómo responder si está vacío. | MiniJarvis pide nombre o dato inicial. |
| Concatenación y expresiones simples | Mixto | H1-S4 / H1-S5, al personalizar salida | Cómo unir texto y variables sin perder legibilidad. | Crear respuestas personalizadas y revisarlas con otra persona. | Mensaje personalizado con dato leído. |
| Conversión de tipos básica | Explicación breve / ampliación | H1-S5 o recuperación, solo si se leen números | Diferencia entre leer texto y convertir a número. | Probar qué pasa si se introduce texto donde se espera número. | Mini ejercicio de conversión, no núcleo obligatorio si H1 solo usa texto. |
| Error de sintaxis y error de compilación | Explicación docente | H1-S2-H1-S7, cada vez que aparezca | Cómo distinguir error propio del código y mensaje del IDE. | Registrar un error real y cómo se corrigió. | Evidencia de incidencia o corrección básica. |
| Nombres significativos y comentarios útiles | Investigación guiada | H1-S5 / H1-S6, en revisión | Criterios mínimos: claridad, intención, no comentar obviedades. | Mejorar nombres y eliminar comentarios innecesarios. | README o portfolio con una decisión de limpieza. |
| Evidencia, README básico, portfolio y defensa | Explicación docente | H1-S6 / H1-S7, antes de entregar | Qué prueba aprendizaje: ejecución, código, explicación y defensa. | Seleccionar captura/salida y preparar defensa breve. | README, evidencia de ejecución y defensa H1. |

## 18.2. H2 — Decisiones, bucles, menú y depuración

| Concepto o familia | Tratamiento ABP/HEXA | Momento aconsejado del hito | Qué explica el profesor | Qué investiga o decide el alumnado | Evidencia MiniJarvis |
|---|---|---|---|---|---|
| Condición, booleanos, operadores de comparación y operadores booleanos | Explicación docente | H2-S1, antes de validar entradas | Cómo una expresión decide un camino y cómo combinar condiciones. | Qué condiciones reales necesita MiniJarvis. | Condiciones para entrada vacía o comando reconocido. |
| `if`, `if-else` y condiciones encadenadas | Mixto | H2-S1 / H2-S2, al añadir respuestas alternativas | Sintaxis, flujo y errores frecuentes. | Diseñar respuestas ante casos normales y casos límite. | MiniJarvis responde de forma distinta según entrada. |
| `switch-case`, `default`, `break` y switch mejorado | Explicación docente + comparación | H2-S2, cuando aparezcan varios comandos | Cuándo un `switch` es más claro que muchos `if`; riesgo de olvidar `break`. | Comparar menú con `if/else` y con `switch`. | Menú de comandos legible. |
| `while`, `do-while`, condición de salida y bucle infinito | Explicación docente fuerte | H2-S3, antes de crear el bucle principal | Modelo mental de repetición, actualización de variable y salida segura. | Probar entradas que mantienen o cierran el menú. | Menú que se repite hasta `salir`. |
| `for`, bucle anidado y eficiencia básica | Mixto / ampliación | H2-S4 o conexión con H3 | Para qué sirve repetir con contador y por qué anidar aumenta complejidad. | Detectar si realmente necesitan un `for` o basta `while`. | Ejemplo breve de contador o prueba, sin complicar H2. |
| Menú y comando desconocido | Investigación guiada | H2-S2-H2-S4 | Criterios de usabilidad y seguridad mínima. | Elegir comandos, nombres y respuesta a errores de usuario. | Menú con `ayuda`, `salir` y comando desconocido. |
| Validación de entrada | Mixto | H2-S4, cuando el menú ya funciona | Qué significa aceptar/rechazar datos y cómo avisar. | Probar entradas vacías, espacios y comandos raros. | Tabla de pruebas manuales. |
| Error de ejecución, error lógico y depuración | Explicación docente con demostración | H2-S5-H2-S6, al fallar casos reales | Diferencia entre compilar y funcionar correctamente; trazas básicas. | Registrar un error lógico real y explicar la corrección. | Evidencia de depuración H2. |
| Comportamiento esperado y pruebas manuales | Mixto | H2-S6-H2-S7, antes de entregar | Cómo escribir casos entrada → salida esperada. | Diseñar batería mínima de pruebas. | Documento de pruebas H2. |

## 18.3. H3 — Colecciones y memoria temporal

| Concepto o familia | Tratamiento ABP/HEXA | Momento aconsejado del hito | Qué explica el profesor | Qué investiga o decide el alumnado | Evidencia MiniJarvis |
|---|---|---|---|---|---|
| Estructura de datos y colección | Explicación docente | H3-S1, al plantear memoria | Por qué una variable simple no basta para varios recuerdos. | Qué datos necesita recordar MiniJarvis. | Diseño inicial de memoria temporal. |
| `List<T>`, `ArrayList<T>`, genéricos e índice | Explicación docente con práctica | H3-S2, antes de guardar recuerdos | Cómo crear lista, añadir, consultar tamaño y acceder por posición. | Decidir si el orden de recuerdos importa. | `List<String>` de recuerdos funcionando. |
| Recorrido, `for` y `for` mejorado | Mixto | H3-S3, al mostrar memoria | Diferencia entre recorrer con índice o por elemento. | Elegir cómo mostrar recuerdos: con o sin numeración. | Listado de recuerdos. |
| Mutabilidad e inmutabilidad | Mixto | H3-S4, al revisar diseño | Qué significa modificar una lista y qué riesgos tiene exponerla. | Observar qué pasa si otra clase modifica la lista directamente. | Decisión documentada sobre acceso a memoria. |
| Array | Explicación breve / comparación | H3-S4, como contraste con lista | Tamaño fijo y acceso por índice. | Comparar array frente a `ArrayList` para memoria cambiante. | Justificación de por qué se usa lista. |
| `Set<T>` | Investigación guiada | H3-S5 o ampliación | Qué problema resuelve: no repetir elementos. | Decidir si MiniJarvis debe aceptar recuerdos duplicados. | Mejora opcional contra duplicados. |
| `Map<K,V>` y búsqueda por clave | Investigación guiada / ampliación | H3-S5-H3-S6 | Idea clave-valor y casos de búsqueda rápida. | Proponer preferencias de usuario por clave. | Mapa opcional de preferencias. |
| Clases envoltorio | Explicación breve | H3-S6, si aparecen listas numéricas | Por qué `List<int>` no se usa y sí `List<Integer>`. | Identificar cuándo necesitan números en colecciones. | Ejemplo breve si se usan puntuaciones o contadores. |

## 18.4. H4 — Orientación a objetos y diseño inicial

| Concepto o familia | Tratamiento ABP/HEXA | Momento aconsejado del hito | Qué explica el profesor | Qué investiga o decide el alumnado | Evidencia MiniJarvis |
|---|---|---|---|---|---|
| POO, clase, objeto, instancia y `new` | Explicación docente fuerte | H4-S1, antes de separar `Main` | Diferencia entre plantilla y objeto real; por qué organizar el programa en clases. | Identificar entidades de MiniJarvis. | Primer diseño de clases. |
| Atributo, estado, comportamiento y método | Mixto | H4-S2, al crear `Agent` y `Memory` | Cómo una clase guarda datos y ofrece operaciones. | Decidir qué estado y qué métodos pertenecen a cada clase. | `Agent` y `Memory` con responsabilidades visibles. |
| Parámetro, retorno, método procedimiento y método función | Explicación docente | H4-S2-H4-S3 | Cómo comunicar datos entre métodos sin mezclar consola y lógica. | Clasificar métodos de su código. | Métodos con nombres y retornos defendibles. |
| Constructor, constructor por defecto, constructor con parámetros, sobrecarga y `this` | Explicación docente con ejemplo | H4-S3, antes de instanciar clases propias | Cómo crear objetos válidos e inicializar atributos. | Decidir qué necesita cada objeto para nacer válido. | Constructores de `Agent`/`Memory`. |
| Referencia y tipo referencia | Explicación docente con demostración | H4-S4, cuando se comparten objetos | Que la variable apunta a un objeto y puede haber alias. | Observar efectos de compartir una misma memoria. | Explicación en defensa o portfolio. |
| Responsabilidad y separación de responsabilidades | Mixto | H4-S1-H4-S5, durante todo el rediseño | Criterios para mover código fuera de `Main`. | Decidir qué clase debe hacer cada cosa. | Tabla clase → responsabilidad. |
| Encapsulación, `private`, `public` e invariante | Explicación docente fuerte | H4-S5, antes de cerrar diseño | Por qué proteger atributos y mantener objetos válidos. | Detectar riesgos de atributos públicos. | Atributos privados y métodos públicos mínimos. |
| Paquete, librería y clase predefinida | Explicación breve | H4-S6, al ordenar proyecto | Qué es código propio frente a código de Java. | Ordenar clases sin sobreestructurar. | Estructura de carpetas/paquetes razonable. |
| Javadoc | Investigación guiada | H4-S6-H4-S7 | Qué debe documentarse y qué no. | Escribir documentación útil de un método público. | Javadoc breve en clase clave. |
| Diagrama de clases y relación diagrama-código | Mixto | H4-S7, antes de entregar | Notación mínima y correspondencia con código real. | Crear y defender un diagrama que no sea decorativo. | Diagrama H4 conectado con código. |

## 18.5. H5 — Pruebas, interfaces, polimorfismo y Command

| Concepto o familia | Tratamiento ABP/HEXA | Momento aconsejado del hito | Qué explica el profesor | Qué investiga o decide el alumnado | Evidencia MiniJarvis |
|---|---|---|---|---|---|
| Test de clase, test unitario y aserto | Explicación docente fuerte | H5-S1, antes de refactorizar | Qué se prueba, qué es un aserto y cómo se interpreta un fallo. | Elegir comportamientos pequeños que merecen prueba. | Primer test de `Memory` o comando. |
| TDD y rojo-verde-refactor | Explicación docente + práctica guiada | H5-S2, al añadir una mejora pequeña | Ciclo mínimo sin convertirlo en dogma. | Aplicar TDD a una validación concreta. | Evidencia rojo-verde-refactor. |
| Comportamiento esperado y refactorización segura | Mixto | H5-S2-H5-S3 | Por qué no se refactoriza a ciegas y cómo protegerse. | Crear checklist antes/después. | Tests o pruebas que pasan tras refactor. |
| Interfaz, implementación y método común | Explicación docente | H5-S3, justo antes de crear `Tool` | Interfaz como contrato y clase como implementación. | Identificar qué tienen en común los comandos. | `Tool` y primeras herramientas. |
| Polimorfismo y `List<Tool>` | Explicación docente con demostración | H5-S4, cuando hay varias herramientas | Usar un tipo general para objetos concretos. | Añadir una herramienta nueva sin tocar muchas partes. | Lista de herramientas ejecutables. |
| Command simplificado | Mixto | H5-S4-H5-S5, después de sufrir menú grande | Qué problema resuelve y por qué no se introdujo antes. | Comparar menú con `switch` frente a herramientas. | Registro de refactorización a Command. |
| Clean code y nombres significativos | Investigación guiada | H5-S5-H5-S6 | Criterios mínimos de legibilidad y simplicidad. | Revisar código de otro grupo o versión propia. | Informe de revisión de código. |
| Método default y métodos privados en interfaz | Explicación breve / ampliación | H5-S6 o HF | Que existen, pero no son necesarios para el núcleo. | Valorar si aportan claridad o complejidad innecesaria. | Solo ampliación si el diseño lo pide. |
| RuntimeException y validaciones de dominio | Explicación docente | H5-S6-H5-S7 | Cuándo lanzar excepción por uso incorrecto. | Decidir qué reglas no se pueden romper. | Test de validación o excepción. |

## 18.6. H6 — Persistencia, logs, excepciones y Repository inicial

| Concepto o familia | Tratamiento ABP/HEXA | Momento aconsejado del hito | Qué explica el profesor | Qué investiga o decide el alumnado | Evidencia MiniJarvis |
|---|---|---|---|---|---|
| Persistencia, fichero y ruta | Explicación docente | H6-S1, al plantear memoria persistente | Diferencia entre memoria temporal y datos guardados. | Qué datos merece la pena conservar. | Recuerdos que sobreviven a cerrar el programa. |
| Lectura y escritura de fichero | Explicación docente con práctica | H6-S2, antes de tocar disco | Flujo básico de leer/escribir y riesgos de rutas. | Probar guardar, cerrar y volver a cargar. | Prueba de persistencia. |
| Excepción, `try-catch`, `IOException` y `throws` | Explicación docente fuerte | H6-S2-H6-S3, cuando aparece E/S | Qué puede fallar y cómo no ocultar errores. | Diseñar mensajes comprensibles para fallos. | Manejo de error de fichero. |
| Método peligroso y mensaje de error significativo | Mixto | H6-S3 | Identificar operaciones que pueden fallar. | Simular fallo y comprobar respuesta. | Incidencia documentada. |
| Invariante y estado consistente | Mixto | H6-S4 | Mantener reglas aunque haya persistencia. | Probar datos corruptos o vacíos. | Validaciones antes de guardar/cargar. |
| Log, trazabilidad y reproducibilidad | Mixto | H6-S4-H6-S5 | Qué registrar para reconstruir sin invadir privacidad. | Decidir campos de log y formato seguro. | Historial o log sin secretos. |
| Secreto, placeholder, `.env real`, `.env.example` y datos personales reales | Explicación normativa docente | H6-S5, antes de cualquier configuración | Qué está prohibido subir y cómo usar ejemplos ficticios. | Auditar su entrega buscando datos sensibles. | Checklist de seguridad H6. |
| Repository como idea inicial | Mixto | H6-S6, cuando fichero ya funciona | Separar “qué necesita el dominio” de “cómo se guarda”. | Comparar guardar en lista, fichero y posible BD. | Interfaz o explicación `MemoryRepository`. |
| Base de datos, conexión, consulta, CRUD y transacción | Investigación guiada / ampliación | H6-S7 o HF, nunca como núcleo si el grupo no está listo | Conceptos mínimos y riesgos de persistencia avanzada. | Proponer cómo cambiar fichero por BD. | Diseño opcional o mejora HF. |

## 18.7. H7 — IA responsable, abstracción y programación funcional

| Concepto o familia | Tratamiento ABP/HEXA | Momento aconsejado del hito | Qué explica el profesor | Qué investiga o decide el alumnado | Evidencia MiniJarvis |
|---|---|---|---|---|---|
| IA responsable, prompt, registro de prompts y validación humana | Explicación normativa docente | H7-S1, antes de usar o simular IA | Semáforo de uso, obligación de validar y defensa individual. | Analizar ejemplos de prompts buenos/malos. | Registro IA H7. |
| Simulación de IA y proveedor real de IA | Mixto | H7-S2, antes de integrar componente IA | Por qué se usa simulación para no depender de secretos. | Comparar ventajas/riesgos de simulación frente a proveedor real. | `SimulatedAiAssistant` documentado. |
| PromptSafety, política de seguridad, secretos y datos personales | Explicación docente fuerte | H7-S2-H7-S3, antes de aceptar prompts | Reglas de bloqueo y datos prohibidos. | Diseñar casos de prueba seguros/inseguros. | Validación de prompts. |
| Abstracción y Strategy | Mixto | H7-S3-H7-S4, cuando hay más de una forma de responder | Intercambiar comportamiento sin romper `Agent`. | Valorar si Strategy aporta claridad o es excesivo. | Estrategia opcional o justificación de no usarla. |
| Record y enum | Explicación docente breve + práctica | H7-S4 | `record` para datos inmutables y `enum` para opciones cerradas. | Buscar cadenas mágicas o datos transportados. | `AiResponse` o `CommandType` si procede. |
| Optional | Explicación docente con ejemplo | H7-S5, al buscar herramientas o resultados opcionales | Representar ausencia sin abusar de `null`. | Comparar `null` frente a `Optional<Tool>`. | Búsqueda segura de herramienta. |
| Lambda, interfaz funcional, Predicate, Function, Consumer, Supplier | Explicación breve + exploración | H7-S5-H7-S6 | Sintaxis mínima y relación con funciones. | Modificar filtros o transformaciones simples. | Pequeña mejora expresiva. |
| Stream, filter, map, forEach, operaciones intermedias y terminales | Mixto | H7-S6, después de dominar bucles | Procesar colecciones de forma declarativa sin sustituir comprensión de bucles. | Comparar versión con bucle y con stream. | Filtrado de recuerdos o historial. |
| Función pura, efecto secundario, inmutabilidad y función de orden superior | Investigación guiada | H7-S6-H7-S7 | Diferenciar cálculo puro de operaciones que cambian estado. | Identificar qué métodos son puros y cuáles no. | Reflexión técnica en portfolio. |

## 18.8. HF — Cierre, recuperación y mejora avanzada

| Concepto o familia | Tratamiento ABP/HEXA | Momento aconsejado del hito | Qué explica el profesor | Qué investiga o decide el alumnado | Evidencia MiniJarvis |
|---|---|---|---|---|---|
| Portfolio, demo, defensa y recuperación específica | Explicación docente | HF-S1, al abrir el cierre | Qué evidencia demuestra aprendizaje y cómo será la defensa. | Seleccionar evidencias por hito y detectar lagunas. | Portfolio final y plan de recuperación. |
| Mejora opcional | Mixto | HF-S1-HF-S2 | Criterio: mejorar sin romper núcleo ni ocultar carencias. | Elegir una mejora realista y defendible. | Plan de mejora final. |
| Evento, JavaFX, vista, controlador, panel, control, ventana modal, tabla visual y mensaje de error en UI | Explicación docente breve + investigación guiada | HF-S2-HF-S3, solo si hay mejora gráfica | Modelo mínimo de interfaz gráfica y separación de lógica. | Diseñar pantalla y flujo de eventos. | Prototipo o diseño JavaFX opcional. |
| MVC | Mixto | HF-S3, si se trabaja GUI | Separación Modelo-Vista-Controlador. | Clasificar clases existentes según MVC. | Diagrama MVC de MiniJarvis. |
| Arquitectura hexagonal, puerto, adaptador y adaptador de salida | Explicación docente guiada | HF-S3-HF-S4, si se trabaja arquitectura | Dominio independiente de interfaz, fichero, BD o IA externa. | Identificar dominio, puertos y adaptadores del proyecto. | Diagrama hexagonal simplificado. |
| Base de datos, consulta parametrizada, inserción, actualización, borrado, CRUD y transacción | Explicación docente + práctica controlada | HF-S4, solo como ampliación o recuperación avanzada | Riesgos de persistencia, consultas seguras y consistencia. | Diseñar o implementar CRUD mínimo de recuerdos. | Mejora con SQLite o diseño defendido. |
| Repository avanzado | Mixto | HF-S4-HF-S5 | Cambiar almacenamiento sin romper lógica de negocio. | Comparar fichero y BD como adaptadores. | `MemoryRepository` con segunda implementación o diseño. |
| Defensa global de conceptos | Investigación y defensa del alumnado | HF-S5-HF-S6 | Cómo conectar evidencias con conceptos del curso. | Preparar respuestas: dónde aparece cada concepto y cómo lo sabe. | Defensa individual final. |

## 18.9. Resumen de decisión rápida para el profesorado

| Tipo de concepto | Tratamiento recomendado | Ejemplos |
|---|---|---|
| Bloquea el avance inmediato | Explicación docente antes de programar | `main`, sintaxis, variable, `Scanner`, `while`, clase, constructor. |
| Tiene alto riesgo de malentendido | Explicación docente con demostración | referencia, encapsulación, excepción, polimorfismo, `Optional`. |
| Afecta a seguridad, privacidad o evaluación | Explicación normativa docente | secretos, `.env`, datos personales, IA responsable, defensa. |
| Es una decisión de diseño con alternativas | Investigación guiada | `List` vs `Set` vs `Map`, nombres, responsabilidades, logs. |
| Tiene sentido solo tras sufrir un problema | Mixto después de experiencia práctica | Command, Repository, Strategy, MVC, arquitectura hexagonal. |
| Es avanzado o no imprescindible | Ampliación HF o recuperación específica | JavaFX, base de datos, transacciones, Builder, clases selladas. |

## 18.10. Regla de cierre para ABP/HEXA

```text
El alumnado puede investigar alternativas, comparar soluciones y defender decisiones.
El profesor no delega en la investigación libre los conceptos que sostienen la seguridad, la sintaxis mínima, el modelo mental de ejecución, la POO básica, las pruebas o la evaluación.
```

Aplicación práctica:

```text
Cada hito debe terminar con una pregunta de defensa:
¿Dónde aparece este concepto en tu MiniJarvis, qué problema resuelve y cómo sabes que funciona?
```
