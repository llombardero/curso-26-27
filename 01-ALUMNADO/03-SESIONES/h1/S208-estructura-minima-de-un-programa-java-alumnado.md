# Sesión 208 — Ficha de trabajo del alumnado

## Estructura mínima de un programa Java

| Hoy vas a… | Al terminar debes poder… |
|---|---|
| Reconocer las partes básicas de un programa Java sencillo. | Localizar `Main`, `main`, los bloques, las instrucciones y explicar dónde comienza la ejecución. |

**Tiempo previsto:** 45 minutos.
**Hito:** H1.
**Fase HEXA:** Investigar.
**Modalidad:** Individual.

---

## Material que necesitas

- Un ordenador con JDK e IntelliJ disponibles.
- El proyecto H1.
- El capítulo 01 del libro como referencia.

---

## 1. Punto de partida

En la sesión anterior aprendiste a abrir, ejecutar y modificar un proyecto.

Ahora vamos a entender mejor qué estamos ejecutando.

Observa esta estructura mínima:

```java
public class Main {
    public static void main(String[] args) {
        System.out.println("Hola.");
    }
}
```

No necesitas memorizarla como una fórmula.

Necesitas reconocer sus partes y saber qué papel cumple cada una.

---

## 2. Localiza las partes

Sobre el código anterior, identifica:

```text
archivo
clase
método main
bloque de la clase
bloque del método
instrucción
texto que aparecerá en consola
```

Comprueba especialmente que puedes distinguir:

```text
Main
```

de:

```text
main
```

No representan lo mismo.

---

## 3. Dónde comienza la ejecución

En este programa Java, la ejecución comienza en:

```java
public static void main(String[] args)
```

Por ahora no necesitas explicar en profundidad cada palabra de esa línea.

Sí debes poder reconocer que `main` es el punto de entrada de este programa.

Señálalo directamente en tu propio código.

---

## 4. Sigue el orden de las instrucciones

Observa:

```java
public class Main {
    public static void main(String[] args) {
        System.out.println("Uno");
        System.out.println("Dos");
        System.out.println("Tres");
    }
}
```

Antes de ejecutarlo, predice la salida.

Después ejecútalo y comprueba tu predicción.

A continuación intercambia dos instrucciones.

Vuelve a predecir y ejecutar.

Explica:

```text
qué has cambiado
qué se ha mantenido igual
por qué ha cambiado la salida
```

---

## 5. Reconoce los bloques

Las llaves delimitan bloques de código.

En este ejemplo:

```java
public class Main {
    public static void main(String[] args) {
        System.out.println("MiniJarvis empieza.");
    }
}
```

hay un bloque de la clase y otro bloque dentro de `main`.

Localiza:

```text
{
}
```

y comprueba qué apertura corresponde con qué cierre.

No necesitas todavía estudiar estructuras más complejas.

---

## 6. Reconoce una instrucción

Una instrucción como:

```java
System.out.println("MiniJarvis empieza.");
```

produce un resultado observable.

En este caso:

```text
MiniJarvis empieza.
```

Localiza en tu programa:

1. una instrucción;
2. el texto que contiene;
3. el resultado que produce.

---

## 7. Comprueba errores de estructura

Introduce de forma controlada un único error cada vez.

### Prueba A — Punto y coma

Elimina temporalmente:

```text
;
```

de una instrucción.

Predice qué ocurrirá.

Comprueba el resultado y corrígelo.

### Prueba B — Comillas

Modifica temporalmente una línea para que falte una comilla.

Observa qué señala IntelliJ.

Corrige el error antes de continuar.

### Prueba C — Llave

Elimina temporalmente una llave de cierre.

Observa cómo cambia la interpretación de la estructura.

Después restáurala.

No cambies varios elementos a la vez.

---

## 8. Reescribe el programa mínimo

Sin copiar línea por línea, intenta reconstruir un programa que:

1. tenga una clase `Main`;
2. contenga el método `main`;
3. muestre tres mensajes;
4. compile;
5. se ejecute.

Puedes consultar el capítulo 01 si necesitas recordar alguna parte.

El objetivo no es hacerlo de memoria perfecta, sino comprender qué pieza falta cuando algo no funciona.

---

## 9. Resultado observable

Al terminar debes poder demostrar directamente:

```text
[ ] Localizo Main.java.
[ ] Localizo la clase Main.
[ ] Localizo el método main.
[ ] Sé dónde comienza la ejecución.
[ ] Distingo clase y método.
[ ] Reconozco los bloques delimitados por llaves.
[ ] Reconozco una instrucción.
[ ] Puedo predecir el orden de varias salidas.
[ ] Puedo corregir un error sencillo de sintaxis.
[ ] El programa compila y se ejecuta.
```

La comprobación se realiza sobre el propio código.

No necesitas una captura ni un documento adicional.

---

## 10. Fuente canónica

El resultado de esta sesión permanece en el proyecto H1.

No crees:

- una ficha adicional de estructura;
- una captura de IntelliJ;
- un informe de errores;
- una copia del código en otro documento.

Si aparece un aprendizaje individual especialmente significativo, puede anotarse brevemente en el diario.

Si aparece un bloqueo técnico relevante para el equipo, puede registrarse en Scrum.

---

## 11. Uso de IA

Primero intenta:

```text
leer
↓
predecir
↓
ejecutar
↓
observar
↓
corregir
```

Puedes utilizar IA para pedir una explicación de un error o de una parte del código que no comprendas.

No la utilices para sustituir la lectura y explicación de tu propio programa.

Si su intervención es significativa, deja una anotación breve en la fuente correspondiente.

No es necesario registrar consultas triviales.

Nunca introduzcas datos personales, contraseñas, tokens ni claves API.

---

## 12. Si te bloqueas

Antes de pedir ayuda, responde:

```text
¿Qué parte del programa estoy mirando?

¿Qué esperaba que ocurriera?

¿Qué ha ocurrido?

¿Qué línea he cambiado?

¿Qué error señala IntelliJ?
```

Después formula una pregunta concreta.

---

## 13. Cierre

Sobre tu propio código, señala y explica:

1. dónde está la clase `Main`;
2. dónde está el método `main`;
3. dónde comienza la ejecución;
4. qué instrucciones se ejecutan;
5. en qué orden se ejecutan;
6. qué resultado produce cada una.

La sesión está completada cuando puedes señalar estas partes directamente en tu programa, modificar una instrucción y explicar el efecto del cambio.
