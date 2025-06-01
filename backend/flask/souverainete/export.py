"""
Script d’export des données pour la souveraineté numérique Dihya Coding.

Ce module permet d’exporter tout ou partie de la base de données (ou d’autres ressources)
dans un format ouvert (CSV, JSON) pour garantir la portabilité, la transparence et la souveraineté des utilisateurs.

Bonnes pratiques :
- Toujours logger chaque export avec horodatage et type d’export.
- Ne jamais exporter de secrets ou de données confidentielles sans contrôle d’accès.
- Documenter précisément le périmètre de l’export (tables, champs, etc.).
- Prévoir des formats ouverts et interopérables.
- Tester la validité des fichiers exportés.

Exécution :
    python export.py

"""

import sqlite3
import json
import csv
from datetime import datetime

DB_PATH = "dihya.db"
EXPORT_DIR = "souverainete/exports"
LOG_FILE = "souverainete/export.log"

import os
os.makedirs(EXPORT_DIR, exist_ok=True)

def log(msg):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"{datetime.utcnow().isoformat()} | {msg}\n")

def export_table_to_json(table):
    """
    Exporte une table de la base en JSON.
    """
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    try:
        cur.execute(f"SELECT * FROM {table}")
        rows = cur.fetchall()
        columns = [desc[0] for desc in cur.description]
        data = [dict(zip(columns, row)) for row in rows]
        out_file = f"{EXPORT_DIR}/{table}_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}.json"
        with open(out_file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        log(f"Export JSON réussi pour la table {table} : {out_file}")
    except Exception as e:
        log(f"Erreur export JSON table {table} : {e}")
    finally:
        conn.close()

def export_table_to_csv(table):
    """
    Exporte une table de la base en CSV.
    """
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    try:
        cur.execute(f"SELECT * FROM {table}")
        rows = cur.fetchall()
        columns = [desc[0] for desc in cur.description]
        out_file = f"{EXPORT_DIR}/{table}_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}.csv"
        with open(out_file, "w", encoding="utf-8", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(columns)
            writer.writerows(rows)
        log(f"Export CSV réussi pour la table {table} : {out_file}")
    except Exception as e:
        log(f"Erreur export CSV table {table} : {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    # Exemple : exporter les tables principales
    export_table_to_json("users")
    export_table_to_csv("users")
    export_table_to_json("projects")
    export_table_to_csv("projects")
    log("Export terminé.")