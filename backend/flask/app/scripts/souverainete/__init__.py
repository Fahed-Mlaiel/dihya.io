"""
Initialisation avancée du module souveraineté Dihya Coding.
Centralise les imports critiques : audit, plugins, i18n, services, validators.
Expose les hooks, blueprints, extensions, documentation, multitenancy, sécurité, RGPD, accessibilité, CI/CD.
"""
from .audit import log_souverainete_audit
from .plugins import SouverainetePluginBase
from .i18n import I18N_MESSAGES
from .services import anonymize_data, export_data, import_data
from .validators import validate_souverainete_config

__all__ = [
    "log_souverainete_audit",
    "SouverainetePluginBase",
    "I18N_MESSAGES",
    "anonymize_data",
    "export_data",
    "import_data",
    "validate_souverainete_config"
]
