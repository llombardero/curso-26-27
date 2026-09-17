# Guía de publicación en Moodle Centros Andalucía

## MiniJarvis — Programación y Entornos de Desarrollo — 1.º DAW — Curso 2026/2027

Versión del documento: 1.0 — septiembre de 2026

---

## 1. Finalidad y alcance

Esta guía explica cómo trasladar el paquete MiniJarvis a un aula real de **Moodle Centros Andalucía** sin convertir el curso en un almacén de archivos.

Está dirigida al profesorado que vaya a preparar y mantener el aula virtual de 1.º DAW. Particulariza el uso de Moodle para el servicio corporativo de la Consejería de Desarrollo Educativo y Formación Profesional de la Junta de Andalucía.

Este paquete es una **maqueta documental para publicación**. El archivo ZIP que lo acompaña:

- sirve para transportar y conservar los materiales;
- no es una copia de seguridad restaurable de Moodle;
- no debe renombrarse como `.mbz`;
- no crea automáticamente actividades, grupos, calificaciones ni finalización.

Una copia `.mbz` fiable debe generarse desde una instalación Moodle compatible después de crear y comprobar el curso.

---

## 2. Qué está confirmado y qué debe verificarse

### 2.1. Confirmado en la información oficial publicada por la Junta

La página oficial de Moodle Centros consultada en septiembre de 2026 indica para la plataforma publicada:

- acceso del profesorado mediante credenciales **IdEA**;
- activación de las aulas que vaya a utilizar cada docente;
- uso del bloque específico **Gestión de aulas**;
- presencia del alumnado a través de la información corporativa y PASEN;
- disponibilidad de recursos, tareas, foros, evaluación y actividades interactivas;
- soporte mediante **CAUCE**;
- versión anunciada para 2025/2026: **Moodle 4.5.2+**.

Fuente oficial:

`https://www.juntadeandalucia.es/educacion/eaprendizaje/servicios-educativos-digitales-2/moodle-centros/`

### 2.2. Comprobación obligatoria al comenzar 2026/2027

La publicación oficial consultada todavía muestra novedades de 2025/2026. Antes de construir el aula definitiva hay que comprobar en la instancia real:

- versión exacta de Moodle Centros 2026/2027;
- que el servicio del centro está activo;
- que Programación y Entornos aparecen correctamente en el horario de Séneca;
- cursos que ofrece el bloque Gestión de aulas;
- alumnado y profesorado enrolados;
- tamaño máximo de archivo permitido;
- tipos de actividad y complementos habilitados;
- disponibilidad de grupos, agrupamientos, rúbricas, banco de contenido y finalización;
- comportamiento de la sincronización con Séneca;
- procedimiento y límites vigentes para copias `.mbz`.

No deben inventarse ni fijarse en esta guía límites de subida, complementos o plazos que dependen de la configuración anual de la plataforma.

---

## 3. Modelo de aula recomendado

### Decisión recomendada

Crear un aula principal de **Programación — 1.º DAW — MiniJarvis** desde Gestión de aulas y utilizarla como espacio operativo del proyecto.

Si Entornos de Desarrollo dispone de un aula distinta, mantener separadas:

- las actividades evaluables;
- las calificaciones;
- los RA y CE;
- las recuperaciones;
- las evidencias propias de cada módulo.

Se pueden coordinar ambos módulos mediante enlaces, nombres de hitos y entregables comunes, pero no deben mezclarse sus calificaciones en una única actividad sin una decisión docente explícita.

### Nombre largo sugerido

`Programación — 1.º DAW — MiniJarvis — 2026/2027`

### Nombre corto sugerido

`PROG-1DAW-MINIJARVIS-26-27`

### Formato del curso

Usar **formato por temas**. Los temas representan hitos y no semanas, porque un hito puede ocupar varias sesiones y atravesar interrupciones del calendario.

### Secciones propuestas

```text
00. Empieza aquí
01. H0 — Diseñamos el equipo: HADA, Scrum y torre
02. H1 — Primer MiniJarvis ejecutable
03. H2 — Decisiones, bucles y depuración
04. H3 — Memoria temporal y colecciones
05. H4 — MiniJarvis orientado a objetos
06. H5 — Extensibilidad, Clean Code y patrones
07. H6 — Persistencia, excepciones y trazabilidad
08. H7 — IA responsable, si procede
09. HF — Portfolio, demo, defensa y mejora
10. Recuperación y mejora
11. Ejemplos de Laura — visibles después del intento propio
```

No publicar una sección independiente llamada «Guías docentes». Esos archivos deben permanecer fuera de la vista del alumnado.

---

## 4. Activación inicial en Moodle Centros

