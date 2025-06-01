#!/usr/bin/env python3
"""
Script de sauvegarde (backup) de la base de données pour Dihya Coding.

Ce script permet de créer une copie de sécurité de la base de données du backend Flask.
À utiliser uniquement en environnement de développement ou de production avec précaution.

Sécurité :
- Ne jamais stocker les backups dans un dossier public ou accessible via le web.
- Protéger les fichiers de backup avec des permissions restreintes.
- Ne jamais inclure de données sensibles dans les logs.

Usage :
    python backup_db.py [chemin/vers/le/backup.db]
    (par défaut : backup_dihya.db dans le dossier courant)
"""

import os
import sys
import shutil
from datetime import datetime

# Adapter le chemin selon la config SQLAlchemy
DB_PATH = os.getenv("DIHYA_DB_PATH", "dihya.db")

def backup_db(backup_path=None):
    """Crée une copie de la base de données SQLite."""
    if not os.path.exists(DB_PATH):
        print(f"Base de données introuvable : {DB_PATH}")
        sys.exit(1)
    if not backup_path:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = f"backup_dihya_{timestamp}.db"
    shutil.copy2(DB_PATH, backup_path)
    os.chmod(backup_path, 0o600)  # Permissions restreintes
    print(f"Backup créé : {backup_path}")

if __name__ == "__main__":
    dest = sys.argv[1] if len(sys.argv) > 1 else None
    backup_db(dest)