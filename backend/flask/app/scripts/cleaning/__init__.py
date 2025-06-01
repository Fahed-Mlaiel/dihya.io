"""
Initialisation avancée du module cleaning Dihya Coding.
Centralise les imports critiques : audit, plugins, i18n, services, validators.
Expose les hooks, blueprints, extensions, documentation, multitenancy, sécurité, RGPD, accessibilité, CI/CD.
"""
from .audit import log_cleaning_audit
from .plugins import CleaningPluginBase
from .i18n import I18N_MESSAGES
from .services import perform_cleaning
from .validators import validate_cleaning_config

__all__ = [
    "log_cleaning_audit",
    "CleaningPluginBase",
    "I18N_MESSAGES",
    "perform_cleaning",
    "validate_cleaning_config"
]
