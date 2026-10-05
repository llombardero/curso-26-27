# Enunciados y entregas de MiniJarvis

## 1. Regla general

MiniJarvis crece de H1 a H7 como un único programa Java versionado en un mismo repositorio.

Para evitar duplicaciones, distinguimos tres cosas:

```text
lo que construyes
      ↓
lo que debe quedar localizable y comprobable
      ↓
lo que identifica oficialmente la entrega en Moodle
```

No son lo mismo.

Una evidencia no tiene que copiarse a Moodle para ser evaluable si ya está correctamente conservada en su fuente canónica.

Reglas generales:

- no crees un informe por sesión;
- no copies código, README, pruebas, diario o Scrum en varios lugares;
- conserva cada evidencia en su fuente canónica;
- actualiza diario y Scrum solo cuando exista algo significativo que registrar;
- utiliza Drive únicamente para evidencia no-code excepcional sin una ubicación mejor;
- actualiza Sites en los checkpoints C1, C2 y HF, no en cada hito;
- identifica en Moodle la versión concreta que debe evaluarse;
- realiza la defensa sobre el producto y las evidencias reales, sin crear un documento paralelo.

La idea de fondo es:

> El equipo construye. Cada persona demuestra.

---

## 2. Dónde queda cada evidencia

| Evidencia | Fuente canónica | Regla |
|---|---|---|
| Código, historial, pruebas técnicas ligadas al proyecto y versión evaluada | Repositorio Git desde H1 | No se copia de forma rutinaria a Drive o Moodle. |
| Ejecución, comprobaciones, decisiones técnicas, depuración y limitaciones relevantes | README del proyecto | Una explicación breve sustituye informes separados cuando sea suficiente. |
| Aprendizaje o aportación individual significativa | Diario individual | Solo cuando exista algo relevante que conservar. |
| Tareas, decisiones, bloqueos, review, retrospectiva o uso colectivo significativo de IA | Scrum del equipo | Se actualiza cuando cambia el trabajo real, no para demostrar que terminó una sesión. |
| Evidencia no-code sin una fuente mejor | Drive | Uso excepcional. |
| Selección periódica de evidencias y comunicación | Sites | Solo en C1, C2 y HF. |
| Instrucción, identificación de la versión entregada y feedback | Moodle | No funciona como copia del repositorio ni del README. |
| Autoría, comprensión y capacidad de modificar | Defensa | Se realiza sobre el producto real; no necesita un documento independiente. |

Los enlaces estables se registran una vez y solo se corrigen o vuelven a proporcionar si cambian o si una actividad lo solicita expresamente.

---

## 3. Qué debe quedar al cerrar cada tramo

| Tramo | Incremento de MiniJarvis | Qué debe quedar localizable y comprobable |
|---|---|---|
| H0 | Equipo, Scrum y reto inicial de organización | Scrum, ticket individual y evidencia no-code del reto cuando proceda. H0 no necesita repositorio Git ni Sites obligatorios. |
| H1 | Primer asistente por consola | Programa Java mínimo, README técnico, ejecución y comprobaciones, versión estable identificable y defensa individual. |
| H2 | Decisiones, bucles y depuración | Versión estable; comportamiento comprobado y depuración relevante explicada junto al producto. |
| H3 | Memoria con colecciones | Versión estable; estructuras utilizadas, decisiones y casos límite relevantes localizables. |
| C1 | Selección de H1-H3 | Selección periódica de evidencias en Sites y cierre correspondiente, sin copiar todo lo producido en los hitos. |
| H4 | Diseño orientado a objetos | Versión estable; diseño de clases y relación entre el modelo y el código, incluido el diagrama de clases cuando corresponda. |
| H5 | Extensibilidad y código limpio | Versión estable; refactorización y decisiones de diseño o patrón usado o descartado cuando proceda. |
| C2 | Selección de H4-H5 | Selección periódica de evidencias en Sites y cierre correspondiente. |
| H6 | Persistencia y trazabilidad | Versión estable; persistencia, comprobación, seguridad y reproducibilidad según el alcance trabajado. |
| H7 | Integración responsable de IA o simulación robusta | Versión estable; entradas o prompts cuando proceda, riesgos, validación humana, cambios, límites y ausencia de secretos. |
| HF | Producto y comunicación final | Versión final identificable, selección final en Sites y defensa; recuperación únicamente de las evidencias o aprendizajes que correspondan. |

