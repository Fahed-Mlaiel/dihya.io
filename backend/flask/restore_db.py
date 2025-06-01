#!/usr/bin/env python3
"""
Script de restauration (restore) de la base de données pour Dihya Coding.

Ce script permet de restaurer la base de données du backend Flask à partir d’un fichier de backup.
À utiliser uniquement en environnement de développement ou de production avec précaution.

Sécurité :
- Vérifier l’intégrité et la provenance du fichier de backup avant toute restauration.
- Ne jamais restaurer un backup non vérifié en production.
- Protéger les fichiers de backup/restauration avec des permissions restreintes.
- Ne jamais inclure de données sensibles dans les logs.

Usage :
    python restore_db.py chemin/vers/le/backup.db
"""

import os
import sys
import shutil

# Adapter le chemin selon la config SQLAlchemy
DB_PATH = os.getenv("DIHYA_DB_PATH", "dihya.db")

def restore_db(backup_path):
    """Restaure la base de données à partir d’un fichier de backup."""
    if not backup_path or not os.path.exists(backup_path):
        print(f"Fichier de backup introuvable : {backup_path}")
        sys.exit(1)
    if os.path.exists(DB_PATH):
        confirm = input(f"ATTENTION : {DB_PATH} va être écrasé. Continuer ? (oui/non) : ")
        if confirm.lower() != "oui":
            print("Restauration annulée.")
            sys.exit(0)
        os.remove(DB_PATH)
    shutil.copy2(backup_path, DB_PATH)
    os.chmod(DB_PATH, 0o600)  # Permissions restreintes
    print(f"Base de données restaurée depuis : {backup_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage : python restore_db.py chemin/vers/le/backup.db")
        sys.exit(1)
    restore_db(sys.argv[1])