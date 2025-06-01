"""
Exemple de plugin Manufacturing : RGPD, i18n, audit, fallback IA, etc.
"""
from .base import ManufacturingPluginBase

class ExampleManufacturingPlugin(ManufacturingPluginBase):
    name = "example"
    description = "Plugin d'exemple pour Manufacturing."
    version = "1.0.0"
    author = "Dihya Team"

    def process(self, data):
        # Traitement RGPD, i18n, fallback IA, etc.
        data['example'] = 'ok'
        return data
