"""
Initialisation du package api pour tests_centralises.
Expose les sous-modules api pour import explicite.

Exemple d’import :
    from .controllers import *
    from .docs import *
    from .middlewares import *
    from .pagination import *
    from .routes import *
    from .versioning import *
"""
from .controllers import *
from .docs import *
from .middlewares import *
from .pagination import *
from .routes import *
# versioning peut être optionnel si non présent
try:
    from .versioning import *
except ImportError:
    pass

__all__ = [name for name in dir() if not name.startswith('_')]
