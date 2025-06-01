"""
Gestion des plugins pour les scripts de performance Dihya Coding.
- Extensibilité, hooks, sécurité, RGPD, accessibilité, multilingue.
"""
class PerformancePluginBase:
    def before_benchmark(self, context):
        pass
    def after_benchmark(self, context):
        pass
