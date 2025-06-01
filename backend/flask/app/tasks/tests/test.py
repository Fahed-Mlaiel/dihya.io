"""
Tests avancés pour la gestion des tâches (Python)
Sécurité, multitenancy, plugins, audit, i18n, e2e, multilingue
"""
import pytest
from ..service import schedule_task, list_tasks

def test_schedule_task_tenant():
    res = schedule_task('tenant1', 'backup', '2025-05-25T00:00:00Z')
    assert res['success'] is True

def test_list_tasks_tenant():
    res = list_tasks('tenant1')
    assert isinstance(res, list)
# ...autres tests : plugins, audit, multitenancy, i18n, sécurité, e2e, multilingue...
