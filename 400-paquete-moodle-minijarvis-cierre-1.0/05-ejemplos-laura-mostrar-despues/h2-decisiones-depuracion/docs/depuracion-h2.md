# Informe de depuración — H2

Alumno/a o equipo: Laura García Martín  
Fecha: ejemplo docente

---

## 1. Problema o comportamiento investigado

```text
Quería comprobar por qué el programa entraba en una rama concreta del if/else cuando escribía un comando.
```

---

## 2. Breakpoint usado

Archivo:

```text
src/Main.java
```

Línea o zona:

```text
Después de leer el comando con String command = scanner.nextLine().trim().toLowerCase();
```

---

## 3. Variables observadas

| Variable | Valor observado | Qué significa |
|---|---|---|
| `command` | `ayuda`, después `saluda`, después `salir` | Es el comando escrito por la persona usuaria. |
| `running` | `true` hasta escribir `salir` | Controla si el bucle continúa. |
| `userName` | `Laura` | Nombre leído al inicio. |

---

## 4. Qué descubrí

```text
Descubrí que command cambia en cada vuelta del bucle. Cuando command vale salir, el programa entra en la rama de salir y cambia running a false.
```

---

## 5. Solución o aprendizaje

```text
Entendí que el bucle while depende de running. Si running sigue true, el menú continúa. Si running pasa a false, el programa termina.
```

---

## 6. Verificación posterior

```text
Volví a ejecutar el programa, escribí ayuda, saluda, estado y salir. Comprobé que cada comando entraba en la rama esperada.
```
