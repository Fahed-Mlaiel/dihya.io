"""
Gestion des plugins pour les scripts de monitoring Dihya Coding.
- Extensibilité, hooks, sécurité, RGPD, accessibilité, multilingue.
"""
class MonitoringPluginBase:
    def before_monitoring(self, context):
        pass
    def after_monitoring(self, context):
        pass
