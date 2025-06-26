"""
Initialisation avancée du module de tests backup.
Ce module prépare les tests de sauvegarde et restauration métier.
"""
from .test_backup import *

__all__ = [name for name in dir() if not name.startswith('_')]
