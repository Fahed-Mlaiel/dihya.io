"""
Initialisation avancée du module ecommerce.
- Import explicite des sous-modules critiques (schemas, plugins, validators, audit, i18n, services, tests)
- Prêt pour l’extensibilité, la CI/CD, la documentation automatique
"""
from . import schemas, plugins, validators, audit, i18n, services
__all__ = [
    "schemas", "plugins", "validators", "audit", "i18n", "services"
]
