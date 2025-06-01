"""
Initialisation avancée du module RGPD Dihya Coding.
Centralise les imports critiques : audit, plugins, i18n, services, validators.
Expose les hooks, blueprints, extensions, documentation, multitenancy, sécurité, RGPD, accessibilité, CI/CD.
"""
from .audit import log_rgpd_audit
from .plugins import RgpdPluginBase
from .i18n import I18N_MESSAGES
from .services import anonymize_data, purge_rgpd_data
from .validators import validate_rgpd_config

__all__ = [
    "log_rgpd_audit",
    "RgpdPluginBase",
    "I18N_MESSAGES",
    "anonymize_data",
    "purge_rgpd_data",
    "validate_rgpd_config"
]
