"""
Dihya – Module Social
---------------------
Ce package fournit les templates et outils pour la gestion des interactions sociales (réseaux, communautés, posts, commentaires, notifications, etc.) sur la plateforme Dihya.

- Multilingue (fr, en, ar, amazigh)
- Sécurité avancée (permissions, audit, conformité RGPD/social)
- Extensible, compatible multi-stack (Django, React, Node, Flutter…)
- Prêt pour CI/CD, testé, souveraineté numérique garantie
- Gestion des rôles, modération, accessibilité, notifications, intégration réseaux sociaux souverains

À importer dans vos vues, middlewares, tests, ou scripts sociaux.
"""

__version__ = "1.0.0"
__author__ = "DihyaOrg"
__all__ = []

# Chargement dynamique des sous-modules social si besoin
try:
    import importlib
    import os

    current_dir = os.path.dirname(__file__)
    for filename in os.listdir(current_dir):
        if filename.endswith(".py") and filename not in ("__init__.py",):
            module_name = filename[:-3]
            module = importlib.import_module(f".{module_name}", package=__name__)
            __all__.append(module_name)
except Exception as e:
    # Logging sécurisé, pas de fuite d'information sensible
    import logging
    logger = logging.getLogger("dihya.social")
    logger.warning(f"Chargement dynamique social partiel : {e}")

# Prêt à l'emploi, conforme, sécurisé, multilingue, extensible.
