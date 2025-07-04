"""
Initialisation ultra avancée du module Education (Dihya Coding).
- Gestion CRUD, API, plugins, audit, RGPD, multilingue, accessibilité, extension, CI/CD, tests, production ready.
- Auto-discovery, hooks, extension dynamique, auditabilité, logs, validation, multitenancy, i18n, plugins, tests, doc intégrée.
"""

import logging
from . import schemas, views, plugins
from .utils import audit, i18n, pluginManager, rbac, validators, ai_fallback, exporter, metrics, logger

__all__ = ['schemas', 'views', 'plugins', 'audit', 'i18n', 'pluginManager', 'rbac', 'validators', 'ai_fallback', 'exporter', 'metrics', 'logger']

# Logging initialisation
logger = logging.getLogger('education')
logger.info('Module Education initialisé (Dihya Coding)')

# RGPD, audit, accessibilité, extension, CI/CD, production ready