1. Acceder a Moodle Centros con la cuenta **IdEA** del profesorado.
2. Confirmar que se está entrando en la plataforma y curso escolar correctos.
3. Localizar el bloque **Gestión de aulas**.
4. Activar solo el aula o las aulas que realmente se utilizarán.
5. Esperar la creación y sincronización cuando el proceso no sea inmediato.
6. Entrar en el aula creada y comprobar:
   - nombre del curso;
   - módulo, grupo y nivel;
   - profesorado participante;
   - listado de alumnado;
   - permisos de edición.
7. Si falta una materia, grupo o estudiante, revisar primero los datos y el horario en Séneca. Si la incidencia persiste, utilizar el canal oficial CAUCE.
8. No crear cuentas manuales duplicadas para sustituir IdEA o PASEN sin autorización institucional.

### Precaución sobre el enrolamiento

La sincronización con Séneca es una particularidad central de Moodle Centros. Antes de añadir o eliminar manualmente usuarios:

- comprobar la situación en Séneca;
- comprobar si el aula procede de Gestión de aulas;
- evitar duplicar matrículas;
- no usar una automatriculación abierta como mecanismo ordinario del grupo oficial.

---

## 5. Configuración base del curso

### 5.1. Apariencia y navegación

- Formato por temas.
- Una sección visible cada vez que comience el hito correspondiente.
- Seguimiento de finalización activado, si está disponible.
- Fechas visibles solo cuando hayan sido confirmadas en el calendario real.
- Descripción breve en la cabecera; las instrucciones completas deben estar en actividades o páginas.
- Bloques laterales mínimos para no sobrecargar la navegación.

### 5.2. Grupos

Crear los equipos provisionales después de HADA y antes de la torre, no antes de observar al grupo.

Configuración recomendada:

- grupos de tres o cuatro;
- nombres neutros: `Equipo 01`, `Equipo 02`, etc.;
- un agrupamiento `Equipos MiniJarvis`;
- modo de grupos separados en las entregas de equipo;
- entregas individuales sin modo de grupo;
- composición revisable después de la retrospectiva de H0.

No incluir puntuaciones HADA, etiquetas personales, necesidades específicas de apoyo ni observaciones privadas en el nombre o descripción pública del grupo.

### 5.3. Finalización

Cuando la instancia lo permita, configurar finalización por condiciones observables:

- consultar la ficha del reto;
- realizar la entrega;
- obtener una calificación o revisión cuando corresponda;
- completar la reflexión o defensa indicada.

No usar «marcar como completada» como sustituto de una evidencia evaluable cuando el hito exige código, pruebas, documentación o defensa.

### 5.4. Libro de calificaciones

Mantener categorías diferenciadas por módulo y evaluación si se usa un espacio coordinado.

No introducir porcentajes hasta que estén confirmados en la programación didáctica vigente. Las rúbricas del paquete sirven para orientar la calidad de las evidencias, pero no autorizan por sí solas un peso numérico.

---

## 6. Correspondencia entre el paquete y Moodle

| Carpeta del paquete | Destino en Moodle Centros | Publicación |
|---|---|---|
| `01-documentos-base/` | Sección `00. Empieza aquí` | Selección de documentos útiles para el alumnado. |
| `02-libro-alumnado-por-hitos/` | Recurso **Libro** o páginas por hito | Publicación progresiva. |
| `03-hitos-fichas-plantillas-checklists/` | Sección de cada hito | Fichas, plantillas y listas de comprobación. |
| `04-guias-docentes-autonomas/` | Archivo privado del profesorado | No publicar íntegramente. |
| `05-ejemplos-laura-mostrar-despues/` | Sección oculta `Ejemplos de Laura` | Mostrar solo después del intento propio. |
| `06-plantillas-globales/` | Sección `Empieza aquí` o hito correspondiente | Solo las plantillas necesarias. |

### Formato de publicación recomendado

- **Página**: instrucciones breves, normas, preguntas guía y avisos.
- **Libro**: capítulos de contenidos del alumnado.
- **Archivo**: PDF, plantilla descargable o documento que no convenga convertir.
- **Carpeta**: conjunto pequeño y coherente de plantillas; evitar carpetas masivas.
- **URL**: repositorio, tablero o recurso externo autorizado.
- **Tarea**: entrega individual o de equipo.
- **Foro**: dudas, decisiones argumentadas o retrospectivas cuando aporte interacción real.

Los archivos Markdown no son el formato de lectura más cómodo dentro de Moodle. Para el contenido que se consultará en línea, copiar y revisar el texto en una Página o Libro. Mantener el `.md` como fuente descargable solo cuando el alumnado vaya a editarlo o incluirlo en su repositorio.

---

## 7. Plantilla de cada sección de hito

Cada sección H0–HF debe conservar este orden:

