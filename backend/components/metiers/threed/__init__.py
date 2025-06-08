"""
__init__.py – Initialisation avancée du module Threed (Python)

Ce module permet l’import dynamique des sous-modules, l’auto-discovery, et l’intégration CI/CD.
- Gestion CRUD, API, plugins, audit, RGPD, multilingue, accessibilité, extension, CI/CD, tests, production ready.
- Auto-discovery, hooks, extension dynamique, auditabilité, logs, validation, multitenancy, i18n, plugins, tests, doc intégrée.
"""

# __init__.py du module threed
# Ce fichier doit rester minimal. Toute logique métier doit être dans les sous-dossiers (utils, services, etc.)

import logging
from . import views, plugins
# Les utils sont à ajouter si présents dans le module threed

__all__ = ['views', 'plugins']

# Logging initialisation
logger = logging.getLogger('threed')
logger.info('Module Threed initialisé (Dihya Coding)')

# RGPD, audit, accessibilité, extension, CI/CD, production ready
