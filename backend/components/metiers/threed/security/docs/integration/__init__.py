# __init__.py – integration
# Point d'entrée centralisé pour l'intégration Python
# Importez les sous-modules pour chaque techno si besoin
# Exemple : from .nodejs import *
# Exemple : from .python import *
# Exemple : from .samples import *

from . import nodejs
from . import python

__all__ = ['nodejs', 'python']
