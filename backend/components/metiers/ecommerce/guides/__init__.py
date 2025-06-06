"""
Dihya Coding – Initialisation du module Guides eCommerce
-------------------------------------------------------
Ce package permet la gestion, l’import et l’extension des guides métiers pour l’e-commerce (audit, RGPD, accessibilité, hooks, plugins, multilingue).

🇫🇷 Initialisation du package guides eCommerce (sécurité, extensibilité, multilingue, audit, RGPD, accessibilité)
🇬🇧 Ecommerce guides package initialization (security, extensibility, multilingual, audit, GDPR, accessibility)
🇦🇪 تهيئة حزمة الأدلة للتجارة الإلكترونية (الأمان، التوسعة، متعدد اللغات، التدقيق، RGPD، الوصول)
ⵣ Tazwart n guides n tzemre (amatu, extensibility, multilingual, audit, RGPD, accessibility)
"""

# Import dynamique des guides (exemple)
import importlib
import logging

MODULES = [
    'ACCESSIBILITY_GUIDE', 'PLUGINS_GUIDE', 'SECURITY_GUIDE', 'RGPD_GUIDE', 'TEST_STRATEGY'
]
for mod in MODULES:
    try:
        importlib.import_module(f'.{mod}', __name__)
    except Exception as e:
        logging.warning(f"Guide {mod} non importé: {e}")

logging.getLogger(__name__).info("Guides eCommerce initialisés (Dihya)")
