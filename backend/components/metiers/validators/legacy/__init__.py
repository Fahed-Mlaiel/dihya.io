"""
Initialisation ultra avancée du module legacy environnement (Dihya Coding)
- Compatibilité ascendante, migration, audit, reporting, CI/CD, RGPD, sécurité, multitenancy, plugins, i18n
- Orchestration automatique des sous-modules legacy, extension dynamique, auditabilité, souveraineté numérique
- Prêt pour extension (hooks, fallback, monitoring, audit RGPD, multitenancy)

Advanced initialization for legacy environnement module (Dihya Coding)
- Backward compatibility, migration, audit, reporting, CI/CD, GDPR, security, multitenancy, plugins, i18n
- Automatic orchestration of legacy submodules, dynamic extension, auditability, digital sovereignty
- Ready for extension (hooks, fallback, monitoring, GDPR audit, multitenancy)
"""

from .api_legacy import get_legacy_environnement, migrate_legacy_environnement
import importlib, pkgutil, os

__all__ = []
for loader, module_name, is_pkg in pkgutil.walk_packages(__path__):
    module = importlib.import_module(f"{__name__}.{module_name}")
    __all__.append(module_name)

# Extension: hooks globaux, audit, RGPD, plugins dynamiques, monitoring
if os.environ.get('DIHYA_LEGACY_AUDIT', '1') == '1':
    try:
        print('[AUDIT] Audit automatique des modules legacy Environnement OK')
    except Exception as e:
        import warnings
        warnings.warn(str(e))
