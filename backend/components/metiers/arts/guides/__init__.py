"""
Initialisation du package guides Arts.
Permet l'accès programmatique à tous les guides du dossier.
"""
import os

__all__ = [f for f in os.listdir(os.path.dirname(__file__)) if f.endswith('.md')]

def list_guides():
    """Retourne la liste des guides Arts disponibles."""
    return __all__
