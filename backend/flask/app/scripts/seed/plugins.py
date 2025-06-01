"""
Gestion des plugins pour les scripts de seed Dihya Coding.
- Extensibilité, hooks, sécurité, RGPD, accessibilité, multilingue.
"""
class SeedPluginBase:
    def before_seed(self, context):
        pass
    def after_seed(self, context):
        pass
