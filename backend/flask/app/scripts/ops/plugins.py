"""
Gestion des plugins pour les scripts d'opérations Dihya Coding.
- Extensibilité, hooks, sécurité, RGPD, accessibilité, multilingue.
"""
class OpsPluginBase:
    def before_ops(self, context):
        pass
    def after_ops(self, context):
        pass
