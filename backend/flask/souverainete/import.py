"""
Script d’import de données pour la souveraineté numérique Dihya Coding.

Ce module permet d’importer des données (CSV, JSON) dans la base de données du projet,
pour restaurer, migrer ou synchroniser des ressources tout en respectant la souveraineté et la sécurité.

Bonnes pratiques :
- Toujours logger chaque import avec horodatage, type et résultat.
- Valider la structure et le contenu des fichiers avant import.
- Ne jamais importer de secrets ou de données confidentielles sans contrôle d’accès.
- Documenter précisément le périmètre de l’import (tables, champs, etc.).
- Tester l’intégrité de la base après import.

Exécution :
    python import.py

"""

import sqlite3
import json
import csv
import os
from datetime import datetime

DB_PATH = "dihya.db"
IMPORT_DIR = "souverainete/exports"
LOG_FILE = "souverainete/import.log"

def log(msg):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"{datetime.utcnow().isoformat()} | {msg}\n")

def import_json_to_table(json_file, table):
    """
    Importe un fichier JSON dans une table de la base.
    """
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    try:
        with open(json_file, "r", encoding="utf-8") as f:
            data = json.load(f)
        if not isinstance(data, list):
            log(f"Format JSON invalide pour {json_file}")
            return
        for row in data:
            columns = ','.join(row.keys())
            placeholders = ','.join(['?'] * len(row))
            values = list(row.values())
            cur.execute(f"INSERT INTO {table} ({columns}) VALUES ({placeholders})", values)
        conn.commit()
        log(f"Import JSON réussi dans {table} depuis {json_file}")
    except Exception as e:
        log(f"Erreur import JSON {json_file} : {e}")
    finally:
        conn.close()

def import_csv_to_table(csv_file, table):
    """
    Importe un fichier CSV dans une table de la base.
    """
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    try:
        with open(csv_file, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            columns = next(reader)
            for row in reader:
                placeholders = ','.join(['?'] * len(row))
                cur.execute(f"INSERT INTO {table} ({','.join(columns)}) VALUES ({placeholders})", row)
        conn.commit()
        log(f"Import CSV réussi dans {table} depuis {csv_file}")
    except Exception as e:
        log(f"Erreur import CSV {csv_file} : {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    # Exemple d'import (adapter les noms de fichiers/tables selon besoin)
    import_json_to_table(f"{IMPORT_DIR}/users_latest.json", "users")
    import_csv_to_table(f"{IMPORT_DIR}/projects_latest.csv", "projects")
    log("Import terminé.")