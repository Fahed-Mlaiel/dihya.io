"""
Initialisation du package devops pour tests_centralises.
Expose les sous-modules devops pour import explicite.

Exemple d’import :
    from .alerting import *
    from .backup import *
    from .ci_cd import *
    from .cloud import *
    from .compliance import *
    from .infrastructure import *
    from .logs import *
    from .monitoring import *
"""
from .alerting import *
from .backup import *
from .ci_cd import *
from .cloud import *
from .compliance import *
from .infrastructure import *
from .logs import *
from .monitoring import *

__all__ = [name for name in dir() if not name.startswith('_')]
