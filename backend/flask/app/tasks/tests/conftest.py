"""
Fichier de configuration des tests (conftest) pour le module Tasks – Dihya Coding.

Ce fichier centralise les fixtures, hooks et configurations Pytest
pour les tests unitaires et d’intégration des tâches asynchrones (emails, notifications, génération, nettoyage, etc.).

Bonnes pratiques :
- Définir ici les fixtures réutilisables (mocks, contextes, données de test)
- Ne jamais inclure de secrets ou données sensibles
- Documenter chaque fixture ou hook ajouté
- Prévoir l’extensibilité pour de nouveaux scénarios de test
"""

import pytest

@pytest.fixture
def fake_email_task():
    """
    Fixture fournissant une tâche d’envoi d’email factice pour les tests.
    """
    return {
        "task_id": "send_welcome_email",
        "recipient": "test@example.com",
        "subject": "Bienvenue sur Dihya Coding",
        "body": "Votre inscription a bien été prise en compte.",
        "status": "pending"
    }

@pytest.fixture
def fake_cleanup_task():
    """
    Fixture fournissant une tâche de nettoyage factice pour les tests.
    """
    return {
        "task_id": "cleanup_temp_files",
        "files_deleted": 12,
        "status": "completed"
    }

@pytest.fixture
def tasks_test_context():
    """
    Fixture simulant un contexte d’exécution de tâches (file d’attente, logs, etc.).
    """
    return {
        "queue_length": 3,
        "last_task_id": "cleanup_temp_files",
        "logs": []
    }

# Exemple d’utilisation :
# def test_email_task_status(fake_email_task):
#     assert fake_email_task["status"] == "pending"