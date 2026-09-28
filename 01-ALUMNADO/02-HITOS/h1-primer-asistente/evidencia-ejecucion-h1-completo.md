# Evidencia de ejecución H1 — MiniJarvis

> No entregues este archivo por separado. Usa su contenido para completar `README.md`, que es la fuente canónica de ejecución y pruebas.

## Caso mínimo

- Comando o procedimiento de ejecución: `java -cp src Main`
- Entrada:
  ```
  Nombre: Ana
  Número: 5
  ```
- Salida esperada:
  ```
  Hola, Ana. Bienvenida a MiniJarvis.
  El doble de 5 es 10.
  ```
- Salida obtenida:
  ```
  Hola, Ana. Bienvenida a MiniJarvis.
  El doble de 5 es 10.
  ```
- Fecha y commit probado: 2026-10-15, commit `abc123def456` (tag `h1-entrega`)

## Caso alternativo

- Entrada o condición:
  ```
  Nombre: Carlos
  Número: -3
  ```
- Predicción antes de ejecutar:
  El programa debe mostrar "El número no es positivo" porque -3 no es mayor que 0, por lo que se ejecuta la rama `else` del `if/else`.
- Resultado:
  ```
  Hola, Carlos. Bienvenido a MiniJarvis.
  El número no es positivo.
  ```
- Explicación:
  La comparación `numero > 0` evalúa a `false` cuando numero = -3. Por tanto, se ejecuta la rama `else` que imprime "El número no es positivo." en lugar de calcular y mostrar el doble.

---

Una captura es opcional. El texto reproducible y el commit son obligatorios; nunca captures datos personales, rutas sensibles o credenciales.
