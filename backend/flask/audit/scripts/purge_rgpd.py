"""
Script de purge sélective des logs d’audit pour conformité RGPD (Dihya Coding).

Ce script permet de supprimer ou d’anonymiser les entrées de log liées à un utilisateur spécifique,
en réponse à une demande d’effacement ou d’anonymisation (droit à l’oubli).

Bonnes pratiques :
- Restreindre l’accès à ce script aux administrateurs ou responsables conformité.
- Toujours archiver le log avant toute purge (voir rotate_audit_logs.py).
- Logger chaque opération de purge pour traçabilité.
- Prévoir un mode "dry-run" pour simuler la purge sans modification.

Exécution :
    python purge_rgpd.py --logfile ../audit.log --user alice --anonymize --dry-run
"""

import argparse
import shutil
import os

def purge_log(logfile, user, anonymize=False, dry_run=False):
    if not os.path.isfile(logfile):
        print(f"Fichier log introuvable : {logfile}")
        return

    backup_file = logfile + ".bak"
    shutil.copy2(logfile, backup_file)
    print(f"Backup créé : {backup_file}")

    purged_lines = []
    with open(logfile, "r", encoding="utf-8") as f:
        lines = f.readlines()

    for line in lines:
        if f"| {user} |" in line:
            if anonymize:
                # Remplace le nom d'utilisateur par "anonymized"
                purged_line = line.replace(f"| {user} |", "| anonymized |")
                purged_lines.append(purged_line)
            else:
                # Supprime la ligne (purge totale)
                continue
        else:
            purged_lines.append(line)

    if dry_run:
        print("Mode dry-run activé. Aucune modification écrite.")
        print(f"Lignes qui seraient modifiées ou supprimées pour l’utilisateur '{user}':")
        for line in lines:
            if f"| {user} |" in line:
                print(line.strip())
        return

    with open(logfile, "w", encoding="utf-8") as f:
        f.writelines(purged_lines)
    print(f"Purge terminée pour l’utilisateur '{user}'. Log mis à jour.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Purge RGPD sélective des logs d’audit Dihya Coding")
    parser.add_argument("--logfile", type=str, required=True, help="Chemin du fichier de log d’audit à purger")
    parser.add_argument("--user", type=str, required=True, help="Nom d’utilisateur à purger/anonymiser")
    parser.add_argument("--anonymize", action="store_true", help="Anonymiser au lieu de supprimer")
    parser.add_argument("--dry-run", action="store_true", help="Simuler la purge sans écrire")
    args = parser.parse_args()

    purge_log(args.logfile, args.user, anonymize=args.anonymize, dry_run=args.dry_run)