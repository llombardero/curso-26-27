# Incidencia H1 — registro completado (Ana García)

Los bloqueos cotidianos se registran en el Diario individual o en Scrum. Completa una incidencia separada únicamente si el análisis del error demuestra un aprendizaje que no cabe en una fila.

## Reproducción

- **Fecha y commit:** 2026-10-08, commit `def456` (S211 — constantes y operaciones)
- **Qué esperaba:** Que al declarar `final int DOBLE_FACTOR = 2;` y usar `int resultado = numero * DOBLE_FACTOR;`, el programa calculase correctamente el doble del número introducido.
- **Qué ocurrió:** El compilador rechazó el código con el error:
  ```
  error: cannot assign a value to final variable DOBLE_FACTOR
      DOBLE_FACTOR = 3;
      ^
  ```
- **Mensaje exacto, sin datos personales:** `cannot assign a value to final variable DOBLE_FACTOR`
- **Pasos mínimos para reproducir:**
  1. Declarar `final int DOBLE_FACTOR = 2;`
  2. Intentar reasignar `DOBLE_FACTOR = 3;` en una línea posterior
  3. Compilar → error

## Hipótesis y prueba

- **Hipótesis:** Al usar `final`, la variable se convierte en constante y no se puede reasignar. El error indica que intenté cambiar el valor de una constante después de inicializarla.
- **Prueba mínima:**
  ```java
  final int DOBLE_FACTOR = 2;
  DOBLE_FACTOR = 3;  // Error de compilación
  ```
- **Resultado:** El compilador muestra `cannot assign a value to final variable DOBLE_FACTOR`.
- **Cambio aplicado:** Eliminé la línea `DOBLE_FACTOR = 3;` y dejé solo la declaración inicial. El programa compiló y ejecutó correctamente.
- **Nueva comprobación:**
  ```java
  final int DOBLE_FACTOR = 2;
  int numero = 5;
  int resultado = numero * DOBLE_FACTOR;
  System.out.println("El doble de " + numero + " es " + resultado);
  // Salida: El doble de 5 es 10
  ```

## Enlaces

- **Fila del diario o Scrum donde apareció:** Diario S211, fila de "Error provocado y corregido"
- **Código o commit relacionado:** [commit def456](https://github.com/ejemplo/minijarvis-h1/commit/def456)
- **Sección del README si afecta a una prueba entregada:** Microprácticas → "Constantes, literales y operadores"

## Aprendizaje

Este error me enseñó que `final` no es solo una etiqueta decorativa: es una restricción del compilador. Una vez declarada con `final`, la variable se convierte en constante y no se puede modificar. Esto es útil para valores que nunca deben cambiar (como factores de cálculo, umbrales, o mensajes fijos), porque previene errores accidentales de reasignación.