```text
1. Página — Reto, producto, límites y criterios de éxito
2. Página o Libro — Qué necesitas aprender
3. Archivo/Carpeta — Plantillas de trabajo
4. Tarea — Entrega principal
5. Tarea o actividad — Evidencia individual y defensa
6. Página — Checklist antes de entregar
7. Foro/Página — Review y retrospectiva, cuando corresponda
8. Ejemplo de Laura — oculto inicialmente
```

### Etiquetas visibles sugeridas

- `H — Comprende el reto`
- `E — Explora y formula hipótesis`
- `X — Explica lo aprendido`
- `A — Aplica, prueba, documenta y defiende`

Estas etiquetas hacen visible el ciclo HEXA completo sin fragmentar artificialmente cada sesión.

---

## 8. Configuración de las tareas

### 8.1. Entrega individual

Usar para:

- portfolio individual;
- explicación técnica;
- registro de IA;
- prueba o depuración individual;
- autoevaluación;
- defensa escrita previa;
- recuperación específica.

Configuración recomendada:

- texto en línea para respuestas breves;
- archivo para portfolio o evidencias estructuradas;
- número limitado de archivos cuando sea posible;
- fecha de entrega confirmada;
- botón de envío definitivo si aporta trazabilidad;
- declaración de autoría solo si está disponible y el centro la utiliza;
- retroalimentación mediante comentarios o rúbrica.

### 8.2. Entrega de equipo

Usar para:

- producto o repositorio del hito;
- README del equipo;
- tablero o backlog;
- evidencias de pruebas;
- review y retrospectiva conjunta;
- contrato de equipo.

Comprobar antes de abrirla:

- grupos ya creados;
- agrupamiento correcto;
- actividad configurada como entrega por equipos;
- exigencia de pertenecer a un grupo, si la opción existe;
- una única entrega compartida o entrega individual enlazada, según la evidencia;
- calificación individual separada cuando deba valorarse la defensa personal.

Una calificación de equipo no sustituye la defensa individual.

### 8.3. Qué no debe entregarse en Moodle

- contraseñas;
- tokens o claves API;
- archivos `.env` reales;
- credenciales IdEA o PASEN;
- datos personales innecesarios;
- puntuaciones HADA individuales;
- historiales completos de conversación con datos identificables;
- repositorios con secretos en su historial Git.

---

## 9. Publicación progresiva del itinerario

### Al comenzar el curso

Hacer visibles únicamente:

- bienvenida y funcionamiento;
- política de IA;
- sistema de evidencias y defensa;
- H0;
- materiales estrictamente necesarios para la sesión actual.

### Al comenzar cada hito

1. Revisar las fechas.
2. Revisar los enlaces.
3. Publicar la ficha del reto.
4. Publicar solo los capítulos del libro necesarios.
5. Abrir las plantillas.
6. Configurar las tareas y grupos.
7. Probar la vista del alumnado.
8. Mantener oculto el ejemplo de Laura.

### Después del intento propio

El ejemplo de Laura puede mostrarse para:

- comparar decisiones;
- detectar omisiones;
- mejorar una primera versión;
- preparar la defensa;
- calibrar el nivel esperado.

No debe utilizarse como solución inicial para copiar.

---

## 10. Diseño de H0 en Moodle Centros

La sección H0 debe reflejar la secuencia vigente y proteger la privacidad:

```text
S201 — Curso, MiniJarvis y evidencias
S202 — Scrum mínimo e hipótesis individual HADA
S203 — Equipos provisionales y funciones operativas
S204 — Dos ciclos de torre, prueba, review y retrospectiva
S205 — Revisión del equipo y transferencia a MiniJarvis
```

### Recursos visibles

- presentación del reto;
- ficha del alumnado;
- reglas y materiales de la torre una vez aprobados;
- backlog del equipo;
- criterios de prueba;
- contrato de equipo;
- retrospectiva;
- primer backlog de MiniJarvis.

### Información privada

No publicar ni pedir como entrega pública:

- hoja HADA individual completa;
- puntuaciones por dimensión;
- matriz docente de composición;
- necesidades de apoyo;
- observaciones personales.

HADA es una hipótesis privada de contribución, no una nota, personalidad o rol permanente.

---

## 11. IA responsable dentro del aula virtual

Publicar la política del semáforo de IA en `Empieza aquí` y enlazarla desde cada tarea relevante.

Toda actividad evaluable que permita IA debe indicar:

- usos permitidos;
- usos que requieren registro;
- usos prohibidos;
- evidencia de verificación;
- preguntas posibles de defensa;
- consecuencias educativas de no poder explicar la entrega.

No deben introducirse en herramientas de IA externas:

- nombres completos del alumnado;
- credenciales;
- calificaciones;
- informes personales;
- puntuaciones HADA;
- datos de salud o apoyo educativo;
- código con secretos.

---

