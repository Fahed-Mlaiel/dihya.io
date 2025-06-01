"""
Script de gestion des upgrades/downgrades de version pour la base de données Dihya Coding.

Ce module permet d’appliquer ou de revenir à une version précise du schéma de base de données,
en complément des outils ORM classiques, pour garantir la compatibilité et la traçabilité des évolutions.

Bonnes pratiques :
- Toujours effectuer un backup avant toute opération d’upgrade/downgrade.
- Logger chaque opération avec horodatage, version cible et statut.
- Valider le schéma et les données après chaque migration.
- Documenter chaque version et changement appliqué.
- Ne jamais inclure de données sensibles dans les logs.

Exécution :
    python upgrade.py --to <version>
    python upgrade.py --downgrade <version>

"""

import argparse
import sqlite3
from datetime import datetime

DB_PATH = "dihya.db"
LOG_FILE = "migrations/upgrade.log"

VERSIONS = {
    "1.0": [
        # Exemple : "ALTER TABLE users ADD COLUMN last_login TEXT"
    ],
    "1.1": [
        # Exemple : "ALTER TABLE projects ADD COLUMN archived INTEGER DEFAULT 0"
    ],
    # Ajouter ici les versions et leurs requêtes SQL associées
}

def log(msg):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"{datetime.utcnow().isoformat()} | {msg}\n")

def apply_migration(version, direction="upgrade"):
    """
    Applique ou annule les migrations pour une version donnée.
    """
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    try:
        queries = VERSIONS.get(version, [])
        if direction == "downgrade":
            queries = reversed(queries)  # À adapter selon la logique de rollback
        for query in queries:
            cur.execute(query)
        conn.commit()
        log(f"{direction.capitalize()} vers version {version} : SUCCESS")
    except Exception as e:
        log(f"{direction.capitalize()} vers version {version} : FAIL | {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Upgrade/Downgrade DB schema Dihya Coding")
    parser.add_argument("--to", type=str, help="Version cible pour upgrade")
    parser.add_argument("--downgrade", type=str, help="Version cible pour downgrade")
    args = parser.parse_args()

    if args.to:
        apply_migration(args.to, direction="upgrade")
    elif args.downgrade:
        apply_migration(args.downgrade, direction="downgrade")
    else:
        print("Usage : python upgrade.py --to <version> | --downgrade <version>")