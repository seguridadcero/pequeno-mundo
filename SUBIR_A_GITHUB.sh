#!/usr/bin/env bash
set -euo pipefail
REPO='https://github.com/seguridadcero/pequeno-mundo.git'
SOURCE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
command -v git >/dev/null || { echo 'Git no está instalado.' >&2; exit 1; }
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT
# Clonar primero conserva los commits ya publicados y evita reescribir el historial.
git clone "$REPO" "$TMP/repo"
cd "$TMP/repo"
# Copiar el proyecto completo excepto archivos de control y el propio script.
cp -R "$SOURCE/app" "$SOURCE/assets" "$SOURCE/prototipos" "$SOURCE/docs" .
cp "$SOURCE/AGENTS.md" "$SOURCE/README.md" "$SOURCE/.gitignore" .
git add -A
if git diff --cached --quiet; then echo 'GitHub ya está actualizado.'; exit 0; fi
# Configuración local solo para este commit; no modifica la configuración global.
git -c user.name='Pequeno Mundo Migration' -c user.email='migration@users.noreply.github.com' commit -m 'Importar app V11, pruebas, assets candidatos y prototipos'
git push origin HEAD
printf '\nSubida completada: %s\n' "$REPO"
