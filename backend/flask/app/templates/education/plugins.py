"""
Gestion des plugins métier Éducation – Dihya Coding
Extensible, sécurisé, auditable, RGPD, multilingue.
"""
from typing import Any, Dict, Callable, List
from flask import current_app

PLUGIN_HOOKS: Dict[str, List[Callable]] = {}

def register_plugin_hook(event: str, func: Callable):
    """Enregistre un hook plugin pour un événement métier."""
    if event not in PLUGIN_HOOKS:
        PLUGIN_HOOKS[event] = []
    PLUGIN_HOOKS[event].append(func)

def run_plugin_hooks(event: str, *args, **kwargs):
    """Exécute tous les hooks plugins pour un événement donné."""
    for func in PLUGIN_HOOKS.get(event, []):
        func(*args, **kwargs)

# Exemple d’extension plugin
# def after_add_course_plugin(data):
#     ...
# register_plugin_hook('after_add_course', after_add_course_plugin)
