"""
Tests unitaires et d’intégration pour le module Scheduler – Dihya Coding.

Ce fichier vérifie la planification, l’exécution et la gestion des tâches programmées,
en simulant différents scénarios métier et de sécurité.

Bonnes pratiques :
- Utiliser des fixtures pour les tâches et contextes (voir conftest.py)
- Tester les cas de succès, d’échec, de désactivation et de logs
- Ne jamais utiliser de données réelles ou sensibles
- Documenter chaque scénario de test
"""

import pytest
from backend.flask.app.scheduler.scheduler import schedule_task, run_scheduled_tasks, disable_task

def test_schedule_task_success(fake_scheduled_task, scheduler_context):
    """
    Teste l’ajout d’une tâche planifiée valide.
    """
    result = schedule_task(fake_scheduled_task, scheduler_context)
    assert result["status"] == "scheduled"
    assert fake_scheduled_task["task_id"] in scheduler_context["active_tasks"]

def test_run_scheduled_tasks(fake_scheduled_task, scheduler_context):
    """
    Teste l’exécution des tâches planifiées.
    """
    scheduler_context["active_tasks"].append(fake_scheduled_task["task_id"])
    logs_before = len(scheduler_context["logs"])
    result = run_scheduled_tasks(scheduler_context)
    assert result["status"] == "executed"
    assert len(scheduler_context["logs"]) > logs_before

def test_disable_task(fake_scheduled_task, scheduler_context):
    """
    Teste la désactivation d’une tâche planifiée.
    """
    scheduler_context["active_tasks"].append(fake_scheduled_task["task_id"])
    result = disable_task(fake_scheduled_task["task_id"], scheduler_context)
    assert result["status"] == "disabled"
    assert fake_scheduled_task["task_id"] not in scheduler_context["active_tasks"]

def test_schedule_task_invalid_data(scheduler_context):
    """
    Teste l’ajout d’une tâche planifiée avec des données invalides.
    """
    invalid_task = {"task_id": "", "schedule": "", "enabled": True}
    result = schedule_task(invalid_task, scheduler_context)
    assert result["status"] == "error"
    assert "reason" in result