"""
Point d’entrée Python pour tous les modules de samples sécurité (clé en main)

Ce module agit comme un point d’entrée modulaire, important dynamiquement tous les
modules nécessaires pour les samples de sécurité. Il permet une intégration facile et
rapide des différents composants du système de sécurité.

Voir index.js pour l’entrée unique JS.
"""

from .access import *
from .audit import *
from .rgpd import *
from .monitoring import *
from .compliance import *
from .onboarding import *
from .rbac import *
