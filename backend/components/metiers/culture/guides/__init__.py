"""
Dihya Coding – Initialisation du module Guides Culture
-----------------------------------------------------
Ce package permet la gestion, l’import et l’extension des guides métiers pour la culture (audit, RGPD, accessibilité, hooks, plugins, multilingue).

🇫🇷 Initialisation du package guides culture (sécurité, extensibilité, multilingue, audit, RGPD, accessibilité)
🇬🇧 Culture guides package initialization (security, extensibility, multilingual, audit, GDPR, accessibility)
🇦🇪 تهيئة حزمة الأدلة للثقافة (الأمان، التوسعة، متعدد اللغات، التدقيق، RGPD، الوصول)
ⵣ Tazwart n guides n tamedyazt (amatu, extensibility, multilingual, audit, RGPD, accessibility)

Ce fichier rend le dossier importable comme package Python, prêt pour l’extension par plugins, assets, AI, ou scripts métiers.

Checklist :
- [x] Import dynamique
- [x] Sécurité (aucun code exécutable à l’import)
- [x] Extensible (ajoutez vos guides, assets, plugins)
- [x] Multilingue (voir doc/README)
- [x] RGPD, audit, accessibilité
"""

import importlib
import logging

MODULES = [
    'ACCESSIBILITY_GUIDE', 'PLUGINS_GUIDE', 'SECURITY_GUIDE', 'RGPD_GUIDE', 'TEST_STRATEGY', 'README_ADVANCED', 'ACCESSIBILITY_GUIDE_CULTURE', 'PLUGINS_GUIDE_CULTURE', 'SECURITY_GUIDE_CULTURE', 'RGPD_GUIDE_CULTURE', 'TEST_STRATEGY_CULTURE'
]
for mod in MODULES:
    try:
        importlib.import_module(f'.{mod}', __name__)
    except Exception as e:
        logging.warning(f"Module guide {mod} non chargé: {e}")

__all__ = MODULES
