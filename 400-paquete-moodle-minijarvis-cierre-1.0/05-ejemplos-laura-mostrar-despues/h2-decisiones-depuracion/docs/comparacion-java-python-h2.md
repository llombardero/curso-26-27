# Comparación Java ↔ Python — H2

Alumno/a: Laura García Martín  
Fecha: ejemplo docente

---

## 1. Qué hace el programa en Java

```text
El programa pide el nombre, entra en un bucle, lee comandos y responde según el comando escrito. Termina cuando el usuario escribe salir.
```

---

## 2. Fragmento Java relevante

```java
boolean running = true;

while (running) {
    System.out.print("> ");
    String command = scanner.nextLine().trim().toLowerCase();

    if (command.equals("ayuda")) {
        System.out.println("Comandos disponibles: ayuda, saluda, estado, salir");
    } else if (command.equals("salir")) {
        running = false;
    } else {
        System.out.println("No entiendo ese comando. Escribe ayuda.");
    }
}
```

---

## 3. Versión o pseudoversión Python

```python
running = True

while running:
    command = input("> ").strip().lower()

    if command == "ayuda":
        print("Comandos disponibles: ayuda, saluda, estado, salir")
    elif command == "salir":
        running = False
    else:
        print("No entiendo ese comando. Escribe ayuda.")
```

---

## 4. Diferencias observadas

| Aspecto | Java | Python |
|---|---|---|
| Leer texto | `scanner.nextLine()` | `input()` |
| Bucle | `while (running)` | `while running:` |
| Decisiones | `if`, `else if`, `else` | `if`, `elif`, `else` |
| Comparar texto | `command.equals("ayuda")` | `command == "ayuda"` |
| Salir del programa | `running = false;` | `running = False` |

---

## 5. Uso de IA

```text
Usé IA para pedir una versión Python equivalente y después revisé que mantuviera la misma lógica del menú. No copié código Java desde IA.
```

---

## 6. Qué he entendido

```text
He entendido que Java y Python pueden expresar la misma lógica, pero Java usa más sintaxis: tipos, punto y coma, llaves y equals para comparar texto. Python es más corto, pero la idea del bucle y las decisiones es parecida.
```

<!-- AJUSTE-COBERTURA-CONCEPTOS-32 -->

## Respuesta de Laura — cobertura de conceptos de Programación

Relación con `32-lista-conceptos-programacion-por-tema.md`:

```text
H2 trabaja principalmente: Temas 1 y 3.
Foco de aprendizaje: decisiones, menú, repetición y depuración.
```

Conceptos que Laura debe saber defender en este hito:

- if/else
- boolean
- comparaciones
- switch
- enhanced switch como ampliación
- while
- do-while como comparación
- for
- condición de salida
- bucle infinito
- pruebas manuales
- error de compilación
- error lógico
- eficiencia básica

Respuesta modelo de Laura:

> En H2 explico cómo mi agente decide qué hacer, cómo se mantiene funcionando en un bucle y cómo comprobé errores con pruebas concretas.

Evidencia que Laura debe señalar:

- una parte concreta del código o documento donde aparezca el concepto;
- una prueba, ejecución, captura o explicación que demuestre que no lo ha copiado sin entender;
- una mejora razonable que podría hacer si tuviera más tiempo.

