"""
Initialisation du middleware pour Dihya Coding.

Ce module permet d'importer et d'enregistrer facilement tous les middlewares (CORS, rate limiting, etc.)
dans l'application Flask principale, selon les bonnes pratiques Dihya Coding.

Bonnes pratiques :
- Centraliser l'activation des middlewares pour clarté et maintenabilité
- Ne jamais activer un middleware critique (CORS, rate limiting) sans configuration stricte
- Prévoir l'extensibilité (ajout facile de nouveaux middlewares)
"""

from .cors import cors_middleware
from .rate_limit import rate_limited

def register_middlewares(app):
    """
    Enregistre tous les middlewares nécessaires sur l'app Flask.
    À appeler dans create_app().
    """
    cors_middleware(app)
    # Ajouter ici d'autres middlewares si besoin (rate limiting, audit, etc.)
    # Exemple : app.before_request(rate_limited)