"""
Initialisation avancée du module monitoring Dihya Coding.
Centralise les imports critiques : audit, plugins, i18n, services, validators.
Expose les hooks, blueprints, extensions, documentation, multitenancy, sécurité, RGPD, accessibilité, CI/CD.
"""
from .audit import log_monitoring_audit
from .plugins import MonitoringPluginBase
from .i18n import I18N_MESSAGES
from .services import perform_monitoring
from .validators import validate_monitoring_config

__all__ = [
    "log_monitoring_audit",
    "MonitoringPluginBase",
    "I18N_MESSAGES",
    "perform_monitoring",
    "validate_monitoring_config"
]
