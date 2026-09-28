# S214 — Píldoras: README y evidencias

> Material de consulta de la sesión S214. Documentar no significa copiar la misma información en varios lugares: cada espacio cumple una función.

## 1. README mínimo de H1

El README permite que otra persona entienda qué hace el proyecto y cómo comprobarlo sin depender de una explicación oral.

### Ejemplo 1 — Qué hace y qué no hace

```markdown
## Qué hace
MiniJarvis muestra un saludo, pide un nombre ficticio y responde por consola.

## Límites de H1
Todavía no incluye menú, bucle, memoria, ficheros ni conexión con una IA real.
```

### Ejemplo 2 — Cómo ejecutar

```markdown
## Cómo ejecutar
1. Abre el proyecto con el JDK indicado.
2. Abre `Main.java`.
3. Ejecuta el método `main`.
4. Escribe un nombre ficticio cuando lo pida la consola.
```

### Ejemplo 3 — Ejemplo verificable

```markdown
## Ejemplo
Entrada: Laura
Salida esperada: Encantado, Laura.
```

### Ejemplo 4 — README que promete demasiado

Evita frases como «MiniJarvis recuerda conversaciones y usa IA» si H1 no lo implementa. El README describe el producto real y sus límites.

## 2. Una evidencia debe demostrar algo

Una evidencia útil conecta una prueba con una afirmación concreta.

### Ejemplo 1 — Evidencia débil

```text
Funciona.
```

No indica qué se probó, con qué entrada ni qué resultado apareció.

### Ejemplo 2 — Evidencia verificable

```text
Prueba: saludo con nombre ficticio.
Entrada usada: Laura.
Salida esperada: Encantado, Laura.
Salida obtenida: Encantado, Laura.
Demuestra: la entrada leída se guarda y se usa en la salida.
Enlace: archivo o captura concreta, no la carpeta general.
```

### Ejemplo 3 — Evidencia de dos ramas

```text
Caso A: horas = 5 → Objetivo alcanzado.
Caso B: horas = 2 → Objetivo pendiente.
Demuestra: se han probado las dos ramas del if/else.
```

### Ejemplo 4 — Evidencia de error útil

```text
Entrada: hola.
Operación: Integer.parseInt(texto).
Resultado: error durante la ejecución.
Demuestra: un texto no convertible no produce un entero válido.
```

No publiques contraseñas, tokens, datos personales ni capturas que los contengan.

## 3. Diario, Site personal y Site de equipo no son lo mismo

Cada lugar responde a una pregunta distinta. No copies la misma reflexión completa en todos.

### Ejemplo 1 — Diario individual: proceso personal

```text
Objetivo: leer un nombre con Scanner.
Acción y prueba: ejecuté dos veces con nombres ficticios.
Bloqueo: olvidé guardar el resultado de nextLine().
Siguiente paso: usar la variable en el saludo.
```

### Ejemplo 2 — Site personal: selección explicada

```text
He seleccionado la prueba de Scanner porque demuestra que puedo seguir el flujo pedir → leer → guardar → usar. El enlace lleva a la evidencia concreta.
```

El Site personal selecciona y explica; no copia todas las entradas del diario.

### Ejemplo 3 — Site de equipo: trabajo colectivo

```text
Decisión del equipo: usar mensajes breves y coherentes.
Prueba compartida: revisión cruzada de la salida.
Review: el incremento muestra el flujo previsto.
Retrospectiva: necesitamos acordar los nombres antes de programar.
```

### Ejemplo 4 — Moodle: índice de entrega

En Moodle se entregan los enlaces solicitados. No hace falta pegar otra copia de todo el diario, el README y los Sites.

## Errores frecuentes

- Enlazar una carpeta general en lugar del archivo o evidencia concreta.
- Guardar una captura sin entrada, salida ni explicación.
- Copiar la misma reflexión en diario, Sites y Moodle.
- Publicar permisos cerrados que impiden revisar la evidencia.
- Incluir datos personales o credenciales.

## Comprueba que lo entiendes

1. Pide a otra persona que ejecute H1 siguiendo solo tu README.
2. Completa una evidencia con entrada, salida esperada, salida obtenida y qué demuestra.
3. Clasifica tres contenidos entre diario, Site personal y Site de equipo.
4. Comprueba cada enlace desde una cuenta que tenga los permisos adecuados.
