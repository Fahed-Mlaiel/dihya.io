"""
Fichier de configuration des tests (conftest) pour le module quotas d’AI Fallback – Dihya Coding.

Ce fichier permet de centraliser les fixtures, hooks et configurations Pytest
pour les tests unitaires et d’intégration du module de gestion des quotas IA.

Bonnes pratiques :
- Définir ici les fixtures réutilisables (mocks, contextes, données de test)
- Séparer les données sensibles ou critiques (jamais de secrets réels)
- Documenter chaque fixture ou hook ajouté
- Prévoir l’extensibilité pour de nouveaux scénarios de test
"""

import pytest

@pytest.fixture
def fake_quota_data():
    """
    Fixture fournissant des données de quotas factices pour les tests.
    """
    return {
        "user_id": "test_user",
        "quota_limit": 1000,
        "quota_used": 100,
        "reset_period": "monthly"
    }

# Exemple d’utilisation dans un test :
# def test_quota_limit(fake_quota_data):
#     assert fake_quota_data["quota_limit"] == 1000