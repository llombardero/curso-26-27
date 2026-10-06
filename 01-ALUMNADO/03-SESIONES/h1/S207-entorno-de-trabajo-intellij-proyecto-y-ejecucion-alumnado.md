# H1.2 — Entorno de trabajo, IntelliJ, proyecto y ejecución

## Entorno de trabajo: IntelliJ, proyecto y ejecución

| Hoy vas a… | Al terminar debes poder… |
|---|---|
| Crear o abrir un proyecto Java mínimo, localizar sus elementos básicos y ejecutarlo desde IntelliJ. | Encontrar `Main.java`, ejecutar el programa, modificar una salida y comprobar el cambio. |

**Tiempo previsto:** 45 minutos.
**Hito:** H1.
**Fase HEXA:** Investigar.
**Modalidad:** Individual.

---

## Material que necesitas

- Un ordenador con JDK e IntelliJ disponibles.
- El espacio de trabajo del proyecto H1.
- La ficha de H1 y el capítulo 01 del libro como referencia.

No necesitas utilizar datos personales, contraseñas, tokens ni claves API.

---

## 1. Objetivo de hoy

Hoy no vamos a construir todavía todo MiniJarvis.

El objetivo es dominar el recorrido mínimo:

```text
abrir proyecto
      ↓
localizar código
      ↓
ejecutar
      ↓
observar resultado
      ↓
modificar
      ↓
volver a ejecutar
```

Si este ciclo no funciona, todavía no tiene sentido añadir más código.

---

## 2. Localiza el proyecto

Abre el proyecto H1 en IntelliJ.

Identifica:

```text
proyecto
└── src
    └── Main.java
```

Comprueba que puedes responder:

- ¿cómo se llama el proyecto?
- ¿dónde está la carpeta `src`?
- ¿dónde está `Main.java`?
- ¿qué archivo estás editando realmente?

No continúes hasta poder localizar estas partes.

---

## 3. Primera ejecución

Abre `Main.java`.

Utiliza un programa mínimo como punto de partida si todavía no existe:

```java
public class Main {
    public static void main(String[] args) {
        System.out.println("Hola, MiniJarvis.");
    }
}
```

Ejecuta el programa desde IntelliJ.

Observa la consola.

Debes poder localizar:

```text
código fuente
     ↓
Run
     ↓
consola
     ↓
resultado
```

---

## 4. Comprueba que estás ejecutando tu código

Antes de seguir, predice qué ocurrirá si cambias:

```java
System.out.println("Hola, MiniJarvis.");
```

por:

```java
System.out.println("MiniJarvis empieza ahora.");
```

Haz el cambio.

Vuelve a ejecutar.

Comprueba que la salida ha cambiado.

Si la consola sigue mostrando el mensaje anterior, no añadas más código hasta averiguar por qué.

---

## 5. Distingue editar y ejecutar

Completa oralmente o en tus notas de trabajo:

```text
Editar significa...

Ejecutar significa...

La consola me permite...

Main.java está...
```

No necesitas memorizar una definición exacta.

Debes poder explicar qué haces en cada paso.

---

## 6. Comprueba un error sencillo

Introduce de forma controlada un error pequeño.

Por ejemplo, elimina temporalmente el punto y coma:

```java
System.out.println("MiniJarvis empieza ahora.")
```

Antes de ejecutar, predice:

```text
¿Compilará?
¿Se ejecutará?
¿Qué crees que mostrará IntelliJ?
```

Comprueba qué ocurre.

Después restaura:

```java
System.out.println("MiniJarvis empieza ahora.");
```

y vuelve a ejecutar.

El objetivo no es memorizar mensajes de error.

El objetivo es reconocer que IntelliJ puede ayudarte a localizar un problema antes de que el programa llegue a ejecutarse.

---

## 7. Resultado observable

Al terminar la sesión debes poder demostrar directamente:

```text
[ ] Sé abrir el proyecto H1.
[ ] Sé localizar src/Main.java.
[ ] Sé localizar la clase Main.
[ ] Sé ejecutar el programa desde IntelliJ.
[ ] Sé encontrar la consola.
[ ] Sé modificar un mensaje.
[ ] Sé volver a ejecutar y comprobar el cambio.
[ ] He observado al menos un error sencillo y lo he corregido.
```

La propia ejecución es la comprobación principal.

No necesitas realizar una captura de pantalla.

---

## 8. Fuente canónica

El resultado técnico de esta sesión permanece en el proyecto.

No crees:

- un informe de ejecución;
- una captura para demostrar que IntelliJ funciona;
- un documento adicional de la sesión.

Si aparece un bloqueo técnico importante que convenga conservar para el equipo, puede anotarse en Scrum.

Si aparece un aprendizaje individual especialmente significativo, puede anotarse brevemente en el diario.

---

## 9. Uso de IA

Primero intenta ejecutar, observar el mensaje de IntelliJ y localizar el problema.

Puedes utilizar IA para comprender un error o un concepto que no entiendas.

No la utilices para sustituir el intento propio ni para generar código innecesariamente complejo.

Si su intervención es significativa, deja una anotación breve en:

- diario individual, si afecta a tu aprendizaje;
- Scrum, si afecta a una decisión o bloqueo del equipo.

No es necesario registrar consultas triviales.

Nunca introduzcas datos personales, contraseñas, tokens ni claves API.

---

## 10. Si te bloqueas

Antes de pedir ayuda, identifica:

```text
¿Qué esperaba que ocurriera?

¿Qué ha ocurrido realmente?

¿Qué mensaje muestra IntelliJ?

¿Qué archivo estoy ejecutando?

¿Qué fue lo último que cambié?
```

Después pide ayuda con esos datos.

No cambies muchas cosas a la vez.

---

## 11. Cierre

Sin mirar una respuesta preparada, explica:

1. dónde está `Main.java`;
2. cómo ejecutas el programa;
3. dónde observas la salida;
4. qué cambio has realizado;
5. cómo has comprobado que se estaba ejecutando la versión modificada.

La sesión está completada cuando puedes abrir, ejecutar, modificar y volver a ejecutar el proyecto H1 sin necesitar una evidencia paralela.
