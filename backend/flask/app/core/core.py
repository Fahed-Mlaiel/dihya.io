"""
Module core – Dihya Coding

Ce module centralise les helpers transversaux, classes de base et outils communs à tout le backend.
Il vise à éviter la duplication de code, à garantir la cohérence métier et à faciliter la maintenance.

Bonnes pratiques :
- Toute classe ou fonction réutilisable doit être ici ou dans utils/
- Documenter chaque helper ou base class
- Ne jamais inclure de logique métier spécifique à un module
"""

import logging
from typing import Any, Dict

class DihyaBaseException(Exception):
    """Exception de base pour toutes les erreurs métier Dihya Coding."""
    pass

class ServiceResponse:
    """
    Standardise la structure de réponse des services internes.

    Attributes:
        success (bool): Statut de l’opération.
        data (dict): Données retournées.
        error (str): Message d’erreur éventuel.
    """
    def __init__(self, success: bool, data: Any = None, error: str = ""):
        self.success = success
        self.data = data
        self.error = error

    def to_dict(self) -> Dict[str, Any]:
        """Retourne la réponse sous forme de dictionnaire."""
        return {
            "success": self.success,
            "data": self.data,
            "error": self.error
        }

def get_logger(name: str) -> logging.Logger:
    """
    Fournit un logger configuré pour l’application Dihya Coding.

    Args:
        name (str): Nom du logger.

    Returns:
        logging.Logger: Logger prêt à l’emploi.
    """
    logger = logging.getLogger(name)
    if not logger.hasHandlers():
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(name)s %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    return logger