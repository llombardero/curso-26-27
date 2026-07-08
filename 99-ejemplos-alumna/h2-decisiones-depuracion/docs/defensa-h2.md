# Preparación de defensa — H2

Alumno/a: Laura García Martín  
Equipo: Equipo Ada  
Fecha: ejemplo docente

---

## 1. Explicación general

```text
MiniJarvis H2 es una evolución de H1. Ahora el programa tiene un bucle while que mantiene el menú activo hasta escribir salir. Lee comandos con Scanner, normaliza la entrada con trim y toLowerCase, y usa if/else para responder a ayuda, saluda, estado, salir o comando desconocido.
```

---

## 2. Preguntas esenciales

### ¿Cómo se repite el menú?

```text
Con un bucle while que se ejecuta mientras running sea true.
```

### ¿Qué comando permite salir?

```text
El comando salir. Cuando command equals salir, running pasa a false.
```

### ¿Qué ocurre si escribo un comando desconocido?

```text
El programa entra en el else final y muestra: No entiendo ese comando. Escribe ayuda.
```

### ¿Dónde pusiste el breakpoint?

```text
Después de leer command con scanner.nextLine().trim().toLowerCase().
```

### ¿Qué variable observaste?

```text
Observé command, running y userName.
```

### ¿Qué prueba hiciste para `salir`?

```text
Escribí salir y comprobé que el programa mostraba despedida y terminaba.
```

### ¿Qué diferencia viste entre Java y Python?

```text
En Java comparo texto con equals, mientras que en Python se usa ==. Python usa input() y Java usa Scanner.
```

---

## 3. Fragmento que sé defender

```java
while (running) {
    System.out.print("> ");
    String command = scanner.nextLine().trim().toLowerCase();

    if (command.equals("ayuda")) {
        System.out.println("Comandos disponibles: ayuda, saluda, estado, salir");
    } else if (command.equals("salir")) {
        System.out.println("Hasta pronto, " + userName + ".");
        running = false;
    } else {
        System.out.println("No entiendo ese comando. Escribe ayuda.");
    }
}
```

Explicación:

```text
Este fragmento repite el menú, lee el comando, decide qué respuesta dar y termina cuando el comando es salir.
```

---

## 4. Autoevaluación

```text
[x] Puedo explicar el bucle.
[x] Puedo explicar if/else o switch.
[x] Puedo explicar el comando salir.
[x] Puedo explicar una prueba.
[x] Puedo explicar el breakpoint.
```
