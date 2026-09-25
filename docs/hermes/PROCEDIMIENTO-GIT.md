# Procedimiento Git/GitHub de MiniJarvis

## Qué es Git y qué es GitHub

### Git

Git es el sistema de control de versiones que funciona en tu ordenador.

Permite:
- saber qué archivos han cambiado;
- guardar puntos de control llamados commits;
- crear ramas;
- comparar versiones;
- recuperar estados anteriores.

El repositorio Git local de MiniJarvis está dentro de:

`/mnt/compartido/Programación-26-27/Minijarvis/.git`

### GitHub

GitHub es un servicio en Internet donde puedes guardar una copia remota de un repositorio Git.

Git y GitHub no son lo mismo:

- `git status`, `git add`, `git commit`, `git branch` trabajan principalmente en tu equipo;
- `git fetch`, `git pull` y `git push` se comunican con un remoto como GitHub.

Un commit puede existir en tu ordenador y todavía no existir en GitHub.

## Conceptos básicos

### Repositorio
Carpeta cuyo historial controla Git.

### Working tree
Los archivos que ves y editas normalmente.

### Staging area
Zona intermedia que contiene lo que entrará en el próximo commit.

### Commit
Punto de control guardado en el historial local.

### Rama
Línea independiente de trabajo.

### Remote
Referencia a otro repositorio, normalmente en GitHub.

### origin
Nombre convencional del remoto principal.

### push
Envía commits locales al remoto.

### fetch
Consulta y descarga información del remoto sin mezclarla con tu trabajo.

### pull
Descarga y además intenta integrar cambios. Por eso debe usarse con más cuidado.

## Comprobación inicial obligatoria

Ejecuta primero:

```bash
pwd
git rev-parse --show-toplevel
git branch --show-current
git status
git remote -v
```

La raíz esperada es:

`/mnt/compartido/Programación-26-27/Minijarvis`

Si no coincide, detén las operaciones Git.

## Cómo leer `git status`

Casos frecuentes:

### `modified`
Archivo que Git ya conocía y ha cambiado.

### `deleted`
Archivo controlado por Git que ahora falta.

### `untracked`
Archivo nuevo que Git todavía no controla.

### `Changes to be committed`
Cambios ya preparados con `git add`.

### `Your branch is ahead of origin/...`
Tienes commits locales que aún no se han enviado a GitHub.

### `Your branch is up to date`
Tu rama local y la referencia remota conocida están sincronizadas.

## Flujo seguro de trabajo

### 1. Antes de trabajar

```bash
git status
git branch --show-current
```

### 2. Después de modificar

```bash
git diff
```

### 3. Preparar solo lo que quieres guardar

Ejemplo:

```bash
git add archivo1 archivo2
```

Evita usar `git add .` a ciegas.

### 4. Revisar lo preparado

```bash
git diff --cached
git status
```

### 5. Comprobar errores de formato

```bash
git diff --check
```

### 6. Crear el commit

```bash
git commit -m "mensaje descriptivo"
```

### 7. Comprobar

```bash
git status
git log --oneline --decorate -5
```

### 8. Antes de subir

```bash
git fetch
git status
```

### 9. Subir a GitHub

```bash
git push
```

## Operaciones prohibidas sin autorización

No ejecutes:

```bash
git reset --hard
git clean -f
git clean -fd
git push --force
git push --force-with-lease
git rebase
git checkout -- .
git restore .
```

No:
- elimines ramas;
- descartes cambios;
- reescribas historial;
- sobrescribas trabajo;
- resuelvas conflictos destructivamente.

## Commits

Cada commit debe:
- corresponder a una tarea concreta;
- no mezclar asuntos independientes;
- tener mensaje descriptivo;
- contener solo archivos relacionados;
- excluir temporales, secretos y artefactos no versionables.

Antes:

```bash
git status
git diff
git diff --check
```

Ejecuta pruebas relevantes.

## Sincronización

Para consultar remoto usa primero:

```bash
git fetch
git status
git log --oneline --decorate --graph --all
```

No hagas `pull` automáticamente si puede provocar mezcla o conflicto inesperado.

## Push

Antes del primer push de la sesión informa:
- rama;
- remoto;
- commits;
- resumen;
- pruebas;
- `git diff --check`;
- advertencias.

Nunca hagas `force push`.

## Archivos problemáticos

No subas:
- secretos;
- `.env` sensibles;
- `.~lock.*#`;
- temporales;
- archivos inesperadamente grandes sin analizarlos;
- artefactos generados excluidos por `.gitignore`.

Si un ZIP, PDF, PPTX u otro binario puede regenerarse de forma fiable, analiza si debe seguir versionado.
