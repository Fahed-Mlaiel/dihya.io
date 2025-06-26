"""
Initialisation du package pagination pour l’API threed.
Expose les tests de pagination Python réels, centralise l’import/export métier.

Exemple d’import :
    from .test_pagination import *
"""
from .test_pagination import *

__all__ = [name for name in dir() if not name.startswith('_')]
