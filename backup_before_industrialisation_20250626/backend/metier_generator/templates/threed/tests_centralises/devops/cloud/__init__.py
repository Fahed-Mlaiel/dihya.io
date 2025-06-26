"""
Initialisation avancée du module de tests cloud.
Ce module prépare les tests de gestion cloud métier.
"""

from .test_cloud import *

__all__ = [name for name in dir() if not name.startswith('_')]
