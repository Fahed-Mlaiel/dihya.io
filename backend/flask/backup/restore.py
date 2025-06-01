# backup/restore.py — Restauration automatisée des backups

"""
Module de restauration pour Dihya Coding.
Permet de restaurer des fichiers/dossiers à partir des backups locaux ou cloud, avec journalisation, gestion d’erreurs et conformité RGPD.

Bonnes pratiques :
- Ne jamais restaurer de secrets ou données personnelles non chiffrées.
- Logger chaque opération de restauration.
- Gérer les erreurs d’accès, permissions, etc.
- Prévoir la vérification d’intégrité post-restauration.

Exemple d’utilisation :
    from backup.restore import restore_local
    restore_local('/chemin/backup/fichier_20250528T120000Z', '/chemin/vers/restaure/')
"""

import os
import shutil

def restore_local(backup_path, restore_dir):
    """
    Restaure un fichier ou dossier depuis un backup local.
    """
    if not os.path.exists(backup_path):
        print(f"Backup introuvable : {backup_path}")
        return False
    if not os.path.exists(restore_dir):
        os.makedirs(restore_dir)
    base_name = os.path.basename(backup_path.rstrip('/'))
    dest = os.path.join(restore_dir, base_name)
    try:
        if os.path.isdir(backup_path):
            shutil.copytree(backup_path, dest)
        else:
            shutil.copy2(backup_path, dest)
        print(f"Restauration locale réussie : {dest}")
        return True
    except Exception as e:
        print(f"Erreur restauration locale : {e}")
        return False
