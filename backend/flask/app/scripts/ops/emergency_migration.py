"""
Script d’opération d’urgence pour migrations critiques – Dihya Coding

Ce script permet d’appliquer ou de restaurer rapidement une migration critique
en cas de problème de production, rollback urgent ou failover.

Bonnes pratiques :
- Toujours documenter la raison de l’utilisation du script
- Ne jamais modifier la structure sans validation préalable
- Logger toutes les opérations pour auditabilité
- Protéger l’accès à ce script (usage restreint, logs horodatés)
"""

import logging
import sys
from datetime import datetime
from alembic.config import CommandLine, Config

# Configuration du logger
logging.basicConfig(
    filename='emergency_migration.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s'
)

def log_and_print(msg):
    print(msg)
    logging.info(msg)

def apply_migration(revision="head"):
    """
    Applique la migration jusqu’à la révision spécifiée (par défaut 'head').
    """
    log_and_print(f"Début de la migration vers la révision : {revision}")
    alembic_cfg = Config("alembic.ini")
    try:
        CommandLine().run_cmd(alembic_cfg, ['upgrade', revision])
        log_and_print(f"Migration appliquée avec succès jusqu’à {revision}")
    except Exception as e:
        logging.error(f"Erreur lors de la migration : {e}")
        sys.exit(1)

def downgrade_migration(revision):
    """
    Restaure la base à la révision spécifiée (rollback).
    """
    log_and_print(f"Rollback vers la révision : {revision}")
    alembic_cfg = Config("alembic.ini")
    try:
        CommandLine().run_cmd(alembic_cfg, ['downgrade', revision])
        log_and_print(f"Rollback effectué avec succès jusqu’à {revision}")
    except Exception as e:
        logging.error(f"Erreur lors du rollback : {e}")
        sys.exit(1)

if __name__ == "__main__":
    """
    Usage :
        python emergency_migration.py upgrade [revision]
        python emergency_migration.py downgrade [revision]
    """
    if len(sys.argv) < 3:
        print("Usage : python emergency_migration.py [upgrade|downgrade] [revision]")
        sys.exit(1)

    action = sys.argv[1]
    revision = sys.argv[2]

    log_and_print(f"--- Script d’urgence lancé par {sys.argv[0]} à {datetime.utcnow()} ---")
    if action == "upgrade":
        apply_migration(revision)
    elif action == "downgrade":
        downgrade_migration(revision)
    else:
        print("Action non reconnue. Utilisez 'upgrade' ou 'downgrade'.")
        sys.exit(1)