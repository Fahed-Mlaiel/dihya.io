"""
Dihya – Initialisation du package guides Blockchain
--------------------------------------------------
Ce package regroupe les guides avancés pour la blockchain.

Fonction utilitaire : lister tous les guides markdown disponibles.
"""

import os

def list_guides():
    """Retourne la liste des fichiers guides markdown du dossier."""
    base = os.path.dirname(__file__)
    return [f for f in os.listdir(base) if f.endswith('.md')]

__all__ = ['list_guides']
