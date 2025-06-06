# __init__.py

"""
Initialisation du package guides pour le métier Industrie.
Permet l’import Python et la découverte automatique des guides disponibles.
"""

import os

def lister_guides():
    """Retourne la liste des guides Markdown disponibles dans ce dossier."""
    return [f for f in os.listdir(os.path.dirname(__file__)) if f.endswith('.md')]
