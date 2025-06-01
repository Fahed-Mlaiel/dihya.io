#!/bin/bash
# Script de surveillance Git en temps réel pour Codespace
# Respecte la logique métier : ne fait un pull que si le repo est propre
# Journalise chaque action dans git_auto_pull.log

REPO_PATH="$(pwd)"
LOG_FILE="$REPO_PATH/git_auto_pull.log"

while true; do
    # Surveille les modifications dans le dossier de travail (hors .git)
    inotifywait -r -e modify,create,delete --exclude ".git|node_modules|__pycache__|\.venv|env|dist|build|\.mypy_cache|\.pytest_cache" "$REPO_PATH" >/dev/null 2>&1
    # Vérifie si le repo est propre
    if git -C "$REPO_PATH" diff --quiet && git -C "$REPO_PATH" diff --cached --quiet; then
        echo "[$(date)] Changement détecté, repo propre, git pull en cours..." >> "$LOG_FILE"
        git -C "$REPO_PATH" pull >> "$LOG_FILE" 2>&1
        echo "[$(date)] git pull terminé." >> "$LOG_FILE"
    else
        echo "[$(date)] Changement détecté, mais repo non propre, pull ignoré." >> "$LOG_FILE"
    fi
    sleep 2
done
