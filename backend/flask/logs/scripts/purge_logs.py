"""
Script de purge et de rotation des logs pour Dihya Coding.

Ce module permet de supprimer ou d’archiver les anciens fichiers de logs afin de limiter l’encombrement disque,
de respecter la confidentialité et de garantir la conformité (RGPD, souveraineté).

Bonnes pratiques :
- Ne jamais supprimer de logs critiques sans backup préalable.
- Logger chaque opération de purge avec horodatage.
- Prévoir une politique de rétention configurable (ex : nombre de jours, taille max).
- Restreindre l’accès à ce script aux administrateurs.
- Tester la validité des archives après rotation.

Exécution :
    python purge_logs.py

"""

import os
import shutil
from datetime import datetime, timedelta

LOGS_DIR = "logs"
ARCHIVE_DIR = "logs/archive"
RETENTION_DAYS = int(os.getenv("LOG_RETENTION_DAYS", "30"))
LOG_FILE = "logs/scripts/purge_logs.log"

def log(msg):
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"{datetime.utcnow().isoformat()} | {msg}\n")

def purge_old_logs():
    """
    Archive ou supprime les logs plus anciens que la période de rétention.
    """
    now = datetime.utcnow()
    os.makedirs(ARCHIVE_DIR, exist_ok=True)
    for filename in os.listdir(LOGS_DIR):
        filepath = os.path.join(LOGS_DIR, filename)
        if os.path.isfile(filepath) and filename.endswith(".log"):
            mtime = datetime.utcfromtimestamp(os.path.getmtime(filepath))
            if (now - mtime).days > RETENTION_DAYS:
                archive_path = os.path.join(ARCHIVE_DIR, filename + f".{mtime.strftime('%Y%m%d')}.bak")
                shutil.move(filepath, archive_path)
                log(f"Log archivé : {filename} -> {archive_path}")

def purge_logs_hook(event, sector=None):
    """Injecte la logique métier et le secteur dans l’événement de purge."""
    event['sector'] = sector or 'default'
    return event

# Export DWeb/IPFS (mock)
def export_purged_logs_to_ipfs():
    """Exporte les logs purgés sur IPFS (mock/demo)."""
    # TODO: Intégration réelle IPFS
    return True

if __name__ == "__main__":
    purge_old_logs()
    log("Purge des logs terminée.")
