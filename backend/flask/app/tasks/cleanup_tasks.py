"""
Tâches asynchrones de nettoyage et maintenance pour Dihya Coding.

Ce module centralise les tâches de nettoyage périodique (fichiers temporaires, logs, données obsolètes, etc.)
pour garantir la performance, la sécurité et la conformité du backend.

Bonnes pratiques :
- Protéger l’accès aux tâches critiques par des vérifications de permissions.
- Logger chaque opération de nettoyage pour audit et monitoring.
- Prévoir des options de dry-run pour éviter les suppressions accidentelles.
- Ne jamais supprimer de données critiques sans sauvegarde préalable.
- Prévoir des tests unitaires pour chaque tâche de nettoyage.

Exemple d’utilisation :
    from backend.flask.app.tasks.cleanup_tasks import cleanup_temp_files

    cleanup_temp_files.delay(dry_run=True)
"""

import os
import logging
from typing import Optional

try:
    from backend.flask.app.tasks import celery_app
except ImportError:
    celery_app = None  # fallback pour tests sans Celery

TEMP_DIR = "/tmp/dihya"
LOGS_DIR = "/workspaces/Dihya/Dihya/backend/flask/logs"

def list_files(directory: str):
    """Liste les fichiers d’un répertoire (non récursif)."""
    try:
        return [os.path.join(directory, f) for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    except Exception as e:
        logging.error(f"[CLEANUP] Erreur lors du listing de {directory}: {e}")
        return []

if celery_app:
    @celery_app.task(bind=True, name="cleanup_temp_files")
    def cleanup_temp_files(self, dry_run: bool = True) -> dict:
        """
        Tâche asynchrone de nettoyage des fichiers temporaires.

        Args:
            dry_run (bool): Si True, ne supprime rien, retourne la liste des fichiers ciblés.

        Returns:
            dict: Statut et liste des fichiers supprimés ou à supprimer.

        Sécurité :
            - Logger chaque suppression.
            - Ne jamais supprimer de fichiers critiques.
        """
        files = list_files(TEMP_DIR)
        if dry_run:
            logging.info(f"[CLEANUP] (DRY RUN) Fichiers à supprimer : {files}")
            return {"status": "dry_run", "files": files}
        deleted = []
        for f in files:
            try:
                os.remove(f)
                deleted.append(f)
                logging.info(f"[CLEANUP] Fichier supprimé : {f}")
            except Exception as e:
                logging.error(f"[CLEANUP] Erreur suppression {f}: {e}")
        return {"status": "success", "deleted": deleted}
else:
    def cleanup_temp_files(dry_run: bool = True) -> dict:
        """
        Version synchrone fallback pour tests locaux sans Celery.
        """
        files = list_files(TEMP_DIR)
        if dry_run:
            logging.info(f"[CLEANUP] (DRY RUN) Fichiers à supprimer : {files}")
            return {"status": "dry_run", "files": files}
        deleted = []
        for f in files:
            try:
                os.remove(f)
                deleted.append(f)
                logging.info(f"[CLEANUP] Fichier supprimé : {f}")
            except Exception as e:
                logging.error(f"[CLEANUP] Erreur suppression {f}: {e}")
        return {"status": "success", "deleted": deleted}