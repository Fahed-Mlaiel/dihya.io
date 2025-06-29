# plugins/__init__.py
import importlib
import pkgutil
from typing import Dict, Type

from .base import AnalyticsPluginBase

# Dictionnaire pour enregistrer les plugins disponibles
PLUGINS: Dict[str, Type[AnalyticsPluginBase]] = {}


def register_plugin(plugin_class: Type[AnalyticsPluginBase]):
    """Enregistre un plugin dans le système."""
    PLUGINS[plugin_class.name] = plugin_class


def get_plugin(name: str) -> Type[AnalyticsPluginBase]:
    """Récupère une classe de plugin par son nom."""
    return PLUGINS.get(name)


def load_plugins():
    """Charge tous les modules de plugins dans le package plugins."""
    package = __name__
    prefix = package + "."

    for _, modname, _ in pkgutil.iter_modules(__path__, prefix):
        importlib.import_module(modname)


# Initialisation automatique des plugins lors de l'importation du package
load_plugins()