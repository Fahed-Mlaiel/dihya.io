"""
Initialisation avancée du module de tests ci_cd.
Ce module prépare les tests CI/CD métier.
"""
from .test_ci_cd import *

__all__ = [name for name in dir() if not name.startswith('_')]
