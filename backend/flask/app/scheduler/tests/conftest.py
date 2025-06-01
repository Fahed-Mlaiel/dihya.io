"""
Fichier de configuration des tests (conftest) pour le module Scheduler – Dihya Coding.

Ce fichier centralise les fixtures, hooks et configurations Pytest
pour les tests unitaires et d’intégration du planificateur de tâches (scheduler).

Bonnes pratiques :
- Définir ici les fixtures réutilisables (mocks, contextes, données de test)
- Ne jamais inclure de secrets ou données sensibles
- Documenter chaque fixture ou hook ajouté
- Prévoir l’extensibilité pour de nouveaux scénarios de test
"""

import pytest

@pytest.fixture
def fake_scheduled_task():
    """
    Fixture fournissant une tâche planifiée factice pour les tests.
    """
    return {
        "task_id": "cleanup_temp_files",
        "schedule": "0 3 * * *",
        "enabled": True,
        "last_run": "2025-05-15T03:00:00Z"
    }

@pytest.fixture
def scheduler_context():
    """
    Fixture simulant un contexte d’exécution du scheduler (état, logs, etc.).
    """
    return {
        "active_tasks": ["cleanup_temp_files", "send_daily_report"],
        "logs": [],
        "timezone": "UTC"
    }

# Exemple d’utilisation :
# def test_scheduler_task(fake_scheduled_task):
#     assert fake_scheduled_task["enabled"] is True