"""
Script d’opération d’urgence pour restauration critique – Dihya Coding

Ce script permet de restaurer rapidement une base de données PostgreSQL
à partir d’un backup en cas d’incident, de rollback urgent ou de failover.

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
import gzip

# Configuration du logger
logging.basicConfig(
    filename='emergency_restore.log',
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

def restore_postgres(backup_file):
    """
    Restaure une base PostgreSQL à partir d’un fichier backup gzip.

    Utilise les variables d’environnement :
        - PGHOST
        - PGPORT
        - PGUSER
        - PGPASSWORD
        - PGDATABASE

    Args:
        backup_file (str): Chemin vers le fichier de backup .sql.gz
    """
    db_name = get_env("PGDATABASE")
    user = get_env("PGUSER")
    host = get_env("PGHOST")
    port = get_env("PGPORT", required=False) or "5432"

    log_and_print(f"Début de la restauration de la base {db_name} depuis {backup_file}")

    try:
        with gzip.open(backup_file, "rb") as f:
            proc = subprocess.run(
                [
                    "psql",
                    "-h", host,
                    "-p", port,
                    "-U", user,
                    "-d", db_name
                ],
                input=f.read(),
                check=True
            )
        log_and_print(f"Restauration terminée avec succès depuis {backup_file}")
    except Exception as e:
        logging.error(f"Erreur lors de la restauration : {e}")
        sys.exit(1)

if __name__ == "__main__":
    """
    Usage :
        PGHOST=... PGUSER=... PGPASSWORD=... PGDATABASE=... python emergency_restore.py <backup_file.sql.gz>
    """
    if len(sys.argv) != 2:
        print("Usage : python emergency_restore.py <backup_file.sql.gz>")
        sys.exit(1)
    backup_file = sys.argv[1]
    log_and_print(f"--- Script de restauration d’urgence lancé à {datetime.utcnow()} ---")
    restore_postgres(backup_file)