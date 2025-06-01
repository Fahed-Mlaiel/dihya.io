"""
Script d’opération d’urgence pour backup critique – Dihya Coding

Ce script permet d’effectuer un backup manuel et rapide de la base de données
en cas d’incident, de maintenance urgente ou avant une opération à risque.

Bonnes pratiques :
- Toujours documenter la raison de l’utilisation du script
- Logger toutes les opérations pour auditabilité
- Protéger l’accès à ce script (usage restreint, logs horodatés)
- Ne jamais inclure de credentials en dur (utiliser variables d’environnement)
"""

import os
import sys
import logging
from datetime import datetime
import subprocess

# Configuration du logger
logging.basicConfig(
    filename='emergency_backup.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s'
)

def log_and_print(msg):
    print(msg)
    logging.info(msg)

def get_env(var_name, required=True):
    value = os.getenv(var_name)
    if required and not value:
        log_and_print(f"Variable d’environnement manquante : {var_name}")
        sys.exit(1)
    return value

def backup_postgres():
    """
    Effectue un dump PostgreSQL sécurisé de la base Dihya.
    Utilise les variables d’environnement :
        - PGHOST
        - PGPORT
        - PGUSER
        - PGPASSWORD
        - PGDATABASE
    """
    db_name = get_env("PGDATABASE")
    user = get_env("PGUSER")
    host = get_env("PGHOST")
    port = get_env("PGPORT", required=False) or "5432"
    backup_dir = os.getenv("BACKUP_DIR", ".")
    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    backup_file = os.path.join(backup_dir, f"backup_{db_name}_{timestamp}.sql.gz")

    log_and_print(f"Début du backup de la base {db_name} vers {backup_file}")

    try:
        with open(backup_file, "wb") as f:
            proc = subprocess.run(
                [
                    "pg_dump",
                    "-h", host,
                    "-p", port,
                    "-U", user,
                    "-d", db_name
                ],
                check=True,
                env=os.environ,
                stdout=subprocess.PIPE
            )
            import gzip
            f.write(gzip.compress(proc.stdout))
        log_and_print(f"Backup terminé avec succès : {backup_file}")
    except Exception as e:
        logging.error(f"Erreur lors du backup : {e}")
        sys.exit(1)

if __name__ == "__main__":
    """
    Usage :
        PGHOST=... PGUSER=... PGPASSWORD=... PGDATABASE=... python emergency_backup.py
    """
    log_and_print(f"--- Script de backup d’urgence lancé à {datetime.utcnow()} ---")
    backup_postgres()