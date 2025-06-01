"""
Dihya – Module Science
----------------------
Ce package fournit les templates et outils pour la gestion des activités scientifiques (expériences, projets, laboratoires, publications, etc.) sur la plateforme Dihya.

- Multilingue (fr, en, ar, amazigh)
- Sécurité avancée (permissions, audit, conformité RGPD)
- Extensible, compatible multi-stack (Django, React, Node, Flutter…)
- Prêt pour CI/CD, testé, souveraineté numérique garantie

À importer dans vos vues, tests, ou scripts science.
"""

__version__ = "1.0.0"
__author__ = "DihyaOrg"
__all__ = []

# Chargement dynamique des sous-modules science si besoin
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
    logger = logging.getLogger("dihya.science")
    logger.warning(f"Chargement dynamique science partiel : {e}")

# Prêt à l'emploi, conforme, sécurisé, multilingue, extensible.
