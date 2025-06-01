"""
Initialisation avancée du module beaute.
- Import explicite des sous-modules critiques (schemas, plugins, validators, audit, i18n, services, tests)
- Prêt pour l’extensibilité, la CI/CD, la documentation automatique
"""
from . import schemas, plugins, validators, audit, i18n, services
__all__ = [
    "schemas", "plugins", "validators", "audit", "i18n", "services"
]

"""
Blueprint-Export für Beaute (Kompatibilität für Integrationstests)
"""
try:
    from backend.flask.app.templates.beaute import blueprint
except ImportError:
    blueprint = None
