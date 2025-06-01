"""
Fichier de configuration des tests (conftest) pour le module Metrics – Dihya Coding.

Ce fichier centralise les fixtures, hooks et configurations Pytest
pour les tests unitaires et d’intégration des métriques de performance, sécurité et usage.

Bonnes pratiques :
- Définir ici les fixtures réutilisables (mocks, contextes, données de test)
- Ne jamais inclure de secrets ou données sensibles
- Documenter chaque fixture ou hook ajouté
- Prévoir l’extensibilité pour de nouveaux scénarios de test
"""

import pytest

@pytest.fixture
def fake_metrics_data():
    """
    Fixture fournissant des métriques factices pour les tests.
    """
    return {
        "dihya_backend_up": 1,
        "dihya_backend_requests_total": 42,
        "dihya_backend_memory_usage_bytes": 12345678,
        "dihya_backend_cpu_usage_percent": 2.5,
        "timestamp": "2025-05-15T12:00:00Z"
    }

@pytest.fixture
def metrics_test_context():
    """
    Fixture simulant un contexte de requête pour les endpoints de métriques.
    """
    return {
        "remote_addr": "127.0.0.1",
        "headers": {"Authorization": "Bearer testtoken"}
    }

# Exemple d’utilisation :
# def test_metrics_format(fake_metrics_data):
#     assert fake_metrics_data["dihya_backend_up"] == 1