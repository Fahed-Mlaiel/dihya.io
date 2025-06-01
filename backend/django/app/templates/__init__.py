"""
Dihya – Templates App
---------------------
Ce package racine regroupe tous les templates ultra avancés de la plateforme Dihya :
- Validators, Voice, Voyage, VR/AR, et extensions métiers.
- Multilingue (fr, en, ar, amazigh)
- Sécurité avancée, modularité, extensibilité, souveraineté numérique
- Prêt CI/CD, testé, compatible multi-stack (Django, React, Node, Flutter…)

À importer dans vos apps Django, middlewares, tests, scripts, plugins, ou extensions.
"""

__version__ = "1.0.0"
__author__ = "DihyaOrg"
__all__ = []

# Chargement dynamique des sous-modules principaux (validators, voice, voyage, vr_ar)
try:
    import importlib
    import os

    current_dir = os.path.dirname(__file__)
    for dirname in os.listdir(current_dir):
        dirpath = os.path.join(current_dir, dirname)
        if os.path.isdir(dirpath) and not dirname.startswith("__"):
            try:
                module = importlib.import_module(f".{dirname}", package=__name__)
                __all__.append(dirname)
            except Exception as e:
                import logging
                logger = logging.getLogger("dihya.templates")
                logger.warning(f"Chargement dynamique du sous-module {dirname} partiel : {e}")
except Exception as e:
    import logging
    logger = logging.getLogger("dihya.templates")
    logger.warning(f"Chargement dynamique templates partiel : {e}")

# Prêt à l'emploi, sécurisé, multilingue, extensible, souverain.
