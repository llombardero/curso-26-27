# Sesión 209 — Ficha de trabajo del alumnado

## Salida por pantalla y mensajes del asistente

| Hoy vas a… | Al terminar debes poder… |
|---|---|
| Utilizar `System.out.println` para construir una salida clara y ordenada. | Diseñar, implementar y revisar una primera presentación por consola de MiniJarvis. |

**Tiempo previsto:** 45 minutos.
**Hito:** H1.
**Fase HEXA:** Idear.
**Modalidad:** Equipo.

---

## Material que necesitas

- Un ordenador con JDK e IntelliJ disponibles.
- El proyecto H1.
- El capítulo 01 del libro como referencia.
- Pizarra, papel reutilizable o espacio temporal para bosquejar los mensajes antes de modificar el código.

No necesitas crear un documento nuevo para conservar el bosquejo.

---

## 1. Punto de partida

Hasta ahora MiniJarvis ya puede ejecutar instrucciones.

Hoy vamos a trabajar cómo se presenta por consola.

Una primera versión puede limitarse a mostrar mensajes fijos.

Por ejemplo:

```text
Hola.
Soy MiniJarvis.
Esta es mi primera versión.
Estoy aprendiendo a comunicarme por consola.
```

Todavía no necesitamos:

- pedir datos;
- utilizar variables;
- tomar decisiones;
- repetir acciones;
- conectar una IA real.

---

## 2. Una instrucción produce una salida

Observa:

```java
System.out.println("Hola.");
```

La instrucción contiene el mensaje que aparecerá en la consola.

Si añadimos varias:

```java
System.out.println("Hola.");
System.out.println("Soy MiniJarvis.");
System.out.println("Esta es mi primera versión.");
```

se ejecutarán en orden.

Antes de probarlo, predice la salida.

Después ejecútalo y comprueba si coincide.

---

## 3. Diseña el primer guion

Antes de modificar el programa, el equipo debe decidir qué mensajes necesita esta primera presentación.

El guion debe ser breve.

Puede incluir:

```text
saludo
nombre del programa
qué versión es
qué puede hacer ahora
qué aprenderá más adelante
```

No escribáis todavía código.

Primero decidid qué debería leer una persona usuaria.

---

## 4. Revisa el guion

Comprobad vuestro diseño con estas preguntas:

```text
¿Se entiende quién habla?

¿Los mensajes aparecen en un orden lógico?

¿Hay información repetida?

¿Algún mensaje promete algo que MiniJarvis todavía no puede hacer?

¿Una persona que no conoce el proyecto entendería esta primera salida?
```

El objetivo no es hacer muchos mensajes.

El objetivo es que los que existan sean útiles y comprensibles.

---

## 5. Llévalo al programa

Convierte cada mensaje necesario en una instrucción.

Por ejemplo:

```java
public class Main {
    public static void main(String[] args) {
        System.out.println("Hola.");
        System.out.println("Soy MiniJarvis.");
        System.out.println("Esta es mi primera versión.");
    }
}
```

Ejecuta después de introducir los cambios.

Comprueba el resultado directamente en la consola.

---

## 6. Cambia el orden

Elige dos mensajes e intercambia sus instrucciones.

Antes de ejecutar, predice:

```text
¿Qué cambiará?

¿Qué permanecerá igual?
```

Ejecuta.

Comprueba tu predicción.

Después decide qué orden comunica mejor la idea.

No se trata solo de que el programa funcione.

También debe resultar comprensible.

---

## 7. Mejora un mensaje

Elige un mensaje de vuestro programa que pueda expresarse mejor.

Por ejemplo, compara:

```text
Programa iniciado.
```

con:

```text
Hola. Soy MiniJarvis.
```

No hay una única frase correcta.

Debéis poder justificar por qué una redacción resulta más adecuada para esta primera versión.

Modificad únicamente el mensaje elegido y volved a ejecutar.

---

## 8. Resultado observable

Al terminar la sesión debéis poder mostrar directamente una salida que:

```text
[ ] presenta MiniJarvis;
[ ] utiliza varias instrucciones println;
[ ] aparece en el orden previsto;
[ ] resulta comprensible;
[ ] no promete funciones que todavía no existen;
[ ] puede modificarse y volver a comprobarse ejecutando el programa.
```

La consola es la comprobación principal.

No necesitáis una captura de pantalla ni un informe adicional.

---

## 9. Fuente canónica

El resultado técnico queda en el proyecto H1.

Si el equipo toma una decisión significativa sobre cómo debe presentarse MiniJarvis, puede conservarla en Scrum si resulta útil para el trabajo posterior.

No creéis:

- un documento separado con los mensajes;
- una captura de la consola;
- un informe de la sesión;
- una copia del código fuera del repositorio.

---

## 10. Uso de IA

Primero diseñad y revisad vuestro propio guion.

La IA puede utilizarse para:

- aclarar qué hace `System.out.println`;
- comprender un error;
- revisar si un mensaje resulta claro.

No la utilicéis para sustituir la decisión del equipo sobre cómo debe presentarse esta primera versión.

Si su intervención es significativa, registradla en la fuente correspondiente:

- diario individual, si afecta principalmente a un aprendizaje personal;
- Scrum, si afecta a una decisión significativa del equipo.

No es necesario registrar consultas triviales.

Nunca introduzcáis datos personales, contraseñas, tokens ni claves API.

---

## 11. Si os bloqueáis

Antes de pedir ayuda, comprobad:

```text
¿Qué mensaje esperábamos ver?

¿Qué aparece realmente?

¿En qué orden están las instrucciones?

¿Hemos guardado el último cambio?

¿Estamos ejecutando la versión correcta?
```

Cambiad una sola cosa cada vez.

---

## 12. Cierre

Ejecutad vuestra versión y responded:

1. ¿qué instrucción produce cada mensaje?
2. ¿por qué habéis elegido ese orden?
3. ¿qué mensaje habéis mejorado?
4. ¿qué capacidad de MiniJarvis habéis evitado prometer porque todavía no existe?

La sesión está completada cuando el equipo puede ejecutar la presentación de MiniJarvis, explicar el orden de los mensajes y modificar uno de ellos justificando el cambio.
