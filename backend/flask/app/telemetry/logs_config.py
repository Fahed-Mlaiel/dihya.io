"""
Configuration centralisée des logs – Dihya Coding

Ce module fournit une configuration standardisée pour le logging de toute la plateforme backend.
Il permet d’assurer la cohérence, la traçabilité et la sécurité des logs, tout en évitant la duplication de configuration.

Bonnes pratiques :
- Utiliser ce module pour configurer tous les loggers applicatifs
- Ne jamais logger de données sensibles (mots de passe, tokens…)
- Prévoir différents niveaux de logs (INFO, WARNING, ERROR)
- Permettre l’export vers fichiers, stdout, ou systèmes externes (ELK, Loki…)
"""

import logging
import sys

def setup_logging(
    level=logging.INFO,
    log_to_file: bool = True,
    filename: str = "dihya_backend.log"
):
    """
    Configure le logging global de l’application Dihya Coding.

    Args:
        level (int): Niveau de log (logging.INFO, logging.ERROR…)
        log_to_file (bool): Active le log vers fichier.
        filename (str): Nom du fichier de log (si log_to_file).
    """
    handlers = [logging.StreamHandler(sys.stdout)]
    if log_to_file:
        handlers.append(logging.FileHandler(filename))

    logging.basicConfig(
        level=level,
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
        handlers=handlers
    )

def get_logger(name: str) -> logging.Logger:
    """
    Fournit un logger configuré pour l’application Dihya Coding.

    Args:
        name (str): Nom du logger.

    Returns:
        logging.Logger: Logger prêt à l’emploi.
    """
    return logging.getLogger(name)