"""
__init__.py - Initialisation minimale du package plugins pour Threed
Toute logique métier doit être dans les sous-dossiers (core, helpers, fallback, etc.)
"""

__all__ = []
# Hooks, audit, sécurité, CI/CD, extension (voir sous-modules)

from .core import AdvancedPlugin
