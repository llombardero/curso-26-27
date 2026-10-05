# Evidencias, IA y seguridad digital

## Programación — 1.º DAW

Este documento es una referencia rápida.

La política completa de uso de IA se encuentra en:

`05-politica-uso-ia-semaforo-registro-defensa.md`

---

## 1. Producto, evidencia y defensa

Durante el curso distinguiremos tres ideas.

| Concepto | Qué significa |
|---|---|
| **Producto** | Lo que has construido. |
| **Evidencia** | Algo localizable y comprobable que permite demostrar funcionamiento o aprendizaje. |
| **Defensa** | La explicación, comprobación o modificación que realizas sobre el producto o la evidencia real. |

Por ejemplo:

```text
Producto
→ programa MiniJarvis

Comprobación
→ ejecutarlo y observar su comportamiento

Defensa
→ localizar una parte del código,
   explicarla y modificarla
```

Que un producto funcione es necesario, pero no demuestra por sí solo que comprendes lo que has construido.

---

## 2. La evidencia debe poder comprobarse

Una evidencia útil debe permitir, según corresponda:

- localizar qué se ha hecho;
- ejecutar o revisar el resultado;
- comprobar su comportamiento;
- relacionarlo con el trabajo realizado;
- explicar decisiones importantes;
- modificar una parte adecuada al nivel trabajado.

No necesitas crear un documento nuevo para cada evidencia.

Utiliza su fuente canónica.

---

## 3. Dónde queda cada cosa

| Resultado | Fuente habitual |
|---|---|
| Código y versiones | Repositorio |
| Instrucciones de ejecución y documentación técnica necesaria | README |
| Tareas, decisiones, bloqueos o retrospectiva significativos del equipo | Scrum |
| Aprendizaje o aportación individual significativa | Diario |
| Uso significativo de IA | Diario o Scrum, según autoría |
| Selección periódica de evidencias | Site en los cierres establecidos |
| Evidencia no-code excepcional sin una ubicación mejor | Espacio previsto para ello |
| Versión evaluada | Mecanismo indicado en la entrega Moodle |
| Defensa | Sobre el producto real; no necesita un documento paralelo |

No copies la misma evidencia en varios lugares únicamente para volver a entregarla.

---

## 4. Semáforo de IA

### Verde — Apoyo al aprendizaje

Por ejemplo:

- pedir una explicación;
- solicitar un ejemplo pequeño;
- aclarar vocabulario;
- comprender un error;
- preparar preguntas de repaso;
- revisar la claridad de una explicación.

Una consulta trivial de este tipo no necesita registrarse de forma rutinaria.

---

### Ámbar — Intervención significativa

Por ejemplo:

- generar un fragmento de código que después utilizas;
- proponer una refactorización;
- generar pruebas que finalmente incorporas;
- ayudar a resolver un bloqueo técnico importante;
- proponer una decisión de diseño que influye en el producto;
- generar documentación que después forma parte del trabajo.

Estos usos requieren:

```text
revisión
   ↓
adaptación cuando sea necesaria
   ↓
comprobación
   ↓
capacidad para explicar y modificar
```

Si la intervención ha sido significativa en un trabajo evaluable, deja trazabilidad en el diario o en Scrum según corresponda.

No necesitas crear un registro de IA independiente.

---

### Rojo — Uso no permitido

Por ejemplo:

- entregar una solución completa que no comprendes;
- presentar como propio código que no puedes explicar;
- ocultar una intervención significativa de IA;
- utilizar IA cuando una actividad individual no lo permita;
- inventar pruebas o resultados que no se han realizado;
- utilizar IA para saltarse las restricciones de una actividad;
- introducir contraseñas, tokens, claves API o datos personales.

---

## 5. Trazabilidad del uso significativo de IA

No se registra cada consulta realizada.

Cuando la IA haya influido de forma significativa en el trabajo evaluable, la anotación debe permitir explicar:

```text
¿Para qué utilicé la IA?

¿Qué aportó?

¿Qué acepté, modifiqué o descarté?

¿Cómo comprobé el resultado?
```

### Si el uso es principalmente individual

Anótalo brevemente en el **diario individual**.

### Si afecta a una decisión o trabajo del equipo

Anótalo en **Scrum**.

No dupliques la misma información en ambos lugares.

No es necesario copiar conversaciones completas ni conservar prompts triviales.

---

## 6. Verificación

Una propuesta de IA no se considera correcta por haber sido generada.

Debes comprobarla.

Si es código:

```text
leer
↓
entender
↓
ejecutar
↓
probar
↓
modificar
↓
explicar
```

Si es documentación, debe describir el proyecto real.

Si es una prueba, debe haberse realizado o razonado correctamente.

Si es un diagrama, debe corresponder con el código o diseño real.

Si es una explicación, debes poder expresarla con tus propias palabras.

---

## 7. Seguridad y privacidad

Nunca introduzcas en una IA ni publiques en el repositorio:

- contraseñas;
- tokens;
- claves API;
- credenciales;
- archivos `.env` con valores reales;
- datos personales;
- información privada de otras personas;
- logs que contengan información sensible;
- capturas que expongan cuentas o credenciales.

Utiliza datos ficticios para las pruebas y ejemplos.

Por ejemplo:

```text
Nombre: Laura
Horas: 4
usuario_ejemplo
API_KEY_EJEMPLO
```

Una clave de ejemplo debe ser claramente ficticia y no permitir acceso a ningún servicio real.

---

## 8. Antes de compartir una evidencia

Comprueba:

```text
[ ] Puedo localizarla.
[ ] Puedo explicar qué demuestra.
[ ] El resultado puede comprobarse.
[ ] Puedo explicar las partes importantes.
[ ] Si hubo IA significativa, existe trazabilidad en diario o Scrum.
[ ] No estoy duplicando información sin necesidad.
[ ] No contiene datos personales ni secretos.
```

Esta lista sirve para revisar.

No tienes que copiarla ni entregarla como otro documento.

---

## 9. Idea clave

```text
El producto se construye.
La evidencia se comprueba.
La persona demuestra que comprende.
La IA significativa deja trazabilidad.
Los secretos nunca se comparten.
```