## 12. Prueba antes de abrir el curso

Usar la función de cambio de rol o vista como estudiante, si está habilitada, y verificar:

- solo se ven las secciones previstas;
- las guías docentes no son accesibles;
- Laura permanece oculta;
- los enlaces funcionan;
- las instrucciones no dependen de rutas locales;
- las plantillas se descargan;
- las tareas admiten el formato previsto;
- los grupos se aplican a la actividad correcta;
- la finalización no bloquea injustificadamente;
- no aparecen nombres, puntuaciones o documentos privados;
- las fechas coinciden con el calendario real.

Realizar una entrega de prueba con una cuenta o procedimiento autorizado por el centro cuando sea posible. No usar una cuenta personal ficticia si contraviene la gestión corporativa de usuarios.

---

## 13. Copias de seguridad y cambio de curso escolar

Moodle Centros se organiza por cursos escolares. No debe asumirse que el aula seguirá disponible indefinidamente en la misma instancia.

Antes del cierre del curso:

1. revisar y limpiar archivos temporales o innecesarios;
2. generar una copia de seguridad `.mbz` desde Moodle;
3. valorar una copia sin datos del alumnado para reutilizar la estructura;
4. conservar aparte las evidencias que deban custodiarse conforme a la política del centro;
5. comprobar que la descarga terminó correctamente;
6. registrar fecha, módulo, grupo y versión de Moodle;
7. almacenar la copia en una ubicación institucional protegida;
8. no guardar indefinidamente datos personales sin necesidad ni base organizativa.

Al restaurar el curso siguiente:

- hacerlo primero en un aula vacía o de prueba si existe esa posibilidad;
- revisar usuarios, grupos, fechas, restricciones y calificaciones;
- actualizar referencias al curso escolar;
- no restaurar matrículas antiguas sobre el nuevo grupo;
- comprobar compatibilidad con la versión vigente.

---

## 14. Incidencias y soporte

### Revisar primero

- curso escolar y provincia correctos;
- credenciales IdEA/PASEN;
- horario y matrículas en Séneca;
- Gestión de aulas;
- sincronización pendiente;
- permisos de edición;
- tamaño y tipo del archivo;
- grupo y agrupamiento de la actividad;
- visibilidad y restricciones de acceso.

### Escalar mediante CAUCE

Si la incidencia afecta a la plataforma corporativa, sincronización, creación del aula o acceso y no se resuelve con las comprobaciones anteriores, utilizar el soporte oficial CAUCE indicado en la página de Moodle Centros.

Antes de enviar la incidencia, recopilar sin exponer secretos:

- centro y curso escolar;
- aula o materia afectada;
- rol de la persona afectada;
- fecha y hora aproximadas;
- pasos para reproducir el problema;
- mensaje exacto de error;
- captura sin datos personales innecesarios.

---

## 15. Checklist de publicación

### Aula y usuarios

- [ ] Acceso con IdEA comprobado.
- [ ] Aula activada desde Gestión de aulas.
- [ ] Profesorado y alumnado sincronizados con Séneca.
- [ ] No existen cuentas o matrículas manuales duplicadas.

### Estructura

- [ ] Formato por temas.
- [ ] Secciones 00, H0–H7, HF y recuperación.
- [ ] Guías docentes fuera de la vista del alumnado.
- [ ] Ejemplos de Laura ocultos inicialmente.

### Actividades

- [ ] Cada tarea identifica responsable, formato y evidencia.
- [ ] Entregas individuales y de equipo diferenciadas.
- [ ] Grupos y agrupamiento comprobados.
- [ ] Defensa individual prevista.
- [ ] Finalización coherente con las evidencias.

### Seguridad y privacidad

- [ ] Política de IA publicada.
- [ ] No se solicitan secretos ni `.env` reales.
- [ ] HADA y observaciones docentes permanecen privadas.
- [ ] No hay datos personales innecesarios.

### Verificación final

- [ ] Vista del alumnado revisada.
- [ ] Enlaces y descargas comprobados.
- [ ] Fechas confirmadas.
- [ ] Versión y límites de la instancia 2026/2027 registrados.
- [ ] Procedimiento de copia `.mbz` planificado.

---

## 16. Resultado esperado

El aula de Moodle Centros debe funcionar como interfaz de trabajo del curso:

- muestra al alumnado solo lo que necesita en cada momento;
- conserva la trazabilidad H–E–X–A;
- diferencia evidencias individuales y de equipo;
- mantiene separada la evaluación de cada módulo;
- protege HADA, datos personales y credenciales;
- retrasa los ejemplos de Laura hasta el intento propio;
- permite entregar, revisar, defender y mejorar MiniJarvis;
- puede respaldarse al terminar el curso mediante una copia `.mbz` generada desde la propia plataforma.
