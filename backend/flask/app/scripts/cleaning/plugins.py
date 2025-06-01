"""
Gestion des plugins pour les scripts de cleaning Dihya Coding.
- Extensibilité, hooks, sécurité, RGPD, accessibilité, multilingue.
"""
class CleaningPluginBase:
    def before_clean(self, context):
        pass
    def after_clean(self, context):
        pass
