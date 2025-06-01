"""
Fichier de configuration des tests (conftest) pour le module Schemas – Dihya Coding.

Ce fichier centralise les fixtures, hooks et configurations Pytest
pour les tests unitaires et d’intégration des schémas de validation (utilisateur, projet, plugin, etc.).

Bonnes pratiques :
- Définir ici les fixtures réutilisables (mocks, contextes, données de test)
- Ne jamais inclure de secrets ou données sensibles
- Documenter chaque fixture ou hook ajouté
- Prévoir l’extensibilité pour de nouveaux scénarios de test
"""

import pytest

@pytest.fixture
def fake_user_schema():
    """
    Fixture fournissant un schéma utilisateur factice pour les tests.
    """
    return {
        "id": "test_user",
        "email": "test@example.com",
        "roles": ["user"],
        "active": True
    }

@pytest.fixture
def fake_project_schema():
    """
    Fixture fournissant un schéma de projet factice pour les tests.
    """
    return {
        "project_id": "proj_123",
        "name": "Projet Test",
        "owner_id": "test_user",
        "features": ["auth", "notifications"]
    }

@pytest.fixture
def schema_test_context():
    """
    Fixture simulant un contexte de validation de schéma (langue, options, etc.).
    """
    return {
        "locale": "fr",
        "strict": True
    }

# Exemple d’utilisation :
# def test_user_schema_fields(fake_user_schema):
#     assert "email" in fake_user_schema