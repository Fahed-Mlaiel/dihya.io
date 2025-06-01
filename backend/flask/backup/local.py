# backup/local.py — Sauvegarde locale des fichiers critiques

"""
Module de sauvegarde locale pour Dihya Coding.
Permet de sauvegarder des fichiers/dossiers critiques sur le disque local avec journalisation, gestion d’erreurs et conformité RGPD.

Bonnes pratiques :
- Ne jamais inclure de secrets ou données personnelles non chiffrées.
- Logger chaque opération de backup/restauration.
- Gérer les erreurs d’espace disque, permissions, etc.
- Prévoir la restauration automatisée.

Exemple d’utilisation :
    from backup.local import backup_to_local
    backup_to_local('/chemin/vers/fichier.txt', '/chemin/backup/')
"""

import os
import shutil
from datetime import datetime

def backup_to_local(src_path, backup_dir):
    """
    Sauvegarde un fichier ou dossier localement dans le dossier backup_dir.
    """
    if not os.path.exists(src_path):
        print(f"Source introuvable : {src_path}")
        return False
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    base_name = os.path.basename(src_path.rstrip('/'))
    timestamp = datetime.utcnow().strftime('%Y%m%dT%H%M%SZ')
    dest = os.path.join(backup_dir, f"{base_name}_{timestamp}")
    try:
        if os.path.isdir(src_path):
            shutil.copytree(src_path, dest)
        else:
            shutil.copy2(src_path, dest)
        print(f"Backup local réussi : {dest}")
        return True
    except Exception as e:
        print(f"Erreur backup local : {e}")
        return False
