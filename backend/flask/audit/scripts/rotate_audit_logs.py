"""
Script de rotation automatique des logs d’audit pour Dihya Coding.

Ce script archive le fichier de log d’audit actuel avec un timestamp, puis crée un nouveau fichier vide.
Il permet de limiter la taille des logs, d’assurer la conformité RGPD et de faciliter l’audit externe.

Bonnes pratiques :
- Restreindre l’accès à ce script aux administrateurs ou responsables conformité.
- Ne jamais supprimer les logs sans archivage préalable.
- Logger chaque rotation pour traçabilité.
- Prévoir une politique de rétention (ex : suppression des archives trop anciennes).

Exécution :
    python rotate_audit_logs.py --logfile ../audit.log --archive-dir ../archives --max-archives 12
"""

import os
import shutil
import argparse
from datetime import datetime

def rotate_log(logfile, archive_dir, max_archives=12):
    if not os.path.isfile(logfile):
        print(f"Fichier log introuvable : {logfile}")
        return

    os.makedirs(archive_dir, exist_ok=True)
    timestamp = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    archive_file = os.path.join(archive_dir, f"audit_{timestamp}.log")

    # Archive le log actuel
    shutil.move(logfile, archive_file)
    print(f"Log archivé : {archive_file}")

    # Crée un nouveau fichier log vide
    with open(logfile, "w", encoding="utf-8") as f:
        f.write("# Nouveau fichier de log d’audit (rotation)\n")

    # Supprime les archives les plus anciennes si dépassement du quota
    archives = sorted([f for f in os.listdir(archive_dir) if f.startswith("audit_") and f.endswith(".log")])
    if len(archives) > max_archives:
        to_delete = archives[:len(archives)-max_archives]
        for old in to_delete:
            os.remove(os.path.join(archive_dir, old))
            print(f"Archive supprimée (rétention) : {old}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Rotation automatique des logs d’audit Dihya Coding")
    parser.add_argument("--logfile", type=str, required=True, help="Chemin du fichier de log d’audit à archiver")
    parser.add_argument("--archive-dir", type=str, required=True, help="Dossier où archiver les logs")
    parser.add_argument("--max-archives", type=int, default=12, help="Nombre maximum d’archives à conserver")
    args = parser.parse_args()

    rotate_log(args.logfile, args.archive_dir, args.max_archives)