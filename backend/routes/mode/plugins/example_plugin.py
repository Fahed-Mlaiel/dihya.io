"""
Exemple de plugin Mode : RGPD, i18n, audit, fallback IA, etc.
"""
from .base import ModePluginBase

class ExampleModePlugin(ModePluginBase):
    name = "example"
    description = "Plugin d'exemple pour Mode."
    version = "1.0.0"
    author = "Dihya Team"

    def process(self, data):
        # Traitement RGPD, i18n, fallback IA, etc.
        data['example'] = 'ok'
        return data
