"""
Initialisation du package controllers pour l’API threed.
Expose les contrôleurs Python réels, centralise l’import et l’export métier.

Exemple d’import :
    from .test_controllers import *
"""
from .test_controllers import *

__all__ = [name for name in dir() if not name.startswith('_')]
