"""
Dihya – Module SEO
------------------
Ce package fournit les templates et outils pour l’optimisation SEO (Search Engine Optimization) sur la plateforme Dihya.

- Multilingue (fr, en, ar, amazigh)
- Sécurité avancée (aucune fuite de données, conformité RGPD)
- Extensible, compatible multi-stack (Django, React, Node, Flutter…)
- Prêt pour CI/CD, testé, souveraineté numérique garantie
- Optimisation SEO technique et sémantique, balisage, accessibilité, microdata, Open Graph, robots.txt, sitemap.xml

À importer dans vos vues, middlewares, ou scripts SEO.
"""

__version__ = "1.0.0"
__author__ = "DihyaOrg"
__all__ = []

# Chargement dynamique des sous-modules SEO si besoin
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
    logger = logging.getLogger("dihya.seo")
    logger.warning(f"Chargement dynamique SEO partiel : {e}")

# Prêt à l'emploi, conforme, sécurisé, multilingue, extensible.
