"""
Initialisation avancée du module maintenance Dihya Coding.

Centralise les imports critiques : audit, plugins, i18n, services, validators.
Expose les hooks, blueprints, extensions, documentation, multitenancy, sécurité, RGPD, accessibilité, CI/CD.
"""

from .audit import log_maintenance_audit
from .plugins import MaintenancePluginBase
from .i18n import I18N_MESSAGES
from .services import perform_maintenance
from .validators import validate_maintenance_config

__all__ = [
    "log_maintenance_audit",
    "MaintenancePluginBase",
    "I18N_MESSAGES",
    "perform_maintenance",
    "validate_maintenance_config"
]
