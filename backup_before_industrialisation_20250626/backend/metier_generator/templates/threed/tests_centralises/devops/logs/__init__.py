"""
Initialisation avancée du module de tests logs.
Ce module prépare les tests de logs métier.
"""
from .test_logs import *

__all__ = [name for name in dir() if not name.startswith('_')]
