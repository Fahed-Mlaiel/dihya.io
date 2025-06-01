"""
Script de seed avancé pour injecter des données de démonstration dans Dihya Coding.

Ce script permet d’ajouter des utilisateurs, projets, contenus multilingues, etc.
pour faciliter les tests, la démo et l’onboarding.

Bonnes pratiques :
- Ne jamais inclure de données sensibles ou de vrais secrets dans les seeds.
- Logger chaque opération de seed avec horodatage.
- Prévoir des seeds multilingues (fr, en, autres dialectes).
- Valider la cohérence des données après injection.
- Utiliser ce script uniquement en environnement de développement ou de test.

Exécution :
    python demo_data.py

"""

import sqlite3
from datetime import datetime

DB_PATH = "dihya.db"

def log(msg):
    with open("seed/seed.log", "a", encoding="utf-8") as f:
        f.write(f"{datetime.utcnow().isoformat()} | {msg}\n")

def seed_users():
    users = [
        ("alice", "alice@dihya.dev", "user", "fr"),
        ("bob", "bob@dihya.dev", "admin", "en"),
        ("karim", "karim@dihya.dev", "user", "ber")
    ]
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    for username, email, role, lang in users:
        try:
            cur.execute(
                "INSERT INTO users (username, email, role, lang) VALUES (?, ?, ?, ?)",
                (username, email, role, lang)
            )
            log(f"Utilisateur seedé : {username} ({role}, {lang})")
        except Exception as e:
            log(f"Erreur seed utilisateur {username} : {e}")
    conn.commit()
    conn.close()

def seed_projects():
    # Exemple de seed de projets multilingues
    projects = [
        ("Projet Amazigh", "Plateforme e-commerce inspirée de la culture amazighe.", "alice"),
        ("Education4All", "App éducative multilingue pour enfants.", "bob"),
    ]
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    for name, desc, owner in projects:
        try:
            cur.execute(
                "INSERT INTO projects (name, description, owner) VALUES (?, ?, ?)",
                (name, desc, owner)
            )
            log(f"Projet seedé : {name} (owner: {owner})")
        except Exception as e:
            log(f"Erreur seed projet {name} : {e}")
    conn.commit()
    conn.close()

if __name__ == "__main__":
    seed_users()
    seed_projects()
    log("Seed de démonstration terminé.")