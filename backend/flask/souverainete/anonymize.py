"""
Script d’anonymisation des données pour la souveraineté numérique Dihya Coding.

Ce module permet d’anonymiser les données personnelles ou sensibles dans la base de données,
afin de respecter la confidentialité, la législation (RGPD) et la souveraineté des utilisateurs.

Bonnes pratiques :
- Toujours effectuer un backup avant toute anonymisation.
- Logger chaque opération avec horodatage.
- Ne jamais anonymiser sans consentement ou hors cadre légal.
- Documenter précisément les champs anonymisés.
- Tester l’intégrité de la base après anonymisation.

Exécution :
    python anonymize.py

"""

import sqlite3
from datetime import datetime

DB_PATH = "dihya.db"
LOG_FILE = "souverainete/anonymize.log"

def log(msg):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"{datetime.utcnow().isoformat()} | {msg}\n")

def anonymize_users():
    """
    Anonymise les données personnelles des utilisateurs (username, email).
    """
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    try:
        cur.execute("UPDATE users SET username = 'anonymous', email = 'anonymous@dihya.dev'")
        conn.commit()
        log("Anonymisation des utilisateurs effectuée.")
    except Exception as e:
        log(f"Erreur anonymisation utilisateurs : {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    anonymize_users()
    log("Anonymisation terminée.")