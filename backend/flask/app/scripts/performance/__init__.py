"""
Initialisation avancée du module performance Dihya Coding.
Centralise les imports critiques : audit, plugins, i18n, services, validators.
Expose les hooks, blueprints, extensions, documentation, multitenancy, sécurité, RGPD, accessibilité, CI/CD.
"""
from .audit import log_performance_audit
from .plugins import PerformancePluginBase
from .i18n import I18N_MESSAGES
from .services import run_benchmark, run_stress_test
from .validators import validate_performance_config

__all__ = [
    "log_performance_audit",
    "PerformancePluginBase",
    "I18N_MESSAGES",
    "run_benchmark",
    "run_stress_test",
    "validate_performance_config"
]
