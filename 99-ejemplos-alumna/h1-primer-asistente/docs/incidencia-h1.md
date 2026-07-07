# Incidencia — H1 Primer asistente básico

Alumno/a o equipo: Laura García Martín  
Fecha: ejemplo docente  
Estado: Resuelta

---

## 1. Descripción del problema

¿Qué ocurrió?

```text
Al principio intenté imprimir el nombre del asistente escribiendo ASSISTANT_NAME dentro de las comillas. El programa imprimía el texto ASSISTANT_NAME en vez del valor MiniJarvis.
```

---

## 2. Dónde ocurrió

Archivo o lugar:

```text
src/Main.java
```

Línea aproximada, si procede:

```text
Mensaje de saludo inicial.
```

---

## 3. Mensaje de error o síntoma

```text
No era un error de compilación. Era un error de salida: el programa mostraba un texto que no era el esperado.
```

---

## 4. Pasos para reproducir

1. Escribir `System.out.println("Hola, soy ASSISTANT_NAME.");`.
2. Ejecutar el programa.
3. Ver que la salida muestra `ASSISTANT_NAME` como texto literal.

---

## 5. Causa probable

```text
Dentro de las comillas Java interpreta todo como texto literal. Para usar el valor de una constante, debe ir fuera de las comillas y unirse con +.
```

---

## 6. Solución aplicada

¿Qué cambiaste?

```text
Cambié la línea por System.out.println("Hola, soy " + ASSISTANT_NAME + ".");
```

---

## 7. Verificación

¿Cómo comprobaste que ya funcionaba?

```text
Ejecuté otra vez el programa y comprobé que ahora mostraba Hola, soy MiniJarvis.
```

---

## 8. Qué aprendí

```text
Aprendí la diferencia entre escribir texto literal dentro de comillas y usar el valor de una variable o constante fuera de las comillas.
```

---

## 9. Uso de IA, si procede

¿Usaste IA para entender o resolver la incidencia?

```text
No para esta incidencia concreta.
```
