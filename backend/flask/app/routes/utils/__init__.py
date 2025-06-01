"""
Module utilitaire transverse Dihya (Flask).
Inclut : services, schémas, plugins, validation, audit, i18n, tests, documentation.
Ultra avancé, extensible, sécurisé, RGPD, production-ready.
"""

from .services import *
from .schemas import *
from .plugins import *
from .validators import *
from .audit import *
from .i18n import *

__all__ = [
    "services", "schemas", "plugins", "validators", "audit", "i18n"
]
