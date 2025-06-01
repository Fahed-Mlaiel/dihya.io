"""
Initialisation avancée du module seed Dihya Coding.
Centralise les imports critiques : audit, plugins, i18n, services, validators.
Expose les hooks, blueprints, extensions, documentation, multitenancy, sécurité, RGPD, accessibilité, CI/CD.
"""
from .audit import log_seed_audit
from .plugins import SeedPluginBase
from .i18n import I18N_MESSAGES
from .services import seed_data, generate_demo_data
from .validators import validate_seed_config

__all__ = [
    "log_seed_audit",
    "SeedPluginBase",
    "I18N_MESSAGES",
    "seed_data",
    "generate_demo_data",
    "validate_seed_config"
]
