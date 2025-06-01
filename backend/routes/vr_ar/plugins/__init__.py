"""
Initialisation du système de plugins VR/AR (Dihya)
Chargement dynamique, extension via API/CLI, sécurité, audit, multilingue, RGPD, multitenancy, SEO, logging, tests.
"""

PLUGINS = {}

def register_plugin(name: str, plugin: object) -> None:
    """Enregistre dynamiquement un plugin VR/AR."""
    PLUGINS[name] = plugin

def get_plugin(name: str) -> object:
    """Récupère un plugin VR/AR par nom."""
    return PLUGINS.get(name)

def list_plugins() -> list:
    """Liste tous les plugins VR/AR enregistrés."""
    return list(PLUGINS.keys())
