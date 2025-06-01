"""
Exemple de plugin Gamer : RGPD, i18n, audit, fallback IA, etc.
"""
from .base import GamerPluginBase

class ExampleGamerPlugin(GamerPluginBase):
    name = "example"
    description = "Plugin d'exemple pour Gamer."
    version = "1.0.0"
    author = "Dihya Team"

    def process(self, data):
        # Traitement RGPD, i18n, fallback IA, etc.
        data['example'] = 'ok'
        return data
