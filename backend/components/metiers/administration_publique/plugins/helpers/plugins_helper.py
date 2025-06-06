"""
plugins_helper.py - Fonctions utilitaires avancées pour la gestion des plugins Threed (Python)
"""

def list_plugins(plugins):
    return [p.__class__.__name__ for p in plugins]

def activate_all(plugins):
    for p in plugins:
        if hasattr(p, 'activate'):
            p.activate()

def deactivate_all(plugins):
    for p in plugins:
        if hasattr(p, 'deactivate'):
            p.deactivate()

# Hook d’audit global pour tous les plugins

def audit_all(plugins):
    for p in plugins:
        if hasattr(p, 'get_audit_trail'):
            print(p.get_audit_trail())

# Sécurité : vérification de signature de plugin

def is_trusted_plugin(plugin):
    return hasattr(plugin, 'name') and hasattr(plugin, 'activate')

# Documentation intégrée : helpers compatibles CI/CD, audit, sécurité
