"""
Fichier de configuration des tests (conftest) pour le module GraphQL – Dihya Coding.

Ce fichier centralise les fixtures, hooks et configurations Pytest
pour les tests unitaires et d’intégration des schémas, résolveurs et endpoints GraphQL.

Bonnes pratiques :
- Définir ici les fixtures réutilisables (mocks, contextes, données de test)
- Ne jamais inclure de secrets ou credentials réels
- Documenter chaque fixture ou hook ajouté
- Prévoir l’extensibilité pour de nouveaux scénarios de test
"""

import pytest

@pytest.fixture
def fake_graphql_query():
    """
    Fixture fournissant une requête GraphQL factice pour les tests.
    """
    return """
    query {
        user(id: "test_user") {
            id
            name
            email
        }
    }
    """

@pytest.fixture
def fake_graphql_context():
    """
    Fixture simulant un contexte d’exécution GraphQL (utilisateur, permissions, etc.).
    """
    return {
        "user_id": "test_user",
        "roles": ["admin"],
        "locale": "fr"
    }

# Exemple d’utilisation :
# def test_graphql_query(fake_graphql_query):
#     assert "user" in fake_graphql_query