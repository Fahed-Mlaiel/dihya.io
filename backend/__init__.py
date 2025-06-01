"""
Initialisation du package Dihya Backend
Ultra avancé : sécurité, i18n, audit, RGPD, plugins, multitenancy, SEO, logging, monitoring, tests, CI-ready.
"""

from .i18n import *
from .security import *
from .audit import *
from .plugins import *
from .seo import *
from .utils import *

__version__ = '2025.05.30'
__all__ = [
    'i18n', 'security', 'audit', 'plugins', 'seo', 'utils'
]
