"""
Dihya – Validators
------------------
Ce package fournit des validateurs avancés, multilingues, sécurisés et souverains pour tous les modules Dihya.

- Validation de données (emails, mots de passe, formats, accès, RGPD…)
- Multilingue (fr, en, ar, amazigh)
- Sécurité avancée (anti-injection, conformité RGPD, audit)
- Compatible multi-stack (Django, React, Node, Flutter…)
- Prêt CI/CD, testé, zéro warning, souveraineté numérique garantie

À importer dans vos modèles, formulaires, APIs, scripts, middlewares, tests, etc.
"""

__version__ = "1.0.0"
__author__ = "DihyaOrg"
__all__ = []

# Chargement dynamique des sous-modules validators si besoin
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
    logger = logging.getLogger("dihya.validators")
    logger.warning(f"Chargement dynamique validators partiel : {e}")

# Prêt à l'emploi, conforme, sécurisé, multilingue, extensible.
