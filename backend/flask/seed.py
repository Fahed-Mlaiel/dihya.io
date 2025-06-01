#!/usr/bin/env python3
"""
Script pour initialiser ou remplir la base de données avec des données de test pour Dihya Coding.

Ce script crée des utilisateurs de test, des rôles, et tout autre jeu de données utile au développement.
À utiliser uniquement en environnement de développement !

Usage :
    python seed.py
"""

import os
import sys

# Adapter l'import selon la structure de ton projet
sys.path.append(os.path.join(os.path.dirname(__file__), "app"))

from app import create_app
from backend.flask.app.models.user import User
from app import db

def seed_users():
    """Crée des utilisateurs de test."""
    users = [
        User(username="admin", email="admin@dihya.dev"),
        User(username="alice", email="alice@dihya.dev"),
        User(username="bob", email="bob@dihya.dev"),
    ]
    users[0].set_password("admin123")
    users[1].set_password("alice123")
    users[2].set_password("bob123")
    users[0].role = "admin"
    users[1].role = "user"
    users[2].role = "user"
    for user in users:
        db.session.add(user)
    db.session.commit()
    print("Utilisateurs de test créés.")

def main():
    app = create_app("backend.config.Config")
    with app.app_context():
        db.drop_all()
        db.create_all()
        print("Base de données initialisée.")
        seed_users()
        print("Jeu de données de test inséré.")

if __name__ == "__main__":
    main()

