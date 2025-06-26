"""
Initialisation des blueprints DevOps (Python)
Exporte tous les générateurs de pipelines, scripts et monitoring métiers
"""
import importlib
import os

from .pipelines import *
from .scripts import *
from .monitoring import *

def run_full_devops_pipeline(repo=None, env=None, notifications=None):
    """
    Exécution complète du pipeline DevOps (exemple minimal, à adapter selon la logique métier)
    """
    print(f"Pipeline lancé pour le repo {repo} en environnement {env}.")
    if notifications and hasattr(notifications, 'send'):
        notifications.send(f"Pipeline terminé pour {repo}.")
    return True

__all__ = ['run_full_devops_pipeline']
