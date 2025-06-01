"""
Fichier de configuration des tests (conftest) pour le module Plugins – Dihya Coding.

Ce fichier centralise les fixtures, hooks et configurations Pytest
pour les tests unitaires et d’intégration des plugins (analytics, CMS, custom, etc.).

Bonnes pratiques :
- Définir ici les fixtures réutilisables (mocks, contextes, données de test)
- Ne jamais inclure de secrets ou données sensibles
- Documenter chaque fixture ou hook ajouté
- Prévoir l’extensibilité pour de nouveaux scénarios de test
"""

import pytest

@pytest.fixture
def fake_plugin():
    """
    Fixture fournissant un plugin factice pour les tests.
    """
    return {
        "name": "analytics_plugin",
        "enabled": True,
        "config": {"tracking_id": "UA-XXXXX", "auto_track": True}
    }

@pytest.fixture
def plugin_test_context():
    """
    Fixture simulant un contexte d’exécution de plugin (utilisateur, permissions, etc.).
    """
    return {
        "user_id": "test_user",
        "roles": ["admin", "plugin_manager"],
        "locale": "fr"
    }

# Exemple d’utilisation :
# def test_plugin_enabled(fake_plugin):
#     assert fake_plugin["enabled"] is True