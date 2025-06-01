"""
Gestion des plugins pour les scripts RGPD Dihya Coding.
- Extensibilité, hooks, sécurité, RGPD, accessibilité, multilingue.
"""
class RgpdPluginBase:
    def before_rgpd(self, context):
        pass
    def after_rgpd(self, context):
        pass
