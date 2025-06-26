"""
Initialisation avancée du module de tests infrastructure.
Ce module prépare les tests d'infrastructure métier.
"""
from .test_infrastructure import *

__all__ = [name for name in dir() if not name.startswith('_')]
