"""
Initialisation du package docs pour l’API threed.
Expose la documentation API, centralise l’import/export métier.

Exemple d’import :
    from .test_api_docs import *
"""
from .test_api_docs import *

__all__ = [name for name in dir() if not name.startswith('_')]
