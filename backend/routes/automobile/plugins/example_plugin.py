"""
Exemple de plugin Automobile : RGPD, i18n, audit, fallback IA, etc.
"""
from .base import AutomobilePluginBase

class ExampleAutomobilePlugin(AutomobilePluginBase):
    name = "example"
    description = "Plugin d'exemple pour Automobile."
    version = "1.0.0"
    author = "Dihya Team"

    def process(self, data):
        # Traitement RGPD, i18n, fallback IA, etc.
        data['example'] = 'ok'
        return data
