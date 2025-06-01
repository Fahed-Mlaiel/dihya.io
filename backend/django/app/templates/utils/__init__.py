"""
Dihya – Utils
-------------
Ce package fournit des utilitaires avancés, multilingues, sécurisés et souverains pour tous les modules Dihya.

- Fonctions d’aide génériques (formatage, sécurité, i18n, accessibilité, audit, fallback IA open source…)
- Multilingue (fr, en, ar, amazigh)
- Sécurité avancée (sanitization, logging, conformité RGPD)
- Compatible multi-stack (Django, React, Node, Flutter…)
- Prêt CI/CD, testé, zéro warning, souveraineté numérique garantie

À importer dans vos modules, templates, scripts, tests, middlewares, plugins, etc.
"""

__version__ = "1.0.0"
__author__ = "DihyaOrg"
__all__ = []

# Chargement dynamique des sous-modules utils si besoin
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
    logger = logging.getLogger("dihya.utils")
    logger.warning(f"Chargement dynamique utils partiel : {e}")

# Prêt à l'emploi, conforme, sécurisé, multilingue, extensible.
