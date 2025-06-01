"""
Fichier de configuration des tests (conftest) pour le module AI Fallback – Dihya Coding.

Ce fichier centralise les fixtures, hooks et configurations Pytest
pour les tests unitaires et d’intégration du fallback IA (modèles open source, gestion des quotas, etc.).

Bonnes pratiques :
- Définir ici les fixtures réutilisables (mocks, contextes, données de test)
- Ne jamais inclure de secrets ou credentials réels
- Documenter chaque fixture ou hook ajouté
- Prévoir l’extensibilité pour de nouveaux scénarios de test
"""

import pytest

@pytest.fixture
def fake_fallback_response():
    """
    Fixture fournissant une réponse factice d’un fallback IA pour les tests.
    """
    return {
        "model": "mixtral",
        "output": "Ceci est une réponse simulée.",
        "confidence": 0.95,
        "usage": {"prompt_tokens": 10, "completion_tokens": 20}
    }

@pytest.fixture
def fallback_context():
    """
    Fixture simulant un contexte d’appel fallback IA (user, quotas, etc.).
    """
    return {
        "user_id": "test_user",
        "quota_remaining": 900,
        "language": "fr",
        "dialect": "kabyle"
    }

# Exemple d’utilisation :
# def test_fallback_output(fake_fallback_response):
#     assert "output" in fake_fallback_response