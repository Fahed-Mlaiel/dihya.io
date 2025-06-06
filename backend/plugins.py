"""
plugins.py – Système de plugins ultra avancé Dihya
- Chargement dynamique, sécurité, audit, RGPD, multitenancy
- Extension via API/CLI, logs structurés, conformité RGPD
"""
from backend.flask.app.plugins.plugin_manager import get_plugin as plugin_manager
import logging

def load_plugin(name: str):
    """Charge dynamiquement un plugin sécurisé, audité, RGPD-ready."""
    logging.info(f"[plugin] Chargement plugin: {name}")
    return plugin_manager(name)
