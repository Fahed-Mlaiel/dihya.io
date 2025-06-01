"""
Dihya – Module Voice
--------------------
Ce package fournit les templates et outils pour la gestion de la voix (reconnaissance, synthèse, transcription, commandes vocales, accessibilité, notifications audio, etc.) sur la plateforme Dihya.

- Multilingue (fr, en, ar, amazigh)
- Sécurité avancée (permissions, chiffrement, audit, conformité RGPD/voix)
- Extensible, compatible multi-stack (Django, React, Node, Flutter…)
- Prêt pour CI/CD, testé, souveraineté numérique garantie
- Gestion des rôles (admin, utilisateur, invité, auditeur), accessibilité, notifications, intégration plateformes vocales souveraines

À importer dans vos vues, middlewares, tests, scripts ou plugins voice.
"""

__version__ = "1.0.0"
__author__ = "DihyaOrg"
__all__ = []

# Chargement dynamique des sous-modules voice si besoin
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
    logger = logging.getLogger("dihya.voice")
    logger.warning(f"Chargement dynamique voice partiel : {e}")

# Prêt à l'emploi, conforme, sécurisé, multilingue, extensible.
