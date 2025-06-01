"""
Initialisation avancée du module ops Dihya Coding.
Centralise les imports critiques : audit, plugins, i18n, services, validators.
Expose les hooks, blueprints, extensions, documentation, multitenancy, sécurité, RGPD, accessibilité, CI/CD.
"""
from .audit import log_ops_audit
from .plugins import OpsPluginBase
from .i18n import I18N_MESSAGES
from .services import perform_ops
from .validators import validate_ops_config

__all__ = [
    "log_ops_audit",
    "OpsPluginBase",
    "I18N_MESSAGES",
    "perform_ops",
    "validate_ops_config"
]
