"""
Point d’entrée Python pour tous les modules de documentation sécurité (clé en main)

Importe dynamiquement tous les modules si besoin.

Voir index.js pour l’entrée unique JS.
"""

from . import guides
from . import integration
from . import policies

__all__ = [
    'guides',
    'integration',
    'policies',
]
