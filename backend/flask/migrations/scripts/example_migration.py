"""
Exemple de script de migration personnalisée pour Dihya Coding.

Ce script montre comment appliquer une migration manuelle sur la base de données,
en complément des outils ORM classiques (ex : ajout de colonne, migration de données, etc.).

Bonnes pratiques :
- Toujours sauvegarder la base avant toute migration.
- Logger chaque opération avec horodatage.
- Valider le schéma après migration.
- Ne jamais inclure de données sensibles dans les logs.
- Documenter chaque étape de la migration.

Exécution :
    python example_migration.py

"""

import sqlite3
import os
from datetime import datetime

DB_PATH = os.getenv("DIHYA_DB_PATH", "dihya.db")
LOG_FILE = "migrations/scripts/migration.log"

def log(msg):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"{datetime.utcnow().isoformat()} | {msg}\n")

def migrate():
    log("Début de la migration : ajout de la colonne 'last_login' à la table 'users'")
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    try:
        cur.execute("ALTER TABLE users ADD COLUMN last_login TEXT")
        conn.commit()
        log("Migration réussie : colonne 'last_login' ajoutée.")
    except Exception as e:
        log(f"Erreur migration : {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    migrate()