Esta tabla describe **qué debe existir y poder evaluarse**.

No significa que todos esos elementos se vuelvan a subir como archivos a Moodle.

---

## 4. Qué se entrega oficialmente en Moodle

Moodle registra la entrega oficial, pero no debe convertirse en otro repositorio.

Desde H1, la regla general es:

```text
versión evaluada
       +
confirmación de que las fuentes estables siguen accesibles
       +
evidencia no-code excepcional solo si realmente hace falta
```

El enunciado de cada hito concretará si existe algún requisito adicional.

No añadas archivos o enlaces por rutina si la información ya está correctamente conservada en su fuente canónica.

En los checkpoints C1, C2 y HF, Moodle puede registrar el cierre correspondiente, mientras la selección de evidencias permanece en Sites según la estructura prevista para el curso.

---

## 5. Entrega concreta de H1

H1 identifica la primera versión evaluable de MiniJarvis.

En Moodle debes indicar:

```text
Tag: h1-entrega
```

o, si no se utiliza el tag:

```text
Commit estable: <identificador del commit>
```

La versión indicada debe ser la que puedes ejecutar, explicar y defender.

Antes de entregar comprueba:

```text
[ ] La versión indicada es la que quiero presentar.
[ ] El programa se ejecuta.
[ ] El README permite saber qué hace H1 y cómo ejecutarlo.
[ ] Los enlaces estables al diario y Scrum siguen siendo válidos.
[ ] Diario y Scrum están actualizados si durante H1 hubo algo significativo que registrar.
[ ] Puedo explicar y modificar el código de esta versión.
```

No escribas en el diario o Scrum únicamente para completar esta lista.

### En H1 no debes volver a subir de forma rutinaria

- otra copia del código;
- otra copia del README;
- capturas de consola o del repositorio;
- tablas independientes de pruebas;
- informes de ejecución;
- documentos para preparar la defensa;
- un registro independiente de IA;
- copias del diario o Scrum;
- exportaciones PDF o XLSX;
- enlaces estables que ya fueron proporcionados y no han cambiado.

### Evidencia no-code excepcional

Añade un archivo adicional en Moodle solo cuando H1 haya generado una evidencia necesaria que:

1. no sea código;
2. deba conservarse para la evaluación;
3. no tenga ya una fuente canónica adecuada.

Si no existe esa evidencia excepcional, no añadas ningún archivo extra.

---

## 6. Uso de IA y comparación Java-Python

No se entrega un registro independiente de IA.

Si la IA ha tenido una intervención significativa, su trazabilidad debe quedar integrada en:

- el diario individual, si corresponde al aprendizaje o trabajo individual;
- Scrum, si corresponde a una decisión significativa del equipo.

Las consultas triviales no requieren registro.

La comparación Java-Python se realiza cuando corresponda y puede aportar aprendizaje al diario o seleccionarse posteriormente en Sites durante el cierre correspondiente, pero no genera por defecto un informe independiente por hito.

---

## 7. Idea clave

```text
Moodle identifica la entrega.
El repositorio conserva el producto y su historia.
El README explica y permite reproducir.
Diario y Scrum conservan solo proceso significativo.
Drive guarda únicamente evidencia excepcional.
Sites seleccionan en C1, C2 y HF.
La defensa demuestra comprensión.
```

No dupliques una evidencia para demostrar que existe.
