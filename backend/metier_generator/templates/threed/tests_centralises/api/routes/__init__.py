"""
Initialisation du package routes pour l’API threed.
Expose les routes Python réelles, centralise l’import/export métier.

Exemple d’import :
    from .test_routes import *
"""
from .test_routes import *

__all__ = [name for name in dir() if not name.startswith('_')]
