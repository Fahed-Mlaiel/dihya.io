#!/usr/bin/env python3
"""
Script de gestion centralisé pour le backend Flask Dihya Coding.

Permet de lancer le serveur, gérer les migrations, lancer les tests, initialiser la base,
et d'autres tâches courantes de développement et de maintenance.

Usage :
    python manage.py run         # Lancer le serveur Flask
    python manage.py migrate     # Générer une migration Alembic
    python manage.py upgrade     # Appliquer les migrations
    python manage.py downgrade   # Annuler la dernière migration
    python manage.py test        # Lancer les tests unitaires
    python manage.py seed        # Remplir la base avec des données de test (si seed.py existe)
    python manage.py shell       # Ouvrir un shell Python avec le contexte Flask
"""

import os
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python manage.py [run|migrate|upgrade|downgrade|test|seed|shell]")
        sys.exit(1)
    cmd = sys.argv[1]
    if cmd == "run":
        os.system("flask run")
    elif cmd == "migrate":
        os.system("flask db migrate")
    elif cmd == "upgrade":
        os.system("flask db upgrade")
    elif cmd == "downgrade":
        os.system("flask db downgrade")
    elif cmd == "test":
        os.system("pytest app/")
    elif cmd == "seed":
        if os.path.exists("seed.py"):
            os.system("python seed.py")
        else:
            print("Le fichier seed.py n'existe pas.")
    elif cmd == "shell":
        os.system("flask shell")
    else:
        print(f"Commande inconnue : {cmd}")

if __name__ == "__main__":
    main()