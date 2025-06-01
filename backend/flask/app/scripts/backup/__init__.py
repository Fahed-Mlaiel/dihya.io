"""
Initialisation avancée du module backup Dihya Coding.
Centralise les imports critiques : audit, plugins, i18n, services, validators.
Expose les hooks, blueprints, extensions, documentation, multitenancy, sécurité, RGPD, accessibilité, CI/CD.
"""
from .audit import log_backup_audit
from .plugins import BackupPluginBase
from .i18n import I18N_MESSAGES
from .services import perform_backup, restore_backup
from .validators import validate_backup_config

__all__ = [
    "log_backup_audit",
    "BackupPluginBase",
    "I18N_MESSAGES",
    "perform_backup",
    "restore_backup",
    "validate_backup_config"
]
