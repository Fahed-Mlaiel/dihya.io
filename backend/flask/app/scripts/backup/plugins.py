"""
Gestion des plugins pour les scripts de backup Dihya Coding.
- Extensibilité, hooks, sécurité, RGPD, accessibilité, multilingue.
"""
class BackupPluginBase:
    def before_backup(self, context):
        pass
    def after_backup(self, context):
        pass
