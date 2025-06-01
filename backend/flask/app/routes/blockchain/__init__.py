"""
Initialisation avancée du module blockchain.
- Import explicite des sous-modules critiques (schemas, plugins, validators, audit, i18n, services, tests)
- Auto-discovery possible pour plugins/audit
- Prêt pour l’extensibilité, la CI/CD, la documentation automatique
"""
from . import schemas, plugins, validators, audit, i18n, services
# Optionnel : auto-registration de plugins/audit
# from .plugins import seo_plugin, accessibility_plugin, rgpd_plugin, audit_plugin
# from .audit import log_audit
# from .services import *

__all__ = [
    "schemas", "plugins", "validators", "audit", "i18n", "services"
]
