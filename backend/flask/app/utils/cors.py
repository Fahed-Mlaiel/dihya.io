"""
Gestion avancée du CORS pour Dihya Coding.

Ce module centralise la configuration et la validation des origines autorisées pour les requêtes cross-origin (CORS).
Il permet de sécuriser l’API contre les accès non autorisés tout en facilitant le développement multi-frontend.

Bonnes pratiques :
- Restreindre les origines autorisées en production.
- Permettre les méthodes et headers nécessaires uniquement.
- Logger les tentatives d’accès CORS refusées pour audit.
- Ne jamais autoriser les credentials sauf nécessité absolue.
- Documenter la configuration pour chaque environnement.

Exemple d’utilisation :
    from backend.flask.app.utils.cors import configure_cors
    configure_cors(app)
"""

from flask_cors import CORS

ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "https://app.dihya.dev",
    # Ajouter ici les domaines frontends autorisés
]

def configure_cors(app):
    """
    Configure CORS pour l’application Flask.
    :param app: instance Flask
    """
    CORS(
        app,
        origins=ALLOWED_ORIGINS,
        supports_credentials=False,
        methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        allow_headers=["Authorization", "Content-Type", "X-Requested-With"],
        expose_headers=["Content-Disposition"],
        max_age=3600
    )