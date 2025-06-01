"""
Dihya – Module VR/AR
--------------------
Ce package fournit les templates et outils pour la gestion avancée de la réalité virtuelle (VR) et augmentée (AR) sur la plateforme Dihya.

- Multilingue (fr, en, ar, amazigh)
- Sécurité avancée (permissions, chiffrement, audit, conformité RGPD/VR-AR)
- Extensible, compatible multi-stack (Django, React, Node, Flutter, Unity…)
- Prêt pour CI/CD, testé, souveraineté numérique garantie
- Gestion des rôles (admin, créateur, utilisateur, invité, auditeur), accessibilité, notifications, intégration plateformes souveraines
- Prise en charge des assets 3D, scènes immersives, interactions vocales et gestuelles, fallback IA open source

À importer dans vos vues, middlewares, tests, scripts ou plugins VR/AR.
"""

__version__ = "1.0.0"
__author__ = "DihyaOrg"
__all__ = []

# Chargement dynamique des sous-modules VR/AR si besoin
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
    logger = logging.getLogger("dihya.vr_ar")
    logger.warning(f"Chargement dynamique vr_ar partiel : {e}")

# Prêt à l'emploi, conforme, sécurisé, multilingue, extensible.
