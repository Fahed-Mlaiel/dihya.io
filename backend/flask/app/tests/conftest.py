"""
Fixtures et configuration globale pour les tests Dihya Coding (backend Flask).

Ce fichier permet de définir des fixtures réutilisables pour pytest,
comme l'initialisation de l'application, la base de données en mémoire,
et la création d'un client de test sécurisé.

Bonnes pratiques :
- Utiliser des bases de données temporaires pour les tests.
- Nettoyer les données entre chaque test.
- Générer des tokens JWT valides pour les tests d'authentification.
"""

import pytest
from backend.flask.app import create_app

@pytest.fixture
def app():
    """Fixture pour créer une instance de l'application Flask en mode test."""
    app = create_app("backend.config.Config")
    app.config.update({
        "TESTING": True,
        "DEBUG": False,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
        "WTF_CSRF_ENABLED": False,
    })
    yield app

@pytest.fixture
def client(app):
    """Fixture pour obtenir un client de test Flask."""
    return app.test_client()

@pytest.fixture
def runner(app):
    """Fixture pour obtenir un runner de commandes Flask."""
    return app.test_cli_runner()
