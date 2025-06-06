"""
Initialisation ultra avancée des utilitaires pour Environnement.
Inclut : audit, i18n, gestion des plugins, RBAC, validateurs, vues, fallback IA, etc.
Permet l'import dynamique, l'orchestration automatique et l'extension CI/CD des utilitaires métier.
"""

from .audit import *
from .exporter import *
from .i18n import *
from .logger import *
from .metrics import *
from .pluginManager import *
from .rbac import *
from .sample_plugin import *
from .validators import *
from .views import *
from .ai_fallback import *

# Orchestration automatique des sous-modules utils
import importlib, pkgutil
__all__ = []
for loader, module_name, is_pkg in pkgutil.walk_packages(__path__):
    module = importlib.import_module(f"{__name__}.{module_name}")
    __all__.append(module_name)
